# UNI: appunti e riassunti di Informatica (UniTo, canale B, 1° anno 2026/27)

Questa cartella contiene i riassunti Word di Emanuele per 4 materie. Claude sostituisce il flusso
che prima faceva con NotebookLM: da fonti (appunti a mano, schede, dispense, slide, libri, audio
trascritti) a capitoli di riassunto che continuano il Word esistente.

## Struttura
**Aprire Claude Code in `C:\Users\admin\Desktop\UNI\agente`**: qui stanno CLAUDE.md, skill e comandi. La cartella padre `UNI\` contiene solo le 4 materie e questa cartella `agente\`.
- `../Algebra lineare/`, `../Matematica discreta/`, `../Fondamenti Info/`, `../Programmazione/` (cartelle sorelle di `agente`): i Word di riassunti (fonte di verità, NON si riscrivono da zero).
- `_sistema/fonti/<materia>/`: copie ordinate delle fonti (lezione per lezione: `L3_appunti_7ott.pdf`, `L3_scheda.pdf`, libri, slide).
- `_sistema/audio/` → `_sistema/trascrizioni/`: audio delle lezioni e loro trascrizione (`scripts/trascrivi.py`).
- `_sistema/fonti_testo/<materia>/`: **cache di testo** delle fonti (PDF con testo estratti, appunti a mano già trascritti `L<n>_appunti_*.md`). Leggere SEMPRE prima questa, poi i PDF originali. `DA_TRASCRIVERE.txt` elenca le scansioni ancora senza testo (slide Fondamenti, libro Mori).
- `_sistema/glossario.txt`: termini tecnici per Whisper.
- `_sistema/scripts/`: `trascrivi.py` (Whisper), `aggiungi_capitolo.py` (inserisce nel Word; poi controlla e fa backup da solo), `verifica_word.py` (qualità dei Word), `backup_onedrive.py`, `estrai_fonti.py`, `stili_word.py` (Titolo 1/2 veri), `genera_esercizi.py` (quiz/problemi verificati con SymPy), `anki_build.py`, `installa_globale.py`. Il percorso del Word si dà relativo a `UNI\`, es. `"Algebra lineare/Riassunto Algebra lineare.docx"`.
- `_sistema/bozze/`: bozze dei capitoli prima dell'inserimento nel Word.
- `_sistema/backup/`: copia automatica del Word prima di ogni modifica. Copia aggiuntiva sincronizzata: `C:\Users\admin\OneDrive\UNI-backup\`.
- `_sistema/esami/`: banca degli esami di Mate discreta (`quiz_*.md` 150 domande, `prob_*.md` 30 problemi svolti, `MAPPA_ESAMI.md`, `generati/`). Le soluzioni ufficiali contengono errori noti (righe "ATTENZIONE").
- `_sistema/flashcard/<materia>.md` → `_sistema/anki/<materia>.apkg` (mazzi Anki). `_sistema/errori.md`: registro errori delle simulazioni. `_sistema/esercizi/`: formulari ed esercizi.
- `STATO.md` (in questa cartella): a che capitolo/lezione è ogni materia. Aggiornarlo SEMPRE dopo ogni capitolo.
- `STILE.md` (in questa cartella): stile di scrittura da imitare.

## Regole ferree
0. Il repo Git sta in `UNI\` (cartella padre); le esclusioni (audio, fonti, backup, file temporanei di Word) sono in `.git/info/exclude`, non c'è un `.gitignore` visibile.
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
- `/trascrivi`: trascrive gli audio nuovi (Whisper locale, in background).
- `/ripasso <materia> [lezione]`: formulario, esercizi svolti, flashcard Anki, mappa concettuale.
- `/esame [quiz|problema|completo] [argomento]`: simulazione d'esame di Matematica discreta con correzione e registro errori.
- `/moodle`: controlla slide, annunci, esami e registrazioni su Moodle (il login lo fa sempre Emanuele).
- Skill, comandi e revisore sono installati anche a livello utente (`~/.claude`), quindi funzionano da qualsiasi cartella; dopo ogni modifica a `agente/.claude` rilanciare `python _sistema/scripts/installa_globale.py`.

## Altre regole operative
9. Dopo ogni inserimento nel Word: `aggiungi_capitolo.py` esegue da solo `verifica_word.py` e `backup_onedrive.py`; se segnala ERRORE, correggere prima di proseguire.
10. Il repo Git (in `UNI\`) ha il remoto GitHub privato `uni-appunti`: dopo un lavoro concluso, `git add -A && git commit` e `git push`. Mai pubblicare in repo pubblici.
11. Mai scrivere sui Word che sono aperti in Word (file di blocco `~$`): avvisare Emanuele di chiuderli.
12. Convenzione permutazioni (Mate discreta): composizione da destra a sinistra.

## Moodle automatico
- Attività pianificata `moodle-controllo-giornaliero` (ogni giorno ~08:12, solo con l'app aperta): legge i 4 corsi su Moodle, scarica **in automatico solo i PDF nuovi ≤ 25 MB** (autorizzazione permanente di Emanuele, 8 ott 2026, limitata a questo), elenca senza scaricare ogni altro file e le registrazioni Webex, riassume gli annunci (⚠ per date d'esame). Report in `_sistema/moodle_report.md`, stato in `_sistema/moodle_stato.json`.
- Se la sessione Moodle è scaduta l'attività si ferma e lo dice: il login lo fa SEMPRE Emanuele nel browser pane. Mai inserire password.
- Webex, video, zip, docx/pptx: mai scaricati senza un nuovo ok esplicito.
