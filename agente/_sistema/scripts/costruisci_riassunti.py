"""Converte i Word dei riassunti in pagine web leggibili da qualunque dispositivo (anche senza Word).

Legge:  Riassunto <materia>.docx (nella cartella UNI)
Scrive: pagina_studio/riassunti/<materia>/index.html (+ media/ con le figure)
Il Quaderno le linka dalla scheda «Riassunti»; serve.py le serve, e si pubblicano come file statici.
Serve pandoc (https://pandoc.org). Uso:  python costruisci_riassunti.py
"""
import re
import shutil
import subprocess
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent          # _sistema
UNI = BASE.parent.parent                                # cartella UNI
PAG = BASE / "pagina_studio"
OUT = PAG / "riassunti"
MATERIE = {  # slug -> (file Word, titolo)
    "algebra-lineare": ("Riassunto Algebra lineare.docx", "Algebra lineare"),
    "fondamenti-informatica": ("Riassunto Fondamenti Informatica.docx", "Fondamenti di Informatica"),
    "laboratorio": ("Riassunto Laboratorio.docx", "Laboratorio"),
    "matematica-discreta": ("Riassunto Matematica discreta.docx", "Matematica discreta"),
    "programmazione": ("Riassunto Programmazione.docx", "Programmazione"),
}


def main():
    pandoc = shutil.which("pandoc")
    if not pandoc:
        sys.exit("pandoc non trovato: installalo da https://pandoc.org")
    for slug, (nome, titolo) in MATERIE.items():
        src = UNI / nome
        if not src.exists():
            print(f"  salto {slug}: manca {nome}")
            continue
        d = OUT / slug
        if d.exists():
            shutil.rmtree(d)
        d.mkdir(parents=True)
        subprocess.run([pandoc, str(src), "-f", "docx", "-t", "html5", "--mathml", "--extract-media=.", "--toc", "--toc-depth=2",
                        "--template", str(PAG / "riassunto_template.html"), "-M", f"pagetitle={titolo}", "-M", f"title={titolo}", "-o", "index.html"],
                       cwd=d, check=True, stdin=subprocess.DEVNULL)
        n = len(list((d / "media").glob("*"))) if (d / "media").exists() else 0
        print(f"  {titolo}: {(d / 'index.html').stat().st_size // 1024} KB, {n} figure")


if __name__ == "__main__":
    main()
