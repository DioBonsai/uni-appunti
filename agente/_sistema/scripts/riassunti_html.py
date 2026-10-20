"""Converte i 5 Word dei riassunti in pagine HTML per il Quaderno online (con le evidenziazioni gialle, il codice,
apici/pedici e le figure). Non modifica mai i Word.

Uso: python riassunti_html.py <cartella_uscita>
Scrive: <uscita>/riassunti/index.html, <uscita>/riassunti/<slug>.html, <uscita>/riassunti/img/<hash>.<ext>
"""
import hashlib
from datetime import datetime
import html
import json
import re
import sys
from pathlib import Path

import docx
from docx.oxml.ns import qn

UNI = Path(__file__).resolve().parents[3]
BASE = Path(__file__).resolve().parents[1]
# (slug, nome, file Word, chiave in studiato_manuale.json)
MATERIE = [
    ("algebra", "Algebra lineare", "Riassunto Algebra lineare.docx", "Algebra lineare"),
    ("matematica-discreta", "Matematica discreta", "Riassunto Matematica discreta.docx", "Matematica discreta"),
    ("fondamenti", "Fondamenti dell'Informatica", "Riassunto Fondamenti Informatica.docx", "Fondamenti Info"),
    ("programmazione", "Programmazione", "Riassunto Programmazione.docx", "Programmazione"),
    ("laboratorio", "Programmazione, Laboratorio", "Riassunto Laboratorio.docx", "Programmazione, Laboratorio"),
]
COLORI = {"algebra": ("#2744a8", "#8fadff"), "matematica-discreta": ("#b8302c", "#ff9188"), "fondamenti": ("#16703f", "#70dca2"),
          "programmazione": ("#b25a0a", "#ffb866"), "laboratorio": ("#7a4fb5", "#c3a6ff")}
EXT = {"image/png": "png", "image/jpeg": "jpg", "image/gif": "gif", "image/svg+xml": "svg", "image/webp": "webp"}
W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"

