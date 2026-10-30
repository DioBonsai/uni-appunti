# 35. Le Mosse di Gauss e il Significato Geometrico del Determinante
## Tre operazioni che si possono fare su righe e colonne
Dopo lo sviluppo di Laplace e la regola per i fattori comuni (cap. 33 e 34), la Lezione 10 (Matrici III) raccoglie le proprietà che dicono **come cambia il determinante quando si modifica la matrice**. Sia A una matrice n × n.

1. Se A′ si ottiene da A **scambiando due righe** (o due colonne), allora det A′ = −det A.
2. Se A′ si ottiene da A **moltiplicando una riga** (o una colonna) **per un numero λ**, allora det A′ = λ · det A.
3. Se A′ si ottiene da A **aggiungendo a una riga** (o a una colonna) **il multiplo di un'altra**, allora det A′ = det A.

Queste tre trasformazioni si chiamano **mosse di Gauss**. Sulle colonne si scrivono così: C_{i} ↔ C_{j} (scambio), C_{i} → λC_{i} (moltiplicazione) e C_{i} → C_{i} + λC_{j} con j ≠ i (somma di un multiplo); qui C_{i} è la i-esima colonna, da non confondere con la sottomatrice C_{ij} dello sviluppo di Laplace.

**In parole povere:** lo scambio cambia il segno, la moltiplicazione di una riga per λ moltiplica il determinante per λ, e aggiungere a una riga un multiplo di un'altra **non cambia niente**.

Il perché si vede così: la (1) segue dallo sviluppo di Laplace lungo una riga non scambiata; la (2) è la proprietà già vista (cap. 34); per la (3), il termine che si aggiunge è il determinante di una matrice con due righe uguali, che vale 0. Le regole per le colonne seguono da det(ᵗA) = det A (cap. 32).

La terza mossa è la più utile, perché **può introdurre degli zeri**: lo si sfrutta per ridurre un determinante a uno più piccolo.

## Un esempio con le mosse di Gauss
Sia A = ( 1 3 7 ; 1 5 5 ; 1 4 10 ). Si vogliono far comparire degli zeri nella prima riga. Si sostituisce C_{2} con C_{2} − 3C_{1} e C_{3} con C_{3} − 7C_{1}, mosse che non cambiano il determinante:
det A = det( 1 0 7 ; 1 2 5 ; 1 1 10 ) = det( 1 0 0 ; 1 2 −2 ; 1 1 3 ).
Sviluppando lungo la prima riga, che ha due zeri, resta solo l'elemento 1 (segno +):
det A = 1 · det( 2 −2 ; 1 3 ) = 6 − (−2) = **8**.
(Controllo con lo sviluppo lungo la prima riga: 1·(50 − 20) − 3·(10 − 5) + 7·(4 − 5) = 30 − 15 − 7 = 8.)

Se invece una mossa produce una **colonna di zeri**, il determinante è 0: per A = ( 1 3 7 ; 1 3 5 ; 1 3 10 ), la mossa C_{2} → C_{2} − 3C_{1} dà una colonna nulla e quindi det A = 0.

## Determinante nullo e dipendenza lineare
**Proposizione.** Una matrice quadrata A ha det A = 0 se e solo se **una sua riga (o colonna) è combinazione lineare delle altre**, cioè se le righe (o, equivalentemente, le colonne) sono linearmente dipendenti.

**Spiegazione.** Se, per esempio, la prima riga è A_{1} = c_{2}A_{2} + … + c_{n}A_{n}, si parte dalla matrice A′ con la prima riga nulla, che ha determinante 0. Aggiungendo alla prima riga prima c_{2}A_{2}, poi c_{3}A_{3} e così via con la terza mossa, il determinante non cambia e alla fine si ottiene proprio A: quindi det A = 0. Il viceversa (det A = 0 implica che una riga è combinazione lineare delle altre) è affermato dalla proposizione, ma qui non è dimostrato.

**In parole povere:** se una riga si può ottenere dalle altre, la matrice «perde una dimensione» e il determinante crolla a zero; se tutte le righe sono davvero indipendenti, il determinante è diverso da zero.

Per esempio, per A = ( 1 2 3 ; 4 5 6 ; 7 8 9 ) si sottrae la prima riga dalla seconda e dalla terza, ottenendo ( 1 2 3 ; 3 3 3 ; 6 6 6 ); poi si sottrae due volte la seconda riga dalla terza, ottenendo la riga nulla ( 0 0 0 ). Quindi det A = 0: la terza riga è combinazione lineare delle prime due.

## Interpretazione geometrica
Il determinante ha anche un significato geometrico.

**In R².** Sia A = (A¹ | A²) una matrice 2 × 2, con colonne A¹, A² ∈ R². I due vettori (disegnati dall'origine) sono i lati di un **parallelogramma** P, e
**Area(P) = |det A|.**

**In R³.** Sia A = (A¹ | A² | A³) una matrice 3 × 3, con colonne in R³. I tre vettori sono gli spigoli di un **parallelepipedo** P, e
**|det A| = Vol(P).**

**In parole povere:** il valore assoluto del determinante misura «quanto spazio» occupano i vettori colonna: un'area in due dimensioni, un volume in tre. Se i vettori sono dipendenti (stanno sullo stesso piano o sulla stessa retta) l'area o il volume è 0, e infatti il determinante è 0: è lo stesso fatto del paragrafo precedente.

Un esempio mostra la terza mossa: per A = ( 1 1 ; 0 2 ), con colonne A¹ = (1, 0) e A² = (1, 2), la mossa C_{2} → C_{2} + C_{1} dà ( 1 2 ; 0 2 ), con colonne (1, 0) e (2, 2). I due parallelogrammi P₁ e P₂ hanno la stessa base (A¹) e la stessa altezza, quindi la stessa area, e infatti det( 1 1 ; 0 2 ) = det( 1 2 ; 0 2 ) = 2: la terza mossa «inclina» il parallelogramma senza cambiarne l'area.

Il capitolo seguente usa il determinante per decidere se una matrice è invertibile e per calcolarne l'inversa.
