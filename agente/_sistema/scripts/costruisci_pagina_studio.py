"""Costruisce la pagina di studio interattiva ("Quaderno di ripasso") con i dati veri.

Legge:  esami/quiz_*.md, esami/prob_*.md, flashcard/<materia>*.md, i Word (evidenziazioni gialle = studiato),
        piano_oggi.md, pagina_studio/{template.html (solo <head> e CSS), extra.css, body.html, app.js, gen.js}
Scrive: pagina_studio/index.html (la pagina) e pagina_studio/data.json (i dati, caricati con fetch).
Il sito si apre con apri_quaderno.bat o serve.py (che ricostruisce e serve su http://127.0.0.1:8765).

Il collaudo del generatore di esercizi è pagina_studio/test_gen.js (node test_gen.js).
Uso: python costruisci_pagina_studio.py
"""
import hashlib
import json
import re
import sys
from datetime import date
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent          # _sistema
UNI = BASE.parent.parent                                # cartella UNI
PAG = BASE / "pagina_studio"
sys.path.insert(0, str(Path(__file__).resolve().parent))
from anki_build import parse_cards  # noqa: E402

# Percorsi dei Word: accetta sia i file sciolti in UNI\ sia le vecchie sottocartelle.
WORD = {
    "Algebra lineare": ["Riassunto Algebra lineare.docx", "Algebra lineare/Riassunto Algebra lineare.docx"],
    "Matematica discreta": ["Riassunto Matematica discreta.docx", "Matematica discreta/Appunti matematica discreta.docx"],
    "Fondamenti Info": ["Riassunto Fondamenti Informatica.docx", "Fondamenti Info/Fondamenti Informatica.docx"],
    "Programmazione": ["Riassunto Programmazione.docx", "Programmazione/Riassunto Programmazione.docx"],
}
# Testi a mano (non deducibili dai file): lezioni coperte e note. I capitoli studiati si calcolano dalle evidenziazioni.
LEZIONI = {
    "Algebra lineare": "3 di 26 (L4 Polinomi pronta, in attesa dell'ok)",
    "Matematica discreta": "5 fatte",
    "Fondamenti Info": "cap. 1 del libro",
    "Programmazione": "slide 00-02C, laboratorio Lab01",
}
# Date d'esame (AAAA-MM-GG), da compilare quando Moodle le pubblica; si possono anche inserire nella pagina.
ESAMI = {}

# Pesi d'esame di Matematica discreta: (tema, quiz su 150, problemi su 30, parole chiave per «nel Word»)
FREQ = [
    ("Permutazioni: cicli, tipo, periodo", 48, 14, r"permutazion|cicli disgiunti"), ("Aritmetica modulare e congruenze", 21, 10, r"congruenz|aritmetica modulare"),
    ("Z_N moltiplicativo (inversi, φ di Eulero)", 16, 9, r"φ di Eulero|funzione di Eulero|invertibil[ei] in ℤ"), ("Omomorfismi tra gruppi", 1, 9, r"omomorfism"),
    ("Coefficienti binomiali e combinatoria", 15, 15, r"coefficient[ei] binomial|combinatori"), ("Gruppi, sottogruppi, generatori", 29, 11, r"sottogrupp|gruppo ciclico|generator"),
    ("Parità delle permutazioni", 6, 6, r"parità"), ("MCD e algoritmo di Euclide", 1, 7, r"algoritmo di euclide|massimo comun divisore|MCD"),
    ("Funzioni, composizione, iniettività", 33, 4, r"iniettiv"), ("Appartenenza, inclusione, insiemi", 37, 0, r"appartenenza|inclusione"),
    ("Prodotto cartesiano, operazioni sugli insiemi", 21, 4, r"prodotto cartesiano"), ("Relazioni, equivalenze, induzione", 0, 0, r"equivalenz|induzione"),
]

