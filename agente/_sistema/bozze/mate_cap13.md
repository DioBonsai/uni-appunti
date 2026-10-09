# 13. Immagine e Controimmagine
## L'immagine di un elemento e di un sottoinsieme
Sia f : A → B una funzione e a ∈ A. Il valore b = f(a) si chiama **immagine di a**. Il termine non indica necessariamente un numero: è un elemento del codominio, qualunque sia la natura degli insiemi. Per la funzione "quadrato", per esempio, 4 è l'immagine di 2 e 9 è l'immagine di 3.

La nozione si estende ai sottoinsiemi. Se S ⊆ A, si calcola f su tutti gli elementi di S e si ottiene

f(S) = {f(s) | s ∈ S} = {b ∈ B | ∃ s ∈ S tale che f(s) = b} ⊆ B,

cioè un sottoinsieme del **codominio**, non di S. Questo insieme è l'**immagine di S**. Nel caso S = A si ottiene f(A), detta **immagine (totale)** della funzione e indicata anche con Im(f).

## La controimmagine
Si può percorrere la strada inversa: partire dal codominio e chiedersi quali elementi del dominio finiscono lì. Per un sottoinsieme T ⊆ B si definisce la **controimmagine** (o immagine inversa)

f^{-1}(T) = {a ∈ A | f(a) ∈ T} ⊆ A.

Se T = {b} ha un solo elemento si scrive f^{-1}(b) = {a ∈ A | f(a) = b}, detta **fibra** di b. Attenzione alla notazione: f^{-1}(T) esiste per qualunque funzione e **non** significa che f sia invertibile (l'inversa si vedrà nel capitolo 15).

## La differenza fondamentale
Un singolo elemento del dominio ha **un'unica** immagine, perché una funzione assume un valore e uno solo su ogni elemento. Un singolo elemento del codominio, invece, può avere **tanti** elementi che lo hanno per immagine. Per questo la controimmagine di un elemento è un **sottoinsieme** di A, non un elemento di A. La scrittura f^{-1}(b) va sempre letta come un insieme.

Due proprietà legate a questo fatto vanno ricordate bene:
- se S ≠ ∅, allora f(S) ≠ ∅: l'immagine di un insieme non vuoto non è mai vuota;
- al contrario, f^{-1}(T) può essere vuota anche se T ≠ ∅, se nessun elemento di A viene mandato in T.

Poter avere l'insieme vuoto come risultato evita casi particolari: la controimmagine è sempre definita.

## Esempio: la parabola f(x) = x²
Sia f : ℝ → ℝ, f(x) = x². Il grafico è una parabola con vertice nell'origine. Per l'immagine si prende un punto sull'asse x, si guarda il grafico e si proietta sull'asse y. Per la controimmagine si fa il contrario: si parte da un punto b del codominio, si traccia la retta orizzontale e si proiettano sull'asse x i punti in cui incontra il grafico. Tre casi:
- se b > 0: f^{-1}(b) = {−√b, √b}, due elementi;
- se b = 0: f^{-1}(0) = {0}, un solo elemento;
- se b < 0: f^{-1}(b) = ∅, perché nessun numero reale ha quadrato negativo.

Anche per i sottoinsiemi il ragionamento regge. Per T = [0, 4]: x² ∈ [0, 4] equivale a −2 ≤ x ≤ 2, quindi f^{-1}([0, 4]) = [−2, 2]. Per T = [−1, 4] il risultato è lo stesso, [−2, 2]: la parte [−1, 0) del sottoinsieme non viene mai raggiunta dalla funzione, perché i quadrati sono sempre non negativi, quindi non aggiunge nulla.

## Calcolare immagini e controimmagini
Calcolare un'immagine, quando si ha un'espressione, significa sostituire il valore nell'espressione. Calcolare una controimmagine è più difficile: bisogna **risolvere l'equazione** f(x) = y nell'incognita x, e in certi casi risolverla può essere impossibile da fare esplicitamente. Il caso è concettualmente più difficile anche quando le funzioni non sono numeriche: se a ogni persona di un gruppo associamo la sua altezza in centimetri, la controimmagine di 170 è il sottoinsieme delle persone del gruppo alte esattamente 170 cm, che può avere molti elementi, uno solo o nessuno.

Con queste due nozioni possiamo classificare le funzioni in base a come "coprono" il codominio e a come si comportano su elementi distinti.
