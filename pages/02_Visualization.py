"""
visualization_app/app.py
────────────────────────────────────────────────────────────────────────────
ChemoFilter · Visualization Micro-App
────────────────────────────────────────────────────────────────────────────

Standalone Streamlit app dedicated entirely to molecular visualization.
95% of screen space = visualization.
Input via URL query params: ?smiles=<SMILES>

Run:  streamlit run visualization_app/app.py
────────────────────────────────────────────────────────────────────────────
"""
import streamlit as st
import urllib.parse
import base64
import io
import os
import sys

# Allow import of parent modules
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

st.set_page_config(
    page_title="ChemoFilter · Visualization",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── Minimal chrome CSS — 95%+ screen for visualization ───────────────────────
st.markdown("""<style>
@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@300;400;500&family=Syne:wght@700;800&display=swap');
:root { --teal:#00d2be; --bg:#020408; --bg1:#040a12; --tx:#e4eeec; --tx2:rgba(180,220,215,.6); }
#MainMenu, footer, header, [data-testid="stToolbar"], .stDeployButton { visibility:hidden !important; }
[data-testid="stAppViewContainer"], [data-testid="stMain"] {
  background: var(--bg) !important; padding:0 !important; }
[data-testid="block-container"] { padding: 8px 16px !important; max-width:100% !important; }
section[data-testid="stSidebar"] { display:none !important; }
.viz-header {
  display:flex; align-items:center; gap:16px; padding:10px 0 14px;
  border-bottom:1px solid rgba(0,210,190,.1); margin-bottom:10px;
}
.viz-brand { font-family:'Syne',sans-serif; font-size:1.1rem; font-weight:800;
  color:var(--teal); letter-spacing:-0.5px; }
.viz-sub { font-family:'JetBrains Mono',monospace; font-size:.55rem;
  letter-spacing:3px; text-transform:uppercase; color:rgba(0,210,190,.4); }
.prop-row { display:flex; flex-wrap:wrap; gap:8px; margin:8px 0; }
.prop-chip {
  font-family:'JetBrains Mono',monospace; font-size:.6rem; letter-spacing:1px;
  padding:5px 12px; border-radius:20px;
  background:rgba(0,210,190,.06); border:1px solid rgba(0,210,190,.18);
  color:var(--teal); white-space:nowrap;
}
.prop-chip.warn { background:rgba(240,160,32,.06); border-color:rgba(240,160,32,.2); color:#f0a020; }
.prop-chip.bad  { background:rgba(248,113,113,.06); border-color:rgba(248,113,113,.2); color:#f87171; }
.mol-frame {
  background:rgba(255,255,255,.03); border:1px solid rgba(0,210,190,.1);
  border-radius:14px; padding:12px; text-align:center; margin:8px 0;
}
</style>""", unsafe_allow_html=True)

# ── Header ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="viz-header">
  <div>
    <div class="viz-brand">⬡ ChemoFilter Visualization</div>
    <div class="viz-sub">Advanced Molecular Visualization Engine · Crystalline Noir Edition</div>
  </div>
</div>""", unsafe_allow_html=True)

# ── SMILES input (from URL params OR manual entry) ────────────────────────────
try:
    params = st.query_params
    url_smiles = params.get("smiles", "")
    if isinstance(url_smiles, list):
        url_smiles = url_smiles[0] if url_smiles else ""
except Exception:
    url_smiles = ""

col_input, col_btn = st.columns([5, 1])
with col_input:
    smiles = st.text_input(
        "SMILES", value=url_smiles or st.session_state.get("viz_smiles", ""),
        placeholder="Paste SMILES string… e.g. CC(=O)Oc1ccccc1C(=O)O",
        label_visibility="collapsed", key="viz_smiles_input")
with col_btn:
    st.markdown("<div style='height:4px'></div>", unsafe_allow_html=True)
    render_btn = st.button("⬡ Render", use_container_width=True)

# Sample molecules
SAMPLES = {
    "Aspirin": "CC(=O)Oc1ccccc1C(=O)O",
    "Caffeine": "Cn1cnc2c1c(=O)n(C)c(=O)n2C",
    "Ibuprofen": "CC(C)Cc1ccc(cc1)C(C)C(=O)O",
    "Paracetamol": "CC(=O)Nc1ccc(O)cc1",
    "Asparagine": "N[C@@H](CC(N)=O)C(=O)O",
}
sample_cols = st.columns(len(SAMPLES))
for i, (name, smi) in enumerate(SAMPLES.items()):
    with sample_cols[i]:
        if st.button(name, key=f"_viz_s_{name}", use_container_width=True):
            smiles = smi
            st.query_params["smiles"] = smi

# Use smiles from button click or input
active_smiles = smiles.strip() if smiles else ""

# ─────────────────────────────────────────────────────────────────────────────
# RENDERING ENGINE
# ─────────────────────────────────────────────────────────────────────────────

def _mol_to_svg(smi: str, width: int = 700, height: int = 500) -> str | None:
    try:
        from rdkit import Chem
        from rdkit.Chem.Draw import rdMolDraw2D
        from rdkit.Chem import rdDepictor
        mol = Chem.MolFromSmiles(smi)
        if mol is None:
            return None
        rdDepictor.Compute2DCoords(mol)
        drawer = rdMolDraw2D.MolDraw2DSVG(width, height)
        drawer.drawOptions().addStereoAnnotation = True
        drawer.drawOptions().addAtomIndices = False
        drawer.drawOptions().padding = 0.1
        # Dark background styling
        drawer.drawOptions().backgroundColour = (0.02, 0.04, 0.08, 1.0)
        drawer.drawOptions().bondLineWidth = 2.0
        drawer.DrawMolecule(mol)
        drawer.FinishDrawing()
        return drawer.GetDrawingText()
    except Exception:
        return None


def _mol_props(smi: str) -> dict:
    try:
        from rdkit import Chem
        from rdkit.Chem import Descriptors, rdMolDescriptors, Crippen
        mol = Chem.MolFromSmiles(smi)
        if mol is None:
            return {}
        return {
            "MW": round(Descriptors.MolWt(mol), 2),
            "LogP": round(Crippen.MolLogP(mol), 2),
            "TPSA": round(Descriptors.TPSA(mol), 2),
            "HBD": rdMolDescriptors.CalcNumHBD(mol),
            "HBA": rdMolDescriptors.CalcNumHBA(mol),
            "Rings": rdMolDescriptors.CalcNumRings(mol),
            "RotBonds": rdMolDescriptors.CalcNumRotatableBonds(mol),
            "HeavyAtoms": mol.GetNumHeavyAtoms(),
            "QED": round(Descriptors.qed(mol), 3),
            "Fsp3": round(rdMolDescriptors.CalcFractionCSP3(mol), 3),
            "Aromatic": rdMolDescriptors.CalcNumAromaticRings(mol),
            "Stereocenters": len(Chem.FindMolChiralCenters(mol, includeUnassigned=True)),
        }
    except Exception:
        return {}


def _lipinski(props: dict) -> list[tuple[str, bool]]:
    return [
        ("MW ≤ 500", props.get("MW", 0) <= 500),
        ("LogP ≤ 5", props.get("LogP", 0) <= 5),
        ("HBD ≤ 5", props.get("HBD", 0) <= 5),
        ("HBA ≤ 10", props.get("HBA", 0) <= 10),
    ]


def _radarchart(props: dict):
    """Create a radar/spider chart of key properties."""
    try:
        import plotly.graph_objects as go

        categories = ["QED", "Fsp3", "CNS\nViability", "Oral\nBio", "Synth\nEase"]
        mw = props.get("MW", 500)
        logp = props.get("LogP", 3)
        tpsa = props.get("TPSA", 70)
        hbd = props.get("HBD", 2)
        qed = props.get("QED", 0.5)
        fsp3 = props.get("Fsp3", 0.4)

        cns_score = max(0, min(1, 1 - tpsa / 140))
        oral_score = max(0, min(1, (1 - abs(logp - 2) / 5) * (1 - mw / 800)))
        synth_ease = max(0, min(1, 1 - props.get("Stereocenters", 0) * 0.1 - props.get("Rings", 3) * 0.05))

        values = [qed, fsp3, cns_score, oral_score, synth_ease]
        values_pct = [v * 100 for v in values]

        fig = go.Figure()
        fig.add_trace(go.Scatterpolar(
            r=values_pct + [values_pct[0]],
            theta=categories + [categories[0]],
            fill='toself',
            fillcolor='rgba(0,210,190,0.12)',
            line=dict(color='#00d2be', width=2),
            name="Profile"
        ))
        fig.update_layout(
            polar=dict(
                radialaxis=dict(visible=True, range=[0, 100],
                                tickfont=dict(size=9, color='rgba(180,220,215,.5)'),
                                gridcolor='rgba(0,210,190,.08)',
                                linecolor='rgba(0,210,190,.1)'),
                angularaxis=dict(tickfont=dict(size=10, color='rgba(180,220,215,.7)',
                                               family='JetBrains Mono'),
                                 linecolor='rgba(0,210,190,.1)',
                                 gridcolor='rgba(0,210,190,.08)'),
                bgcolor='rgba(4,10,18,0.9)'
            ),
            paper_bgcolor='rgba(4,10,18,0)',
            plot_bgcolor='rgba(4,10,18,0)',
            margin=dict(l=40, r=40, t=30, b=30),
            height=300,
            showlegend=False,
        )
        return fig
    except Exception:
        return None


def _barchart(props: dict):
    """Property comparison bar chart."""
    try:
        import plotly.graph_objects as go

        keys = ["MW", "LogP", "TPSA", "HBD", "HBA", "RotBonds", "Rings"]
        vals = [props.get(k, 0) for k in keys]
        limits = [500, 5, 140, 5, 10, 10, 6]
        colors = ['#22d88a' if v <= l else '#f87171' for v, l in zip(vals, limits)]

        fig = go.Figure(go.Bar(
            x=keys, y=vals,
            marker_color=colors,
            text=[str(v) for v in vals],
            textposition='outside',
            textfont=dict(size=11, color='rgba(228,238,236,.8)',
                          family='JetBrains Mono'),
        ))
        # Add reference lines
        for i, (k, lim) in enumerate(zip(keys, limits)):
            fig.add_shape(type="line", x0=i-0.4, x1=i+0.4,
                          y0=lim, y1=lim,
                          line=dict(color='rgba(240,160,32,.6)', width=1.5, dash='dot'))
        fig.update_layout(
            paper_bgcolor='rgba(4,10,18,0)',
            plot_bgcolor='rgba(4,10,18,0.4)',
            xaxis=dict(tickfont=dict(size=10, color='rgba(180,220,215,.7)',
                                     family='JetBrains Mono'),
                       gridcolor='rgba(0,210,190,.05)'),
            yaxis=dict(tickfont=dict(size=9, color='rgba(180,220,215,.5)'),
                       gridcolor='rgba(0,210,190,.05)'),
            margin=dict(l=20, r=20, t=20, b=20),
            height=280,
        )
        return fig
    except Exception:
        return None


def _similar_compounds(smi: str) -> list[str]:
    """Return a few structurally similar SMILES (scaffold neighbours)."""
    try:
        from rdkit import Chem
        from rdkit.Chem.Scaffolds import MurckoScaffold
        mol = Chem.MolFromSmiles(smi)
        if mol is None:
            return []
        scaf = MurckoScaffold.GetScaffoldForMol(mol)
        return [Chem.MolToSmiles(scaf)] if scaf else []
    except Exception:
        return []


# ─────────────────────────────────────────────────────────────────────────────
# MAIN VISUALIZATION PANEL
# ─────────────────────────────────────────────────────────────────────────────

if active_smiles:
    with st.spinner("Rendering…"):
        props = _mol_props(active_smiles)

    if not props:
        st.error("❌ Invalid SMILES — cannot render molecule.")
    else:
        # ── Property chips row ────────────────────────────────────────────────
        def _chip_class(key, val):
            limits = {"MW": 500, "LogP": 5, "TPSA": 140, "HBD": 5, "HBA": 10,
                      "RotBonds": 10}
            if key not in limits:
                return ""
            return "" if val <= limits[key] else ("warn" if val <= limits[key] * 1.2 else "bad")

        chips_html = '<div class="prop-row">'
        for k, v in props.items():
            cls = _chip_class(k, v)
            chips_html += f'<span class="prop-chip {cls}">{k}: {v}</span>'
        chips_html += '</div>'
        st.markdown(chips_html, unsafe_allow_html=True)

        # ── Lipinski rules ─────────────────────────────────────────────────────
        rules = _lipinski(props)
        pass_count = sum(1 for _, p in rules)
        rule_html = '<div class="prop-row">'
        for label, passed in rules:
            col = "#22d88a" if passed else "#f87171"
            icon = "✅" if passed else "❌"
            rule_html += f'<span class="prop-chip" style="border-color:{col}40;color:{col}">{icon} {label}</span>'
        rule_html += f'<span class="prop-chip">Lipinski {pass_count}/4</span></div>'
        st.markdown(rule_html, unsafe_allow_html=True)

        # ── Main panel: 2D structure + charts ─────────────────────────────────
        col_2d, col_charts = st.columns([3, 2])

        with col_2d:
            st.markdown('<div class="mol-frame">', unsafe_allow_html=True)

            svg = _mol_to_svg(active_smiles, width=680, height=480)
            if svg:
                # Embed SVG directly (scales perfectly)
                st.markdown(
                    f'<div style="width:100%;overflow:hidden;border-radius:8px">'
                    f'{svg}</div>',
                    unsafe_allow_html=True)

                # PNG download
                try:
                    from rdkit import Chem
                    from rdkit.Chem.Draw import rdMolDraw2D
                    from rdkit.Chem import rdDepictor
                    mol = Chem.MolFromSmiles(active_smiles)
                    if mol:
                        rdDepictor.Compute2DCoords(mol)
                        drawer = rdMolDraw2D.MolDraw2DCairo(900, 700)
                        drawer.DrawMolecule(mol)
                        drawer.FinishDrawing()
                        png_bytes = drawer.GetDrawingText()
                        st.download_button(
                            "⬇ Download 2D Structure (PNG)",
                            data=png_bytes,
                            file_name="molecule.png",
                            mime="image/png",
                            use_container_width=True)
                except Exception:
                    pass
            else:
                st.error("Cannot render 2D structure — check SMILES")

            st.markdown('</div>', unsafe_allow_html=True)

        with col_charts:
            # Radar chart
            radar = _radarchart(props)
            if radar:
                st.markdown("**Drug Profile Radar**", help="Normalized drug-likeness dimensions")
                st.plotly_chart(radar, use_container_width=True,
                                config={"displayModeBar": False})

            # Bar chart
            bar = _barchart(props)
            if bar:
                st.markdown("**Property vs Limits**",
                            help="Orange dotted lines = Lipinski/Veber thresholds")
                st.plotly_chart(bar, use_container_width=True,
                                config={"displayModeBar": False})

        # ── Advanced analysis tabs ─────────────────────────────────────────────
        tab_3d, tab_fingerprint, tab_scaffold, tab_data = st.tabs([
            "🔮 3D View", "🧬 Fingerprint", "🔬 Scaffold", "📊 Full Data"])

        with tab_3d:
            try:
                from rdkit import Chem
                from rdkit.Chem import AllChem
                mol3d = Chem.MolFromSmiles(active_smiles)
                if mol3d:
                    mol3d = Chem.AddHs(mol3d)
                    AllChem.EmbedMolecule(mol3d, AllChem.ETKDGv3())
                    AllChem.MMFFOptimizeMolecule(mol3d)
                    conf = mol3d.GetConformer()
                    # Extract atom positions
                    positions = [(conf.GetAtomPosition(i).x,
                                  conf.GetAtomPosition(i).y,
                                  conf.GetAtomPosition(i).z)
                                 for i in range(mol3d.GetNumAtoms())]
                    atoms = [mol3d.GetAtomWithIdx(i).GetSymbol()
                             for i in range(mol3d.GetNumAtoms())]

                    # Build minimal 3D scatter via Plotly
                    import plotly.graph_objects as go
                    colors = {"C": "#c8deff", "N": "#60a5fa", "O": "#f87171",
                              "S": "#fbbf24", "F": "#34d399", "Cl": "#a78bfa",
                              "Br": "#fb923c", "H": "rgba(200,200,200,.3)"}
                    x, y, z = zip(*positions)
                    atom_colors = [colors.get(a, "#94a3b8") for a in atoms]
                    fig3d = go.Figure()
                    # Bonds
                    for bond in mol3d.GetBonds():
                        i1, i2 = bond.GetBeginAtomIdx(), bond.GetEndAtomIdx()
                        p1, p2 = positions[i1], positions[i2]
                        fig3d.add_trace(go.Scatter3d(
                            x=[p1[0], p2[0]], y=[p1[1], p2[1]], z=[p1[2], p2[2]],
                            mode='lines', line=dict(color='rgba(0,210,190,.5)', width=4),
                            showlegend=False, hoverinfo='skip'))
                    # Atoms
                    fig3d.add_trace(go.Scatter3d(
                        x=list(x), y=list(y), z=list(z),
                        mode='markers+text',
                        marker=dict(size=[8 if a != 'H' else 3 for a in atoms],
                                    color=atom_colors,
                                    line=dict(width=1, color='rgba(255,255,255,.2)')),
                        text=[a if a != 'H' else '' for a in atoms],
                        textfont=dict(size=10, color='white'),
                        hovertext=atoms,
                        showlegend=False))
                    fig3d.update_layout(
                        scene=dict(
                            bgcolor='rgba(4,10,18,0.95)',
                            xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                            yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                            zaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                        ),
                        paper_bgcolor='rgba(4,10,18,0)',
                        margin=dict(l=0, r=0, t=0, b=0),
                        height=500,
                    )
                    st.plotly_chart(fig3d, use_container_width=True)
                    st.caption("🔮 3D conformation generated via MMFF94 force-field optimisation")
            except Exception as e:
                st.info(f"3D generation requires RDKit with 3D support. ({str(e)[:80]})")

        with tab_fingerprint:
            try:
                from rdkit import Chem
                from rdkit.Chem import AllChem
                import plotly.graph_objects as go
                import numpy as np

                mol_fp = Chem.MolFromSmiles(active_smiles)
                if mol_fp:
                    fp = AllChem.GetMorganFingerprintAsBitVect(mol_fp, 2, nBits=512)
                    bits = list(fp)
                    # Display as 32×16 grid
                    grid = np.array(bits).reshape(16, 32)
                    fig_fp = go.Figure(go.Heatmap(
                        z=grid,
                        colorscale=[[0, 'rgba(4,10,18,1)'], [1, 'rgba(0,210,190,0.9)']],
                        showscale=False,
                        xgap=1, ygap=1,
                    ))
                    fig_fp.update_layout(
                        paper_bgcolor='rgba(4,10,18,0)',
                        plot_bgcolor='rgba(4,10,18,0)',
                        margin=dict(l=10, r=10, t=10, b=10),
                        height=240,
                        xaxis=dict(showticklabels=False, showgrid=False),
                        yaxis=dict(showticklabels=False, showgrid=False),
                    )
                    on_bits = fp.GetNumOnBits()
                    st.markdown(f"**ECFP4 Fingerprint (512-bit)** — {on_bits} bits set "
                                f"({on_bits/512*100:.1f}% density)")
                    st.plotly_chart(fig_fp, use_container_width=True,
                                    config={"displayModeBar": False})
                    st.caption("Each teal cell = active bit in the Morgan ECFP4 fingerprint")
            except Exception:
                st.info("Fingerprint visualization requires RDKit.")

        with tab_scaffold:
            try:
                from rdkit import Chem
                from rdkit.Chem.Scaffolds import MurckoScaffold
                from rdkit.Chem.Draw import rdMolDraw2D
                from rdkit.Chem import rdDepictor

                mol_sc = Chem.MolFromSmiles(active_smiles)
                if mol_sc:
                    scaf = MurckoScaffold.GetScaffoldForMol(mol_sc)
                    generic = MurckoScaffold.MakeScaffoldGeneric(scaf) if scaf else None
                    c1, c2 = st.columns(2)
                    with c1:
                        st.markdown("**Murcko Scaffold**")
                        if scaf:
                            rdDepictor.Compute2DCoords(scaf)
                            dr = rdMolDraw2D.MolDraw2DSVG(400, 300)
                            dr.drawOptions().backgroundColour = (0.02, 0.04, 0.08, 1.0)
                            dr.DrawMolecule(scaf)
                            dr.FinishDrawing()
                            st.markdown(dr.GetDrawingText(), unsafe_allow_html=True)
                            st.code(Chem.MolToSmiles(scaf), language=None)
                    with c2:
                        st.markdown("**Generic Scaffold**")
                        if generic:
                            rdDepictor.Compute2DCoords(generic)
                            dr2 = rdMolDraw2D.MolDraw2DSVG(400, 300)
                            dr2.drawOptions().backgroundColour = (0.02, 0.04, 0.08, 1.0)
                            dr2.DrawMolecule(generic)
                            dr2.FinishDrawing()
                            st.markdown(dr2.GetDrawingText(), unsafe_allow_html=True)
                            st.code(Chem.MolToSmiles(generic), language=None)
            except Exception as e:
                st.info(f"Scaffold decomposition: {str(e)[:100]}")

        with tab_data:
            try:
                import sys, os
                sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
                from data_engine import compute_feature_vector
                import pandas as pd

                with st.spinner("Computing full feature vector…"):
                    fv = compute_feature_vector(active_smiles)

                # Display by category
                cats = {
                    "Core": ["mw","exact_mw","logp","tpsa","hbd","hba",
                              "rotatable_bonds","rings","aromatic_rings",
                              "heavy_atoms","fsp3","qed","bertz_complexity"],
                    "Drug-Likeness": ["lipinski_pass","veber_pass","ghose_pass",
                                      "egan_pass","muegge_pass","ro3_pass",
                                      "drug_likeness_score","drug_like_flag",
                                      "lead_like_flag","fragment_like_flag"],
                    "ADMET": ["hia_predicted","bbb_predicted","cns_mpo_score",
                               "oral_bioavailability_score","cyp3a4_inhibitor",
                               "cyp2d6_inhibitor","cyp1a2_inhibitor",
                               "herg_risk","dili_risk","ames_mutagenicity"],
                    "Efficiency": ["lead_score","grade","ligand_efficiency",
                                   "lipophilic_efficiency","optimization_score",
                                   "risk_reward_score","development_priority",
                                   "synthetic_accessibility","np_likeness_score"],
                    "Decision": ["key_concern","recommendation","next_step"],
                }
                for cat_name, keys in cats.items():
                    with st.expander(f"📂 {cat_name}"):
                        rows = [(k, fv.get(k, "—")) for k in keys if k in fv]
                        if rows:
                            df_cat = pd.DataFrame(rows, columns=["Property", "Value"])
                            st.dataframe(df_cat, use_container_width=True, hide_index=True)
            except Exception as e:
                st.info(f"Full data requires data_engine.py: {str(e)[:100]}")
else:
    st.markdown("""
<div style="text-align:center;padding:80px 40px;font-family:'JetBrains Mono',monospace">
  <div style="font-size:3rem;margin-bottom:20px">🔬</div>
  <div style="font-size:1rem;color:rgba(0,210,190,.6);margin-bottom:12px">
    Enter a SMILES string above or pick a sample compound
  </div>
  <div style="font-size:.65rem;letter-spacing:2px;text-transform:uppercase;
    color:rgba(0,210,190,.3)">
    2D Structure · 3D View · Fingerprint · Scaffold · Full Property Data
  </div>
</div>""", unsafe_allow_html=True)

# ── Footer ────────────────────────────────────────────────────────────────────
st.markdown("""
<div style="border-top:1px solid rgba(0,210,190,.06);padding:10px 0 0;
  font-family:'JetBrains Mono',monospace;font-size:.5rem;letter-spacing:2px;
  text-transform:uppercase;color:rgba(0,210,190,.2);text-align:center">
  ChemoFilter Visualization · RDKit · Plotly · VIT Chennai MDP 2026
</div>""", unsafe_allow_html=True)
