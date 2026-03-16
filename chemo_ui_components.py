
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

def render_chemo_test_results(results):
    st.markdown('<div class="rh">Molecular Validation Tests (50+)</div>', unsafe_allow_html=True)
    
    # Group tests
    structure_keys = ["valid", "valence_ok", "disconnected", "abnormal_bonds", "has_rings", "has_aromatic", "has_hetero", "normalized", "highly_charged", "chiral", "reactive", "inchi_ok"]
    property_keys = ["mw", "logp", "tpsa", "rot_bonds", "rings", "hbd", "hba", "fsp3", "atom_count", "heavy_atoms", "carbon_fraction", "hetero_ratio"]
    quality_keys = ["lipinski", "qed", "sa_score", "no_pains", "no_brenk", "no_nih", "drug_like", "murcko_heavy", "bridgehead"]
    
    t1, t2, t3 = st.tabs(["🏗 Structure", "📏 Properties", "🏆 Quality"])
    
    with t1:
        cols = st.columns(3)
        for i, k in enumerate(structure_keys):
            val = results.get(k)
            c = cols[i % 3]
            if isinstance(val, bool):
                icon = "✅" if val else "❌"
                c.markdown(f"**{k.replace('_',' ').title()}**: {icon}")
            else:
                c.markdown(f"**{k.replace('_',' ').title()}**: `{val}`")
                
    with t2:
        cols = st.columns(3)
        for i, k in enumerate(property_keys):
            val = results.get(k)
            c = cols[i % 3]
            c.markdown(f"**{k.upper()}**: `{val}`")
            
    with t3:
        cols = st.columns(3)
        for i, k in enumerate(quality_keys):
            val = results.get(k)
            c = cols[i % 3]
            if isinstance(val, bool):
                icon = "✅" if val else "❌"
                c.markdown(f"**{k.replace('_',' ').title()}**: {icon}")
            else:
                c.markdown(f"**{k.replace('_',' ').title()}**: `{val}`")

def render_chemo_score_card(pkg):
    score = pkg["score"]
    grade = pkg["grade"]
    
    st.markdown(f"""
    <div style="background:linear-gradient(135deg, #0f172a, #1a2e5a); padding:30px; border-radius:20px; border:1px solid #1e40af; text-align:center">
        <div style="font-family:'JetBrains Mono'; font-size:0.8rem; color:#60a5fa; letter-spacing:5px">CHEMOSCORE V1.0</div>
        <div style="font-family:'Playfair Display'; font-size:5rem; font-weight:900; color:white; margin:10px 0">{score}</div>
        <div style="font-family:'Playfair Display'; font-size:2rem; color:#e8a020">GRADE: {grade}</div>
    </div>
    """, unsafe_allow_html=True)
    
    # Component Chart
    comp = pkg["components"]
    fig = go.Figure(go.Bar(
        x=list(comp.keys()),
        y=list(comp.values()),
        marker_color=['#3b82f6', '#10b981', '#f59e0b', '#ef4444', '#8b5cf6']
    ))
    fig.update_layout(
        title="Score Component Breakdown",
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font_color='#c8deff',
        yaxis_range=[0, 1]
    )
    st.plotly_chart(fig, use_container_width=True)

def render_preset_selector():
    return st.selectbox("Preset Filter Modes", [
        "Standard Drug-Like (Lipinski)",
        "Lead-Like (Moderate)",
        "Fragment-Like (Small)",
        "CNS Focused (Lower TPSA)",
        "Tox-Free Precision",
        "Natural Product Likeness"
    ])

def get_preset_parameters(mode):
    defaults = {
        "mw_max": 500, "logp_min": -2.0, "logp_max": 5.0,
        "tpsa_max": 140, "hbd_max": 5, "hba_max": 10, "rot_max": 10
    }
    
    if mode == "Standard Drug-Like (Lipinski)":
        return defaults
    elif mode == "Lead-Like (Moderate)":
        return {**defaults, "mw_max": 450, "logp_max": 4.5, "rot_max": 8}
    elif mode == "Fragment-Like (Small)":
        return {**defaults, "mw_max": 300, "logp_max": 3.0, "tpsa_max": 60, "hbd_max": 3, "hba_max": 3}
    elif mode == "CNS Focused (Lower TPSA)":
        return {**defaults, "mw_max": 400, "tpsa_max": 79, "logp_max": 4.0}
    elif mode == "Tox-Free Precision":
        return {**defaults, "mw_max": 500} # Logic usually handles this via filters
    return defaults

def plot_chemo_property_distribution(df, prop, title):
    if df.empty or prop not in df: return None
    fig = px.histogram(df, x=prop, title=title, 
                       color_discrete_sequence=['#3b82f6'],
                       template="plotly_dark",
                       nbins=30)
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font_color='#c8deff',
        bargap=0.05
    )
    return fig

def plot_chemo_scatter(df, x_prop, y_prop, color_prop="ChemoScore"):
    if df.empty or x_prop not in df or y_prop not in df: return None
    fig = px.scatter(df, x=x_prop, y=y_prop, color=color_prop,
                     title=f"{x_prop} vs {y_prop}",
                     template="plotly_dark",
                     color_continuous_scale="Viridis",
                     hover_data=["ID"])
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font_color='#c8deff'
    )
    return fig
