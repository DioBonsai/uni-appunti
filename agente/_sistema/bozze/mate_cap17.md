# 17. Rendere Biettiva una Funzione: Cambiare Codominio e Dominio
## L'idea generale
Una funzione definita da un'espressione può non essere né iniettiva né suriettiva, ma spesso si può **ritoccare** la funzione, cambiando l'insieme di arrivo e quello di partenza, fino a ottenerne una biettiva. Si procede in due passi: prima si **riduce il codominio** a ciò che la funzione raggiunge davvero, e la funzione diventa suriettiva; poi si **restringe il dominio**, scartando alcuni elementi in modo consistente, fino a rendere la funzione iniettiva.

In linea di principio questo si può fare per qualsiasi funzione. Il prezzo è che a ogni passo si ottiene una funzione diversa da quella di partenza (capitolo 10), con le stesse regole di calcolo ma con proprietà diverse.

## Esempio: f(x) = x²
Come già visto nel capitolo 14, f : ℝ → ℝ, f(x) = x² non è suriettiva: l'equazione x² = −1 non ha soluzioni, quindi i numeri negativi non sono mai immagine di nulla. Basta trovare **un solo** elemento fuori dall'immagine per concludere che una funzione non è suriettiva.

**Passo 1: ridurre il codominio.** Poiché i quadrati sono sempre maggiori o uguali a zero, possiamo pensare f come funzione da ℝ in ℝ^{≥0} = [0, +∞). Ora è suriettiva: se y ≥ 0, l'equazione x² = y ha soluzione, per esempio x = √y (la radice quadrata esiste sempre per y ≥ 0).

**Non è ancora iniettiva:** (−1)² = 1² = 1, quindi due numeri diversi come −1 e 1 hanno la stessa immagine, in contrasto con la definizione.

**Passo 2: restringere il dominio.** Graficamente la mancanza di iniettività si vede dal fatto che ogni valore positivo ha due soluzioni, una positiva e una negativa. Per ottenere l'iniettività bisogna sceglierne una e scartare l'altra; il modo di scegliere deve essere **consistente**, non a caso. Come sottolineato a lezione, la scelta è convenzionale ma va fatta in modo consistente, non scartando elementi a caso. Una scelta possibile è eliminare tutte le soluzioni negative: S = ℝ^{≥0}, e si considera la restrizione f|_{S} : ℝ^{≥0} → ℝ^{≥0}. Resta suriettiva (per ogni y ≥ 0 c'è una radice non negativa) e ora è anche iniettiva: è quindi **biettiva**.

## Esempio: la funzione seno
Il grafico del seno è un'onda periodica.
- sen : ℝ → ℝ non è suriettiva (il grafico è tutto contenuto tra −1 e 1, quindi un valore come 2 non viene mai raggiunto) e non è iniettiva (una retta orizzontale a quota tra −1 e 1 incontra la curva in tanti punti: tanti valori di x danno lo stesso valore del seno).
- Primo passo, come per x²: il seno assume solo valori in [−1, 1], quindi lo si considera come sen : ℝ → [−1, 1], che è suriettiva.
- Secondo passo: serve una scelta, e la più comune è l'intervallo [−π/2, π/2], dove il seno va da −1 a 1. Sulla porzione centrale del grafico una retta orizzontale incontra la curva al più in un punto: sen : [−π/2, π/2] → [−1, 1] è **biettiva**.

Un discorso analogo si fa per il coseno (che ha lo stesso grafico traslato) e per la tangente. Nella tangente, che ha asintoti, non si prende un intervallo chiuso ma l'intervallo aperto (−π/2, π/2) come dominio e tutta la retta come codominio: la funzione risulta biettiva.

Sono costruzioni che si conoscono già, anche se non in questa forma. Funzioni iniettive e suriettive le incontreremo man mano nel corso.
