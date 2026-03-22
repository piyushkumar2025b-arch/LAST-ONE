"""
comparison_mode.py
────────────────────────────────────────────────────────────────────────────
ChemoFilter · Comparison Mode — Tab 37 (PHASE 3)
• Side-by-side property comparison of selected compounds
• Radar / spider chart for multi-property visualisation
• Delta table showing property differences
• Fully isolated — read-only access to res list
────────────────────────────────────────────────────────────────────────────
"""

import streamlit as st

try:
    import plotly.graph_objects as go
    _PLT_OK = True
except Exception:
    _PLT_OK = False

_COMPARE_PROPS = ["MW", "LogP", "tPSA", "QED", "SA_Score", "LeadScore", "OralBioScore"]
_RADAR_PROPS   = ["QED", "LeadScore", "OralBioScore"]


def _normalise(value, min_v, max_v) -> float:
    """Normalise value to 0–1."""
    try:
        v = float(value)
        span = max_v - min_v
        if span == 0:
            return 0.5
        return max(0.0, min(1.0, (v - min_v) / span))
    except Exception:
        return 0.0


def _radar_fig(compounds: list):
    if not _PLT_OK or not compounds:
        return None

    categories = ["QED×100", "LeadScore", "OralBioScore", "BBB(%)", "HIA(%)"]

    fig = go.Figure()
    colors = ["#f5a623", "#4ade80", "#38bdf8", "#a78bfa", "#fb923c"]

    for idx, cpd in enumerate(compounds):
        qed_val  = float(cpd.get("QED", cpd.get("_qed", 0.5))) * 100
        lead_val = float(cpd.get("LeadScore", 60))
        oral_val = float(cpd.get("OralBioScore", 60))
        bbb_val  = 80.0 if cpd.get("_bbb") else 20.0
        hia_val  = 80.0 if cpd.get("_hia") else 20.0

        r_vals = [qed_val, lead_val, oral_val, bbb_val, hia_val]

        fig.add_trace(go.Scatterpolar(
            r=r_vals + [r_vals[0]],
            theta=categories + [categories[0]],
            fill="toself",
            name=cpd.get("ID", f"Cpd-{idx+1}"),
            line_color=colors[idx % len(colors)],
            fillcolor=colors[idx % len(colors)].replace("#", "rgba(").rstrip(")") + ",0.08)"
            if colors[idx % len(colors)].startswith("#") else "rgba(245,166,35,0.08)",
        ))

    fig.update_layout(
        polar=dict(
            radialaxis=dict(visible=True, range=[0, 100], color="#c8deff"),
            angularaxis=dict(color="#c8deff"),
            bgcolor="rgba(0,0,0,0)",
        ),
        paper_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#c8deff", size=11),
        height=420,
        title="Multi-Property Radar",
    )
    return fig


