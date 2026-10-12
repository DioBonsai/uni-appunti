# UNI: appunti e riassunti di Informatica (UniTo, canale B, 1° anno 2026/27)

Questa cartella contiene i riassunti Word di Emanuele per 4 materie. Claude sostituisce il flusso
che prima faceva con NotebookLM: da fonti (appunti a mano, schede, dispense, slide, libri, audio
trascritti) a capitoli di riassunto che continuano il Word esistente.

## Struttura
**Aprire Claude Code in `C:\Users\admin\Desktop\UNI\agente`**: qui stanno CLAUDE.md, skill e comandi. La cartella padre `UNI\` contiene solo i 5 Word di riassunti (file sciolti, nessuna sottocartella per materia) e questa cartella `agente\`.
- `../Riassunto Algebra lineare.docx`, `../Riassunto Matematica discreta.docx`, `../Riassunto Fondamenti Informatica.docx`, `../Riassunto Programmazione.docx`, `../Riassunto Laboratorio.docx` (file sciolti in `UNI\`, accanto a `agente`): i Word di riassunti (fonte di verità, NON si riscrivono da zero).
- `_sistema/fonti/<materia>/`: copie ordinate delle fonti (lezione per lezione: `L3_appunti_7ott.pdf`, `L3_scheda.pdf`, libri, slide).
- `_sistema/audio/` → `_sistema/trascrizioni/`: audio delle lezioni e loro trascrizione (`scripts/trascrivi.py`).
- `_sistema/fonti_testo/<materia>/`: **cache di testo** delle fonti (PDF con testo estratti, appunti a mano già trascritti `L<n>_appunti_*.md`). Leggere SEMPRE prima questa, poi i PDF originali. `DA_TRASCRIVERE.txt` elenca le scansioni ancora senza testo (slide Fondamenti, libro Mori).
- `_sistema/glossario.txt`: termini tecnici per Whisper.
- `_sistema/scripts/`: `trascrivi.py` (Whisper), `aggiungi_capitolo.py` (inserisce nel Word; poi controlla e fa backup da solo), `verifica_word.py` (qualità dei Word), `backup_onedrive.py`, `estrai_fonti.py`, `stili_word.py` (Titolo 1/2 veri), `genera_esercizi.py` (quiz/problemi verificati con SymPy), `anki_build.py`, `installa_globale.py`. Il percorso del Word si dà relativo a `UNI\`, es. `"Riassunto Algebra lineare.docx"`.
- `_sistema/bozze/`: bozze dei capitoli prima dell'inserimento nel Word.
- `_sistema/backup/`: copia automatica del Word prima di ogni modifica. Copia aggiuntiva sincronizzata: `C:\Users\admin\OneDrive\UNI-backup\`.
- `_sistema/esami/`: banca degli esami di Mate discreta (`quiz_*.md` 150 domande, `prob_*.md` 30 problemi svolti, `MAPPA_ESAMI.md`, `generati/`). Le soluzioni ufficiali contengono errori noti (righe "ATTENZIONE").
- `_sistema/flashcard/<materia>.md` → `_sistema/anki/<materia>.apkg` (mazzi Anki). `_sistema/errori.md`: registro errori delle simulazioni. `_sistema/esercizi/`: formulari ed esercizi.
- `STATO.md` (in questa cartella): a che capitolo/lezione è ogni materia. Aggiornarlo SEMPRE dopo ogni capitolo.
- `STILE.md` (in questa cartella): stile di scrittura da imitare.

Nota: oltre ai 4 Word delle materie esiste `../Riassunto Laboratorio.docx` (riassunto del laboratorio di Programmazione, numerazione propria, chiave `Programmazione/Laboratorio` negli script). I capitoli si aggiungono con `aggiungi_capitolo.py "Riassunto Laboratorio.docx" bozza.md`. Formato bozze: `**grassetto**`, `~corsivo~`, backtick per comandi/codice in linea (Consolas), blocchi ``` per il codice (Consolas 8,5 pt), backslash+asterisco per un `*` letterale.

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

