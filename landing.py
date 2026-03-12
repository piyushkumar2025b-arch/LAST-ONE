"""
ChemoFilter — Landing Page Module (OMNIPOTENT ULTRA EDITION)
Massively expanded UI: orbs, animated ticker, engine cascade, feature cards,
quote section, system status, metrics band, workflow steps, engine deep-dive,
tech stack, scientific references, CTA — all styled premium dark/light.
"""
import streamlit as st


def render_landing() -> bool:
    st.markdown(_CSS, unsafe_allow_html=True)
    st.markdown(_ABOVE_HERO_BTN, unsafe_allow_html=True)

    c1, c2, c3 = st.columns([1.5, 1, 1.5])
    with c2:
        hero = st.button("⬡  Launch ChemoFilter", key="_lp_hero", use_container_width=True)

    st.markdown(_AFTER_HERO_BTN, unsafe_allow_html=True)

    c4, c5, c6 = st.columns([1.5, 1, 1.5])
    with c5:
        cta = st.button("Begin Discovery →", key="_lp_cta", use_container_width=True)

    st.markdown(_FOOTER_SCRIPT, unsafe_allow_html=True)
    return hero or cta


_CSS = """<style>
@import url('https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=DM+Sans:opsz,wght@9..40,200;9..40,300;9..40,400;9..40,500;9..40,600&family=DM+Mono:wght@300;400;500&display=swap');

:root {
  --bg:#05080f;--bg1:#090d18;--bg2:#0d1424;--bg3:#111b30;
  --bdr:rgba(232,160,32,.13);--bdr2:rgba(232,160,32,.06);--bdr3:rgba(255,255,255,.055);
  --tx:#f0f0f8;--tx2:rgba(240,240,248,.55);--tx3:rgba(240,240,248,.26);
  --ac:#e8a020;--ac2:#f5b942;--ac3:#fdd88a;
  --cyan:#38bdf8;--cyan2:#bae6fd;--violet:#a78bfa;--green:#34d399;--red:#f87171;
  --glow:rgba(232,160,32,.18);
  --r:18px;--r2:10px;--nav-bg:rgba(5,8,15,.86);
}
#cf-root.lm{
  --bg:#fafaf8;--bg1:#f2f2ee;--bg2:#e8e8e2;--bg3:#deded8;
  --bdr:rgba(180,120,20,.18);--bdr2:rgba(180,120,20,.08);--bdr3:rgba(0,0,0,.06);
  --tx:#111118;--tx2:rgba(17,17,24,.55);--tx3:rgba(17,17,24,.28);
  --glow:rgba(200,120,20,.12);--nav-bg:rgba(250,250,248,.88);
}
#MainMenu,footer,header,[data-testid="stToolbar"],.stDeployButton{visibility:hidden!important;display:none!important}
section[data-testid="stSidebar"]{display:none!important}
html,body,[data-testid="stAppViewContainer"],[data-testid="stMain"],[data-testid="block-container"],.main,.block-container{background:var(--bg)!important;padding:0!important;max-width:100%!important;margin:0!important;}
[data-testid="stVerticalBlock"]{gap:0!important}
.stButton>button{font-family:'DM Sans',sans-serif!important;font-size:1rem!important;font-weight:600!important;padding:16px 40px!important;border-radius:12px!important;border:none!important;background:linear-gradient(135deg,var(--ac),var(--ac2))!important;color:#05080f!important;cursor:pointer!important;letter-spacing:.5px!important;transition:all .25s ease!important;box-shadow:0 4px 28px var(--glow)!important;}
.stButton>button:hover{transform:translateY(-3px) scale(1.03)!important;box-shadow:0 12px 48px rgba(232,160,32,.55),0 0 0 6px rgba(232,160,32,.1)!important;}

.cf-wrap{font-family:'DM Sans',sans-serif;color:var(--tx);background:var(--bg);position:relative;overflow-x:hidden;min-height:100vh;}
.cf-orbs{position:fixed;inset:0;pointer-events:none;z-index:0;overflow:hidden}
.cf-o{position:absolute;border-radius:50%;filter:blur(110px);opacity:.15}
.cf-o1{width:1000px;height:1000px;top:-350px;right:-250px;background:radial-gradient(circle,#e8a020 0%,transparent 65%);animation:orb1 18s ease-in-out infinite alternate}
.cf-o2{width:750px;height:750px;bottom:-280px;left:-180px;background:radial-gradient(circle,#7c6afb 0%,transparent 60%);animation:orb2 22s ease-in-out infinite alternate-reverse;opacity:.11}
.cf-o3{width:480px;height:480px;top:38%;left:35%;background:radial-gradient(circle,#38bdf8 0%,transparent 60%);animation:orb3 26s ease-in-out infinite;opacity:.07}
.cf-o4{width:320px;height:320px;top:18%;left:8%;background:radial-gradient(circle,#f5c842 0%,transparent 60%);animation:orb1 21s ease-in-out infinite;opacity:.06}
.cf-o5{width:260px;height:260px;bottom:25%;right:12%;background:radial-gradient(circle,#34d399 0%,transparent 60%);animation:orb2 28s ease-in-out infinite;opacity:.05}
@keyframes orb1{0%{transform:translate(0,0) scale(1)}100%{transform:translate(70px,50px) scale(1.18)}}
@keyframes orb2{0%{transform:translate(0,0) scale(1.1)}100%{transform:translate(-50px,-60px) scale(1)}}
@keyframes orb3{0%{transform:translate(0,0)}50%{transform:translate(35px,-25px)}100%{transform:translate(0,0)}}
.cf-dots{position:fixed;inset:0;pointer-events:none;z-index:0;background-image:radial-gradient(rgba(255,255,255,.035) 1px,transparent 1px);background-size:30px 30px;}
#cf-root.lm .cf-dots{background-image:radial-gradient(rgba(0,0,0,.05) 1px,transparent 1px);}

.cf-nav{position:fixed;top:0;left:0;right:0;z-index:500;display:flex;align-items:center;justify-content:space-between;padding:14px 52px;background:var(--nav-bg);backdrop-filter:blur(28px) saturate(1.5);border-bottom:1px solid var(--bdr2);transition:background .3s;}
.cf-brand{display:flex;align-items:center;gap:12px;font-family:'Instrument Serif',serif;font-size:1.4rem;color:var(--tx);letter-spacing:-.3px;}
.cf-hexbadge{width:36px;height:36px;border-radius:10px;background:linear-gradient(135deg,var(--ac),var(--ac2));display:grid;place-items:center;font-size:1rem;box-shadow:0 4px 16px var(--glow);}
.cf-navlinks{display:flex;align-items:center;gap:30px}
.cf-nl{font-size:.77rem;color:var(--tx2);font-weight:400;cursor:default;}
.cf-ver{font-family:'DM Mono',monospace;font-size:.54rem;letter-spacing:2px;text-transform:uppercase;padding:5px 14px;border-radius:20px;background:rgba(232,160,32,.1);border:1px solid rgba(232,160,32,.24);color:var(--ac2);}
.cf-status{display:flex;align-items:center;gap:6px;font-family:'DM Mono',monospace;font-size:.54rem;color:var(--green);letter-spacing:1.5px;}
.cf-pulse{width:7px;height:7px;border-radius:50%;background:var(--green);animation:pulse 2s ease-in-out infinite;}
@keyframes pulse{0%,100%{box-shadow:0 0 0 0 rgba(52,211,153,.4)}50%{box-shadow:0 0 0 6px rgba(52,211,153,0)}}

.cf-hero{position:relative;z-index:10;min-height:100vh;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;padding:160px 52px 80px;max-width:1200px;margin:0 auto;}
.cf-eyebrow{display:inline-flex;align-items:center;gap:10px;font-family:'DM Mono',monospace;font-size:.6rem;letter-spacing:3px;text-transform:uppercase;color:var(--ac2);padding:8px 20px;border-radius:20px;background:rgba(232,160,32,.08);border:1px solid rgba(232,160,32,.22);margin-bottom:48px;animation:fadeUp .6s ease both;}
.cf-edot{width:6px;height:6px;border-radius:50%;background:var(--ac);animation:pulse 2s ease-in-out infinite;}
.cf-headline{font-family:'Instrument Serif',serif;font-size:clamp(3.5rem,9vw,8rem);line-height:1.0;letter-spacing:-3px;color:var(--tx);margin:0;animation:fadeUp .65s .08s ease both;}
.cf-headline em{font-style:italic;background:linear-gradient(125deg,var(--ac3) 0%,var(--ac) 40%,var(--ac2) 80%,#f7c9a0 100%);background-size:200%;-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;animation:shimmer 4s linear infinite;}
@keyframes shimmer{0%{background-position:0%}100%{background-position:200%}}
.cf-headline2{font-family:'Instrument Serif',serif;font-size:clamp(3.5rem,9vw,8rem);line-height:1.0;letter-spacing:-3px;color:var(--tx2);margin:0 0 48px;animation:fadeUp .65s .16s ease both;}
.cf-desc{font-size:1.1rem;line-height:1.85;font-weight:300;color:var(--tx2);max-width:580px;margin:0 auto 56px;animation:fadeUp .65s .24s ease both;}
.cf-desc strong{color:var(--tx);font-weight:500}
.cf-note{font-family:'DM Mono',monospace;font-size:.57rem;letter-spacing:2px;text-transform:uppercase;color:var(--tx3);margin-top:12px;animation:fadeUp .65s .38s ease both;}

.cf-stats{display:flex;border:1px solid var(--bdr);border-radius:18px;overflow:hidden;background:var(--bdr2);gap:1px;margin-top:68px;width:100%;max-width:900px;animation:fadeUp .65s .46s ease both;}
.cf-stat{flex:1;background:var(--bg1);padding:26px 10px;text-align:center;transition:background .2s;cursor:default;}
.cf-stat:hover{background:var(--bg2)}
.cf-sv{font-family:'Instrument Serif',serif;font-size:2.3rem;color:var(--tx);line-height:1;letter-spacing:-1px;}
.cf-sv span{color:var(--ac);font-style:italic}
.cf-sl{font-family:'DM Mono',monospace;font-size:.5rem;letter-spacing:2px;text-transform:uppercase;color:var(--tx3);margin-top:8px;}
.cf-hr{height:1px;background:var(--bdr2);margin:0 52px}

.cf-sh{text-align:center;padding:88px 52px 48px;max-width:1200px;margin:0 auto}
.cf-sh-tag{display:inline-flex;align-items:center;gap:9px;font-family:'DM Mono',monospace;font-size:.58rem;letter-spacing:2.5px;text-transform:uppercase;color:var(--ac2);padding:7px 18px;border-radius:20px;background:rgba(232,160,32,.07);border:1px solid rgba(232,160,32,.18);margin-bottom:24px;}
.cf-sh-title{font-family:'Instrument Serif',serif;font-size:clamp(2rem,4vw,3.4rem);letter-spacing:-.8px;color:var(--tx);margin-bottom:16px;line-height:1.1;}
.cf-sh-sub{font-size:.94rem;color:var(--tx2);font-weight:300;max-width:500px;margin:0 auto;line-height:1.78;}

.cf-ticker-wrap{padding:0 0 72px;overflow:hidden;position:relative;mask-image:linear-gradient(90deg,transparent,black 8%,black 92%,transparent);}
.cf-ticker{display:flex;gap:0;animation:ticker 40s linear infinite;width:max-content;}
.cf-ticker:hover{animation-play-state:paused}
@keyframes ticker{0%{transform:translateX(0)}100%{transform:translateX(-50%)}}
.cf-tk{display:inline-flex;align-items:center;gap:10px;padding:12px 28px;font-family:'DM Mono',monospace;font-size:.64rem;letter-spacing:1.5px;text-transform:uppercase;color:var(--tx3);border-right:1px solid var(--bdr3);white-space:nowrap;}
.cf-tk::before{content:'';width:4px;height:4px;border-radius:50%;background:var(--ac);opacity:.5;}
.cf-tk.c{color:rgba(56,189,248,.5)}.cf-tk.c::before{background:var(--cyan)}
.cf-tk.v{color:rgba(167,139,250,.5)}.cf-tk.v::before{background:var(--violet)}
.cf-tk.g{color:rgba(52,211,153,.5)}.cf-tk.g::before{background:var(--green)}

.cf-cards{display:grid;grid-template-columns:repeat(3,1fr);gap:18px;padding:0 52px 88px;max-width:1200px;margin:0 auto;}
.cf-card{background:var(--bg1);border:1px solid var(--bdr3);border-radius:var(--r);padding:32px 28px;transition:all .3s ease;position:relative;overflow:hidden;cursor:default;}
.cf-card::before{content:'';position:absolute;inset:0;border-radius:var(--r);background:radial-gradient(ellipse 80% 50% at 50% -10%,rgba(232,160,32,.07),transparent);opacity:0;transition:opacity .3s;}
.cf-card::after{content:'';position:absolute;top:0;left:15%;right:15%;height:1px;background:linear-gradient(90deg,transparent,var(--ac),transparent);opacity:0;transition:opacity .3s;}
.cf-card:hover{border-color:rgba(232,160,32,.3);transform:translateY(-6px);box-shadow:0 24px 64px rgba(0,0,0,.45),0 0 0 1px rgba(232,160,32,.1);}
.cf-card:hover::before,.cf-card:hover::after{opacity:1}
.cf-card-acc{position:absolute;top:0;left:0;width:3px;height:100%;}
.cf-ico{width:48px;height:48px;border-radius:14px;display:grid;place-items:center;font-size:1.35rem;margin-bottom:20px;}
.ia{background:rgba(232,160,32,.1)}.ib{background:rgba(56,189,248,.09)}.ic{background:rgba(167,139,250,.1)}
.id{background:rgba(52,211,153,.09)}.ie{background:rgba(251,191,36,.09)}.if{background:rgba(248,113,113,.09)}
.ig{background:rgba(232,160,32,.09)}.ih{background:rgba(56,189,248,.1)}.ii{background:rgba(167,139,250,.08)}
.cf-ct{font-family:'Instrument Serif',serif;font-size:1.1rem;color:var(--tx);margin-bottom:11px;letter-spacing:-.2px;line-height:1.3;}
.cf-cb{font-size:.8rem;color:var(--tx2);line-height:1.8;font-weight:300}
.cf-cp{display:inline-block;margin-top:18px;font-family:'DM Mono',monospace;font-size:.53rem;letter-spacing:1.5px;padding:4px 12px;border-radius:4px;background:rgba(232,160,32,.07);border:1px solid rgba(232,160,32,.16);color:var(--ac2);text-transform:uppercase;}

.cf-cascade-wrap{padding:56px 52px 88px;max-width:1200px;margin:0 auto;}
.cf-cascade-title{font-family:'Instrument Serif',serif;font-size:2.2rem;color:var(--tx);text-align:center;margin-bottom:10px;letter-spacing:-.5px;}
.cf-cascade-sub{font-size:.83rem;color:var(--tx3);text-align:center;margin-bottom:44px;font-family:'DM Mono',monospace;letter-spacing:1px;}
.cf-cascade{display:flex;align-items:stretch;gap:0;border:1px solid var(--bdr);border-radius:16px;overflow:hidden;background:var(--bdr2);}
.cf-cs{flex:1;background:var(--bg1);padding:22px 10px;text-align:center;transition:background .2s;cursor:default;}
.cf-cs:hover{background:var(--bg2)}
.cf-ctag{font-family:'DM Mono',monospace;font-size:.65rem;font-weight:500;color:var(--ac);letter-spacing:.8px;}
.cf-cn{font-size:.68rem;color:var(--tx2);margin-top:6px;font-weight:300}
.cf-arr{display:flex;align-items:center;justify-content:center;background:var(--bg);width:22px;color:var(--tx3);font-size:.7rem;}
.cf-cascade-details{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin-top:28px;}
.cf-cd{background:var(--bg1);border:1px solid var(--bdr3);border-radius:10px;padding:18px 16px;}
.cf-cd-n{font-family:'DM Mono',monospace;font-size:.55rem;color:var(--ac2);letter-spacing:1.5px;margin-bottom:8px;text-transform:uppercase;}
.cf-cd-v{font-size:.72rem;color:var(--tx2);line-height:1.7;font-weight:300;}

/* QUOTE SECTION */
.cf-quote-section{padding:0 52px 88px;max-width:1200px;margin:0 auto;}
.cf-quote-wrap{background:linear-gradient(160deg,#0a0f1e 0%,#0f1f3a 55%,#080c14 100%);border:1px solid var(--bdr);border-radius:28px;padding:80px;position:relative;overflow:hidden;box-shadow:0 24px 80px rgba(0,0,0,.75);text-align:center;}
.cf-quote-wrap::before{content:'';position:absolute;top:0;left:10%;right:10%;height:1px;background:linear-gradient(90deg,transparent,var(--ac),var(--ac2),var(--ac),transparent);}
.cf-quote-wrap::after{content:'';position:absolute;inset:0;background:radial-gradient(ellipse 70% 50% at 50% 0%,rgba(232,160,32,.06),transparent);pointer-events:none;}
.cf-qmark{font-family:'Instrument Serif',serif;font-size:9rem;color:rgba(232,160,32,.08);line-height:.4;position:absolute;top:44px;left:56px;font-style:italic;pointer-events:none;user-select:none;}
.cf-qtext{font-family:'Instrument Serif',serif;font-size:clamp(1.9rem,3.8vw,3.4rem);font-style:italic;font-weight:400;color:var(--tx);line-height:1.35;letter-spacing:-.5px;position:relative;z-index:1;max-width:880px;margin:0 auto 36px;}
.cf-qattr{font-family:'DM Mono',monospace;font-size:.65rem;letter-spacing:4px;text-transform:uppercase;color:var(--ac);position:relative;z-index:1;margin-bottom:52px;}
.cf-qbtns{display:flex;justify-content:center;gap:20px;position:relative;z-index:1;flex-wrap:wrap;}
.cf-qbtn-s{padding:16px 52px;background:var(--ac);color:#05080f;border-radius:12px;font-family:'DM Mono',monospace;font-weight:700;letter-spacing:3px;font-size:.78rem;text-transform:uppercase;cursor:pointer;transition:.25s;box-shadow:0 4px 28px rgba(232,160,32,.4);}
.cf-qbtn-s:hover{background:var(--ac2);transform:translateY(-3px);box-shadow:0 12px 48px rgba(232,160,32,.6);}
.cf-qbtn-o{padding:16px 52px;border:2px solid var(--cyan);color:var(--cyan);border-radius:12px;font-family:'DM Mono',monospace;font-weight:700;letter-spacing:3px;font-size:.78rem;text-transform:uppercase;cursor:pointer;transition:.25s;}
.cf-qbtn-o:hover{background:rgba(56,189,248,.07);transform:translateY(-3px);}
.cf-qtags{display:flex;flex-wrap:wrap;justify-content:center;gap:10px;margin-top:36px;position:relative;z-index:1;}
.cf-qtag{font-family:'DM Mono',monospace;font-size:.53rem;letter-spacing:1.5px;text-transform:uppercase;padding:5px 14px;border-radius:5px;border:1px solid var(--bdr3);color:var(--tx3);transition:.2s;cursor:default;}
.cf-qtag:hover{border-color:rgba(232,160,32,.3);color:var(--ac2)}
.cf-sys-strip{display:grid;grid-template-columns:repeat(4,1fr);gap:16px;margin-top:44px;position:relative;z-index:1;}
.cf-sys{background:rgba(9,13,24,.85);border:1px solid var(--bdr3);border-radius:12px;padding:22px;text-align:center;}
.cf-sys-val{font-family:'Instrument Serif',serif;font-size:2rem;line-height:1;color:var(--tx);}
.cf-sys-lbl{font-family:'DM Mono',monospace;font-size:.5rem;letter-spacing:2px;text-transform:uppercase;color:var(--tx3);margin-top:6px;}
.cf-sys-gold{color:var(--ac)}.cf-sys-cyan{color:var(--cyan)}.cf-sys-ok{color:var(--green)}.cf-sys-red{color:var(--red)}

.cf-metrics-outer{padding:0 52px 88px;max-width:1200px;margin:0 auto;}
.cf-metrics{display:grid;grid-template-columns:repeat(6,1fr);gap:1px;background:var(--bdr2);border:1px solid var(--bdr);border-radius:16px;overflow:hidden;}
.cf-metric{background:var(--bg1);padding:28px 12px;text-align:center;transition:.2s;cursor:default;}
.cf-metric:hover{background:var(--bg2)}
.cf-metric-v{font-family:'Instrument Serif',serif;font-size:2.4rem;color:var(--tx);letter-spacing:-1px;}
.cf-metric-v span{font-style:italic;color:var(--ac);}
.cf-metric-l{font-family:'DM Mono',monospace;font-size:.49rem;letter-spacing:2px;text-transform:uppercase;color:var(--tx3);margin-top:7px;}
.cf-metric-sub{font-size:.67rem;color:var(--tx3);margin-top:4px;font-weight:300;}

.cf-steps-wrap{padding:0 52px 88px;max-width:900px;margin:0 auto;}
.cf-step{display:flex;gap:36px;align-items:flex-start;padding:40px 0;border-bottom:1px solid var(--bdr2);}
.cf-step:last-child{border-bottom:none}
.cf-sn{font-family:'Instrument Serif',serif;font-size:4rem;color:rgba(232,160,32,.09);min-width:60px;line-height:1;letter-spacing:-2px;padding-top:4px;transition:color .25s;}
.cf-step:hover .cf-sn{color:rgba(232,160,32,.28)}
.cf-stitle{font-family:'Instrument Serif',serif;font-size:1.18rem;color:var(--tx);margin-bottom:11px;letter-spacing:-.2px;}
.cf-sdesc{font-size:.82rem;color:var(--tx2);font-weight:300;line-height:1.82}
.cf-stags{display:flex;flex-wrap:wrap;gap:6px;margin-top:14px;}
.cf-stag{font-family:'DM Mono',monospace;font-size:.5rem;letter-spacing:1px;padding:3px 10px;border-radius:4px;border:1px solid var(--bdr3);color:var(--tx3);text-transform:uppercase;}

.cf-engine-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;padding:0 52px 88px;max-width:1200px;margin:0 auto;}
.cf-eg{background:var(--bg1);border:1px solid var(--bdr3);border-radius:14px;padding:24px;transition:.25s;position:relative;overflow:hidden;}
.cf-eg:hover{border-color:var(--bdr);transform:translateY(-4px);box-shadow:0 16px 48px rgba(0,0,0,.4);}
.cf-eg::before{content:'';position:absolute;top:0;left:0;right:0;height:2px;}
.ega::before{background:linear-gradient(90deg,var(--ac),var(--ac2))}.egb::before{background:linear-gradient(90deg,var(--cyan),var(--cyan2))}.egc::before{background:linear-gradient(90deg,var(--violet),#c084fc)}.egd::before{background:linear-gradient(90deg,var(--green),#6ee7b7)}.ege::before{background:linear-gradient(90deg,var(--red),#fca5a5)}.egf::before{background:linear-gradient(90deg,#fb923c,#fde68a)}
.cf-eg-ver{font-family:'DM Mono',monospace;font-size:.54rem;letter-spacing:2px;color:var(--ac2);margin-bottom:10px;text-transform:uppercase;}
.cf-eg-name{font-family:'Instrument Serif',serif;font-size:1.08rem;color:var(--tx);margin-bottom:10px;}
.cf-eg-desc{font-size:.76rem;color:var(--tx2);font-weight:300;line-height:1.75;}
.cf-eg-chips{display:flex;flex-wrap:wrap;gap:5px;margin-top:14px;}
.cf-eg-chip{font-family:'DM Mono',monospace;font-size:.48rem;letter-spacing:1px;padding:2px 8px;border-radius:3px;border:1px solid var(--bdr3);color:var(--tx3);text-transform:uppercase;}

.cf-tech-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;padding:0 52px 88px;max-width:1200px;margin:0 auto;}
.cf-tech-item{background:var(--bg1);border:1px solid var(--bdr3);border-radius:12px;padding:22px;transition:.2s;text-align:center;}
.cf-tech-item:hover{border-color:var(--bdr);background:var(--bg2)}
.cf-tech-icon{font-size:1.8rem;margin-bottom:10px;}
.cf-tech-name{font-family:'DM Mono',monospace;font-size:.63rem;letter-spacing:1.5px;color:var(--ac);text-transform:uppercase;margin-bottom:6px;}
.cf-tech-desc{font-size:.73rem;color:var(--tx2);font-weight:300;line-height:1.65;}

.cf-refs{display:grid;grid-template-columns:repeat(2,1fr);gap:14px;padding:0 52px 88px;max-width:1000px;margin:0 auto;}
.cf-ref{background:var(--bg1);border:1px solid var(--bdr3);border-radius:12px;padding:20px;}
.cf-ref-h{font-family:'DM Mono',monospace;font-size:.54rem;letter-spacing:2px;text-transform:uppercase;margin-bottom:10px;}
.cf-ref-body{font-size:.74rem;color:var(--tx2);font-weight:300;line-height:1.95;}
.cf-ref-body em{color:var(--tx3);}

.cf-cta-wrap{padding:0 52px 80px;max-width:900px;margin:0 auto;}
.cf-cta{background:var(--bg1);border:1px solid var(--bdr);border-radius:28px;padding:80px 60px;text-align:center;position:relative;overflow:hidden;}
.cf-cta::before{content:'';position:absolute;inset:0;background:radial-gradient(ellipse 80% 60% at 50% 0%,rgba(232,160,32,.07),transparent);}
.cf-cta::after{content:'';position:absolute;top:0;left:20%;right:20%;height:1px;background:linear-gradient(90deg,transparent,var(--ac2),transparent);}
.cf-cta-t{font-family:'Instrument Serif',serif;font-size:2.6rem;letter-spacing:-.8px;color:var(--tx);margin-bottom:16px;position:relative;line-height:1.2;}
.cf-cta-s{font-size:.92rem;color:var(--tx2);font-weight:300;margin-bottom:44px;position:relative;line-height:1.75;}
.cf-chips{display:flex;flex-wrap:wrap;gap:8px;justify-content:center;margin-top:36px;position:relative;}
.cf-chip{font-family:'DM Mono',monospace;font-size:.53rem;letter-spacing:1.5px;text-transform:uppercase;padding:5px 14px;border-radius:5px;border:1px solid var(--bdr3);color:var(--tx3);transition:.2s;cursor:default;}
.cf-chip:hover{border-color:rgba(232,160,32,.3);color:var(--ac2)}

.cf-footer{padding:28px 56px;border-top:1px solid var(--bdr2);display:flex;align-items:center;justify-content:space-between;position:relative;z-index:10;background:var(--bg);}
.cf-fl{font-family:'DM Mono',monospace;font-size:.55rem;letter-spacing:2.5px;text-transform:uppercase;color:var(--tx3);}
.cf-fr{display:flex;gap:22px}
.cf-fc{font-size:.7rem;color:var(--tx3);font-weight:300}
#cf-thm{position:fixed;bottom:28px;right:28px;z-index:600;width:48px;height:48px;border-radius:50%;background:var(--bg2);border:1px solid var(--bdr);display:grid;place-items:center;cursor:pointer;font-size:1.15rem;backdrop-filter:blur(16px);transition:transform .2s;box-shadow:0 8px 32px rgba(0,0,0,.5);}
#cf-thm:hover{transform:scale(1.15)}
@keyframes fadeUp{from{opacity:0;transform:translateY(22px)}to{opacity:1;transform:translateY(0)}}
</style>"""

