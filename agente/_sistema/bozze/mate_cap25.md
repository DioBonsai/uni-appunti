# 25. Insiemi Finiti, Cardinalità e Principio dei Cassetti
## Contare gli elementi di un insieme
Contare gli elementi di un insieme A significa, intuitivamente, dare l'etichetta «1» a un elemento, «2» a un altro, e così via fino a esaurirli: nel linguaggio degli insiemi è una funzione iniettiva α : A → ℕ. Per questo approccio ci sono due problemi. Il risultato finale potrebbe dipendere da come si conta, cioè dalla funzione α scelta, e non è detto che una tale funzione esista. La definizione corretta parte da un criterio che dice quando due insiemi hanno lo stesso numero di elementi, senza contarli.

**Definizione.** Due insiemi A e B si dicono **equipollenti** se esiste una funzione biettiva f : A → B. In questo caso si dice che hanno la stessa **cardinalità** e si scrive |A| = |B|.

Poiché la composizione di biiezioni è una biiezione, se |A| = |B| e |B| = |C| allora |A| = |C|. La definizione può però dare risultati controintuitivi quando gli insiemi sono infiniti:
- la funzione f : ℕ → 2ℕ, f(n) = 2n, è una biiezione (ha come inversa g(m) = m/2), quindi ℕ e 2ℕ, l'insieme dei numeri pari, sono equipollenti, anche se i pari sono solo una parte dei naturali;
- anche ℕ × ℕ è equipollente a ℕ: si elencano le coppie (a, b) in ordine crescente di a + b e, a parità di somma, per a crescente, cioè (0, 0), (0, 1), (1, 0), (0, 2), (1, 1), (2, 0), … ; ogni coppia compare in questa lista, e il posto occupato nella lista è una biiezione con ℕ.

![Le coppie di ℕ × ℕ elencate lungo le diagonali a + b = costante: il numero nella casella è il posto nella lista.](figure/mate/ch25_diagonali.png|9)

**Definizione.** Si scrive |A| ≤ |B| se esiste una funzione **iniettiva** A → B. In modo equivalente (per A non vuoto), se esiste una funzione suriettiva B → A. Per esempio, se A ⊆ B l'inclusione è una funzione iniettiva e quindi |A| ≤ |B|; e per ogni insieme X la funzione x ↦ {x} da X in P(X) è iniettiva, quindi |X| ≤ |P(X)|.

Si accettano senza dimostrazione due fatti, intuitivamente chiari: tra due insiemi A e B vale sempre |A| ≤ |B| oppure |B| ≤ |A|; e se |A| ≤ |B| e |B| ≤ |A| allora |A| = |B| (teorema di Schröder-Bernstein).

## Insiemi finiti e infiniti
**Definizione.** Un insieme A si dice **infinito** se è equipollente a un suo sottoinsieme proprio, cioè se esiste una funzione f : A → A iniettiva ma non suriettiva. Un insieme si dice **finito** se non è infinito, cioè se ogni funzione iniettiva f : A → A è anche suriettiva.

Per gli insiemi finiti la casistica delle funzioni da A in A è molto semplice.

**Proposizione.** Sia A un insieme finito e sia f : A → A una funzione. Le seguenti affermazioni sono equivalenti: f è iniettiva; f è suriettiva; f è biettiva.

Dimostrazione. Se f è iniettiva, è anche suriettiva per la definizione di insieme finito, quindi biettiva. Se f è suriettiva, ogni elemento a ha almeno una controimmagine, e si può definire una funzione g : A → A scegliendo per ogni a un elemento di f^{-1}(a). Poiché le controimmagini di elementi diversi sono disgiunte, g è iniettiva, quindi (per quanto appena visto) biettiva, e in particolare suriettiva: questo vuol dire che ogni controimmagine è fatta da un solo elemento: se f^{-1}(a) avesse due elementi x e x', uno solo sarebbe g(a), e l'altro non sarebbe valore di g su nessun elemento (le controimmagini sono disgiunte), contro la suriettività di g. Quindi f è iniettiva. Infine, se f è biettiva è sia iniettiva sia suriettiva.

Con ℕ non succede: f(n) = n + 1 è iniettiva ma non suriettiva (0 non è immagine di niente), e questo conferma che ℕ è infinito.

