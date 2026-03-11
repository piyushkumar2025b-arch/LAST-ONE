"""
ChemoFilter — Professional UI Upgrade Module
=============================================
Injects dark/light mode, professional typography, enhanced data display,
and new UI components into the existing ChemoFilter app.

ZERO impact on any existing Python analysis functions.
Only CSS/JS/HTML display is changed.

HOW TO USE in app.py — add at the top after imports:
    from ui_upgrade import inject_ui, theme_toggle_sidebar, render_metric_card, render_compound_header, render_score_badge, render_section_header

Then call inject_ui() once at the very start of your app (before any st.* calls).
"""

import streamlit as st


# ══════════════════════════════════════════════════════════════════════════
#  MAIN INJECTION  —  call once at app startup
# ══════════════════════════════════════════════════════════════════════════
def inject_ui():
    """
    Injects the complete professional UI layer.
    Call at the top of app.py after st.set_page_config().
    Does NOT change any analysis logic.
    """
    _inject_fonts()
    _inject_theme_system()
    _inject_component_styles()


def _inject_fonts():
    st.markdown("""
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=DM+Sans:opsz,wght@9..40,300;9..40,400;9..40,500;9..40,600&family=DM+Mono:wght@400;500&display=swap" rel="stylesheet">
""", unsafe_allow_html=True)


