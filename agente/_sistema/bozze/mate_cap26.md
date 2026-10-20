# 26. Le Combinazioni Semplici e i Coefficienti Binomiali
## Contare i sottoinsiemi di k elementi
Nel capitolo 24 le scelte avevano un ordine. Qui l'ordine non conta, e il modello matematico è un **sottoinsieme**. Sia A un insieme con n elementi e fissiamo un numero k con 0 ≤ k ≤ n. Una **combinazione semplice** di ordine k in A è la scelta di un sottoinsieme S ⊆ A con |S| = k. Il numero di queste scelte si indica con C_{n,k}, e quindi C_{n,k} = |{ S ⊆ A : |S| = k }|. Il problema è calcolare questo numero.

(In parole povere: una combinazione è una scelta "a mucchio", in cui interessa solo chi è stato scelto e non l'ordine in cui lo si è preso. Scegliere tre amici per una partita è lo stesso che scegliere gli stessi tre in un altro ordine.)

Conviene fare delle osservazioni preliminari, con n fissato e k variabile fra 0 e n. Ci sono due casi estremi, che sono chiari. Con k = 0 si vuole un sottoinsieme senza elementi: ce n'è uno solo, l'insieme vuoto, perché non si fa nessuna scelta; quindi C_{n,0} = 1. Con k = n bisogna prendere tutti gli elementi e c'è un solo modo di farlo; quindi C_{n,n} = 1. Il caso generale richiede un'idea in più.

## L'idea: dalle disposizioni alle combinazioni
Dal punto di vista pratico, come si sceglie un sottoinsieme di tre oggetti? Se ne sceglie uno, poi un secondo, poi un terzo. Sebbene alla fine l'ordine non interessi, scegliendo un elemento alla volta si sta facendo una **disposizione semplice**: si estraggono k elementi da n in un certo ordine. Di disposizioni semplici ce ne sono D_{n,k} = n!/(n − k)!, come si è visto nel capitolo 24.

Il punto è che si vuole poi **dimenticare l'ordine** con cui gli elementi sono stati scelti. Si prenda un insieme di sei elementi a, b, c, d, e, f e si scelgano nell'ordine c, e, f. Il sottoinsieme ottenuto è S = {c, e, f}, ma si otterrebbe lo stesso con le scelte e, c, f oppure f, c, e, e così via: ogni modo di scrivere gli stessi tre elementi in un altro ordine è una disposizione diversa che dà lo stesso insieme. Le scritture diverse sono tante quanti gli ordinamenti di tre elementi, cioè 3! = 6.

![Le 6 disposizioni (c, e, f), (c, f, e), …, (f, e, c) danno tutte la stessa combinazione S = {c, e, f}.](figure/mate/ch26_riordinamenti.png|12)

Nel caso generale una disposizione è una funzione iniettiva da I_{k} = {1, …, k} in A, che a 1 associa a_{1}, a 2 associa a_{2}, e così via fino a k, che ha come immagine a_{k}; il sottoinsieme che si ottiene è S = {a_{1}, …, a_{k}}. Riordinare questi k elementi si può fare in k! modi, quindi **ci sono esattamente k! disposizioni semplici che danno lo stesso sottoinsieme**.

Ne segue che ogni combinazione si ottiene da k! disposizioni diverse, e quindi il numero delle combinazioni è il numero delle disposizioni diviso k!:

C_{n,k} = (1/k!) · D_{n,k} = n! / (k! (n − k)!).

(In parole povere: si fa finta, per un momento, che l'ordine conti, e si contano tutte le scelte ordinate. Poi si corregge: ogni gruppo di k persone è stato contato k! volte, una per ogni modo di metterle in fila, e quindi si divide per k!.)

## I coefficienti binomiali
I numeri n!/(k!(n − k)!) sono molto importanti perché capitano spesso in diversi settori della matematica. Per questo hanno un simbolo e un nome particolari: si scrivono con n sopra k fra parentesi tonde, **senza barra di frazione**, e si leggono «n su k». Si chiamano **coefficienti binomiali**, e perché si chiamino così si scoprirà fra non molto. Quindi

C_{n,k} = (n su k) = n! / (k! (n − k)!).

(In parole povere: "n su k" è semplicemente il numero di modi di scegliere k oggetti da un mucchio di n quando l'ordine non conta. Si legge come "n su k" e non è una divisione, anche se per calcolarlo si usano i fattoriali.)

I due casi estremi tornano dalla formula, ed è qui che la convenzione 0! = 1 è utile. Per k = 0 si ha (n su 0) = n!/(0! · n!) = 1, e per k = n si ha (n su n) = n!/(n! · 0!) = 1. Nella formula con k = 0 si dovrebbe scrivere prima 0! e poi (n − 0)!, ma poiché si stanno moltiplicando dei numeri l'ordine dei fattori non cambia il risultato.

## Calcolare i coefficienti
Quanti modi ci sono di scegliere tre oggetti fra sei? La risposta è (6 su 3):

(6 su 3) = 6! / (3! · 3!) = (6 · 5 · 4 · 3 · 2 · 1) / ((3 · 2 · 1) · (3 · 2 · 1)).

Questi numeri sono molto più semplici da calcolare di quanto sembri, perché si semplificano quasi sempre molti fattori. Il 3 · 2 · 1 del numeratore si cancella con uno dei due fattoriali del denominatore, rimane (6 · 5 · 4)/(3 · 2 · 1) e, poiché 3 · 2 = 6, si cancella anche il 6: restano 5 · 4 = 20. Conviene **semplificare prima e usare la calcolatrice solo alla fine**. Se si scrive la lista di tutti i sottoinsiemi di tre elementi di {a, b, c, d, e, f}, in ordine alfabetico da {a, b, c} a {d, e, f}, si contano in effetti 20 sottoinsiemi.

Una conferma per un caso semplice: scegliere un solo elemento fra n dà n possibilità, e in effetti (n su 1) = n!/(1! (n − 1)!) = n. Per esempio (15 su 1) = 15.

## Il superenalotto
Un esempio concreto è il superenalotto. Si estraggono 6 numeri da 1 a 90 e per vincere bisogna indovinare i sei che escono, non l'ordine di uscita. Per sapere quante sestine possono uscire bisogna contare i sottoinsiemi di 6 elementi di I_{90} = {1, …, 90}: è una combinazione semplice, e quindi il numero delle sestine è

C_{90,6} = 90! / (6! · 84!) = (90 · 89 · 88 · 87 · 86 · 85) / 720.

Il 90! si semplifica con 84! lasciando solo i primi sei fattori, e poi si divide per 6! = 720. Il risultato è circa **622 milioni** (622 614 630). Sono tutte sestine ugualmente possibili, e quindi, giocandone una sola, si ha una possibilità su circa 622 milioni di vincere (senza entrare nel discorso della probabilità).

## Riassumendo
I casi di scelte che si sono visti finora si possono classificare con due domande: l'ordine conta? Le scelte si possono ripetere? Le **disposizioni** (con ripetizione: n^{k}; semplici: n!/(n − k)!) sono ordinate; le **combinazioni semplici**, che si sono viste in questo capitolo, non lo sono e non ammettono ripetizioni, e il loro numero è il coefficiente binomiale (n su k). Resta da vedere il caso delle combinazioni con ripetizione. Prima, il capitolo successivo mostra come si usano le combinazioni nei problemi in cui le scelte sono più di una.