CSS = r"""
:root{--bg:#fbfaf7;--fg:#1d2330;--mut:#667085;--lin:#e3e0d8;--acc:#1f4e9c;--tit:#b42318;--sub:#b54708;--cod:#f1efe9;--mark:#fff59d;--card:#ffffff;--bar:#fbfaf7e8;--ok:#1e8449;--hl:#ffd54f;--fs:18px}
@media (prefers-color-scheme:dark){:root:not([data-theme=light]){--bg:#14171d;--fg:#e3e6ec;--mut:#98a1b3;--lin:#2a2f3a;--acc:#8fb4ff;--tit:#ff8f80;--sub:#ffb066;--cod:#1c2029;--mark:#6a5c00;--card:#1a1e26;--bar:#14171de8;--ok:#5fd08a;--hl:#a88400}}
:root[data-theme=dark]{--bg:#14171d;--fg:#e3e6ec;--mut:#98a1b3;--lin:#2a2f3a;--acc:#8fb4ff;--tit:#ff8f80;--sub:#ffb066;--cod:#1c2029;--mark:#6a5c00;--card:#1a1e26;--bar:#14171de8;--ok:#5fd08a;--hl:#a88400}
*{box-sizing:border-box}html{scroll-padding-top:72px;-webkit-text-size-adjust:100%}html.ready{scroll-behavior:smooth}
body{margin:0;background:var(--bg);color:var(--fg);font:var(--fs)/1.72 "Iowan Old Style","Palatino Linotype",Palatino,Georgia,serif;text-rendering:optimizeLegibility}
a{color:var(--acc)}button,input,select{font:inherit}
.sans{font-family:system-ui,-apple-system,"Segoe UI",Roboto,sans-serif}
/* barra in alto */
.top{position:sticky;top:0;z-index:20;background:var(--bar);backdrop-filter:blur(8px);border-bottom:1px solid var(--lin);font:14px/1.2 system-ui,-apple-system,"Segoe UI",sans-serif}
.top-in{max-width:94rem;margin:0 auto;padding:.5rem 1rem;display:flex;align-items:center;gap:.6rem;flex-wrap:wrap}
.top a.back{text-decoration:none;font-weight:600;white-space:nowrap;display:inline-flex;align-items:center;min-height:36px;padding:0 .85rem;border:1px solid var(--lin);border-radius:99px;background:var(--card)}.top a.back:hover{border-color:var(--acc)}
.top .mat{font-weight:700;white-space:nowrap}
.top .cur{color:var(--mut);white-space:nowrap;overflow:hidden;text-overflow:ellipsis;max-width:28rem;min-width:0;flex:1 1 8rem}
.top .grow{flex:1}
.tb{appearance:none;border:1px solid var(--lin);background:var(--card);color:var(--fg);border-radius:8px;padding:.32rem .6rem;cursor:pointer;line-height:1.2}
.tb:hover{border-color:var(--acc)}.tb[aria-pressed=true]{background:var(--mark)}
select.tb{max-width:8.6rem;text-overflow:ellipsis}
#ctrls{display:contents}.top a.back{order:-2}#mats{order:-1}#msearch,#mopts,#mbar,#scrim{display:none}
.search{display:flex;align-items:center;gap:.3rem;background:var(--card);border:1px solid var(--lin);border-radius:8px;padding:0 .3rem 0 .55rem}
.search:focus-within{border-color:var(--acc)}
.search input{border:0;outline:0;background:none;color:var(--fg);width:12rem;padding:.35rem 0}
.search .n{color:var(--mut);font-size:12px;min-width:3.2rem;text-align:right}
.search button{border:0;background:none;color:var(--mut);cursor:pointer;padding:.2rem .35rem;border-radius:5px}.search button:hover{color:var(--fg);background:var(--lin)}
#prog{position:absolute;left:0;bottom:-1px;height:2px;width:0;background:var(--acc);transition:width .1s linear}
/* impaginazione */
.wrap{display:grid;grid-template-columns:17.5rem minmax(0,46rem) 13.5rem;justify-content:center;gap:2.2rem;max-width:94rem;margin:0 auto;padding:1rem 1rem 0}
nav.toc{position:sticky;top:3.9rem;align-self:start;max-height:calc(100vh - 4.6rem);overflow:auto;font:14px/1.35 system-ui,-apple-system,"Segoe UI",sans-serif;padding:.2rem .6rem 2rem 0;scrollbar-width:thin}
nav.toc h4{margin:.2rem 0 .5rem;font-size:11px;letter-spacing:.08em;text-transform:uppercase;color:var(--mut)}
nav.toc a{display:flex;gap:.55rem;align-items:flex-start;padding:.38rem .5rem;border-radius:8px;text-decoration:none;color:var(--fg);border-left:3px solid transparent}
nav.toc a:hover{background:var(--cod)}
nav.toc a.on{background:var(--cod);border-left-color:var(--acc);font-weight:600}
nav.toc .num{color:var(--mut);min-width:1.5rem;text-align:right;font-variant-numeric:tabular-nums;flex:none}
nav.toc .st{flex:none;width:.62rem;height:.62rem;border-radius:50%;border:1.5px solid var(--lin);margin-top:.28rem}
nav.toc .st1{border-color:var(--ok);background:linear-gradient(90deg,var(--ok) 50%,transparent 50%)}
nav.toc .st2{border-color:var(--ok);background:var(--ok)}
nav.toc .ttl{flex:1}
aside.rail{position:sticky;top:3.9rem;align-self:start;max-height:calc(100vh - 4.6rem);overflow:auto;font:13px/1.35 system-ui,-apple-system,"Segoe UI",sans-serif;padding:.2rem 0 2rem;scrollbar-width:thin}
aside.rail h4{margin:.2rem 0 .5rem;font-size:11px;letter-spacing:.08em;text-transform:uppercase;color:var(--mut)}
aside.rail a{display:block;padding:.28rem .6rem;color:var(--mut);text-decoration:none;border-left:2px solid var(--lin)}
aside.rail a:hover{color:var(--fg)}aside.rail a.on{color:var(--sub);border-left-color:var(--sub);font-weight:600}
main{min-width:0;padding-bottom:6rem}
main h2{color:var(--tit);font-size:1.7rem;line-height:1.25;margin:3.2rem 0 .8rem;padding-top:1.2rem;border-top:2px solid var(--lin);font-family:system-ui,-apple-system,"Segoe UI",sans-serif;font-weight:750;letter-spacing:-.01em}
main section.cap:first-child h2{margin-top:.8rem;border-top:0;padding-top:0}
main h3{color:var(--sub);font-size:1.12rem;margin:2rem 0 .3rem;font-family:system-ui,-apple-system,"Segoe UI",sans-serif;font-weight:700}
p{margin:.7rem 0;hyphens:auto;-webkit-hyphens:auto}ul,ol{margin:.6rem 0;padding-left:1.5rem}li{margin:.28rem 0}
mark{background:var(--mark);color:inherit;border-radius:3px;padding:.02em .08em}body.nomark mark{background:none}
code,pre{font:.8em/1.5 "Cascadia Mono",Consolas,"SFMono-Regular",Menlo,monospace}code{background:var(--cod);padding:.05em .3em;border-radius:4px}
pre{position:relative;background:var(--cod);padding:.85rem 1rem;border-radius:10px;overflow:auto;margin:.9rem 0;border:1px solid var(--lin);tab-size:4}pre code{background:none;padding:0;font-size:1em}
pre .cp{position:absolute;top:.4rem;right:.4rem;opacity:0;transition:opacity .15s;font:12px system-ui,sans-serif;padding:.2rem .5rem}
pre:hover .cp,pre .cp:focus{opacity:1}
figure{margin:1.2rem 0;text-align:center}figure img{max-width:100%;height:auto;background:#fff;border-radius:8px;border:1px solid var(--lin);cursor:zoom-in}
table{border-collapse:collapse;margin:.9rem 0;font:15px system-ui,sans-serif;display:block;overflow:auto}td,th{border:1px solid var(--lin);padding:.35rem .65rem}
.hit{background:var(--hl);color:#000;border-radius:2px}.hit.cur{outline:2px solid var(--acc);background:#ffb300}
.pn{display:flex;justify-content:space-between;gap:1rem;margin:2.4rem 0 0;font:14px system-ui,-apple-system,sans-serif}
.pn a{flex:1;text-decoration:none;color:var(--fg);border:1px solid var(--lin);background:var(--card);border-radius:10px;padding:.7rem .9rem;line-height:1.3}
.pn a:hover{border-color:var(--acc)}.pn small{display:block;color:var(--mut);font-size:12px;margin-bottom:.15rem}.pn a.next{text-align:right}
#lb{position:fixed;inset:0;z-index:50;background:#000c;display:none;align-items:center;justify-content:center;cursor:zoom-out}#lb.on{display:flex}#lb img{max-width:94vw;max-height:92vh;background:#fff;border-radius:6px}
#toast{position:fixed;left:50%;bottom:1.2rem;transform:translateX(-50%);z-index:30;background:var(--card);border:1px solid var(--lin);border-radius:12px;box-shadow:0 8px 30px #0003;padding:.6rem .9rem;font:14px system-ui,sans-serif;display:none;gap:.8rem;align-items:center}#toast.on{display:flex}
@media (max-width:1280px){.wrap{grid-template-columns:16.5rem minmax(0,46rem)}aside.rail{display:none}}
@media (max-width:1180px){.top .cur{display:none}.search input{width:7.2rem}.top-in{gap:.4rem}.tb{padding:.3rem .5rem}}
@media (max-width:900px){
.wrap{display:block;padding:.8rem 1rem 0}:root{--fs:17px}html{scroll-padding-top:64px}.top .cur{display:none}
nav.toc{position:fixed;left:0;right:0;bottom:0;top:auto;z-index:40;max-height:74vh;background:var(--card);border-top:1px solid var(--lin);border-radius:18px 18px 0 0;padding:1rem 1rem calc(1rem + env(safe-area-inset-bottom));transform:translateY(105%);transition:transform .25s ease;box-shadow:0 -12px 40px #0006;font-size:15.5px;align-self:auto}
nav.toc.open{transform:none}
nav.toc a{min-height:48px;align-items:center}
#scrim{display:block;position:fixed;inset:0;z-index:35;background:#0008;opacity:0;pointer-events:none;transition:opacity .2s}#scrim.on{opacity:1;pointer-events:auto}
#mbar{display:grid;position:fixed;left:0;right:0;bottom:0;z-index:30;grid-template-columns:56px 1fr 56px;gap:8px;padding:6px 10px calc(6px + env(safe-area-inset-bottom));background:var(--bar);backdrop-filter:blur(10px);border-top:1px solid var(--lin);font:15px system-ui,-apple-system,sans-serif}
#mbar button{min-height:48px;border:1px solid var(--lin);border-radius:14px;background:var(--card);color:var(--fg);font:inherit;cursor:pointer}
#mbar button:active{transform:scale(.97)}#mbar #mcap{font-weight:650}#mbar button[disabled]{opacity:.4}
#toast{bottom:calc(76px + env(safe-area-inset-bottom));width:calc(100% - 1.6rem);justify-content:space-between}
main{padding-bottom:7.5rem}
}
@media (max-width:720px){
.top{padding-top:env(safe-area-inset-top)}
.top-in{gap:.3rem;padding:.3rem .5rem;min-height:54px;flex-wrap:wrap}
.top a.back{font-size:0;display:grid;place-items:center;width:44px;height:44px;border-radius:12px;border:0;background:none;padding:0}.top a.back::before{content:"\2039";font-size:36px;line-height:1;color:var(--acc);margin-top:-4px}
.top .mat{flex:1;min-width:0;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;font-size:16px;border-left:0;padding-left:0}
#msearch,#mopts{display:grid;place-items:center;width:44px;height:44px;border:0;background:none;color:var(--fg);border-radius:12px;cursor:pointer;padding:0}
#msearch svg,#mopts svg{width:24px;height:24px;fill:none;stroke:currentColor;stroke-width:2;stroke-linecap:round;stroke-linejoin:round}
#msearch:active,#mopts:active{background:var(--lin)}
#ctrls{display:flex;position:fixed;left:0;right:0;bottom:0;z-index:40;flex-wrap:wrap;gap:.6rem;padding:1.1rem 1rem calc(1.1rem + env(safe-area-inset-bottom));background:var(--card);border-radius:18px 18px 0 0;box-shadow:0 -12px 40px #0006;transform:translateY(105%);transition:transform .25s ease}
#ctrls.open{transform:none}
#ctrls .tb{min-height:48px;font-size:15px;flex:1 1 40%;padding:.5rem .8rem}
#ctrls select.tb{flex:1 1 100%;max-width:none;order:0}
.search{display:none}.top.srch .search{display:flex;flex:1 0 100%;order:5;padding:.1rem .3rem .1rem .7rem;margin:0 0 .2rem}
.search input{width:100%;font-size:16px;padding:.6rem 0}
.search button{min-width:44px;min-height:44px;font-size:18px}
.search .n{min-width:3.6rem;font-size:13px}
.hero{padding:1.1rem 1rem 1.2rem;margin-bottom:1.6rem}.hero h1{font-size:1.55rem}
.hero .map{gap:6px}.hero .map a{width:38px;height:38px;font-size:13px}
.hero .act .btn{flex:1 1 100%;text-align:center;padding:.85rem 1rem;font-size:1rem}
main h2{font-size:1.45rem}main h3{font-size:1.1rem}
.pn{flex-direction:column}.pn a{padding:.9rem 1rem}
.idx{padding:1.2rem .9rem 3rem}.idx h1{font-size:1.7rem}.idx a.mcard{padding:1.1rem 1.1rem}
}
:focus-visible{outline:2px solid var(--acc);outline-offset:2px;border-radius:4px}
.skip{position:absolute;left:.5rem;top:-4rem;z-index:60;background:var(--acc);color:#fff;padding:.6rem 1rem;border-radius:10px;font:600 14px system-ui,sans-serif;text-decoration:none}.skip:focus{top:.5rem}
@media (prefers-reduced-motion:reduce){*,*::before,*::after{animation:none!important;transition:none!important}html.ready{scroll-behavior:auto}}
@media print{.top,nav.toc,aside.rail,.pn,#toast,#lb,.cp{display:none!important}.wrap{display:block;padding:0}body{background:#fff;color:#000;font-size:11pt}main h2{break-before:page;border:0}main section.cap:first-child h2{break-before:auto}mark{background:#fff59d!important;-webkit-print-color-adjust:exact;print-color-adjust:exact}pre,figure{break-inside:avoid}}
body{--mc:var(--mcl,#1f4e9c)}
@media (prefers-color-scheme:dark){:root:not([data-theme=light]) body{--mc:var(--mcd,#8fb4ff)}}
:root[data-theme=dark] body{--mc:var(--mcd,#8fb4ff)}
.top .mat{color:var(--mc)}@media (min-width:721px){.top .mat{border-left:3px solid var(--mc);padding-left:.55rem}}
.idx-top .top-in{max-width:62rem;min-height:58px;padding:.5rem 1rem}.idx-top .mat{color:var(--fg);border-left:0;padding-left:0;font-size:1.05rem}.idx-top .grow{flex:1}
#prog{background:var(--mc)}
nav.toc a.on{border-left-color:var(--mc)}
.hero{margin:.2rem 0 2.2rem;padding:1.4rem 1.5rem 1.3rem;background:var(--card);border:1px solid var(--lin);border-left:6px solid var(--mc);border-radius:16px;font-family:system-ui,-apple-system,"Segoe UI",sans-serif}
.hero h1{margin:0 0 .2rem;font-size:1.9rem;line-height:1.15;letter-spacing:-.015em;color:var(--mc)}
.hero p{margin:0;color:var(--mut);font-size:.95rem}
.hero .map{display:flex;flex-wrap:wrap;gap:5px;margin:1.1rem 0 .3rem}
.hero .map a{width:30px;height:30px;display:grid;place-items:center;border-radius:8px;font-size:12px;font-weight:700;text-decoration:none;color:var(--mut);border:1.5px solid var(--lin);font-variant-numeric:tabular-nums}
.hero .map a:hover{border-color:var(--mc);color:var(--fg)}
.hero .map a.st1{border-color:var(--ok);background:linear-gradient(135deg,color-mix(in srgb,var(--ok) 40%,transparent) 50%,transparent 50%);color:var(--fg)}
.hero .map a.st2{background:var(--ok);border-color:var(--ok);color:#fff}
.hero .leg{font-size:12px;color:var(--mut);margin:.2rem 0 1rem}
.hero .act{display:flex;gap:.6rem;flex-wrap:wrap}
.btn{display:inline-block;text-decoration:none;font-weight:700;font-size:.95rem;padding:.6rem 1rem;border-radius:10px;background:var(--mc);color:#fff;border:1px solid var(--mc)}
.btn:hover{filter:brightness(1.08)}.btn.ghost{background:transparent;color:var(--fg);border-color:var(--lin)}.btn.ghost:hover{border-color:var(--mc)}
:root[data-theme=dark] .btn:not(.ghost){color:#10131a}
@media (prefers-color-scheme:dark){:root:not([data-theme=light]) .btn:not(.ghost){color:#10131a}}
.capmeta{display:flex;gap:.7rem;align-items:center;margin:-.3rem 0 1rem;font:13px system-ui,-apple-system,sans-serif;color:var(--mut)}
.badge{display:inline-flex;align-items:center;gap:.35rem;font-weight:700;font-size:12px;padding:.15rem .6rem;border-radius:99px;border:1px solid var(--lin)}
.badge i{width:.55rem;height:.55rem;border-radius:50%;border:1.5px solid var(--mut)}
.badge.b1{color:var(--ok);border-color:var(--ok)}.badge.b1 i{border-color:var(--ok);background:linear-gradient(90deg,var(--ok) 50%,transparent 50%)}
.badge.b2{color:var(--ok);border-color:var(--ok)}.badge.b2 i{border-color:var(--ok);background:var(--ok)}
/* indice delle materie */
.idx{max-width:62rem;margin:0 auto;padding:2rem 1rem 4rem;font-family:system-ui,-apple-system,"Segoe UI",sans-serif}
.idx h1{font-size:2rem;letter-spacing:-.02em;margin:.2rem 0 .2rem}.idx .lead{color:var(--mut);margin:0 0 1.4rem}
.idx .grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(18rem,1fr));gap:1rem}
.idx a.mcard{display:flex;flex-direction:column;gap:.5rem;background:var(--card);border:1px solid var(--lin);border-top:5px solid var(--mc);border-radius:16px;padding:1.1rem 1.2rem 1rem;text-decoration:none;color:var(--fg);box-shadow:0 1px 0 #0001;transition:transform .15s,box-shadow .15s,border-color .15s}
.idx a.mcard:hover{transform:translateY(-2px);box-shadow:0 10px 26px -12px #0006;border-color:var(--mc)}
.idx .foot{margin:2rem 0 0;color:var(--mut);font-size:13px;line-height:1.6}.idx kbd{font:12px/1 ui-monospace,Consolas,monospace;border:1px solid var(--lin);border-bottom-width:2px;border-radius:5px;padding:.1rem .35rem;background:var(--card)}
.idx a.mcard{--mc:var(--mcl)}
@media (prefers-color-scheme:dark){:root:not([data-theme=light]) .idx a.mcard{--mc:var(--mcd)}}
:root[data-theme=dark] .idx a.mcard{--mc:var(--mcd)}
.idx .mc-top{display:flex;justify-content:space-between;align-items:baseline;gap:.6rem}.idx .mc-nm{font-weight:750;font-size:1.2rem;color:var(--mc)}.idx .mc-pct{font-weight:700;font-variant-numeric:tabular-nums}
.idx .bar{height:7px;border-radius:99px;background:var(--lin);overflow:hidden}.idx .bar i{display:block;height:100%;background:var(--ok);border-radius:99px}
.idx .mc-sub{font-size:13px;color:var(--mut)}.idx .mc-next{font-size:13.5px;line-height:1.4;min-height:2.8em}.idx .mc-next b{font-weight:650}
.idx .mc-go{margin-top:auto;font-weight:700;font-size:.92rem;color:var(--mc)}
#resume{display:none;border:1px solid var(--acc);border-radius:14px;padding:.8rem 1.2rem;margin:.4rem 0 1.2rem;font:15px system-ui,sans-serif;background:var(--card)}#resume a{font-weight:700}
@media (max-width:900px){.top{backdrop-filter:none;-webkit-backdrop-filter:none;background:var(--bg)}}
@media (max-width:720px){
.hero{padding:1.1rem 1rem 1.2rem;margin-bottom:1.6rem}.hero h1{font-size:1.55rem}
.hero .map{gap:6px}.hero .map a{width:38px;height:38px;font-size:13px}
.hero .act .btn{flex:1 1 100%;text-align:center;padding:.85rem 1rem;font-size:1rem}
.idx{padding:1.2rem .9rem 3rem}.idx h1{font-size:1.7rem}.idx a.mcard{padding:1.1rem}
.capmeta{margin-bottom:.8rem}
}

/* ---- controlli di lettura ---- */
.top-in{gap:.5rem}
.ibtn{appearance:none;display:inline-flex;align-items:center;justify-content:center;gap:.45rem;height:36px;border:1px solid var(--lin);background:var(--card);color:var(--fg);border-radius:10px;padding:0 .7rem;cursor:pointer;font:600 13.5px/1 system-ui,-apple-system,"Segoe UI",sans-serif}
.ibtn:hover{border-color:var(--mc)}
.ibtn svg,.search svg,#totop svg{width:18px;height:18px;fill:none;stroke:currentColor;stroke-width:1.9;stroke-linecap:round;stroke-linejoin:round;flex:none}
.segm{display:inline-flex;border:1px solid var(--lin);border-radius:10px;overflow:hidden;background:var(--card)}
.segm button{appearance:none;border:0;background:none;color:var(--fg);padding:0 .8rem;cursor:pointer;font:700 15px/1 system-ui,sans-serif;height:34px}
.segm button+button{border-left:1px solid var(--lin)}.segm button:hover{background:var(--cod)}.segm .a-s{font-size:12px}.segm .a-l{font-size:18px}
.sw-btn{appearance:none;display:inline-flex;align-items:center;gap:.55rem;height:36px;border:1px solid var(--lin);background:var(--card);color:var(--fg);border-radius:10px;padding:0 .85rem 0 .65rem;cursor:pointer;font:600 13.5px/1 system-ui,-apple-system,sans-serif;white-space:nowrap}
.sw{width:30px;height:18px;border-radius:99px;background:var(--lin);position:relative;transition:background .15s;flex:none}
.sw::after{content:"";position:absolute;left:2px;top:2px;width:14px;height:14px;border-radius:50%;background:#fff;box-shadow:0 1px 2px #0004;transition:transform .15s}
.sw-btn[aria-checked=true]{border-color:var(--mc)}.sw-btn[aria-checked=true] .sw{background:var(--mc)}.sw-btn[aria-checked=true] .sw::after{transform:translateX(12px)}
#theme svg{display:none}#theme[data-t=auto] .t-auto,#theme[data-t=light] .t-light,#theme[data-t=dark] .t-dark{display:block}#theme .lbl{display:none}
.search{height:36px;border-radius:10px;padding:0 .3rem 0 .65rem;flex:1 1 14rem;max-width:28rem}
.search svg{stroke:var(--mut);width:17px;height:17px}
.search input{width:auto;flex:1;min-width:4rem;padding:0}
select.tb.mats{height:36px;max-width:13rem;border-radius:10px;font-weight:700;color:var(--mc);padding:0 .7rem}
@media (min-width:721px){.top .mat,.top .cur{display:none}.idx-top .mat{display:inline}.top a.back{order:-3}#mats{order:-2}.search{order:-1}.top-in{padding:.5rem 1rem}}
/* ---- riquadro "In parole povere", link alle sezioni, torna su ---- */
main p.pp{margin:1.1rem 0;padding:.85rem 1rem .9rem;border-radius:12px;background:var(--cod);background:color-mix(in srgb,var(--mc) 8%,var(--card));border:1px solid var(--lin);border-left:4px solid var(--mc)}
main p.pp::before{content:"In parole povere";display:block;font:700 11px/1 system-ui,-apple-system,sans-serif;letter-spacing:.09em;text-transform:uppercase;color:var(--mc);margin-bottom:.45rem}
main h2,main h3{position:relative}
.ha{position:absolute;left:-1.7rem;top:0;opacity:0;font:600 .9rem system-ui,sans-serif;text-decoration:none;color:var(--mut);padding:.1rem .35rem;border-radius:6px}.ha::before{content:"#"}
main h2:hover .ha,main h3:hover .ha,.ha:focus{opacity:1}.ha:hover{color:var(--mc);background:var(--cod)}
#totop{position:fixed;right:1.3rem;bottom:1.4rem;z-index:25;width:46px;height:46px;border-radius:50%;border:1px solid var(--lin);background:var(--card);color:var(--fg);display:grid;place-items:center;cursor:pointer;box-shadow:0 6px 20px #0004;opacity:0;pointer-events:none;transform:translateY(8px);transition:opacity .2s,transform .2s}
#totop.on{opacity:1;pointer-events:auto;transform:none}#totop svg{width:22px;height:22px;stroke-width:2.2}
@media (max-width:900px){.ha{display:none}#totop{bottom:calc(84px + env(safe-area-inset-bottom));right:.9rem}}
@media (max-width:720px){
#ctrls .segm,#ctrls .sw-btn,#ctrls .ibtn{min-height:48px;height:auto;flex:1 1 40%;font-size:15px;justify-content:center}
#ctrls .segm button{flex:1;height:46px}#ctrls .sw-btn{justify-content:flex-start;gap:.7rem}
#theme .lbl{display:inline}#ctrls select.tb.mats{height:48px;max-width:none}
main p.pp{padding:.8rem .9rem .85rem}
}
"""