## Gli insiemi I_{n} e il numero di elementi
Per n ≥ 1 si pone I_{n} = {1, 2, …, n}: sono i prototipi degli insiemi finiti. Insieme all'insieme vuoto (che ha 0 elementi) esauriscono tutte le cardinalità finite, nel senso del seguente teorema.

**Teorema.**
- Per ogni n ≥ 1 l'insieme I_{n} è finito.
- Se m ≠ n, gli insiemi I_{m} e I_{n} non sono equipollenti.
- Se m ≤ n allora |I_{m}| ≤ |I_{n}|.
- Ogni insieme finito non vuoto è equipollente a un I_{n}.
- Per ogni insieme infinito X si ha |ℕ| ≤ |X|.

La dimostrazione del libro usa l'induzione su n, un ragionamento per assurdo e una costruzione di sottoinsiemi decrescenti A ⊃ A₁ ⊃ A₂ ⊃ …: non serve ripeterla qui. La conseguenza importante è che per un insieme finito A esiste un unico n tale che A e I_{n} sono equipollenti, e si pone |A| = n: è **il numero di elementi** di A. In pratica contare gli elementi di A vuol dire costruire una biiezione tra I_{n} e A, come si è fatto per gli ordinamenti nel capitolo 23.

Questo permette di estendere la proposizione precedente a funzioni tra due insiemi diversi ma con lo stesso numero di elementi: se A e B hanno lo stesso numero di elementi, una funzione f : A → B è iniettiva se e solo se è suriettiva se e solo se è biettiva. Basta comporre con due biiezioni φ_{A} : I_{n} → A e φ_{B} : I_{n} → B e applicare la proposizione a φ_{B}^{-1} ∘ f ∘ φ_{A}.

## Il principio dei cassetti
Una conseguenza molto utile, che nei capitoli 22 e 24 è già stata usata, riguarda due insiemi finiti A e B con |A| > |B|: non possono esistere funzioni iniettive A → B. Il fatto è noto come **principio dei cassetti** o **delle gabbie dei piccioni**, e si enuncia così:

**se ci sono più piccioni che gabbie, almeno una gabbia contiene più di un piccione.**

Infatti, se P è l'insieme dei piccioni e G quello delle gabbie, assegnare a ogni piccione una gabbia è una funzione f : P → G. Per ogni gabbia g i piccioni che stanno nella gabbia g sono la controimmagine f^{-1}(g). Poiché i piccioni sono più delle gabbie, f non può essere iniettiva, e questo vuol dire che c'è una gabbia la cui controimmagine ha più di un elemento.

Il principio serve in casi concreti per arrivare a conclusioni altrimenti difficili da verificare. Su un corpo umano crescono circa 5 milioni di peli; ne segue che in una metropoli con ben più di 5 milioni di abitanti, anche escludendo chi è del tutto glabro, ci sono almeno due persone con lo stesso numero esatto di peli. Un altro esempio: un PIN di 4 cifre ha 10 000 possibilità, quindi tra 10 001 smartphone almeno due hanno lo stesso PIN.

## Insiemi numerabili
**Definizione.** Un insieme X si dice **numerabile** se è equipollente a ℕ. In concreto, X è numerabile se si possono elencare tutti i suoi elementi in una successione, X = {a₁, a₂, a₃, …}. Per esempio ℤ è numerabile, perché la lista 0, 1, −1, 2, −2, 3, −3, … include tutti i numeri interi (l'ordine in cui si alternano positivi e negativi non ha importanza). Anche ℚ è numerabile: si elencano i razionali non negativi come frazioni a/b, con b ≥ 1, secondo l'ordine di grandezza di a + b (con le frazioni non ridotte che si scartano o si ripetono), come si è fatto per ℕ × ℕ, e poi si intervallano i razionali negativi seguendo l'esempio di ℤ.

Intorno al 1880 Cantor dimostrò che esistono insiemi infiniti non numerabili, che ℝ non è numerabile e che per ogni insieme X l'insieme delle parti P(X) ha cardinalità strettamente maggiore di |X|. Qui ci si limita a ricordare questi fatti, rimandando ai testi specialistici per le tecniche di dimostrazione.

Con questo si chiude la parte sul conteggio: gli insiemi finiti e il principio dei cassetti sono alla base dei metodi dei capitoli 21-24, e il capitolo seguente (le combinazioni) riprenderà le scelte non ordinate.
