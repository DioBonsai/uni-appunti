# 31. Il Determinante di una Matrice Quadrata
## Un nuovo numero associato a una matrice
Dopo la trasposta, il rango e la traccia, la lezione introduce un'altra quantità associata a una matrice, più complicata delle precedenti ma molto importante: il **determinante**. Come sottolineato a lezione, è un concetto che purtroppo è ancora più complicato di quelli visti finora, ma **tutti devono saperlo calcolare**. È definito **solo per le matrici quadrate**, cioè con lo stesso numero di righe e di colonne.

A cosa serve? Come sottolineato a lezione, il determinante servirà a decidere se una matrice è **invertibile** o no e a calcolare gli **autovalori** di una matrice (concetti che si vedranno più avanti nel corso). Per il momento è come la traccia: si definisce, si impara a calcolarlo, e il suo significato verrà dopo.

## La definizione
**Definizione.** Sia A una matrice quadrata n × n. Il **determinante** di A è il numero
det A = Σ_{σ ∈ S_{n}} sgn(σ) · a_{1σ(1)} · a_{2σ(2)} · … · a_{nσ(n)}.

Qui S_{n} indica l'insieme delle **permutazioni** di {1, …, n}, e sgn(σ) = ±1 è il **segno** della permutazione σ. Ricordando che il primo indice di a_{ij} è la riga e il secondo la colonna, ogni termine della somma è un prodotto che sceglie **un elemento in ogni riga**: dalla riga 1 l'elemento di colonna σ(1), dalla riga 2 quello di colonna σ(2), e così via. Come osserva anche la dispensa, la definizione non è facile da decifrare e si comprende meglio esaminando i casi piccoli.

**In parole povere:** il determinante è una somma di tanti prodotti. Ogni prodotto si forma scegliendo un numero per riga in modo che le colonne scelte siano tutte diverse; ogni prodotto si prende con il suo segno + o −, e poi si sommano tutti.

## Le permutazioni e il loro segno
Una **permutazione** dell'insieme {1, 2, …, n} è un **riordinamento** degli n numeri: si usano tutti, una volta sola, ma non necessariamente nell'ordine 1, 2, …, n. Per n = 4, per esempio, [4 1 3 2] è una permutazione. In termini più matematici è una funzione biettiva dall'insieme in sé stesso: biettiva vuol dire che non si dimentica nessun elemento (suriettiva) e nessun elemento compare due volte (iniettiva). Si indica la permutazione σ con il simbolo [σ(1) … σ(n)].

Le permutazioni di n elementi sono **n!** (n fattoriale): per il primo posto si hanno n scelte, per il secondo ne restano n − 1, per il terzo n − 2, e così via (cap. 23 di Matematica discreta).

Il **segno** di una permutazione è +1 o −1. Una **trasposizione** è una permutazione che **scambia due elementi** e lascia tutti gli altri invariati: per esempio con n = 7, [1 2 3 7 5 6 4] scambia 4 e 7. Ogni permutazione si può ottenere componendo trasposizioni; se σ è un prodotto di k trasposizioni, allora
sgn(σ) = (−1)^{k}.

Il numero di trasposizioni necessarie può essere scelto in più modi, ma ogni volta che si applica una trasposizione il segno cambia: quindi il segno non dipende dal modo scelto, ma solo dal fatto che il numero di trasposizioni sia pari (segno +1) o dispari (segno −1). L'identità, che non scambia niente, ha 0 trasposizioni e segno +1; due scambi consecutivi che si annullano danno ancora segno +1.

**In parole povere:** il segno dice se per rimettere in ordine la permutazione servono un numero pari o dispari di scambi. Per queste nozioni la lezione rimanda alla Matematica discreta, dove sono trattate in dettaglio.

## I casi piccoli
**n = 1.** La matrice è un solo numero, A = (a_{11}). L'insieme S_{1} contiene solo l'identità, che ha segno +1 (0 trasposizioni). Quindi **det A = a_{11}**.

**n = 2.** Con A = ( a_{11} a_{12} ; a_{21} a_{22} ), l'insieme S_{2} contiene due permutazioni: l'identità [1 2], che ha segno +, e la trasposizione [2 1], che ha segno −. Quindi
**det A = a_{11}a_{22} − a_{12}a_{21}.**
Come sottolineato a lezione, è il prodotto degli elementi sulla diagonale principale meno il prodotto degli elementi dell'altra diagonale, e per le matrici 2 × 2 lo si può sempre fare così.

**n = 3.** S_{3} ha sei permutazioni: [1 2 3], [1 3 2], [3 2 1], [2 1 3], [2 3 1], [3 1 2]. Le tre trasposizioni [1 3 2], [3 2 1] e [2 1 3] hanno segno −1; le altre tre (l'identità e due permutazioni che richiedono due scambi) hanno segno +1. Quindi
det A = a_{11}a_{22}a_{33} − a_{11}a_{23}a_{32} − a_{13}a_{22}a_{31} − a_{12}a_{21}a_{33} + a_{12}a_{23}a_{31} + a_{13}a_{21}a_{32}.

![Tre dei sei termini del determinante 3 × 3: ogni termine sceglie un elemento in ogni riga e in ogni colonna, con il segno della permutazione.](figure/alg/det_permutazioni.png|14)

## Esempi
Il determinante di (3) è 3. Per la matrice 2 × 2 ( 1 2 ; −1 4 ) vale 4 − (−2) = 6. Per la matrice 3 × 3 ( 1 2 1 ; 2 1 2 ; −1 0 1 ) si applica la formula dei sei termini:
1·1·1 − 1·2·0 − 1·1·(−1) − 2·2·1 + 2·2·(−1) + 1·2·0 = 1 − 0 + 1 − 4 − 4 + 0 = −6.

Come sottolineato a lezione, la definizione è la «definizione formale» del determinante, ma **in pratica non si usa mai** per calcolarlo: il capitolo seguente spiega perché e introduce metodi molto più veloci.
