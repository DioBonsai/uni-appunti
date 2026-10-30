# 33. Lo Sviluppo di Laplace
## Un metodo più furbo
Esistono vari algoritmi per calcolare il determinante in modo più agevole della definizione. Uno è lo **sviluppo di Laplace**, che riduce il calcolo di un determinante n × n a quello di determinanti (n − 1) × (n − 1), più piccoli, e così via fino a matrici 2 × 2, per le quali si conosce la formula (cap. 31).

Sia A una matrice n × n con n ≥ 2. Si indica con **C_{ij}** la sottomatrice (n − 1) × (n − 1) che si ottiene da A **cancellando la i-esima riga e la j-esima colonna**.

**In parole povere:** C_{ij} è ciò che resta della matrice dopo aver «tagliato via» la riga e la colonna in cui si trova l'elemento a_{ij}.

## Il teorema
**Teorema (sviluppo di Laplace lungo una riga).** Per ogni i fissato vale
det A = Σ_{j=1}^{n} (−1)^{i+j} · a_{ij} · det C_{ij}.

Si sceglie una riga (la i-esima) e si sommano, per tutti gli elementi di quella riga, i prodotti «elemento × determinante della sottomatrice che resta cancellando riga e colonna dell'elemento», ciascuno con il segno (−1)^{i+j}. Poiché det(ᵗA) = det A (cap. 32), vale lo stesso risultato anche **sulle colonne**:

**Corollario (sviluppo lungo una colonna).** Per ogni j fissato vale
det A = Σ_{i=1}^{n} (−1)^{i+j} · a_{ij} · det C_{ij}.

## I segni
Il segno (−1)^{i+j} associato alla casella (i, j) vale + se i + j è pari e − se i + j è dispari: **si alterna come su una scacchiera**, con il + in alto a sinistra. Come sottolineato a lezione, bisogna solo sapere se si inizia con un meno o con un più: poi il segno cambia sempre da una casella alla successiva.

![I segni (−1)^{i+j} dello sviluppo di Laplace formano una scacchiera di + e −, con + nella casella (1, 1).](figure/alg/laplace_scacchiera.png|8)

**In parole povere:** per sviluppare lungo una riga si scorre la riga elemento per elemento, si moltiplica ogni elemento per il determinante di ciò che resta e si alternano i segni + − + − …, partendo dal segno giusto per quella riga.

## Un esempio svolto, in tre modi
Si consideri A = ( 1 2 1 ; 2 1 2 ; −1 0 1 ), il cui determinante è −6 (cap. 31). Lo sviluppo di Laplace dà lo stesso risultato **qualunque riga o colonna si scelga**.

**Sviluppo lungo la prima riga** (i = 1, segni + − +):
det A = 1 · det( 1 2 ; 0 1 ) − 2 · det( 2 2 ; −1 1 ) + 1 · det( 2 1 ; −1 0 ) = 1 · 1 − 2 · 4 + 1 · 1 = 1 − 8 + 1 = −6.

**Sviluppo lungo la seconda colonna** (j = 2, segni − + −): l'elemento 2 è in riga 1, colonna 2, quindi 1 + 2 = 3 è dispari e il segno è −; cancellando la prima riga e la seconda colonna resta ( 2 2 ; −1 1 ). Poi l'elemento 1 in riga 2, colonna 2 (2 + 2 = 4 pari, segno +), con ( 1 1 ; −1 1 ), e infine l'elemento 0, che non contribuisce:
det A = −2 · det( 2 2 ; −1 1 ) + 1 · det( 1 1 ; −1 1 ) + 0 = −2 · 4 + 1 · 2 = −8 + 2 = −6.

**Sviluppo lungo la terza riga** (i = 3, segni + − +): l'elemento −1 è in riga 3, colonna 1 (3 + 1 = 4 pari, segno +) con la sottomatrice ( 2 1 ; 1 2 ); l'elemento 0 non contribuisce; l'elemento 1 è in riga 3, colonna 3 (segno +) con la sottomatrice ( 1 2 ; 2 1 ):
det A = (−1) · det( 2 1 ; 1 2 ) + 0 + 1 · det( 1 2 ; 2 1 ) = (−1) · 3 + 1 · (−3) = −3 − 3 = −6.

Come sottolineato a lezione, **con ogni metodo si deve sempre ottenere lo stesso risultato**, −6: è un buon modo per controllare i conti.

## Altri esempi dalla dispensa
**Una matrice 3 × 3 sviluppata lungo la prima riga:**
det( 1 −1 0 ; 2 −1 5 ; 1 1 −1 ) = 1 · det( −1 5 ; 1 −1 ) − (−1) · det( 2 5 ; 1 −1 ) + 0 · det( 2 −1 ; 1 1 ) = (1 − 5) + (−2 − 5) + 0 = −4 − 7 + 0 = −11.

**Conviene sviluppare lungo una riga o una colonna che contiene degli zeri**, perché i termini con a_{ij} = 0 si annullano e non serve calcolare il determinante della sottomatrice corrispondente. Per esempio, per ( 1 0 1 ; 2 0 1 ; π 3 √7 ) si sviluppa lungo la seconda colonna, che ha due zeri: l'unico elemento non nullo è 3, in riga 3 e colonna 2 (3 + 2 = 5 dispari, segno −), e
det = (−1) · 3 · det( 1 1 ; 2 1 ) = −3 · (1 − 2) = 3.
In questo esempio π e √7 non compaiono nemmeno nel risultato, perché stavano sulla riga cancellata.

Nello sviluppo bisogna sempre fare attenzione al segno (−1)^{i+j} della casella (i, j), che varia «come su una scacchiera».

Il capitolo seguente raccoglie le proprietà del determinante che permettono di scegliere in modo ancora più intelligente come calcolarlo.
