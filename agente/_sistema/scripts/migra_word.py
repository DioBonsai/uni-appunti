"""Migrazione una tantum: dai 5 Word dei riassunti ai contenuti strutturati del sito (fonte unica d'ora in poi).

Per ogni materia scrive <repo sito>/contenuti/<slug>.json: capitoli, blocchi di testo (con un id stabile, es. "cap26.12"),
figure e tabelle, SENZA evidenziazioni. Le evidenziazioni gialle dei Word diventano intervalli di caratteri per blocco
e finiscono in <repo sito>/contenuti/_seed_evidenziazioni.json (poi caricate sul database dal sito).
Non modifica mai i Word.

Uso: python migra_word.py [--repo CARTELLA_SITO]
"""
import argparse
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
REPO_DEFAULT = Path.home() / "Documents" / "GitHub" / "quaderno-privato"
W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
A = "{http://schemas.openxmlformats.org/drawingml/2006/main}"
WP = "{http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing}"
R = "{http://schemas.openxmlformats.org/officeDocument/2006/relationships}"
EXT = {"image/png": "png", "image/jpeg": "jpg", "image/gif": "gif", "image/svg+xml": "svg", "image/webp": "webp"}
MATERIE = [
    ("algebra", "Algebra lineare", "Riassunto Algebra lineare.docx", "Algebra lineare"),
    ("matematica-discreta", "Matematica discreta", "Riassunto Matematica discreta.docx", "Matematica discreta"),
    ("fondamenti", "Fondamenti dell'Informatica", "Riassunto Fondamenti Informatica.docx", "Fondamenti Info"),
    ("programmazione", "Programmazione", "Riassunto Programmazione.docx", "Programmazione"),
    ("laboratorio", "Programmazione, Laboratorio", "Riassunto Laboratorio.docx", "Programmazione, Laboratorio"),
]


def u16(t):
    """Lunghezza in unità UTF-16 (come le stringhe JavaScript del browser)."""
    return len(t.encode("utf-16-le")) // 2


def numero(titolo):
    m = re.match(r"^\s*(?:Capitolo\s+)?(\d+)\b", titolo)
    return int(m.group(1)) if m else None


def numbering_kinds(d):
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


