"""Converte i 5 Word dei riassunti in pagine HTML per il Quaderno online (con le evidenziazioni gialle, il codice,
apici/pedici e le figure). Non modifica mai i Word.

Uso: python riassunti_html.py <cartella_uscita>
Scrive: <uscita>/riassunti/index.html, <uscita>/riassunti/<slug>.html, <uscita>/riassunti/img/<hash>.<ext>
"""
import hashlib
import html
import re
import sys
from pathlib import Path

import docx
from docx.oxml.ns import qn

UNI = Path(__file__).resolve().parents[3]
MATERIE = [
    ("algebra", "Algebra lineare", "Riassunto Algebra lineare.docx"),
    ("matematica-discreta", "Matematica discreta", "Riassunto Matematica discreta.docx"),
    ("fondamenti", "Fondamenti dell'Informatica", "Riassunto Fondamenti Informatica.docx"),
    ("programmazione", "Programmazione", "Riassunto Programmazione.docx"),
    ("laboratorio", "Programmazione, Laboratorio", "Riassunto Laboratorio.docx"),
]
EXT = {"image/png": "png", "image/jpeg": "jpg", "image/gif": "gif", "image/svg+xml": "svg", "image/webp": "webp"}
W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
CSS = """
:root{--bg:#fbfaf7;--fg:#1d2330;--mut:#667085;--lin:#e3e0d8;--acc:#1f4e9c;--tit:#c0392b;--sub:#d35400;--cod:#f0eee8;--mark:#fff176;--card:#fff}
@media (prefers-color-scheme:dark){:root{--bg:#14171d;--fg:#e6e8ee;--mut:#98a1b3;--lin:#2b303b;--acc:#8fb4ff;--tit:#ff8a7a;--sub:#ffb066;--cod:#1d222c;--mark:#6b5d00;--card:#1a1e26}}
*{box-sizing:border-box}html{scroll-behavior:smooth}
body{margin:0;background:var(--bg);color:var(--fg);font:17px/1.65 Georgia,"Times New Roman",serif}
a{color:var(--acc)}
.top{position:sticky;top:0;z-index:5;background:var(--bg);border-bottom:1px solid var(--lin);padding:.5rem 1rem;display:flex;gap:1rem;align-items:center;flex-wrap:wrap;font:14px system-ui,sans-serif}
.top b{font-size:15px}.top label{color:var(--mut);cursor:pointer}.top input[type=search]{padding:.3rem .5rem;border:1px solid var(--lin);border-radius:6px;background:var(--card);color:var(--fg);min-width:11rem}
.wrap{display:grid;grid-template-columns:minmax(0,17rem) minmax(0,1fr);gap:2rem;max-width:78rem;margin:0 auto;padding:1rem}
nav.toc{position:sticky;top:3.6rem;align-self:start;max-height:calc(100vh - 4.6rem);overflow:auto;font:14px/1.35 system-ui,sans-serif;border-right:1px solid var(--lin);padding-right:1rem}
nav.toc a{display:block;padding:.28rem .2rem;text-decoration:none;color:var(--fg)}nav.toc a:hover{color:var(--acc)}
main{min-width:0;padding-bottom:6rem}
main h2{color:var(--tit);font-size:1.55rem;margin:2.6rem 0 .6rem;padding-top:.6rem;border-top:2px solid var(--lin);scroll-margin-top:3.6rem}
main h3{color:var(--sub);font-size:1.15rem;margin:1.6rem 0 .3rem;scroll-margin-top:3.6rem}
p{margin:.55rem 0}ul,ol{margin:.5rem 0;padding-left:1.4rem}li{margin:.2rem 0}
mark{background:var(--mark);color:inherit;border-radius:2px;padding:0 1px}body.nomark mark{background:none}
code,pre{font:14.5px/1.45 Consolas,"Cascadia Mono",monospace}code{background:var(--cod);padding:0 .25rem;border-radius:3px}
pre{background:var(--cod);padding:.7rem .9rem;border-radius:8px;overflow:auto;margin:.7rem 0;border:1px solid var(--lin)}pre code{background:none;padding:0}
figure{margin:1rem 0;text-align:center}figure img{max-width:100%;height:auto;background:#fff;border-radius:6px}
table{border-collapse:collapse;margin:.8rem 0;font:15px system-ui,sans-serif}td,th{border:1px solid var(--lin);padding:.3rem .6rem}
.hit{background:#ffd54f;color:#000}
@media (max-width:820px){.wrap{display:block}nav.toc{position:static;max-height:none;border:0;border-bottom:1px solid var(--lin);margin-bottom:1rem;padding:0 0 .6rem}body{font-size:16px}}
.idx{max-width:46rem;margin:2rem auto;padding:0 1rem}.idx a.card{display:block;background:var(--card);border:1px solid var(--lin);border-radius:12px;padding:1rem 1.2rem;margin:.8rem 0;text-decoration:none;color:var(--fg)}
.idx a.card:hover{border-color:var(--acc)}.idx small{color:var(--mut);font:13px system-ui,sans-serif}
"""
JS = """
(function(){
var cb=document.getElementById('hl');
try{var v=localStorage.getItem('riass-evid');if(v==='0'){cb.checked=false;document.body.classList.add('nomark')}}catch(e){}
cb.addEventListener('change',function(){document.body.classList.toggle('nomark',!cb.checked);try{localStorage.setItem('riass-evid',cb.checked?'1':'0')}catch(e){}});
var q=document.getElementById('q'),main=document.querySelector('main');
function clear(){main.querySelectorAll('span.hit').forEach(function(s){var p=s.parentNode;p.replaceChild(document.createTextNode(s.textContent),s);p.normalize()})}
var t;q.addEventListener('input',function(){clearTimeout(t);t=setTimeout(function(){
 clear();var k=q.value.trim();if(k.length<3)return;var re=new RegExp(k.replace(/[.*+?^${}()|[\\]\\\\]/g,'\\\\$&'),'gi'),first=null,n=0;
 var w=document.createTreeWalker(main,NodeFilter.SHOW_TEXT),nodes=[];while(w.nextNode())nodes.push(w.currentNode);
 nodes.forEach(function(nd){if(n>300||!re.test(nd.nodeValue))return;re.lastIndex=0;var f=document.createDocumentFragment(),s=nd.nodeValue,l=0,m;
  while((m=re.exec(s))&&n<=300){f.appendChild(document.createTextNode(s.slice(l,m.index)));var sp=document.createElement('span');sp.className='hit';sp.textContent=m[0];f.appendChild(sp);if(!first)first=sp;l=m.index+m[0].length;n++}
  f.appendChild(document.createTextNode(s.slice(l)));nd.parentNode.replaceChild(f,nd)});
 if(first)first.scrollIntoView({block:'center'})},250)});
})();
"""


