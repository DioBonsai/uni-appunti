# 34. Quanti Cicli Ci Sono e il Teorema di Scomposizione in Cicli Disgiunti
## Ripasso: i cicli
La lezione riprende i cicli del capitolo precedente. Un **ciclo** è una permutazione per cui esiste un sottoinsieme {i₁, …, i_ℓ} (con ℓ ≥ 2) dei primi n numeri tale che l'immagine di i₁ è i₂, quella di i₂ è i₃, …, quella di i_ℓ è i₁, mentre ogni t che non sta tra questi numeri resta fermo. Un ciclo, quindi, sposta alcuni numeri nel successivo, l'ultimo nel primo, e non muove gli altri.

Si scrive con la notazione compatta: (4 1 2 5) vuol dire che 4 va in 1, 1 va in 2, 2 va in 5, 5 va in 4, e per esempio il 3 resta fermo. La scrittura non è unica: lo stesso ciclo si può scrivere partendo da 1, da 2 o da 5, per esempio (2 5 4 1). Ci sono quattro possibilità, perché si può scegliere come primo uno qualsiasi dei quattro numeri. Il numero ℓ di elementi mossi è la **lunghezza** del ciclo (in parole povere: quanti numeri il ciclo sposta): questo è un ciclo di lunghezza 4. Come si vedrà, la lunghezza avrà un ruolo importante.

