# CHEMOFILTER — MASTER IMPLEMENTATION PROMPT
### For: Gemini 2.5 Pro | Target Files: data_engine.py · api_manager.py · terminology.py · ui_upgrade.py

---

## WHO YOU ARE & WHAT YOU'RE DOING

You are a senior computational chemistry software architect upgrading a production-grade Streamlit drug discovery platform called **ChemoFilter**. The platform computes 380+ molecular features per compound (physicochemical, structural, ADMET, toxicity, efficiency metrics) from SMILES strings using RDKit, then surfaces them via a scientific UI.

You have been given **four Python files** to upgrade simultaneously. Each upgrade must be **surgical — never delete existing logic, never rename variables unless instructed, never break working imports**. Your only job is to insert, replace, and inject the improvements described below into the correct locations of each file.

---

## THE FOUR FILES — WHAT THEY DO, WHERE THEY LIVE

| File | Role | Critical Class/Function |
|---|---|---|
| `data_engine.py` | Computes 380-column feature vectors, persists to Parquet | `store_batch()`, `compute_feature_vector()`, `_rebuild_index()` |
| `api_manager.py` | Orchestrates 14 external API calls (PubChem, ChEMBL, etc.) | `_safe_get()`, `_safe_post()`, `fetch_api()` |
| `terminology.py` | Flat TERM dict → scientific display labels | `TERM{}`, `label()` function |
| `ui_upgrade.py` | Injects CSS design tokens, fonts, component styles | `inject_ui()`, `_inject_design_system()`, `_inject_component_library()` |

---

## UPGRADE 1 — `data_engine.py`

### Problem A: O(N²) Parquet Write in `store_batch()`

**WHERE:** Find the function `store_batch(rows: list[dict])` — around line 340 in the file.

**WHY IT'S BROKEN:** The current implementation calls `pd.read_parquet(COMPOUNDS_PATH, columns=["smiles"])` to load all existing SMILES for deduplication, then uses `fastparquet.write(..., append=True)`. But if `fastparquet` isn't installed, the WAL fallback writes a literal `"\\n"` string instead of a real newline. Also, `_rebuild_index()` is called on every single batch write — this is unnecessary and expensive.

**WHAT TO CHANGE:** Replace the entire `store_batch` function body with this:

```python
def store_batch(rows: list[dict]):
    """Store multiple rows — O(1) append mode with WAL fallback."""
    if not _df_available() or not rows:
        return
    try:
        # Deduplicate against in-memory index (never read full Parquet for this)
        global _SMILES_INDEX
        if not _INDEX_BUILT:
            _rebuild_index()

        filtered_rows = [r for r in rows if r.get("smiles") not in _SMILES_INDEX]
        if not filtered_rows:
            return

        df_new = pd.DataFrame(filtered_rows)

        if COMPOUNDS_PATH.exists():
            try:
                import fastparquet
                fastparquet.write(str(COMPOUNDS_PATH), df_new, append=True)
            except ImportError:
                # WAL fallback — correct newline, not escaped \\n
                import json
                wal_path = DATA_DIR / "compounds_wal.jsonl"
                with open(wal_path, "a", encoding="utf-8") as f:
                    for rv in filtered_rows:
                        f.write(json.dumps(rv) + "\n")  # real newline, not \\n
        else:
            df_new.to_parquet(COMPOUNDS_PATH, engine="pyarrow",
                              compression="snappy", index=False)

        # Update in-memory index incrementally — do NOT call _rebuild_index() here
        curr_len = len(_SMILES_INDEX)
        for i, row in enumerate(filtered_rows):
            smi = row.get("smiles", "")
            ik = row.get("inchikey", "")
            if smi:
                _SMILES_INDEX[smi] = curr_len + i
            if ik:
                _INCHI_INDEX[ik] = curr_len + i

    except Exception as e:
        import json
        wal_path = DATA_DIR / "compounds_wal.jsonl"
        try:
            with open(wal_path, "a", encoding="utf-8") as f:
                for rv in rows:
                    f.write(json.dumps(rv) + "\n")
        except Exception:
            pass
        print(f"[store_batch] Parquet write failed, flushed to WAL: {e}")
```

**WHY:** The old code called `_rebuild_index()` after every write — this reads the entire Parquet file on each batch. The new code updates `_SMILES_INDEX` and `_INCHI_INDEX` incrementally in-memory (O(1) per row). The WAL fallback is also fixed — the original had a Python escape `"\\n"` which wrote a literal backslash-n to the file instead of a newline character.