JS_COMUNE = r"""
(function(){
var root=document.documentElement;
function ls(k,v){try{if(v===undefined)return localStorage.getItem(k);localStorage.setItem(k,v)}catch(e){return null}}
var th=ls('quaderno-tema')||'auto';
if(th!=='auto')root.setAttribute('data-theme',th);
var fs=parseInt(ls('riass-fs'),10);if(fs>=14&&fs<=24)root.style.setProperty('--fs',fs+'px');
if(ls('riass-evid')==='0')document.documentElement.classList.add('nomark0');
})();
"""

JS_PAGINA = r"""
(function(){
var $=function(s,r){return (r||document).querySelector(s)},$$=function(s,r){return Array.prototype.slice.call((r||document).querySelectorAll(s))};
var root=document.documentElement,body=document.body,SLUG=body.dataset.slug;
function ls(k,v){try{if(v===undefined)return localStorage.getItem(k);localStorage.setItem(k,v)}catch(e){return null}}
var main=$('main'),caps=$$('section.cap',main),toc=$('nav.toc'),rail=$('aside.rail');
/* ancora iniziale: salto immediato (lo scorrimento morbido verso un punto lontano si interrompe); poi si riallinea finché la pagina si assesta */
var early=true;function toHash(){if(!location.hash||!early)return;var e=document.getElementById(decodeURIComponent(location.hash.slice(1)));if(e)e.scrollIntoView({behavior:'instant'})}
toHash();window.addEventListener('load',toHash);setTimeout(function(){early=false;root.classList.add('ready')},2500);
['wheel','touchstart','keydown','mousedown'].forEach(function(ev){window.addEventListener(ev,function(){early=false;root.classList.add('ready')},{passive:true,once:true})});

/* evidenziazioni, tema, dimensione del testo */
var hl=$('#hl');function setHl(on){body.classList.toggle('nomark',!on);hl.setAttribute('aria-checked',on?'true':'false');ls('riass-evid',on?'1':'0')}
setHl(ls('riass-evid')!=='0');hl.addEventListener('click',function(){setHl(body.classList.contains('nomark'))});
var tb=$('#theme');function lab(){var t=ls('quaderno-tema')||'auto',nm={auto:'automatico',light:'chiaro',dark:'scuro'}[t]||'automatico';tb.dataset.t=t;tb.title='Tema: '+nm+' (tocca per cambiare)';tb.setAttribute('aria-label','Tema: '+nm+', tocca per cambiare');var l=tb.querySelector('.lbl');if(l)l.textContent='Tema: '+nm}
lab();tb.addEventListener('click',function(){var t=ls('quaderno-tema')||'auto',n={auto:'light',light:'dark',dark:'auto'}[t]||'auto';ls('quaderno-tema',n);if(n==='auto')root.removeAttribute('data-theme');else root.setAttribute('data-theme',n);lab()});
function size(d){var c=parseInt(getComputedStyle(root).getPropertyValue('--fs'),10)||18,n=Math.max(14,Math.min(24,c+d));root.style.setProperty('--fs',n+'px');ls('riass-fs',String(n))}
$('#fsm').addEventListener('click',function(){size(-1)});$('#fsp').addEventListener('click',function(){size(1)});
$('#mats').addEventListener('change',function(e){if(e.target.value&&e.target.value!==SLUG+'.html')location.href=e.target.value});

/* capitolo attivo, indice, barra di avanzamento */
var q=$('#q'),links=$$('a[data-cap]',toc),active=-1,hs=[],railLinks=[],ticking=false,cur=$('#cur'),prog=$('#prog'),mc=$('#mcap'),mp=$('#mprev'),mn=$('#mnext'),ctrls=$('#ctrls'),scrim=$('#scrim');
function buildRail(i){
  rail.innerHTML='<h4>In questo capitolo</h4>';hs=$$('h3',caps[i]);railLinks=[];
  hs.forEach(function(h){var a=document.createElement('a');a.href='#'+h.id;a.textContent=h.textContent;rail.appendChild(a);railLinks.push(a)});
  if(!hs.length)rail.innerHTML='';
}
function update(){
  ticking=false;var y=window.scrollY+110,i=0;
  for(var k=0;k<caps.length;k++){if(caps[k].offsetTop<=y)i=k;else break}
  if(i!==active){
    if(active>=0)links[active].classList.remove('on');
    active=i;links[i].classList.add('on');cur.textContent=links[i].dataset.t;mc.textContent='Cap. '+(links[i].querySelector('.num').textContent||(i+1))+' / '+caps.length;mp.disabled=i===0;mn.disabled=i===caps.length-1;
    var r=links[i].getBoundingClientRect(),t=toc.getBoundingClientRect();
    if(r.top<t.top||r.bottom>t.bottom)links[i].scrollIntoView({block:'center'});
    buildRail(i);
  }
  var f=-1;for(var j=0;j<hs.length;j++){if(hs[j].getBoundingClientRect().top<=140)f=j;else break}
  railLinks.forEach(function(a,j){a.classList.toggle('on',j===f)});
  var h=document.documentElement.scrollHeight-window.innerHeight;prog.style.width=(h>0?Math.min(100,window.scrollY/h*100):0)+'%';
  savePos();
}
var st=null;function savePos(){clearTimeout(st);st=setTimeout(function(){if(window.scrollY>300)ls('riass-pos:'+SLUG,JSON.stringify({id:caps[active].id,t:links[active].dataset.t,y:Math.round(window.scrollY),m:body.dataset.nome,u:location.pathname,ts:Date.now()}))},500)}
window.addEventListener('scroll',function(){if(!ticking){ticking=true;requestAnimationFrame(update)}},{passive:true});
window.addEventListener('resize',update);update();

/* telefono: pannelli dal basso, ricerca a scomparsa, capitolo precedente/successivo */
function closeAll(){ctrls.classList.remove('open');toc.classList.remove('open');scrim.classList.remove('on')}
function openPanel(el){var was=el.classList.contains('open');closeAll();if(!was){el.classList.add('open');scrim.classList.add('on')}}
$('#mopts').addEventListener('click',function(){openPanel(ctrls)});
$('#mcap').addEventListener('click',function(){openPanel(toc);var a=$('a.on',toc);if(a)a.scrollIntoView({block:'center'})});
scrim.addEventListener('click',closeAll);
links.forEach(function(a){a.addEventListener('click',function(e){if(window.innerWidth<=900){e.preventDefault();closeAll();var id=a.getAttribute('href').slice(1),t=document.getElementById(id);if(t){t.scrollIntoView({behavior:'instant'});history.replaceState(null,'','#'+id);update()}}})});
$('#msearch').addEventListener('click',function(){var t=$('.top');t.classList.toggle('srch');if(t.classList.contains('srch')){q.focus()}else{q.value='';q.dispatchEvent(new Event('input'))}});
function jump(d){var n=Math.max(0,Math.min(caps.length-1,active+d));caps[n].scrollIntoView({behavior:'instant'});history.replaceState(null,'','#'+caps[n].id);update()}
mp.addEventListener('click',function(){jump(-1)});mn.addEventListener('click',function(){jump(1)});
document.addEventListener('keydown',function(e){if(e.key==='Escape')closeAll()});

/* riprendi da dove eri */
var toast=$('#toast');
function say(html,ms){toast.innerHTML=html;toast.classList.add('on');if(ms)setTimeout(function(){toast.classList.remove('on')},ms)}
(function(){if(location.hash)return;var p=null;try{p=JSON.parse(ls('riass-pos:'+SLUG))}catch(e){}if(!p||!p.id||!document.getElementById(p.id))return;
  say('Riprendi da: <b>'+p.t.replace(/</g,'&lt;')+'</b> <button class="tb" id="go">Vai</button> <button class="tb" id="no">&times;</button>',12000);
  $('#go').onclick=function(){window.scrollTo({top:p.y,behavior:'auto'});toast.classList.remove('on')};$('#no').onclick=function(){toast.classList.remove('on')}})();

/* ricerca nel testo */
var cnt=$('#cnt'),hits=[],ci=-1,t=null;
function clear(){$$('span.hit',main).forEach(function(s){var p=s.parentNode;p.replaceChild(document.createTextNode(s.textContent),s);p.normalize()});hits=[];ci=-1;cnt.textContent=''}
function go(d){if(!hits.length)return;if(ci>=0)hits[ci].classList.remove('cur');ci=(ci+d+hits.length)%hits.length;hits[ci].classList.add('cur');hits[ci].scrollIntoView({block:'center'});cnt.textContent=(ci+1)+' / '+hits.length}
function run(){clear();var k=q.value.trim();if(k.length<3)return;
  var re=new RegExp(k.replace(/[.*+?^${}()|[\]\\]/g,'\\$&'),'gi'),w=document.createTreeWalker(main,NodeFilter.SHOW_TEXT,{acceptNode:function(n){return n.parentNode.closest('script,style')?NodeFilter.FILTER_REJECT:NodeFilter.FILTER_ACCEPT}}),nodes=[];
  while(w.nextNode())nodes.push(w.currentNode);
  nodes.forEach(function(nd){if(hits.length>500)return;re.lastIndex=0;if(!re.test(nd.nodeValue))return;re.lastIndex=0;
    var f=document.createDocumentFragment(),s=nd.nodeValue,l=0,m;
    while((m=re.exec(s))){f.appendChild(document.createTextNode(s.slice(l,m.index)));var sp=document.createElement('span');sp.className='hit';sp.textContent=m[0];f.appendChild(sp);hits.push(sp);l=m.index+m[0].length;if(m[0].length===0)re.lastIndex++}
    f.appendChild(document.createTextNode(s.slice(l)));nd.parentNode.replaceChild(f,nd)});
  if(!hits.length){cnt.textContent='nessuno';return}go(1)}
q.addEventListener('input',function(){clearTimeout(t);t=setTimeout(run,250)});
q.addEventListener('keydown',function(e){if(e.key==='Enter'){e.preventDefault();go(e.shiftKey?-1:1)}else if(e.key==='Escape'){q.value='';clear();q.blur()}});
$('#sp').addEventListener('click',function(){go(-1)});$('#sn').addEventListener('click',function(){go(1)});

/* scorciatoie: / cerca, j/k capitolo, h evidenziazioni */
document.addEventListener('keydown',function(e){
  if((e.target.closest&&e.target.closest('input,select,textarea'))||e.ctrlKey||e.metaKey||e.altKey)return;
  if(e.key==='/'){e.preventDefault();q.focus();q.select()}
  else if(e.key==='j'||e.key==='k'){jump(e.key==='j'?1:-1)}
  else if(e.key==='h'){setHl(body.classList.contains('nomark'))}
  else if(e.key==='Escape'){$('#lb').classList.remove('on')}
});

/* torna su e link alle sezioni */
var totop=$('#totop');totop.addEventListener('click',function(){window.scrollTo({top:0,behavior:'instant'})});
window.addEventListener('scroll',function(){totop.classList.toggle('on',window.scrollY>1400)},{passive:true});
main.addEventListener('click',function(e){var a=e.target.closest('a.ha');if(!a)return;e.preventDefault();var id=a.getAttribute('href').slice(1),u=location.origin+location.pathname+'#'+id;
  history.replaceState(null,'','#'+id);(navigator.clipboard?navigator.clipboard.writeText(u):Promise.reject()).then(function(){say('Link alla sezione copiato',2000)},function(){say('Link: '+u,4000)})});

/* copia il codice, ingrandisci le figure */
$$('pre',main).forEach(function(p){var b=document.createElement('button');b.className='tb cp';b.type='button';b.textContent='Copia';
  b.addEventListener('click',function(){var tx=p.innerText.replace(/Copia$/,'').replace(/\s+$/,'');(navigator.clipboard?navigator.clipboard.writeText(tx):Promise.reject()).then(function(){b.textContent='Copiato'},function(){b.textContent='Errore'});setTimeout(function(){b.textContent='Copia'},1500)});p.appendChild(b)});
var lb=$('#lb'),lbi=$('#lb img');
main.addEventListener('click',function(e){var im=e.target.closest('figure img');if(im){lbi.src=im.src;lb.classList.add('on')}});
lb.addEventListener('click',function(){lb.classList.remove('on')});
})();
"""