def pagina(titolo, corpo, extra_top="", toc=""):
    return f"""<!doctype html><html lang="it"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex,nofollow,noarchive"><title>{html.escape(titolo)}</title><style>{CSS}</style></head><body>
{corpo}</body></html>"""


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
        # le figure escono dal paragrafo
        figs = re.findall("\x00(.*?)\x00", s, flags=re.S)
        s = re.sub("\x00.*?\x00", "", s, flags=re.S)
        return s, "".join(figs)

    def solo_codice(self, p):
        rs = [r for r in p.runs if r.text.strip()]
        return bool(rs) and all(r.font.name and "consolas" in r.font.name.lower() for r in rs)

    # ---- documento
    def converti(self):
        body = self.d.element.body
        out, toc = [], []
        lista = []          # pila di (tag, ilvl)
        pre = []

        def chiudi_liste(fino=-1):
            while lista and lista[-1][1] > fino:
                out.append(f"</li></{lista.pop()[0]}>")

        def chiudi_pre():
            if pre:
                out.append("<pre><code>" + "\n".join(pre) + "</code></pre>")
                pre.clear()

        n_h = 0
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
                out.append(f'<h{lv} id="{hid}">{re.sub("</?(strong|em|mark|code)>", "", s)}</h{lv}>')
                if lv == 2:
                    toc.append((hid, html.unescape(re.sub("<[^>]+>", "", s))))
                continue
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
        return "".join(out), toc

    def tabella(self, t):
        righe = []
        for row in t.rows:
            celle = []
            for c in row.cells:
                celle.append("<td>" + "<br>".join(self.par_html(p)[0] for p in c.paragraphs if p.text.strip()) + "</td>")
            righe.append("<tr>" + "".join(celle) + "</tr>")
        return "<table>" + "".join(righe) + "</table>"


def main(argv):
    if len(argv) != 2:
        print(__doc__); return 1
    base = Path(argv[1]) / "riassunti"
    base.mkdir(parents=True, exist_ok=True)
    schede = []
    for slug, nome, f in MATERIE:
        src = UNI / f
        if not src.exists():
            print("manca", src); continue
        d = docx.Document(str(src))
        c = Conv(d, base)
        corpo, toc = c.converti()
        voci = "".join(f'<a href="#{i}">{html.escape(t)}</a>' for i, t in toc)
        top = (f'<div class="top"><a href="../">&larr; Quaderno</a><a href="./">Riassunti</a><b>{html.escape(nome)}</b>'
               f'<input id="q" type="search" placeholder="Cerca nel testo (min. 3 lettere)"><label><input id="hl" type="checkbox" checked> evidenziazioni</label></div>')
        pag = (top + f'<div class="wrap"><nav class="toc">{voci}</nav><main>{corpo}</main></div><script>{JS}</script>')
        (base / f"{slug}.html").write_text(pagina(f"{nome} - Riassunto", pag), encoding="utf-8")
        schede.append((slug, nome, len(toc), c.nimg))
        print(f"{nome}: {len(toc)} capitoli, {c.nimg} figure, {len(corpo) // 1024} KB")
    cards = "".join(f'<a class="card" href="{s}.html"><b>{html.escape(n)}</b><br><small>{k} capitoli &middot; {m} figure</small></a>' for s, n, k, m in schede)
    idx = f'<div class="top"><a href="../">&larr; Quaderno</a><b>Riassunti</b></div><div class="idx"><h1>Riassunti</h1>{cards}</div>'
    (base / "index.html").write_text(pagina("Riassunti", idx), encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
