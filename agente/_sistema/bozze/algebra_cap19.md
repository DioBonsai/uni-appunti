# 19. Le Matrici e lo Spazio M(m, n, 𝕂)
## Un nuovo esempio fondamentale
Dopo aver visto gli spazi vettoriali e i primi esempi (ℝ^{n}, i polinomi, le funzioni), si introduce un altro esempio molto importante: lo **spazio delle matrici**. Come sottolineato a lezione, da qui in poi le matrici compaiono in quasi tutte le lezioni del corso, quindi vale la pena impararle bene fin dall'inizio.

Come sempre bisogna fissare prima il campo degli scalari: sia 𝕂 un campo fissato. Chi trova astratta questa frase può pensare che 𝕂 sia ℝ oppure ℂ: nel 99% degli esempi e delle applicazioni è così. Esistono moltissimi altri campi, ma la teoria funziona allo stesso modo per tutti, e i matematici la scrivono in generale proprio per questo.

## Che cos'è una matrice
**Definizione.** Una **matrice** m × n a coefficienti in 𝕂 (si legge «m per n») è una tabella rettangolare con m righe e n colonne
A = ( a_{11} a_{12} … a_{1n} ; a_{21} a_{22} … a_{2n} ; … ; a_{m1} a_{m2} … a_{mn} ),
in cui ogni a_{ij} è un elemento di 𝕂 (qui le righe sono separate da punto e virgola). Gli a_{ij} si chiamano **coefficienti**, **entrate** o **termini** della matrice.

**In parole povere:** una matrice è una tabella di numeri, con righe in orizzontale e colonne in verticale. Dire che è «m per n» significa che ha m righe e n colonne. Ogni numero ha un indirizzo, dato da due indici: la riga in cui sta e la colonna in cui sta.

![Una matrice m × n: l'entrata a_{ij} sta nella i-esima riga e nella j-esima colonna.](figure/alg/matrice_indici.png|10)

Gli indici si leggono sempre nello stesso ordine: **prima la riga, poi la colonna**. L'entrata a_{ij} è quella nella i-esima riga e nella j-esima colonna, con i da 1 a m e j da 1 a n. Sembra un dettaglio, ma è importantissimo: in Excel, per esempio, una casella si chiama C2, cioè prima la colonna (la lettera) e poi la riga (il numero), mentre in matematica è esattamente il contrario. Tutti i matematici, in ogni libro e in ogni articolo, usano questa convenzione, e invertire l'ordine è un errore tipico da esame.

Le **righe** di A si indicano con A_{1}, …, A_{m} e le **colonne** con A^{1}, …, A^{n}; per esempio A_{i} = (a_{i1}, a_{i2}, …, a_{in}) è la i-esima riga.

L'insieme di tutte le matrici m × n a coefficienti in 𝕂 si indica con **M(m, n, 𝕂)**, o semplicemente M(m, n) quando il campo è chiaro.

**In parole povere:** M(m, n, 𝕂) è la scatola che contiene tutte le tabelle di m righe e n colonne con numeri presi da 𝕂.

## Qualche esempio
- ( 2 , π , 1 ; √2 , −1 , 0 ) è una matrice 2 × 3 a coefficienti reali: ha due righe e tre colonne, e a_{12} = π.
- ( 3+i , π ; i , √2+1 ; 1 , √5 ) è una matrice 3 × 2 a coefficienti in ℂ.
- Una matrice con **una sola riga** è una matrice 1 × n, per esempio (1, 7, −2). Quando le entrate sono vicine conviene scriverle con una virgola per non confondere 1, 7, −2 con il numero 17 e il segno meno.
- Una matrice con **una sola colonna** è una matrice m × 1. Ma allora è semplicemente un vettore colonna: M(m, 1, 𝕂) si identifica con 𝕂^{m}. Per esempio una matrice 3 × 1 è un elemento di ℝ³, e una matrice 4 × 1 è un elemento di ℝ⁴. Si può quindi pensare ai vettori di 𝕂^{m} come a particolari matrici, ed è molto comodo farlo.

Una nota di precisione: formalmente una colonna di numeri e un elemento di 𝕂^{m} sono oggetti distinti, ma si possono identificare senza rischio. Conviene farlo proprio perché permette di pensare sempre ai vettori di 𝕂^{m} come a vettori colonna.

## Somma e prodotto per scalare
Per fare di M(m, n, 𝕂) uno spazio vettoriale bisogna dire come si sommano due matrici e come si moltiplica una matrice per uno scalare. Si fa **entrata per entrata**: per A = (a_{ij}) e B = (b_{ij}) dello stesso tipo e per λ ∈ 𝕂,
(A + B)_{ij} = a_{ij} + b_{ij}   e   (λA)_{ij} = λ·a_{ij}.

**In parole povere:** per sommare due matrici si sommano i numeri che stanno nello stesso posto; per moltiplicarle per un numero si moltiplica ogni entrata per quel numero. È come lavorare con due tabelle sovrapposte, casella per casella.

Esempi in M(3, 2, ℝ), con le righe separate da punto e virgola:
- ( 2 3 ; 1 1 ; 0 5 ) + ( −1 1 ; 0 1 ; 1 4 ) = ( 1 4 ; 1 2 ; 1 9 ): in ogni posto si sommano le due entrate (per esempio, nella prima riga, 2 + (−1) = 1 e 3 + 1 = 4);
- −2 · ( 1 2 ; 3 4 ; 5 6 ) = ( −2 −4 ; −6 −8 ; −10 −12 ): ogni entrata si moltiplica per −2.

Si possono sommare solo due matrici **della stessa taglia**, cioè con lo stesso numero di righe e lo stesso numero di colonne: non ha senso sommare una matrice 3 × 2 e una 7 × 9. Qualcuno potrebbe pensare di completare con degli zeri la più piccola, ma è un'idea che non è utile e non si usa.

## M(m, n, 𝕂) è uno spazio vettoriale
Con queste due operazioni **M(m, n, 𝕂) è uno spazio vettoriale su 𝕂**: le proprietà della somma e del prodotto per scalare (commutativa, associativa, distributive, ecc.) si controllano facilmente perché le operazioni si fanno entrata per entrata, e in ogni singola entrata sono quelle dei numeri di 𝕂.

- Il **vettore nullo** (la matrice «zero») è la matrice con tutte le entrate uguali a 0; si ottiene anche come 0·A per una matrice A qualunque.
- L'**opposto** di una matrice A è la matrice −A = (−1)·A, con tutte le entrate cambiate di segno.

Quindi una matrice è un **vettore** nel senso del capitolo 17: un elemento di uno spazio vettoriale. Come sottolineato a lezione, la parola «vettore» non va associata solo alle frecce o alle colonne di numeri: è un elemento di un qualunque spazio vettoriale, e può essere una matrice, una funzione, un polinomio, o semplicemente un numero.

Il capitolo successivo parte da qui per chiedersi quali pezzi di uno spazio vettoriale sono a loro volta spazi: i sottospazi.