def _inject_theme_system():
    st.markdown("""
<style>
/* ════════════════════════════════════
   THEME TOKEN SYSTEM
   ════════════════════════════════════ */
:root {
  /* Dark theme (default) */
  --cf-bg:        #09090e;
  --cf-bg1:       #0f0f16;
  --cf-bg2:       #141420;
  --cf-bg3:       #1c1c2a;
  --cf-bg4:       #212132;
  --cf-surface:   rgba(255,255,255,0.03);
  --cf-border:    rgba(255,255,255,0.08);
  --cf-border2:   rgba(255,255,255,0.05);
  --cf-border3:   rgba(255,255,255,0.03);

  --cf-text:      #ededf5;
  --cf-text2:     rgba(237,237,245,0.6);
  --cf-text3:     rgba(237,237,245,0.35);
  --cf-text4:     rgba(237,237,245,0.18);

  /* Brand — warm terracotta gold */
  --cf-acc:       #d4845a;
  --cf-acc2:      #e8a07a;
  --cf-acc3:      #f5c4a0;
  --cf-acc-bg:    rgba(212,132,90,0.10);
  --cf-acc-bdr:   rgba(212,132,90,0.22);

  /* Status colors */
  --cf-green:     #52d99a;
  --cf-green-bg:  rgba(82,217,154,0.10);
  --cf-red:       #f87171;
  --cf-red-bg:    rgba(248,113,113,0.10);
  --cf-yellow:    #fbbf24;
  --cf-yellow-bg: rgba(251,191,36,0.10);
  --cf-teal:      #5dd4c8;
  --cf-teal-bg:   rgba(93,212,200,0.10);
  --cf-purple:    #a68afb;
  --cf-purple-bg: rgba(166,138,251,0.10);

  --cf-r:  16px;
  --cf-r2: 10px;
  --cf-r3: 6px;
  --cf-shadow: 0 4px 24px rgba(0,0,0,0.4);
  --cf-shadow2: 0 1px 3px rgba(0,0,0,0.3);

  --cf-font-head: 'Instrument Serif', serif;
  --cf-font-body: 'DM Sans', sans-serif;
  --cf-font-mono: 'DM Mono', monospace;
}

/* ── LIGHT MODE ── */
[data-cf-theme="light"] {
  --cf-bg:        #f8f8f6;
  --cf-bg1:       #f0f0ed;
  --cf-bg2:       #e8e8e4;
  --cf-bg3:       #ddddd8;
  --cf-bg4:       #d2d2cc;
  --cf-surface:   rgba(0,0,0,0.02);
  --cf-border:    rgba(0,0,0,0.09);
  --cf-border2:   rgba(0,0,0,0.06);
  --cf-border3:   rgba(0,0,0,0.03);
  --cf-text:      #18181f;
  --cf-text2:     rgba(24,24,31,0.60);
  --cf-text3:     rgba(24,24,31,0.36);
  --cf-text4:     rgba(24,24,31,0.18);
}

/* ════════════════════════════════════
   GLOBAL APP STYLES
   ════════════════════════════════════ */
html, body {
  background: var(--cf-bg) !important;
  font-family: var(--cf-font-body) !important;
  color: var(--cf-text) !important;
}

/* Streamlit containers */
[data-testid="stAppViewContainer"],
[data-testid="stMain"],
.main, .block-container {
  background: var(--cf-bg) !important;
  color: var(--cf-text) !important;
}

/* Sidebar */
[data-testid="stSidebar"] {
  background: var(--cf-bg1) !important;
  border-right: 1px solid var(--cf-border2) !important;
}
[data-testid="stSidebar"] * {
  color: var(--cf-text) !important;
}

/* Streamlit text elements */
h1, h2, h3, h4, h5, h6,
.stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {
  font-family: var(--cf-font-head) !important;
  color: var(--cf-text) !important;
  letter-spacing: -0.3px !important;
}
p, .stMarkdown p, label, span {
  font-family: var(--cf-font-body) !important;
  color: var(--cf-text2) !important;
}

/* Input fields */
.stTextInput input, .stTextArea textarea {
  background: var(--cf-bg2) !important;
  border: 1px solid var(--cf-border) !important;
  border-radius: var(--cf-r2) !important;
  color: var(--cf-text) !important;
  font-family: var(--cf-font-mono) !important;
  font-size: 0.85rem !important;
  transition: border-color 0.2s !important;
}
.stTextInput input:focus, .stTextArea textarea:focus {
  border-color: var(--cf-acc) !important;
  box-shadow: 0 0 0 2px var(--cf-acc-bg) !important;
  outline: none !important;
}

/* Buttons */
.stButton > button {
  font-family: var(--cf-font-body) !important;
  font-weight: 500 !important;
  border-radius: var(--cf-r2) !important;
  border: 1px solid var(--cf-border) !important;
  background: var(--cf-bg2) !important;
  color: var(--cf-text) !important;
  transition: all 0.18s ease !important;
  font-size: 0.85rem !important;
}
.stButton > button:hover {
  border-color: var(--cf-acc) !important;
  background: var(--cf-acc-bg) !important;
  color: var(--cf-acc2) !important;
}
/* Primary button override */
.stButton > button[kind="primary"] {
  background: var(--cf-acc) !important;
  border-color: transparent !important;
  color: #fff !important;
}
.stButton > button[kind="primary"]:hover {
  background: var(--cf-acc2) !important;
}

/* Select box */
.stSelectbox > div > div {
  background: var(--cf-bg2) !important;
  border: 1px solid var(--cf-border) !important;
  border-radius: var(--cf-r2) !important;
  color: var(--cf-text) !important;
}

/* Tabs */
.stTabs [data-baseweb="tab-list"] {
  background: var(--cf-bg1) !important;
  border-bottom: 1px solid var(--cf-border) !important;
  gap: 2px !important;
  padding: 4px 8px 0 !important;
}
.stTabs [data-baseweb="tab"] {
  font-family: var(--cf-font-mono) !important;
  font-size: 0.68rem !important;
  letter-spacing: 0.5px !important;
  text-transform: uppercase !important;
  color: var(--cf-text3) !important;
  background: transparent !important;
  border-radius: 6px 6px 0 0 !important;
  padding: 8px 14px !important;
  border: none !important;
  transition: color 0.2s, background 0.2s !important;
}
.stTabs [aria-selected="true"] {
  color: var(--cf-acc2) !important;
  background: var(--cf-bg2) !important;
  border-bottom: 2px solid var(--cf-acc) !important;
}
.stTabs [data-baseweb="tab"]:hover {
  color: var(--cf-text2) !important;
  background: var(--cf-surface) !important;
}
.stTabs [data-baseweb="tab-panel"] {
  background: var(--cf-bg) !important;
  padding: 20px 0 !important;
}

/* Expander */
.streamlit-expanderHeader {
  background: var(--cf-bg1) !important;
  border: 1px solid var(--cf-border) !important;
  border-radius: var(--cf-r2) !important;
  color: var(--cf-text) !important;
  font-family: var(--cf-font-body) !important;
}
.streamlit-expanderContent {
  background: var(--cf-bg1) !important;
  border: 1px solid var(--cf-border) !important;
  border-top: none !important;
  border-radius: 0 0 var(--cf-r2) var(--cf-r2) !important;
}

/* Dataframe / table */
[data-testid="stDataFrame"] {
  border: 1px solid var(--cf-border) !important;
  border-radius: var(--cf-r) !important;
  overflow: hidden !important;
}
.dvn-scroller { background: var(--cf-bg1) !important; }
.col-header-cell { background: var(--cf-bg2) !important; color: var(--cf-text2) !important; }

/* Metrics */
[data-testid="stMetric"] {
  background: var(--cf-bg1) !important;
  border: 1px solid var(--cf-border) !important;
  border-radius: var(--cf-r) !important;
  padding: 18px 20px !important;
}
[data-testid="stMetricLabel"] {
  font-family: var(--cf-font-mono) !important;
  font-size: 0.62rem !important;
  letter-spacing: 1.5px !important;
  text-transform: uppercase !important;
  color: var(--cf-text3) !important;
}
[data-testid="stMetricValue"] {
  font-family: var(--cf-font-head) !important;
  font-size: 1.8rem !important;
  color: var(--cf-text) !important;
  letter-spacing: -0.5px !important;
}

/* Dividers */
hr { border-color: var(--cf-border2) !important; }

/* Code blocks */
code, .stCode {
  font-family: var(--cf-font-mono) !important;
  background: var(--cf-bg2) !important;
  color: var(--cf-acc2) !important;
  border-radius: 4px !important;
  font-size: 0.82rem !important;
}

/* Alerts */
[data-testid="stAlert"] {
  border-radius: var(--cf-r2) !important;
  border: 1px solid var(--cf-border) !important;
}

/* Progress bar */
.stProgress > div > div {
  background: var(--cf-acc) !important;
  border-radius: 4px !important;
}
.stProgress > div {
  background: var(--cf-bg2) !important;
  border-radius: 4px !important;
}

/* Scrollbar */
::-webkit-scrollbar { width: 6px; height: 6px; }
::-webkit-scrollbar-track { background: var(--cf-bg1); }
::-webkit-scrollbar-thumb { background: var(--cf-border); border-radius: 3px; }
::-webkit-scrollbar-thumb:hover { background: var(--cf-acc); }

/* Selection */
::selection { background: var(--cf-acc-bg); color: var(--cf-acc2); }
</style>
""", unsafe_allow_html=True)


