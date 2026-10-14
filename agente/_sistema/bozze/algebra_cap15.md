# 15. Somma e Prodotto per Scalare in ℝ^{n}
## Quali operazioni si possono fare
Come sottolineato a lezione, il punto dell'algebra è questo: ogni volta che si introduce un insieme, ci si deve chiedere **quali operazioni si possono fare** su di esso. Su ℝ^{n} le operazioni importanti sono due: una **somma** tra vettori e una **moltiplicazione** di un vettore per un numero reale.

## La somma di vettori
La somma prende come input due vettori e restituisce un nuovo vettore. Si calcola **termine a termine**: se v = (x_{1}, …, x_{n}) e w = (y_{1}, …, y_{n}), allora

v + w = (x_{1} + y_{1}, …, x_{n} + y_{n}).

La prima componente della somma è la somma delle prime componenti, la seconda è la somma delle seconde, e così via fino alla n-esima. Per esempio in ℝ² con v = (3, 1) e w = (1, 2) si ha v + w = (3 + 1, 1 + 2) = (4, 3).

A livello geometrico la somma si ottiene con la **regola del parallelogramma**. Si pensano i due vettori come frecce uscenti dall'origine e si costruisce il parallelogramma che ha v e w come lati: il vertice opposto all'origine è esattamente la somma v + w. Nell'esempio si parte da (3, 1) e (1, 2) e si arriva al punto (4, 3), come in figura.

## Il prodotto per uno scalare
Dato un vettore v = (x_{1}, …, x_{n}) e un numero reale a, il **prodotto** a·v è ancora un vettore, le cui componenti si ottengono moltiplicando tutte le componenti di v per a:

a·v = (a x_{1}, …, a x_{n}).

Geometricamente, moltiplicare per a vuol dire **allungare** (o accorciare) la freccia di un fattore a. Con v = (3, 1) e a = 2 si ottiene 2v = (6, 2): la freccia ha lunghezza doppia. Se il numero a è **negativo**, il vettore a·v ha lunghezza |a| volte quella di v e verso opposto a quello di v: moltiplicare per un numero negativo vuol dire invertire il verso. Per esempio −v = (−3, −1) è la freccia di v con il verso invertito.

![Somma di due vettori di ℝ² con la regola del parallelogramma, e prodotto di un vettore per lo scalare 2 e per −1.](figure/alg/ch15_somma_prodotto.png|13.5)

Il **coefficiente angolare** di una freccia, cioè il rapporto tra la y e la x, non cambia quando la si moltiplica per uno scalare: per v = (3, 1) vale 3 diviso 1 e quello di 2v = (6, 2) è 6 diviso 2, lo stesso numero (il rapporto non è definito se x = 0). Il coefficiente angolare individua la retta su cui sta la freccia, mentre il segno dello scalare ne determina il verso: moltiplicare per uno scalare non sposta dunque la freccia fuori dalla sua retta, ma ne cambia la lunghezza e, se lo scalare è negativo, il verso.

## Gli scalari
Nella moltiplicazione per un numero i numeri hanno un ruolo particolare: non servono a quantificare nulla, ma a **moltiplicare vettori**. In questo contesto i numeri si chiamano **scalari**, e l'operazione si chiama **moltiplicazione per scalare**.

**Definizione.** Uno **scalare** è un numero o, più precisamente, un elemento di un campo. Il campo va scelto in anticipo: potrebbe essere il campo dei numeri reali, e allora gli scalari sono numeri reali, oppure il campo dei numeri complessi, e allora gli scalari sono numeri complessi, e così via. Per ora, in ℝ^{n}, gli scalari sono numeri reali.

Il capitolo successivo raccoglie le proprietà di queste due operazioni e dà il nome alla struttura algebrica che ne risulta.
