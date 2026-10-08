---
name: esame
description: Simulazione d'esame di Matematica discreta (quiz da 10 domande e/o problema con punti), nel formato degli esami UniTo, con correzione e registro degli errori. Si usa con /esame o quando Emanuele chiede di "interrogarmi", "fare un quiz", "simulare l'esame", "esercizi di mate discreta".
---

# /esame [quiz|problema|completo] [argomento]

Leggi `CLAUDE.md`, `_sistema/esami/MAPPA_ESAMI.md` e `_sistema/errori.md`. Scopo: allenare Emanuele sul formato vero dell'esame, e poi correggere con spiegazione.

## Fonti di domande (in ordine)
1. **Generatore verificato** (preferito, domande nuove con risposta calcolata da SymPy):
   `python _sistema/scripts/genera_esercizi.py quiz --n 10` oppure `... problema`.
   Scrive `_sistema/esami/generati/<nome>.md` (testo) e `<nome>.json` (risposte e spiegazioni).
2. **Banca d'esame vera**: `_sistema/esami/quiz_*.md` (150 domande con RISPOSTA e SPIEGAZIONE) e `prob_*.md` (30 problemi svolti). Per "simulazione ufficiale": 10 domande scelte a caso dallo stesso file/prova.
3. Se Emanuele indica un argomento, filtra per l'etichetta `argomenti:` della banca. Se `errori.md` ha argomenti con molti errori, riservagli almeno 3 domande su 10.

## Svolgimento
1. Mostra SOLO il testo delle domande (mai il .json, né la riga RISPOSTA/SPIEGAZIONE o le soluzioni dei problemi). Per il quiz: tabella di risposte da compilare (es. `1:4 2:2 ...`). Dì che l'esame vero dura il tempo che vuole lui: non c'è cronometro, ma può dirti quando parte.
2. Attendi le risposte. Non anticipare nulla.
3. Correggi: per ogni domanda ✅/❌ + spiegazione breve (dal campo SPIEGAZIONE; se la domanda è della banca vera, ricalcola prima tu: le soluzioni ufficiali contengono errori noti, vedi righe ATTENZIONE). Per i problemi: confronta passo passo con la soluzione e assegna i punti per sottodomanda.
4. Punteggio finale (quiz: x/10) e i 2-3 argomenti più deboli.
5. Aggiorna `_sistema/errori.md` (riga di registro per ogni errore + tabella riassuntiva in cima).
6. Offri: ripetere solo sugli argomenti sbagliati, oppure aggiungere le domande sbagliate come flashcard (`_sistema/flashcard/Matematica discreta.md`, poi `python _sistema/scripts/anki_build.py "Matematica discreta"`).

## Regole
- Convenzione permutazioni: composizione da destra a sinistra.
- Non inventare domande a mano se esiste il generatore: le risposte devono essere verificate.
- Se Emanuele chiede un argomento non ancora fatto a lezione (es. gruppi), dillo ma procedi: serve come anteprima.
