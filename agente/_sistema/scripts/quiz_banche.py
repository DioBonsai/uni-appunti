"""Banche di quiz per materia, lette da esami/*.md e uniformate per la pagina di ripasso.

Ogni domanda: id, m (materia), theme, prova, args, q, o (2-8 opzioni), a (1..n), s (spiegazione), w (avvertenza).
- Matematica discreta: esami/quiz_*.md (150 domande delle prove 2024-2026, 5 opzioni).
- Algebra lineare, Programmazione: esami/banca_algebra.md, esami/banca_programmazione.md (stesso formato).
- Fondamenti Info: esami/fondamenti_quiz.md (quiz del sito esami), solo le domande a scelta singola o vero/falso
  senza figure; le altre tipologie (abbinamenti, risposte multiple) restano nelle schede.
"""
import re
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
ESAMI = BASE / "esami"

TEMI_ALGEBRA = {"campi": "Campi", "numeri-complessi": "Numeri complessi", "coniugato-modulo": "Coniugato e modulo", "forma-polare": "Forma polare",
                "potenze-radici": "Potenze e radici", "vettori": "Vettori"}
TEMI_PROG = {"algoritmi": "Algoritmi", "assembly": "Assembly e macchina", "tipi-e-memoria": "Tipi e memoria", "variabili-assegnamento": "Variabili e assegnamento",
             "operatori": "Operatori", "puntatori": "Puntatori", "scanf-printf": "Input e output", "compilazione-cli": "Compilazione e terminale",
             "controllo-flusso": "Controllo di flusso"}


TEMI_FND = {"binario": "Rappresentazione binaria", "complemento-eccesso": "Rappresentazione binaria", "virgola-mobile": "Rappresentazione binaria",
            "memoria": "Circuiti e memoria", "circuiti-logica": "Circuiti e memoria", "codifica-testo": "Rappresentazione binaria",
            "compressione": "Compressione ed errori", "errori-hamming": "Compressione ed errori"}


def parse_numbered(path, materia, temi, prefix_prova):
    """Formato '## [id] argomenti: tag' + testo + '1. ' ... '5. ' + RISPOSTA + SPIEGAZIONE (+ ATTENZIONE)."""
    out = []
    if not path.exists():
        return out
    prova = prefix_prova
    for blk in re.split(r"(?m)^(?=#{1,2} )", path.read_text(encoding="utf-8")):
        if blk.startswith("# "):
            prova = blk.splitlines()[0][2:].strip() or prefix_prova
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
        first = next((i for i, l in enumerate(lines) if re.match(r"^1\.\s", l)), None)
        if first is None:
            continue
        opts = [re.sub(r"^\d\.\s*", "", l).strip() for l in lines[first:] if re.match(r"^\d\.\s", l)]
        if not 2 <= len(opts) <= 8 or not 1 <= int(r.group(1)) <= len(opts):
            continue
        sp = re.search(r"(?ms)SPIEGAZIONE:\s*(.*?)(?=^ATTENZIONE:|\Z)", post)
        at = re.search(r"(?ms)ATTENZIONE:\s*(.*)", post)
        args = [a.strip() for a in m.group(2).split(",") if a.strip()]
        theme = temi(args) if callable(temi) else (temi.get(args[0], args[0]) if args else "Altro")
        out.append(dict(id=m.group(1), m=materia, theme=theme, prova=prova, args=args, q="\n".join(lines[:first]).strip(), o=opts,
                        a=int(r.group(1)), s=(sp.group(1).strip() if sp else ""), w=(at.group(1).strip() if at else "")))
    return out