---

### Problem B: Session State Duplication in `compute_feature_vector()`

**WHERE:** Find the `@st.cache_data(max_entries=2000, ttl=3600, show_spinner=False)` decorator above `compute_feature_vector`.

**WHY IT'S A PROBLEM:** `@st.cache_data` already handles memoization. The function also writes to `_ROW_CACHE` (the internal dict) at the end. This means every computed vector is stored twice: once in Streamlit's cache layer, once in `_ROW_CACHE`. For 380-column dicts, this doubles memory consumption under heavy use.

**WHAT TO CHANGE:** At the very end of `compute_feature_vector`, find the lines:
```python
    _cache_put(ck, row)
    return row
```

Keep `_cache_put(ck, row)` — it serves the `get_compound_by_smiles()` fast-path. But add a guard so it only caches when `@st.cache_data` is NOT active (i.e., when called from non-Streamlit contexts). Replace with:

```python
    # Only populate local dict cache for non-Streamlit callers.
    # st.cache_data already handles memoization in the Streamlit context.
    if not _ST_OK:
        _cache_put(ck, row)
    return row
```

---

### Problem C: Add WAL Compaction Utility

**WHERE:** After the `_rebuild_index()` function, add this new function:

```python
def compact_wal_to_parquet():
    """
    Merge compounds_wal.jsonl into the main Parquet store.
    Call this at session end or via a scheduled trigger — never during hot path.
    """
    wal_path = DATA_DIR / "compounds_wal.jsonl"
    if not wal_path.exists() or not _df_available():
        return 0

    try:
        import json
        rows = []
        with open(wal_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    try:
                        rows.append(json.loads(line))
                    except json.JSONDecodeError:
                        continue

        if not rows:
            wal_path.unlink(missing_ok=True)
            return 0

        store_batch(rows)
        wal_path.unlink(missing_ok=True)
        return len(rows)
    except Exception as e:
        print(f"[compact_wal_to_parquet] Failed: {e}")
        return 0
```

**WHY:** When `fastparquet` is unavailable, rows pile up in `compounds_wal.jsonl`. Without a compaction step, this file grows forever. Call `compact_wal_to_parquet()` from `app.py` inside a `@st.cache_resource` block that runs once per session, or on a periodic basis.

---

## UPGRADE 2 — `api_manager.py`

### Problem A: Retry Logic is Structurally Incomplete

**WHERE:** Find `_safe_get()` and `_safe_post()`.

**WHY IT'S BROKEN:** The current exponential backoff in both functions only activates when `_RELIABILITY_OK` is False and falls through to the raw `requests` path. When `_RELIABILITY_OK` is True, the retry loop runs but `_reliability_get()` already handles one attempt internally — the outer loop just calls it up to 3 times without actually checking whether the request should be retried vs. permanently failed. There is also no jitter, meaning all concurrent callers retry at the same timestamp under load.

**WHAT TO CHANGE:** Replace both `_safe_get` and `_safe_post` with these versions:

```python
def _safe_get(url: str, params: dict | None = None,
              timeout: int = _TIMEOUT_DEFAULT, max_retries: int = 3) -> tuple:
    """
    Returns (response_json_or_None, error_string_or_None).
    Exponential backoff with jitter. Works with or without reliability layer.
    """
    import time, random
    last_err = "No attempts made"

    for attempt in range(max_retries):
        try:
            if _RELIABILITY_OK:
                import urllib.parse as _up
                full = url + ("?" + _up.urlencode(params) if params else "")
                result = _reliability_get(full, timeout=timeout, source="http")
                if result.get("status") == "success":
                    return result.get("data", {}), None
                last_err = result.get("error", "reliability layer failed")
            else:
                if not _REQ_OK:
                    return None, "requests library not available"
                r = _req.get(url, params=params, timeout=timeout)
                r.raise_for_status()
                return r.json(), None
        except Exception as e:
            last_err = str(e)[:150]

        if attempt < max_retries - 1:
            # Jittered backoff: base 2^attempt seconds ± 0–500ms
            sleep_time = (2 ** attempt) + random.uniform(0, 0.5)
            time.sleep(sleep_time)

    return None, last_err


def _safe_post(url: str, json_body: dict,
               timeout: int = _TIMEOUT_DEFAULT, max_retries: int = 3) -> tuple:
    """
    Returns (response_json_or_None, error_string_or_None).
    Exponential backoff with jitter. Works with or without reliability layer.
    """
    import time, random
    last_err = "No attempts made"

    for attempt in range(max_retries):
        try:
            if _RELIABILITY_OK:
                result = _reliability_post(url, json_body, timeout=timeout, source="http")
                if result.get("status") == "success":
                    return result.get("data", {}), None
                last_err = result.get("error", "reliability layer failed")
            else:
                if not _REQ_OK:
                    return None, "requests library not available"
                r = _req.post(url, json=json_body, timeout=timeout)
                r.raise_for_status()
                return r.json(), None
        except Exception as e:
            last_err = str(e)[:150]

        if attempt < max_retries - 1:
            sleep_time = (2 ** attempt) + random.uniform(0, 0.5)
            time.sleep(sleep_time)

    return None, last_err
```

