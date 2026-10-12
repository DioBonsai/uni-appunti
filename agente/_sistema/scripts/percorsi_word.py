"""Trova i Word dei riassunti sia nella vecchia struttura (UNI/<materia>/<file>) sia come file sciolti in UNI/."""
from pathlib import Path

LOOSE = {
    "Riassunto Algebra lineare.docx": "Riassunto Algebra lineare.docx",
    "Appunti matematica discreta.docx": "Riassunto Matematica discreta.docx",
    "Fondamenti Informatica.docx": "Riassunto Fondamenti Informatica.docx",
    "Riassunto Programmazione.docx": "Riassunto Programmazione.docx",
    "Laboratorio.docx": "Riassunto Laboratorio.docx",
}


def trova(uni: Path, cartella: str, fname: str) -> Path:
    """Percorso del Word: quello vecchio se esiste, altrimenti il file sciolto in UNI/ (se c'è), altrimenti il vecchio."""
    old = uni / cartella / fname
    if old.exists():
        return old
    new = uni / LOOSE.get(fname, fname)
    return new if new.exists() else old