JS_INDICE = r"""
(function(){
var tb=document.getElementById('theme');
function ls(k,v){try{if(v===undefined)return localStorage.getItem(k);localStorage.setItem(k,v)}catch(e){return null}}
function lab(){var t=ls('quaderno-tema')||'auto',nm={auto:'automatico',light:'chiaro',dark:'scuro'}[t]||'automatico';tb.dataset.t=t;tb.title='Tema: '+nm+' (tocca per cambiare)';tb.setAttribute('aria-label','Tema: '+nm+', tocca per cambiare')}
if(tb){lab();tb.addEventListener('click',function(){var t=ls('quaderno-tema')||'auto',n={auto:'light',light:'dark',dark:'auto'}[t]||'auto';ls('quaderno-tema',n);if(n==='auto')document.documentElement.removeAttribute('data-theme');else document.documentElement.setAttribute('data-theme',n);lab()})}
})();
(function(){
var el=document.getElementById('resume'),best=null;
['algebra','matematica-discreta','fondamenti','programmazione','laboratorio'].forEach(function(s){try{var p=JSON.parse(localStorage.getItem('riass-pos:'+s));if(p&&p.u&&p.m&&(!best||(p.ts||0)>(best.ts||0)))best=p;}catch(e){}});
if(best){el.style.display='block';el.innerHTML='Continua da dove eri: <a href="'+best.u+'#'+best.id+'">'+best.m+' &mdash; '+best.t.replace(/</g,'&lt;')+'</a>'}
})();
"""