class Migra:
    def __init__(self, d, imgdir):
        self.d, self.imgdir = d, imgdir
        self.kinds = numbering_kinds(d)

    # ---------------------------------------------------------------- figure
    def figura(self, drawing):
        blip = drawing.find(".//" + A + "blip")
        if blip is None:
            return None
        try:
            part = self.d.part.related_parts[blip.get(R + "embed")]
        except KeyError:
            return None
        blob = part.blob
        name = hashlib.sha1(blob).hexdigest()[:14] + "." + EXT.get(part.content_type, "png")
        f = self.imgdir / name
        if not f.exists():
            f.write_bytes(blob)
        ext = drawing.find(".//" + WP + "extent")
        cx = int(ext.get("cx")) if ext is not None and ext.get("cx") else 0
        cy = int(ext.get("cy")) if ext is not None and ext.get("cy") else 0
        return {"t": "fig", "src": name, "w": cx // 9525 if cx else 0, "cx": cx, "cy": cy}

    # ---------------------------------------------------------------- run -> parti
    def parti(self, p):
        parts, figs = [], []
        for r in p.runs:
            f = r.font
            fl = dict(b=bool(f.bold), i=bool(f.italic), sup=bool(f.superscript), sub=bool(f.subscript and not f.superscript),
                      code=bool(f.name and "consolas" in f.name.lower()), mk=f.highlight_color is not None)
            buf = ""
            for ch in r._r:
                if ch.tag == W + "t":
                    buf += ch.text or ""
                elif ch.tag == W + "tab":
                    buf += " "
                elif ch.tag in (W + "br", W + "cr"):
                    if buf:
                        parts.append({**fl, "t": buf}); buf = ""
                    parts.append({**fl, "t": "", "br": True})
                elif ch.tag == W + "drawing":
                    if buf:
                        parts.append({**fl, "t": buf}); buf = ""
                    g = self.figura(ch)
                    if g:
                        figs.append(g)
            if buf:
                parts.append({**fl, "t": buf})
        return parts, figs


def html_parti(parts, codice=True):
    out = []
    for pt in parts:
        if pt.get("br"):
            out.append("<br>"); continue
        t = html.escape(pt["t"])
        if not t.strip():
            out.append(t); continue
        if pt["code"] and codice:
            t = f"<code>{t}</code>"
        if pt["sup"]:
            t = f"<sup>{t}</sup>"
        elif pt["sub"]:
            t = f"<sub>{t}</sub>"
        if pt["b"]:
            t = f"<strong>{t}</strong>"
        if pt["i"]:
            t = f"<em>{t}</em>"
        out.append(t)
    return "".join(out)


def intervalli(parts, base=0):
    """Intervalli [inizio, fine) evidenziati, in unità UTF-16 sul testo del blocco (base = scostamento iniziale)."""
    res, pos = [], base
    for pt in parts:
        n = u16(pt["t"])
        if pt.get("mk") and n and not pt.get("br"):
            if res and res[-1][1] == pos:
                res[-1][1] = pos + n
            else:
                res.append([pos, pos + n])
        pos += n
    return res, pos


def testo(parts):
    return "".join(pt["t"] for pt in parts)


def togli_prefisso(parts, n):
    """Toglie n caratteri dall'inizio del testo, attraverso le parti."""
    while n > 0 and parts:
        pt = parts[0]
        if len(pt["t"]) <= n:
            n -= len(pt["t"]); parts.pop(0)
        else:
            pt["t"] = pt["t"][n:]; n = 0
    while parts and not parts[0].get("br") and parts[0]["t"] == "":
        parts.pop(0)


def riquadro_pp(parts):
    """'(In parole povere: ...)' -> riquadro: toglie l'intestazione e le parentesi (l'etichetta la mette lo stile).
    Restituisce True se il paragrafo era un 'In parole povere'."""
    full = testo(parts)
    m = re.match(r"^\s*(\()?\s*In parole povere\s*:?\s*", full, flags=re.I)
    if not m:
        return False
    togli_prefisso(parts, m.end())
    if m.group(1):
        for pt in reversed(parts):
            if pt.get("br"):
                continue
            s = pt["t"].rstrip()
            if s.endswith(")"):
                pt["t"] = s[:-1]
            break
    # un eventuale pezzo vuoto in coda/inizio si ripulisce; la prima lettera diventa maiuscola
    parts[:] = [pt for pt in parts if pt.get("br") or pt["t"] != ""]
    for pt in parts:
        if pt.get("br"):
            continue
        s = pt["t"].lstrip()
        if s:
            pt["t"] = s[0].upper() + s[1:]
            break
    return True


class Costruttore:
    """Scorre un Word e produce capitoli e blocchi con id stabili e intervalli di evidenziazione."""

    def __init__(self, d, repo):
        self.d = d
        self.m = Migra(d, repo / "contenuti" / "img")
        self.capitoli, self.pre = [], []
        self.cap = None
        self.cur = self.pre
        self.n = 0
        self.usati = set()
        self.evid, self.verifica = {}, {}
        self.cod = None                    # blocco di codice in costruzione

    def nuovo_id(self):
        self.n += 1
        return f"{self.cap['id'] if self.cap else 'pre'}.{self.n}"

    def registra(self, bid, rng, tx):
        """Memorizza gli intervalli evidenziati (scartando quelli fatti solo di spazi)."""
        enc = tx.encode("utf-16-le")
        buone = []
        for a, b in rng:
            if enc[a * 2:b * 2].decode("utf-16-le", errors="ignore").strip():
                buone.append([a, b])
        if buone:
            self.evid[bid] = buone
            self.verifica[bid] = [enc[a * 2:b * 2].decode("utf-16-le", errors="ignore") for a, b in buone]

    def chiudi_codice(self):
        if not self.cod:
            return
        bid = self.nuovo_id()
        self.cur.append({"t": "pre", "b": bid, "h": chr(10).join(self.cod["h"])})
        self.registra(bid, self.cod["rng"], chr(10).join(self.cod["tx"]))
        self.cod = None

    def aggiungi_codice(self, parts, tx):
        if self.cod is None:
            self.cod = {"h": [], "tx": [], "rng": [], "pos": 0}
        c = self.cod
        if c["h"]:
            c["pos"] += 1                                   # l'a capo fra due righe
        rng, _ = intervalli(parts, base=c["pos"])
        for a, b in rng:
            if c["rng"] and c["rng"][-1][1] == a:
                c["rng"][-1][1] = b
            else:
                c["rng"].append([a, b])
        c["h"].append(html_parti(parts, codice=False))
        c["tx"].append(tx)
        c["pos"] += u16(tx)

    def tabella(self, el):
        t = docx.table.Table(el, self.d)
        righe = []
        for row in t.rows:
            celle = []
            for c in row.cells:
                celle.append("<td>" + "<br>".join(html_parti(self.m.parti(p)[0]) for p in c.paragraphs if p.text.strip()) + "</td>")
            righe.append("<tr>" + "".join(celle) + "</tr>")
        self.cur.append({"t": "tab", "h": "<table>" + "".join(righe) + "</table>"})

    def paragrafo(self, p):
        stile = p.style.name if p.style is not None else ""
        parts, figs = self.m.parti(p)
        tx = testo(parts)
        if not tx.strip() and not figs:
            return
        if stile.startswith("Heading"):
            self.chiudi_codice()
            titolo = re.sub(r"\s+", " ", tx).strip()
            if stile.endswith("1"):
                n = numero(titolo)
                cid = f"cap{n}" if n is not None and n not in self.usati else f"c{len(self.capitoli) + 1}"
                if n is not None:
                    self.usati.add(n)
                self.cap = {"id": cid, "num": n, "titolo": titolo, "blocks": []}
                self.capitoli.append(self.cap)
                self.cur = self.cap["blocks"]
                self.n = 0
            else:
                bid = self.nuovo_id()
                neutri = [{**pt, "mk": False, "b": False, "i": False, "code": False} for pt in parts]
                self.cur.append({"t": "h3", "b": bid, "h": html_parti(neutri)})
            return
        solo_codice = (not figs) and any(pt["t"].strip() for pt in parts) and all(pt["code"] for pt in parts if pt["t"].strip())
        if solo_codice:
            self.aggiungi_codice(parts, tx)
            return
        self.chiudi_codice()
        numpr = p._p.pPr.numPr if p._p.pPr is not None else None
        if numpr is not None and numpr.numId is not None and tx.strip():
            il = int(numpr.ilvl.val) if numpr.ilvl is not None else 0
            kind = self.m.kinds.get((str(numpr.numId.val), str(il)), "ul")
            bid = self.nuovo_id()
            rng, _ = intervalli(parts)
            self.cur.append({"t": "li", "b": bid, "h": html_parti(parts), "k": kind, "l": il})
            self.registra(bid, rng, tx)
            for g in figs:
                self.cur.append({**g, "inli": True})
            return
        if tx.strip():
            pp = riquadro_pp(parts)
            tx2 = testo(parts)
            bid = self.nuovo_id()
            rng, _ = intervalli(parts)
            blk = {"t": "p", "b": bid, "h": html_parti(parts)}
            if pp:
                blk["c"] = "pp"
            self.cur.append(blk)
            self.registra(bid, rng, tx2)
        for g in figs:
            self.cur.append(g)

    def esegui(self):
        for el in self.d.element.body.iterchildren():
            if el.tag == W + "tbl":
                self.chiudi_codice()
                self.tabella(el)
            elif el.tag == W + "p":
                self.paragrafo(docx.text.paragraph.Paragraph(el, self.d))
        self.chiudi_codice()


def migra(path, slug, nome, chiave, repo):
    d = docx.Document(str(path))
    c = Costruttore(d, repo)
    c.esegui()
    out = {"slug": slug, "nome": nome, "chiave": chiave, "preambolo": c.pre, "capitoli": c.capitoli}
    (repo / "contenuti" / f"{slug}.json").write_text(json.dumps(out, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    stat = []
    for cap in c.capitoli:
        stat.append((cap["num"], sum(1 for b in cap["blocks"] if b.get("b") in c.evid and b["t"] != "h3")))
    return c.evid, c.verifica, stat


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", default=str(REPO_DEFAULT))
    a = ap.parse_args()
    repo = Path(a.repo)
    (repo / "contenuti" / "img").mkdir(parents=True, exist_ok=True)
    try:
        man = json.loads((BASE / "studiato_manuale.json").read_text(encoding="utf-8"))
    except Exception:
        man = {}
    seed = {"evid": {}, "man": {}}
    ver = {}
    for slug, nome, f, chiave in MATERIE:
        src = UNI / f
        if not src.exists():
            print("manca", src); continue
        evid, verifica, stat = migra(src, slug, nome, chiave, repo)
        seed["evid"][slug] = evid
        seed["man"][slug] = man.get(chiave) or []
        ver[slug] = verifica
        studiati = sum(1 for _n, h in stat if h >= 3)
        print(f"{nome}: {len(stat)} capitoli, {sum(h for _n, h in stat)} paragrafi evidenziati, {studiati} capitoli con almeno 3")
    (repo / "contenuti" / "_seed_evidenziazioni.json").write_text(json.dumps(seed, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    (repo / "contenuti" / "_verifica_testi.json").write_text(json.dumps(ver, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