# Tag delle domande -> tema. L'ordine di PRIORITA decide il tema quando una domanda ha più tag.
TAG_TEMA = {
    "permutazioni": "Permutazioni", "cicli-tipo-periodo": "Permutazioni", "parita": "Permutazioni",
    "aritmetica-modulare": "Aritmetica modulare e ℤ_N", "Z_N-moltiplicativo": "Aritmetica modulare e ℤ_N", "Z_N-additivo": "Aritmetica modulare e ℤ_N",
    "generatori": "Aritmetica modulare e ℤ_N", "MCD-euclide": "Aritmetica modulare e ℤ_N",
    "gruppi": "Gruppi e omomorfismi", "sottogruppi": "Gruppi e omomorfismi", "omomorfismi": "Gruppi e omomorfismi", "nucleo-immagine": "Gruppi e omomorfismi",
    "combinatoria": "Combinatoria", "disposizioni": "Combinatoria", "combinazioni": "Combinatoria", "coefficienti-binomiali": "Combinatoria",
    "funzioni": "Funzioni", "iniettiva-suriettiva-inversa": "Funzioni", "composizione": "Funzioni",
    "partizioni": "Partizioni e relazioni", "insiemi": "Insiemi", "appartenenza-inclusione": "Insiemi", "operazioni-insiemi": "Insiemi", "prodotto-cartesiano": "Insiemi",
    "base-2": "Binario", "altro": "Altro",
}
PRIORITA = ["Permutazioni", "Gruppi e omomorfismi", "Aritmetica modulare e ℤ_N", "Combinatoria", "Funzioni", "Partizioni e relazioni", "Binario", "Insiemi", "Altro"]
# Capitoli del Word di Mate discreta per tema (None = non ancora nel Word)
TEMI = {t: {"capitoli": None} for t in PRIORITA}
TEMI["Insiemi"]["capitoli"] = "cap. 1-3"
TEMI["Partizioni e relazioni"]["capitoli"] = "cap. 6-9"
TEMI["Funzioni"]["capitoli"] = "cap. 10-19"
# Peso d'esame del tema (0..1), dalla tabella FREQ
PESO_TEMA = {"Permutazioni": 0.0, "Aritmetica modulare e ℤ_N": 0.0, "Gruppi e omomorfismi": 0.0, "Combinatoria": 0.0, "Funzioni": 0.0, "Insiemi": 0.0, "Partizioni e relazioni": 0.0, "Binario": 0.0, "Altro": 0.0}
PESO_FREQ = {"Permutazioni": [0, 6], "Aritmetica modulare e ℤ_N": [1, 2, 7], "Gruppi e omomorfismi": [3, 5], "Combinatoria": [4], "Funzioni": [8], "Insiemi": [9, 10], "Partizioni e relazioni": [11]}


# Copertura: un tema di quiz compare solo se il Word di quella materia lo tratta (almeno 3 occorrenze delle parole chiave).
# Così i quiz seguono le lezioni fatte: quando si aggiungono capitoli sul tema, le domande compaiono da sole.
COPERTURA_RX = {
    ("Matematica discreta", "Insiemi"): r"appartenenza|inclusione|prodotto cartesiano",
    ("Matematica discreta", "Partizioni e relazioni"): r"partizion|equivalenz",
    ("Matematica discreta", "Funzioni"): r"iniettiv",
    ("Matematica discreta", "Numeri naturali e induzione"): r"induzione",
    ("Matematica discreta", "Permutazioni"): r"permutazion|cicli disgiunti",
    ("Matematica discreta", "Aritmetica modulare e ℤ_N"): r"congruenz|aritmetica modulare|classi di resto",
    ("Matematica discreta", "Gruppi e omomorfismi"): r"omomorfism|sottogruppo|gruppo ciclico|struttura di gruppo",
    ("Matematica discreta", "Combinatoria"): r"coefficient[ei] binomial|combinazion|disposizion",
    ("Matematica discreta", "Binario"): r"notazione binaria|scrittura in base|base 2",
    ("Algebra lineare", "Campi"): r"\bcamp[oi]\b", ("Algebra lineare", "Numeri complessi"): r"numeri complessi", ("Algebra lineare", "Coniugato e modulo"): r"coniugat",
    ("Algebra lineare", "Forma polare"): r"polare", ("Algebra lineare", "Potenze e radici"): r"radic[ei] n-esim|moivre|potenz", ("Algebra lineare", "Vettori"): r"vettor",
    ("Fondamenti Info", "Rappresentazione binaria"): r"binari|complemento a due|esadecimal", ("Fondamenti Info", "Circuiti e memoria"): r"flip-flop|\bram\b|memoria",
    ("Fondamenti Info", "Compressione ed errori"): r"compressione|hamming", ("Fondamenti Info", "Logica proposizionale"): r"tavol[ae] di verit|tautologi|contraddizion",
    ("Fondamenti Info", "Automi e grammatiche"): r"\bautom[ai]\b|grammatic", ("Fondamenti Info", "Insiemi e relazioni"): r"relazion[ei] di equivalenza|prodotto cartesiano",
    ("Programmazione", "Algoritmi"): r"algoritm", ("Programmazione", "Assembly e macchina"): r"assembly", ("Programmazione", "Tipi e memoria"): r"memoria",
    ("Programmazione", "Variabili e assegnamento"): r"assegnament", ("Programmazione", "Operatori"): r"operator", ("Programmazione", "Puntatori"): r"puntator",
    ("Programmazione", "Input e output"): r"scanf|printf", ("Programmazione", "Compilazione e terminale"): r"gcc|compilazion", ("Programmazione", "Controllo di flusso"): r"\bfor\b|\bwhile\b|\bif\b",
}


