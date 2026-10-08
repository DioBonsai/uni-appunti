# Audit fattuale - Fondamenti dell'Informatica (Brookshear, cap. 1)

**Riepilogo:** 4 problemi totali: 1 alta, 1 media, 2 bassa.

**Capitoli controllati:** tutti gli 11 (1 Flip-flop, 2 Esadecimale, 3 Memoria di massa, 4 Testo e colori, 5 Architettura/RAM, 6 Codifica dati, 7 Binario, 8 Interi, 9 Virgola mobile, 10 Compressione, 11 Errori).
Numeri di paragrafo = indice dello script (enumerate(d.paragraphs,1)).

Capitoli senza problemi: 1, 2, 4 (salvo nota bassa), 5, 6, 8, 9, 11. Verificati con Python/libro: 101101012=B5, A4C8, 100101=37, 13=1101, 101.101=5,625, -6=1010, 7-5=0010 (carry troncato), 5+4=1001 (-7), 2 5/8 -> 01101010 (2 1/2), 2 1/2+1/8+1/8 = 2 1/2 vs 2 3/4, LZW 121343434, RLE 253+118+87=458, 44100x32 = 1.411.200 bit/s, 15 bit per 25.000 parole, 6x8=48 bit, Hamming 3/5, parita, CD-DA 1/2 e CD-ROM 1/20.000, JPEG 10:1-30:1, 2x2 -> fattore 4, MP3 64 Kbps, MPEG 40 Mbps.

---

### [GRAVITÀ: alta] Capitolo 7, paragrafo 198
**Testo attuale:** «Ultimo riporto registrato a sinistra: 1 Risultato finale: 1010101 (corrispondente al valore decimale 53).»
**Problema:** 11010 + 11011 = 110101 (53), non 1010101 (che vale 85): il risultato scritto contraddice sia i passi elencati sopra sia il valore decimale indicato.
**Correzione proposta:** «Ultimo riporto registrato a sinistra: 1. Risultato finale: 110101 (corrispondente al valore decimale 53 = 26 + 27).»
**Fonte/verifica:** calcolo Python: bin(0b11010+0b11011) = 0b110101 = 53; 0b1010101 = 85.

### [GRAVITÀ: media] Capitolo 3, paragrafo 67
**Testo attuale:** «capacità superiori a 50 GB»
**Problema:** il libro non cita 50 GB: dice solo che il Blu-ray offre "oltre cinque volte la capacità di un DVD"; il dato reale e 25 GB (strato singolo) / 50 GB (doppio strato), quindi "superiori a 50 GB" e impreciso.
**Correzione proposta:** «e capacità oltre cinque volte quella di un DVD (25 GB a strato singolo, fino a 50 GB a doppio strato).»
**Fonte/verifica:** libro sez. 1.3 (grep «Blu-ray», righe ~1813-1816: «over five times the capacity of a DVD»).

### [GRAVITÀ: bassa] Capitolo 10, paragrafo 266
**Testo attuale:** «LZW - Lempel-Ziv-Welsh ... Lempel, Ziv e Welsh»
**Problema:** il terzo autore e Terry Welch (il libro scrive "Welsh", grafia errata ereditata); da usare comunque coerentemente: se si vuole la grafia storica corretta e Welch.
**Correzione proposta:** «LZW - Lempel-Ziv-Welch ... Lempel, Ziv e Welch» (all'esame va bene anche la grafia del libro, "Welsh").
**Fonte/verifica:** libro sez. 1.9 (grep «Welsh», riga ~3567); conoscenza storica (Terry Welch, 1984).

### [GRAVITÀ: bassa] Capitolo 4, paragrafo 80
**Testo attuale:** «Nato negli anni '40 e '50 per standardizzare la comunicazione tra macchine diverse»
**Problema:** il libro dice che negli anni '40 e '50 esistevano molti codici incompatibili e che l'ANSI adotto poi l'ASCII per risolvere il problema; l'ASCII non e "nato" negli anni '40-'50 (standardizzato nel 1963).
**Correzione proposta:** «Negli anni '40 e '50 esistevano molti codici incompatibili tra le diverse macchine; per risolvere il problema l'ANSI adotto il codice ASCII (standardizzato nei primi anni '60), che utilizzava originariamente sequenze di 7 bit...»
**Fonte/verifica:** libro sez. 1.4 (grep «ASCII», righe ~1899-1905).