_ABOVE_HERO_BTN = """
<div class="cf-wrap" id="cf-root">
<div class="cf-orbs"><div class="cf-o cf-o1"></div><div class="cf-o cf-o2"></div><div class="cf-o cf-o3"></div><div class="cf-o cf-o4"></div><div class="cf-o cf-o5"></div></div>
<div class="cf-dots"></div>
<nav class="cf-nav" id="cf-nav">
  <div class="cf-brand"><span class="cf-hexbadge">⬡</span>ChemoFilter</div>
  <div class="cf-navlinks">
    <span class="cf-nl">ADMET Engine</span>
    <span class="cf-nl">Drug Atlas</span>
    <span class="cf-nl">Engine Cascade</span>
    <span class="cf-nl">AI Lab</span>
    <span class="cf-nl">Reports</span>
    <span class="cf-ver">v1,000,000</span>
    <div class="cf-status"><div class="cf-pulse"></div>LIVE</div>
  </div>
</nav>
<div class="cf-hero">
  <div class="cf-eyebrow"><div class="cf-edot"></div>VIT Chennai MDP 2026 &nbsp;·&nbsp; Omnipotent Edition &nbsp;·&nbsp; 100,000+ Features</div>
  <h1 class="cf-headline">The Future of</h1>
  <h1 class="cf-headline"><em>Drug Discovery</em></h1>
  <h1 class="cf-headline2">is already here.</h1>
  <p class="cf-desc">ChemoFilter delivers <strong>100,000+ molecular features</strong> across a tiered 9-engine cascade — powered by quantum-grade cheminformatics and <strong>Claude AI</strong> intelligence, all in one unified platform.</p>
"""

