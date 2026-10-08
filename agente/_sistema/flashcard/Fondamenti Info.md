## Flip-flop
D: Cos'è un flip-flop e quali sono i suoi stati di ingresso?
R: Il circuito che memorizza 1 bit. Impulso sul comando di set → uscita 1; impulso sul reset → uscita 0; ingressi entrambi a 0 → conserva il valore; entrambi a 1 → comando non lecito (instabile).

## Esadecimale
D: Perché si usa l'esadecimale e come si converte da/verso il binario?
R: È una forma abbreviata per leggere sequenze di bit: ogni cifra esadecimale (0–9, A–F) corrisponde a 4 bit. Binario → hex: si divide in blocchi da 4 partendo da destra. Esempio: 10110101₂ = B5₁₆; 0xFF = 255.

## Memoria
D: Differenza tra memoria principale (RAM) e memoria di massa.
R: La RAM è volatile e ad accesso casuale (celle da 1 byte con indirizzo); la memoria di massa (HDD, ottici, SSD) è non volatile, più capiente e più lenta.

## Memoria
D: Cosa sono MSB, LSB e indirizzo di una cella?
R: MSB = bit più significativo (estrema sinistra), LSB = meno significativo (estrema destra). L'indirizzo è il numero univoco, a partire da 0, che identifica ogni cella di memoria.

## Dischi
D: Come è organizzato un HDD e come si misura il suo tempo di accesso?
R: Piatti con tracce concentriche divise in settori; le tracce alla stessa distanza formano un cilindro. Tempo di accesso = seek time (posizionamento della testina) + latency (rotazione fino al settore).

## SSD
D: Perché gli SSD usano il wear-leveling?
R: Ogni ciclo di scrittura/cancellazione degrada le celle flash. Il controller distribuisce le riscritture su blocchi diversi per uniformare l'usura e allungare la vita del disco.

## Testo
D: Come si rappresenta il testo in ASCII e in Unicode/UTF-8?
R: ASCII usa 7 bit (128 simboli), poi esteso a 8. Unicode assegna un codice a ogni simbolo con fino a 21 bit; in UTF-8 i caratteri ASCII occupano 1 byte, gli altri da 2 a 4 byte.

## Immagini
D: Quanti byte occupa un pixel RGB e quanti colori si ottengono? E la grafica vettoriale?
R: 3 byte (24 bit): 256 livelli per canale, oltre 16,7 milioni di colori. La grafica vettoriale descrive figure con equazioni, quindi si ridimensiona senza perdere nitidezza (a differenza della bitmap).

## Suono
D: Differenza tra campionamento audio e MIDI.
R: Il campionamento misura l'ampiezza a intervalli regolari (CD: 44.100 campioni/s a 16 bit per canale). Il MIDI memorizza invece le istruzioni per un sintetizzatore (strumento, nota, intensità, durata): file molto più piccolo.

## Binario
D: Come si converte un decimale in binario? Esempio con 13.
R: Divisioni successive per 2 leggendo i resti dal basso verso l'alto: 13 → 1101.

## Complemento a due
D: Come si ottiene l'opposto di un numero in complemento a due ("copia e complementa")? Qual è l'intervallo con n bit?
R: Da destra si copiano i bit fino al primo 1 compreso, poi si invertono tutti gli altri. Con n bit l'intervallo va da −2^(n−1) a 2^(n−1) − 1. Esempio a 4 bit: +6 = 0110 → −6 = 1010.

## Complemento a due
D: Come si rileva l'overflow nella somma in complemento a due?
R: Due positivi che danno risultato negativo, o due negativi che danno positivo. Positivo + negativo non può mai dare overflow. Es. a 4 bit: 5 + 4 = 0101 + 0100 = 1001 (−7).

## Virgola mobile
D: Com'è fatto il byte in virgola mobile del modello didattico?
R: 1 bit di segno, 3 bit di esponente in notazione eccesso-4, 4 bit di mantissa (punto radice a sinistra della mantissa). IEEE 754: singola precisione 32 bit (1+8+23, eccesso 127), doppia 64 bit (1+11+52, eccesso 1023).

## Virgola mobile
D: Perché l'addizione in virgola mobile non è associativa? Che regola ne deriva?
R: Sommando un numero molto grande a uno molto piccolo, il piccolo può essere troncato. Esempio: 2 1/2 + 1/8 + 1/8 dà 2 1/2 ma 1/8 + 1/8 = 1/4 e poi + 2 1/2 dà 2 3/4. Regola: sommare per primi i numeri più piccoli.

## Compressione
D: Differenza tra compressione lossless e lossy, con esempi.
R: Lossless: il dato decompresso è identico (testo, programmi). Lossy: si perde informazione non essenziale (immagini, audio, video: JPEG, MP3, MPEG).

## Compressione
D: Come funzionano RLE, Huffman e LZW?
R: - RLE: sostituisce sequenze ripetute con (valore, numero di ripetizioni).
- Huffman: codici a lunghezza variabile, più brevi per i simboli frequenti.
- LZW: dizionario adattivo costruito durante la codifica e ricostruito identico in decodifica.

## JPEG
D: Quali sono le fasi del JPEG baseline?
R: Sottocampionamento della crominanza (blocchi 2×2), DCT su blocchi 8×8, quantizzazione (valori sotto soglia a zero), poi RLE, codifica relativa e a lunghezza variabile. Rapporti 10:1 – 30:1.

## Errori
D: Come funziona il bit di parità e quali errori non rileva?
R: Si aggiunge un bit perché il numero di 1 sia pari (parità pari) o dispari. Rileva errori su un numero dispari di bit, ma non un numero pari di errori simultanei.

## Errori
D: Cos'è la distanza di Hamming e come permette di correggere gli errori?
R: Il numero di posizioni in cui due stringhe di pari lunghezza differiscono. Con distanza minima 3 tra parole legali si rilevano 2 errori e se ne corregge 1; con distanza minima 5 se ne rilevano 4 e se ne correggono 2.
