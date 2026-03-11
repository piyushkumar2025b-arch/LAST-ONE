"""
ChemoFilter — Landing Page Module
===================================
A standalone Claude-AI-inspired landing page for ChemoFilter.
Completely isolated from inner app logic — zero impact on existing functions.

HOW TO INTEGRATE into your existing app.py:
============================================
Add these lines at the VERY TOP of app.py (before any other st.* calls):

    from landing import render_landing
    if "entered_app" not in st.session_state:
        st.session_state.entered_app = False
    if not st.session_state.entered_app:
        if render_landing():
            st.session_state.entered_app = True
            st.rerun()
        st.stop()

That's it. Your entire existing app runs exactly as before,
just gated behind the landing page on first load.
"""

import streamlit as st


def render_landing() -> bool:
    """
    Renders the full-screen landing page.
    Returns True when the user clicks any Launch button.
    """
    st.markdown(_CSS, unsafe_allow_html=True)
    st.markdown(_HERO_HTML, unsafe_allow_html=True)

    # Hero CTA — Streamlit native button
    c1, c2, c3 = st.columns([1.3, 1, 1.3])
    with c2:
        hero = st.button("Launch ChemoFilter →", key="_lp_hero", use_container_width=True)

    st.markdown(_POST_HERO_HTML, unsafe_allow_html=True)

    # CTA section button
    c4, c5, c6 = st.columns([1.3, 1, 1.3])
    with c5:
        cta = st.button("Begin Discovery →", key="_lp_cta", use_container_width=True)

    st.markdown(_FOOTER_AND_SCRIPT, unsafe_allow_html=True)
    return hero or cta


