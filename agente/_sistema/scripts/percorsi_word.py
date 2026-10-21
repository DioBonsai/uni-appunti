"""I Word dei riassunti stanno come file sciolti nella cartella UNI (nessuna sottocartella per materia).
trova() accetta anche i vecchi percorsi (es. "Matematica discreta/Appunti matematica discreta.docx") e li traduce nel nome nuovo."""
from pathlib import Path

NOMI = {  # vecchio nome -> nome attuale
    "Appunti matematica discreta.docx": "Riassunto Matematica discreta.docx",
    "Fondamenti Informatica.docx": "Riassunto Fondamenti Informatica.docx",
    "Laboratorio.docx": "Riassunto Laboratorio.docx",
}


ARCHIVIO = "_archivio_word"  # dal 21 ott 2026 i Word stanno qui (non servono piu': i riassunti sono nel sito)


def trova(uni: Path, cartella: str, fname: str) -> Path:
    """UNI/_archivio_word/<nome attuale> (o UNI/<nome> se ancora sciolto); la cartella vecchia viene ignorata."""
    n = NOMI.get(fname, fname)
    a = uni / ARCHIVIO / n
    return a if a.exists() else uni / n