def pagina(titolo, head_extra, corpo, js=""):
    return ("<!doctype html><html lang=\"it\"><head><meta charset=\"utf-8\"><meta name=\"viewport\" content=\"width=device-width,initial-scale=1,viewport-fit=cover\"><meta name=\"theme-color\" media=\"(prefers-color-scheme:light)\" content=\"#fbfaf7\"><meta name=\"theme-color\" media=\"(prefers-color-scheme:dark)\" content=\"#14171d\"><link rel=\"manifest\" href=\"/manifest.webmanifest\"><link rel=\"apple-touch-icon\" href=\"/apple-touch-icon.png\"><meta name=\"mobile-web-app-capable\" content=\"yes\"><meta name=\"apple-mobile-web-app-capable\" content=\"yes\"><meta name=\"apple-mobile-web-app-title\" content=\"Quaderno\">"
            "<meta name=\"robots\" content=\"noindex,nofollow,noarchive\"><meta name=\"color-scheme\" content=\"light dark\">"
            f"<title>{html.escape(titolo)}</title><script>{JS_COMUNE}</script><style>{CSS}</style>{head_extra}</head>{corpo}</html>")


def numbering_kinds(d):
    """Restituisce {(numId, ilvl): 'ol'|'ul'} leggendo numbering.xml."""
    kinds = {}
    try:
        root = d.part.numbering_part.element
    except Exception:
        return kinds
    abstr = {}
    for a in root.findall(qn("w:abstractNum")):
        aid = a.get(qn("w:abstractNumId"))
        for lv in a.findall(qn("w:lvl")):
            f = lv.find(qn("w:numFmt"))
            abstr[(aid, lv.get(qn("w:ilvl")))] = (f.get(qn("w:val")) if f is not None else "bullet")
    for n in root.findall(qn("w:num")):
        a = n.find(qn("w:abstractNumId"))
        if a is None:
            continue
        for (aid, il), fmt in abstr.items():
            if aid == a.get(qn("w:val")):
                kinds[(n.get(qn("w:numId")), il)] = "ul" if fmt in ("bullet", "none") else "ol"
    return kinds