**WHY:** Jitter (`random.uniform(0, 0.5)`) prevents the "thundering herd" problem where all concurrent requests retry at the exact same moment. `last_err` is now tracked across all attempts so the final error is meaningful, not silently dropped.

---

### Problem B: `fetch_api()` Caches Failed Results to Session State

**WHERE:** Find `fetch_api()`, specifically the line:
```python
    store_result(api_key, cache_key_str, result)
```

**WHY IT'S BROKEN:** `store_result()` writes to `st.session_state`. Failed results (`status: "failed"`) are also being cached there. This means if an API times out once, every subsequent call in that session returns the stale failure without retrying.

**WHAT TO CHANGE:** Replace that single line with:
```python
    # Only persist successful results to session state cache
    if result.get("status") in ("ok", "success"):
        store_result(api_key, cache_key_str, result)
```

---

### Problem C: Add SHA-256 Request Deduplication for Identical Payloads

**WHERE:** Add this utility function immediately before `_FETCH_DISPATCH`:

```python
def _payload_hash(endpoint: str, payload: dict) -> str:
    """
    Deterministic SHA-256 fingerprint for a (endpoint, payload) pair.
    Used to detect duplicate API calls that can be served from disk cache.
    """
    canonical = f"{endpoint}::{sorted(payload.items()) if payload else ''}"
    return hashlib.sha256(canonical.encode()).hexdigest()[:16]
```

Then in `fetch_api()`, before the dispatch call, add:
```python
    # Deduplicate: if the same logical request was already completed this session
    dedup_key = _payload_hash(api_key, {"smiles": smiles, "query": query, **kwargs})
    if dedup_key in st.session_state:
        cached_dedup = st.session_state[dedup_key]
        if cached_dedup.get("status") in ("ok", "success"):
            return cached_dedup
```

And after a successful result, store it:
```python
    if result.get("status") in ("ok", "success"):
        st.session_state[dedup_key] = result
```

**WHY:** Two different UI components can independently call `fetch_api("pubchem", smiles=same_smiles)`. Without this, both trigger separate HTTP requests. The SHA-256 dedup key ensures the second call returns instantly from session memory.

---

## UPGRADE 3 — `terminology.py`

### Problem: Flat TERM Dict Cannot Categorize, Cannot Be Extended Without Conflict

**WHERE:** The file currently has a single top-level dict called `TERM`. It has a `label()` and `tooltip()` function at the bottom.

**WHAT TO ADD:** Immediately after the existing `TERM = { ... }` dict closes (after the last `}` on its final entry), insert this **additive block** — do not remove or modify `TERM`:

