
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
import pandas as pd

def render_chemo_test_results(results):
    st.markdown('<div class="rh">Comprehensive Molecular Validation (250+ Tests)</div>', unsafe_allow_html=True)
    
    # Categorization of keys
    structure_keys = [
        "valid", "valence_ok", "unusual_valency", "disconnected", "abnormal_bonds", "has_rings", 
        "has_aromatic", "has_hetero", "normalized", "inchi_ok", "highly_charged", 
        "chiral", "stereocenter_count", "bond_density", "hetero_ratio",
        "flexibility", "crowding", "compactness", "bridgehead_count", "spiro_count", "ring_complexity"
    ]
    
    physchem_keys = [
        "mw", "logp", "mr", "tpsa", "hbd", "hba", "rot_bonds", "rings", 
        "aro_rings", "het_rings", "heavy_atoms", "total_atoms", "fsp3", 
        "formal_charge", "complexity", "labute_asa", "hall_kier_alpha"
    ]
    
    rules_keys = [
        "lipinski", "veber", "ghose", "qed", "sa_score", 
        "no_pains", "no_brenk", "no_nih", "no_zinc"
    ]
    
    # Functional groups and Descriptors are many, we'll handle them specially
    all_keys = list(results.keys())
    fg_keys = [k for k in all_keys if k.startswith("has_")]
    ratio_keys = [k for k in all_keys if k.startswith("ratio_")]
    desc_keys = [k for k in all_keys if k not in structure_keys + physchem_keys + rules_keys + fg_keys + ratio_keys and not k.startswith("fg_") and k != "similarity" and not k.startswith("_")]

    t1, t2, t3, t4, t5 = st.tabs(["🏗 Structure", "📏 PhysChem", "🏆 Rules", "🧪 Groups", "📊 Descriptors"])
    
    with t1:
        cols = st.columns(3)
        for i, k in enumerate(structure_keys):
            val = results.get(k)
            c = cols[i % 3]
            display_name = k.replace('_',' ').title()
            if isinstance(val, bool):
                icon = "✅ Pass" if val else "❌ Fail"
                c.markdown(f"**{display_name}**: {icon}")
            else:
                c.markdown(f"**{display_name}**: `{val:.3f}`" if isinstance(val, float) else f"**{display_name}**: `{val}`")
        
        st.markdown("---")
        st.markdown("**Atom Distribution (Ratios)**")
        r_cols = st.columns(4)
        for i, k in enumerate(ratio_keys):
            val = results.get(k)
            c = r_cols[i % 4]
            name = k.replace("ratio_", "").upper()
            c.metric(name, f"{val:.1%}")
                
    with t2:
        cols = st.columns(3)
        for i, k in enumerate(physchem_keys):
            val = results.get(k)
            c = cols[i % 3]
            display_name = k.upper() if len(k) <= 4 else k.replace('_',' ').title()
            c.markdown(f"**{display_name}**: `{val:.2f}`" if isinstance(val, (float, int)) else f"**{display_name}**: `{val}`")
            
    with t3:
        cols = st.columns(3)
        for i, k in enumerate(rules_keys):
            val = results.get(k)
            c = cols[i % 3]
            display_name = k.replace('_',' ').title()
            if isinstance(val, bool):
                icon = "✅ Pass" if val else "❌ Fail"
                c.markdown(f"**{display_name}**: {icon}")
            else:
                c.markdown(f"**{display_name}**: `{val:.2f}`" if isinstance(val, float) else f"**{display_name}**: `{val}`")

    with t4:
        st.markdown("**Functional Groups Detected**")
        present_fgs = [k for k in fg_keys if results.get(k)]
        if present_fgs:
            cols = st.columns(4)
            for i, k in enumerate(present_fgs):
                c = cols[i % 4]
                name = k.replace("has_", "").replace("_", " ").title()
                count = results.get(f"fg_{k.replace('has_', '')}", 1)
                c.markdown(f"🔹 {name} ({count})")
        else:
            st.info("No common functional groups detected.")
            
    with t5:
        st.markdown("**Advanced Molecular Descriptors**")
        with st.expander("Show all 200+ descriptors"):
            # Sort and display in a grid
            sorted_descs = sorted(desc_keys)
            cols = st.columns(4)
            for i, k in enumerate(sorted_descs):
                val = results.get(k)
                c = cols[i % 4]
                c.markdown(f"<small>**{k}**</small>: `{val:.2f}`" if isinstance(val, float) else f"<small>**{k}**</small>: `{val}`", unsafe_allow_html=True)

def render_chemo_score_card(pkg):
    score = pkg["score"]
    grade = pkg["grade"]
    
    st.markdown(f"""
    <div style="background:linear-gradient(135deg, #0f172a, #1a2e5a); padding:30px; border-radius:20px; border:1px solid #1e40af; text-align:center">
        <div style="font-family:'JetBrains Mono'; font-size:0.8rem; color:#60a5fa; letter-spacing:5px">CHEMOSCORE V2.0</div>
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
        template="plotly_dark",
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
        "Natural Product Likeness",
        "Custom Sandbox"
    ])

def get_preset_parameters(mode):
    defaults = {
        "mw_min": 0, "mw_max": 500, "logp_min": -2.0, "logp_max": 5.0,
        "tpsa_min": 0, "tpsa_max": 140, "hbd_max": 5, "hba_max": 10, "rot_max": 10
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
        return {**defaults, "mw_max": 500} 
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

def render_batch_intelligence(stats):
    st.markdown('<div class="rh">Dataset Intelligence Report</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("### 🧬 Diversity & Composition")
        div_val = stats.get("diversity_score", 0)
        st.metric("Tanimoto Diversity", f"{div_val:.3f}", help="1.0 = High Diversity, 0.0 = High Redundancy")
        
        # Simple progress bar for diversity
        st.progress(div_val)
        
        # Grade breakdown
        st.markdown("**Grade Distribution**")
        gd = stats.get("grade_dist", {})
        for g, count in gd.items():
            st.markdown(f"**{g}**: `{count}` compounds")
            
    with col2:
        st.markdown("### 🏗 Top Scaffolds")
        scafs = stats.get("top_scaffolds", [])
        if scafs:
            scaf_df = pd.DataFrame(scafs)
            st.dataframe(scaf_df, display_data=False, hide_index=True, use_container_width=True)
        else:
            st.info("No scaffolds identified.")
            
    st.markdown("### 🧪 Functional Group Frequency")
    fg_dist = stats.get("fg_distribution", {})
    if fg_dist:
        fg_df = pd.DataFrame({"Group": list(fg_dist.keys()), "Count": list(fg_dist.values())})
        fig = px.bar(fg_df, x="Group", y="Count", color="Count",
                     color_continuous_scale="Tealgrn",
                     template="plotly_dark")
        fig.update_layout(height=350, plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)')
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("No common groups detected across dataset.")
