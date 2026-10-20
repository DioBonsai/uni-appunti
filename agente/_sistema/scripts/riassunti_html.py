"""Converte i 5 Word dei riassunti in pagine HTML per il Quaderno online (con le evidenziazioni gialle, il codice,
apici/pedici e le figure). Non modifica mai i Word.

Uso: python riassunti_html.py <cartella_uscita>
Scrive: <uscita>/riassunti/index.html, <uscita>/riassunti/<slug>.html, <uscita>/riassunti/img/<hash>.<ext>
"""
import hashlib
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
EXT = {"image/png": "png", "image/jpeg": "jpg", "image/gif": "gif", "image/svg+xml": "svg", "image/webp": "webp"}
W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"

CSS = r"""
:root{--bg:#fbfaf7;--fg:#1d2330;--mut:#667085;--lin:#e3e0d8;--acc:#1f4e9c;--tit:#b42318;--sub:#b54708;--cod:#f1efe9;--mark:#fff59d;--card:#ffffff;--bar:#fbfaf7e8;--ok:#1e8449;--hl:#ffd54f;--fs:18px}
@media (prefers-color-scheme:dark){:root:not([data-theme=light]){--bg:#14171d;--fg:#e3e6ec;--mut:#98a1b3;--lin:#2a2f3a;--acc:#8fb4ff;--tit:#ff8f80;--sub:#ffb066;--cod:#1c2029;--mark:#6a5c00;--card:#1a1e26;--bar:#14171de8;--ok:#5fd08a;--hl:#a88400}}
:root[data-theme=dark]{--bg:#14171d;--fg:#e3e6ec;--mut:#98a1b3;--lin:#2a2f3a;--acc:#8fb4ff;--tit:#ff8f80;--sub:#ffb066;--cod:#1c2029;--mark:#6a5c00;--card:#1a1e26;--bar:#14171de8;--ok:#5fd08a;--hl:#a88400}
*{box-sizing:border-box}html{scroll-behavior:smooth;scroll-padding-top:72px;-webkit-text-size-adjust:100%}
body{margin:0;background:var(--bg);color:var(--fg);font:var(--fs)/1.72 "Iowan Old Style","Palatino Linotype",Palatino,Georgia,serif;text-rendering:optimizeLegibility}
a{color:var(--acc)}button,input,select{font:inherit}
.sans{font-family:system-ui,-apple-system,"Segoe UI",Roboto,sans-serif}
/* barra in alto */
.top{position:sticky;top:0;z-index:20;background:var(--bar);backdrop-filter:blur(8px);border-bottom:1px solid var(--lin);font:14px/1.2 system-ui,-apple-system,"Segoe UI",sans-serif}
.top-in{max-width:94rem;margin:0 auto;padding:.5rem 1rem;display:flex;align-items:center;gap:.6rem;flex-wrap:wrap}
.top a.back{text-decoration:none;font-weight:600;white-space:nowrap}
.top .mat{font-weight:700;white-space:nowrap}
.top .cur{color:var(--mut);white-space:nowrap;overflow:hidden;text-overflow:ellipsis;max-width:28rem;min-width:0;flex:1 1 8rem}
.top .grow{flex:1}
.tb{appearance:none;border:1px solid var(--lin);background:var(--card);color:var(--fg);border-radius:8px;padding:.32rem .6rem;cursor:pointer;line-height:1.2}
.tb:hover{border-color:var(--acc)}.tb[aria-pressed=true]{background:var(--mark)}
select.tb{max-width:8.6rem;text-overflow:ellipsis}
#tocbtn{display:none}
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
@media (max-width:900px){.wrap{display:block}nav.toc{position:static;max-height:none;padding:0 0 .8rem;margin-bottom:.8rem;border-bottom:1px solid var(--lin)}nav.toc.coll{max-height:0;overflow:hidden;padding:0;margin:0;border:0}#tocbtn{display:inline-block}.top .cur{display:none}.search input{width:7rem}:root{--fs:17px}}
@media print{.top,nav.toc,aside.rail,.pn,#toast,#lb,.cp{display:none!important}.wrap{display:block;padding:0}body{background:#fff;color:#000;font-size:11pt}main h2{break-before:page;border:0}main section.cap:first-child h2{break-before:auto}mark{background:#fff59d!important;-webkit-print-color-adjust:exact;print-color-adjust:exact}pre,figure{break-inside:avoid}}
/* indice delle materie */
.idx{max-width:48rem;margin:0 auto;padding:1.6rem 1rem 4rem}.idx h1{font:750 1.7rem system-ui,sans-serif;margin:.4rem 0 1.2rem}
.idx a.card{display:block;background:var(--card);border:1px solid var(--lin);border-radius:14px;padding:1rem 1.2rem;margin:.8rem 0;text-decoration:none;color:var(--fg);font-family:system-ui,sans-serif}
.idx a.card:hover{border-color:var(--acc)}.idx .nm{font-weight:700;font-size:1.1rem}.idx small{color:var(--mut);font-size:13px}
.idx .bar{height:6px;border-radius:99px;background:var(--lin);margin:.7rem 0 .25rem;overflow:hidden}.idx .bar i{display:block;height:100%;background:var(--ok)}
#resume{display:none;border:1px solid var(--acc);border-radius:14px;padding:.8rem 1.2rem;margin:.4rem 0 1.2rem;font:15px system-ui,sans-serif;background:var(--card)}#resume a{font-weight:700}
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

/* evidenziazioni, tema, dimensione del testo */
var hl=$('#hl');function setHl(on){body.classList.toggle('nomark',!on);hl.setAttribute('aria-pressed',on?'true':'false');ls('riass-evid',on?'1':'0')}
setHl(ls('riass-evid')!=='0');hl.addEventListener('click',function(){setHl(body.classList.contains('nomark'))});
var tb=$('#theme');function lab(){var t=ls('quaderno-tema')||'auto';tb.textContent='Tema: '+({auto:'auto',light:'chiaro',dark:'scuro'}[t]||'auto')}
lab();tb.addEventListener('click',function(){var t=ls('quaderno-tema')||'auto',n={auto:'light',light:'dark',dark:'auto'}[t]||'auto';ls('quaderno-tema',n);if(n==='auto')root.removeAttribute('data-theme');else root.setAttribute('data-theme',n);lab()});
function size(d){var c=parseInt(getComputedStyle(root).getPropertyValue('--fs'),10)||18,n=Math.max(14,Math.min(24,c+d));root.style.setProperty('--fs',n+'px');ls('riass-fs',String(n))}
$('#fsm').addEventListener('click',function(){size(-1)});$('#fsp').addEventListener('click',function(){size(1)});
$('#mats').addEventListener('change',function(e){if(e.target.value)location.href=e.target.value});
var tg=$('#tocbtn');if(tg)tg.addEventListener('click',function(){toc.classList.toggle('coll')});
if(window.innerWidth<=900)toc.classList.add('coll');

/* capitolo attivo, indice, barra di avanzamento */
var links=$$('a[data-cap]',toc),active=-1,hs=[],railLinks=[],ticking=false,cur=$('#cur'),prog=$('#prog');
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
    active=i;links[i].classList.add('on');cur.textContent=links[i].dataset.t;
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

/* riprendi da dove eri */
var toast=$('#toast');
function say(html,ms){toast.innerHTML=html;toast.classList.add('on');if(ms)setTimeout(function(){toast.classList.remove('on')},ms)}
(function(){if(location.hash)return;var p=null;try{p=JSON.parse(ls('riass-pos:'+SLUG))}catch(e){}if(!p||!p.id||!document.getElementById(p.id))return;
  say('Riprendi da: <b>'+p.t.replace(/</g,'&lt;')+'</b> <button class="tb" id="go">Vai</button> <button class="tb" id="no">&times;</button>',12000);
  $('#go').onclick=function(){window.scrollTo({top:p.y,behavior:'auto'});toast.classList.remove('on')};$('#no').onclick=function(){toast.classList.remove('on')}})();

/* ricerca nel testo */
var q=$('#q'),cnt=$('#cnt'),hits=[],ci=-1,t=null;
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
  else if(e.key==='j'||e.key==='k'){var n=Math.max(0,Math.min(caps.length-1,active+(e.key==='j'?1:-1)));caps[n].scrollIntoView({behavior:'instant'});history.replaceState(null,'','#'+caps[n].id);update()}
  else if(e.key==='h'){setHl(body.classList.contains('nomark'))}
  else if(e.key==='Escape'){$('#lb').classList.remove('on')}
});

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
var el=document.getElementById('resume'),best=null;
['algebra','matematica-discreta','fondamenti','programmazione','laboratorio'].forEach(function(s){try{var p=JSON.parse(localStorage.getItem('riass-pos:'+s));if(p&&p.u&&p.m&&(!best||(p.ts||0)>(best.ts||0)))best=p;}catch(e){}});
if(best){el.style.display='block';el.innerHTML='Continua da dove eri: <a href="'+best.u+'#'+best.id+'">'+best.m+' &mdash; '+best.t.replace(/</g,'&lt;')+'</a>'}
})();
"""


