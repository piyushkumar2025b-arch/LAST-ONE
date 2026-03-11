"""
ChemoFilter — Landing Page Module (REMASTERED)
"""
import streamlit as st


def render_landing() -> bool:
    st.markdown(_CSS, unsafe_allow_html=True)
    st.markdown(_ABOVE_BTN, unsafe_allow_html=True)

    c1, c2, c3 = st.columns([1.4, 1, 1.4])
    with c2:
        hero = st.button("Launch ChemoFilter →", key="_lp_hero", use_container_width=True)

    st.markdown(_BELOW_BTN, unsafe_allow_html=True)

    c4, c5, c6 = st.columns([1.4, 1, 1.4])
    with c5:
        cta = st.button("Begin Discovery →", key="_lp_cta", use_container_width=True)

    st.markdown(_FOOTER_SCRIPT, unsafe_allow_html=True)
    return hero or cta


_CSS = """<style>
@import url('https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=DM+Sans:opsz,wght@9..40,200;9..40,300;9..40,400;9..40,500;9..40,600&family=DM+Mono:wght@300;400;500&display=swap');

:root {
  --bg:#06060a; --bg1:#0c0c12; --bg2:#12121a; --bg3:#1a1a25;
  --bdr:rgba(255,255,255,0.07); --bdr2:rgba(255,255,255,0.035);
  --tx:#f0f0f8; --tx2:rgba(240,240,248,0.52); --tx3:rgba(240,240,248,0.24);
  --ac:#c8783a; --ac2:#e0954e; --ac3:#f5be86;
  --glow:rgba(200,120,58,0.18);
  --r:20px; --r2:12px;
  --nav-bg:rgba(6,6,10,0.82);
}
#cf-root.lm {
  --bg:#fafaf8; --bg1:#f3f3f0; --bg2:#ebebE6; --bg3:#e2e2dc;
  --bdr:rgba(0,0,0,0.09); --bdr2:rgba(0,0,0,0.045);
  --tx:#111118; --tx2:rgba(17,17,24,0.54); --tx3:rgba(17,17,24,0.28);
  --glow:rgba(200,120,58,0.12);
  --nav-bg:rgba(250,250,248,0.88);
}
#MainMenu,footer,header,[data-testid="stToolbar"],.stDeployButton{visibility:hidden!important;display:none!important}
section[data-testid="stSidebar"]{display:none!important}
html,body,[data-testid="stAppViewContainer"],[data-testid="stMain"],[data-testid="block-container"],.main,.block-container{
  background:var(--bg)!important;padding:0!important;max-width:100%!important;margin:0!important;}
[data-testid="stVerticalBlock"]{gap:0!important}

.stButton>button{
  font-family:'DM Sans',sans-serif!important;font-size:.95rem!important;font-weight:600!important;
  padding:15px 32px!important;border-radius:var(--r2)!important;border:none!important;
  background:linear-gradient(135deg,var(--ac),var(--ac2))!important;color:#fff!important;
  cursor:pointer!important;letter-spacing:.3px!important;transition:all .25s ease!important;
  box-shadow:0 4px 28px var(--glow)!important;
}
.stButton>button:hover{transform:translateY(-3px) scale(1.03)!important;box-shadow:0 12px 48px rgba(200,120,58,.5),0 0 0 6px rgba(200,120,58,.1)!important;}
.stButton>button:active{transform:translateY(-1px)!important}

.cf-wrap{font-family:'DM Sans',sans-serif;color:var(--tx);background:var(--bg);position:relative;overflow-x:hidden;min-height:100vh;}
.cf-orbs{position:fixed;inset:0;pointer-events:none;z-index:0;overflow:hidden}
.cf-o{position:absolute;border-radius:50%;filter:blur(100px);opacity:.18}
.cf-o1{width:900px;height:900px;top:-300px;right:-200px;background:radial-gradient(circle,#c8783a 0%,transparent 60%);animation:orb1 16s ease-in-out infinite alternate}
.cf-o2{width:700px;height:700px;bottom:-250px;left:-150px;background:radial-gradient(circle,#7c6afb 0%,transparent 60%);animation:orb2 20s ease-in-out infinite alternate-reverse;opacity:.13}
.cf-o3{width:400px;height:400px;top:40%;left:38%;background:radial-gradient(circle,#3dd4cf 0%,transparent 60%);animation:orb3 24s ease-in-out infinite;opacity:.07}
.cf-o4{width:300px;height:300px;top:20%;left:10%;background:radial-gradient(circle,#f5c842 0%,transparent 60%);animation:orb1 19s ease-in-out infinite;opacity:.06}
@keyframes orb1{0%{transform:translate(0,0) scale(1)}100%{transform:translate(60px,40px) scale(1.15)}}
@keyframes orb2{0%{transform:translate(0,0) scale(1.1)}100%{transform:translate(-40px,-50px) scale(1)}}
@keyframes orb3{0%{transform:translate(0,0)}50%{transform:translate(30px,-20px)}100%{transform:translate(0,0)}}

.cf-dots{position:fixed;inset:0;pointer-events:none;z-index:0;background-image:radial-gradient(rgba(255,255,255,.04) 1px,transparent 1px);background-size:32px 32px;}
#cf-root.lm .cf-dots{background-image:radial-gradient(rgba(0,0,0,.06) 1px,transparent 1px);}

.cf-nav{position:fixed;top:0;left:0;right:0;z-index:500;display:flex;align-items:center;justify-content:space-between;padding:16px 56px;background:var(--nav-bg);backdrop-filter:blur(28px) saturate(1.4);border-bottom:1px solid var(--bdr2);transition:background .3s;}
.cf-brand{display:flex;align-items:center;gap:12px;font-family:'Instrument Serif',serif;font-size:1.4rem;color:var(--tx);letter-spacing:-.3px;}
.cf-hexbadge{width:36px;height:36px;border-radius:10px;background:linear-gradient(135deg,var(--ac),var(--ac2));display:grid;place-items:center;font-size:1.05rem;box-shadow:0 4px 16px var(--glow);}
.cf-navlinks{display:flex;align-items:center;gap:36px}
.cf-nl{font-size:.78rem;color:var(--tx2);font-weight:400;letter-spacing:.2px;}
.cf-ver{font-family:'DM Mono',monospace;font-size:.56rem;letter-spacing:2px;text-transform:uppercase;padding:5px 14px;border-radius:20px;background:rgba(200,120,58,.1);border:1px solid rgba(200,120,58,.24);color:var(--ac2);}

#cf-thm{position:fixed;bottom:28px;right:28px;z-index:600;width:48px;height:48px;border-radius:50%;background:var(--bg2);border:1px solid var(--bdr);display:grid;place-items:center;cursor:pointer;font-size:1.15rem;backdrop-filter:blur(16px);transition:transform .2s,box-shadow .2s;box-shadow:0 8px 32px rgba(0,0,0,.5);}
#cf-thm:hover{transform:scale(1.15)}

.cf-hero{position:relative;z-index:10;min-height:100vh;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;padding:160px 52px 40px;max-width:1120px;margin:0 auto;}
.cf-eyebrow{display:inline-flex;align-items:center;gap:10px;font-family:'DM Mono',monospace;font-size:.6rem;letter-spacing:3px;text-transform:uppercase;color:var(--ac2);padding:8px 20px;border-radius:20px;background:rgba(200,120,58,.08);border:1px solid rgba(200,120,58,.2);margin-bottom:48px;animation:fadeUp .6s ease both;}
.cf-eyebrow::before{content:'';width:6px;height:6px;border-radius:50%;background:var(--ac);animation:pulse 2s ease-in-out infinite;box-shadow:0 0 0 0 rgba(200,120,58,.4);}
@keyframes pulse{0%,100%{box-shadow:0 0 0 0 rgba(200,120,58,.4)}50%{box-shadow:0 0 0 6px rgba(200,120,58,0)}}
.cf-headline{font-family:'Instrument Serif',serif;font-size:clamp(3.2rem,8vw,7.5rem);line-height:1.01;letter-spacing:-2.5px;color:var(--tx);margin:0;animation:fadeUp .65s .08s ease both;}
.cf-headline em{font-style:italic;background:linear-gradient(125deg,var(--ac3) 0%,var(--ac) 40%,var(--ac2) 80%,#f7c9a0 100%);background-size:200%;-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;animation:shimmer 4s linear infinite;}
@keyframes shimmer{0%{background-position:0%}100%{background-position:200%}}
.cf-headline2{font-family:'Instrument Serif',serif;font-size:clamp(3.2rem,8vw,7.5rem);line-height:1.01;letter-spacing:-2.5px;color:var(--tx2);margin:0 0 40px;animation:fadeUp .65s .16s ease both;}
.cf-desc{font-size:1.08rem;line-height:1.8;font-weight:300;color:var(--tx2);max-width:540px;margin:0 auto 52px;animation:fadeUp .65s .24s ease both;}
.cf-desc strong{color:var(--tx);font-weight:500}
.cf-note{font-family:'DM Mono',monospace;font-size:.58rem;letter-spacing:2px;text-transform:uppercase;color:var(--tx3);margin-top:12px;animation:fadeUp .65s .38s ease both;}
.cf-stats{display:flex;border:1px solid var(--bdr);border-radius:16px;overflow:hidden;background:var(--bdr);gap:1px;margin-top:64px;width:100%;max-width:800px;animation:fadeUp .65s .46s ease both;}
.cf-stat{flex:1;background:var(--bg1);padding:24px 10px;text-align:center;transition:background .2s;}
.cf-stat:hover{background:var(--bg2)}
.cf-sv{font-family:'Instrument Serif',serif;font-size:2.2rem;color:var(--tx);line-height:1;letter-spacing:-1px;}
.cf-sv span{color:var(--ac);font-style:italic}
.cf-sl{font-family:'DM Mono',monospace;font-size:.52rem;letter-spacing:2px;text-transform:uppercase;color:var(--tx3);margin-top:7px;}
.cf-hr{height:1px;background:var(--bdr2);margin:0 52px}
.cf-sh{text-align:center;padding:88px 52px 48px;max-width:1120px;margin:0 auto}
.cf-sh-tag{display:inline-flex;align-items:center;gap:9px;font-family:'DM Mono',monospace;font-size:.58rem;letter-spacing:2.5px;text-transform:uppercase;color:var(--ac2);padding:7px 18px;border-radius:20px;background:rgba(200,120,58,.07);border:1px solid rgba(200,120,58,.18);margin-bottom:24px;}
.cf-sh-title{font-family:'Instrument Serif',serif;font-size:clamp(2rem,4vw,3.2rem);letter-spacing:-.8px;color:var(--tx);margin-bottom:16px;line-height:1.1;}
.cf-sh-sub{font-size:.93rem;color:var(--tx2);font-weight:300;max-width:440px;margin:0 auto;line-height:1.75;}
.cf-cards{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;padding:0 52px 80px;max-width:1120px;margin:0 auto;}
.cf-card{background:var(--bg1);border:1px solid var(--bdr);border-radius:var(--r);padding:32px 28px;transition:all .28s ease;position:relative;overflow:hidden;cursor:default;}
.cf-card::before{content:'';position:absolute;inset:0;border-radius:var(--r);background:radial-gradient(ellipse 80% 50% at 50% -10%,rgba(200,120,58,.07),transparent);opacity:0;transition:opacity .3s;}
.cf-card::after{content:'';position:absolute;top:0;left:15%;right:15%;height:1px;background:linear-gradient(90deg,transparent,var(--ac),transparent);opacity:0;transition:opacity .3s;}
.cf-card:hover{border-color:rgba(200,120,58,.32);transform:translateY(-5px);box-shadow:0 20px 60px rgba(0,0,0,.4),0 0 0 1px rgba(200,120,58,.1);}
.cf-card:hover::before,.cf-card:hover::after{opacity:1}
.cf-ico{width:46px;height:46px;border-radius:12px;display:grid;place-items:center;font-size:1.3rem;margin-bottom:18px;}
.ia{background:rgba(200,120,58,.12)}.ib{background:rgba(61,212,207,.1)}.ic{background:rgba(166,138,251,.12)}.id{background:rgba(82,217,154,.1)}.ie{background:rgba(250,196,0,.1)}.if{background:rgba(248,113,113,.1)}
.cf-ct{font-family:'Instrument Serif',serif;font-size:1.08rem;color:var(--tx);margin-bottom:10px;letter-spacing:-.2px;line-height:1.3;}
.cf-cb{font-size:.79rem;color:var(--tx2);line-height:1.75;font-weight:300}
.cf-cp{display:inline-block;margin-top:16px;font-family:'DM Mono',monospace;font-size:.54rem;letter-spacing:1.5px;padding:4px 11px;border-radius:4px;background:rgba(200,120,58,.07);border:1px solid rgba(200,120,58,.16);color:var(--ac2);text-transform:uppercase;}
.cf-ticker-wrap{padding:0 0 72px;overflow:hidden;position:relative;mask-image:linear-gradient(90deg,transparent,black 10%,black 90%,transparent);}
.cf-ticker{display:flex;gap:0;animation:ticker 34s linear infinite;width:max-content;}
.cf-ticker:hover{animation-play-state:paused}
@keyframes ticker{0%{transform:translateX(0)}100%{transform:translateX(-50%)}}
.cf-tk{display:inline-flex;align-items:center;gap:10px;padding:12px 28px;font-family:'DM Mono',monospace;font-size:.65rem;letter-spacing:1.5px;text-transform:uppercase;color:var(--tx3);border-right:1px solid var(--bdr2);white-space:nowrap;}
.cf-tk::before{content:'';width:4px;height:4px;border-radius:50%;background:var(--ac);opacity:.5;}
.cf-cascade-wrap{padding:56px 52px 88px;max-width:1120px;margin:0 auto;}
.cf-cascade-title{font-family:'Instrument Serif',serif;font-size:2rem;color:var(--tx);text-align:center;margin-bottom:48px;letter-spacing:-.5px;}
.cf-cascade{display:flex;align-items:stretch;gap:0;border:1px solid var(--bdr);border-radius:16px;overflow:hidden;background:var(--bdr);}
.cf-cs{flex:1;background:var(--bg1);padding:20px 12px;text-align:center;transition:background .2s;}
.cf-cs:hover{background:var(--bg2)}
.cf-ctag{font-family:'DM Mono',monospace;font-size:.62rem;font-weight:500;color:var(--ac);letter-spacing:.8px;}
.cf-cn{font-size:.7rem;color:var(--tx2);margin-top:5px;font-weight:300}
.cf-arr{display:flex;align-items:center;justify-content:center;background:var(--bg);width:20px;color:var(--tx3);font-size:.6rem;}
.cf-steps-wrap{padding:0 52px 88px;max-width:820px;margin:0 auto;}
.cf-step{display:flex;gap:32px;align-items:flex-start;padding:36px 0;border-bottom:1px solid var(--bdr2);}
.cf-step:last-child{border-bottom:none}
.cf-sn{font-family:'Instrument Serif',serif;font-size:3.5rem;color:rgba(200,120,58,.1);min-width:56px;line-height:1;letter-spacing:-2px;padding-top:2px;transition:color .25s;}
.cf-step:hover .cf-sn{color:rgba(200,120,58,.28)}
.cf-stitle{font-family:'Instrument Serif',serif;font-size:1.12rem;color:var(--tx);margin-bottom:10px;letter-spacing:-.2px;}
.cf-sdesc{font-size:.81rem;color:var(--tx2);font-weight:300;line-height:1.8}
.cf-cta-wrap{padding:0 52px 80px;max-width:780px;margin:0 auto;}
.cf-cta{background:var(--bg1);border:1px solid var(--bdr);border-radius:28px;padding:72px 60px;text-align:center;position:relative;overflow:hidden;}
.cf-cta::before{content:'';position:absolute;inset:0;background:radial-gradient(ellipse 80% 60% at 50% 0%,rgba(200,120,58,.07),transparent);}
.cf-cta::after{content:'';position:absolute;top:0;left:20%;right:20%;height:1px;background:linear-gradient(90deg,transparent,var(--ac2),transparent);}
.cf-cta-t{font-family:'Instrument Serif',serif;font-size:2.4rem;letter-spacing:-.8px;color:var(--tx);margin-bottom:16px;position:relative;line-height:1.2;}
.cf-cta-s{font-size:.9rem;color:var(--tx2);font-weight:300;margin-bottom:40px;position:relative;line-height:1.7;}
.cf-chips{display:flex;flex-wrap:wrap;gap:8px;justify-content:center;margin-top:32px;position:relative;}
.cf-chip{font-family:'DM Mono',monospace;font-size:.54rem;letter-spacing:1.5px;text-transform:uppercase;padding:5px 13px;border-radius:5px;border:1px solid var(--bdr);color:var(--tx3);transition:border-color .2s,color .2s;}
.cf-chip:hover{border-color:rgba(200,120,58,.3);color:var(--ac2)}
.cf-footer{padding:28px 56px;border-top:1px solid var(--bdr2);display:flex;align-items:center;justify-content:space-between;position:relative;z-index:10;}
.cf-fl{font-family:'DM Mono',monospace;font-size:.56rem;letter-spacing:2.5px;text-transform:uppercase;color:var(--tx3);}
.cf-fr{display:flex;gap:22px}
.cf-fc{font-size:.7rem;color:var(--tx3);font-weight:300}
@keyframes fadeUp{from{opacity:0;transform:translateY(22px)}to{opacity:1;transform:translateY(0)}}
</style>"""


