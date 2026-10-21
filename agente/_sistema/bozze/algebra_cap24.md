# 24. Dipendenza Lineare: Proprietà ed Esempi
## Dipendente significa «uno è combinazione degli altri»
**Proposizione.** Un insieme {v₁, …, vₙ} è linearmente dipendente se e solo se c'è un vᵢ che è combinazione lineare degli altri.

**Dimostrazione.** Se i vettori sono dipendenti, esiste una combinazione lineare λ₁v₁ + … + λₙvₙ = 0 con almeno un coefficiente λᵢ ≠ 0. Si porta vᵢ a sinistra e il resto a destra e si divide per λᵢ (che si può invertire perché 𝕂 è un campo e λᵢ ≠ 0): vᵢ = −(λ₁/λᵢ)v₁ − … − (λₙ/λᵢ)vₙ, dove a destra non compare vᵢ. Viceversa, se vᵢ è combinazione lineare degli altri, spostando tutti i termini a sinistra si ottiene una combinazione nulla in cui il coefficiente di vᵢ è 1, quindi non tutti i coefficienti sono nulli. ∎

**In parole povere:** dipendente vuol dire che almeno un vettore si può ricostruire con gli altri, quindi non aggiunge niente di nuovo. È l'idea di ridondanza dell'esempio del capitolo precedente.

Come fatto notare a lezione da uno studente, la proposizione ha senso soprattutto quando i vettori sono almeno due: con un solo vettore non ci sono «altri» di cui fare la combinazione, e il caso va trattato a parte (si veda sotto).

## Casi particolari
- **L'insieme contiene il vettore nullo.** Allora è dipendente: per esempio {v₁, v₂, 0} è dipendente perché 0 = 0·v₁ + 0·v₂ + 1·0 ha un coefficiente non nullo (il coefficiente 1 moltiplica il vettore nullo; si può scrivere anche 0·v₁ + 0·v₂ − 1·0 = 0).
- **Un vettore è multiplo di un altro.** Per esempio {v₁, v₂ = 2v₁, v₃} è dipendente, perché v₂ = 2v₁ + 0·v₃.
- **Due soli vettori.** {v₁, v₂} è linearmente dipendente se e solo se uno è multiplo dell'altro, cioè v₁ = a·v₂ oppure v₂ = a·v₁ per qualche a ∈ 𝕂 (la scelta fra le due scritture serve nel caso in cui uno dei due sia il vettore nullo). Come sottolineato a lezione, «multiplo» ha un senso preciso: due vettori sono multipli solo se uno è uguale all'altro moltiplicato per uno **scalare**, non per un'espressione qualunque (per esempio x e x² sono polinomi diversi ma non sono multipli: nessuno scalare trasforma x in x²).
- **Un solo vettore.** {v₁} è dipendente se e solo se esiste a ≠ 0 con 0 = a·v₁, cioè se e solo se v₁ = 0. Quindi **{v₁} è linearmente indipendente se e solo se v₁ ≠ 0**: un vettore diverso da zero è sempre un insieme indipendente.

Con tre o più vettori il problema è meno immediato: tre vettori possono essere a coppie non multipli e risultare comunque dipendenti nel loro insieme, come (1, 1, 0), (0, 1, 1) e (1, 0, −1) di ℝ³, che soddisfano v₁ − v₂ − v₃ = 0. Per questo la verifica si fa in generale con la definizione, come nell'esempio più sotto.

## Sottoinsiemi e insiemi più grandi
**Proposizione.**
- Se {v₁, …, vₙ} è linearmente indipendente, **ogni suo sottoinsieme** è linearmente indipendente.
- Se {v₁, …, vₙ} è un insieme di generatori, **ogni insieme che lo contiene** è un insieme di generatori.

**In parole povere:** gli insiemi indipendenti non perdono la proprietà se li si accorcia; gli insiemi di generatori non la perdono se li si allunga. Come sottolineato a lezione, per questo agli insiemi indipendenti piace essere piccoli e agli insiemi di generatori piace essere grandi: una base è il punto d'incontro, né troppo piccola né troppo grande.

**Spiegazione.** Per il primo punto, se un sottoinsieme fosse dipendente, una sua combinazione lineare nulla con coefficienti non tutti nulli si estenderebbe a tutto l'insieme aggiungendo coefficienti uguali a 0, e questo contraddirebbe l'indipendenza. Per il secondo, qualunque vettore si ottiene già con i generatori di partenza; ai vettori aggiunti si dà coefficiente 0.

Come conseguenza, se v₁, …, vₙ sono indipendenti allora sono tutti diversi da zero e sono a coppie non multipli. Queste condizioni sono necessarie ma, per n ≥ 3, **non sufficienti**: l'esempio (1, 1, 0), (0, 1, 1), (1, 0, −1) lo dimostra.

## Come si verifica l'indipendenza
Per decidere se v₁, …, vₙ sono linearmente indipendenti si chiede in quanti modi si può scrivere il vettore nullo come loro combinazione lineare: se l'unico è quello con tutti i coefficienti nulli, sono indipendenti; altrimenti sono dipendenti.

**Esempio.** Sono linearmente indipendenti v₁ = (2, 1) e v₂ = (0, 1) in ℝ²? Si scrive
(0, 0) = a·(2, 1) + b·(0, 1) = (2a, a + b),
che dà il sistema di due equazioni lineari in due incognite
- 2a = 0
- a + b = 0.

La prima equazione dà a = 0, e sostituendo nella seconda si ottiene b = 0. L'unica soluzione è a = b = 0, quindi i due vettori sono **linearmente indipendenti**. Come sottolineato a lezione, i sistemi di equazioni lineari verranno studiati più avanti, in generale; qui il sistema è banale e si risolve a mano. Con tre vettori il sistema avrebbe tre incognite, e così via.

**Esempio.** I vettori e₁ = (1, 0, 0), e₂ = (0, 1, 0), e₃ = (0, 0, 1) di ℝ³ sono indipendenti: λ₁e₁ + λ₂e₂ + λ₃e₃ = (λ₁, λ₂, λ₃) è il vettore nullo solo per λ₁ = λ₂ = λ₃ = 0.

Il capitolo successivo mostra perché le basi sono così importanti: ogni vettore dello spazio si scrive in un solo modo rispetto a una base.