class Conv:
    def __init__(self, d, outdir):
        self.d, self.out = d, outdir
        self.imgdir = outdir / "img"
        self.imgdir.mkdir(parents=True, exist_ok=True)
        self.kinds = numbering_kinds(d)
        self.nimg = 0

    # ---- figure
    def immagine(self, drawing):
        blip = drawing.find(".//" + "{http://schemas.openxmlformats.org/drawingml/2006/main}blip")
        if blip is None:
            return ""
        rid = blip.get("{http://schemas.openxmlformats.org/officeDocument/2006/relationships}embed")
        try:
            part = self.d.part.related_parts[rid]
        except KeyError:
            return ""
        blob = part.blob
        ext = EXT.get(part.content_type, "png")
        name = hashlib.sha1(blob).hexdigest()[:14] + "." + ext
        f = self.imgdir / name
        if not f.exists():
            f.write_bytes(blob)
        self.nimg += 1
        ext_el = drawing.find(".//{http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing}extent")
        style = ""
        if ext_el is not None and ext_el.get("cx"):
            cx, cy = int(ext_el.get("cx")), int(ext_el.get("cy") or 0)
            style = f' style="width:{cx // 9525}px' + (f';aspect-ratio:{cx}/{cy}' if cy else "") + '"'
        return f'<figure><img src="img/{name}" loading="lazy" alt="Figura"{style}></figure>'

    # ---- run -> html
    def run(self, r):
        parts = []
        for ch in r._r:
            if ch.tag == W + "t":
                parts.append(html.escape(ch.text or ""))
            elif ch.tag == W + "tab":
                parts.append("&emsp;")
            elif ch.tag in (W + "br", W + "cr"):
                parts.append("<br>")
            elif ch.tag == W + "drawing":
                parts.append("\x00" + self.immagine(ch) + "\x00")
        t = "".join(parts)
        if not t.strip("\x00 "):
            return t
        f = r.font
        if f.name and "consolas" in f.name.lower():
            t = f"<code>{t}</code>"
        if f.superscript:
            t = f"<sup>{t}</sup>"
        elif f.subscript:
            t = f"<sub>{t}</sub>"
        if f.bold:
            t = f"<strong>{t}</strong>"
        if f.italic:
            t = f"<em>{t}</em>"
        if f.highlight_color is not None:
            t = f"<mark>{t}</mark>"
        return t

    def par_html(self, p):
        s = "".join(self.run(r) for r in p.runs)
        figs = re.findall("\x00(.*?)\x00", s, flags=re.S)
        s = re.sub("\x00.*?\x00", "", s, flags=re.S)
        return s, "".join(figs)

    def solo_codice(self, p):
        rs = [r for r in p.runs if r.text.strip()]
        return bool(rs) and all(r.font.name and "consolas" in r.font.name.lower() for r in rs)

    # ---- documento: restituisce una lista di capitoli
    def converti(self):
        """-> (preambolo_html, [ {id, titolo, html, marks} ... ])"""
        body = self.d.element.body
        capitoli = []        # chiusi
        cur = {"pre": []}    # capitolo in costruzione ("pre" = html fuori dai capitoli)
        out = cur["pre"]
        lista = []
        pre = []

        def chiudi_liste(fino=-1):
            while lista and lista[-1][1] > fino:
                out.append(f"</li></{lista.pop()[0]}>")

        def chiudi_pre():
            if pre:
                out.append("<pre><code>" + "\n".join(pre) + "</code></pre>")
                pre.clear()

        n_h = 0
        marks = 0
        capo = None          # dizionario del capitolo corrente
        preambolo = None
        for el in body.iterchildren():
            if el.tag == W + "tbl":
                chiudi_liste(); chiudi_pre()
                out.append(self.tabella(docx.table.Table(el, self.d)))
                continue
            if el.tag != W + "p":
                continue
            p = docx.text.paragraph.Paragraph(el, self.d)
            stile = p.style.name if p.style is not None else ""
            testo = p.text.strip()
            s, figs = self.par_html(p)
            if not testo and not figs:
                continue
            if stile.startswith("Heading"):
                chiudi_liste(); chiudi_pre()
                lv = 2 if stile.endswith("1") else 3
                n_h += 1
                hid = f"s{n_h}"
                titolo_pl = html.unescape(re.sub("<[^>]+>", "", s))
                h = re.sub("</?(strong|em|mark|code)>", "", s)
                if lv == 2:
                    if capo is None:
                        preambolo = "".join(out)
                    else:
                        capo["html"] = "".join(out); capo["marks"] = marks
                        capitoli.append(capo)
                    out = []; marks = 0
                    capo = {"id": hid, "titolo": titolo_pl}
                    out.append(f'<h2 id="{hid}">{h}<a class="ha" href="#{hid}" aria-label="Copia il link a questa sezione"></a></h2>')
                else:
                    out.append(f'<h3 id="{hid}">{h}<a class="ha" href="#{hid}" aria-label="Copia il link a questa sezione"></a></h3>')
                continue
            if "<mark>" in s:
                marks += 1
            if self.solo_codice(p) and not figs:
                chiudi_liste()
                pre.append(re.sub(r"</?code>", "", s))
                continue
            chiudi_pre()
            numpr = p._p.pPr.numPr if p._p.pPr is not None else None
            if numpr is not None and numpr.numId is not None and testo:
                il = int(numpr.ilvl.val) if numpr.ilvl is not None else 0
                kind = self.kinds.get((str(numpr.numId.val), str(il)), "ul")
                while lista and lista[-1][1] > il:
                    out.append(f"</li></{lista.pop()[0]}>")
                if lista and lista[-1][1] == il:
                    out.append("</li><li>")
                else:
                    lista.append((kind, il)); out.append(f"<{kind}><li>")
                out.append(s)
                if figs:
                    out.append(figs)
                continue
            chiudi_liste()
            if s.strip():
                if re.match(r"^\s*(?:<[^>]+>)*\(?\s*In parole povere", s, flags=re.I):
                    # riquadro "In parole povere": l'etichetta la mette lo stile, tolgo la dicitura e le parentesi duplicate
                    s2 = re.sub(r"^(\s*(?:<[^>]+>)*)\(?\s*In parole povere\s*:?\s*", r"\1", s, count=1, flags=re.I)
                    s2 = re.sub(r"\)\s*((?:</[^>]+>)*)\s*$", r"\1", s2) if re.match(r"^\s*(?:<[^>]+>)*\(", s) else s2
                    s2 = re.sub(r"<(strong|em|mark|code)>\s*</\1>", "", s2)            # tag rimasti vuoti
                    s2 = re.sub(r"^((?:\s|<[^>]+>)*)([a-zàèéìòù])", lambda m: m.group(1) + m.group(2).upper(), s2, count=1)   # inizia con la maiuscola
                    out.append(f'<p class="pp">{s2.strip()}</p>')
                else:
                    out.append(f"<p>{s}</p>")
            if figs:
                out.append(figs)
        chiudi_liste(); chiudi_pre()
        if capo is not None:
            capo["html"] = "".join(out); capo["marks"] = marks
            capitoli.append(capo)
        return (preambolo or ""), capitoli

    def tabella(self, t):
        righe = []
        for row in t.rows:
            celle = []
            for c in row.cells:
                celle.append("<td>" + "<br>".join(self.par_html(p)[0] for p in c.paragraphs if p.text.strip()) + "</td>")
            righe.append("<tr>" + "".join(celle) + "</tr>")
        return "<table>" + "".join(righe) + "</table>"


