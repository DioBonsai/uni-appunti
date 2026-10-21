# 23. Generatori, Ridondanza e Indipendenza Lineare
## Due domande sugli stessi vettori
Nel capitolo precedente lo Span ha risposto a una domanda: dati dei vettori, quali vettori si riescono a costruire combinandoli? Come sottolineato a lezione, davanti a un insieme di vettori ci si pongono due domande: generano tutto lo spazio? E lo generano in modo efficace, cioè senza vettori inutili? Per rispondere si introducono tre concetti fondamentali: insieme di generatori, insieme linearmente indipendente e base. Gli esempi che seguono servono a motivare le definizioni, che arrivano alla fine del capitolo.

## Esempio (a): tre vettori in ℝ²
Sia V = ℝ² e si considerino v₁ = (1, 0), v₂ = (−1, 0) e v₃ = (0, 1). Il loro Span è l'insieme di tutti i vettori della forma
a·v₁ + b·v₂ + c·v₃ = (a − b, c), con a, b, c ∈ ℝ qualunque.

Per ottenere un qualunque vettore (x, y) del piano basta scegliere a = x, b = 0 e c = y: quindi **Span(v₁, v₂, v₃) = ℝ²**, e si dice che v₁, v₂, v₃ **generano** ℝ². Un vettore può però essere scritto in più modi. Per esempio (5, 6) = 5·v₁ + 0·v₂ + 6·v₃, ma anche (5, 6) = 0·v₁ − 5·v₂ + 6·v₃.

Il fatto che ci siano più scritture è il segnale che qualcosa è di troppo: **un vettore non serve, è ridondante**. Qui v₂ si ricava dagli altri: v₂ = (−1, 0) = (−1)·v₁ + 0·v₃. Portando tutto a sinistra si ottiene la relazione
v₁ + v₂ + 0·v₃ = 0 (il vettore nullo),
che è la stessa uguaglianza vista da un'altra parte (basta spostare i termini da un membro all'altro). Per questo motivo si dice che v₁, v₂, v₃ sono **linearmente dipendenti**: una loro combinazione lineare con coefficienti non tutti nulli dà il vettore nullo.

![A sinistra v₁, v₂, v₃ generano ℝ² ma v₂ = −v₁ è ridondante; a destra Span(w) è una retta.](figure/alg/generatori_ridondanti.png|14)

## Esempio (b): un solo vettore
Si prenda ora il solo vettore w = (1, 1). Il suo Span è { a·(1, 1) | a ∈ ℝ } = { (a, a) | a ∈ ℝ }, cioè la retta formata dai multipli di w (la bisettrice del primo e terzo quadrante). Due osservazioni:
1. Span(w) ≠ ℝ²: da solo w non genera tutto il piano.
2. Esiste un valore di a diverso da 0 per cui a·w = (0, 0)? No: l'unico modo di ottenere il vettore nullo è a = 0. Quindi w non è ridondante: togliendolo non resterebbe nulla che generi qualcosa, oltre all'origine.

In questo caso si dice che w è **linearmente indipendente**: ha la proprietà buona di non essere ridondante, ma non genera tutto lo spazio.

## Esempio (c): generare senza ridondanze
Tornando a (a): se si toglie v₂ si ottiene {v₁, v₃} = {(1, 0), (0, 1)}, che genera ancora tutto ℝ², stavolta **senza ridondanze**. Insiemi di vettori di questo tipo, che hanno entrambe le proprietà buone, si chiameranno **basi**.

## Le definizioni
Sia V uno spazio vettoriale su un campo 𝕂 e siano v₁, …, vₙ ∈ V alcuni vettori.

**Definizione (insieme di generatori).** I vettori v₁, …, vₙ sono un **insieme di generatori** di V se Span(v₁, …, vₙ) = V. In modo equivalente: ogni vettore v ∈ V si può scrivere come v = a₁v₁ + … + aₙvₙ per qualche a₁, …, aₙ ∈ 𝕂.

**In parole povere:** i vettori generano lo spazio se, mescolandoli con le dosi giuste, si riesce a ottenere qualunque vettore dello spazio, come un set di colori primari da cui si ricavano tutti gli altri. Non si chiede che la dosatura sia unica: basta che ce ne sia almeno una.

**Definizione (indipendenza lineare).** I vettori v₁, …, vₙ sono **linearmente indipendenti** (l.i.) se l'unico modo di scrivere il vettore nullo come 0 = a₁v₁ + … + aₙvₙ è con a₁ = a₂ = … = aₙ = 0, cioè con la combinazione lineare banale. Altrimenti sono **linearmente dipendenti**.

**In parole povere:** i vettori sono indipendenti se nessuno si può ricostruire con gli altri: per tornare al punto di partenza, cioè all'origine, l'unica ricetta possibile è «non prendere niente di nessuno». Se invece esiste una ricetta con dosi non tutte nulle che riporta allo zero, qualcosa è di troppo.

L'indipendenza lineare è il concetto più delicato da digerire, ed è quello che a lezione si presenta come la proprietà che ci piace (la non ridondanza). Come sottolineato a lezione, nell'esempio (a) c'era un insieme che genera tutto ma non è indipendente; nell'esempio (b) c'era un insieme indipendente che non è di generatori; e {v₁, v₃} dell'esempio (c) ha entrambe le proprietà.

## Le basi
**Definizione (base).** I vettori v₁, …, vₙ sono una **base** di V se sono sia linearmente indipendenti sia un insieme di generatori di V.

**In parole povere:** una base è un «kit» di vettori completo e senza sprechi: togliendone uno non si genera più tutto; aggiungendone uno, il nuovo vettore si può già ricostruire con gli altri (è di troppo).

Riassumendo gli esempi: {v₁, v₂, v₃} genera ma non è l.i.; {w} è l.i. ma non genera; {v₁, v₃} è una base di ℝ².

Il capitolo successivo studia come riconoscere se un insieme di vettori è dipendente o indipendente, e quali proprietà seguono dalle definizioni.