```python
# ═════════════════════════════════════════════════════════════════════════════
# SCIENTIFIC REGISTRY — Categorical extension of TERM
# Replaces all "AI / Engine / Smart" nomenclature with research-grade identifiers
# Query order: SCIENTIFIC_REGISTRY → TERM (legacy fallback)
# ═════════════════════════════════════════════════════════════════════════════

SCIENTIFIC_REGISTRY: dict[str, dict[str, tuple[str, str]]] = {
    "Physicochemical": {
        "mw":           ("Molecular Weight (MW)", "Total molecular mass in Daltons (Da)."),
        "logp":         ("Lipophilicity (LogP)", "Octanol-water partition coefficient. Ideal range: -0.4 to 5.6."),
        "tpsa":         ("Topological Polar Surface Area (TPSA)", "Sum of polar atom surface areas. Oral absorption limit: ≤140 Ų."),
        "hbd":          ("Hydrogen Bond Donors (HBD)", "Count of N–H and O–H groups. Lipinski limit: ≤5."),
        "hba":          ("Hydrogen Bond Acceptors (HBA)", "Count of N and O atoms. Lipinski limit: ≤10."),
        "fsp3":         ("Fraction sp³ Carbons (Fsp3)", "Proportion of saturated carbons. >0.4 improves aqueous solubility."),
        "qed":          ("Drug-Likeness Score (QED)", "Quantitative Estimate of Drug-likeness (0–1). >0.6 is drug-like."),
        "log_s_esol":   ("ESOL Aqueous Solubility (logS)", "Predicted aqueous solubility via ESOL model. logS > -4 is acceptable."),
        "rotatable_bonds": ("Rotatable Bond Count", "Single bonds permitting free rotation. >10 reduces oral bioavailability."),
    },
    "Structural_Alerts": {
        "pains_count":       ("PAINS Structural Alert Count", "Pan-Assay Interference Compound alerts — predicts assay false positives."),
        "brenk_count":       ("Brenk Structural Alert Count", "Toxicophore and metabolic liability alert count (Brenk filter)."),
        "total_alert_count": ("Total Structural Alert Count", "Aggregate of all PAINS, Brenk, and NIH structural alerts."),
        "ames_mutagenicity": ("Ames Mutagenicity Prediction", "Predicted bacterial mutagenicity. Indicates potential genotoxicity."),
        "dili_risk":         ("Drug-Induced Liver Injury Risk (DILI)", "Predicted hepatotoxic liability based on physicochemical surrogates."),
        "herg_risk":         ("hERG Cardiac Liability", "Predicted hERG potassium channel blockade risk. HIGH = potential QT prolongation."),
        "toxicophore_count": ("Toxicophore Fragment Count", "Number of reactive chemical groups known to cause toxicity."),
    },
    "SAR_Inference": {
        # All 'AI / Engine / Smart' terms are remapped here
        "ai_explainer":              ("Mechanistic SAR Derivation Profiler",
                                      "Structure-Activity Relationship inference engine. Derives mechanism from structural features."),
        "engine_agreement_score":    ("Algorithmic Consensus Metric",
                                      "Normalized agreement score across independent statistical ensemble models."),
        "engine_count":              ("Active Predictive Modalities",
                                      "Number of independent ensemble nodes contributing to the consensus prediction."),
        "engine_divergence_score":   ("Inter-Model Divergence Score",
                                      "Normalized standard deviation across ensemble model outputs. High = unstable prediction."),
        "universal_analysis":        ("Universal Pharmacophore Profiling Suite",
                                      "High-throughput physicochemical and pharmacophoric filtering pipeline."),
        "smart_filter":              ("Adaptive Structural Exclusion Filter",
                                      "Context-aware chemical space filter using substructure and physicochemical constraints."),
        "ai_score":                  ("Ensemble Predictive Confidence Score",
                                      "Aggregated statistical confidence of multi-model consensus prediction."),
    },
    "Efficiency_Metrics": {
        "ligand_efficiency":     ("Ligand Efficiency (LE)", "Binding energy per heavy atom. Optimal scaffold optimisation guide."),
        "lipophilic_efficiency": ("Lipophilic Ligand Efficiency (LLE)", "pIC50 minus LogP. LLE > 5 is excellent."),
        "lead_score":            ("Lead Optimisation Score", "Composite decision score (0–100) integrating ADMET, safety, and drug-likeness."),
        "drug_likeness_score":   ("Drug-Likeness Composite Score", "Fraction of Lipinski/Veber/Ghose/Egan/Muegge rules passed (0–1)."),
        "synthetic_accessibility": ("Synthetic Accessibility Index", "Estimated synthetic difficulty (1=trivial, 10=impractical)."),
        "optimization_score":    ("Multi-Parameter Optimisation Score (MPO)", "Weighted composite of LE, drug-likeness, and alert-free structure."),
    },
}


def label(key: str) -> str:
    """
    Safe label lookup. Priority: SCIENTIFIC_REGISTRY → TERM legacy fallback.
    Always returns a human-readable string. Never raises.
    """
    k = key.lower().replace(" ", "_").replace("-", "_")

    # 1. Search categorical registry first
    for _cat, term_map in SCIENTIFIC_REGISTRY.items():
        if k in term_map:
            return term_map[k][0]

    # 2. Legacy TERM fallback
    if k in TERM:
        return TERM[k][0]

    # 3. Graceful degradation
    return key.replace("_", " ").title()


def tooltip(key: str) -> str:
    """
    Safe tooltip lookup. Priority: SCIENTIFIC_REGISTRY → TERM legacy fallback.
    Always returns a string. Never raises.
    """
    k = key.lower().replace(" ", "_").replace("-", "_")

    for _cat, term_map in SCIENTIFIC_REGISTRY.items():
        if k in term_map:
            return term_map[k][1]

    if k in TERM:
        return TERM[k][1]

    return f"No definition available for '{key}'."


def category(key: str) -> str:
    """Return the registry category for a key, or 'General' if not found."""
    k = key.lower().replace(" ", "_").replace("-", "_")
    for cat, term_map in SCIENTIFIC_REGISTRY.items():
        if k in term_map:
            return cat
    return "General"
```