def numero(titolo):
    m = re.match(r"^\s*(?:Capitolo\s+)?(\d+)\b", titolo)
    return int(m.group(1)) if m else None


def breve(titolo):
    return re.sub(r"^\s*(?:Capitolo\s+)?\d+\s*[.:]?\s*", "", titolo)


def stato(cap, manuali):
    n = numero(cap["titolo"])
    if n is not None and n in manuali:
        return 2
    m = cap["marks"]
    return 2 if m >= 3 else (1 if m else 0)   # stessa regola del Quaderno: da 3 paragrafi evidenziati = studiato


def minuti(htm):
    return max(1, round(len(re.sub(r"<[^>]+>", " ", htm).split()) / 190))


def durata(m):
    h, mm = divmod(m, 60)
    return f"{h} h {mm:02d} min" if h else f"{mm} min"


IC_CERCA = '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="11" cy="11" r="6.5"/><path d="M16 16l4.5 4.5"/></svg>'
IC_OPZ = '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="5" cy="12" r="1.3"/><circle cx="12" cy="12" r="1.3"/><circle cx="19" cy="12" r="1.3"/></svg>'

IC_TEMA = ('<svg class="t-auto" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="8.5"/><path d="M12 3.5v17" /><path d="M12 3.5a8.5 8.5 0 0 1 0 17z" fill="currentColor" stroke="none"/></svg>'
           '<svg class="t-light" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2.5v2.3M12 19.2v2.3M2.5 12h2.3M19.2 12h2.3M5.3 5.3l1.6 1.6M17.1 17.1l1.6 1.6M18.7 5.3l-1.6 1.6M6.9 17.1l-1.6 1.6"/></svg>'
           '<svg class="t-dark" viewBox="0 0 24 24" aria-hidden="true"><path d="M20 14.5A8.5 8.5 0 0 1 9.5 4a8.5 8.5 0 1 0 10.5 10.5z"/></svg>')
IC_SU = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 19V5M5.5 11.5L12 5l6.5 6.5"/></svg>'
ETICHETTE = ["Da studiare", "Iniziato", "Studiato"]


