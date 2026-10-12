"""I Word dei riassunti stanno come file sciolti nella cartella UNI (nessuna sottocartella per materia).
trova() accetta anche i vecchi percorsi (es. "Matematica discreta/Appunti matematica discreta.docx") e li traduce nel nome nuovo."""
from pathlib import Path

NOMI = {  # vecchio nome -> nome attuale
    "Appunti matematica discreta.docx": "Riassunto Matematica discreta.docx",
    "Fondamenti Informatica.docx": "Riassunto Fondamenti Informatica.docx",
    "Laboratorio.docx": "Riassunto Laboratorio.docx",
}


def trova(uni: Path, cartella: str, fname: str) -> Path:
    """UNI/<nome attuale>; la cartella (vecchia struttura) viene ignorata."""
    return uni / NOMI.get(fname, fname)
