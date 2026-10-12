# 12. Radici di un Polinomio e Molteplicità
## Che cos'è una radice
Se p(x) è un polinomio e a è un numero (reale o complesso), si indica con p(a) il numero che si ottiene **sostituendo** a al posto di x. Per esempio, se p(x) = x² − 2 e a = −2, allora p(−2) = (−2)² − 2 = 4 − 2 = 2. Si può interpretare un polinomio come una funzione: si sceglie un valore per x e il polinomio restituisce p(x).

Un numero a è una **radice** di p(x) se e solo se p(a) = 0. Determinare le radici di un polinomio è uno dei problemi più classici dell'algebra.

## Il criterio con la divisione
**Proposizione.** a è una radice di p(x) se e solo se (x − a) divide p(x), cioè se e solo se p(x) = (x − a)q(x) per qualche polinomio q(x), senza resto.

**Dimostrazione.**
1. Si fa la divisione con resto di p(x) per (x − a): esistono q(x) e r(x) con p(x) = (x − a)q(x) + r(x).
2. Il grado di r(x) è strettamente minore del grado di (x − a), che vale 1: quindi r(x) è una costante r₀ (eventualmente nulla), che non dipende da x.
3. Si calcola p in a: p(a) = (a − a)q(a) + r₀ = 0 + r₀ = r₀.
4. Quindi a è radice di p ⟺ p(a) = 0 ⟺ r₀ = 0 ⟺ il resto è zero ⟺ (x − a) divide p(x).

Il senso del risultato: a è radice se e solo se si può **togliere un fattore (x − a)** dal polinomio.

## La molteplicità
Se a è una radice, si può dividere p(x) per (x − a) e, nel quoziente, forse dividere ancora per (x − a), e magari una terza volta. La **molteplicità** di una radice a è il massimo numero naturale k tale che (x − a)^{k} divide p(x); è sempre almeno 1, altrimenti a non sarebbe una radice. In un certo senso, nel polinomio ci sono k fattori (x − a).

## Esempio 1: x³ − 1
Sia p(x) = x³ − 1, un polinomio di grado 3 a coefficienti reali. Si vede subito che a = 1 è una radice: p(1) = 1³ − 1 = 0. Per la proposizione (x − 1) divide p(x). Si fa la divisione:
1. x³ : x = x²; x²(x − 1) = x³ − x², sottratto da p lascia x² − 1.
2. x² : x = x; x(x − 1) = x² − x, sottratto lascia x − 1.
3. x − 1 : (x − 1) = 1, resto 0.

Quindi x³ − 1 = (x − 1)(x² + x + 1) e il resto è zero, come doveva essere. La molteplicità è almeno 1. Per vedere se si può togliere un secondo fattore (x − 1) bisogna controllare se 1 è radice del quoziente q(x) = x² + x + 1: q(1) = 1 + 1 + 1 = 3 ≠ 0. Quindi (x − 1) non divide q(x) e la **molteplicità di 1 è 1**.

## Esempio 2: x³ − 2x² + x
Sia p(x) = x³ − 2x² + x. Anche qui a = 1 è una radice: p(1) = 1 − 2 + 1 = 0. La divisione per (x − 1) dà il quoziente x² − x con resto 0, quindi p(x) = (x − 1)(x² − x). Si controlla se 1 è radice anche di q(x) = x² − x: q(1) = 1 − 1 = 0, quindi sì. Dividendo ancora, x² − x = (x − 1)x e così

p(x) = (x − 1)² · x.

Non si può togliere un terzo fattore (x − 1), perché dividendo x per (x − 1) resterebbe un resto. La **molteplicità di 1 è 2**. C'è anche la radice **0**, con molteplicità 1 (è il fattore x).

## Radici "contate con molteplicità"
Nel secondo esempio il polinomio ha grado 3 e ha due radici distinte, 1 e 0, ma 1 ha molteplicità 2: contata con la sua molteplicità vale come due radici, quindi in totale si hanno 2 + 1 = 3 radici. Questo è il senso di "radici contate con molteplicità": le due radici "uguali" sono lo stesso numero, ma si contano due volte.

Nel prossimo capitolo si vede quante radici può avere al massimo un polinomio.
