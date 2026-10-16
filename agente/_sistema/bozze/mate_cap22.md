# 22. Il Metodo delle Scelte Successive
## Il prodotto cartesiano conta le scelte indipendenti
Nel capitolo 3 si è visto che se |A| = m e |B| = n allora |A × B| = m · n. La ragione si vede elencando gli elementi, A = {a₁, …, a_{m}} e B = {b₁, …, b_{n}}: le coppie si dispongono in una griglia rettangolare, con una riga per ogni elemento di A, che contiene tutte le coppie con quel primo elemento, e una colonna per ogni elemento di B. La griglia ha m righe e n colonne, quindi m · n caselle, una per ciascuna coppia.

![Le coppie di A × B in una griglia con m righe e n colonne: in tutto m · n.](figure/mate/ch22_griglia.png|10)

Il prodotto cartesiano modella una situazione in cui si fa una scelta arbitraria in un insieme e un'altra scelta, indipendente, in un secondo insieme. La stessa idea vale con tre, quattro o più insiemi.

**Proposizione.** Se A₁, A₂, …, A_{k} sono insiemi finiti con |A_{i}| = n_{i}, allora |A₁ × A₂ × … × A_{k}| = n₁ · n₂ · … · n_{k}.

Si dimostra per induzione su k: il caso k = 2 è quello già noto, e per k > 2 gli insiemi (A₁ × … × A_{k−1}) × A_{k} e A₁ × … × A_{k−1} × A_{k} si corrispondono uno a uno (una biiezione ovvia riordina le parentesi), quindi |A₁ × … × A_{k}| = |A₁ × … × A_{k−1}| · |A_{k}| = (n₁ · … · n_{k−1}) · n_{k}.

## Un esempio: il menù
Un ristorante offre un menù composto da un panino, una bibita e un dolce. Qualunque panino, qualunque bibita e qualunque dolce si scelga, si ottiene un menù valido. Se ci sono 12 panini, 5 bibite e 4 dolci, ogni menù è una terna ordinata (panino, bibita, dolce), cioè un elemento del prodotto cartesiano P × B × D dei tre insiemi. Il numero di menù possibili è quindi

|P| · |B| · |D| = 12 · 5 · 4 = 240.

Questo vuol dire che si può andare al ristorante per 240 giorni di seguito senza mai ripetere lo stesso menù.

## L'albero delle scelte
Lo stesso risultato si può vedere con un **albero**. Si parte dalla radice e si disegna un ramo per ogni possibile prima scelta (12 panini); dalla fine di ciascun ramo partono altri 5 rami, uno per ogni bibita; dalla fine di questi partono 4 rami, uno per ogni dolce. I punti finali dell'albero rappresentano tutte le possibili scelte complete, e il loro numero è il prodotto 12 · 5 · 4.

![L'albero delle scelte per il menù: a ogni livello le scelte sono nello stesso insieme.](figure/mate/ch22_albero_menu.png|13)

Il **metodo delle scelte successive** si può così enunciare: se una situazione si ottiene con una successione di k scelte indipendenti, e per la prima ci sono n₁ possibilità, per la seconda n₂, per la terza n₃ e così via, il numero totale di situazioni è n = n₁ · n₂ · … · n_{k}.

C'è una differenza importante con il prodotto cartesiano. Nel caso del menù le scelte avvengono sempre negli stessi insiemi, quali che siano le scelte precedenti. In generale invece l'insieme in cui si sceglie a un certo passo può **dipendere** dalle scelte fatte prima: se, per esempio, scegliendo un certo panino cambiano le bibite disponibili, le bibite tra cui scegliere sono diverse, ma è sufficiente che il loro **numero** sia sempre lo stesso a quel livello perché la formula continui a valere. Si vedrà tra poco un caso del genere con gli ordinamenti.

## Altri esempi
- **Le targhe.** Se una targa è formata da 3 lettere dell'alfabeto inglese (26 lettere) seguite da 4 cifre, con ripetizioni ammesse, i modi sono 26 · 26 · 26 · 10 · 10 · 10 · 10 = 175 760 000.
- **I PIN.** Un PIN di 4 cifre ha 10 · 10 · 10 · 10 = 10⁴ = 10 000 possibilità. Se si hanno 10 001 smartphone, per il principio delle gabbie dei piccioni almeno due devono avere lo stesso PIN.
- **Le funzioni da A in B.** Se |A| = m e |B| = n, per definire una funzione f : A → B bisogna dire quanto vale f(a) per ognuno degli m elementi di A, e ogni valore si può scegliere tra gli n elementi di B, senza vincoli sugli altri. Quindi le funzioni da A in B sono n · n · … · n = n^{m}.