## Strumenti di qualità e studio (aggiunti l'8 ott 2026)
- `python _sistema/scripts/selftest.py`: collaudo di tutto il sistema (librerie, Word, generatore, Anki, backup/ripristino, Whisper, git, Moodle). Lanciarlo a inizio sessione se qualcosa non torna.
- `python _sistema/scripts/misura_stile.py`: elenchi/paragrafi per capitolo; i nuovi capitoli devono restare vicini alla mediana (≈44% elenchi, paragrafi ≈30 parole). Emanuele ha chiesto più discorsivo, meno bullet.
- `python _sistema/scripts/frasi_docente.py`: estrae dalle trascrizioni le frasi "da esame/attenzione/errore" con timestamp (output in `_sistema/trascrizioni/da_esame/`). Usarle come suggerimenti per i capitoli, verificando sulle fonti (le trascrizioni sbagliano termini).
- `powershell -File _sistema/scripts/esporta_pdf.ps1`: PDF dei Word in `OneDrive\UNI-PDF` (per il telefono).
- `COPERTURA.md`: programma ufficiale vs Word. `/piano`: piano di ripasso. Audit dei capitoli esistenti in `_sistema/audit/` (le correzioni sono già applicate, vedi `applica_correzioni.py`); i punti lasciati aperti sono in `_sistema/audit/DA_DECIDERE.md`.
- **Feedback di stile**: quando Emanuele corregge lo stile ("troppo bullet", "più discorsivo", "meno schematico", ecc.) aggiungere SUBITO una riga alla sezione "Correzioni di Emanuele" di `STILE.md`.
- **Quaderno di ripasso (sito locale)**: si apre con `apri_quaderno.bat` (doppio clic) o `python _sistema/pagina_studio/serve.py` → http://127.0.0.1:8765 (solo su questo computer; se è già acceso apre solo il browser). Ricostruisce la pagina a ogni avvio. L'artefatto su claude.ai è stato abbandonato (12 ott 2026). Quiz per materia (si sceglie ogni volta: Matematica discreta 150 domande d'esame, Fondamenti 84, Algebra 40, Programmazione 40 + esercizi generati e verificati per Mate, Algebra e Fondamenti; banche in `_sistema/esami/`: `quiz_*.md`, `banca_algebra.md`, `banca_fondamenti.md`, `banca_programmazione.md`, `fondamenti_quiz.md`; loader in `scripts/quiz_banche.py`). Contiene: sessione di oggi (schede in scadenza + domande pesate + esercizi generati), quiz con correzione o simulazione a tempo, 30 problemi d'esame svolti, schede con 4 voti e intervalli accorciati dalla data d'esame, esporta/importa progressi, avanzamento letto dalle evidenziazioni dei Word. I progressi si salvano nel browser E in `_sistema/progressi.json` (v, ts, `th` = errori per tema, `qs` = domande, `cards`, `probs` = problemi, `hist`, `exams`): leggerlo per `/piano` e `/esame`. Sorgenti in `_sistema/pagina_studio/` (`body.html`, `app.js`, `extra.css`, `gen.js` generatore di esercizi, `template.html` solo head/CSS, `serve.py`); rigenerare a mano con `python _sistema/scripts/costruisci_pagina_studio.py`. Collaudo del generatore: `node _sistema/pagina_studio/test_gen.js` (deve dire 0 errori). Le date d'esame si mettono in `ESAMI` nello script o nella pagina.
- Percorsi dei Word: file sciolti in `UNI\` (`Riassunto <materia>.docx`); `scripts/percorsi_word.py` traduce ancora i vecchi percorsi con sottocartella, se capitano in qualche comando.
- Audit dei Word: `_sistema/audit/*.md` (report), `applica_correzioni.py` (registro delle 57 correzioni applicate l'8 ott), `DA_DECIDERE.md` (punti aperti).
- Registri automatici: `_sistema/moodle_report.md` / `moodle_log.md` (Moodle), `_sistema/piano_oggi.md` (piano di ripasso generato ogni sera alle 18:30 circa).