def main(argv):
    if len(argv) != 2:
        print(__doc__); return 1
    base = Path(argv[1]) / "riassunti"
    base.mkdir(parents=True, exist_ok=True)
    try:
        manuale = json.loads((BASE / "studiato_manuale.json").read_text(encoding="utf-8"))
    except Exception:
        manuale = {}
    opzioni = "".join(f'<option value="{s}.html">{html.escape(n)}</option>' for s, n, _f, _k in MATERIE)
    schede = []
    for slug, nome, f, chiave in MATERIE:
        src = UNI / f
        if not src.exists():
            print("manca", src); continue
        d = docx.Document(str(src))
        c = Conv(d, base)
        pre, caps = c.converti()
        man = set(manuale.get(chiave) or [])
        st = [stato(cp, man) for cp in caps]
        usati = set()
        for cp in caps:                      # id dei capitoli: cap<N> (usato anche dai link dal Quaderno)
            n = numero(cp["titolo"])
            cp["sid"] = f"cap{n}" if n is not None and n not in usati else f"c{cp['id']}"
            if n is not None:
                usati.add(n)
            cp["min"] = minuti(cp["html"])
        tot_min = sum(cp["min"] for cp in caps)
        voci, quadr = [], []
        for i, cp in enumerate(caps):
            n = numero(cp["titolo"])
            voci.append(f'<a href="#{cp["id"]}" data-cap="{i}" data-t="{html.escape(cp["titolo"], quote=True)}">'
                        f'<span class="num">{n if n is not None else ""}</span><span class="ttl">{html.escape(breve(cp["titolo"]))}</span>'
                        f'<span class="st st{st[i]}" title="{ETICHETTE[st[i]].lower()}"></span></a>')
            quadr.append(f'<a class="st{st[i]}" href="#{cp["sid"]}" title="{html.escape(cp["titolo"], quote=True)} ({ETICHETTE[st[i]].lower()})">{n if n is not None else i + 1}</a>')
        prossimo = next((i for i, x in enumerate(st) if x != 2), None)
        fatti = sum(1 for x in st if x == 2); inz = sum(1 for x in st if x == 1); tot = len(caps)
        if prossimo is None:
            btn = f'<a class="btn" href="#{caps[0]["sid"]}">Ripassa dall&rsquo;inizio</a>'
        else:
            nn = numero(caps[prossimo]["titolo"])
            etichetta = f"Continua dal capitolo {nn}" if nn is not None else "Continua a leggere"
            btn = (f'<a class="btn" href="#{caps[prossimo]["sid"]}">{etichetta}</a>'
                   f'<a class="btn ghost" href="#{caps[0]["sid"]}">Dall&rsquo;inizio</a>')
        extra_inz = f", {inz} iniziati" if inz else ""
        hero = (f'<div class="hero"><h1>{html.escape(nome)}</h1>'
                f'<p>{tot} capitoli &middot; {fatti} studiati{extra_inz} &middot; lettura di circa {durata(tot_min)}</p>'
                f'<div class="map" role="navigation" aria-label="Mappa dei capitoli">{"".join(quadr)}</div>'
                f'<div class="leg">Pieno = studiato &middot; a metà = iniziato &middot; vuoto = da studiare</div>'
                f'<div class="act">{btn}</div></div>')
        sezioni = []
        for i, cp in enumerate(caps):
            nav = '<div class="pn">'
            if i > 0:
                nav += f'<a class="prev" href="#{caps[i-1]["sid"]}"><small>&larr; Capitolo precedente</small>{html.escape(caps[i-1]["titolo"])}</a>'
            else:
                nav += "<span></span>"
            if i + 1 < len(caps):
                nav += f'<a class="next" href="#{caps[i+1]["sid"]}"><small>Capitolo successivo &rarr;</small>{html.escape(caps[i+1]["titolo"])}</a>'
            else:
                nav += "<span></span>"
            nav += "</div>"
            meta = f'<div class="capmeta"><span class="badge b{st[i]}"><i></i>{ETICHETTE[st[i]]}</span><span>{cp["min"]} min di lettura</span></div>'
            corpo_cap = cp["html"].replace("</h2>", "</h2>" + meta, 1)
            sezioni.append(f'<section class="cap" id="{cp["sid"]}" data-num="{numero(cp["titolo"]) or ""}">{corpo_cap}{nav}</section>')
        top = ('<header class="top"><div class="top-in">'
               '<a class="back" href="../" aria-label="Torna al Quaderno">&larr; Quaderno</a>'
               f'<span class="mat">{html.escape(nome)}</span><span class="cur" id="cur"></span>'
               '<div class="search">' + IC_CERCA + '<input id="q" type="search" placeholder="Cerca nel testo   ( / )" aria-label="Cerca nel testo" autocomplete="off">'
               '<span class="n" id="cnt"></span><button id="sp" type="button" title="Precedente (Maiusc+Invio)">&uarr;</button><button id="sn" type="button" title="Successivo (Invio)">&darr;</button></div>'
               '<button id="msearch" type="button" aria-label="Cerca nel testo">' + IC_CERCA + '</button>'
               '<button id="mopts" type="button" aria-label="Opzioni di lettura">' + IC_OPZ + '</button>'
               '<div id="ctrls" role="group" aria-label="Opzioni di lettura">'
               '<select class="tb mats" id="mats" aria-label="Cambia materia">' + opzioni.replace(f'value="{slug}.html"', f'value="{slug}.html" selected') + '</select>'
               '<div class="segm" role="group" aria-label="Dimensione del testo"><button id="fsm" type="button" title="Testo più piccolo" aria-label="Testo più piccolo"><span class="a-s">A</span></button>'
               '<button id="fsp" type="button" title="Testo più grande" aria-label="Testo più grande"><span class="a-l">A</span></button></div>'
               '<button class="sw-btn" id="hl" type="button" role="switch" aria-checked="true" title="Mostra o nascondi le evidenziazioni (h)"><span class="sw"></span><span>Evidenziazioni</span></button>'
               '<button class="ibtn" id="theme" type="button" data-t="auto">' + IC_TEMA + '<span class="lbl">Tema</span></button></div>'
               '</div><div id="prog"></div></header>')
        cl, cd = COLORI[slug]
        corpo = (f'<body data-slug="{slug}" data-nome="{html.escape(nome, quote=True)}" style="--mcl:{cl};--mcd:{cd}"><a class="skip" href="#main">Vai al contenuto</a>{top}'
                 f'<div class="wrap"><nav class="toc"><h4>Capitoli</h4>{"".join(voci)}</nav>'
                 f'<main id="main">{hero}{pre}{"".join(sezioni)}</main><aside class="rail"></aside></div>'
                 '<button id="totop" type="button" aria-label="Torna in cima">' + IC_SU + '</button>'
                 '<div id="scrim"></div><div id="mbar"><button id="mprev" type="button" aria-label="Capitolo precedente">&lsaquo;</button>'
                 '<button id="mcap" type="button" aria-label="Elenco dei capitoli">Capitoli</button>'
                 '<button id="mnext" type="button" aria-label="Capitolo successivo">&rsaquo;</button></div>'
                 '<div id="toast" role="status"></div><div id="lb"><img alt=""></div>'
                 f'<script>{JS_PAGINA}</script></body>')
        (base / f"{slug}.html").write_text(pagina(f"{nome} - Riassunto", "", corpo), encoding="utf-8")
        nxt = None if prossimo is None else (numero(caps[prossimo]["titolo"]), breve(caps[prossimo]["titolo"]), caps[prossimo]["sid"])
        schede.append((slug, nome, tot, fatti, inz, nxt, tot_min))
        print(f"{nome}: {tot} capitoli ({fatti} studiati), {c.nimg} figure")
    cards = ""
    for s, n, k, fatti, inz, nxt, tmin in schede:
        pct = round(100 * fatti / k) if k else 0
        cl, cd = COLORI[s]
        if nxt:
            num, tit, sid = nxt
            prefisso = f"Cap. {num} &middot; " if num is not None else ""
            nxt_html = f"Prossimo da studiare: <b>{prefisso}{html.escape(tit)}</b>"
            href = f"{s}.html#{sid}"
        else:
            nxt_html = "Hai studiato tutto: puoi ripassare dall&rsquo;inizio."
            href = f"{s}.html"
        extra_inz = f" &middot; {inz} iniziati" if inz else ""
        vai = "Continua" if nxt else "Apri"
        cards += (f'<a class="mcard" href="{href}" style="--mcl:{cl};--mcd:{cd}"><div class="mc-top"><span class="mc-nm">{html.escape(n)}</span><span class="mc-pct">{pct}%</span></div>'
                  f'<div class="bar"><i style="width:{pct}%"></i></div>'
                  f'<div class="mc-sub">{fatti} di {k} capitoli studiati{extra_inz} &middot; circa {durata(tmin)} di lettura</div>'
                  f'<div class="mc-next">{nxt_html}</div><span class="mc-go">{vai} &rarr;</span></a>')
    ora = datetime.now().strftime("%d/%m/%Y alle %H:%M")
    idx = ('<body><a class="skip" href="#main">Vai al contenuto</a>'
           '<header class="top idx-top"><div class="top-in"><a class="back" href="../" aria-label="Torna al Quaderno">&larr; Quaderno</a><span class="mat">Riassunti</span><span class="grow"></span>'
           '<button class="ibtn" id="theme" type="button" data-t="auto" aria-label="Cambia tema">' + IC_TEMA + '</button></div></header>'
           '<div class="idx" id="main"><h1>Riassunti</h1><p class="lead">Scegli una materia: il pulsante ti porta al primo capitolo che non hai ancora studiato.</p>'
           f'<div id="resume"></div><div class="grid">{cards}</div>'
           f'<p class="foot">Aggiornato il {ora}. Nella pagina di lettura: <kbd>/</kbd> cerca, <kbd>j</kbd> e <kbd>k</kbd> cambiano capitolo, <kbd>h</kbd> mostra o nasconde le evidenziazioni.</p></div>'
           f'<script>{JS_INDICE}</script></body>')
    (base / "index.html").write_text(pagina("Riassunti", "", idx), encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
