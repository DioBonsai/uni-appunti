# 32. Il Determinante di Matrici Speciali: Triangolari, Identità e Trasposta
## Perché la definizione non basta
Per una matrice n × n la definizione del determinante è una somma su **n! permutazioni**. Con n = 2 ci sono 2 termini, con n = 3 ce ne sono 6, ma già con **n = 4** sono 24 (12 con segno + e 12 con segno −; come sottolineato a lezione, in generale metà delle permutazioni ha segno + e metà segno −) e con n = 5 sono 120. Per ogni termine bisogna anche decidere se il segno è + o −: è un lavoro enorme e non è il metodo con cui si calcola un determinante. Come sottolineato a lezione, il metodo più furbo arriva nel capitolo successivo; qui si guardano invece i casi in cui la definizione stessa dà subito il risultato.

## Le matrici triangolari
Una matrice è **triangolare superiore** se tutti gli elementi **sotto la diagonale principale sono zero**; gli elementi sulla diagonale e sopra possono essere qualsiasi. Si parla di matrice **triangolare inferiore** quando sono zero tutti quelli sopra la diagonale.

(In parole povere: una matrice triangolare ha tutti zeri da una parte della diagonale, a forma di triangolo.)

**Proposizione.** Se A è una matrice triangolare (superiore o inferiore), il suo determinante è il **prodotto degli elementi sulla diagonale principale**:
det A = a_{11} · a_{22} · … · a_{nn}.

**Spiegazione.** Nella formula del determinante ogni prodotto sceglie **un elemento in ogni riga e un elemento in ogni colonna**. Per una matrice triangolare superiore, quale elemento si può scegliere nella prima colonna senza ottenere un prodotto nullo? Solo quello in alto, a_{11}: tutti gli altri della prima colonna sono zeri. Nella seconda colonna ci sono due elementi non nulli possibili (a_{12} e a_{22}), ma la prima riga è già stata usata da a_{11}, quindi si deve scegliere a_{22}; e così via per tutte le colonne. Ogni altra permutazione prende almeno un elemento sotto la diagonale, cioè uno zero, e il suo termine vale 0. L'unico termine che sopravvive è quello della permutazione identità, che ha segno +1. Lo stesso ragionamento vale per le triangolari inferiori.

**In parole povere:** per le matrici triangolari il determinante si legge sulla diagonale: basta moltiplicare i numeri sulla diagonale principale, senza calcoli lunghi.

Come sottolineato a lezione, è una proposizione importante e **bisogna saperla**: all'esame di settembre si dovevano calcolare gli autovalori di una matrice 3 × 3 (un concetto che si vedrà più avanti), il che richiedeva un determinante, e quel determinante era quello di una matrice triangolare; uno studente l'ha scritto in una riga, moltiplicando gli elementi sulla diagonale, mentre tutti gli altri hanno fatto il calcolo per esteso.

Per esempio, per A = ( 2 5 1 ; 0 3 4 ; 0 0 −1 ) si ha det A = 2 · 3 · (−1) = −6.

## La matrice identità
La **matrice identità** di taglia n × n, indicata con I_{n}, è la matrice con **1 sulla diagonale principale e 0 altrove**. Poiché è triangolare (anzi, è diagonale), il suo determinante è il prodotto dei valori sulla diagonale: **det(I_{n}) = 1**.

(In parole povere: la matrice identità è la matrice «neutra» del prodotto, quella che ha tutti 1 sulla diagonale e zeri altrove.) Si è già incontrata nel calcolo del rango (cap. 28), dove le sue colonne sono i vettori della base canonica.

## La trasposta
**Proposizione.** Per ogni matrice quadrata A vale **det(ᵗA) = det A**.

**Spiegazione.** Trasporre una matrice significa scambiare il concetto di riga e di colonna. Nella formula del determinante c'è sempre un elemento di ogni riga e un elemento di ogni colonna: se si scambiano righe e colonne, le scelte possibili sono le stesse, solo lette «al contrario». Bisogna verificare soltanto che anche il **segno** non cambi, e non cambia: il termine della permutazione σ per ᵗA corrisponde, riordinando i fattori, a quello della permutazione inversa σ^{-1} per A (osservazione nostra), e σ e σ^{-1} hanno lo stesso segno: se σ è un prodotto di k trasposizioni, σ^{-1} è il prodotto delle stesse trasposizioni in ordine inverso, quindi ne servono ancora k. Dunque il determinante della trasposta è semplicemente il determinante della matrice di partenza: niente cambia.

**In parole povere:** il determinante non si accorge se la matrice viene «ribaltata» lungo la diagonale: righe e colonne hanno lo stesso ruolo.

Una conseguenza pratica è che **ogni proprietà del determinante dimostrata per le righe vale anche per le colonne**: lo si userà nel capitolo successivo per lo sviluppo lungo una colonna.