**WHY:** The flat `TERM` dict cannot support categorized iteration (e.g., "show me all Structural_Alert labels"). The `SCIENTIFIC_REGISTRY` adds this while the dual-fallback `label()` function maintains full backward compatibility — nothing that currently calls `label(key)` will break.

**CRITICAL:** Do NOT remove the existing `TERM` dict or any existing `label()`/`tooltip()` functions. If those already exist at the bottom of the file, **replace only the function bodies** with the new dual-lookup logic above. If they don't exist, add the whole block.

---

## UPGRADE 4 — `ui_upgrade.py`

### Problem A: Missing Skeleton Loader and Data-State Transition CSS

**WHERE:** Find `_inject_component_library()`. Inside it, there is a `st.markdown("""<style>...</style>""", ...)` call. **Append the following CSS inside that existing `<style>` block**, before the closing `</style>` tag.

**DO NOT** create a new `st.markdown` call — find the existing one and append inside it.

```css
/* ════════════════════════════════════════════════════════════════════
   DATA-STATE TRANSITION SYSTEM — Non-blocking UI feedback layer
   ════════════════════════════════════════════════════════════════════ */

/* 1. SKELETON LOADER — rendered while data_engine is computing */
.skeleton-data {
  background: linear-gradient(
    90deg,
    var(--n-bg2) 25%,
    var(--n-bg3) 50%,
    var(--n-bg2) 75%
  );
  background-size: 400% 100%;
  animation: skelPulse 1.2s ease-in-out infinite;
  border-radius: var(--n-r3);
  pointer-events: none;
  opacity: 0.7;
  min-height: 36px;
}

.skeleton-box {
  background: linear-gradient(
    90deg,
    var(--n-bg2) 25%,
    var(--n-bg3) 50%,
    var(--n-bg2) 75%
  );
  background-size: 400% 100%;
  animation: skelPulse 1.5s ease-in-out infinite;
  border-radius: var(--n-r2);
  min-height: 40px;
}

@keyframes skelPulse {
  0%   { background-position: 200% 0; }
  100% { background-position: -200% 0; }
}

/* 2. PROGRESSIVE REVEAL — data replaces skeleton */
.data-ready {
  animation: smoothReveal 0.4s cubic-bezier(0.2, 0.8, 0.2, 1) forwards;
}

.data-loaded {
  animation: dataReveal 0.4s cubic-bezier(0.2, 0.8, 0.2, 1) forwards;
}

@keyframes smoothReveal {
  from { opacity: 0.2; transform: translateY(4px) scale(0.99); }
  to   { opacity: 1;   transform: translateY(0)   scale(1);    }
}

@keyframes dataReveal {
  from { opacity: 0; transform: translateY(4px); }
  to   { opacity: 1; transform: translateY(0);   }
}

/* 3. VALUE UPDATE HIGHLIGHT — teal flash when a metric changes */
.value-updated {
  animation: valueFlash 0.8s ease-out forwards;
}

@keyframes valueFlash {
  0%   { background: rgba(0, 210, 190, 0.18); border-radius: var(--n-r3); }
  100% { background: transparent; }
}

/* 4. INLINE ERROR STATE */
.sci-alert {
  border-left: 2px solid var(--n-red);
  background: var(--n-red-bg);
  padding: var(--space-3) var(--space-4);
  font-family: var(--n-font-mono);
  font-size: 0.72rem;
  color: var(--n-tx2);
  animation: smoothReveal 0.3s ease-out;
  border-radius: 0 var(--n-r3) var(--n-r3) 0;
}

/* 5. CARD HOVER DEPTH */
.card {
  padding: var(--space-6);
  border-radius: var(--n-r2);
  box-shadow: var(--shadow-flat);
  transition: all 0.3s cubic-bezier(0.2, 0.8, 0.2, 1);
  background: var(--n-bg2);
  border: 1px solid var(--n-bdr2);
}

.card:hover {
  transform: translateY(-2px);
  box-shadow: var(--shadow-hover);
  border-color: var(--n-teal-bdr);
}
```

