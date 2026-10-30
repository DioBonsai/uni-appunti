# 34. Proprietà del Determinante e Calcolo Intelligente
## Una riga o una colonna nulla
**Proposizione.** Se gli elementi di una riga (o di una colonna) di A sono tutti nulli, allora det A = 0.

**Dimostrazione.** È una conseguenza diretta dello sviluppo di Laplace: si sviluppa lungo la riga (o colonna) tutta nulla, e ogni termine contiene un elemento a_{ij} = 0, quindi la somma è 0 + 0 + … + 0 = 0. ∎

## Moltiplicare una riga o una colonna per un numero
**Proposizione.** Se la matrice A′ si ottiene da A moltiplicando **tutti gli elementi di una riga (o colonna) per il numero c**, allora det(A′) = c · det(A).

**Spiegazione.** Si sviluppa il determinante di A′ lungo proprio quella riga. Gli unici elementi che cambiano sono quelli della riga scelta, che diventano c volte più grandi; le sottomatrici C_{ij} che si ottengono cancellando quella riga **non cambiano**, perché la riga modificata è esattamente quella che si cancella. Quindi ogni termine della somma risulta moltiplicato per c, e c si può mettere in evidenza: il determinante è moltiplicato per c.

Un esempio: se una matrice ha determinante −6 e si moltiplica la seconda riga per 3, tenendo uguale il resto, il nuovo determinante vale −18.

**In parole povere:** se si «allarga» una sola riga (o colonna) di un fattore c, il determinante si allarga dello stesso fattore c; viceversa, un fattore comune a tutti gli elementi di una riga (o colonna) si può portare fuori dal determinante.

## Moltiplicare tutta la matrice
Che cosa succede a det(cA), cioè se si moltiplica **ogni** elemento della matrice per c? Si moltiplica una riga alla volta: ogni riga moltiplicata per c produce un fattore c, e le righe sono n, quindi si ottiene un fattore c^{n}.

**Corollario.** det(cA) = c^{n} · det(A), e in particolare **det(−A) = (−1)^{n} · det(A)**.

Come sottolineato a lezione, per una matrice 2 × 2 le matrici A e −A hanno lo stesso determinante, mentre per una matrice 3 × 3 i determinanti di A e −A sono opposti (n è dispari).

## Come scegliere il metodo di calcolo
Come sottolineato a lezione, quando si calcola un determinante bisogna **guardare la matrice** e scegliere bene come procedere, perché tra un terzo e metà degli studenti sceglie lo sviluppo lungo la prima riga senza guardare la matrice: si arriva al risultato con molta fatica, e se non si sbaglia è giusto, ma il rischio di errori di calcolo è alto. In ordine, dal peggiore al migliore:
1. il metodo peggiore è scrivere tutte le permutazioni, con i segni, e usare la definizione (per una matrice 4 × 4 sono 24 termini);
2. il secondo peggiore è sviluppare per forza lungo la prima riga, senza guardare la matrice;
3. il metodo migliore è **scegliere la riga o la colonna con più zeri**, oppure **semplificare** la matrice portando fuori fattori comuni, e poi sviluppare lungo quella riga o colonna.

Come detto a lezione, negli esami compaiono spesso matrici triangolari o con molti zeri: i docenti «provano a farlo semplice».

## Esercizio 9.13
Si calcola il determinante di
A = ( 2+i 0 −5 0 ; 3−i 1 2i 0 ; 4+4i −2 −1 0 ; −1/2 i 1−i i ).

L'ultima colonna ha **tre zeri**: conviene svilupparla lungo di essa. L'unico elemento non nullo è a_{44} = i, in posizione (4, 4) (4 + 4 = 8 pari, segno +), quindi
det A = i · det( 2+i 0 −5 ; 3−i 1 2i ; 4+4i −2 −1 ).
Il determinante 3 × 3 si calcola sviluppando lungo la prima riga:
(2+i)·(1·(−1) − 2i·(−2)) − 0 + (−5)·((3−i)·(−2) − 1·(4+4i)) = (2+i)(−1+4i) − 5(−10−2i) = (−6+7i) + (50+10i) = 44 + 17i.
Quindi det A = i · (44 + 17i) = 44i + 17i² = **−17 + 44i**.

## Esercizio 9.14
Si calcola il determinante di
B = ( 5i 4√2 0 √2 ; 5i 8√2 0 −√2 ; −5i −4√2 −1 2√2 ; −10i 4√2 1 √2 ).

Gli elementi sono scomodi (compaiono i e √2), ma alcune colonne hanno **fattori comuni**: la prima colonna è 5i · (1, 1, −1, −2), la seconda è 4√2 · (1, 2, −1, 1) e la quarta è √2 · (1, −1, 2, 1). Portando fuori questi fattori si ottiene
det B = 5i · 4√2 · √2 · det D = 40i · det D,
dove D è la matrice con colonne (1, 1, −1, −2), (1, 2, −1, 1), (0, 0, −1, 1) e (1, −1, 2, 1), cioè la matrice di soli interi
D = ( 1 1 0 1 ; 1 2 0 −1 ; −1 −1 −1 2 ; −2 1 1 1 ).
Ora si sviluppa lungo la **terza colonna**, che ha due zeri: gli elementi non nulli sono −1 in posizione (3, 3) (segno +) e 1 in posizione (4, 3) (segno −), quindi
det D = (−1) · det( 1 1 1 ; 1 2 −1 ; −2 1 1 ) − 1 · det( 1 1 1 ; 1 2 −1 ; −1 −1 2 ) = (−1) · 9 − 1 · 3 = −12.
Dunque det D = −12 e det B = 40i · (−12) = **−480i**.

L'idea di fondo è quella della lezione: scegliendo bene la riga o la colonna e portando fuori i fattori comuni, anche un determinante con numeri complicati si riduce a pochi conti. Per fare più pratica, come suggerito a lezione, si possono inventare a casa altri esempi con matrici 3 × 3 o 4 × 4.

Nei capitoli successivi il determinante tornerà per decidere l'invertibilità di una matrice e per calcolare gli autovalori.
