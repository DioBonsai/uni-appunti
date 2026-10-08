# UNI: appunti e riassunti di Informatica (UniTo, canale B, 1° anno 2026/27)

Questa cartella contiene i riassunti Word di Emanuele per 4 materie. Claude sostituisce il flusso
che prima faceva con NotebookLM: da fonti (appunti a mano, schede, dispense, slide, libri, audio
trascritti) a capitoli di riassunto che continuano il Word esistente.

## Struttura
- `Algebra lineare/`, `Matematica discreta/`, `Fondamenti Info/`, `Programmazione/`: i Word di riassunti (fonte di verità, NON si riscrivono da zero).
- `_sistema/fonti/<materia>/`: copie ordinate delle fonti (lezione per lezione: `L3_appunti_7ott.pdf`, `L3_scheda.pdf`, libri, slide).
- `_sistema/audio/` → `_sistema/trascrizioni/`: audio delle lezioni e loro trascrizione (`scripts/trascrivi.py`).
- `_sistema/scripts/`: `trascrivi.py`, `aggiungi_capitolo.py`.
- `_sistema/backup/`: copia automatica del Word prima di ogni modifica.
- `_sistema/anki/`, `_sistema/esercizi/`: output di ripasso (fase 3).
- `STATO.md`: a che capitolo/lezione è ogni materia. Aggiornarlo SEMPRE dopo ogni capitolo.
- `STILE.md`: stile di scrittura da imitare.

## Regole ferree
1. Mai riscrivere o spostare i Word esistenti. Solo aggiungere in fondo, con backup (usa `aggiungi_capitolo.py`). Se il Word è aperto (`~$...` presente) fermarsi e dirlo.
2. Un capitolo alla volta; prima l'elenco dei macro-argomenti e dei capitoli, attendere l'ok, poi i capitoli. La numerazione continua da quella del Word.
3. Fonti in ordine di fiducia: dispense/libro > schede > appunti a mano > trascrizioni audio (possono avere errori sui termini tecnici). Se due fonti si contraddicono, dirlo, non scegliere in silenzio.
4. Non inventare. Se un dato non è nelle fonti, segnalarlo come "da verificare".
5. Ogni capitolo passa dal revisore (subagente `revisore-riassunti`) prima di essere inserito nel Word.
6. Lingua: italiano. Pronomi per Emanuele: lui/neutro, non assumere altro.
7. File in `~/Downloads` non universitari: non toccarli e non leggerli.
8. Python: `C:\Users\admin\AppData\Local\Programs\Python\Python312\python.exe`.

## Comandi
- `/riassunto <materia> <lezione>`: flusso completo (vedi `.claude/skills/riassunto/SKILL.md`).
- `/trascrivi`: trascrive gli audio nuovi.
- `/ripasso <materia>`: formulario, esercizi, flashcard Anki (fase 3).
