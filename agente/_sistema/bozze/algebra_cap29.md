# 29. Il Prodotto fra Matrici
## Quando si possono moltiplicare due matrici
Le matrici si possono anche moltiplicare fra loro. Si prendono una matrice A ∈ M(m, n, 𝕂), con m righe e n colonne, e una matrice B ∈ M(n, p, 𝕂) a coefficienti nello stesso campo. L'unica condizione che interessa è che **il numero di colonne di A sia uguale al numero di righe di B**: entrambi valgono n.

**Definizione.** Il **prodotto** AB è la matrice di M(m, p, 𝕂), cioè con lo stesso numero di righe di A e lo stesso numero di colonne di B, la cui entrata in riga i (1 ≤ i ≤ m) e colonna j (1 ≤ j ≤ p) è
(AB)_{ij} = A_{i1}B_{1j} + A_{i2}B_{2j} + … + A_{in}B_{nj} = Σ_{k=1}^{n} A_{ik}B_{kj}.

**In parole povere:** per ottenere l'entrata (i, j) si prende la riga i di A e la colonna j di B, che hanno lo stesso numero di entrate, si moltiplicano a due a due le entrate nella stessa posizione (prima con prima, seconda con seconda, …) e si sommano i prodotti.

Come sottolineato a lezione, il simbolo di sommatoria non è altro che il ciclo `for` dell'informatica: si sommano gli n termini al variare di k da 1 a n. Il prodotto si chiama anche **prodotto riga per colonna**, perché l'entrata (i, j) si ottiene dalla riga i di A e dalla colonna j di B.

## Quando il prodotto non esiste
Siano A = ( 3 1 1 ; 2 0 5 ) ∈ M(2, 3) e B = ( 1 2 ; −1 0 ) ∈ M(2, 2). Il prodotto AB **non si può fare**, perché A ha 3 colonne e B ha 2 righe, e 3 ≠ 2: il prodotto non è ben definito. Come sottolineato a lezione, per fare un prodotto serve che il numero di colonne della prima matrice sia uguale al numero di righe della seconda.

## Un esempio svolto
Sia C = ( 2 −1 ; 1 1 ; 0 1 ) ∈ M(3, 2). Ora AC si può fare, perché le colonne di A sono 3 e le righe di C sono 3, e il risultato è una matrice con 2 righe (quante ne ha A) e 2 colonne (quante ne ha C):
AC = ( 3 1 1 ; 2 0 5 ) · ( 2 −1 ; 1 1 ; 0 1 ).

Si calcola un'entrata alla volta. Il primo indice dell'entrata indica la riga di A da usare, il secondo la colonna di C:
- entrata (1, 1): riga 1 di A per colonna 1 di C: 3·2 + 1·1 + 1·0 = 6 + 1 + 0 = 7;
- entrata (1, 2): riga 1 di A per colonna 2 di C: 3·(−1) + 1·1 + 1·1 = −3 + 1 + 1 = −1;
- entrata (2, 1): riga 2 di A per colonna 1 di C: 2·2 + 0·1 + 5·0 = 4 + 0 + 0 = 4;
- entrata (2, 2): riga 2 di A per colonna 2 di C: 2·(−1) + 0·1 + 5·1 = −2 + 0 + 5 = 3.

Quindi AC = ( 7 −1 ; 4 3 ).

![Il prodotto riga per colonna: l'entrata (1, 1) di AC si ottiene dalla riga 1 di A e dalla colonna 1 di C, con 3·2 + 1·1 + 1·0 = 7.](figure/alg/prodotto_riga_colonna.png|12)

Un modo comodo per non sbagliare le righe e le colonne: si scrive A a sinistra, la seconda matrice C in alto a destra e il prodotto sotto C e a destra di A, come nella figura. Per ogni casella del prodotto si guarda la riga di A alla sua sinistra e la colonna di C sopra di essa. Come sottolineato a lezione, questi conti si faranno presto «nel sonno».

## Il prodotto matrice per vettore
Se A è m × n e x è una matrice n × 1, cioè un vettore colonna di 𝕂^{n}, il prodotto Ax è una matrice m × 1, cioè un vettore colonna di 𝕂^{m}. Per esempio ( 1 2 ; −1 1 ; 0 3 ) · ( 1 ; −1 ) = ( 1·1 + 2·(−1) ; −1·1 + 1·(−1) ; 0·1 + 3·(−1) ) = ( −1 ; −2 ; −3 ).

## Matrici 1 × 1 e numeri
Come sottolineato a lezione, quando una matrice è 1 × 1 è formata da una sola entrata e c'è poca differenza fra pensarla come matrice e come numero: le parentesi sono quasi l'unica differenza. Si può quindi identificare lo spazio delle matrici 1 × 1 con l'insieme dei numeri di 𝕂.

Il prodotto fra matrici ha proprietà simili a quello fra numeri, ma anche una differenza importante: il capitolo successivo le raccoglie, insieme alla traccia.