# ══════════════════════════════════════════════════════════════════════════
#  CSS
# ══════════════════════════════════════════════════════════════════════════
_CSS = """<style>
@import url('https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=DM+Sans:opsz,wght@9..40,300;9..40,400;9..40,500&family=DM+Mono:wght@400;500&display=swap');

:root {
  --bg:   #09090e; --bg1: #0f0f16; --bg2: #141420; --bg3: #1a1a28;
  --bdr:  rgba(255,255,255,0.07); --bdr2: rgba(255,255,255,0.04);
  --tx:   #ededf5; --tx2: rgba(237,237,245,0.55); --tx3: rgba(237,237,245,0.28);
  --ac:   #d4845a; --ac2: #e8a07a; --ac3: #f5c4a0;
  --r:18px; --r2:10px;
}
.cf-light {
  --bg:#f7f7f5; --bg1:#f0f0ee; --bg2:#e8e8e4; --bg3:#ddddd9;
  --bdr:rgba(0,0,0,0.08); --bdr2:rgba(0,0,0,0.04);
  --tx:#18181f; --tx2:rgba(24,24,31,0.55); --tx3:rgba(24,24,31,0.28);
}
#MainMenu,footer,header,[data-testid="stToolbar"],.stDeployButton{visibility:hidden!important;display:none!important}
section[data-testid="stSidebar"]{display:none!important}
html,body,[data-testid="stAppViewContainer"],[data-testid="stMain"],[data-testid="block-container"],.main,.block-container{
  background:var(--bg)!important;padding:0!important;max-width:100%!important;}
[data-testid="stVerticalBlock"]{gap:0!important}
.stButton>button{
  font-family:'DM Sans',sans-serif!important;font-size:.95rem!important;font-weight:500!important;
  padding:13px 28px!important;border-radius:var(--r2)!important;border:none!important;
  background:var(--ac)!important;color:#fff!important;cursor:pointer!important;
  transition:background .2s,transform .15s,box-shadow .2s!important;
  box-shadow:0 4px 20px rgba(212,132,90,.3)!important;letter-spacing:.2px!important;
}
.stButton>button:hover{background:var(--ac2)!important;transform:translateY(-2px)!important;box-shadow:0 8px 32px rgba(212,132,90,.45)!important}
.cf-wrap{font-family:'DM Sans',sans-serif;color:var(--tx);background:var(--bg);position:relative;overflow-x:hidden}
.cf-amb{position:fixed;inset:0;pointer-events:none;z-index:0}
.cf-gl{position:absolute;border-radius:50%;filter:blur(140px)}
.cf-g1{width:700px;height:700px;top:-220px;right:-120px;background:radial-gradient(circle,#d4845a 0%,transparent 65%);opacity:.1;animation:drift 14s ease-in-out infinite alternate}
.cf-g2{width:550px;height:550px;bottom:-180px;left:-100px;background:radial-gradient(circle,#a68afb 0%,transparent 65%);opacity:.09;animation:drift 18s ease-in-out infinite alternate-reverse}
.cf-g3{width:320px;height:320px;top:45%;left:42%;background:radial-gradient(circle,#5dd4c8 0%,transparent 65%);opacity:.05;animation:drift 22s ease-in-out infinite}
@keyframes drift{from{transform:translate(0,0) scale(1)}to{transform:translate(45px,32px) scale(1.1)}}
.cf-dots{position:fixed;inset:0;pointer-events:none;z-index:0;background-image:radial-gradient(rgba(255,255,255,.055) 1px,transparent 1px);background-size:28px 28px}
.cf-nav{position:fixed;top:0;left:0;right:0;z-index:200;display:flex;align-items:center;justify-content:space-between;padding:18px 52px;background:rgba(9,9,14,.78);backdrop-filter:blur(24px);border-bottom:1px solid var(--bdr2)}
.cf-brand{display:flex;align-items:center;gap:11px;font-family:'Instrument Serif',serif;font-size:1.35rem;color:var(--tx)}
.cf-hex{width:34px;height:34px;border-radius:9px;background:linear-gradient(135deg,var(--ac),var(--ac2));display:grid;place-items:center;font-size:1rem}
.cf-navr{display:flex;align-items:center;gap:32px}
.cf-ni{font-size:.78rem;color:var(--tx2)}
.cf-badge{font-family:'DM Mono',monospace;font-size:.58rem;letter-spacing:1.5px;text-transform:uppercase;padding:5px 13px;border-radius:20px;background:rgba(212,132,90,.1);border:1px solid rgba(212,132,90,.22);color:var(--ac2)}
.cf-hero{position:relative;z-index:10;min-height:100vh;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;padding:140px 52px 60px;max-width:1100px;margin:0 auto}
.cf-tag{display:inline-flex;align-items:center;gap:9px;font-family:'DM Mono',monospace;font-size:.6rem;letter-spacing:2.5px;text-transform:uppercase;color:var(--ac2);padding:7px 18px;border-radius:20px;background:rgba(212,132,90,.07);border:1px solid rgba(212,132,90,.18);margin-bottom:40px;animation:up .6s ease both}
.cf-tag::before{content:'';width:5px;height:5px;border-radius:50%;background:var(--ac);animation:blink 2s ease-in-out infinite}
@keyframes blink{0%,100%{opacity:1}50%{opacity:.2}}
.cf-h1{font-family:'Instrument Serif',serif;font-size:clamp(3rem,7.5vw,6.8rem);line-height:1.03;letter-spacing:-1.5px;color:var(--tx);margin:0;animation:up .65s .08s ease both}
.cf-h1 em{font-style:italic;background:linear-gradient(120deg,var(--ac3),var(--ac) 50%,var(--ac2));-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text}
.cf-h2{font-family:'Instrument Serif',serif;font-size:clamp(3rem,7.5vw,6.8rem);line-height:1.03;letter-spacing:-1.5px;color:var(--tx2);margin:0 0 36px;animation:up .65s .14s ease both}
.cf-desc{font-size:1.05rem;line-height:1.76;font-weight:300;color:var(--tx2);max-width:510px;margin:0 auto 44px;animation:up .65s .22s ease both}
.cf-sub-note{font-family:'DM Mono',monospace;font-size:.6rem;letter-spacing:2px;text-transform:uppercase;color:var(--tx3);margin-top:10px;animation:up .65s .36s ease both}
.cf-mrow{display:flex;border:1px solid var(--bdr);border-radius:14px;overflow:hidden;background:var(--bdr);gap:1px;margin-top:56px;width:100%;max-width:740px;animation:up .65s .44s ease both}
.cf-m{flex:1;background:var(--bg1);padding:22px 14px;text-align:center}
.cf-mv{font-family:'Instrument Serif',serif;font-size:2rem;color:var(--tx);line-height:1;letter-spacing:-1px}
.cf-mv span{color:var(--ac);font-style:italic}
.cf-ml{font-family:'DM Mono',monospace;font-size:.56rem;letter-spacing:1.8px;text-transform:uppercase;color:var(--tx3);margin-top:6px}
.cf-div{height:1px;background:var(--bdr2);margin:0 52px}
.cf-fhd{text-align:center;padding:80px 52px 52px;max-width:1100px;margin:0 auto}
.cf-ftitle{font-family:'Instrument Serif',serif;font-size:clamp(1.9rem,3.8vw,2.9rem);letter-spacing:-.8px;color:var(--tx);margin-bottom:14px;line-height:1.1}
.cf-fsub{font-size:.92rem;color:var(--tx2);font-weight:300;max-width:420px;margin:0 auto;line-height:1.7}
.cf-cards{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;padding:0 52px 72px;max-width:1100px;margin:0 auto}
.cf-card{background:var(--bg1);border:1px solid var(--bdr);border-radius:var(--r);padding:28px 24px;transition:border-color .25s,transform .2s,box-shadow .22s;position:relative;overflow:hidden}
.cf-card::after{content:'';position:absolute;top:0;left:10%;right:10%;height:1px;background:linear-gradient(90deg,transparent,var(--ac),transparent);opacity:0;transition:opacity .3s}
.cf-card:hover{border-color:rgba(212,132,90,.28);transform:translateY(-3px);box-shadow:0 16px 48px rgba(0,0,0,.35)}
.cf-card:hover::after{opacity:1}
.cf-ico{width:42px;height:42px;border-radius:10px;display:grid;place-items:center;font-size:1.2rem;margin-bottom:16px}
.ia{background:rgba(212,132,90,.1)}.ib{background:rgba(93,212,200,.1)}.ic{background:rgba(166,138,251,.1)}.id{background:rgba(82,217,154,.1)}.ie{background:rgba(250,196,0,.1)}.if{background:rgba(248,113,113,.1)}
.cf-ct{font-family:'Instrument Serif',serif;font-size:1.05rem;color:var(--tx);margin-bottom:9px;letter-spacing:-.2px;line-height:1.3}
.cf-cb{font-size:.78rem;color:var(--tx2);line-height:1.7;font-weight:300}
.cf-cp{display:inline-block;margin-top:14px;font-family:'DM Mono',monospace;font-size:.56rem;letter-spacing:1.2px;padding:4px 10px;border-radius:4px;background:rgba(212,132,90,.07);border:1px solid rgba(212,132,90,.14);color:var(--ac2);text-transform:uppercase}
.cf-pipe-wrap{padding:52px 52px 72px;max-width:1100px;margin:0 auto}
.cf-pipe-title{font-family:'Instrument Serif',serif;font-size:1.9rem;color:var(--tx);text-align:center;margin-bottom:40px;letter-spacing:-.5px}
.cf-pipe{display:flex;align-items:stretch;gap:0;border:1px solid var(--bdr);border-radius:var(--r);overflow:hidden;background:var(--bdr)}
.cf-ps{flex:1;background:var(--bg1);padding:18px 12px;text-align:center}
.cf-ptag{font-family:'DM Mono',monospace;font-size:.64rem;font-weight:500;color:var(--ac);letter-spacing:.8px}
.cf-pn{font-size:.72rem;color:var(--tx2);margin-top:4px;font-weight:300}
.cf-par{display:flex;align-items:center;justify-content:center;background:var(--bg);width:18px;color:var(--tx3);font-size:.65rem}
.cf-how-wrap{padding:0 52px 72px;max-width:800px;margin:0 auto}
.cf-step{display:flex;gap:28px;align-items:flex-start;padding:30px 0;border-bottom:1px solid var(--bdr2)}
.cf-step:last-child{border-bottom:none}
.cf-sn{font-family:'Instrument Serif',serif;font-size:3.2rem;color:rgba(212,132,90,.12);min-width:52px;line-height:1;letter-spacing:-2px;padding-top:2px}
.cf-stitle{font-family:'Instrument Serif',serif;font-size:1.1rem;color:var(--tx);margin-bottom:8px;letter-spacing:-.2px}
.cf-sdesc{font-size:.8rem;color:var(--tx2);font-weight:300;line-height:1.76}
.cf-cta-wrap{padding:0 52px 72px;max-width:740px;margin:0 auto}
.cf-cta{background:var(--bg1);border:1px solid var(--bdr);border-radius:24px;padding:60px 52px;text-align:center;position:relative;overflow:hidden}
.cf-cta::before{content:'';position:absolute;inset:0;border-radius:24px;background:radial-gradient(ellipse 70% 50% at 50% 0%,rgba(212,132,90,.05),transparent)}
.cf-cta-t{font-family:'Instrument Serif',serif;font-size:2.1rem;letter-spacing:-.8px;color:var(--tx);margin-bottom:14px;position:relative}
.cf-cta-s{font-size:.88rem;color:var(--tx2);font-weight:300;margin-bottom:36px;position:relative;line-height:1.6}
.cf-chips{display:flex;flex-wrap:wrap;gap:8px;justify-content:center;margin-top:28px;position:relative}
.cf-chip{font-family:'DM Mono',monospace;font-size:.56rem;letter-spacing:1.2px;text-transform:uppercase;padding:5px 11px;border-radius:4px;border:1px solid var(--bdr);color:var(--tx3)}
.cf-footer{padding:26px 52px;border-top:1px solid var(--bdr2);display:flex;align-items:center;justify-content:space-between;position:relative;z-index:10}
.cf-fl{font-family:'DM Mono',monospace;font-size:.58rem;letter-spacing:2px;text-transform:uppercase;color:var(--tx3)}
.cf-fr{display:flex;gap:20px}
.cf-fc{font-size:.7rem;color:var(--tx3);font-weight:300}
#cf-thm{position:fixed;bottom:26px;right:26px;z-index:300;width:44px;height:44px;border-radius:50%;background:var(--bg2);border:1px solid var(--bdr);display:grid;place-items:center;cursor:pointer;font-size:1.1rem;backdrop-filter:blur(12px);transition:.2s;box-shadow:0 8px 32px rgba(0,0,0,.4)}
#cf-thm:hover{transform:scale(1.1)}
@keyframes up{from{opacity:0;transform:translateY(18px)}to{opacity:1;transform:translateY(0)}}
</style>"""