_ABOVE_BTN = """
<div class="cf-wrap" id="cf-root">
<div class="cf-orbs"><div class="cf-o cf-o1"></div><div class="cf-o cf-o2"></div><div class="cf-o cf-o3"></div><div class="cf-o cf-o4"></div></div>
<div class="cf-dots"></div>
<nav class="cf-nav" id="cf-nav">
  <div class="cf-brand"><span class="cf-hexbadge">⬡</span>ChemoFilter</div>
  <div class="cf-navlinks">
    <span class="cf-nl">ADMET Engine</span>
    <span class="cf-nl">Drug Atlas</span>
    <span class="cf-nl">Aether v10k</span>
    <span class="cf-nl">AI Lab</span>
    <span class="cf-ver">v1,000,000</span>
  </div>
</nav>
<div class="cf-hero">
  <div class="cf-eyebrow">VIT Chennai MDP 2026 &nbsp;·&nbsp; Omnipotent Edition</div>
  <h1 class="cf-headline">The Future of</h1>
  <h1 class="cf-headline"><em>Drug Discovery</em></h1>
  <h1 class="cf-headline2">starts here.</h1>
  <p class="cf-desc">ChemoFilter delivers <strong>21+ ADMET parameters</strong>, quantum-grade accuracy engines, and <strong>Claude AI-powered</strong> molecular intelligence — all in one platform.</p>
"""


