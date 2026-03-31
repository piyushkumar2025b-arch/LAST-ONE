"""
pages/full_report.py
────────────────────────────────────────────────────────────────────────────
ChemoFilter · Full Report — Standalone Page (Phase 4 multi-page migration)
• Reuses cached analysis results from session_state
• Zero recomputation — reads data written by main app
• Only renders when navigated to
────────────────────────────────────────────────────────────────────────────
"""
import streamlit as st

# ── Try to load session data written by main app ──────────────────────────
_data = None
_synth_keys = [k for k in st.session_state if k.startswith("_synth_data_")]
if _synth_keys:
    _data = st.session_state.get(_synth_keys[0]) if _synth_keys else None

st.markdown("""
<div style="font-family:'JetBrains Mono',monospace;font-size:.55rem;
letter-spacing:3px;color:rgba(232,160,32,.45);text-transform:uppercase;
margin-bottom:20px">⬡ ChemoFilter · Full Report Export</div>
""", unsafe_allow_html=True)

if not _data or not isinstance(_data, list):
    st.info(
        "**No analysis data available.**\n\n"
        "Run an analysis from the main ChemoFilter page first, "
        "then navigate back here to view the full report."
    )
    if st.button("← Back to Main App"):
        st.switch_page("app.py")
    st.stop()

# ── Display summary ───────────────────────────────────────────────────────
st.markdown(f"### Full Dataset Report — {len(_data)} compounds")

import pandas as pd

_SHOW_COLS = ["ID", "Grade", "LeadScore", "QED", "MW", "LogP", "tPSA",
              "SA_Score", "OralBioScore", "HIA", "BBB", "PAINS"]
_available = [c for c in _SHOW_COLS if any(c in d for d in _data)]
df = pd.DataFrame([{c: d.get(c, "–") for c in _available} for d in _data])

# Grade colouring
_GRADE_COLORS = {"A": "🟢", "B": "🟡", "C": "🟠", "F": "🔴"}
if "Grade" in df.columns:
    df["Grade"] = df["Grade"].map(lambda g: f"{_GRADE_COLORS.get(g,'')} {g}")

st.dataframe(df, use_container_width=True, height=600)

# ── Download buttons ──────────────────────────────────────────────────────
st.markdown("---")
c1, c2 = st.columns(2)
with c1:
    csv = df.to_csv(index=False).encode()
    st.download_button(
        "↓ Download CSV",
        data=csv,
        file_name="chemofilter_full_report.csv",
        mime="text/csv",
    )
with c2:
    txt_lines = [f"{d.get('ID','?')} | Grade:{d.get('Grade','?')} | "
                 f"Lead:{d.get('LeadScore','?')} | QED:{d.get('QED','?')} | "
                 f"MW:{d.get('MW','?')} | LogP:{d.get('LogP','?')}"
                 for d in _data]
    txt = "ChemoFilter Full Report\n" + "="*60 + "\n" + "\n".join(txt_lines)
    st.download_button(
        "↓ Download TXT",
        data=txt.encode(),
        file_name="chemofilter_full_report.txt",
        mime="text/plain",
    )
