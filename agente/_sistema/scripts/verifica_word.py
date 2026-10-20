"""Controllo di qualita' dei Word di riassunti.

Uso:
    python verifica_word.py                      # controlla tutti e 4 i Word
    python verifica_word.py "Algebra lineare"    # una sola materia (nome della cartella)

Controlla: marcatori rimasti (** ^{ _{), graffe sbilanciate, doppi spazi, frasi vietate
("le fonti", "come detto nell'audio"...), refusi noti, numerazione dei capitoli (salti/duplicati).
Esce con codice 1 se trova problemi "ERRORE", cosi' si puo' usare in automatico.
"""
import re
import sys
from pathlib import Path

from docx import Document

UNI = Path(__file__).resolve().parent.parent.parent.parent
WORDS = {
    "Algebra lineare": "Riassunto Algebra lineare.docx",
    "Matematica discreta": "Riassunto Matematica discreta.docx",
    "Fondamenti Info": "Riassunto Fondamenti Informatica.docx",
    "Programmazione": "Riassunto Programmazione.docx",
    "Programmazione/Laboratorio": "Riassunto Laboratorio.docx",
}
FORBIDDEN = [
    r"\ble fonti\b", r"\bfonti fornite\b", r"come (detto|ricordato) nell'audio", r"\bnell'audio\b",
    r"\bsecondo il documento\b", r"\bnotebook\b",
]
KNOWN_TYPOS = {
    r"Algebraic Logic Unit": "ALU = Arithmetic Logic Unit",
    r"\bNascosto negli anni": "refuso ('Nascosto' -> 'Nato')",
    r"\bdell me overflow\b": "refuso ('dell me overflow')",
    r"\bin movement\b": "refuso ('movement' -> 'movimento')",
    r"all'\s*$": None,  # frase troncata
}
HEAD = re.compile(r"^\s*(?:Capitolo\s+)?(\d+)\s*[.:]\s*\S")


def is_heading(p) -> bool:
    t = p.text.strip()
    if not t or len(t) > 130 or not HEAD.match(t):
        return False
    return bool(p.runs) and bool(p.runs[0].bold)


def is_code(p) -> bool:
    """Paragrafo di codice/schema (font a spaziatura fissa): niente controlli tipografici."""
    return any((r.font.name or "").lower() in ("consolas", "courier new") for r in p.runs)


def is_formula(t: str) -> bool:
    return bool(re.search(r"[⟺⟹⇒→∈∉∧∨=]", t)) and "  " in t


def check(name: str) -> tuple[int, int]:
    path = UNI / WORDS[name]
    if not path.exists():
        print(f"[{name}] file non trovato: {path}")
        return 1, 0
    doc = Document(str(path))
    errors, warns = [], []
    nums = []
    for i, p in enumerate(doc.paragraphs, 1):
        t = p.text
        if not t.strip():
            continue
        loc = f"par.{i} «{t[:50]}…»"
        code = is_code(p)
        # marcatori rimasti: **parola** (coppia con testo dentro), ^{ o _{ ; un "**" isolato puo' essere codice C (es. int** p)
        if re.search(r"\*\*[^\s*][^*]*[^\s*]\*\*|\*\*[^\s*]\*\*|\^\{|_\{", t):
            errors.append(f"{loc}: marcatore di formattazione rimasto")
        if not code and t.count("{") != t.count("}"):
            errors.append(f"{loc}: graffe sbilanciate")
        for pat in FORBIDDEN:
            if re.search(pat, t, re.I):
                warns.append(f"{loc}: frase da evitare ({pat})")
        for pat, why in KNOWN_TYPOS.items():
            if why and re.search(pat, t):
                errors.append(f"{loc}: {why}")
        if not code and not is_formula(t) and re.search(r"\S  +\S", t) and len(t) > 40:
            warns.append(f"{loc}: doppio spazio")
        base_t = "".join(r.text for r in p.runs if not (r.font.subscript or r.font.superscript))   # senza i pedici delle basi (…₂)
        if any(not re.fullmatch(r"[01]+", m) for m in re.findall(r"\d{12,}", base_t)):   # le stringhe binarie lunghe sono legittime
            warns.append(f"{loc}: sequenza numerica sospetta (residuo di immagine?)")
        if is_heading(p):
            nums.append((int(HEAD.match(t.strip()).group(1)), i, t.strip()[:60]))
    for (a, _, _), (b, ib, tb) in zip(nums, nums[1:]):
        if b == a:
            errors.append(f"numerazione: capitolo {b} duplicato («{tb}», par.{ib})")
        elif b != a + 1:
            warns.append(f"numerazione: salto da {a} a {b} («{tb}», par.{ib})")
    print(f"\n=== {name}: {len(doc.paragraphs)} paragrafi, {len(nums)} titoli numerati "
          f"(ultimo: {nums[-1][0] if nums else '-'}) ===")
    for e in errors:
        print("  ERRORE:", e)
    for w in warns:
        print("  avviso:", w)
    if not errors and not warns:
        print("  tutto ok")
    return len(errors), len(warns)


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    names = [a for a in sys.argv[1:]] or list(WORDS)
    tot_e = 0
    for n in names:
        if n not in WORDS:
            sys.exit(f"Materia sconosciuta: {n}. Valide: {', '.join(WORDS)}")
        e, _ = check(n)
        tot_e += e
    sys.exit(1 if tot_e else 0)


if __name__ == "__main__":
    main()
