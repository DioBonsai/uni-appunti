"""Esporta i 4 Word di riassunti in PDF per il telefono, senza usare Word: docx -> HTML (mammoth) -> PDF (Edge in modalita' headless).
Output: OneDrive\\UNI-PDF\\<Materia>.pdf (si sincronizza da solo). Salta i PDF gia' aggiornati.
Il PDF ha segnalibri "naturali" solo se Edge li genera; i titoli mantengono i colori dei Word (rosso/arancione).
Non vengono riportate le evidenziazioni gialle (restano solo nei Word).

Uso: python esporta_pdf.py [--force]
"""
import subprocess
import sys
import tempfile
from pathlib import Path

import mammoth

UNI = Path(__file__).resolve().parent.parent.parent.parent
DEST = Path.home() / "OneDrive" / "UNI-PDF"
WORDS = {
    "Algebra lineare": "Riassunto Algebra lineare.docx",
    "Matematica discreta": "Riassunto Matematica discreta.docx",
    "Fondamenti Info": "Riassunto Fondamenti Informatica.docx",
    "Programmazione": "Riassunto Programmazione.docx",
    "Programmazione/Laboratorio": "Riassunto Laboratorio.docx",
}
EDGE = [Path(r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"),
        Path(r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"),
        Path(r"C:\Program Files\Google\Chrome\Application\chrome.exe")]
CSS = """
@page { size: A4; margin: 16mm 14mm; }
body { font-family: 'Segoe UI', Arial, sans-serif; font-size: 11pt; line-height: 1.45; color: #111; }
h1 { color: #EE0000; font-size: 16pt; margin: 22pt 0 6pt; page-break-after: avoid; }
h2 { color: #E97132; font-size: 12.5pt; margin: 14pt 0 4pt; page-break-after: avoid; }
p { margin: 0 0 6pt; } ul, ol { margin: 0 0 6pt 18pt; padding: 0; } li { margin: 0 0 3pt; }
code, pre { font-family: Consolas, monospace; font-size: 9pt; }
"""


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    force = "--force" in sys.argv
    edge = next((e for e in EDGE if e.exists()), None)
    if edge is None:
        sys.exit("Edge/Chrome non trovato.")
    DEST.mkdir(parents=True, exist_ok=True)
    for materia, fname in WORDS.items():
        src = UNI / fname
        pdf = DEST / (materia.replace("/", " - ") + ".pdf")
        if pdf.exists() and pdf.stat().st_mtime >= src.stat().st_mtime and not force:
            print(f"gia' aggiornato: {materia}")
            continue
        with open(src, "rb") as f:
            html = mammoth.convert_to_html(f).value
        with tempfile.TemporaryDirectory() as td:
            h = Path(td) / "doc.html"
            h.write_text(f"<!doctype html><html lang='it'><head><meta charset='utf-8'><style>{CSS}</style></head><body>{html}</body></html>", encoding="utf-8")
            r = subprocess.run([str(edge), "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
                                f"--print-to-pdf={pdf}", h.as_uri()], capture_output=True, timeout=180)
        ok = pdf.exists() and pdf.stat().st_size > 5000
        print(f"{'PDF creato' if ok else 'ERRORE'}: {materia} ({pdf.stat().st_size // 1024} KB)" if pdf.exists() else f"ERRORE: {materia}")


if __name__ == "__main__":
    main()
