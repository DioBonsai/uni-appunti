"""Cache testuale delle fonti: converte i PDF/Word con testo in .md in _sistema/fonti_testo/<materia>/.

Cosi' le fonti si leggono una volta sola (e si puo' cercare con grep) invece di rileggerle ogni volta.
I PDF scansionati / scritti a mano NON hanno testo: vengono elencati in `DA_TRASCRIVERE.txt` e si
trascrivono (con la lettura visiva di Claude) in file `<nome>.md` messi nella stessa cartella.

Uso:  python estrai_fonti.py
"""
import sys
from pathlib import Path

import pymupdf
from docx import Document

BASE = Path(__file__).resolve().parent.parent
FONTI = BASE / "fonti"
OUT = BASE / "fonti_testo"
MIN_CHARS_PER_PAGE = 120   # sotto questa media la pagina e' considerata "immagine"


def pdf_text(path: Path):
    doc = pymupdf.open(path)
    pages = [p.get_text("text") for p in doc]
    n = max(1, len(pages))
    avg = sum(len(t.strip()) for t in pages) / n
    return pages, avg


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    OUT.mkdir(exist_ok=True)
    todo, done = [], 0
    for src in sorted(FONTI.rglob("*")):
        if src.suffix.lower() not in (".pdf", ".docx"):
            continue
        rel = src.relative_to(FONTI)
        dst = (OUT / rel).with_suffix(".md")
        if dst.exists() and dst.stat().st_mtime >= src.stat().st_mtime:
            continue
        dst.parent.mkdir(parents=True, exist_ok=True)
        try:
            if src.suffix.lower() == ".docx":
                text = "\n".join(p.text for p in Document(str(src)).paragraphs)
                dst.write_text(text, encoding="utf-8"); done += 1
                continue
            pages, avg = pdf_text(src)
            if avg < MIN_CHARS_PER_PAGE:
                todo.append(f"{rel}  ({len(pages)} pagine, ~{int(avg)} car/pagina)")
                continue
            body = "\n\n".join(f"<!-- pagina {i} -->\n{t.strip()}" for i, t in enumerate(pages, 1))
            dst.write_text(f"# {src.stem}\n\n{body}\n", encoding="utf-8"); done += 1
        except Exception as e:  # noqa: BLE001
            todo.append(f"{rel}  (errore: {e})")
    (OUT / "DA_TRASCRIVERE.txt").write_text(
        "PDF senza testo (scansioni/appunti a mano): trascrivere a mano o con lettura visiva.\n\n" + "\n".join(todo) + "\n",
        encoding="utf-8")
    print(f"Estratti {done} file in fonti_testo/. Senza testo (da trascrivere): {len(todo)}")
    for t in todo:
        print("  -", t)


if __name__ == "__main__":
    main()