_BELOW_BTN = """
  <p class="cf-note">No setup · Streamlit Cloud · Open Source</p>
  <div class="cf-stats">
    <div class="cf-stat"><div class="cf-sv">21<span>+</span></div><div class="cf-sl">ADMET Params</div></div>
    <div class="cf-stat"><div class="cf-sv">100<span>k+</span></div><div class="cf-sl">Features</div></div>
    <div class="cf-stat"><div class="cf-sv">200<span>+</span></div><div class="cf-sl">FDA Refs</div></div>
    <div class="cf-stat"><div class="cf-sv">25</div><div class="cf-sl">Analysis Tabs</div></div>
    <div class="cf-stat"><div class="cf-sv">99<span>.9%</span></div><div class="cf-sl">Accuracy</div></div>
    <div class="cf-stat"><div class="cf-sv">8<span>.5M</span></div><div class="cf-sl">Mutations Run</div></div>
  </div>
</div>

<!-- TICKER -->
<div class="cf-ticker-wrap">
  <div class="cf-ticker">
    <span class="cf-tk">Lipinski Ro5</span><span class="cf-tk">BOILED-EGG</span><span class="cf-tk">QED Score</span><span class="cf-tk">SA Score</span><span class="cf-tk">CYP Panel ×5</span><span class="cf-tk">hERG Risk</span><span class="cf-tk">CNS MPO</span><span class="cf-tk">PAINS Filter</span><span class="cf-tk">Lead Score™</span><span class="cf-tk">Oral Bio Score</span><span class="cf-tk">Celestial v1000</span><span class="cf-tk">Xenon v5000</span><span class="cf-tk">Aether v10000</span><span class="cf-tk">Claude AI</span><span class="cf-tk">PBPK Kinetics</span><span class="cf-tk">Retrosynthesis</span>
    <span class="cf-tk">Lipinski Ro5</span><span class="cf-tk">BOILED-EGG</span><span class="cf-tk">QED Score</span><span class="cf-tk">SA Score</span><span class="cf-tk">CYP Panel ×5</span><span class="cf-tk">hERG Risk</span><span class="cf-tk">CNS MPO</span><span class="cf-tk">PAINS Filter</span><span class="cf-tk">Lead Score™</span><span class="cf-tk">Oral Bio Score</span><span class="cf-tk">Celestial v1000</span><span class="cf-tk">Xenon v5000</span><span class="cf-tk">Aether v10000</span><span class="cf-tk">Claude AI</span><span class="cf-tk">PBPK Kinetics</span><span class="cf-tk">Retrosynthesis</span>
  </div>
</div>

<div class="cf-hr"></div>

<div class="cf-sh">
  <div class="cf-sh-tag">Core Capabilities</div>
  <div class="cf-sh-title">Everything your pipeline needs</div>
  <div class="cf-sh-sub">From SMILES input to clinical-grade ADMET profiling in seconds.</div>
</div>
<div class="cf-cards">
  <div class="cf-card"><div class="cf-ico ia">🧬</div><div class="cf-ct">ADMET Intelligence</div><div class="cf-cb">Full absorption, distribution, metabolism, excretion & toxicity profiling with Lipinski Ro5, BOILED-EGG, Veber, Muegge, CNS MPO and 21+ parameters.</div><span class="cf-cp">21 parameters</span></div>
  <div class="cf-card"><div class="cf-ico ib">⚛️</div><div class="cf-ct">Celestial v1000 Engine</div><div class="cf-cb">Mechanistic PBPK kinetics, QUED quantum descriptors, deep Saagar hazard atlas and SHAP-based explainable AI for Phase-III translation.</div><span class="cf-cp">Phase III ready</span></div>
  <div class="cf-card"><div class="cf-ico ic">🤖</div><div class="cf-ct">Claude AI Integration</div><div class="cf-cb">AI-powered medicinal chemistry explainer, structural analogue generation, drug repurposing analysis and retrosynthesis pathway planning.</div><span class="cf-cp">Claude Sonnet 4</span></div>
  <div class="cf-card"><div class="cf-ico id">📊</div><div class="cf-ct">Visual Analytics Suite</div><div class="cf-cb">BOILED-EGG ADME map, PCA chemical space, Tanimoto similarity matrix, per-compound radar charts and parallel coordinate plots.</div><span class="cf-cp">Interactive charts</span></div>
  <div class="cf-card"><div class="cf-ico ie">🛡️</div><div class="cf-ct">Safety Intelligence</div><div class="cf-cb">hERG cardiac risk, AMES mutagenicity, PAINS filter, multi-organ tox atlas, covalent warhead scouting, DDI alerts and eco-toxicology.</div><span class="cf-cp">1000+ tox alerts</span></div>
  <div class="cf-card"><div class="cf-ico if">🔬</div><div class="cf-ct">Aether v10000 Engine</div><div class="cf-cb">Tissue-specific permeability, nanotoxicity scan, quantum orbital dynamics, solvation energy, photo-stability and genetic nexus analysis.</div><span class="cf-cp">100k+ features</span></div>
</div>

<div class="cf-hr"></div>

<div class="cf-cascade-wrap">
  <div class="cf-cascade-title">The Engine Cascade</div>
  <div class="cf-cascade">
    <div class="cf-cs"><div class="cf-ctag">v15</div><div class="cf-cn">ADME/PK</div></div>
    <div class="cf-arr">›</div>
    <div class="cf-cs"><div class="cf-ctag">v20</div><div class="cf-cn">Mega Desc</div></div>
    <div class="cf-arr">›</div>
    <div class="cf-cs"><div class="cf-ctag">v30</div><div class="cf-cn">FDA Anchor</div></div>
    <div class="cf-arr">›</div>
    <div class="cf-cs"><div class="cf-ctag">v50</div><div class="cf-cn">Hyper SAR</div></div>
    <div class="cf-arr">›</div>
    <div class="cf-cs"><div class="cf-ctag">v200</div><div class="cf-cn">Singularity</div></div>
    <div class="cf-arr">›</div>
    <div class="cf-cs"><div class="cf-ctag">v1000</div><div class="cf-cn">Celestial</div></div>
    <div class="cf-arr">›</div>
    <div class="cf-cs"><div class="cf-ctag">v5000</div><div class="cf-cn">Xenon God</div></div>
    <div class="cf-arr">›</div>
    <div class="cf-cs"><div class="cf-ctag">v10k</div><div class="cf-cn">Aether</div></div>
    <div class="cf-arr">›</div>
    <div class="cf-cs"><div class="cf-ctag">v1M</div><div class="cf-cn">Omnipotent</div></div>
  </div>
</div>

<div class="cf-hr"></div>

<div class="cf-sh">
  <div class="cf-sh-tag">Workflow</div>
  <div class="cf-sh-title">Three steps to clinical insight</div>
</div>
<div class="cf-steps-wrap">
  <div class="cf-step"><div class="cf-sn">01</div><div><div class="cf-stitle">Input your SMILES</div><div class="cf-sdesc">Paste one or more SMILES strings (comma-separated) or upload a CSV with a smiles column. Use the Quick Library to instantly load Aspirin, Caffeine, Olanzapine — the gold-standard CNS reference — or any pre-defined compound.</div></div></div>
  <div class="cf-step"><div class="cf-sn">02</div><div><div class="cf-stitle">Run the tiered engine cascade</div><div class="cf-sdesc">ChemoFilter passes each molecule through the full v15 → v10000 pipeline. Every tier builds on previous results — delivering deep mechanistic insight, SAR strategy and multi-organ toxicity profiling.</div></div></div>
  <div class="cf-step"><div class="cf-sn">03</div><div><div class="cf-stitle">Explore, export and act</div><div class="cf-sdesc">Navigate 25 interactive analysis tabs, generate AI-powered drug summaries, download CSV / HTML / PDF dossiers and make data-driven lead decisions in minutes.</div></div></div>
</div>

<div class="cf-hr"></div>

<div class="cf-cta-wrap" style="padding-top:64px">
  <div class="cf-cta">
    <div class="cf-cta-t">Ready to screen your compounds?</div>
    <div class="cf-cta-s">Launch the full ChemoFilter platform — running live on Streamlit Cloud.</div>
"""


_FOOTER_SCRIPT = """
    <div class="cf-chips">
      <span class="cf-chip">RDKit</span><span class="cf-chip">Streamlit</span><span class="cf-chip">Claude AI</span><span class="cf-chip">Plotly 5</span><span class="cf-chip">PubChem API</span><span class="cf-chip">MMFF94</span><span class="cf-chip">Morgan FP</span><span class="cf-chip">Cloudflare D1</span>
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

<button id="cf-thm" onclick="cfToggleTheme()" title="Toggle dark / light">🌙</button>

<script>
(function(){
  var isDark = true;
  window.cfToggleTheme = function(){
    isDark = !isDark;
    var root = document.getElementById('cf-root');
    var nav  = document.getElementById('cf-nav');
    var btn  = document.getElementById('cf-thm');
    if(!isDark){
      root.classList.add('lm');
      if(nav) nav.style.background = 'rgba(250,250,248,0.88)';
      if(btn) btn.innerHTML = '☀️';
    } else {
      root.classList.remove('lm');
      if(nav) nav.style.background = '';
      if(btn) btn.innerHTML = '🌙';
    }
  };
})();
</script>
"""