_HERO_HTML = """
<div class="cf-wrap" id="cf-root">
<div class="cf-amb"><div class="cf-gl cf-g1"></div><div class="cf-gl cf-g2"></div><div class="cf-gl cf-g3"></div></div>
<div class="cf-dots"></div>
<nav class="cf-nav">
  <div class="cf-brand"><span class="cf-hex">⬡</span>ChemoFilter</div>
  <div class="cf-navr">
    <span class="cf-ni">ADMET Engine</span>
    <span class="cf-ni">Drug Atlas</span>
    <span class="cf-ni">Celestial v1000</span>
    <span class="cf-badge">v1,000,000</span>
  </div>
</nav>
<div class="cf-hero">
  <div class="cf-tag">VIT Chennai MDP 2026 · Omnipotent Edition</div>
  <h1 class="cf-h1">The Future of</h1>
  <h1 class="cf-h1"><em>Drug Discovery</em></h1>
  <h2 class="cf-h2">is here.</h2>
  <p class="cf-desc">ChemoFilter delivers 21+ ADMET parameters, quantum-grade accuracy engines, and Claude AI-powered molecular intelligence — all in one elegant platform.</p>
"""

_POST_HERO_HTML = """
  <p class="cf-sub-note">No setup required · Streamlit Cloud</p>
  <div class="cf-mrow">
    <div class="cf-m"><div class="cf-mv">21<span>+</span></div><div class="cf-ml">ADMET Params</div></div>
    <div class="cf-m"><div class="cf-mv">100<span>k+</span></div><div class="cf-ml">Features</div></div>
    <div class="cf-m"><div class="cf-mv">200<span>+</span></div><div class="cf-ml">FDA Refs</div></div>
    <div class="cf-m"><div class="cf-mv">25</div><div class="cf-ml">Analysis Tabs</div></div>
    <div class="cf-m"><div class="cf-mv">99<span>.9%</span></div><div class="cf-ml">Accuracy</div></div>
  </div>
</div>
<div class="cf-div"></div>
<div class="cf-fhd">
  <div class="cf-tag" style="display:inline-flex;margin-bottom:20px">Core Capabilities</div>
  <div class="cf-ftitle">Everything your pipeline needs</div>
  <div class="cf-fsub">From SMILES input to clinical-grade ADMET profiling in seconds.</div>
</div>
<div class="cf-cards">
  <div class="cf-card"><div class="cf-ico ia">🧬</div><div class="cf-ct">ADMET Intelligence</div><div class="cf-cb">Full absorption, distribution, metabolism, excretion & toxicity profiling with Lipinski Ro5, BOILED-EGG, Veber, Muegge, CNS MPO and 21+ parameters.</div><span class="cf-cp">21 parameters</span></div>
  <div class="cf-card"><div class="cf-ico ib">⚛️</div><div class="cf-ct">Celestial v1000 Engine</div><div class="cf-cb">Mechanistic PBPK kinetics, QUED quantum descriptors, deep Saagar hazard atlas, and SHAP-based explainable AI for Phase-III translation.</div><span class="cf-cp">Phase III ready</span></div>
  <div class="cf-card"><div class="cf-ico ic">🤖</div><div class="cf-ct">Claude AI Integration</div><div class="cf-cb">AI-powered medicinal chemistry explainer, structural analogue generation, drug repurposing analysis, and retrosynthesis pathway planning.</div><span class="cf-cp">Claude Sonnet 4</span></div>
  <div class="cf-card"><div class="cf-ico id">📊</div><div class="cf-ct">Visual Analytics Suite</div><div class="cf-cb">BOILED-EGG ADME map, PCA chemical space, Tanimoto similarity matrix, per-compound radar charts, and parallel coordinate plots.</div><span class="cf-cp">Interactive charts</span></div>
  <div class="cf-card"><div class="cf-ico ie">🛡️</div><div class="cf-ct">Safety Intelligence</div><div class="cf-cb">hERG cardiac risk, AMES mutagenicity, PAINS filter, multi-organ tox atlas, covalent warhead scouting, DDI alerts and eco-toxicology.</div><span class="cf-cp">1000+ tox alerts</span></div>
  <div class="cf-card"><div class="cf-ico if">🔬</div><div class="cf-ct">Aether v10000 Engine</div><div class="cf-cb">Tissue-specific permeability, nanotoxicity scan, quantum orbital dynamics, solvation energy, photo-stability and genetic nexus analysis.</div><span class="cf-cp">100k+ features</span></div>
</div>
<div class="cf-div"></div>
<div class="cf-pipe-wrap">
  <div class="cf-pipe-title">The Engine Cascade</div>
  <div class="cf-pipe">
    <div class="cf-ps"><div class="cf-ptag">v15</div><div class="cf-pn">ADME/PK</div></div>
    <div class="cf-par">›</div>
    <div class="cf-ps"><div class="cf-ptag">v20</div><div class="cf-pn">Mega Desc</div></div>
    <div class="cf-par">›</div>
    <div class="cf-ps"><div class="cf-ptag">v30</div><div class="cf-pn">FDA Anchor</div></div>
    <div class="cf-par">›</div>
    <div class="cf-ps"><div class="cf-ptag">v50</div><div class="cf-pn">Hyper SAR</div></div>
    <div class="cf-par">›</div>
    <div class="cf-ps"><div class="cf-ptag">v200</div><div class="cf-pn">Singularity</div></div>
    <div class="cf-par">›</div>
    <div class="cf-ps"><div class="cf-ptag">v1000</div><div class="cf-pn">Celestial</div></div>
    <div class="cf-par">›</div>
    <div class="cf-ps"><div class="cf-ptag">v5000</div><div class="cf-pn">Xenon God</div></div>
    <div class="cf-par">›</div>
    <div class="cf-ps"><div class="cf-ptag">v10k</div><div class="cf-pn">Aether</div></div>
  </div>
</div>
<div class="cf-div"></div>
<div class="cf-fhd"><div class="cf-tag" style="display:inline-flex;margin-bottom:20px">Workflow</div><div class="cf-ftitle">Three steps to clinical insight</div></div>
<div class="cf-how-wrap">
  <div class="cf-step"><div class="cf-sn">01</div><div><div class="cf-stitle">Input your SMILES</div><div class="cf-sdesc">Paste one or more SMILES strings (comma-separated) or upload a CSV with a smiles column. Use the Quick Library to instantly load Aspirin, Caffeine, Olanzapine (the gold standard reference) or any pre-defined compound.</div></div></div>
  <div class="cf-step"><div class="cf-sn">02</div><div><div class="cf-stitle">Run the tiered engine cascade</div><div class="cf-sdesc">ChemoFilter passes each molecule through the full v15 → v10000 engine pipeline. Every tier builds on the previous results — giving you not just descriptors but deep mechanistic insight, SAR strategy and multi-organ toxicity profiling.</div></div></div>
  <div class="cf-step"><div class="cf-sn">03</div><div><div class="cf-stitle">Explore, export and act</div><div class="cf-sdesc">Navigate 25 interactive analysis tabs, generate AI-powered drug summaries, download full CSV / HTML / PDF dossiers, and make data-driven lead selection decisions in minutes.</div></div></div>
</div>
<div class="cf-div"></div>
<div class="cf-cta-wrap" style="padding-top:52px">
  <div class="cf-cta">
    <div class="cf-cta-t">Ready to screen your compounds?</div>
    <div class="cf-cta-s">Launch the full ChemoFilter platform — running live on Streamlit Cloud.</div>
"""