def render_tab(res: list):
    """Render Comparison Mode tab."""
    st.markdown(
        '<div style="font-family:\'JetBrains Mono\',monospace;font-size:.6rem;'
        'letter-spacing:3px;color:rgba(232,160,32,.5);text-transform:uppercase;'
        'margin-bottom:12px">⬡ Comparison Mode — Side-by-Side Analysis</div>',
        unsafe_allow_html=True,
    )

    if not res:
        st.warning("No compounds loaded.")
        return

    # Compound selector
    ids = [c.get("ID", f"Cpd-{i+1}") for i, c in enumerate(res)]
    selected_ids = st.multiselect(
        "Select compounds to compare (2–5 recommended)",
        ids,
        default=ids[:min(3, len(ids))],
        key="_cmp_select",
    )

    if not selected_ids:
        st.info("Select at least one compound.")
        return

    selected = [c for c in res if c.get("ID", "") in selected_ids]

    # ── Radar chart ───────────────────────────────────────────────────────
    if _PLT_OK:
        fig = _radar_fig(selected)
        if fig:
            st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("Plotly not available — radar chart unavailable.")

    # ── Property table ────────────────────────────────────────────────────
    st.subheader("Property Comparison Table")

    # Header row
    header_cols = st.columns([2] + [1] * len(selected))
    header_cols[0].markdown("**Property**")
    for i, cpd in enumerate(selected):
        header_cols[i + 1].markdown(f"**{cpd.get('ID', f'Cpd-{i+1}')}**")

    # Data rows
    for prop in _COMPARE_PROPS:
        row = st.columns([2] + [1] * len(selected))
        row[0].write(prop)
        values = []
        for cpd in selected:
            v = cpd.get(prop, cpd.get(prop.lower(), "–"))
            values.append(v)
        # Highlight best/worst
        try:
            nums = [float(v) for v in values]
            best_i = nums.index(max(nums))
        except Exception:
            best_i = -1

        for i, (col, v) in enumerate(zip(row[1:], values)):
            if i == best_i and prop in ["QED", "LeadScore", "OralBioScore"]:
                col.markdown(f"🏆 **{v}**")
            else:
                col.write(v)

    # ── Delta matrix (first compound as reference) ────────────────────────
    if len(selected) >= 2:
        st.subheader(f"Δ Delta vs {selected[0].get('ID', 'Cpd-1')} (reference)")
        ref = selected[0]
        delta_cols = st.columns([2] + [1] * (len(selected) - 1))
        delta_cols[0].markdown("**Property**")
        for i, cpd in enumerate(selected[1:]):
            delta_cols[i + 1].markdown(f"**{cpd.get('ID', f'Cpd-{i+2}')}**")

        for prop in _COMPARE_PROPS:
            drow = st.columns([2] + [1] * (len(selected) - 1))
            drow[0].write(prop)
            ref_v = ref.get(prop, 0)
            for i, cpd in enumerate(selected[1:]):
                cpd_v = cpd.get(prop, 0)
                try:
                    delta = round(float(cpd_v) - float(ref_v), 2)
                    sign = "+" if delta > 0 else ""
                    color = "#4ade80" if delta >= 0 else "#f87171"
                    drow[i + 1].markdown(
                        f'<span style="color:{color};font-family:JetBrains Mono,monospace">'
                        f'{sign}{delta}</span>',
                        unsafe_allow_html=True,
                    )
                except Exception:
                    drow[i + 1].write("–")

    # NEW CODE START ──────────────────────────────────────────────────────
    # Advanced Comparison Insights — appended below existing table.
    # Nothing above this line has been modified.
    # ─────────────────────────────────────────────────────────────────────
    if len(selected) >= 2:
        _render_advanced_insights(selected)
    # NEW CODE END ────────────────────────────────────────────────────────


# =============================================================================
# NEW CODE START — Advanced Delta Engine & Intelligence Layers
# =============================================================================

# ── Safe optional imports ─────────────────────────────────────────────────
try:
    from rdkit import Chem as _Chem
    from rdkit.Chem import Descriptors as _Desc, rdMolDescriptors as _RDMol, Crippen as _Crippen
    _RDK_OK = True
except Exception:
    _RDK_OK = False

try:
    import admet_benchmark as _ab_mod
    _AB_MOD_OK = True
except Exception:
    _AB_MOD_OK = False

try:
    import reaction_simulator as _rs_mod
    _RS_MOD_OK = True
except Exception:
    _RS_MOD_OK = False


# ── Colour-coding helpers ─────────────────────────────────────────────────

def _delta_badge(value: float, higher_is_better: bool = True) -> str:
    if abs(value) < 0.001:
        return f'<span style="color:#94a3b8;font-family:JetBrains Mono,monospace">⚪ {value:+.2f}</span>'
    improved = (value > 0) == higher_is_better
    icon  = "🟢" if improved else "🔴"
    color = "#4ade80" if improved else "#f87171"
    return f'<span style="color:{color};font-family:JetBrains Mono,monospace">{icon} {value:+.2f}</span>'


def _text_badge(label: str, positive) -> str:
    if positive is True:
        return f'<span style="color:#4ade80">🟢 {label}</span>'
    if positive is False:
        return f'<span style="color:#f87171">🔴 {label}</span>'
    return f'<span style="color:#94a3b8">⚪ {label}</span>'


