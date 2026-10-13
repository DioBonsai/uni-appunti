---
name: riassunto
description: Crea il riassunto di una lezione universitaria (Algebra lineare, Matematica discreta, Fondamenti Info, Programmazione) continuando il Word esistente di Emanuele. Si usa con /riassunto <materia> <lezione> o quando chiede di "fare il riassunto della lezione N", "continuare il Word", "aggiungere la lezione".
---

# /riassunto <materia> <lezione>

Sostituisce il flusso NotebookLM di Emanuele. Leggi sempre prima `CLAUDE.md`, `STILE.md`, `STATO.md` nella cartella UNI.

## 1. Preparazione (senza chiedere nulla)
1. Da `STATO.md` ricava: Word di destinazione, prossima numerazione, cosa è già coperto.
2. Raccogli le fonti della lezione in `_sistema/fonti_testo/<materia>/` (testo già estratto/trascritto: PDF con testo, appunti a mano trascritti `L<n>_appunti_*.md`) e, solo se serve, nei PDF originali in `_sistema/fonti/<materia>/` (leggili con il Read tool senza `pages`); le trascrizioni audio sono in `_sistema/trascrizioni/`. Se esistono PDF senza testo non ancora trascritti (vedi `_sistema/fonti_testo/DA_TRASCRIVERE.txt`) leggili e salva la trascrizione in `fonti_testo` per non rileggerli. Lancia `python _sistema/scripts/estrai_fonti.py` per aggiornare la cache.
   - Se mancano fonti nuove in `_sistema/fonti`, cerca in `C:\Users\admin\Downloads` SOLO per nome pertinente (materia, "lezione", data) e copiale nella cartella, mai altro.
   - I PDF scansionati si leggono con il Read tool (senza `pages`). Per i PDF con testo usa `pdftotext -layout`.
3. Rileggi gli ultimi 2 capitoli del Word (estrai testo dal .docx) per imitare struttura, lunghezza e tono. Per estrarre testo: `python -c "from docx import Document; ..."` con il Python in CLAUDE.md.

## 2. Elenco macro-argomenti (primo e unico checkpoint)
Presenta SOLO:
- i macro-argomenti della lezione, incrociando appunti + audio/trascrizione + dispense/libro (nota se il docente ha detto cose non nel libro, o se il libro ha cose non dette a lezione);
- la proposta di raggruppamento in capitoli con titolo e numero (continuando dal Word);
- eventuali contraddizioni tra fonti o punti da verificare.
Poi ATTENDI l'ok di Emanuele. Non scrivere capitoli prima.

## 3. Un capitolo alla volta
Per ogni capitolo approvato:
1. Scrivi la bozza in `_sistema/bozze/<materia>_cap<N>.md` (usa il formato di `aggiungi_capitolo.py`: `# N. Titolo`, `## Sottotitolo`, `**grassetto**`, `- elenco`). Rispetta `STILE.md`: via di mezzo tra discorsivo ed elenchi. **Figure**: dove un disegno chiarisce una definizione o un esempio (soprattutto Matematica discreta e Algebra: funzioni con le frecce, Venn, grafici, piano complesso, controimmagini) generalo con `_sistema/scripts/figure_math.py`, aprilo con Read per controllare che sia giusto e leggibile, e inseriscilo nella bozza con `![didascalia](figure/nome.png|larghezza_cm)`; il revisore controlla anche le figure. Poche figure ma utili: una per concetto che si capisce meglio vedendolo.
2. Lancia il subagente `revisore-riassunti` passandogli: il percorso della bozza, le fonti usate e `STILE.md`. Non dirgli cosa pensi sia giusto. Applica le correzioni confermate; i dubbi li riporti a Emanuele.
3. Mostra a Emanuele il capitolo (solo testo, senza ripetere la revisione per intero) con in fondo una riga "Revisione: N correzioni applicate, M punti da verificare".
4. Dopo il suo ok (o "procedi"), inserisci nel Word:
   `python _sistema/scripts/aggiungi_capitolo.py "Riassunto <materia>.docx" <bozza>.md`
   Se il Word è aperto lo script si rifiuta: chiedi di chiuderlo.
5. Aggiorna `STATO.md` (capitoli, prossima numerazione, lezione ✅).

## 4. Chiusura lezione
Quando tutti i capitoli sono dentro, proponi (senza farli): formulario di una pagina, 5-10 esercizi tipo esame, flashcard Anki per la lezione (`/ripasso`).

## Cose da non fare
- Non incollare nel testo frasi del tipo "le fonti dicono"/"come detto nell'audio".
- Non inventare dimostrazioni o esempi non supportati: se li aggiungi per chiarezza, devono essere verificabili (controlla i calcoli).
- Non toccare i capitoli esistenti del Word, nemmeno per correggere refusi: quelle correzioni si propongono a parte (fase di pulizia).