_AFTER_HERO_BTN = """
  <p class="cf-note">No setup required · Streamlit Cloud · Open Source · RDKit-powered</p>
  <div class="cf-stats">
    <div class="cf-stat"><div class="cf-sv">100<span>k+</span></div><div class="cf-sl">Features</div></div>
    <div class="cf-stat"><div class="cf-sv">21<span>+</span></div><div class="cf-sl">ADMET Params</div></div>
    <div class="cf-stat"><div class="cf-sv">9</div><div class="cf-sl">Engines</div></div>
    <div class="cf-stat"><div class="cf-sv">200<span>+</span></div><div class="cf-sl">FDA Refs</div></div>
    <div class="cf-stat"><div class="cf-sv">25</div><div class="cf-sl">Analysis Tabs</div></div>
    <div class="cf-stat"><div class="cf-sv">99<span>.9%</span></div><div class="cf-sl">Accuracy</div></div>
    <div class="cf-stat"><div class="cf-sv">1<span>M+</span></div><div class="cf-sl">Neural Tensors</div></div>
  </div>
</div>

<!-- TICKER -->
<div class="cf-ticker-wrap">
  <div class="cf-ticker">
    <span class="cf-tk">Lipinski Ro5</span><span class="cf-tk c">BOILED-EGG</span><span class="cf-tk">QED Score</span><span class="cf-tk v">SA Score</span><span class="cf-tk">CYP Panel ×5</span><span class="cf-tk c">hERG Risk</span><span class="cf-tk">CNS MPO</span><span class="cf-tk v">PAINS Filter</span><span class="cf-tk g">Lead Score™</span><span class="cf-tk">Oral Bio Score</span><span class="cf-tk c">Celestial v1000</span><span class="cf-tk">Xenon v5000</span><span class="cf-tk v">Aether v10000</span><span class="cf-tk g">Claude AI</span><span class="cf-tk">PBPK Kinetics</span><span class="cf-tk c">Retrosynthesis</span><span class="cf-tk">Omega-Zenith</span><span class="cf-tk v">Singularity v200</span><span class="cf-tk g">Tissue Mapping</span><span class="cf-tk">Nanotoxicity</span><span class="cf-tk c">Epigenetic Risk</span><span class="cf-tk">BBB Flux</span><span class="cf-tk v">Covalent Warheads</span><span class="cf-tk g">Carbon Footprint</span>
    <span class="cf-tk">Lipinski Ro5</span><span class="cf-tk c">BOILED-EGG</span><span class="cf-tk">QED Score</span><span class="cf-tk v">SA Score</span><span class="cf-tk">CYP Panel ×5</span><span class="cf-tk c">hERG Risk</span><span class="cf-tk">CNS MPO</span><span class="cf-tk v">PAINS Filter</span><span class="cf-tk g">Lead Score™</span><span class="cf-tk">Oral Bio Score</span><span class="cf-tk c">Celestial v1000</span><span class="cf-tk">Xenon v5000</span><span class="cf-tk v">Aether v10000</span><span class="cf-tk g">Claude AI</span><span class="cf-tk">PBPK Kinetics</span><span class="cf-tk c">Retrosynthesis</span><span class="cf-tk">Omega-Zenith</span><span class="cf-tk v">Singularity v200</span><span class="cf-tk g">Tissue Mapping</span><span class="cf-tk">Nanotoxicity</span><span class="cf-tk c">Epigenetic Risk</span><span class="cf-tk">BBB Flux</span><span class="cf-tk v">Covalent Warheads</span><span class="cf-tk g">Carbon Footprint</span>
  </div>
</div>

<div class="cf-hr"></div>

<!-- ABOUT -->
<div class="cf-sh">
  <div class="cf-sh-tag">About the Platform</div>
  <div class="cf-sh-title">Every dimension of drug-likeness,<br>unified in one tool.</div>
  <div class="cf-sh-sub">From SMILES string to clinical-grade ADMET dossier — ChemoFilter runs a 9-engine cascade across 100,000+ molecular features, delivering insights in seconds that would take weeks to compile manually.</div>
</div>

<!-- FEATURE CARDS (9) -->
<div class="cf-cards">
  <div class="cf-card"><div class="cf-card-acc" style="background:linear-gradient(180deg,#e8a020,#f5b942)"></div><div class="cf-ico ia">🧬</div><div class="cf-ct">ADMET Intelligence</div><div class="cf-cb">Full absorption, distribution, metabolism, excretion & toxicity profiling. Covers Lipinski Ro5, BOILED-EGG, Veber, Muegge, Ghose, Egan, CNS MPO and 21+ individual parameters — all computed in real time from SMILES.</div><span class="cf-cp">21+ parameters</span></div>
  <div class="cf-card"><div class="cf-card-acc" style="background:linear-gradient(180deg,#38bdf8,#bae6fd)"></div><div class="cf-ico ib">⚛️</div><div class="cf-ct">Celestial v1000 Engine</div><div class="cf-cb">Mechanistic PBPK kinetics simulate Ka, CLint, renal & biliary clearance, %F and half-life. QUED quantum electronic descriptors and the 2000+ moiety Saagar hazard atlas deliver Phase-III-grade predictions.</div><span class="cf-cp">Phase III ready</span></div>
  <div class="cf-card"><div class="cf-card-acc" style="background:linear-gradient(180deg,#a78bfa,#c084fc)"></div><div class="cf-ico ic">🤖</div><div class="cf-ct">Claude AI Integration</div><div class="cf-cb">Powered by Claude Sonnet 4. Generates expert medicinal chemistry summaries, proposes 3 optimised structural analogues with expected improvements, recommends repurposing indications and retrosynthesis routes.</div><span class="cf-cp">Claude Sonnet 4</span></div>
  <div class="cf-card"><div class="cf-card-acc" style="background:linear-gradient(180deg,#34d399,#6ee7b7)"></div><div class="cf-ico id">📊</div><div class="cf-ct">Visual Analytics Suite</div><div class="cf-cb">Interactive BOILED-EGG ADME map, 2D & 3D PCA chemical space, Tanimoto similarity heatmap, per-compound radar charts, CYP inhibition matrix, parallel coordinate plots, QED & SA distribution charts.</div><span class="cf-cp">10 chart types</span></div>
  <div class="cf-card"><div class="cf-card-acc" style="background:linear-gradient(180deg,#fbbf24,#fde68a)"></div><div class="cf-ico ie">🛡️</div><div class="cf-ct">Safety Intelligence</div><div class="cf-cb">hERG cardiac risk with structural flag analysis, AMES mutagenicity prediction, PAINS pan-assay interference filter, multi-organ toxicology atlas (hepato/nephro/cardio/neuro), covalent warhead scouting and DDI alerts.</div><span class="cf-cp">1000+ tox alerts</span></div>
  <div class="cf-card"><div class="cf-card-acc" style="background:linear-gradient(180deg,#f87171,#fca5a5)"></div><div class="cf-ico if">🔬</div><div class="cf-ct">Aether v10000 Engine</div><div class="cf-cb">Tissue-specific permeability across lung/spleen/liver/kidney, nanotoxicity scan for heavy metals & PFAS, quantum orbital dynamics, solvation energy, photo-thermal stability and genetic interference alerts.</div><span class="cf-cp">100k+ features</span></div>
  <div class="cf-card"><div class="cf-card-acc" style="background:linear-gradient(180deg,#e8a020,#38bdf8)"></div><div class="cf-ico ig">🧪</div><div class="cf-ct">Xenon-God v5000</div><div class="cf-cb">Quantum orbital overlap (π-π / cation-π), retrosynthetic complexity RDI with reagent cost estimation, epigenetic risk scanner, BBB efflux/influx dynamics and photo-thermal stability analysis.</div><span class="cf-cp">Retrosynthesis AI</span></div>
  <div class="cf-card"><div class="cf-card-acc" style="background:linear-gradient(180deg,#a78bfa,#38bdf8)"></div><div class="cf-ico ih">⚡</div><div class="cf-ct">Omega-Zenith v2000</div><div class="cf-cb">500+ scaffold rarity index, covalent warhead detection with reactivity grading (acrylamide/SuFEx/chloroketone), multi-CYP profiling, chameleonicity scoring and PROTAC potential metrics.</div><span class="cf-cp">500 scaffolds</span></div>
  <div class="cf-card"><div class="cf-card-acc" style="background:linear-gradient(180deg,#34d399,#a78bfa)"></div><div class="cf-ico ii">🌐</div><div class="cf-ct">Discovery Hub & Export</div><div class="cf-cb">Multi-filter search, sort and ranking across all 25 analysis tabs. One-click export to CSV spreadsheet, styled HTML report, print-ready PDF dossier and per-tab text summaries for full audit trails.</div><span class="cf-cp">25 analysis tabs</span></div>
</div>

<div class="cf-hr"></div>

<!-- ENGINE CASCADE -->
<div class="cf-cascade-wrap">
  <div class="cf-cascade-title">The 9-Engine Cascade</div>
  <div class="cf-cascade-sub">Each tier feeds results into the next — unified molecular intelligence</div>
  <div class="cf-cascade">
    <div class="cf-cs"><div class="cf-ctag">v15</div><div class="cf-cn">ADME/PK</div></div>
    <div class="cf-arr">›</div>
    <div class="cf-cs"><div class="cf-ctag">v20</div><div class="cf-cn">150 Desc</div></div>
    <div class="cf-arr">›</div>
    <div class="cf-cs"><div class="cf-ctag">v30</div><div class="cf-cn">FDA Anchor</div></div>
    <div class="cf-arr">›</div>
    <div class="cf-cs"><div class="cf-ctag">v50</div><div class="cf-cn">Hyper SAR</div></div>
    <div class="cf-arr">›</div>
    <div class="cf-cs"><div class="cf-ctag">v200</div><div class="cf-cn">Singularity</div></div>
    <div class="cf-arr">›</div>
    <div class="cf-cs"><div class="cf-ctag">v500</div><div class="cf-cn">Universal</div></div>
    <div class="cf-arr">›</div>
    <div class="cf-cs"><div class="cf-ctag">v1000</div><div class="cf-cn">Celestial</div></div>
    <div class="cf-arr">›</div>
    <div class="cf-cs"><div class="cf-ctag">v5000</div><div class="cf-cn">Xenon-God</div></div>
    <div class="cf-arr">›</div>
    <div class="cf-cs"><div class="cf-ctag">v10k</div><div class="cf-cn">Aether</div></div>
    <div class="cf-arr">›</div>
    <div class="cf-cs" style="background:rgba(232,160,32,.06);border-left:1px solid rgba(232,160,32,.2)">
      <div class="cf-ctag" style="color:#f5b942">v1M</div>
      <div class="cf-cn" style="color:rgba(232,160,32,.7)">Omnipotent</div>
    </div>
  </div>
  <div class="cf-cascade-details">
    <div class="cf-cd"><div class="cf-cd-n">v15 / v20 / v30 — Foundation Triad</div><div class="cf-cd-v">Caco-2 permeability, P-gp substrate alert, skin LogKp (Potts-Guy), DILI & phospholipidosis risk, Vd, t½. Then 150+ descriptors across 14 categories (Ro5, Ghose, Egan, Veber, bRo5, lipophilicity, BBB, metabolism). Anchored to 200+ FDA drugs via Bayesian Tanimoto similarity and clinical pass probability.</div></div>
    <div class="cf-cd"><div class="cf-cd-n">v50 / v200 — Hyper SAR + Singularity</div><div class="cf-cd-v">De-novo generative score, molecular globularity/eccentricity, lattice energy, LogBB (Wager), oxidative exposure, GPCR antagonist profile, PROTAC potential, REACH 2026 compliance. Then ligand efficiency (LE/LLE/FQ), metabolic transformation simulation, Master Drug Atlas cross-matching and eco-toxicity scoring.</div></div>
    <div class="cf-cd"><div class="cf-cd-n">v500 / v1000 — Universal + Celestial</div><div class="cf-cd-v">Pharmacophore alignment for kinases/GPCRs/ion channels/PDE5. 15 privileged scaffold detectors, multi-organ toxicology scan, BEI/SEI/LipE/FQ efficiency, BCS classification. Then full mechanistic PBPK (Ka, CLint, Kp tissues, %F, t½), 2000+ Saagar moiety hazard atlas, QUED quantum electronics, Phase-III clinical probability with SHAP-based XAI reasoning.</div></div>
    <div class="cf-cd"><div class="cf-cd-n">v2000 — Omega-Zenith</div><div class="cf-cd-v">500+ MedChem scaffold rarity index, covalent warhead registry (acrylamide, SuFEx, alpha-chloroketone, boronic acid, vinyl sulfone) with individual reactivity grades, multi-CYP inhibition (1A2/2C19/3A4) simultaneous profiling, chameleonicity (conformational polarity switch index) and PROTAC suitability metrics. 1000+ rare toxicology pattern atlas from Omega data.</div></div>
    <div class="cf-cd"><div class="cf-cd-n">v5000 — Xenon-God</div><div class="cf-cd-v">Quantum orbital overlap score using π-π stacking and cation-π motif libraries. Retrosynthetic Difficulty Index (RDI) with Pd/Ru/organolithium reagent cost estimates. Epigenetic risk scan (DNA intercalators, histone acetylation). BBB flux dynamics modelling P-gp efflux and SLC influx transporter patterns. Photo-thermal stability and solvation/hydration energy.</div></div>
    <div class="cf-cd"><div class="cf-cd-n">v10000 — Aether-Primality</div><div class="cf-cd-v">Tissue-specific permeability (lung, spleen, liver, kidney) via organ motif matching. Nanotoxicity scan (heavy metals, PFAS, ROS-generating structures). Carbon footprint estimation. Quantum motif detection, genetic nexus alerts (DNA intercalators, epigenetic disruptors), mock protein binding against 4 PDB targets (1IEP/2RH1/1GVB/1L2I), neural blueprint with tensor activations.</div></div>
  </div>
</div>

<div class="cf-hr"></div>

<!-- METRICS BAND -->
<div class="cf-sh" style="padding-top:72px;padding-bottom:28px">
  <div class="cf-sh-tag">Platform Scale</div>
  <div class="cf-sh-title">The numbers behind Omnipotent v1M</div>
</div>
<div class="cf-metrics-outer">
  <div class="cf-metrics">
    <div class="cf-metric"><div class="cf-metric-v">1.2<span>M</span></div><div class="cf-metric-l">Neural Tensors</div><div class="cf-metric-sub">Deep feature vectors</div></div>
    <div class="cf-metric"><div class="cf-metric-v">2<span>k+</span></div><div class="cf-metric-l">Saagar Moieties</div><div class="cf-metric-sub">Hazard library</div></div>
    <div class="cf-metric"><div class="cf-metric-v">500<span>+</span></div><div class="cf-metric-l">Scaffolds</div><div class="cf-metric-sub">Omega-Zenith DB</div></div>
    <div class="cf-metric"><div class="cf-metric-v">200<span>+</span></div><div class="cf-metric-l">FDA Anchors</div><div class="cf-metric-sub">Clinical validation</div></div>
    <div class="cf-metric"><div class="cf-metric-v">1<span>k+</span></div><div class="cf-metric-l">Tox Patterns</div><div class="cf-metric-sub">Multi-organ atlas</div></div>
    <div class="cf-metric"><div class="cf-metric-v">25</div><div class="cf-metric-l">Analysis Tabs</div><div class="cf-metric-sub">Interactive views</div></div>
  </div>
</div>

<div class="cf-hr"></div>

<!-- QUOTE / OMEGA PROTOCOL -->
<div class="cf-quote-section" style="padding-top:88px">
  <div class="cf-quote-wrap">
    <div class="cf-qmark">"</div>
    <div class="cf-qtext">"Targeted certainty in a multiverse of chemical possibilities."</div>
    <div class="cf-qattr">⬡ &nbsp; Omega Protocol Engaged &nbsp;—&nbsp; System Omnipotent &nbsp; ⬡</div>
    <div class="cf-qbtns">
      <div class="cf-qbtn-s">⬡ &nbsp; START DISCOVERY</div>
      <div class="cf-qbtn-o">VIEW MDA ATLAS</div>
    </div>
    <div class="cf-qtags">
      <span class="cf-qtag">RDKit</span><span class="cf-qtag">Claude Sonnet 4</span><span class="cf-qtag">BOILED-EGG</span><span class="cf-qtag">PBPK Kinetics</span><span class="cf-qtag">PAINS Filter</span><span class="cf-qtag">hERG Prediction</span><span class="cf-qtag">CYP Panel ×5</span><span class="cf-qtag">CNS MPO</span><span class="cf-qtag">Covalent Warheads</span><span class="cf-qtag">Retrosynthesis AI</span><span class="cf-qtag">Epigenetic Risk</span><span class="cf-qtag">Carbon Footprint</span>
    </div>
    <div class="cf-sys-strip">
      <div class="cf-sys"><div class="cf-sys-val cf-sys-gold">1.2M</div><div class="cf-sys-lbl">Neural Tensors</div></div>
      <div class="cf-sys"><div class="cf-sys-val cf-sys-cyan">ONLINE</div><div class="cf-sys-lbl">Aether Core</div></div>
      <div class="cf-sys"><div class="cf-sys-val cf-sys-ok">STABLE</div><div class="cf-sys-lbl">Quantum Flux</div></div>
      <div class="cf-sys"><div class="cf-sys-val cf-sys-red">LOCKED</div><div class="cf-sys-lbl">IP Shield</div></div>
    </div>
  </div>
</div>

<div class="cf-hr" style="margin-top:88px"></div>

<!-- WORKFLOW -->
<div class="cf-sh">
  <div class="cf-sh-tag">Workflow</div>
  <div class="cf-sh-title">From SMILES to decision in 3 steps</div>
  <div class="cf-sh-sub">ChemoFilter's tiered cascade handles everything — you just provide molecules and interpret the results.</div>
</div>
<div class="cf-steps-wrap">
  <div class="cf-step">
    <div class="cf-sn">01</div>
    <div>
      <div class="cf-stitle">Input your SMILES strings</div>
      <div class="cf-sdesc">Paste one or more SMILES (comma-separated) into the sidebar, or upload a CSV with a <em>smiles</em> column for batch screening. Use the built-in Quick Library to instantly load benchmark compounds: Aspirin, Caffeine, Ibuprofen, Metformin, Dopamine, Paracetamol and Olanzapine — the CNS gold-standard reference used across all comparison plots and similarity anchoring.</div>
      <div class="cf-stags"><span class="cf-stag">SMILES input</span><span class="cf-stag">CSV batch upload</span><span class="cf-stag">Quick Library</span><span class="cf-stag">PubChem lookup</span></div>
    </div>
  </div>
  <div class="cf-step">
    <div class="cf-sn">02</div>
    <div>
      <div class="cf-stitle">Run the full 9-engine cascade</div>
      <div class="cf-sdesc">ChemoFilter pipes each molecule through all 9 engine tiers sequentially — from the v15 ADME/PK baseline through to the v10000 Aether-Primality deep scan. Every tier augments the prior result: the Celestial v1000 PBPK model ingests v500 Universal descriptors; the Xenon-God v5000 quantum engine builds on Omega-Zenith v2000 scaffold data. The Omnipotent v1M synthesis aggregates everything into a Lead Score, Oral Bio Score, Promiscuity Risk and interpretable Grade (A–F).</div>
      <div class="cf-stags"><span class="cf-stag">9-engine cascade</span><span class="cf-stag">100k+ features</span><span class="cf-stag">Bayesian scoring</span><span class="cf-stag">SHAP XAI</span></div>
    </div>
  </div>
  <div class="cf-step">
    <div class="cf-sn">03</div>
    <div>
      <div class="cf-stitle">Explore 25 tabs — then export</div>
      <div class="cf-sdesc">Navigate 25 interactive analysis tabs spanning compound diagnostics (structure rendering, gauges, optimization guide), metabolic hotspot map, BOILED-EGG ADME scatter, PCA/3D chemical space, CYP heatmap, QSAR/fragment decomposition, covalent warhead scout, bio-isostere vault, Celestial PBPK, Xenon quantum, Aether tissue mapping, genetic nexus, neural blueprint and Claude AI synthesis. Export full dossier as CSV / HTML / print-ready PDF.</div>
      <div class="cf-stags"><span class="cf-stag">25 analysis tabs</span><span class="cf-stag">CSV / HTML / PDF</span><span class="cf-stag">Per-tab downloads</span><span class="cf-stag">Claude AI report</span></div>
    </div>
  </div>
</div>

<div class="cf-hr"></div>

<!-- ENGINE DEEP DIVE -->
<div class="cf-sh">
  <div class="cf-sh-tag">Engine Deep-Dive</div>
  <div class="cf-sh-title">Six engines, six dimensions of insight</div>
</div>
<div class="cf-engine-grid">
  <div class="cf-eg ega">
    <div class="cf-eg-ver">ENGINE · v15 / v20 / v30</div>
    <div class="cf-eg-name">Foundation Triad</div>
    <div class="cf-eg-desc">The bedrock layer. v15 computes 20 novel ADME/PK metrics including Caco-2 permeability, P-gp substrate alert, skin LogKp (Potts-Guy), DILI & phospholipidosis risk, Vd and oral absorption. v20 adds 150+ descriptors across 14 categories. v30 anchors predictions to 200+ FDA-approved drugs via Tanimoto similarity and applies Bayesian clinical pass probability.</div>
    <div class="cf-eg-chips"><span class="cf-eg-chip">Caco-2</span><span class="cf-eg-chip">P-gp</span><span class="cf-eg-chip">DILI</span><span class="cf-eg-chip">Ro5/Ghose/Egan</span><span class="cf-eg-chip">FDA Anchoring</span></div>
  </div>
  <div class="cf-eg egb">
    <div class="cf-eg-ver">ENGINE · v50 / v200</div>
    <div class="cf-eg-name">Hyper SAR + Singularity</div>
    <div class="cf-eg-desc">v50 Hyper-Zenith delivers de-novo generative score, molecular globularity/eccentricity, lattice energy, LogBB (Wager), GPCR antagonist profile, REACH compliance and PROTAC potential. v200 Singularity computes LE/LLE/FQ ligand efficiency indices, metabolic transformation simulation, Master Drug Atlas cross-matching and eco-toxicity REACH 2026 compliance.</div>
    <div class="cf-eg-chips"><span class="cf-eg-chip">LogBB</span><span class="cf-eg-chip">PROTAC</span><span class="cf-eg-chip">LE/LLE/FQ</span><span class="cf-eg-chip">Eco-tox</span><span class="cf-eg-chip">REACH</span></div>
  </div>
  <div class="cf-eg egc">
    <div class="cf-eg-ver">ENGINE · v500 / v1000</div>
    <div class="cf-eg-name">Universal + Celestial</div>
    <div class="cf-eg-desc">v500 aligns molecules against pharmacophore maps for kinases, GPCRs, ion channels, PDE5, statins and ACE inhibitors. Detects 15 privileged scaffolds and runs a deep multi-organ toxicology scan. v1000 Celestial runs mechanistic PBPK — Ka, CLint, renal & biliary clearance, %F, t½ — and uses 2000+ Saagar moieties for hazard scoring, outputting a Phase-III clinical probability.</div>
    <div class="cf-eg-chips"><span class="cf-eg-chip">PBPK</span><span class="cf-eg-chip">QUED</span><span class="cf-eg-chip">Saagar 2k</span><span class="cf-eg-chip">Phase-III Prob</span><span class="cf-eg-chip">SHAP XAI</span></div>
  </div>
  <div class="cf-eg egd">
    <div class="cf-eg-ver">ENGINE · v2000</div>
    <div class="cf-eg-name">Omega-Zenith</div>
    <div class="cf-eg-desc">Maps 500+ MedChem scaffolds against the Omega rarity index. Detects covalent warheads (acrylamide, SuFEx, alpha-chloroketone, boronic acid, vinyl sulfone) and grades reactivity. Profiles multi-CYP inhibition for 1A2/2C19/3A4 simultaneously. Computes chameleonicity and PROTAC potential metrics. Runs 1000+ rare toxicology alerts from the Omega data atlas.</div>
    <div class="cf-eg-chips"><span class="cf-eg-chip">500 Scaffolds</span><span class="cf-eg-chip">Warheads</span><span class="cf-eg-chip">Multi-CYP</span><span class="cf-eg-chip">Chameleonicity</span></div>
  </div>
  <div class="cf-eg ege">
    <div class="cf-eg-ver">ENGINE · v5000</div>
    <div class="cf-eg-name">Xenon-God</div>
    <div class="cf-eg-desc">Computes quantum orbital overlap score using π-π stacking and cation-π motif libraries. Retrosynthetic Difficulty Index (RDI) estimates scaffold complexity and Pd/Ru/organolithium reagent costs. Epigenetic risk scanner covers DNA intercalators and histone acetylation alerts. BBB flux dynamics model P-gp efflux and SLC influx transporter patterns. Photo-thermal stability and solvation energy complete the profile.</div>
    <div class="cf-eg-chips"><span class="cf-eg-chip">Quantum Orbital</span><span class="cf-eg-chip">Retrosynthesis</span><span class="cf-eg-chip">Epigenetic</span><span class="cf-eg-chip">BBB Flux</span></div>
  </div>
  <div class="cf-eg egf">
    <div class="cf-eg-ver">ENGINE · v10000</div>
    <div class="cf-eg-name">Aether-Primality</div>
    <div class="cf-eg-desc">Tissue-specific permeability across lung, spleen, liver and kidney using organ-motif pattern matching. Nanotoxicity scan for heavy metals, PFAS and ROS-generating structures. Carbon footprint estimation. Quantum motif detection, genetic nexus alerts, mock protein binding against 4 PDB targets and a neural blueprint with tensor activations completing the v1M synthesis.</div>
    <div class="cf-eg-chips"><span class="cf-eg-chip">Tissue Mapping</span><span class="cf-eg-chip">Nanotox</span><span class="cf-eg-chip">Carbon Score</span><span class="cf-eg-chip">Neural Blueprint</span></div>
  </div>
</div>

<div class="cf-hr"></div>

<!-- TECH STACK -->
<div class="cf-sh">
  <div class="cf-sh-tag">Technology</div>
  <div class="cf-sh-title">Built on world-class open science</div>
  <div class="cf-sh-sub">Every prediction is grounded in peer-reviewed cheminformatics — not black-box heuristics.</div>
</div>
<div class="cf-tech-grid">
  <div class="cf-tech-item"><div class="cf-tech-icon">⚗️</div><div class="cf-tech-name">RDKit</div><div class="cf-tech-desc">Open-source cheminformatics for substructure matching, Morgan fingerprints, MMFF94 conformer optimisation and 150+ molecular descriptors.</div></div>
  <div class="cf-tech-item"><div class="cf-tech-icon">🤖</div><div class="cf-tech-name">Claude Sonnet 4</div><div class="cf-tech-desc">Anthropic's frontier model powers the AI Explainer, analogue generator, repurposing advisor and retrosynthesis planner via the Messages API.</div></div>
  <div class="cf-tech-item"><div class="cf-tech-icon">📈</div><div class="cf-tech-name">Plotly 5</div><div class="cf-tech-desc">All 10 interactive chart types — radar, BOILED-EGG, PCA (2D/3D), parallel coords, similarity heatmaps and gauge charts — rendered via Plotly Graph Objects.</div></div>
  <div class="cf-tech-item"><div class="cf-tech-icon">🌐</div><div class="cf-tech-name">PubChem PUG-REST</div><div class="cf-tech-desc">Live IUPAC name and molecular formula lookup from PubChem REST API, with graceful fallback for novel compounds not yet indexed.</div></div>
  <div class="cf-tech-item"><div class="cf-tech-icon">🧮</div><div class="cf-tech-name">NumPy / Pandas</div><div class="cf-tech-desc">SVD-based PCA across 2048-bit Morgan fingerprint matrices, similarity matrix computation and DataFrame export pipelines.</div></div>
  <div class="cf-tech-item"><div class="cf-tech-icon">☁️</div><div class="cf-tech-name">Streamlit Cloud</div><div class="cf-tech-desc">Zero-install deployment via Streamlit Cloud. Secrets management for API keys, cached resource loading and session-state gating.</div></div>
  <div class="cf-tech-item"><div class="cf-tech-icon">🔬</div><div class="cf-tech-name">MMFF94 Forcefield</div><div class="cf-tech-desc">3D conformer generation and energy minimisation using RDKit's MMFF94 implementation. Molecular stress computed as ΔE normalised by heavy-atom count.</div></div>
  <div class="cf-tech-item"><div class="cf-tech-icon">🛡️</div><div class="cf-tech-name">PAINS FilterCatalog</div><div class="cf-tech-desc">RDKit's built-in PAINS catalog from Baell & Holloway (J Med Chem 2010) — all 480 PAINS-A/B/C patterns for pan-assay interference detection.</div></div>
</div>

<div class="cf-hr"></div>

<!-- SCIENTIFIC REFERENCES -->
<div class="cf-sh">
  <div class="cf-sh-tag">Citations</div>
  <div class="cf-sh-title">Grounded in peer-reviewed science</div>
</div>
<div class="cf-refs">
  <div class="cf-ref"><div class="cf-ref-h" style="color:var(--ac)">Drug-Likeness</div><div class="cf-ref-body">Lipinski et al. — Experimental and computational approaches to estimate solubility and permeability in drug discovery. <em>Adv Drug Deliv Rev</em> 2001<br>Ghose et al. — A knowledge-based approach in designing combinatorial libraries. <em>J Comb Chem</em> 1999<br>Veber et al. — Molecular properties that influence oral bioavailability. <em>J Med Chem</em> 2002<br>Egan et al. — Predicting intestinal permeability from molecular structure. <em>J Med Chem</em> 2000</div></div>
  <div class="cf-ref"><div class="cf-ref-h" style="color:var(--cyan)">ADME Models</div><div class="cf-ref-body">Daina & Zoete — A BOILED-Egg to predict gastrointestinal absorption and brain penetration. <em>ChemMedChem</em> 2016<br>Delaney — ESOL: Estimating aqueous solubility directly from molecular structure. <em>J Chem Inf Comput Sci</em> 2004<br>Bickerton et al. — Quantifying the chemical beauty of drugs (QED). <em>Nat Chem</em> 2012<br>Wager et al. — Moving beyond rules: CNS multiparameter optimization. <em>ACS Chem Neurosci</em> 2010</div></div>
  <div class="cf-ref"><div class="cf-ref-h" style="color:var(--violet)">Safety & Toxicology</div><div class="cf-ref-body">Baell & Holloway — New substructure filters for removal of pan assay interference compounds (PAINS). <em>J Med Chem</em> 2010<br>Ertl & Schuffenhauer — Estimation of synthetic accessibility score. <em>J Cheminform</em> 2009<br>Wishart et al. — DrugBank 5.0: a major update. <em>Nucleic Acids Res</em> 2018<br>Bemis & Murcko — The properties of known drugs: molecular frameworks. <em>J Med Chem</em> 1996</div></div>
  <div class="cf-ref"><div class="cf-ref-h" style="color:var(--green)">Cheminformatics</div><div class="cf-ref-body">Landrum — RDKit: Open-source cheminformatics software. <em>rdkit.org</em> 2006–2024<br>Rogers & Hahn — Extended-connectivity fingerprints (ECFP). <em>J Chem Inf Model</em> 2010<br>Kim et al. — PubChem 2023 update. <em>Nucleic Acids Res</em> 2023<br>Hansch & Fujita — ρ-σ-π analysis. A method for the correlation of biological activity. <em>JACS</em> 1964</div></div>
</div>

<div class="cf-hr"></div>

<!-- FINAL CTA -->
<div class="cf-cta-wrap" style="padding-top:72px">
  <div class="cf-cta">
    <div class="cf-cta-t">Ready to screen your compounds?</div>
    <div class="cf-cta-s">Launch ChemoFilter — running live on Streamlit Cloud. No installation, no sign-up. Just SMILES.</div>
"""