def copertura(texts):
    """{(materia, tema): occorrenze nel Word}; i temi senza espressione (es. «Altro») non sono mai coperti."""
    return {k: len(re.findall(rx, texts.get(k[0], ""), re.I)) for k, rx in COPERTURA_RX.items()}


def parse_quizzes():
    out = []
    for f in sorted((BASE / "esami").glob("quiz_*.md")):
        prova = ""
        for blk in re.split(r"(?m)^(?=#{1,2} )", f.read_text(encoding="utf-8")):
            if blk.startswith("# "):
                prova = blk.splitlines()[0][2:].strip()
                continue
            if not blk.startswith("## ["):
                continue
            head, _, body = blk.partition("\n")
            m = re.match(r"## \[([^\]]+)\]\s*argomenti:\s*(.*)", head)
            r = re.search(r"(?m)^RISPOSTA:\s*(\d)", body)
            if not m or not r:
                continue
            pre, _, post = body.partition("RISPOSTA:")
            lines = pre.strip().splitlines()
            first_opt = next((i for i, l in enumerate(lines) if re.match(r"^1\.\s", l)), None)
            if first_opt is None:
                continue
            opts = [re.sub(r"^\d\.\s*", "", l).strip() for l in lines[first_opt:] if re.match(r"^[1-5]\.\s", l)]
            if len(opts) != 5:
                continue
            sp = re.search(r"(?ms)SPIEGAZIONE:\s*(.*?)(?=^ATTENZIONE:|\Z)", post)
            at = re.search(r"(?ms)ATTENZIONE:\s*(.*)", post)
            out.append(dict(id=m.group(1), prova=prova, args=[a.strip() for a in m.group(2).split(",") if a.strip()],
                            q="\n".join(lines[:first_opt]).strip(), o=opts, a=int(r.group(1)),
                            s=(sp.group(1).strip() if sp else ""), w=(at.group(1).strip() if at else "")))
    return out


def parse_problems():
    out = []
    for f in sorted((BASE / "esami").glob("prob_*.md")):
        for blk in re.split(r"(?m)^(?=## \[)", f.read_text(encoding="utf-8")):
            m = re.match(r"## \[([^\]]+)\]\s*argomenti:\s*(.*)", blk)
            if not m:
                continue
            t = re.search(r"(?ms)\*\*Testo:\*\*\s*(.*?)(?=^\*\*Soluzione:\*\*)", blk)
            s = re.search(r"(?ms)\*\*Soluzione:\*\*\s*(.*?)(?=^\*\*Concetti usati:\*\*|\Z)", blk)
            c = re.search(r"(?ms)\*\*Concetti usati:\*\*\s*(.*?)(?=^## |\Z)", blk)
            if not (t and s):
                continue
            out.append(dict(id=m.group(1), args=[a.strip() for a in m.group(2).split(",") if a.strip()],
                            testo=t.group(1).strip(), soluzione=s.group(1).strip(), concetti=(c.group(1).strip() if c else "")))
    return out


def card_id(mat, title, d):
    return mat[:3] + hashlib.sha1((title + "|" + d).encode("utf-8")).hexdigest()[:10]


def parse_all_cards():
    out, seen = [], set()
    for mat in WORD:
        files = sorted((BASE / "flashcard").glob(f"{mat}.md")) + sorted((BASE / "flashcard").glob(f"{mat}.*.md"))
        for p in files:
            for (t, q, a) in parse_cards(p):
                cid = card_id(mat, t, q)           # id basato sul contenuto: i progressi non si spostano se le schede cambiano
                if cid in seen:
                    continue
                seen.add(cid)
                out.append(dict(id=cid, m=mat, t=t, d=q, r=a, lungo=len(a) > 400, da_quiz=p.name.endswith(".quiz.md")))
    return out


def find_word(mat):
    for rel in WORD[mat]:
        p = UNI / rel
        if p.exists():
            return p
    return None


