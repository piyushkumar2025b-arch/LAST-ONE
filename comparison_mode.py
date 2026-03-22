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


def _radar_fig(compounds: list) -> "go.Figure | None":
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