def pagina(titolo, head_extra, corpo, js=""):
    return ("<!doctype html><html lang=\"it\"><head><meta charset=\"utf-8\"><meta name=\"viewport\" content=\"width=device-width,initial-scale=1\">"
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
            style = f' style="width:{int(ext_el.get("cx")) // 9525}px"'
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
                    out.append(f'<h2 id="{hid}">{h}</h2>')
                else:
                    out.append(f'<h3 id="{hid}">{h}</h3>')
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
        voci = []
        for i, cp in enumerate(caps):
            n = numero(cp["titolo"])
            voci.append(f'<a href="#{cp["id"]}" data-cap="{i}" data-t="{html.escape(cp["titolo"], quote=True)}">'
                        f'<span class="num">{n if n is not None else ""}</span><span class="ttl">{html.escape(breve(cp["titolo"]))}</span>'
                        f'<span class="st st{st[i]}" title="{["da studiare", "iniziato", "studiato"][st[i]]}"></span></a>')
        sezioni = []
        for i, cp in enumerate(caps):
            nav = '<div class="pn">'
            nav += (f'<a class="prev" href="#{caps[i-1]["id"]}"><small>&larr; Capitolo precedente</small>{html.escape(caps[i-1]["titolo"])}</a>' if i > 0 else "<span></span>")
            nav += (f'<a class="next" href="#{caps[i+1]["id"]}"><small>Capitolo successivo &rarr;</small>{html.escape(caps[i+1]["titolo"])}</a>' if i + 1 < len(caps) else "<span></span>")
            nav += "</div>"
            sezioni.append(f'<section class="cap" id="c{cp["id"]}" data-id="{cp["id"]}">{cp["html"]}{nav}</section>')
        top = ('<header class="top"><div class="top-in">'
               '<a class="back" href="../">&larr; Quaderno</a>'
               '<select class="tb" id="mats" aria-label="Cambia materia"><option value="">Materie &#9662;</option>' + opzioni + '</select>'
               f'<span class="mat">{html.escape(nome)}</span><span class="cur" id="cur"></span>'
               '<div class="search"><input id="q" type="search" placeholder="Cerca  ( / )" aria-label="Cerca nel testo" autocomplete="off">'
               '<span class="n" id="cnt"></span><button id="sp" type="button" title="Precedente (Maiusc+Invio)">&uarr;</button><button id="sn" type="button" title="Successivo (Invio)">&darr;</button></div>'
               '<button class="tb" id="fsm" type="button" title="Testo più piccolo">A&minus;</button><button class="tb" id="fsp" type="button" title="Testo più grande">A+</button>'
               '<button class="tb" id="hl" type="button" aria-pressed="true" title="Mostra o nascondi le evidenziazioni (h)">Evidenziazioni</button>'
               '<button class="tb" id="theme" type="button">Tema</button>'
               '<button class="tb" id="tocbtn" type="button">Capitoli</button>'
               '</div><div id="prog"></div></header>')
        corpo = (f'<body data-slug="{slug}" data-nome="{html.escape(nome, quote=True)}">{top}'
                 f'<div class="wrap"><nav class="toc"><h4>Capitoli</h4>{"".join(voci)}</nav>'
                 f'<main>{pre}{"".join(sezioni)}</main><aside class="rail"></aside></div>'
                 '<div id="toast" role="status"></div><div id="lb"><img alt=""></div>'
                 f'<script>{JS_PAGINA}</script></body>')
        (base / f"{slug}.html").write_text(pagina(f"{nome} - Riassunto", "", corpo), encoding="utf-8")
        tot = len(caps); fatti = sum(1 for x in st if x == 2); inz = sum(1 for x in st if x == 1)
        schede.append((slug, nome, tot, c.nimg, fatti, inz))
        print(f"{nome}: {tot} capitoli ({fatti} studiati), {c.nimg} figure")
    cards = ""
    for s, n, k, m, fatti, inz in schede:
        pct = round(100 * fatti / k) if k else 0
        cards += (f'<a class="card" href="{s}.html"><span class="nm">{html.escape(n)}</span>'
                  f'<div class="bar"><i style="width:{pct}%"></i></div>'
                  f'<small>{k} capitoli &middot; {m} figure &middot; {fatti} studiati, {inz} iniziati</small></a>')
    idx = ('<body><header class="top"><div class="top-in"><a class="back" href="../">&larr; Quaderno</a><span class="mat">Riassunti</span></div></header>'
           f'<div class="idx"><h1>Riassunti</h1><div id="resume"></div>{cards}</div><script>{JS_INDICE}</script></body>')
    (base / "index.html").write_text(pagina("Riassunti", "", idx), encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