# ── Data-gathering helpers (lazy, read-only) ──────────────────────────────

def _get_rdkit_props(cpd: dict) -> dict:
    defaults = {
        "ring_count": 0, "aromatic_rings": 0,
        "heavy_atoms": 0, "chiral_centers": 0,
        "lipinski_violations": 0, "veber_ok": False,
    }
    if not _RDK_OK:
        return defaults
    smi = cpd.get("SMILES") or cpd.get("smi") or ""
    if not smi:
        return defaults
    try:
        mol = _Chem.MolFromSmiles(smi)
        if mol is None:
            return defaults
        mw   = _Desc.MolWt(mol)
        logp = _Crippen.MolLogP(mol)
        hbd  = _RDMol.CalcNumHBD(mol)
        hba  = _RDMol.CalcNumHBA(mol)
        tpsa = _Desc.TPSA(mol)
        rot  = _RDMol.CalcNumRotatableBonds(mol)
        viol = sum([mw > 500, logp > 5, hbd > 5, hba > 10])
        veber_ok = tpsa <= 140 and rot <= 10
        chiral = len(_Chem.FindMolChiralCenters(mol, includeUnassigned=True))
        return {
            "ring_count":          _RDMol.CalcNumRings(mol),
            "aromatic_rings":      _RDMol.CalcNumAromaticRings(mol),
            "heavy_atoms":         mol.GetNumHeavyAtoms(),
            "chiral_centers":      chiral,
            "lipinski_violations": viol,
            "veber_ok":            veber_ok,
        }
    except Exception:
        return defaults


def _get_metabolic_risk(cpd: dict) -> dict:
    defaults = {"metabolic_sites": 0, "phase1_vuln": "Unknown", "reactive_risk": "Unknown"}
    if not _RS_MOD_OK:
        return defaults
    smi = cpd.get("SMILES") or cpd.get("smi") or ""
    if not smi:
        return defaults
    try:
        hits = 0
        for rsmarts in _rs_mod._REACTIONS.values():
            if _rs_mod._apply_reaction(rsmarts, smi):
                hits += 1
        phase1  = "High" if hits >= 4 else "Medium" if hits >= 2 else "Low"
        reactive = "High" if hits >= 5 else "Medium" if hits >= 3 else "Low"
        return {"metabolic_sites": hits, "phase1_vuln": phase1, "reactive_risk": reactive}
    except Exception:
        return defaults


def _get_benchmark_score(cpd: dict) -> dict:
    defaults = {"drug_similarity": 50.0, "percentile_rank": 50.0, "outlier_score": 0.0}
    if not _AB_MOD_OK:
        return defaults
    try:
        ref  = _ab_mod._BENCHMARK_SETS["FDA Approved Drugs (n\u22482000)"]
        bm   = _ab_mod._benchmark_compound(cpd, ref)
        if not bm:
            return defaults
        pcts = [v["percentile"] for v in bm.values()]
        avg  = round(sum(pcts) / len(pcts), 1) if pcts else 50.0
        std  = (sum((p - avg) ** 2 for p in pcts) / max(len(pcts), 1)) ** 0.5
        return {"drug_similarity": avg, "percentile_rank": avg, "outlier_score": round(std, 1)}
    except Exception:
        return defaults


def _get_efficiency(cpd: dict) -> dict:
    try:
        qed  = float(cpd.get("QED", cpd.get("_qed", 0.5)))
        mw   = float(cpd.get("MW", 400))
        ha   = max(int(mw / 14), 1)
        le   = round((1.4 * qed * 100) / ha, 3)
        pd_  = round(qed / (mw / 100), 3) if mw > 0 else 0.0
        return {"ligand_efficiency": le, "property_density": pd_}
    except Exception:
        return {"ligand_efficiency": 0.0, "property_density": 0.0}


# ── Core advanced delta engine ────────────────────────────────────────────

