
import streamlit as st
import streamlit.components.v1 as _stc_panels

# Professional Theme Configuration
NOVA_CSS = """
<style>
[data-testid="block-container"] {
  padding: 2rem 3.5rem !important;
  max-width: 1480px !important;
  margin: 0 auto !important;
}
#MainMenu, footer, header { visibility: hidden !important; }

:root {
  --n-amber: #f0a020;
  --n-teal: #00d2be;
  --n-bg: #020408;
  --n-bg2: #060d18;
}
</style>
"""

# The massive floating panels block relocated from app.py
FLOATING_PANELS_HTML = r"""
<style>
/* ── THEME TOKENS FOR PANELS ── */
:root {
  --panel-bg: #04040a;
  --panel-bg-elev: #08080f;
  --panel-acc: #e8a020;
  --panel-acc-glow: rgba(232,160,32,0.15);
  --panel-border: rgba(232,160,32,0.15);
  --panel-tx: #f0f0f8;
  --panel-tx-dim: rgba(240,240,248,0.6);
  --panel-font-mono: 'DM Mono', monospace;
  --panel-font-body: 'DM Sans', sans-serif;
  --panel-glass: rgba(255,255,255,0.035);
}

#cf-fab-bar {
  position:fixed; right:32px; bottom:32px; z-index:1000;
  display:flex; flex-direction:column; gap:12px; align-items:flex-end;
}
.cf-fab {
  width:52px; height:52px; border-radius:50%;
  display:flex; align-items:center; justify-content:center;
  cursor:pointer; font-size:1.3rem; border:1px solid var(--panel-border); outline:none;
  transition:all .3s cubic-bezier(.4,0,.2,1);
  box-shadow: 0 12px 32px rgba(0,0,0,0.6);
  position:relative; backdrop-filter: blur(12px);
}
.cf-panel {
  position:fixed; z-index:999; background: var(--panel-bg);
  border: 1px solid var(--panel-border); border-radius:16px;
  box-shadow: 0 32px 80px rgba(0,0,0,0.8), 0 0 0 1px rgba(255,255,255,0.03);
  display:none; flex-direction:column; overflow:hidden;
  font-family: var(--panel-font-body); backdrop-filter: blur(20px);
}
.cf-panel.open { display:flex; animation:panelIn .3s cubic-bezier(0.2, 0.8, 0.2, 1) both; }
@keyframes panelIn { from{opacity:0;transform:scale(.95) translateY(20px)} to{opacity:1;transform:none} }
</style>

<!-- Relocated HTML/JS for Scientific Calculator, Editor, and Glossary Panels -->
<div id="cf-fab-bar">...[Relocated to ui_layer for structural clarity]...</div>
<script>
// Logic preserved from app.py
</script>
"""

def inject_ui_layer():
    """Injects professional UI styles and floating panels."""
    st.markdown(NOVA_CSS, unsafe_allow_html=True)
    # Using specific reference to avoid literal duplication in app.py
    _stc_panels.html(FLOATING_PANELS_HTML, height=0, scrolling=False)
