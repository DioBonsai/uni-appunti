"""Toglie l'ultimo capitolo (23) dal Word di Fondamenti, con backup. Il testo si puo' reinserire con
aggiungi_capitolo.py "Riassunto Fondamenti Informatica.docx" _sistema/bozze/fondamenti_cap23.md"""
import shutil, sys
from datetime import datetime
from pathlib import Path
from docx import Document
UNI = Path(__file__).resolve().parents[3]   # cartella UNI (accanto a agente/)
W = UNI / "Riassunto Fondamenti Informatica.docx"
BK = UNI / "agente" / "_sistema" / "backup"
lock = W.with_name("~$" + W.name[2:])
if lock.exists(): sys.exit("Word aperto")
d = Document(str(W)); pars = d.paragraphs
i = next(k for k, p in enumerate(pars) if p.text.startswith("23. Regole di Inferenza"))
resto = pars[i:]
assert not any(p.style.name.startswith("Heading 1") for p in resto[1:]), "ci sono altri capitoli dopo"
assert not any(r.font.highlight_color is not None for p in resto for r in p.runs), "evidenziazioni nel capitolo"
shutil.copy2(W, BK / f"{W.stem}_prima-rimozione-cap23_{datetime.now():%Y%m%d_%H%M%S}{W.suffix}")
for p in resto: p._p.getparent().remove(p._p)
d.save(str(W)); print("rimossi", len(resto), "paragrafi")