def compute_advanced_deltas(r1: dict, r2: dict) -> dict:
    """
    Returns structured comparison insights without altering existing outputs.
    r1 = reference compound, r2 = compound being compared.
    """
    rdkit1  = _get_rdkit_props(r1)
    rdkit2  = _get_rdkit_props(r2)
    meta1   = _get_metabolic_risk(r1)
    meta2   = _get_metabolic_risk(r2)
    bench1  = _get_benchmark_score(r1)
    bench2  = _get_benchmark_score(r2)
    eff1    = _get_efficiency(r1)
    eff2    = _get_efficiency(r2)

    def _d(key, d1, d2, dec=2):
        try:
            return round(float(d2.get(key, 0)) - float(d1.get(key, 0)), dec)
        except Exception:
            return 0.0

    def _df(key, dec=2):
        try:
            return round(float(r2.get(key, 0)) - float(r1.get(key, 0)), dec)
        except Exception:
            return 0.0

    # 1. Drug-Likeness
    qed1 = float(r1.get("QED", r1.get("_qed", 0.5)))
    qed2 = float(r2.get("QED", r2.get("_qed", 0.5)))
    dqed = round(qed2 - qed1, 3)
    drug_likeness = {
        "delta_lipinski_violations": _d("lipinski_violations", rdkit1, rdkit2),
        "delta_veber_compliance":    int(rdkit2["veber_ok"]) - int(rdkit1["veber_ok"]),
        "delta_qed":                 dqed,
        "qed_direction":             "Improved" if dqed > 0.02 else "Worse" if dqed < -0.02 else "Neutral",
        "delta_sa_score":            _df("SA_Score"),
    }

    # 2. Risk
    tpsa1 = float(r1.get("tPSA", r1.get("TPSA", 90)))
    tpsa2 = float(r2.get("tPSA", r2.get("TPSA", 90)))
    logp1 = float(r1.get("LogP", 2.5))
    logp2 = float(r2.get("LogP", 2.5))
    mw1   = float(r1.get("MW", 400))
    mw2   = float(r2.get("MW", 400))
    tox1  = int(bool(r1.get("_pains"))) + (1 if r1.get("_herg") == "HIGH" else 0)
    tox2  = int(bool(r2.get("_pains"))) + (1 if r2.get("_herg") == "HIGH" else 0)
    risk = {
        "delta_solubility_risk":    round((logp2 * 0.5 + mw2 / 200) - (logp1 * 0.5 + mw1 / 200), 2),
        "delta_permeability_risk":  round(tpsa2 / 10 - tpsa1 / 10, 2),
        "delta_stability_proxy":    meta2["metabolic_sites"] - meta1["metabolic_sites"],
        "delta_toxicity_flags":     tox2 - tox1,
    }

    # 3. Structure
    structure = {
        "delta_ring_count":     rdkit2["ring_count"] - rdkit1["ring_count"],
        "delta_aromatic_rings": rdkit2["aromatic_rings"] - rdkit1["aromatic_rings"],
        "delta_heavy_atoms":    rdkit2["heavy_atoms"] - rdkit1["heavy_atoms"],
        "delta_chiral_centers": rdkit2["chiral_centers"] - rdkit1["chiral_centers"],
    }

    # 4. Engine consensus
    _ekeys  = ["LeadScore", "OralBioScore", "NP_Score", "ChemoScore"]
    scores1 = [float(r1[k]) for k in _ekeys if r1.get(k) is not None]
    scores2 = [float(r2[k]) for k in _ekeys if r2.get(k) is not None]

    def _var(vals):
        if len(vals) < 2:
            return 0.0
        m = sum(vals) / len(vals)
        return round(sum((v - m) ** 2 for v in vals) / len(vals), 2)

    agg1 = round(sum(scores1) / len(scores1), 2) if scores1 else 0.0
    agg2 = round(sum(scores2) / len(scores2), 2) if scores2 else 0.0
    var1 = _var(scores1)
    var2 = _var(scores2)
    engine = {
        "delta_engine_score":         round(agg2 - agg1, 2),
        "delta_agreement_score":      round(var2 - var1, 2),
        "delta_prediction_stability": round(var1 - var2, 2),
    }

    # 5. Metabolic
    _rmap = {"Low": 1, "Medium": 2, "High": 3, "Unknown": 0}
    metabolic = {
        "delta_metabolic_sites": meta2["metabolic_sites"] - meta1["metabolic_sites"],
        "delta_phase1_vuln":     _rmap.get(meta2["phase1_vuln"], 0) - _rmap.get(meta1["phase1_vuln"], 0),
        "phase1_r1":             meta1["phase1_vuln"],
        "phase1_r2":             meta2["phase1_vuln"],
        "delta_reactive_risk":   _rmap.get(meta2["reactive_risk"], 0) - _rmap.get(meta1["reactive_risk"], 0),
        "reactive_r1":           meta1["reactive_risk"],
        "reactive_r2":           meta2["reactive_risk"],
    }

    # 6. Benchmark
    benchmark = {
        "delta_drug_similarity": round(bench2["drug_similarity"] - bench1["drug_similarity"], 1),
        "delta_percentile_rank": round(bench2["percentile_rank"] - bench1["percentile_rank"], 1),
        "delta_outlier_score":   round(bench2["outlier_score"] - bench1["outlier_score"], 1),
        "pct_r1":                bench1["percentile_rank"],
        "pct_r2":                bench2["percentile_rank"],
    }

    # 7. Efficiency
    efficiency = {
        "delta_ligand_efficiency": round(eff2["ligand_efficiency"] - eff1["ligand_efficiency"], 3),
        "delta_property_density":  round(eff2["property_density"] - eff1["property_density"], 3),
        "le_r1": eff1["ligand_efficiency"],
        "le_r2": eff2["ligand_efficiency"],
    }

    # 8. Alerts
    new_violations = []
    if not r1.get("_pains") and r2.get("_pains"):
        new_violations.append("PAINS introduced")
    if r1.get("_herg") != "HIGH" and r2.get("_herg") == "HIGH":
        new_violations.append("hERG escalated to HIGH")
    if drug_likeness["delta_lipinski_violations"] > 0:
        new_violations.append(f"+{int(drug_likeness['delta_lipinski_violations'])} Lipinski violation(s)")
    if risk["delta_toxicity_flags"] > 0:
        new_violations.append(f"+{risk['delta_toxicity_flags']} tox flag(s)")
    alerts = {
        "new_violations":  new_violations,
        "risk_escalation": len(new_violations) > 0,
        "structural_alerts": (
            "Complexity increased" if structure["delta_heavy_atoms"] > 5
            else "Complexity reduced" if structure["delta_heavy_atoms"] < -5
            else "Complexity stable"
        ),
    }

    # 9. Decision
    abs_better  = int(tpsa2 < tpsa1 and logp2 < logp1) + int(mw2 < mw1 and tpsa2 < 90)
    stab_better = int(var2 < var1) + int(engine["delta_engine_score"] > 0)
    safe_better = int(risk["delta_toxicity_flags"] <= 0) + int(not new_violations)
    sc = {
        "Better for Absorption": abs_better,
        "Better for Stability":  stab_better,
        "Better for Safety":     safe_better,
        "Balanced Improvement":  int(abs_better > 0 and stab_better > 0 and safe_better > 0),
    }
    max_s = max(sc.values())
    if max_s == 0:
        direction = "No Clear Advantage"
    elif sc["Balanced Improvement"] == 1:
        direction = "Balanced Improvement"
    else:
        direction = max(sc, key=sc.get)
    decision = {"optimization_direction": direction, "score_breakdown": sc}

    return {
        "drug_likeness": drug_likeness,
        "risk":          risk,
        "structure":     structure,
        "engine":        engine,
        "metabolic":     metabolic,
        "benchmark":     benchmark,
        "efficiency":    efficiency,
        "decision":      decision,
        "alerts":        alerts,
    }


