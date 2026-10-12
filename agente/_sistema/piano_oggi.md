# Piano di ripasso — 2026-10-12

⚠ **Attenzione prima di tutto**: le cartelle delle materie (`Algebra lineare/`, `Matematica discreta/`, `Fondamenti Info/`, `Programmazione/`) non ci sono più in `UNI\`: i Word sono ora file sciolti nella cartella `UNI\` (es. `Riassunto Algebra lineare.docx`), e le dispense PDF (Algebra, slide Programmazione) risultano cancellate dal repo. Il contenuto dei Word è lo stesso (stesso hash) tranne Matematica discreta, che ha **32 nuove evidenziazioni gialle** non ancora salvate con un commit (bene: segno che hai studiato altro, ma va verificato). Gli script (`aggiungi_capitolo.py`, `verifica_word.py`, `backup_onedrive.py`) puntano ancora ai vecchi percorsi con sottocartella: finché non confermi se questo spostamento è voluto, i prossimi `/riassunto` potrebbero fallire o scrivere nel posto sbagliato. Prima di lanciare un nuovo `/riassunto`, conferma con Emanuele dove devono stare i Word e fai `git add -A && git commit` per mettere in sicurezza lo stato attuale (compresi i cap. già scritti il 9 ott, non ancora committati... verificare).

Date d'esame non ancora note (Moodle oggi ha fatto login correttamente, 0 novità). Priorità basata su rotazione (8 ott Mate discreta, 9 ott Fondamenti, 10 ott Programmazione → oggi tocca Algebra lineare) e su capitoli non ancora studiati.

## Oggi (max 90', 3 blocchi da 30')

**Blocco 1 (30') — Algebra lineare, cap. 1 "Numeri reali: vettori, campi"**
File: `Riassunto Algebra lineare.docx` (ex `Algebra lineare/Riassunto Algebra lineare.docx`). Nessun capitolo di Algebra è ancora evidenziato (cap. 1-9 tutti da studiare): si parte dal cap. 1.

**Blocco 2 (30') — Matematica discreta: prima simulazione, `/esame quiz` su funzioni e appartenenza/inclusione**
`errori.md` è ancora vuoto: non hai mai fatto una simulazione. Tra gli argomenti già nel Word, "funzioni, composizione, iniettiva/suriettiva" (33 domande nei quiz passati) e "appartenenza e inclusione" (17 domande) sono i più frequenti all'esame (vedi `MAPPA_ESAMI.md`): a parità di materiale già pronto, sono quelli con più punti attesi.

**Blocco 3 (30') — Preparazione Algebra lineare L4 "Polinomi"**
Le dispense sono pronte da giorni (vedi `COPERTURA.md`), manca solo l'ok per `/riassunto algebra 4`. Rileggi le fonti e segna i macro-argomenti da proporre, così il prossimo riassunto parte subito dopo il tuo ok — a patto di aver chiarito prima il punto sulle cartelle qui sopra.

## Da tenere aggiornato
- **Struttura cartelle**: vedi avviso in cima — da chiarire con Emanuele prima di altri `/riassunto`.
- **Lezioni senza riassunto**: Algebra L4-L26 (L4 Polinomi pronta, manca l'ok); Mate discreta oltre L5 (prossima quando esce); Fondamenti oltre il cap. 1 del libro (servono le lezioni 07-35 del programma reale, vedi `COPERTURA.md`); Programmazione Lab02 (non ancora uscito).
- **Audio da trascrivere**: nessuno — i 21 audio in `_sistema/audio` hanno tutti la trascrizione corrispondente in `_sistema/trascrizioni`.
- **Novità Moodle**: controllo tornato a funzionare oggi (login ok, 0 novità) dopo 3 giorni di sessione scaduta. Restano aperti da prima: link Webex "Lezione 3: Numeri Complessi, II" di Algebra che punta a una registrazione 2025 (da verificare col docente) e le registrazioni Webex di Fondamenti non ancora scaricate. Ancora nessuna data d'esame pubblicata.
- **Task automatici fermi**: nessuno al momento — `moodle-controllo-giornaliero` ha ripreso a funzionare oggi.

Piano pronto: Algebra lineare