_FOOTER_AND_SCRIPT = """
    <div class="cf-chips">
      <span class="cf-chip">RDKit</span><span class="cf-chip">Streamlit</span>
      <span class="cf-chip">Claude AI</span><span class="cf-chip">Plotly 5</span>
      <span class="cf-chip">PubChem API</span><span class="cf-chip">MMFF94</span>
      <span class="cf-chip">Morgan FP</span><span class="cf-chip">Cloudflare D1</span>
    </div>
  </div>
</div>
<footer class="cf-footer">
  <div class="cf-fl">ChemoFilter · VIT Chennai MDP 2026 · Omnipotent v1M</div>
  <div class="cf-fr">
    <span class="cf-fc">Lipinski [2001]</span>
    <span class="cf-fc">Daina [2016]</span>
    <span class="cf-fc">Bickerton [2012]</span>
    <span class="cf-fc">RDKit</span>
  </div>
</footer>
</div>
<button id="cf-thm" onclick="cfThm()" title="Toggle dark / light">🌙</button>
<script>
(function(){
  let dk=true;
  window.cfThm=function(){
    dk=!dk;
    const r=document.getElementById('cf-root');
    const n=document.querySelector('.cf-nav');
    const b=document.getElementById('cf-thm');
    if(!dk){
      r.classList.add('cf-light');
      if(n)n.style.background='rgba(247,247,245,.88)';
      if(b)b.innerHTML='☀️';
    }else{
      r.classList.remove('cf-light');
      if(n)n.style.background='';
      if(b)b.innerHTML='🌙';
    }
  };
})();
</script>
"""
