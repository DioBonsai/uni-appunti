# 25. Basi e Coordinate
## Unicità della scrittura
Una base ha una proprietà fondamentale che spiega perché la sua definizione è così importante.

**Proposizione.** Sia V uno spazio vettoriale su 𝕂 e sia {v₁, …, vₙ} una base di V. Allora ogni vettore v ∈ V si può esprimere come
v = a₁v₁ + … + aₙvₙ
con **coefficienti a₁, …, aₙ unici**.

**In parole povere:** con una base ogni vettore ha una «ricetta» e una sola. Prima, con vettori che sono solo generatori (come nel capitolo 23, dove (5, 6) si scriveva in due modi), le ricette potevano essere tante; con una base la ricetta è unica.

**Spiegazione.** Poiché i vettori sono generatori, almeno una scrittura esiste. Per l'unicità, si supponga che v = a₁v₁ + … + aₙvₙ = b₁v₁ + … + bₙvₙ. Sottraendo, 0 = (a₁ − b₁)v₁ + … + (aₙ − bₙ)vₙ, e per l'indipendenza lineare tutti i coefficienti sono nulli, cioè aᵢ = bᵢ per ogni i. ∎

## Le coordinate
**Definizione.** I numeri a₁, …, aₙ della proposizione si chiamano le **coordinate** di v nella base {v₁, …, vₙ}.

**In parole povere:** le coordinate sono le istruzioni per costruire v a partire dai vettori della base: «quanti v₁, quanti v₂, …». Sono uniche proprio perché la ricetta è unica.

Come sottolineato a lezione, le coordinate sono numeri che si associano a un punto; allo stesso modo, fissata una base, a ogni vettore si associano n numeri che lo determinano in modo unico. Se si vuole comunicare un vettore a un'altra persona o a un computer che deve fare dei calcoli, conviene mettersi d'accordo prima su una base e poi, invece di comunicare l'oggetto stesso, comunicare solo i suoi coefficienti. A lezione si è anche detto, in modo informale, che uno spazio ha in genere moltissime basi e che si può cambiare base (per esempio ℝ² ne ha infinite).

![Le coordinate di v = (3, 2) nella base canonica {e₁, e₂} sono 3 e 2: v = 3e₁ + 2e₂.](figure/alg/coordinate_base.png|9)

## Un esempio concreto
In ℝ², con e₁ = (1, 0) ed e₂ = (0, 1), il vettore (3, 2) si scrive (3, 2) = 3·(1, 0) + 2·(0, 1) = 3e₁ + 2e₂ = (3, 0) + (0, 2). Le sue coordinate nella base {e₁, e₂} sono 3 e 2. Come sottolineato a lezione, questa è una proprietà molto speciale della base canonica: i coefficienti sono esattamente le entrate del vettore. Con altre basi le coordinate sono in generale numeri diversi dalle entrate del vettore.

Il capitolo successivo applica lo stesso schema a due spazi importanti, 𝕂^{n} e i polinomi di grado limitato: si cerca una base e si contano i suoi elementi, ottenendo la dimensione.