FIG = re.compile(r"qui sotto|seguente circuito|nella figura|in figura|figura|immagine|diagramma|automa (qui|seguente)|tabella (qui|seguente)|seguente (tabella|automa)", re.I)
TEMI_FOND = [  # (tema, espressione): il primo che corrisponde vince
    ("Automi e grammatiche", re.compile(r"automa|grammatica|linguaggio|regolare|derivazion|macchina di turing", re.I)),
    ("Logica e dimostrazioni", re.compile(r"logic|implica|quantific|∀|∃|inferenza|tautolog|proposizion|equivalen|valid[ao]|dimostr|induzion|invarian", re.I)),
    ("Rappresentazione binaria", re.compile(r"binar|\bbit\b|complemento|floating|virgola|ottal|esadecim|\bbyte|ascii|unicode|eccesso|mantissa|compress|hamming|parit", re.I)),
    ("Circuiti e memoria", re.compile(r"circuit|porta|nand|\bnor\b|xor|flip|memoria|disco|\bram\b|cache|ssd|\bcd\b|dvd|nastro", re.I)),
    ("Insiemi e relazioni", re.compile(r"insiem|relazion|funzion|sequenz|prodotto cartesiano|partizion", re.I)),
]


def tema_fondamenti(testo, argomenti):
    for tema, rx in TEMI_FOND:
        if rx.search(testo) or rx.search(argomenti):
            return tema
    return "Altro"


def _norm(s):
    return re.sub(r"\s+", " ", s.strip().strip("'\"“”").rstrip(".").strip()).lower()


def parse_fondamenti():
    p = ESAMI / "fondamenti_quiz.md"
    if not p.exists():
        return []
    out = []
    for blk in re.split(r"(?m)^(?=## \[)", p.read_text(encoding="utf-8")):
        m = re.match(r"## \[([^\]]+)\] argomenti: (.*?) \| tipo: (\w+) \| quiz: (.*)", blk.splitlines()[0] if blk.strip() else "")
        if not m or m.group(3) not in ("multichoice", "truefalse"):
            continue
        qid, arg, tipo, quiz = m.groups()
        body = blk.split("\n", 1)[1] if "\n" in blk else ""
        risp = re.search(r"(?m)^RISPOSTA:\s*(.*)$", body)
        spieg = re.search(r"(?ms)^SPIEGAZIONE:\s*(.*?)(?=^## \[|\Z)", body)
        if not risp:
            continue
        pre = body.split("\nRISPOSTA:")[0].splitlines()
        first = next((i for i, l in enumerate(pre) if re.match(r"^- ([a-z]\.\s|Vero$|Falso$)", l)), None)
        if first is None:
            continue
        testo = "\n".join(pre[:first]).strip()
        opts = [re.sub(r"^- ([a-z]\.\s)?", "", l).strip() for l in pre[first:] if l.startswith("- ")]
        if len(opts) < 2 or FIG.search(testo) or any(FIG.search(o) for o in opts) or len(set(opts)) != len(opts):
            continue
        hit = [i for i, o in enumerate(opts) if _norm(o) == _norm(risp.group(1))]
        if len(hit) != 1:
            continue
        s = (spieg.group(1).strip() if spieg else "")
        s = re.sub(r"\\\(|\\\)", "", s)
        if s.startswith("(nessuna"):
            s = ""
        out.append(dict(id=qid, m="Fondamenti Info", theme=tema_fondamenti(testo + " " + " ".join(opts), arg), prova=re.sub(r"\s*\(risposta sì/no\)|\s*Quiz$", "", quiz).strip(), args=[arg.split("(")[0].strip()],
                        q=re.sub(r"\\\(|\\\)", "", testo), o=opts, a=hit[0] + 1, s=s or "Nessuna spiegazione sul sito: la risposta corretta è «" + opts[hit[0]] + "».", w=""))
    return out


def tutte(mate_quiz):
    """Unisce le banche. mate_quiz = lista già letta per Matematica discreta (con theme)."""
    alg = parse_numbered(ESAMI / "banca_algebra.md", "Algebra lineare", TEMI_ALGEBRA, "Esercizi di Algebra lineare")
    prg = parse_numbered(ESAMI / "banca_programmazione.md", "Programmazione", TEMI_PROG, "Esercizi di Programmazione")
    fnd = parse_numbered(ESAMI / "banca_fondamenti.md", "Fondamenti Info", TEMI_FND, "Esercizi di Fondamenti")
    return mate_quiz + alg + parse_fondamenti() + fnd + prg
