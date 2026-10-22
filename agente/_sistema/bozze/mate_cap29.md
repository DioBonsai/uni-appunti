# 29. Proprietà dei Coefficienti Binomiali: Casi Banali e Simmetria
## Due modi di dimostrare una proprietà
Un coefficiente binomiale (n su k), cioè il numero di sottoinsiemi di k elementi di un insieme di n elementi (combinazioni semplici di ordine k su n), ha una definizione esplicita: (n su k) = n!/(k!(n − k)!). Di questi numeri si vogliono stabilire alcune proprietà, che si possono dimostrare in due modi.

Il primo è lavorare con l'**espressione** con i fattoriali e arrivare al risultato con un calcolo. È un modo corretto, ma, come sottolineato a lezione, è un metodo che dà la risposta ma non spiega nulla: come ha detto il docente, è una cosa da intelligenza artificiale, che risolve i problemi senza spiegare come li fa. Il secondo modo è dare una **spiegazione combinatoria**, cioè interpretare i due lati dell'uguaglianza come numeri di sottoinsiemi: così si capisce *perché* la relazione vale. Nel capitolo si usano entrambi.

## I casi banali
**Proprietà 1.** Per ogni n ≥ 0 vale (n su 0) = (n su n) = 1, e per n ≥ 1 vale (n su 1) = n.

Con la formula: (n su 0) = n!/(0! · (n − 0)!) = 1, perché 0! = 1 e n! si semplifica con (n − 0)! = n!; e (n su n) = n!/(n! · 0!) = 1. Per k = 1: (n su 1) = n!/(1! · (n − 1)!) e, scrivendo n! = n · (n − 1)!, il fattoriale (n − 1)! si cancella e resta n.

Con l'interpretazione: (n su 0) conta i sottoinsiemi di zero elementi, e l'unico è l'insieme vuoto, quindi la risposta è 1. (n su n) conta i sottoinsiemi di n elementi di un insieme di n elementi: l'unico modo è prenderli tutti, quindi 1. (n su 1) conta i sottoinsiemi di un solo elemento: basta prendere un elemento qualunque, e si può fare in n modi.

(In parole povere: scegliere zero oggetti si può fare in un solo modo, quello di non prendere niente; scegliere tutti gli oggetti pure; scegliere un oggetto solo si può fare in tanti modi quanti sono gli oggetti.)

## La simmetria
**Proprietà 2 (simmetria).** (n su k) = (n su n − k).

(In parole povere: scegliere k oggetti da tenere è la stessa cosa che scegliere gli n − k oggetti da lasciare: le possibilità sono tante in entrambi i casi.)

**Dimostrazione con la formula.** (n su n − k) = n!/((n − k)! · (n − (n − k))!) = n!/((n − k)! · k!), che è il coefficiente (n su k) con i due fattori del denominatore scambiati: il prodotto non cambia, quindi i due numeri sono uguali.

**Dimostrazione combinatoria.** Sia A un insieme con |A| = n. Si considerano due insiemi di sottoinsiemi di A:
- A_{k} = { S ⊆ A | |S| = k }, che ha (n su k) elementi;
- A_{n−k} = { T ⊆ A | |T| = n − k }, che ha (n su n − k) elementi.

Per esempio, con un insieme di 12 elementi, da una parte ci sono i sottoinsiemi di 5 elementi e dall'altra quelli di 7. La formula dice che sono altrettanti. Come si controlla che due insiemi finiti hanno lo stesso numero di elementi? Basta trovare una **funzione biettiva** (iniettiva e suriettiva) tra i due: a ogni elemento del primo ne corrisponde esattamente uno del secondo, quindi i due insiemi hanno lo stesso numero di elementi.

La funzione naturale è F: A_{k} → A_{n−k} che a ogni S associa il suo **complementare** in A, F(S) = C_{A}(S) = A ∖ S: se S ha k elementi, il complementare ne ha n − k.

Per dimostrare che F è biettiva si può verificare direttamente iniettività e suriettività, ma c'è una scorciatoia: abbiamo dimostrato che una funzione è biettiva se e solo se è invertibile (cap. 20). Basta quindi **trovare un'inversa**. Si prova con un candidato, come ha fatto il docente: G: A_{n−k} → A_{k}, con G(T) = C_{A}(T). Il complementare del complementare è l'insieme di partenza, quindi:
- (G ∘ F)(S) = G(C_{A}(S)) = C_{A}(C_{A}(S)) = S;
- (F ∘ G)(T) = F(C_{A}(T)) = C_{A}(C_{A}(T)) = T.

Le due composizioni sono entrambe l'identità, quindi G = F⁻¹ e F è biettiva. Ne segue che A_{k} e A_{n−k} hanno lo stesso numero di elementi: (n su k) = (n su n − k). Come sottolineato a lezione, la funzione G sembra uguale a F perché ha la stessa espressione, ma è una funzione **diversa**: dominio e codominio sono scambiati. Una funzione non è solo la sua espressione.

## A cosa serve
La simmetria permette di calcolare solo circa metà dei coefficienti: per un n fissato basta calcolare (n su k) per k da 0 fino alla metà di n, perché gli altri valori sono gli stessi. Per esempio, per calcolare (32 su 26) basta osservare che è uguale a (32 su 6); dopo aver calcolato (32 su 0), (32 su 1), …, (32 su 16), tutti gli altri valori sono già noti.

Il capitolo successivo presenta una proprietà più interessante, che lega i coefficienti con n e con n − 1.
