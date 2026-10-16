# 23. Ordinamenti, Fattoriale e Anagrammi
## Ordinare un insieme
Dato un insieme finito A con n elementi, ci si chiede in quanti modi diversi se ne possono ordinare gli elementi, cioè metterli in fila: pensate a un mazzo di carte da riordinare o a un gruppo di libri da sistemare in uno scaffale. Un insieme non ha un ordine naturale, ma quando serve lo si può scegliere, e i modi sono molti.

Ordinare significa dire quale elemento è il primo, quale il secondo, e così via. Chiamiamo I_{n} = {1, 2, …, n} l'insieme dei primi n numeri naturali: scegliere un ordinamento vuol dire associare un elemento di A a ciascun numero 1, 2, …, n, in modo che ogni elemento di A compaia una e una sola volta. Un **ordinamento** di A è dunque una **funzione biettiva** I_{n} → A, e contare gli ordinamenti equivale a contare le funzioni biettive.

## L'albero e il numero degli ordinamenti
Si costruisce la funzione scegliendo un elemento alla volta. Per la posizione 1 ci sono n scelte, perché si può scegliere qualunque elemento di A. Per la posizione 2 ce ne sono n − 1: l'elemento già scelto non si può usare di nuovo, altrimenti la funzione non sarebbe iniettiva. Per la posizione 3 ne restano n − 2, e così via, finché alla penultima posizione restano 2 scelte e all'ultima una sola: l'unico elemento non ancora scelto.

![L'albero degli ordinamenti di {a, b, c}: 3 scelte, poi 2, poi 1, in tutto 6.](figure/mate/ch23_albero_permutazioni.png|13)

Qui le scelte possibili al secondo livello **dipendono** da dove ci si trova al primo (se si è scelto a, si sceglie tra b e c; se si è scelto b, tra a e c), ma il loro numero è lo stesso, e per questo basta moltiplicare. Con n = 3 si hanno 3 · 2 · 1 = 6 ordinamenti, che si possono scrivere tutti: (a, b, c), (a, c, b), (b, a, c), (b, c, a), (c, a, b), (c, b, a).

Il numero totale di ordinamenti è il prodotto n · (n − 1) · (n − 2) · … · 3 · 2 · 1. Questo numero si chiama **n fattoriale** e si scrive n!.

**Definizione.** Per n ∈ ℕ si pone 0! = 1 e n! = 1 · 2 · 3 · … · n per n ≥ 1.

**Proposizione.** Se A è un insieme finito con n elementi, gli ordinamenti di A sono n!.

Qualche valore: 1! = 1, 2! = 2, 3! = 6, 4! = 24, 5! = 120, 6! = 720, 7! = 5040, 8! = 40 320. Il fattoriale cresce molto in fretta: le 8 persone che partecipano alla finale dei 100 metri possono arrivare in 8! = 40 320 ordini diversi, e i modi di riordinare un mazzo di 52 carte sono 52!, un numero enorme.

Due osservazioni sulla definizione. Primo, 0! = 1 è una **convenzione**: il prodotto 1 · 2 · … · n non ha senso per n = 0, e si pone 0! = 1 perché così certe formule si scrivono senza dover trattare a parte il caso 0. Secondo, vale n! = n · (n − 1)! per ogni n ≥ 1, perché i fattori da n − 1 in giù formano esattamente (n − 1)!. È una **definizione ricorsiva** del fattoriale, come si userebbe in un linguaggio di programmazione che permette le funzioni ricorsive.

## Gli anagrammi
Un caso particolare di riordinamento è l'**anagramma**. Si parte da un insieme di simboli A, che chiamiamo **alfabeto** (le lettere dalla A alla Z, ma anche cifre e simboli speciali: in una password l'alfabeto è l'insieme di tutti i caratteri ammessi). Una **parola** è una successione finita di simboli di A, come TUZAAB, che non deve avere alcun senso compiuto. Fissare una parola di lunghezza ℓ vuol dire fissare una funzione P : I_{ℓ} → A, che dice quale lettera sta al primo posto, al secondo e così via.

In generale questa funzione non è biettiva: non è detto che compaiano tutte le lettere dell'alfabeto, e una lettera può comparire più volte. Un **anagramma** di P è un rimescolamento delle lettere della parola, cioè una parola ottenuta riordinando le stesse lettere, con le ripetizioni incluse (la parola stessa conta come uno dei suoi anagrammi).

Se la parola ha **tutte lettere diverse**, riordinarla significa riordinare l'insieme delle sue lettere, e gli anagrammi sono ℓ!. Gli anagrammi di AGO sono 3! = 6: AGO, AOG, GAO, GOA, OAG, OGA. LUNA, con 4 lettere diverse, ha 4! = 24 anagrammi; PORTA ne ha 5! = 120.

Il problema nasce quando alcune lettere si **ripetono**. La parola ORO non ha 3! = 6 anagrammi, ma solo 3: ORO, OOR, ROO. Rimescolare le due O fra loro, infatti, formalmente è un riordinamento, ma la parola resta la stessa e non conta come anagramma nuovo.

Il ragionamento generale è il seguente: si parte dai ℓ! riordinamenti possibili e, per ogni lettera ripetuta, si divide per il numero di modi in cui si possono scambiare tra loro le sue copie, che non cambiano la parola.

**Proposizione.** Sia P una parola di lunghezza ℓ in cui k simboli compaiono più volte, il j-esimo simbolo compare r_{j} volte. Allora il numero degli anagrammi di P è

ℓ! / (r₁! · r₂! · … · r_{k}!).

Per ogni simbolo che si ripete r volte, i riordinamenti delle sue r copie sono r!, e tutti producono la stessa parola: bisogna quindi dividere per r!, e così per ogni simbolo ripetuto.

**Esempi.**
- ORO: ℓ = 3, la O compare 2 volte, quindi 3!/2! = 6/2 = 3.
- POZZO: ℓ = 5, la O e la Z compaiono due volte ciascuna, quindi 5!/(2! · 2!) = 120/4 = 30.
- MATEMATICA: ℓ = 10; la M compare 2 volte, la T 2 volte, la A 3 volte, mentre E, I e C compaiono una sola volta (e non contano nel prodotto, perché 1! = 1). Gli anagrammi sono 10!/(2! · 2! · 3!) = 3 628 800/24 = 151 200. Il numero importa poco, conta il metodo.
