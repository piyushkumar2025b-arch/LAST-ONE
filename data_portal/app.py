"""
data_portal/app.py
────────────────────────────────────────────────────────────────────────────
ChemoFilter · Data Portal Micro-App
────────────────────────────────────────────────────────────────────────────

Standalone Streamlit app: searchable compound database, documentation,
system overview, usage guide.

Run:  streamlit run data_portal/app.py
────────────────────────────────────────────────────────────────────────────
"""
import streamlit as st
import os, sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

st.set_page_config(
    page_title="ChemoFilter · Data Portal",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown("""<style>
@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@300;400;500&family=Syne:wght@600;700;800&family=Inter:wght@300;400;500&display=swap');
:root {--teal:#00d2be;--amber:#f0a020;--green:#22d88a;--bg:#020408;--bg1:#040a12;--bg2:#06101e;--tx:#e4eeec;--tx2:rgba(180,220,215,.6);--bdr:rgba(0,210,190,.1);}
#MainMenu,footer,[data-testid="stToolbar"],.stDeployButton{visibility:hidden!important;}
[data-testid="stAppViewContainer"],[data-testid="stMain"]{background:var(--bg)!important;}
[data-testid="block-container"]{padding:16px 32px!important;max-width:100%!important;}
.port-hero{padding:32px 0 20px;border-bottom:1px solid var(--bdr);margin-bottom:24px;}
.port-title{font-family:'Syne',sans-serif;font-size:2.4rem;font-weight:800;
  color:var(--tx);letter-spacing:-1.5px;margin-bottom:4px;}
.port-sub{font-family:'JetBrains Mono',monospace;font-size:.58rem;letter-spacing:4px;
  text-transform:uppercase;color:rgba(0,210,190,.4);}
.stat-card{background:var(--bg2);border:1px solid var(--bdr);border-radius:12px;
  padding:18px 22px;text-align:center;}
.stat-val{font-family:'Syne',sans-serif;font-size:2rem;font-weight:700;
  letter-spacing:-1px;color:var(--teal);}
.stat-lbl{font-family:'JetBrains Mono',monospace;font-size:.5rem;letter-spacing:2px;
  text-transform:uppercase;color:rgba(0,210,190,.4);margin-top:4px;}
.doc-section{background:var(--bg2);border:1px solid var(--bdr);border-radius:12px;
  padding:24px 28px;margin:12px 0;}
.doc-h{font-family:'Syne',sans-serif;font-size:1.1rem;font-weight:700;
  color:var(--tx);margin-bottom:10px;}
.doc-p{font-family:'Inter',sans-serif;font-size:.82rem;color:var(--tx2);
  line-height:1.8;}
.badge{display:inline-block;font-family:'JetBrains Mono',monospace;font-size:.5rem;
  letter-spacing:1.5px;text-transform:uppercase;padding:4px 10px;border-radius:20px;
  margin:3px;}
.badge-t{background:rgba(0,210,190,.07);border:1px solid rgba(0,210,190,.2);color:var(--teal);}
.badge-a{background:rgba(240,160,32,.07);border:1px solid rgba(240,160,32,.2);color:var(--amber);}
.badge-g{background:rgba(34,216,138,.07);border:1px solid rgba(34,216,138,.2);color:var(--green);}
</style>""", unsafe_allow_html=True)

# ── Sidebar navigation ─────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
<div style="font-family:'Syne',sans-serif;font-size:1.2rem;font-weight:800;
  color:#00d2be;letter-spacing:-0.5px;padding:8px 0 16px;
  border-bottom:1px solid rgba(0,210,190,.1)">
  ⬡ ChemoFilter<br>
  <span style="font-family:'JetBrains Mono',monospace;font-size:.5rem;
    letter-spacing:3px;color:rgba(0,210,190,.4);font-weight:400">DATA PORTAL</span>
</div>""", unsafe_allow_html=True)
    page = st.radio("", [
        "🏠 Overview",
        "🔍 Compound Explorer",
        "📋 Documentation",
        "📖 Usage Guide",
        "⚙️ API Reference",
        "📈 System Stats",
    ], label_visibility="collapsed")

# ─────────────────────────────────────────────────────────────────────────────
# PAGE: OVERVIEW
# ─────────────────────────────────────────────────────────────────────────────
if "Overview" in page:
    st.markdown("""
<div class="port-hero">
  <div class="port-title">ChemoFilter Data Portal</div>
  <div class="port-sub">⬡ Compound Intelligence Database · VIT Chennai MDP 2026 · Crystalline Noir Edition</div>
</div>""", unsafe_allow_html=True)

    # Stats row
    try:
        from data_engine import get_dataset_stats, cached_count
        stats = get_dataset_stats()
        total = cached_count()
    except Exception:
        stats = {}; total = 0

    c1, c2, c3, c4, c5, c6 = st.columns(6)
    def _stat(col, val, label):
        col.markdown(f'<div class="stat-card"><div class="stat-val">{val}</div>'
                     f'<div class="stat-lbl">{label}</div></div>', unsafe_allow_html=True)

    _stat(c1, f"{total or '—'}", "Compounds Stored")
    _stat(c2, "380+", "Features / Compound")
    _stat(c3, stats.get("avg_lead_score", "—"), "Avg Lead Score")
    _stat(c4, stats.get("grade_a_count", "—"), "Grade A Hits")
    _stat(c5, "21+", "ADMET Parameters")
    _stat(c6, "9", "Engine Tiers")

    st.markdown("<br>", unsafe_allow_html=True)

    # Platform overview
    st.markdown("""
<div class="doc-section">
  <div class="doc-h">🧠 Platform Architecture</div>
  <div class="doc-p">
    ChemoFilter is a <strong>multi-layered computational drug discovery platform</strong>
    designed for high-throughput ADMET screening and lead identification.
    The system operates across 6 architectural layers:
  </div>
  <div style="font-family:'JetBrains Mono',monospace;font-size:0.55rem;color:rgba(0,190,170,0.3);margin-bottom:12px;letter-spacing:1px">
    (Architectural components; non-interactive summary)
  </div>
  <span class="badge badge-t">Core Engine</span>
  <span class="badge badge-t">Data Layer (Parquet)</span>
  <span class="badge badge-t">API Layer (50+ APIs)</span>
  <span class="badge badge-a">Feature Engine (380+ cols)</span>
  <span class="badge badge-a">UI Layer (Streamlit)</span>
  <span class="badge badge-g">External Visualization</span>
  <span class="badge badge-g">Data Portal</span>
</div>""", unsafe_allow_html=True)

    col_l, col_r = st.columns(2)
    with col_l:
        st.markdown("""
<div class="doc-section">
  <div class="doc-h">🔬 Core Capabilities</div>
  <div class="doc-p">
    <strong>ADMET Screening:</strong> 21+ parameters per compound including Lipinski,
    BOILED-EGG, QED, SA Score, CYP panels, hERG risk, CNS MPO, and PAINS/Brenk filters.<br><br>
    <strong>Engine Tiers:</strong> 9 tiered analysis engines from Vanguard Core (RDKit) to
    Aether-Primality v10000 with 100,000+ feature tensors.<br><br>
    <strong>AI Integration:</strong> Claude AI explains ADMET results, generates structural
    analogues, suggests repurposing opportunities, and plans retrosynthesis.
  </div>
</div>""", unsafe_allow_html=True)
    with col_r:
        st.markdown("""
<div class="doc-section">
  <div class="doc-h">📦 Data Storage</div>
  <div class="doc-p">
    <strong>Format:</strong> Apache Parquet (snappy compression) for columnar,
    fast-access storage of 380+ features per compound.<br><br>
    <strong>Access:</strong> O(1) SMILES/InChIKey indexed lookup, lazy paginated
    access, never loads full dataset into memory.<br><br>
    <strong>Files:</strong><br>
    · <code>data/compounds.parquet</code> — identity + physicochemical<br>
    · <code>data/features.parquet</code> — structural + ADMET<br>
    · <code>data/bioactivity.parquet</code> — bioactivity + toxicity
  </div>
</div>""", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────────────────
# PAGE: COMPOUND EXPLORER
# ─────────────────────────────────────────────────────────────────────────────
elif "Explorer" in page:
    st.markdown("## 🔍 Compound Explorer", unsafe_allow_html=False)
    st.markdown('<div style="font-family:\'JetBrains Mono\',monospace;font-size:.55rem;'
                'letter-spacing:3px;text-transform:uppercase;color:rgba(0,210,190,.4);'
                'margin-bottom:16px">Search · Browse · Inspect</div>', unsafe_allow_html=True)

    search_col, filter_col = st.columns([3, 1])
    with search_col:
        query = st.text_input("Search compounds", placeholder="Enter SMILES, name, or InChIKey…",
                               label_visibility="collapsed")
    with filter_col:
        grade_filter = st.selectbox("Grade", ["All", "A", "B", "C", "D"],
                                     label_visibility="collapsed")

    # Try to load from Parquet; fall back to demo data
    df = None
    try:
        from data_engine import cached_search, get_compounds_page, cached_count
        import pandas as pd
        total_count = cached_count()
        if query:
            df = cached_search(query)
        elif total_count > 0:
            df = get_compounds_page(0, page_size=20,
                                    columns=["compound_id","name","smiles","mw","logp",
                                             "tpsa","qed","lead_score","grade",
                                             "drug_like_flag","key_concern","recommendation"])
    except Exception:
        df = None

    if df is None or (hasattr(df, '__len__') and len(df) == 0):
        st.info("""
**No compounds stored yet.** The database populates automatically as you
screen compounds in the main ChemoFilter app. Each compound you analyse is
stored in `data/compounds.parquet` with 380+ features for instant future retrieval.

**To populate:** Run the main app, analyse compounds → they appear here automatically.
""")
        # Show demo table with sample data
        import pandas as pd
        demo = pd.DataFrame([
            {"ID": "ASPIRIN", "MW": 180.16, "LogP": 1.19, "TPSA": 63.6, "QED": 0.554, "Grade": "B", "Key Concern": "None"},
            {"ID": "CAFFEINE", "MW": 194.19, "LogP": -0.07, "TPSA": 58.4, "QED": 0.671, "Grade": "A", "Key Concern": "None"},
            {"ID": "PARACETAMOL", "MW": 151.16, "LogP": 0.46, "TPSA": 49.3, "QED": 0.597, "Grade": "A", "Key Concern": "None"},
            {"ID": "IBUPROFEN", "MW": 206.28, "LogP": 3.97, "TPSA": 37.3, "QED": 0.672, "Grade": "B", "Key Concern": "High LogP"},
        ])
        st.markdown("**Sample Data (demo):**")
        st.dataframe(demo, use_container_width=True, hide_index=True)
    else:
        if grade_filter != "All":
            df = df[df.get("grade", df.get("Grade", pd.Series())).astype(str) == grade_filter]

        st.markdown(f'<div style="font-family:\'JetBrains Mono\',monospace;font-size:.6rem;'
                    f'color:rgba(0,210,190,.5);margin-bottom:8px">'
                    f'{len(df)} results</div>', unsafe_allow_html=True)

        # Pagination
        PAGE_SIZE = 20
        total_pages = max(1, (len(df) + PAGE_SIZE - 1) // PAGE_SIZE)
        page_num = st.number_input("Page", min_value=1, max_value=total_pages,
                                    value=1, step=1) - 1
        df_page = df.iloc[page_num * PAGE_SIZE : (page_num + 1) * PAGE_SIZE]
        st.dataframe(df_page, use_container_width=True, hide_index=True, height=400)

        # Download
        try:
            csv = df_page.to_csv(index=False).encode()
            st.download_button("⬇ Download Page as CSV", csv,
                                "compounds_export.csv", "text/csv")
        except Exception:
            pass

# ─────────────────────────────────────────────────────────────────────────────
# PAGE: DOCUMENTATION
# ─────────────────────────────────────────────────────────────────────────────
elif "Documentation" in page:
    st.markdown("## 📋 System Documentation")

    with st.expander("🧬 ADMET Parameters", expanded=True):
        st.markdown("""
**Absorption**
- Lipinski Rule of Five (MW≤500, LogP≤5, HBD≤5, HBA≤10)
- BOILED-EGG (TPSA vs LogP for HIA/BBB prediction)
- Veber Rule (TPSA≤140, RotBonds≤10)
- Egan Filter, Ghose Filter, Muegge Filter

**Distribution**
- Blood-Brain Barrier (BBB) penetration heuristic
- Human Intestinal Absorption (HIA) heuristic
- CNS MPO Score (Wager 2010) — 0 to 6
- Volume of Distribution proxy

**Metabolism**
- CYP1A2, 2C9, 2C19, 2D6, 3A4 inhibition prediction
- P-glycoprotein (P-gp) substrate/inhibitor prediction
- BCRP substrate prediction
- MAO substrate flag

**Excretion**
- Renal clearance proxy
- Hepatic clearance proxy
- Plasma half-life proxy

**Toxicity**
- hERG cardiac ion channel risk (IC50 proxy)
- AMES mutagenicity prediction
- Drug-Induced Liver Injury (DILI) risk
- PAINS / Brenk / Brenk structural alerts
- Reactive metabolite risk
""")

    with st.expander("⚙️ Engine Tiers"):
        engines = [
            ("Vanguard Core", "Tier 1", "RDKit native — 21 ADMET params", "#00d2be"),
            ("Hyper-Zenith v50", "Tier 3", "Caco-2, P-gp, skin permeability, DILI, metabolic half-life", "#f0a020"),
            ("Omni-Science v20", "Tier 5", "50+ new descriptors, topology, SAR intelligence", "#a78bfa"),
            ("Celestial v1000", "Tier 7", "PBPK kinetics, quantum descriptors, SHAP explainability", "#22d88a"),
            ("Xenon-God v5000", "Tier 8", "50,000+ params, quantum orbital dynamics, BBB flux", "#f0a020"),
            ("Aether-Primality v10000", "Tier 9", "100,000+ tensors, nanotoxicity, quantum Aether motifs", "#00d2be"),
        ]
        for name, tier, desc, color in engines:
            st.markdown(
                f'<div style="background:rgba(6,16,30,.7);border:1px solid {color}20;'
                f'border-left:3px solid {color};border-radius:8px;padding:12px 16px;margin:6px 0">'
                f'<b style="color:{color}">{name}</b> '
                f'<span style="font-size:.6rem;font-family:\'JetBrains Mono\',monospace;'
                f'color:rgba(160,200,190,.4)">{tier}</span>'
                f'<br><span style="font-size:.75rem;color:rgba(160,200,190,.6)">{desc}</span>'
                f'</div>', unsafe_allow_html=True)

    with st.expander("🌐 External API System"):
        st.markdown("""
**Tier 1 — Core APIs** (always available, 24h cached)
- PubChem REST API — compound identity, properties, synonyms
- ChEMBL — bioactivity data, IC50/Ki values, protein targets
- RCSB PDB — 3D protein structures, binding site context

**Tier 2 — Extended APIs** (user-triggered)
- OpenFDA — FDA drug labels, indications, warnings
- UniProt — protein function, organism, sequences
- KEGG — metabolic pathways, compound entries
- Europe PMC — literature search, publications
- ClinicalTrials.gov — ongoing/completed trials
- DisGeNET — gene-disease associations
- GtoPdb — pharmacology targets and ligands
- UniChem — cross-database compound references

**Tier 3 — Experimental APIs** (optional)
- Semantic Scholar — academic paper search
- NCI CACTUS — name→SMILES resolution
- ChemRisk — GHS safety classification

All APIs: lazy-loaded, 24h cached, timeout-protected, offline-safe.
""")

# ─────────────────────────────────────────────────────────────────────────────
# PAGE: USAGE GUIDE
# ─────────────────────────────────────────────────────────────────────────────
elif "Usage" in page:
    st.markdown("## 📖 Usage Guide")

    st.markdown("""
<div class="doc-section">
  <div class="doc-h">🚀 Quick Start (3 Steps)</div>
  <div class="doc-p">
    <strong>1. Input SMILES:</strong> Paste comma-separated SMILES strings in the main app.
    Upload CSV/Excel files, or load SDF/MOL files for batch screening.<br><br>
    <strong>2. Select Engine:</strong> Choose Vanguard Core for fast screening or
    Aether v10000 for maximum depth. All 9 tiers run on demand.<br><br>
    <strong>3. Analyse Results:</strong> Review the compound grid, visualise the
    BOILED-EGG chart, compare leads side-by-side, export reports in CSV/HTML/PDF.
  </div>
</div>""", unsafe_allow_html=True)

    with st.expander("📥 Input Formats"):
        st.markdown("""
**SMILES (primary)**
```
CC(=O)Oc1ccccc1C(=O)O
CC(=O)Oc1ccccc1C(=O)O, Cn1cnc2c1c(=O)n(C)c(=O)n2C
```
- Single or comma-separated
- Canonical SMILES preferred

**CSV/Excel File**
- Must have a `SMILES` column
- Optional: `ID`, `Name`, `Activity` columns

**SDF/MOL File**
- Standard MDL molfile format
- Multi-compound SDF supported

**Drug Name Lookup**
- Enter a drug name → PubChem resolves to SMILES automatically
""")

    with st.expander("📊 Understanding Results"):
        st.markdown("""
**Lead Score (0–100)**
Composite score combining QED, drug-likeness rules, alert count, and efficiency.

| Score | Grade | Meaning |
|-------|-------|---------|
| ≥ 75  | A     | Excellent lead candidate |
| 55–74 | B     | Good, minor concerns |
| 40–54 | C     | Moderate — optimise |
| < 40  | D     | Redesign recommended |

**Traffic Light System**
- 🟢 Green: Property in optimal range
- 🟡 Yellow: Borderline — monitor
- 🔴 Red: Violates threshold — action required

**PAINS Filter**
Pan-Assay Interference Compounds — structural alerts for compounds that give
false positives in biochemical assays. High PAINS count = high risk of
non-specific binding.
""")

    with st.expander("🔬 Visualization App"):
        st.markdown("""
The **Visualization App** (`visualization_app/app.py`) provides:
- Full-screen 2D molecular structure (SVG, downloadable as PNG)
- Interactive 3D conformation (MMFF94 optimised, Plotly 3D)
- ECFP4 fingerprint heatmap
- Murcko + Generic scaffold decomposition
- Full 380+ column feature data

**Access:** Click "🔬 View Full Visualization" on any compound row in the main app,
or run `streamlit run visualization_app/app.py` with `?smiles=<SMILES>` URL params.
""")

# ─────────────────────────────────────────────────────────────────────────────
# PAGE: API REFERENCE
# ─────────────────────────────────────────────────────────────────────────────
elif "API Reference" in page:
    st.markdown("## ⚙️ API & Module Reference")

    modules = {
        "data_engine.py": [
            ("compute_feature_vector(smiles)", "Compute 380+ features. Cached. <100ms."),
            ("enrich_compound(compound)", "Add full feature vector to existing compound dict."),
            ("enrich_batch(compounds)", "Enrich list; store to Parquet."),
            ("get_compound_by_smiles(smiles)", "O(1) lookup. Returns None if not found."),
            ("get_compounds_page(page, size)", "Lazy paginated access. Never loads full dataset."),
            ("search_compounds(query)", "Full-text search across name/SMILES/InChIKey."),
            ("get_dataset_stats()", "Summary stats without loading full dataset."),
        ],
        "api_reliability.py": [
            ("safe_api_call(fn, *args)", "Universal exception shield. Never raises."),
            ("with_retry(fn, retries=2, timeout=5)", "Retry + timeout wrapper."),
            ("get_fallback(api_key, smiles)", "Local fallback for any API. Always succeeds."),
            ("fetch_multiple(api_calls)", "Run multiple APIs, partial success handling."),
            ("render_api_health_panel()", "Show live API health dashboard."),
        ],
        "landing_enhancements.py": [
            ("render_landing_enhancements()", "All 10 landing page interactive additions."),
            ("render_quick_molecule_preview()", "Instant MW/LogP/TPSA + validation."),
            ("render_feature_cards()", "Feature highlight cards with tooltips."),
            ("render_recent_analysis_memory()", "Session-state last compound recall."),
        ],
        "new_columns.py": [
            ("render_new_columns(display_data)", "Injects 5 new smart columns into results."),
            ("get_visualization_url(smiles)", "Build ?smiles=… URL for viz app."),
            ("get_portal_url(smiles)", "Build ?smiles=… URL for data portal."),
            ("get_insight_summary(compound)", "One-line compound insight."),
            ("get_risk_summary(compound)", "Key risk flags."),
            ("get_recommendation(compound)", "Next development step."),
        ],
    }

    for mod, funcs in modules.items():
        with st.expander(f"📄 `{mod}`"):
            for fn, desc in funcs:
                st.markdown(
                    f'<div style="padding:6px 0;border-bottom:1px solid rgba(255,255,255,.04)">'
                    f'<code style="color:#00d2be;background:rgba(0,210,190,.08);'
                    f'padding:2px 6px;border-radius:4px;font-size:.72rem">{fn}</code>'
                    f'<span style="font-size:.72rem;color:rgba(160,200,190,.6);margin-left:12px">{desc}</span>'
                    f'</div>', unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────────────────
# PAGE: SYSTEM STATS
# ─────────────────────────────────────────────────────────────────────────────
elif "Stats" in page:
    st.markdown("## 📈 System Statistics")

    try:
        from data_engine import get_dataset_stats, cached_count
        import pandas as pd

        total = cached_count()
        stats = get_dataset_stats()

        m1, m2, m3, m4 = st.columns(4)
        for col, val, label in [
            (m1, total, "Total Compounds"),
            (m2, stats.get("avg_lead_score", "—"), "Avg Lead Score"),
            (m3, stats.get("grade_a_count", "—"), "Grade A Hits"),
            (m4, stats.get("drug_like_count", "—"), "Drug-Like"),
        ]:
            col.markdown(
                f'<div class="stat-card"><div class="stat-val">{val}</div>'
                f'<div class="stat-lbl">{label}</div></div>',
                unsafe_allow_html=True)

        if total == 0:
            st.info("No compounds in database yet. Analyse compounds in the main app to populate.")
        else:
            # Load summary columns for charts
            try:
                import plotly.express as px
                df = pd.read_parquet(
                    os.path.join(os.path.dirname(os.path.dirname(__file__)),
                                 "data", "compounds.parquet"),
                    columns=["grade", "lead_score", "mw", "logp", "qed"],
                    engine="pyarrow")

                col_chart1, col_chart2 = st.columns(2)
                with col_chart1:
                    grade_counts = df["grade"].value_counts().reset_index()
                    grade_counts.columns = ["Grade", "Count"]
                    fig = px.bar(grade_counts, x="Grade", y="Count",
                                  color="Grade",
                                  color_discrete_map={"A":"#22d88a","B":"#00d2be",
                                                       "C":"#f0a020","D":"#f87171"},
                                  title="Grade Distribution")
                    fig.update_layout(paper_bgcolor='rgba(4,10,18,0)',
                                      plot_bgcolor='rgba(6,16,30,.4)',
                                      height=280, margin=dict(t=30,b=10,l=10,r=10))
                    st.plotly_chart(fig, use_container_width=True,
                                    config={"displayModeBar": False})

                with col_chart2:
                    fig2 = px.scatter(df.head(200), x="logp", y="qed",
                                      color="grade",
                                      color_discrete_map={"A":"#22d88a","B":"#00d2be",
                                                           "C":"#f0a020","D":"#f87171"},
                                      title="QED vs LogP")
                    fig2.update_layout(paper_bgcolor='rgba(4,10,18,0)',
                                       plot_bgcolor='rgba(6,16,30,.4)',
                                       height=280, margin=dict(t=30,b=10,l=10,r=10))
                    st.plotly_chart(fig2, use_container_width=True,
                                    config={"displayModeBar": False})
            except Exception:
                st.info("Charts available once compounds are stored.")
    except Exception as e:
        st.warning(f"Statistics unavailable: {str(e)[:100]}")

# ── Footer ──────────────────────────────────────────────────────────────────────
st.markdown("""
<div style="border-top:1px solid rgba(0,210,190,.06);padding:12px 0 0;margin-top:20px;
  font-family:'JetBrains Mono',monospace;font-size:.5rem;letter-spacing:2px;
  text-transform:uppercase;color:rgba(0,210,190,.2);text-align:center">
  ChemoFilter Data Portal · Apache Parquet · RDKit · Streamlit · VIT Chennai MDP 2026
</div>""", unsafe_allow_html=True)
