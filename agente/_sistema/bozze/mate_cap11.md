# 11. Funzioni Notevoli, Successioni e Restrizione
## Le funzioni che ricorrono sempre
Esiste un piccolo elenco di funzioni standard che conviene conoscere, perché compaiono continuamente, spesso in modo implicito. Per definirle indichiamo a parole come si comporta il valore invece di scrivere esplicitamente il grafico Γ, che sarebbe macchinoso: è però importante ricordare che dietro c'è sempre la tripla (A, B, Γ).

## Funzione identità
Per ogni insieme A, la **funzione identità** id_{A} : A → A è definita da id_{A}(a) = a per ogni a ∈ A. Il pedice A serve perché l'identità esiste per qualunque insieme. Nell'immagine della scatola è quella che restituisce l'oggetto in entrata tale e quale, senza fargli nulla. Il suo grafico è la **diagonale** Δ = {(a, a) | a ∈ A}.

## Funzione costante
Si scelgono due insiemi A e B e un elemento β ∈ B fissato. La **funzione costante** f_{β} : A → B è definita da f_{β}(a) = β per ogni a ∈ A: qualunque cosa si inserisca nella scatola, esce sempre β. Per le funzioni numeriche il grafico è una retta orizzontale.

## Proiezioni
Dati A e B, sul prodotto cartesiano A × B si definiscono due funzioni:
- la **prima proiezione** p_{1} : A × B → A, con p_{1}(a, b) = a (restituisce la prima componente della coppia);
- la **seconda proiezione** p_{2} : A × B → B, con p_{2}(a, b) = b (restituisce la seconda componente).

Il nome viene dal piano cartesiano: p_{1} proietta il punto di coordinate (a, b) sull'asse delle ascisse, p_{2} sull'asse delle ordinate. Con un prodotto di più insiemi A × B × C si hanno anche la terza proiezione, la quarta e così via: in generale, per le n-uple, restituiscono una coordinata fissata, come le componenti di un vettore.

## Inclusione canonica
Se S ⊆ A, l'**inclusione canonica** j : S → A è definita da j(s) = s per ogni s ∈ S. Manda ogni s in sé stesso; se S = A coincide con id_{A}.

## Le successioni come funzioni
Una **successione** è una lista di numeri a_{0}, a_{1}, a_{2}, … (si può partire da 0 o da 1, è irrilevante). Assegnare una successione di numeri reali significa assegnare un valore reale a 0, uno a 1, uno a 2 e così via, cioè definire una funzione

a : ℕ → ℝ, n ↦ a_{n}.

Dunque una successione non è altro che una funzione con dominio ℕ e codominio ℝ. Un esempio di successione è quella di Fibonacci.

## La restrizione di una funzione
Sia f : A → B una funzione e sia S ⊆ A un sottoinsieme del dominio. Poiché gli elementi di S sono particolari elementi di A, f assume un valore anche su di essi. Possiamo allora definire una **nuova funzione** f|_{S} : S → B, la **restrizione di f a S**, con la stessa regola di prima: f|_{S}(s) = f(s) per ogni s ∈ S.

Si sta restringendo il dominio, lasciando invariati i valori; ma dal punto di vista concettuale **f|_{S} è una funzione diversa da f**, perché ha un dominio diverso (si ricordi il criterio di uguaglianza del capitolo 10).

## Funzioni diverse con restrizioni uguali
Non è vero che due funzioni diverse restano diverse dopo la restrizione. Riprendiamo l'esempio del capitolo 10: le espressioni f(x) = 3x² − 1 e g(x) = x³ + 2x − 1 sono definite per ogni numero reale e, come funzioni su ℝ, sono diverse (hanno grafici diversi). Se però le restringiamo a S = {0, 1, 2}, diventano uguali: f|_{S} = g|_{S}.

Lo stesso accade graficamente con due funzioni reali i cui grafici coincidono solo su un intervallo [a, b]: sono diverse su ℝ, ma se le restringiamo a S = [a, b] si ottengono due funzioni uguali. Non è detto che succeda: è una possibilità, e vedremo più avanti perché a volte conviene restringere il dominio apposta.

Il prossimo capitolo affronta una questione molto più delicata, che riguarda le funzioni definite su un insieme quoziente.
