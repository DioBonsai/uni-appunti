# 20. Funzioni Inverse: Esistenza e Unicità
## Una sola composizione non basta
Due funzioni f : A → B e g : B → A sono una l'inversa dell'altra quando valgono **entrambe** le uguaglianze g ∘ f = id_{A} e f ∘ g = id_{B}. Non è un dettaglio: può succedere che una delle due composizioni sia l'identità e l'altra no, e allora f e g non sono inverse. Due esempi lo mostrano.

**Esempio 1: la proiezione.** Sia π₁ : ℤ × ℤ → ℤ la prima proiezione, π₁(m, n) = m, e sia f : ℤ → ℤ × ℤ la funzione f(n) = (n, 0). Componendo nell'ordine π₁ ∘ f, cioè prima f e poi π₁, si ha (π₁ ∘ f)(n) = π₁(n, 0) = n: è l'identità di ℤ. Nell'ordine opposto, invece, (f ∘ π₁)(m, n) = f(m) = (m, 0), che è diversa dalla coppia (m, n) appena n ≠ 0, quindi f ∘ π₁ non è l'identità di ℤ × ℤ. Era prevedibile: la proiezione non è biettiva, e due funzioni inverse devono esserlo entrambe.

**Esempio 2: una partizione.** Sia A = {a, b, c, d} con la partizione {a, b}, {c, d}. L'insieme quoziente Q ha due elementi, Q = {{a, b}, {c, d}}. Definiamo f : A → Q mandando ogni elemento nella propria classe (f(a) = f(b) = {a, b}, f(c) = f(d) = {c, d}) e g : Q → A scegliendo un rappresentante per classe: g({a, b}) = a e g({c, d}) = c. Allora g ∘ f manda a e b in a, c e d in c: non è l'identità di A, e non è nemmeno iniettiva. Invece f ∘ g manda {a, b} in a e poi in {a, b}, e {c, d} in c e poi in {c, d}: è l'identità di Q.

![Nei due esempi una composizione è l'identità e l'altra no: nel primo esempio f non è suriettiva, nel secondo f non è iniettiva.](figure/mate/ch20_una_composizione.png|13)

La lezione è pratica: per verificare che due funzioni sono una l'inversa dell'altra bisogna controllare **tutte e due** le composizioni.

## Ogni funzione biettiva è invertibile
Nel capitolo 19 si è visto che una funzione invertibile deve essere biettiva. Ora si dimostra il verso opposto, e si dimostra anche che l'inversa è unica.

**Teorema.** Sia f : A → B una funzione biettiva. Allora esiste una funzione g : B → A tale che f e g sono una l'inversa dell'altra, e questa g è unica.

Dimostrare l'esistenza vuol dire **costruire** g, cioè dire quanto vale g(y) per ogni y ∈ B. L'idea è di rovesciare il grafico di f, scambiando il ruolo di dominio e codominio. Non basta però usare una sola delle ipotesi.

**Dimostrazione dell'esistenza.** Si fissa y ∈ B.
1. Poiché f è suriettiva, esiste x ∈ A con f(x) = y.
2. Per avere una vera funzione bisogna definire g(y) = x, ma x deve essere scelto in modo non ambiguo: con la sola suriettività y potrebbe avere molte controimmagini, e rovesciando il grafico si otterrebbe una situazione vietata per le funzioni, un elemento del dominio con più valori.
3. Qui si usa l'iniettività: poiché f è iniettiva, la controimmagine di y è un solo elemento. Si pone allora g(y) = l'unico x ∈ A tale che f(x) = y.

Ora si controllano le due composizioni.
- Sia y ∈ B e sia x = g(y). Per definizione di g, x è proprio un elemento con f(x) = y, quindi (f ∘ g)(y) = f(g(y)) = f(x) = y, e f ∘ g = id_{B}.
- Sia x ∈ A e sia y = f(x). L'unico elemento che f manda in y è x, quindi g(y) = x, cioè (g ∘ f)(x) = g(f(x)) = x, e g ∘ f = id_{A}.

**Dimostrazione dell'unicità.** Supponiamo che g e h siano due funzioni da B in A, entrambe inverse di f: g ∘ f = id_{A} = h ∘ f e f ∘ g = id_{B} = f ∘ h. Si considera la composizione di tre funzioni g ∘ f ∘ h : B → A → B → A, che ha senso perché i domini e i codomini si concatenano, e la si calcola in due modi, sfruttando l'associatività della composizione.
1. Raggruppando le prime due funzioni, (g ∘ f) ∘ h = id_{A} ∘ h = h, perché l'identità è neutra per la composizione.
2. Raggruppando le ultime due, g ∘ (f ∘ h) = g ∘ id_{B} = g, ancora per la neutralità dell'identità.
3. Poiché è la stessa espressione, h = g.

Il trucco di calcolare la stessa espressione in due modi diversi è frequente in matematica e porta quasi sempre a qualcosa di interessante.

## Funzione biettiva e funzione invertibile sono la stessa cosa
Mettendo insieme il capitolo 19 e questo teorema, per una funzione **essere biettiva ed essere invertibile equivale**. L'unica inversa si chiama funzione inversa e si indica con f^{-1}, come nel capitolo 15.

Questo spiega perché nel capitolo 17 conveniva rendere biettiva una funzione prima di invertirla: la funzione x² da ℝ in ℝ non è invertibile, ma ristretta a una funzione da [0, +∞) in [0, +∞) diventa biettiva e la sua inversa è la radice quadrata. Infatti, partendo da un numero non negativo, elevare al quadrato e poi estrarre la radice (o fare il contrario) riporta al numero di partenza: le due composizioni sono l'identità.

Lo stesso accade per l'esponenziale e il logaritmo: l'esponenziale va ristretta nel codominio ai numeri positivi, ed è per questo che il logaritmo è definito solo per i numeri maggiori di zero.
