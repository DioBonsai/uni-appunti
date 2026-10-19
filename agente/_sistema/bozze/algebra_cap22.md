# 22. Combinazioni Lineari e Sottospazio Generato (Span)
## Due modi di costruire sottospazi
Finora i sottospazi si sono costruiti **per esclusione**: si impongono condizioni (un'entrata uguale a zero, tante entrate nulle, una simmetria) e ciò che non le rispetta viene scartato. Come sottolineato a lezione, è come far entrare tutti in un'aula e poi mandare fuori, uno per uno, chi non ha gli occhiali. L'altra strada è **per inclusione**: si parte con l'aula vuota e si fanno entrare solo quelli che servono, per esempio tutti quelli con gli occhiali. Questo secondo metodo si chiama sottospazio generato, o **Span**, e richiede prima la nozione di combinazione lineare.

## Combinazioni lineari
Sia V uno spazio vettoriale su 𝕂 e siano v₁, …, v_{k} ∈ V alcuni vettori.

**Definizione.** Una **combinazione lineare** di v₁, …, v_{k} è un vettore della forma
v = λ₁v₁ + λ₂v₂ + … + λ_{k}v_{k},
con λ₁, …, λ_{k} ∈ 𝕂 scalari qualunque.

**In parole povere:** una combinazione lineare è una «ricetta» che usa i vettori che hai già: ne prendi un po' di ciascuno (ogni vettore moltiplicato per un numero, anche negativo o zero) e li sommi. Il risultato è un nuovo vettore dello stesso spazio, perché somma e moltiplicazione per scalare restano dentro lo spazio. Per esempio 3v₁ + 2v₂ − 7v₃ è una combinazione lineare di v₁, v₂, v₃.

Un esempio in ℝ³ con v₁ = (1, 0, 0) e v₂ = (0, 1, 0): la combinazione λ₁v₁ + λ₂v₂ vale (λ₁, 0, 0) + (0, λ₂, 0) = (λ₁, λ₂, 0). Al variare di λ₁ e λ₂ si ottengono tutti i vettori con ultima componente 0, cioè il piano z = 0.

## Lo Span
**Definizione.** Il **sottospazio generato** da v₁, …, v_{k} è l'insieme di tutte le loro combinazioni lineari:
Span(v₁, …, v_{k}) = { λ₁v₁ + … + λ_{k}v_{k} | λ₁, …, λ_{k} ∈ 𝕂 }.
Si legge «span» (dall'inglese ~to span~, che in senso matematico vuol dire generare), ed è il nome che si usa anche in italiano per «lo spazio generato da».

**In parole povere:** lo Span di alcuni vettori è l'insieme di tutto ciò che riesci a costruire usando solo quei vettori, sommandoli e allungandoli o accorciandoli. Con un solo vettore non nullo ottieni la retta che passa per l'origine nella sua direzione; con due vettori non nulli e non paralleli, il piano per l'origine che li contiene; e così via.

![Span(v₁, v₂) in ℝ³ con v₁ = (1, 0, 0) e v₂ = (0, 1, 0): è il piano generato dai due vettori.](figure/alg/span_piano.png|10)

Con un singolo vettore, Span(v) = { λv | λ ∈ 𝕂 }. Per esempio in ℝ², Span((1, 2)) = { (t, 2t) | t ∈ ℝ }, la retta y = 2x.

**Proposizione.** Lo Span(v₁, …, v_{k}) è un sottospazio vettoriale di V.

**Dimostrazione.** Sia W = Span(v₁, …, v_{k}). Si verificano le tre condizioni.
1. **0 ∈ W.** Basta prendere tutti gli scalari uguali a zero: 0·v₁ + … + 0·v_{k} = 0. (Come prendere zero di tutto: il risultato è lo zero.)
2. **Chiusura rispetto alla somma.** Siano v = λ₁v₁ + … + λ_{k}v_{k} e w = μ₁v₁ + … + μ_{k}v_{k} due elementi di W. Usando la commutatività e l'associatività della somma si possono riordinare i termini, e usando la proprietà distributiva (λ + μ)v = λv + μv degli spazi vettoriali si ottiene v + w = (λ₁ + μ₁)v₁ + … + (λ_{k} + μ_{k})v_{k}, che è ancora una combinazione lineare di v₁, …, v_{k}, quindi sta in W.
3. **Chiusura rispetto al prodotto per scalare.** Se v ∈ W e λ ∈ 𝕂, allora λv = (λλ₁)v₁ + … + (λλ_{k})v_{k} (si usa la distributività λ(u + w) = λu + λw e l'associatività del prodotto), che sta ancora in W.

Il significato di questo risultato è che **lo Span è un modo per fabbricare sottospazi**: qualunque insieme di vettori si scelga, lo spazio che generano è sempre un sottospazio.

Come sottolineato a lezione, il fatto che le dimostrazioni di questo capitolo valgano in uno spazio vettoriale qualunque, e non solo in ℝ³, è un punto di forza: lo stesso ragionamento funziona per matrici, polinomi, funzioni derivabili o integrabili, e per qualsiasi spazio che si voglia immaginare, perché quasi ogni oggetto che si studia in matematica ha la struttura di uno spazio vettoriale. Il prezzo è che la teoria sembra più astratta; il vantaggio è che si dimostra una cosa molto più generale. Nel corso gli esempi saranno quasi sempre vettori di ℝⁿ e matrici.

## Esercizi
**Esercizio 6.9.** Sia W ⊆ M(2, ℝ) l'insieme delle matrici della forma ( a b ; b a ), con a, b ∈ ℝ. Si dimostra che W è un sottospazio di M(2, ℝ) e che W = Span( ( 1 0 ; 0 1 ), ( 0 1 ; 1 0 ) ).
- La matrice nulla è di questa forma (a = b = 0).
- La somma di ( a b ; b a ) e ( a′ b′ ; b′ a′ ) è ( a+a′ b+b′ ; b+b′ a+a′ ), ancora della stessa forma con parametri a + a′ e b + b′.
- Il multiplo λ·( a b ; b a ) = ( λa λb ; λb λa ) è ancora della stessa forma.
- Ogni matrice ( a b ; b a ) si scrive come a·( 1 0 ; 0 1 ) + b·( 0 1 ; 1 0 ), quindi sta nello Span; viceversa ogni combinazione lineare delle due matrici ha quella forma. Dunque W coincide con lo Span.

**Esercizio 6.10.** In ℝ³ siano v₁ = (1, 0, 1) e v₂ = (0, 1, 1). Si descrive Span(v₁, v₂) e si controlla quali tra u = (1, 2, 3) e w = (1, 2, 4) vi appartengono.
- Una combinazione è a·v₁ + b·v₂ = (a, b, a + b). Quindi Span(v₁, v₂) = { (x, y, z) | z = x + y }: il piano di equazione z = x + y.
- u = (1, 2, 3): 1 + 2 = 3, quindi z = x + y e u appartiene al piano (si ottiene con a = 1, b = 2).
- w = (1, 2, 4): 1 + 2 = 3 ≠ 4, quindi w **non** appartiene al piano.

Il passo successivo è chiedersi quando alcuni vettori generano tutto lo spazio senza ridondanze: è il tema della dipendenza e indipendenza lineare.