# ── Generic table renderer ────────────────────────────────────────────────

def _render_insight_table(cpd_ids, all_deltas, section, rows):
    hdr = st.columns([2] + [1] * len(cpd_ids))
    hdr[0].markdown("**Metric**")
    for i, cid in enumerate(cpd_ids):
        hdr[i + 1].markdown(f"**{cid}**")

    for label, key, higher_is_better in rows:
        row = st.columns([2] + [1] * len(cpd_ids))
        row[0].write(label)
        for i, cid in enumerate(cpd_ids):
            deltas = all_deltas.get(cid)
            if deltas is None:
                row[i + 1].write("–"); continue
            val = deltas.get(section, {}).get(key)
            if val is None:
                row[i + 1].write("–"); continue
            if isinstance(val, str):
                row[i + 1].write(val); continue
            if higher_is_better is None:
                row[i + 1].markdown(
                    f'<span style="color:#c8deff;font-family:JetBrains Mono,monospace">{val}</span>',
                    unsafe_allow_html=True)
            else:
                row[i + 1].markdown(_delta_badge(float(val), higher_is_better),
                                     unsafe_allow_html=True)


# ── Advanced insights renderer ────────────────────────────────────────────

def _render_advanced_insights(selected: list):
    st.markdown("---")
    st.markdown("### 🔬 Advanced Comparison Insights")

    ref        = selected[0]
    comparisons = selected[1:]
    ref_id     = ref.get("ID", "Ref")

    if not comparisons:
        st.info("Select at least 2 compounds for advanced insights.")
        return

    # Pre-compute all deltas (local, no API calls)
    all_deltas = {}
    for cpd in comparisons:
        cid = cpd.get("ID", "?")
        try:
            all_deltas[cid] = compute_advanced_deltas(ref, cpd)
        except Exception:
            all_deltas[cid] = None

    cpd_ids = [c.get("ID", f"Cpd-{i+2}") for i, c in enumerate(comparisons)]

    itabs = st.tabs([
        "💊 Drug-Likeness",
        "⚠️ Risk",
        "🧱 Structure",
        "⚙️ Engine",
        "🔥 Metabolic",
        "📐 Benchmark",
        "⚡ Efficiency",
        "🚨 Alerts",
        "🎯 Decision",
    ])

    # 1 — Drug-Likeness
    with itabs[0]:
        st.caption(f"Reference: **{ref_id}**")
        _render_insight_table(cpd_ids, all_deltas, "drug_likeness", [
            ("ΔLipinski Violations", "delta_lipinski_violations", False),
            ("ΔVeber Compliance",    "delta_veber_compliance",    True),
            ("ΔQED",                 "delta_qed",                 True),
            ("QED Direction",        "qed_direction",             None),
            ("ΔSA Score",            "delta_sa_score",            False),
        ])

    # 2 — Risk
    with itabs[1]:
        st.caption(f"Reference: **{ref_id}** · Lower risk delta = better")
        _render_insight_table(cpd_ids, all_deltas, "risk", [
            ("ΔSolubility Risk",   "delta_solubility_risk",   False),
            ("ΔPermeability Risk", "delta_permeability_risk", False),
            ("ΔStability Proxy",   "delta_stability_proxy",   False),
            ("ΔToxicity Flags",    "delta_toxicity_flags",    False),
        ])

    # 3 — Structure
    with itabs[2]:
        st.caption(f"Reference: **{ref_id}**")
        _render_insight_table(cpd_ids, all_deltas, "structure", [
            ("ΔRing Count",        "delta_ring_count",      None),
            ("ΔAromatic Rings",    "delta_aromatic_rings",  None),
            ("ΔHeavy Atoms",       "delta_heavy_atoms",     False),
            ("ΔChirality Centers", "delta_chiral_centers",  False),
        ])

    # 4 — Engine
    with itabs[3]:
        st.caption(f"Reference: **{ref_id}** · Higher score + lower variance = better")
        _render_insight_table(cpd_ids, all_deltas, "engine", [
            ("ΔEngine Score",         "delta_engine_score",         True),
            ("ΔAgreement (variance)",  "delta_agreement_score",      False),
            ("ΔPrediction Stability",  "delta_prediction_stability", True),
        ])

    # 5 — Metabolic
    with itabs[4]:
        st.caption(f"Reference: **{ref_id}** · Fewer metabolic sites = lower liability")
        _render_insight_table(cpd_ids, all_deltas, "metabolic", [
            ("ΔMetabolic Sites", "delta_metabolic_sites", False),
            ("ΔPhase I Vuln",    "delta_phase1_vuln",     False),
            ("Phase I (ref)",    "phase1_r1",              None),
            ("Phase I (cpd)",    "phase1_r2",              None),
            ("ΔReactive Risk",   "delta_reactive_risk",   False),
        ])

    # 6 — Benchmark
    with itabs[5]:
        st.caption(f"Reference: **{ref_id}** · vs FDA Approved Drug profile")
        _render_insight_table(cpd_ids, all_deltas, "benchmark", [
            ("ΔDrug Similarity",  "delta_drug_similarity", True),
            ("ΔPercentile Rank",  "delta_percentile_rank", True),
            ("ΔOutlier Score",    "delta_outlier_score",   False),
            ("Pct Rank (ref)",    "pct_r1",                None),
            ("Pct Rank (cpd)",    "pct_r2",                None),
        ])

    # 7 — Efficiency
    with itabs[6]:
        st.caption(f"Reference: **{ref_id}**")
        _render_insight_table(cpd_ids, all_deltas, "efficiency", [
            ("ΔLigand Efficiency",  "delta_ligand_efficiency", True),
            ("ΔProperty Density",   "delta_property_density",  True),
            ("LE (ref)",            "le_r1",                   None),
            ("LE (cpd)",            "le_r2",                   None),
        ])

    # 8 — Alerts
    with itabs[7]:
        st.caption("Red flags introduced vs reference compound")
        for cid, deltas in all_deltas.items():
            if deltas is None:
                st.error(f"{cid}: computation failed"); continue
            a = deltas["alerts"]
            with st.expander(f"**{cid}** — {len(a['new_violations'])} alert(s)", expanded=True):
                if a["risk_escalation"]:
                    for v in a["new_violations"]:
                        st.markdown(f'<span style="color:#f87171">🔴 {v}</span>',
                                    unsafe_allow_html=True)
                else:
                    st.markdown('<span style="color:#4ade80">🟢 No new violations vs reference</span>',
                                unsafe_allow_html=True)
                st.markdown(
                    f'<span style="color:#94a3b8">⚪ Structural: {a["structural_alerts"]}</span>',
                    unsafe_allow_html=True)

    # 9 — Decision
    with itabs[8]:
        st.caption("Optimization direction recommendation vs reference")
        _DIR_COLORS = {
            "Better for Absorption": "#38bdf8",
            "Better for Stability":  "#a78bfa",
            "Better for Safety":     "#4ade80",
            "Balanced Improvement":  "#f5a623",
            "No Clear Advantage":    "#94a3b8",
        }
        _DIR_ICONS = {
            "Better for Absorption": "💧",
            "Better for Stability":  "🔒",
            "Better for Safety":     "🛡️",
            "Balanced Improvement":  "⚖️",
            "No Clear Advantage":    "—",
        }
        for cid, deltas in all_deltas.items():
            if deltas is None:
                st.warning(f"{cid}: could not compute decision"); continue
            d         = deltas["decision"]
            direction = d["optimization_direction"]
            color     = _DIR_COLORS.get(direction, "#94a3b8")
            icon      = _DIR_ICONS.get(direction, "—")
            st.markdown(
                f'<div style="background:rgba(0,0,0,.2);border:1px solid {color}40;'
                f'border-left:4px solid {color};border-radius:8px;'
                f'padding:14px 18px;margin:8px 0">'
                f'<b style="font-family:JetBrains Mono,monospace;color:{color}">'
                f'{icon} {cid}</b><br>'
                f'<span style="color:{color};font-size:1.05rem;font-weight:600">'
                f'{direction}</span></div>',
                unsafe_allow_html=True,
            )
            sc_cols = st.columns(len(d["score_breakdown"]))
            for col, (k, v) in zip(sc_cols, d["score_breakdown"].items()):
                col.metric(k.replace("Better for ", ""), v)

# NEW CODE END ─────────────────────────────────────────────────────────────