---

### Problem B: Missing Typography Hierarchy Tokens in `_inject_design_system()`

**WHERE:** Find `:root { ... }` inside `_inject_design_system()`. Inside that block, after the last variable declaration and before the closing `}`, append:

```css
  /* Extended Typography Scale */
  --n-font-h1: 800 24px/1.2 'Syne', sans-serif;
  --n-font-h2: 700 18px/1.3 'Syne', sans-serif;
  --n-font-h3: 600 14px/1.4 'Syne', sans-serif;
  --n-font-lbl: 600 11px/1.5 'JetBrains Mono', monospace;
  --n-font-data: 500 13px/1.4 'JetBrains Mono', monospace;
  --n-font-body-sm: 400 12px/1.6 'Inter', sans-serif;

  /* Extended Shadow Scale */
  --shadow-low:    0 2px 4px rgba(0, 210, 190, 0.05);
  --shadow-med:    0 8px 16px rgba(0, 210, 190, 0.10);
  --shadow-high:   0 16px 32px rgba(0, 0, 0, 0.80), 0 0 20px rgba(0, 210, 190, 0.15);
  --shadow-float:  0 16px 32px rgba(0, 0, 0, 0.60), 0 0 0 1px var(--n-teal-bdr);
```

**WHY:** The existing `:root` already has `--shadow-flat`, `--shadow-hover`, `--shadow-premium`. These additions extend the depth system to include `--shadow-low/med/high/float` and a complete font-shorthand system, enabling semantic font assignment without repeating full `font-family/weight/size` declarations everywhere.

---

## EXECUTION RULES — READ BEFORE WRITING A SINGLE LINE

1. **Never delete existing working code.** If the instruction says "replace", replace only the specific function body or block described. Keep all surrounding code intact.

2. **Surgical insertion only.** Each change is localized to a named function or block. You are not refactoring the whole file — you are inserting specific improvements.

3. **Preserve all imports.** Do not add imports at the top that are already imported. Do not remove any existing imports.

4. **`fastparquet` is optional.** Always wrap `import fastparquet` in a `try/except ImportError` block. The WAL fallback is the safety net.

5. **The `TERM` dict in `terminology.py` must not be touched.** `SCIENTIFIC_REGISTRY` is additive. The new `label()` and `tooltip()` functions are replacements for the function bodies only — not the data.

6. **CSS goes inside existing `<style>` blocks.** Never create a new `st.markdown("<style>...</style>")` call when one already exists in the same function. Find it and append inside.

7. **Test for import failures gracefully.** Every external lib (`fastparquet`, `requests`, `rdkit`) already has try/except guards in the file. Respect that pattern.

8. **Return all four complete files** after applying changes — not just diffs.

---

## VALIDATION CHECKLIST (run mentally before responding)

- [ ] `store_batch()` uses `_SMILES_INDEX` for dedup, never reads full Parquet, updates index incrementally
- [ ] WAL fallback writes real `"\n"` (not `"\\n"`)  
- [ ] `compact_wal_to_parquet()` exists and merges JSONL → Parquet safely
- [ ] `compute_feature_vector()` only writes to `_ROW_CACHE` when `_ST_OK` is False
- [ ] `_safe_get()` and `_safe_post()` have jittered backoff using `random.uniform(0, 0.5)`
- [ ] `fetch_api()` only caches `status == "ok"` results to session state
- [ ] `_payload_hash()` exists before `_FETCH_DISPATCH`
- [ ] `SCIENTIFIC_REGISTRY` is present in `terminology.py` and does not overwrite `TERM`
- [ ] `label()` checks `SCIENTIFIC_REGISTRY` first, then `TERM`, then graceful degradation
- [ ] `tooltip()` and `category()` functions exist alongside `label()`
- [ ] Skeleton CSS classes (`.skeleton-data`, `.skeleton-box`, `.data-ready`, `.data-loaded`, `.value-updated`, `.sci-alert`, `.card`) exist in `ui_upgrade.py`
- [ ] Extended `:root` tokens (`--shadow-low/med/high/float`, `--n-font-h1/h2/h3/lbl`) are inside the existing `:root` block
- [ ] No existing logic deleted anywhere
- [ ] No new top-level imports added that weren't already present