def chapters(path):
    """[(numero, titolo, stato)] stato 2 = studiato (almeno 3 paragrafi evidenziati), 1 = tracce isolate, 0 = no. Più il testo intero."""
    from docx import Document
    doc = Document(str(path))
    chs, cur, text = [], None, []
    for p in doc.paragraphs:
        txt = p.text.strip()
        text.append(txt)
        if txt and p.style.name.lower().startswith(("heading 1", "titolo 1")):   # ignora titoli vuoti
            m = re.match(r"(?:Capitolo\s+)?(\d+)[.:]?\s*(.*)", txt)
            cur = [int(m.group(1)) if m else len(chs) + 1, (m.group(2) if m else txt), 0, 0]
            chs.append(cur)
        if cur is not None and txt:
            cur[3] += 1
            if any(r.font.highlight_color is not None for r in p.runs):
                cur[2] += 1
    res = []
    for n, t, hl, tot in chs:
        res.append((n, t, 2 if hl >= 3 else (1 if hl else 0), hl, tot))   # le evidenziazioni sono a pezzi: da 3 paragrafi in su = studiato
    return res, "\n".join(text)


def _manuale():
    """studiato_manuale.json: {"Materia": [numeri di capitolo]} segnati come studiati a mano (le evidenziazioni nei Word non si toccano)."""
    f = BASE / "studiato_manuale.json"
    try:
        return json.loads(f.read_text(encoding="utf-8")) if f.exists() else {}
    except Exception:
        return {}


def avanzamento():
    out, texts = {}, {}
    for mat in WORD:
        p = find_word(mat)
        if p is None:
            out[mat] = dict(capitoli=0, studiati=0, lezioni=LEZIONI[mat], prossimo="Word non trovato.", elenco=[])
            continue
        res, text = chapters(p)
        texts[mat] = text
        manuali = set((_manuale().get(mat) or []))   # capitoli che Emanuele ha chiesto di segnare come studiati senza evidenziarli
        res = [(n, t, 2 if n in manuali else s, hl, tot) for n, t, s, hl, tot in res]
        done = [n for n, _, s, *_ in res if s == 2]
        part = [n for n, _, s, *_ in res if s == 1]
        todo = [n for n, _, s, *_ in res if s == 0]
        def rng(l):
            if not l:
                return "nessuno"
            parts, a = [], l[0]
            for i, x in enumerate(l):
                if i + 1 == len(l) or l[i + 1] != x + 1:
                    parts.append(str(a) if a == x else f"{a}-{x}")
                    a = l[i + 1] if i + 1 < len(l) else None
            return ", ".join(parts)
        nota = f"Studiati: {rng(done)}." + (f" In parte: {rng(part)}." if part else "") + (f" Da studiare: {rng(todo)}." if todo else " Tutto studiato.")
        out[mat] = dict(capitoli=len(res), studiati=len(done), lezioni=LEZIONI[mat], prossimo=nota,
                        elenco=[dict(n=n, t=t, s=s, hl=hl, tot=tot) for n, t, s, hl, tot in res])
    lab = UNI / "Riassunto Laboratorio.docx"   # il laboratorio fa parte di ciò che è stato trattato per Programmazione
    if lab.exists() and "Programmazione" in texts:
        texts["Programmazione"] += "\n" + chapters(lab)[1]
    return out, texts


def piano():
    p = BASE / "piano_oggi.md"
    if not p.exists():
        return ""
    t = p.read_text(encoding="utf-8")
    m = re.search(r"(?ms)^## Oggi.*?\n(.*?)(?=^## Da tenere|\Z)", t)
    return m.group(1).strip() if m else ""


