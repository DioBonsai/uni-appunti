"""Backup locale sincronizzato da OneDrive.

Copia i 4 Word e la cartella `agente` (senza audio, fonti, backup, trascrizioni grezze) in
    C:\\Users\\admin\\OneDrive\\UNI-backup\\corrente\\
e, se un Word e' cambiato dall'ultima volta, ne salva anche una versione datata in
    C:\\Users\\admin\\OneDrive\\UNI-backup\\versioni\\<materia>\\
OneDrive si occupa poi di sincronizzare nel cloud. Nessun dato passa da questo script a servizi esterni.

Uso: python backup_onedrive.py            (silenzioso se non c'e' nulla di nuovo)
"""
import hashlib
import shutil
import sys
from datetime import datetime
from pathlib import Path

import sys as _s, pathlib as _pl
_s.path.insert(0, str(_pl.Path(__file__).resolve().parent))
from percorsi_word import trova as _trova  # noqa: E402
UNI = Path(__file__).resolve().parent.parent.parent.parent
DEST = Path.home() / "OneDrive" / "UNI-backup"
WORDS = {
    "Algebra lineare": "Riassunto Algebra lineare.docx",
    "Matematica discreta": "Riassunto Matematica discreta.docx",
    "Fondamenti Info": "Riassunto Fondamenti Informatica.docx",
    "Programmazione": "Riassunto Programmazione.docx",
    "Programmazione/Laboratorio": "Riassunto Laboratorio.docx",
}
SKIP_DIRS = {"audio", "fonti", "backup", "trascrizioni", "__pycache__", ".git"}


def digest(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def sync_file(src: Path, dst: Path) -> bool:
    if dst.exists() and dst.stat().st_size == src.stat().st_size and digest(dst) == digest(src):
        return False
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)
    return True


def main() -> None:
    if not DEST.parent.exists():
        sys.exit(f"OneDrive non trovato in {DEST.parent}: backup saltato.")
    changed = 0
    stamp = datetime.now().strftime("%Y%m%d_%H%M")
    for materia, fname in WORDS.items():
        src = _trova(UNI, '', fname)
        if not src.exists():
            continue
        if sync_file(src, DEST / "corrente" / materia / fname):
            changed += 1
            ver = DEST / "versioni" / materia / f"{src.stem}_{stamp}{src.suffix}"
            ver.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, ver)
    agente = UNI / "agente"
    for src in agente.rglob("*"):
        rel = src.relative_to(agente)
        if src.is_dir() or any(part in SKIP_DIRS for part in rel.parts):
            continue
        if src.stat().st_size > 20 * 1024 * 1024:
            continue
        if sync_file(src, DEST / "corrente" / "agente" / rel):
            changed += 1
    print(f"Backup OneDrive: {changed} file aggiornati in {DEST}" if changed else "Backup OneDrive: gia' aggiornato")


if __name__ == "__main__":
    main()
