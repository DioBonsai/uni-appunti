---
name: piano
description: Piano di ripasso giornaliero o settimanale per Emanuele, basato su cosa ha già studiato (evidenziazioni), argomenti deboli (registro errori), date degli esami e copertura dei programmi. Si usa con /piano o quando chiede "cosa studio oggi", "piano di ripasso", "organizzami lo studio".
---

# /piano [oggi|settimana]

Leggi `CLAUDE.md`, `STATO.md` (sezione "Cosa ha già studiato"), `COPERTURA.md`, `_sistema/errori.md`, `_sistema/moodle_report.md` (date d'esame e annunci, se presenti) e `_sistema/esami/MAPPA_ESAMI.md`.

## Regole di priorità
1. Esami imminenti (date nel report Moodle o dette da Emanuele): materia con l'esame più vicino prima.
2. Argomenti deboli: quelli con più errori in `errori.md`.
3. Capitoli **non studiati** (senza evidenziazioni) dei Word: da leggere e segnare a mano; indicare quali.
4. Ripasso a intervalli (1, 3, 7, 14 giorni) dei capitoli studiati: usa le date in `STATO.md` / git log dei Word per capire da quanto sono fermi.
5. Per Matematica discreta: pesare gli argomenti per frequenza d'esame (MAPPA_ESAMI.md).

## Output (breve, in italiano)
**Oggi** (max 90 minuti, 3 blocchi):
- Blocco 1 (30'): lettura/studio di un capitolo non studiato (nome del capitolo e file).
- Blocco 2 (30'): `/esame quiz <argomento debole>` oppure 15 flashcard Anki del mazzo indicato.
- Blocco 3 (30'): un esercizio/problema (`/esame problema`) o scrittura/revisione del prossimo capitolo con `/riassunto`.
**Settimana**: tabella giorno → materia → attività, con almeno 1 giorno di recupero libero.
Chiudi con una riga: "Cosa c'è di nuovo da fare per tenere il sistema aggiornato" (es. lezioni senza riassunto, audio da trascrivere, novità Moodle).

## Regole
- Non inventare date d'esame: se mancano, dillo e chiedile.
- Se Emanuele segna un blocco come fatto o sbagliato, aggiorna `_sistema/errori.md` e `STATO.md`.