(In parole povere: un ciclo è un «giro» in cui ogni numero passa al posto del successivo e l'ultimo torna al posto del primo.)

## Quanti sono i cicli di una data lunghezza
Fissati n e una lunghezza ℓ, ci si può chiedere quanti cicli di quella lunghezza esistono in S_n. Si parte da un esempio: **quanti cicli di lunghezza 4 ci sono in S₆?**

Per formare un ciclo bisogna scegliere 4 numeri su 6. La scelta è **ordinata** o disordinata? Il ciclo (4 1 2 5) e il ciclo (1 5 4 2) muovono gli stessi quattro numeri, ma in modo diverso (nel primo il successore di 1 è 2, nel secondo è 5): sono funzioni diverse. Quindi **l'ordine conta**, e ovviamente un numero non si può scegliere due volte: si tratta di **disposizioni semplici** di 4 oggetti scelti fra 6, che sono
6! / (6 − 4)! = 6 · 5 · 4 · 3 = 360.

Ma disposizioni diverse possono dare lo stesso ciclo: lo stesso ciclo si può scrivere in 4 modi (uno per ogni possibile punto di partenza). Le disposizioni sono quindi 4 volte tante quanti i cicli, e il numero dei cicli si ottiene dividendo per 4:
360 / 4 = **90**.

**In generale.** Si scelgono ℓ elementi fra n, in modo ordinato: le disposizioni sono n! / (n − ℓ)!. Ogni ciclo di lunghezza ℓ si può scrivere in ℓ modi, scegliendo in modo arbitrario uno degli ℓ elementi come punto di partenza della scrittura circolare. Dunque:

**I cicli di lunghezza ℓ in S_n sono (1/ℓ) · n! / (n − ℓ)!.**

(In parole povere: si contano tutte le liste ordinate di ℓ numeri e si divide per ℓ, perché ogni ciclo compare ℓ volte, una per ogni punto di partenza.)

## Richiamo: cicli disgiunti
Due cicli sono **disgiunti** se gli insiemi dei numeri che muovono hanno intersezione vuota, (in parole povere: due cicli sono disgiunti se muovono numeri completamente diversi) e due cicli disgiunti **commutano** nella composizione: si possono comporre in qualunque ordine e il risultato è sempre lo stesso (capitolo precedente).

## Il teorema di scomposizione
**Teorema.** Sia π ∈ S_n una permutazione **diversa dall'identità**. Allora esiste una scrittura **essenzialmente unica**
**π = C_k ∘ … ∘ C₂ ∘ C₁**,
dove ogni C_i è un ciclo e i cicli C₁, …, C_k sono **a due a due disgiunti**.

Per l'identità non c'è niente da dire: va bene com'è.

(In parole povere: ogni permutazione che non sia l'identità si può spezzare in cicli che non si toccano, e la spezzatura è praticamente una sola.)

L'esempio della lezione precedente (cap. 33), in cui nella permutazione si trovavano due «circuiti», non era una coincidenza: vale per **qualunque** permutazione.

**Un'analogia.** Come sottolineato a lezione, è un po' come il fatto che ogni numero intero si scrive come prodotto di numeri primi (escludendo 0, 1 e −1): fra tutte le permutazioni ce n'è un sottoinsieme particolare, i cicli, che bastano per ricostruire tutte le altre. Di quel fatto sui numeri si parlerà nel capitolo sull'aritmetica.

## Che cosa vuol dire «a due a due disgiunti»
Con più di due cicli bisogna stare attenti. Dire che i cicli sono **a due a due disgiunti** significa che, **comunque se ne prendano due**, la loro intersezione è vuota. Non basta che non ci sia nessun elemento comune a tutti: per esempio gli insiemi {1, 2}, {2, 3} e {1, 3} non hanno nessun elemento in comune a tutti e tre, ma presi a due a due si intersecano (il primo e il secondo condividono il 2, e così via), quindi **non** sono a due a due disgiunti. (In parole povere: comunque si prendano due cicli, non devono avere nessun numero in comune.)

## Che cosa vuol dire «essenzialmente unica»
Siccome ogni coppia di cicli commuta, la scrittura si può riordinare: C₁ ∘ C₂ ∘ C₃ si può scrivere anche C₂ ∘ C₃ ∘ C₁, o C₂ ∘ C₁ ∘ C₃, e così via, perché ogni volta due cicli vicini si possono scambiare. Quindi non è «unica» in senso stretto. È **essenzialmente unica** nel senso che i **cicli che compaiono** sono completamente determinati dalla permutazione di partenza: si possono scrivere in ordine diverso, ma non ce ne possono essere altri. Come per i primi: 36 = 2² · 3², e non esiste un'altra scomposizione, perché i primi 2 e 3 (e i loro esponenti) sono completamente individuati dal numero 36.

(In parole povere: «essenzialmente unica» vuol dire che i cicli sono sempre gli stessi, e cambia al massimo l'ordine in cui si scrivono.)

Una considerazione marginale: se i cicli sono k, poiché ognuno muove almeno due elementi e i cicli muovono elementi diversi, deve essere 2k ≤ n, cioè k ≤ n/2.

## Il tipo di una permutazione
**Definizione.** Sia π ≠ id e sia π = C_k ∘ … ∘ C₁ la sua scrittura in cicli a due a due disgiunti. Sia ℓ_i la lunghezza del ciclo C_i. Poiché i cicli si possono riordinare, si può sempre fare in modo che **ℓ₁ ≥ ℓ₂ ≥ … ≥ ℓ_k**. La sequenza (ℓ₁, ℓ₂, …, ℓ_k) si chiama **tipo** di π.

(In parole povere: il tipo è la lista, dalla più lunga alla più corta, delle lunghezze dei cicli di cui è fatta la permutazione.)

- Una permutazione di tipo (4, 2) è la composizione di un ciclo di lunghezza 4 e di uno di lunghezza 2, disgiunti.
- Una di tipo (3, 3, 2) è fatta da due cicli di lunghezza 3 e uno di lunghezza 2, a due a due disgiunti.

Poiché i cicli sono a due a due disgiunti, la **somma delle lunghezze non supera n**. Se la somma è **minore di n**, ci sono numeri **non spostati** dalla permutazione: per esempio, una permutazione di 6 elementi con un 3-ciclo e un 2-ciclo ha un sesto numero che resta fisso.

**Esempio: i tipi possibili in S₄.** Fissato n = 4, si possono elencare tutti i tipi: (4), cioè un ciclo di lunghezza 4; (3), un 3-ciclo con un elemento fisso; (2, 2), due scambi disgiunti; (2), un solo scambio con gli altri due elementi fissi; e infine l'identità, che non sposta nulla. Sono le uniche possibilità, e sono poche. Si può verificare che le permutazioni di questi tipi sono rispettivamente 6, 8, 3, 6 e 1, che sommate danno 24 = 4!, cioè tutte le permutazioni di S₄.

Per n = 5 le possibilità aumentano, e al crescere di n il numero dei possibili tipi «esplode».

## Un problema collegato: le partizioni di un numero
Elencare i tipi possibili è strettamente imparentato con un problema puramente matematico, di cui si è occupato **Ramanujan**, il matematico indiano di circa un secolo fa: dato n, in quanti modi si può scrivere n come **somma di interi più piccoli**? Per esempio 10 si può scrivere come 10, 9 + 1, 8 + 2, 8 + 1 + 1, 7 + 3, 7 + 2 + 1, 7 + 1 + 1 + 1, e così via. Queste scritture si chiamano **partizioni** di n (in parole povere: i modi di spezzare n in addendi). Non esiste una formula esatta semplice che dia il numero delle partizioni inserendo n: ci sono formule ricorsive e si sa a che velocità cresce questo numero, ma il problema è complicato. La somiglianza con i tipi è evidente, con la differenza che per i tipi la somma può essere anche minore di n.

La dimostrazione del teorema si trova nel capitolo successivo.
