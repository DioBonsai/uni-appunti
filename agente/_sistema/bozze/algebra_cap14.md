# 14. Lo Spazio Euclideo ℝ^{n}: Vettori, Coordinate e Rappresentazioni
## Perché un punto di vista algebrico
Dopo aver costruito gli strumenti necessari (i campi, i numeri complessi, i polinomi), si possono finalmente definire gli **spazi vettoriali**, che saranno gli oggetti fondamentali del corso. Non si parte però dalla definizione generale, ma da un esempio speciale: lo **spazio euclideo**.

Lo spazio euclideo è lo spazio su cui si fa la geometria classica, quella di punti e rette. Gli spazi che si riescono a vedere e su cui si può fare geometria visiva hanno però dimensione due o tre, mentre nelle applicazioni servono spesso spazi molto più grandi, che non si possono disegnare. Per manipolare questi oggetti bisogna quindi farlo in modo **algebrico**: è per questo che lo spazio euclideo si definisce con una formula e non con un disegno.

## Che cos'è ℝ^{n}
Sia n ≥ 1 un numero naturale.

**Definizione.** Lo **spazio euclideo n-dimensionale** è l'insieme ℝ^{n} = ℝ × ℝ × … × ℝ (n copie di ℝ).

Chi ha visto il prodotto cartesiano in Matematica discreta riconosce subito la costruzione: ℝ^{n} è il prodotto cartesiano di ℝ con sé stesso n volte. I suoi elementi sono quindi le **n-uple** (x_{1}, …, x_{n}) di n numeri reali. Per pura comodità, anziché scriverle in orizzontale come si fa di solito, le n-uple si scrivono **in verticale**:

v = (x_{1}, x_{2}, …, x_{n}), con x_{1}, …, x_{n} ∈ ℝ,

cioè come **vettore colonna**, con x_{1} in alto e x_{n} in basso. Nelle formule in questo riassunto un vettore colonna si indica per brevità con le sue componenti separate da virgole.

Un elemento di ℝ^{n} si chiama **vettore**. Il termine in realtà ha un significato più generale, che si vedrà con gli spazi vettoriali, ma per ora "vettore" vuol dire semplicemente "elemento di ℝ^{n}". Dato v = (x_{1}, …, x_{n}), il numero x_{i} è la **i-esima componente** o **i-esima coordinata** di v: x_{1} è la prima componente, x_{2} la seconda e così via.

Il vettore con tutte le componenti nulle, (0, …, 0), si chiama **origine** e si indica con 0 oppure con O.

Il nome "n-dimensionale" va letto per ora come una parola unica: la nozione di dimensione non è ancora stata definita. Come sottolineato a lezione, si vedrà più avanti che ℝ^{n} è effettivamente uno spazio di dimensione n, ma serve prima definire che cosa significa.

## I casi ℝ² e ℝ³
Due casi speciali si possono rappresentare geometricamente.
- Per n = 2, ℝ² = { (x, y) | x, y ∈ ℝ } è l'insieme delle coppie di numeri reali, il **piano cartesiano**: un vettore di coordinate a e b si rappresenta con il punto del piano di coordinate a e b. Per esempio il punto (3, 2) si ottiene partendo dall'origine, andando avanti di 3 unità nella direzione dell'asse x e poi su di 2 unità nella direzione dell'asse y.
- Per n = 3, ℝ³ = { (x, y, z) | x, y, z ∈ ℝ } è lo **spazio cartesiano** a tre dimensioni: il vettore di coordinate a, b, c corrisponde al punto che si raggiunge partendo dall'origine, spostandosi di a unità lungo x, poi di b unità lungo y e infine di c unità lungo z. I tre assi sono tre direzioni indipendenti (alla lavagna un asse esce dal piano della lavagna e non si può disegnare fedelmente). Per esempio il punto con x = 3, y = 4 e z = 2 corrisponde al vettore (3, 4, 2).

![Il vettore (3, 2) in ℝ² e il vettore (3, 4, 2) in ℝ³: punto e freccia dall'origine.](figure/alg/ch14_R2_R3.png|13)

## Tre modi di vedere un vettore
In generale un vettore di ℝ^{n} si può rappresentare in tre modi:
- come **n-upla** di numeri (x_{1}, …, x_{n}): è il modo che si usa di più, perché è quello che permette di fare i conti;
- come **punto** di coordinate (x_{1}, …, x_{n});
- come **freccia** che va dall'origine al punto di coordinate (x_{1}, …, x_{n}).

Queste tre rappresentazioni sono sostanzialmente equivalenti, e si sceglie ogni volta la scrittura più comoda: quando serve calcolare si usa la n-upla, quando serve disegnare il punto o la freccia. Di solito si usano le lettere maiuscole P, Q per i punti e le minuscole v, w per i vettori, ma questo dipende dal contesto.

Il capitolo successivo introduce le due operazioni fondamentali che si possono fare con i vettori di ℝ^{n}: la somma e la moltiplicazione per un numero.