_FOOTER_SCRIPT = """
    <div class="cf-chips">
      <span class="cf-chip">RDKit</span><span class="cf-chip">Streamlit</span><span class="cf-chip">Claude AI</span><span class="cf-chip">Plotly 5</span><span class="cf-chip">PubChem API</span><span class="cf-chip">MMFF94</span><span class="cf-chip">Morgan FP</span><span class="cf-chip">PAINS Catalog</span><span class="cf-chip">NumPy SVD</span><span class="cf-chip">Pandas</span>
    </div>
  </div>
</div>

<footer class="cf-footer">
  <div class="cf-fl">ChemoFilter &nbsp;·&nbsp; VIT Chennai MDP 2026 &nbsp;·&nbsp; Omnipotent v1,000,000</div>
  <div class="cf-fr">
    <span class="cf-fc">Lipinski [2001]</span>
    <span class="cf-fc">Daina [2016]</span>
    <span class="cf-fc">Bickerton [2012]</span>
    <span class="cf-fc">Ertl [2009]</span>
    <span class="cf-fc">RDKit</span>
  </div>
</footer>
</div>

<button id="cf-thm" onclick="cfToggleTheme()" title="Toggle dark / light">🌙</button>

<script>
(function(){
  var isDark=true;
  window.cfToggleTheme=function(){
    isDark=!isDark;
    var root=document.getElementById('cf-root');
    var btn=document.getElementById('cf-thm');
    if(!isDark){root.classList.add('lm');if(btn)btn.innerHTML='☀️';}
    else{root.classList.remove('lm');if(btn)btn.innerHTML='🌙';}
  };
})();
</script>
"""