def _inject_component_styles():
    st.markdown("""
<style>
/* ════════════════════════════════════
   PROFESSIONAL COMPONENT LIBRARY
   ════════════════════════════════════ */

/* ── SECTION HEADER ── */
.cf-sec-hdr {
  display: flex; align-items: flex-start;
  justify-content: space-between;
  padding: 24px 0 18px;
  border-bottom: 1px solid var(--cf-border2);
  margin-bottom: 24px;
}
.cf-sec-hdr-left {}
.cf-sec-eyebrow {
  font-family: var(--cf-font-mono);
  font-size: 0.58rem; letter-spacing: 2.5px; text-transform: uppercase;
  color: var(--cf-acc); margin-bottom: 6px;
}
.cf-sec-title {
  font-family: var(--cf-font-head);
  font-size: 1.55rem; color: var(--cf-text);
  letter-spacing: -0.3px; line-height: 1.2;
}
.cf-sec-sub {
  font-size: 0.8rem; color: var(--cf-text3);
  margin-top: 4px; font-weight: 300;
}
.cf-sec-badge {
  font-family: var(--cf-font-mono);
  font-size: 0.58rem; letter-spacing: 1px; text-transform: uppercase;
  padding: 5px 12px; border-radius: 20px;
  background: var(--cf-acc-bg); border: 1px solid var(--cf-acc-bdr);
  color: var(--cf-acc2); white-space: nowrap;
}

/* ── COMPOUND HEADER CARD ── */
.cf-compound-hdr {
  background: var(--cf-bg1);
  border: 1px solid var(--cf-border);
  border-radius: var(--cf-r);
  padding: 24px 28px;
  display: flex; align-items: center;
  gap: 24px; margin-bottom: 20px;
  position: relative; overflow: hidden;
}
.cf-compound-hdr::before {
  content: '';
  position: absolute; top: 0; left: 0; right: 0; height: 2px;
  background: linear-gradient(90deg, var(--cf-acc), var(--cf-acc2), transparent);
}
.cf-compound-avatar {
  width: 52px; height: 52px; border-radius: 12px;
  background: var(--cf-acc-bg); border: 1px solid var(--cf-acc-bdr);
  display: grid; place-items: center;
  font-size: 1.4rem; flex-shrink: 0;
}
.cf-compound-info { flex: 1; }
.cf-compound-name {
  font-family: var(--cf-font-head);
  font-size: 1.3rem; color: var(--cf-text);
  letter-spacing: -0.3px; margin-bottom: 4px;
}
.cf-compound-smiles {
  font-family: var(--cf-font-mono);
  font-size: 0.72rem; color: var(--cf-text3);
  word-break: break-all;
}
.cf-compound-meta {
  display: flex; gap: 8px; margin-top: 10px; flex-wrap: wrap;
}
.cf-meta-tag {
  font-family: var(--cf-font-mono);
  font-size: 0.58rem; letter-spacing: 1px; text-transform: uppercase;
  padding: 3px 9px; border-radius: 4px;
  background: var(--cf-surface); border: 1px solid var(--cf-border2);
  color: var(--cf-text3);
}

/* ── SCORE BADGE ── */
.cf-score {
  display: inline-flex; align-items: center; gap: 6px;
  font-family: var(--cf-font-mono);
  font-size: 0.7rem; font-weight: 500; letter-spacing: 0.5px;
  padding: 5px 12px; border-radius: 6px;
}
.cf-score-A { background: var(--cf-green-bg); color: var(--cf-green); border: 1px solid rgba(82,217,154,0.2); }
.cf-score-B { background: var(--cf-teal-bg); color: var(--cf-teal); border: 1px solid rgba(93,212,200,0.2); }
.cf-score-C { background: var(--cf-yellow-bg); color: var(--cf-yellow); border: 1px solid rgba(251,191,36,0.2); }
.cf-score-D { background: rgba(251,146,60,0.1); color: #fb923c; border: 1px solid rgba(251,146,60,0.2); }
.cf-score-F { background: var(--cf-red-bg); color: var(--cf-red); border: 1px solid rgba(248,113,113,0.2); }

/* ── METRIC GRID ── */
.cf-metric-grid {
  display: grid; grid-template-columns: repeat(auto-fill, minmax(160px, 1fr));
  gap: 12px; margin-bottom: 20px;
}
.cf-metric-card {
  background: var(--cf-bg1);
  border: 1px solid var(--cf-border);
  border-radius: var(--cf-r2);
  padding: 16px 18px;
  transition: border-color 0.2s, transform 0.15s;
  position: relative; overflow: hidden;
}
.cf-metric-card::after {
  content: '';
  position: absolute; top: 0; left: 0; right: 0; height: 2px;
  background: linear-gradient(90deg, var(--cf-line-col, var(--cf-acc)), transparent);
}
.cf-metric-card:hover {
  border-color: var(--cf-border);
  transform: translateY(-1px);
  box-shadow: var(--cf-shadow);
}
.cf-mc-lbl {
  font-family: var(--cf-font-mono);
  font-size: 0.58rem; letter-spacing: 1.8px; text-transform: uppercase;
  color: var(--cf-text3); margin-bottom: 8px;
}
.cf-mc-val {
  font-family: var(--cf-font-head);
  font-size: 1.55rem; color: var(--cf-text);
  letter-spacing: -0.5px; line-height: 1;
}
.cf-mc-unit {
  font-family: var(--cf-font-mono);
  font-size: 0.65rem; color: var(--cf-text3);
  margin-top: 5px;
}
.cf-mc-status {
  display: inline-block; margin-top: 8px;
  font-family: var(--cf-font-mono);
  font-size: 0.55rem; letter-spacing: 1px; text-transform: uppercase;
  padding: 3px 8px; border-radius: 4px;
}
.cf-mc-ok  { background: var(--cf-green-bg); color: var(--cf-green); }
.cf-mc-warn{ background: var(--cf-yellow-bg); color: var(--cf-yellow); }
.cf-mc-bad { background: var(--cf-red-bg); color: var(--cf-red); }

/* ── DATA TABLE ── */
.cf-table-wrap {
  border: 1px solid var(--cf-border);
  border-radius: var(--cf-r); overflow: hidden;
  margin-bottom: 20px;
}
.cf-table {
  width: 100%; border-collapse: collapse;
  font-family: var(--cf-font-body); font-size: 0.82rem;
}
.cf-table thead tr {
  background: var(--cf-bg2);
  border-bottom: 1px solid var(--cf-border);
}
.cf-table thead th {
  font-family: var(--cf-font-mono);
  font-size: 0.6rem; letter-spacing: 1.5px; text-transform: uppercase;
  color: var(--cf-text3); font-weight: 500;
  padding: 12px 16px; text-align: left;
  white-space: nowrap;
}
.cf-table tbody tr {
  border-bottom: 1px solid var(--cf-border3);
  transition: background 0.15s;
}
.cf-table tbody tr:last-child { border-bottom: none; }
.cf-table tbody tr:hover { background: var(--cf-surface); }
.cf-table tbody td {
  padding: 11px 16px; color: var(--cf-text2);
  vertical-align: middle;
}
.cf-table tbody td:first-child { color: var(--cf-text); font-weight: 500; }
.cf-td-mono { font-family: var(--cf-font-mono); font-size: 0.78rem; }
.cf-td-badge {
  display: inline-flex;
  font-family: var(--cf-font-mono);
  font-size: 0.58rem; letter-spacing: 1px; text-transform: uppercase;
  padding: 3px 8px; border-radius: 4px;
}

/* ── TOX ALERT CARD ── */
.cf-tox-card {
  background: var(--cf-red-bg);
  border: 1px solid rgba(248,113,113,0.2);
  border-radius: var(--cf-r2);
  padding: 14px 16px; margin-bottom: 8px;
  display: flex; align-items: flex-start; gap: 12px;
}
.cf-tox-icon { font-size: 1rem; flex-shrink: 0; margin-top: 1px; }
.cf-tox-name { font-size: 0.82rem; color: var(--cf-text); font-weight: 500; margin-bottom: 3px; }
.cf-tox-detail { font-size: 0.75rem; color: var(--cf-text2); font-weight: 300; }
.cf-tox-sev {
  margin-left: auto; flex-shrink: 0;
  font-family: var(--cf-font-mono); font-size: 0.58rem;
  letter-spacing: 1px; text-transform: uppercase;
  padding: 3px 8px; border-radius: 4px;
  background: rgba(248,113,113,0.15); color: var(--cf-red);
}

/* ── PASS / FAIL PILL ── */
.cf-pass { display:inline-flex;align-items:center;gap:5px;font-family:var(--cf-font-mono);font-size:.62rem;letter-spacing:1px;text-transform:uppercase;padding:4px 10px;border-radius:4px;background:var(--cf-green-bg);color:var(--cf-green);border:1px solid rgba(82,217,154,.2) }
.cf-fail { display:inline-flex;align-items:center;gap:5px;font-family:var(--cf-font-mono);font-size:.62rem;letter-spacing:1px;text-transform:uppercase;padding:4px 10px;border-radius:4px;background:var(--cf-red-bg);color:var(--cf-red);border:1px solid rgba(248,113,113,.2) }
.cf-warn { display:inline-flex;align-items:center;gap:5px;font-family:var(--cf-font-mono);font-size:.62rem;letter-spacing:1px;text-transform:uppercase;padding:4px 10px;border-radius:4px;background:var(--cf-yellow-bg);color:var(--cf-yellow);border:1px solid rgba(251,191,36,.2) }
.cf-pass::before{content:'✓';font-size:.7rem}
.cf-fail::before{content:'✗';font-size:.7rem}
.cf-warn::before{content:'⚠';font-size:.65rem}

/* ── INFO PANEL ── */
.cf-info-panel {
  background: var(--cf-bg1); border: 1px solid var(--cf-border);
  border-radius: var(--cf-r); padding: 20px 24px; margin-bottom: 16px;
}
.cf-info-title {
  font-family: var(--cf-font-mono);
  font-size: 0.62rem; letter-spacing: 2px; text-transform: uppercase;
  color: var(--cf-acc2); margin-bottom: 12px;
}
.cf-info-row {
  display: flex; justify-content: space-between; align-items: center;
  padding: 8px 0; border-bottom: 1px solid var(--cf-border3);
  font-size: 0.82rem;
}
.cf-info-row:last-child { border-bottom: none; }
.cf-info-key { color: var(--cf-text3); font-weight: 400; }
.cf-info-val { color: var(--cf-text); font-weight: 500; font-family: var(--cf-font-mono); font-size: 0.78rem; }

/* ── PROGRESS BAR CUSTOM ── */
.cf-prog-wrap { margin-bottom: 12px; }
.cf-prog-head { display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px; }
.cf-prog-lbl { font-size: 0.78rem; color: var(--cf-text2); }
.cf-prog-val { font-family: var(--cf-font-mono); font-size: 0.72rem; color: var(--cf-text3); }
.cf-prog-bar {
  height: 4px; background: var(--cf-bg3); border-radius: 2px; overflow: hidden;
}
.cf-prog-fill {
  height: 100%; border-radius: 2px;
  background: linear-gradient(90deg, var(--cf-acc), var(--cf-acc2));
  transition: width 0.6s ease;
}

/* ── STATS STRIP ── */
.cf-stats-strip {
  display: grid; grid-template-columns: repeat(9, 1fr);
  gap: 1px; background: var(--cf-border);
  border: 1px solid var(--cf-border); border-radius: var(--cf-r);
  overflow: hidden; margin-bottom: 24px;
}
.cf-stat-cell {
  background: var(--cf-bg1); padding: 16px 12px; text-align: center;
}
.cf-stat-n {
  font-family: var(--cf-font-head);
  font-size: 1.6rem; color: var(--cf-text);
  letter-spacing: -0.5px; line-height: 1;
}
.cf-stat-n.accent { color: var(--cf-acc); }
.cf-stat-n.green  { color: var(--cf-green); }
.cf-stat-n.red    { color: var(--cf-red); }
.cf-stat-n.yellow { color: var(--cf-yellow); }
.cf-stat-lbl {
  font-family: var(--cf-font-mono);
  font-size: 0.52rem; letter-spacing: 1.5px; text-transform: uppercase;
  color: var(--cf-text4); margin-top: 5px;
}

/* ── AI RESPONSE BOX ── */
.cf-ai-box {
  background: linear-gradient(135deg, var(--cf-bg1), var(--cf-bg2));
  border: 1px solid var(--cf-border);
  border-radius: var(--cf-r); padding: 24px 28px;
  margin: 16px 0; position: relative; overflow: hidden;
}
.cf-ai-box::before {
  content: '';
  position: absolute; top: 0; left: 0; right: 0; height: 2px;
  background: linear-gradient(90deg, var(--cf-purple), var(--cf-acc), var(--cf-teal));
}
.cf-ai-header {
  display: flex; align-items: center; gap: 10px;
  margin-bottom: 14px;
}
.cf-ai-icon {
  width: 32px; height: 32px; border-radius: 8px;
  background: var(--cf-purple-bg); display: grid; place-items: center;
  font-size: 0.9rem; border: 1px solid rgba(166,138,251,0.2);
}
.cf-ai-label {
  font-family: var(--cf-font-mono);
  font-size: 0.62rem; letter-spacing: 1.5px; text-transform: uppercase;
  color: var(--cf-purple);
}
.cf-ai-content {
  font-size: 0.88rem; line-height: 1.75; color: var(--cf-text2);
  font-weight: 300;
}

/* ── THEME TOGGLE (floating) ── */
#cf-theme-toggle {
  position: fixed; bottom: 24px; right: 24px; z-index: 9999;
  width: 42px; height: 42px; border-radius: 50%;
  background: var(--cf-bg2); border: 1px solid var(--cf-border);
  display: grid; place-items: center; cursor: pointer;
  font-size: 1rem; backdrop-filter: blur(12px);
  transition: all 0.2s; box-shadow: var(--cf-shadow);
}
#cf-theme-toggle:hover { transform: scale(1.1); background: var(--cf-bg3); }

/* ── SIDEBAR ENHANCEMENTS ── */
.cf-sidebar-brand {
  display: flex; align-items: center; gap: 10px;
  padding: 12px 0 20px;
  border-bottom: 1px solid var(--cf-border2);
  margin-bottom: 16px;
}
.cf-sidebar-hex {
  width: 30px; height: 30px; border-radius: 8px;
  background: linear-gradient(135deg, var(--cf-acc), var(--cf-acc2));
  display: grid; place-items: center; font-size: 0.9rem;
}
.cf-sidebar-name {
  font-family: var(--cf-font-head);
  font-size: 1.1rem; color: var(--cf-text); letter-spacing: -0.2px;
}
.cf-sidebar-ver {
  font-family: var(--cf-font-mono);
  font-size: 0.58rem; letter-spacing: 1.5px; color: var(--cf-acc2);
  text-transform: uppercase;
}
</style>
""", unsafe_allow_html=True)

    # Floating theme toggle
    st.markdown("""
<button id="cf-theme-toggle" onclick="cfMainTheme()" title="Toggle dark / light mode">🌙</button>
<script>
(function(){
  let dark = true;
  window.cfMainTheme = function() {
    dark = !dark;
    const body = document.body;
    const btn  = document.getElementById('cf-theme-toggle');
    if (!dark) {
      document.documentElement.setAttribute('data-cf-theme', 'light');
      body.setAttribute('data-cf-theme', 'light');
      // Fix Streamlit containers
      document.querySelectorAll(
        '[data-testid="stAppViewContainer"],[data-testid="stMain"],.main,.block-container,[data-testid="stSidebar"]'
      ).forEach(el => {
        el.setAttribute('data-cf-theme', 'light');
      });
      if(btn) btn.innerHTML = '☀️';
    } else {
      document.documentElement.removeAttribute('data-cf-theme');
      body.removeAttribute('data-cf-theme');
      document.querySelectorAll('[data-cf-theme]').forEach(el => el.removeAttribute('data-cf-theme'));
      if(btn) btn.innerHTML = '🌙';
    }
  };
})();
</script>
""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════
#  PYTHON HELPER COMPONENTS
# ══════════════════════════════════════════════════════════════════════════

def render_section_header(title: str, eyebrow: str = "", subtitle: str = "", badge: str = ""):
    """Render a professional section header."""
    badge_html = f'<span class="cf-sec-badge">{badge}</span>' if badge else ""
    st.markdown(f"""
<div class="cf-sec-hdr">
  <div class="cf-sec-hdr-left">
    {'<div class="cf-sec-eyebrow">' + eyebrow + '</div>' if eyebrow else ''}
    <div class="cf-sec-title">{title}</div>
    {'<div class="cf-sec-sub">' + subtitle + '</div>' if subtitle else ''}
  </div>
  {badge_html}
</div>
""", unsafe_allow_html=True)


def render_compound_header(name: str, smiles: str, grade: str = "", mw: str = "", qed: str = ""):
    """Render a professional compound header card."""
    grade_html = f'<span class="cf-score cf-score-{grade}">{grade}</span>' if grade else ""
    st.markdown(f"""
<div class="cf-compound-hdr">
  <div class="cf-compound-avatar">🧪</div>
  <div class="cf-compound-info">
    <div class="cf-compound-name">{name}</div>
    <div class="cf-compound-smiles">{smiles[:80]}{'…' if len(smiles)>80 else ''}</div>
    <div class="cf-compound-meta">
      {'<span class="cf-meta-tag">MW ' + mw + '</span>' if mw else ''}
      {'<span class="cf-meta-tag">QED ' + qed + '</span>' if qed else ''}
    </div>
  </div>
  {grade_html}
</div>
""", unsafe_allow_html=True)


def render_score_badge(value: float, label: str = ""):
    """Render a colored score badge based on value (0-100)."""
    if value >= 75:   cls, lbl = "A", "Excellent"
    elif value >= 60: cls, lbl = "B", "Good"
    elif value >= 45: cls, lbl = "C", "Moderate"
    elif value >= 30: cls, lbl = "D", "Poor"
    else:             cls, lbl = "F", "Fail"
    display = label or lbl
    st.markdown(f'<span class="cf-score cf-score-{cls}">{display} · {value:.0f}</span>', unsafe_allow_html=True)


def render_metric_card(label: str, value: str, unit: str = "", status: str = "", color: str = "var(--cf-acc)"):
    """Render a single professional metric card."""
    status_map = {"pass": "cf-mc-ok", "warn": "cf-mc-warn", "fail": "cf-mc-bad"}
    status_html = ""
    if status:
        sc = status_map.get(status.lower(), "cf-mc-ok")
        status_html = f'<div class="cf-mc-status {sc}">{status}</div>'
    st.markdown(f"""
<div class="cf-metric-card" style="--cf-line-col:{color}">
  <div class="cf-mc-lbl">{label}</div>
  <div class="cf-mc-val">{value}</div>
  {'<div class="cf-mc-unit">' + unit + '</div>' if unit else ''}
  {status_html}
</div>
""", unsafe_allow_html=True)


def render_info_panel(title: str, rows: list):
    """
    Render a key-value info panel.
    rows = [("Key", "Value"), ...]
    """
    rows_html = "".join(
        f'<div class="cf-info-row"><span class="cf-info-key">{k}</span><span class="cf-info-val">{v}</span></div>'
        for k, v in rows
    )
    st.markdown(f"""
<div class="cf-info-panel">
  <div class="cf-info-title">{title}</div>
  {rows_html}
</div>
""", unsafe_allow_html=True)


def render_progress_bar(label: str, value: float, max_val: float = 100, unit: str = ""):
    """Render a styled progress bar."""
    pct = min(100, max(0, (value / max_val) * 100)) if max_val else 0
    display_val = f"{value:.1f}{unit}"
    st.markdown(f"""
<div class="cf-prog-wrap">
  <div class="cf-prog-head">
    <span class="cf-prog-lbl">{label}</span>
    <span class="cf-prog-val">{display_val}</span>
  </div>
  <div class="cf-prog-bar">
    <div class="cf-prog-fill" style="width:{pct}%"></div>
  </div>
</div>
""", unsafe_allow_html=True)


def render_pill(text: str, kind: str = "neutral"):
    """
    Render pass/fail/warn/neutral pill.
    kind: 'pass' | 'fail' | 'warn' | 'neutral'
    """
    cls_map = {"pass": "cf-pass", "fail": "cf-fail", "warn": "cf-warn"}
    cls = cls_map.get(kind, "cf-meta-tag")
    st.markdown(f'<span class="{cls}">{text}</span>', unsafe_allow_html=True)


def render_tox_alert(name: str, detail: str = "", severity: str = "High"):
    """Render a single toxicity alert card."""
    icon_map = {"critical": "🔴", "extreme": "🔴", "high": "🟠", "moderate": "🟡", "low": "🟢", "variable": "🔵"}
    icon = icon_map.get(severity.lower(), "🟠")
    st.markdown(f"""
<div class="cf-tox-card">
  <div class="cf-tox-icon">{icon}</div>
  <div>
    <div class="cf-tox-name">{name}</div>
    {'<div class="cf-tox-detail">' + detail + '</div>' if detail else ''}
  </div>
  <div class="cf-tox-sev">{severity}</div>
</div>
""", unsafe_allow_html=True)


def render_ai_response(content: str, label: str = "Claude AI Analysis"):
    """Render an AI response in a styled box."""
    st.markdown(f"""
<div class="cf-ai-box">
  <div class="cf-ai-header">
    <div class="cf-ai-icon">✦</div>
    <div class="cf-ai-label">{label}</div>
  </div>
  <div class="cf-ai-content">{content}</div>
</div>
""", unsafe_allow_html=True)


def render_filter_results_table(compounds: list, columns: list):
    """
    Render a professional styled HTML table for compound results.
    compounds = list of dicts
    columns = list of column keys to display
    """
    if not compounds:
        st.markdown('<div class="cf-info-panel"><div class="cf-info-title">No results</div></div>', unsafe_allow_html=True)
        return

    headers = "".join(f"<th>{c}</th>" for c in columns)
    rows = ""
    for c in compounds:
        cells = ""
        for col in columns:
            val = c.get(col, "—")
            # Auto-style grade cells
            if col.lower() in ("grade", "safety_grade"):
                grade_colors = {"A": "cf-score-A", "B": "cf-score-B", "C": "cf-score-C", "D": "cf-score-D", "F": "cf-score-F", "PASSED": "cf-score-A", "REJECTED": "cf-score-F"}
                gc = grade_colors.get(str(val), "")
                cells += f'<td><span class="cf-score {gc}">{val}</span></td>'
            else:
                cells += f'<td class="cf-td-mono">{val}</td>'
        rows += f"<tr>{cells}</tr>"

    st.markdown(f"""
<div class="cf-table-wrap">
  <table class="cf-table">
    <thead><tr>{headers}</tr></thead>
    <tbody>{rows}</tbody>
  </table>
</div>
""", unsafe_allow_html=True)


def render_sidebar_brand():
    """Render the professional sidebar brand header."""
    st.sidebar.markdown("""
<div class="cf-sidebar-brand">
  <div class="cf-sidebar-hex">⬡</div>
  <div>
    <div class="cf-sidebar-name">ChemoFilter</div>
    <div class="cf-sidebar-ver">v1,000,000 · Omnipotent</div>
  </div>
</div>
""", unsafe_allow_html=True)


def theme_toggle_sidebar():
    """Add a dark/light mode toggle inside the sidebar."""
    st.sidebar.markdown("---")
    col1, col2 = st.sidebar.columns([3, 1])
    with col1:
        st.markdown('<span style="font-size:.78rem;color:var(--cf-text3)">Dark / Light Mode</span>', unsafe_allow_html=True)
    with col2:
        st.markdown('<button onclick="cfMainTheme()" style="background:var(--cf-bg2);border:1px solid var(--cf-border);border-radius:8px;padding:4px 10px;cursor:pointer;font-size:.85rem;color:var(--cf-text2)">⬡</button>', unsafe_allow_html=True)