def diff_evidenziazioni(avanz):
    """Confronta le evidenziazioni gialle di oggi con l'ultimo controllo (evidenziazioni.json) e scrive evidenziazioni_oggi.md."""
    import json as _j
    snap = BASE / "evidenziazioni.json"
    prev = _j.loads(snap.read_text(encoding="utf-8")) if snap.exists() else {}
    cur = {m: {str(c["n"]): [c["hl"], c["tot"], c["t"]] for c in x["elenco"]} for m, x in avanz.items()}
    righe = []
    for m, caps in cur.items():
        for n, (hl, tot, t) in caps.items():
            old = (prev.get("materie", {}).get(m, {}).get(n) or [0])[0]
            if hl != old:
                stato = "studiato" if hl >= 3 else "iniziato"
                righe.append(f"- {m}, cap. {n} «{t}»: {'+' if hl > old else ''}{hl - old} paragrafi evidenziati (ora {hl} su {tot}, {stato})")
    out = [f"# Evidenziazioni: cambiamenti dall'ultimo controllo ({prev.get('data', 'primo controllo')})", ""]
    out += righe or ["Nessun cambiamento."]
    (BASE / "evidenziazioni_oggi.md").write_text("\n".join(out) + "\n", encoding="utf-8")
    snap.write_text(_j.dumps(dict(data=str(date.today()), materie=cur), ensure_ascii=False), encoding="utf-8")
    print("\n".join(out))


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    mate = parse_quizzes()
    for q in mate:  # tema = primo tema per priorità tra i tag della domanda
        q["m"] = "Matematica discreta"
        q["theme"] = next((t for t in PRIORITA if any(TAG_TEMA.get(x) == t for x in q["args"])), TAG_TEMA.get(q["args"][0], "Altro") if q["args"] else "Altro")
    from quiz_banche import tutte
    quiz, probs, cards = tutte(mate), parse_problems(), parse_all_cards()
    avanz, texts = avanzamento()
    cop = copertura(texts)
    visibili, nascoste = [], {}
    for q in quiz:
        if cop.get((q["m"], q["theme"]), 0) >= 3:
            visibili.append(q)
        else:
            nascoste.setdefault(q["m"], {}).setdefault(q["theme"], 0)
            nascoste[q["m"]][q["theme"]] += 1
    quiz = visibili
    from quiz_banche import tema_fondamenti, solo_it, titolo_it, inglese
    for c in cards:   # i quiz del sito sono bilingui: tengo l'italiano, titoli puliti
        if c["m"] == "Fondamenti Info":
            c["d"], c["r"], c["t"] = solo_it(c["d"]), solo_it(c["r"]), titolo_it(solo_it(c["t"]))
    from quiz_banche import chiave_testo, immagini_per_testo
    imm = immagini_per_testo()   # disegni scaricati dal sito esami, collegati alle schede dallo stesso testo
    for c in cards:
        if c["m"] == "Fondamenti Info" and c["da_quiz"] and chiave_testo(c["d"]) in imm:
            c["img"], c["imgf"] = imm[chiave_testo(c["d"])]
    cards = [c for c in cards if not inglese(c["d"] + " " + c["r"])]   # solo italiano: via le schede scritte solo in inglese
    n_cards = len(cards)   # schede ricavate dai quiz del sito di Fondamenti: tolte quelle su argomenti non ancora trattati
    cards = [c for c in cards if not (c["m"] == "Fondamenti Info" and c["da_quiz"]) or cop.get((c["m"], tema_fondamenti(c["d"] + " " + c["r"], c["t"])), 0) >= 3]
    print(f"  schede: {len(cards)} (nascoste {n_cards - len(cards)} su argomenti non ancora trattati)")
    coperti = {m: sorted(t for (mm, t), n in cop.items() if mm == m and n >= 3) for m in WORD}
    if "--diff" in sys.argv:
        diff_evidenziazioni(avanz)
    mate_txt = texts.get("Matematica discreta", "")
    freq = [[t, q, p, len(re.findall(rx, mate_txt, re.I)) >= 2] for (t, q, p, rx) in FREQ]
    pesi = {}
    for tema, idx in PESO_FREQ.items():
        pesi[tema] = sum(FREQ[i][1] / 150 + FREQ[i][2] / 30 for i in idx)
    mx = max(pesi.values()) or 1
    pesi = {k: round(v / mx, 3) for k, v in pesi.items()}
    data = dict(oggi=str(date.today()), quiz=quiz, problemi=probs, cards=cards, materie=avanz, freq=freq,
                tagTema=TAG_TEMA, priorita=PRIORITA, temi=TEMI, pesi=pesi, piano=piano(), esami=ESAMI, nascoste=nascoste, coperti=coperti)
    (PAG / "data.json").write_text(json.dumps(data, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")

    head = (PAG / "template.html").read_text(encoding="utf-8").split('<div class="app">')[0]
    head = head.replace("</style>", (PAG / "extra.css").read_text(encoding="utf-8") + "\n</style>", 1)
    html = '<meta charset="utf-8">\n' + head + (PAG / "body.html").read_text(encoding="utf-8") + "\n<script>\n" + (PAG / "gen.js").read_text(encoding="utf-8").replace("if (typeof module", "if (false && typeof module") + "\n" + (PAG / "app.js").read_text(encoding="utf-8") + "\n</script>\n"
    (PAG / "index.html").write_text(html, encoding="utf-8")
    print(f"{len(quiz)} domande, {len(probs)} problemi, {len(cards)} schede; index.html {len(html) // 1024} KB, data.json {(PAG / 'data.json').stat().st_size // 1024} KB")
    for m, x in avanz.items():
        print(f"  {m}: {x['studiati']}/{x['capitoli']} studiati. {x['prossimo']}")
    print("  nel Word:", [f[0][:18] for f in freq if f[3]])
    print("  quiz visibili:", {m: sum(1 for q in quiz if q["m"] == m) for m in WORD}, "| nascosti (argomenti non ancora trattati):", nascoste)


if __name__ == "__main__":
    main()
