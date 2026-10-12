## Funzioni: definizione
D: Cosa significa "dare una funzione" f: A → B in matematica discreta?
R: Dare la tripla (A, B, Γ): dominio, codominio e grafico Γ ⊆ A × B con ∀a ∈ A ∃! b ∈ B tale che (a, b) ∈ Γ.

## Funzioni: definizione
D: Quali due condizioni può violare un Γ ⊆ A × B per non essere una funzione?
R: Esistenza (sopra qualche a ∈ A nessuna coppia) e unicità (sopra qualche a due o più coppie, valore ambiguo).

## Funzioni: definizione
D: Vero o falso? "In una funzione due elementi diversi del dominio non possono avere la stessa immagine."
R: Falso: è quello che chiede l'iniettività. La definizione richiede un solo valore per ogni a, non valori diversi.

## Funzioni: definizione
D: A = {a,b,c,d}, B = {1,2,3}, Γ = {(a,2),(b,2),(c,3),(d,1)}. È una funzione? Quanto vale f(b)?
R: Sì: sopra ogni elemento di A c'è esattamente una coppia. f(b) = 2; che il valore 2 compaia due volte non è un problema.

## Funzioni: definizione
D: Differenza tra funzione in analisi e in matematica discreta riguardo al dominio.
R: In analisi il dominio si calcola (dove l'espressione ha senso); qui è assegnato insieme alla funzione e f(a) deve esistere per ogni a del dominio scelto.

## Funzioni: definizione
D: Nel disegno con le frecce (Venn), come si vede che non è una funzione?
R: Se da un punto di A non parte nessuna freccia (manca l'esistenza) o ne partono due o più (manca l'unicità).

## Funzioni: uguaglianza
D: Quando due funzioni f = (A,B,Γ) e g = (A′,B′,Γ′) sono uguali?
R: Se e solo se coincidono tutti e tre: A = A′, B = B′ e Γ = Γ′. Non bastano la stessa espressione né gli stessi valori.

## Funzioni: uguaglianza
D: Su {0,1,2} sia f(x) = 3x² − 1 e g(x) = x³ + 2x − 1. Sono uguali? Perché?
R: Sì: f(0)=g(0)=−1, f(1)=g(1)=2, f(2)=g(2)=11. Stesso dominio, codominio e grafico, anche se le espressioni sono diverse.

## Funzioni: uguaglianza
D: Le stesse f(x) = 3x² − 1 e g(x) = x³ + 2x − 1 sono uguali come funzioni ℝ → ℝ? Perché?
R: No: ad esempio f(3) = 26 ma g(3) = 32, quindi i grafici su ℝ sono diversi. Su {0,1,2} diventano uguali.

## Funzioni: uguaglianza
D: Trabocchetto d'esame: perché non basta assegnare una funzione con la sola espressione?
R: Per studiare iniettività e suriettività servono dominio e codominio: cambiandoli, la stessa espressione dà funzioni con proprietà diverse.

## Funzioni notevoli
D: Definisci la funzione identità id_A e il suo grafico.
R: id_A: A → A, id_A(a) = a. Il grafico è la diagonale Δ = {(a, a) | a ∈ A}.

## Funzioni notevoli
D: Definisci la funzione costante f_β: A → B e come appare il grafico per funzioni numeriche.
R: f_β(a) = β per ogni a ∈ A, con β ∈ B fissato. Per le funzioni numeriche il grafico è una retta orizzontale.

## Funzioni notevoli
D: Definisci le proiezioni p1 e p2 su A × B.
R: p1: A × B → A con p1(a, b) = a; p2: A × B → B con p2(a, b) = b. Proiettano il punto sull'asse delle ascisse e delle ordinate.

## Funzioni notevoli
D: Cos'è l'inclusione canonica j: S → A e quando coincide con id_A?
R: Per S ⊆ A, j(s) = s per ogni s ∈ S. Se S = A coincide con id_A.

## Funzioni notevoli
D: Che cos'è una successione in termini di funzioni?
R: Una funzione a: ℕ → ℝ, n ↦ aₙ (dominio ℕ, codominio ℝ). Un esempio è la successione di Fibonacci.

## Funzioni: restrizione
D: Definisci la restrizione f|S di f: A → B a S ⊆ A.
R: f|S: S → B con f|S(s) = f(s). Stessi valori ma dominio ridotto, quindi è una funzione diversa da f.

## Funzioni: restrizione
D: Vero o falso? "Due funzioni diverse hanno sempre restrizioni diverse."
R: Falso: f(x) = 3x² − 1 e g(x) = x³ + 2x − 1 sono diverse su ℝ ma uguali ristrette a S = {0, 1, 2}.

## Funzioni sul quoziente
D: Qual è il rischio quando si definisce una funzione sull'insieme quoziente tramite un rappresentante?
R: La classe si scrive in molti modi ([3] = [5] = [7]); se il risultato dipende dal rappresentante scelto, la regola non è una funzione.

## Funzioni sul quoziente
D: Cosa va verificato per dire che una regola su Q = A/R è ben definita?
R: Che se x ∼ y la regola dia la stessa classe su x e su y: il risultato non deve cambiare cambiando rappresentante.

## Funzioni sul quoziente
D: Classi in ℕ per numero di cifre. Perché F([x]) = [2x] non è una funzione? Controesempio.
R: 3 ∼ 8 (una cifra) ma F([3]) = [6] ≠ [16] = F([8]) (due cifre). Raddoppiare non rispetta l'equivalenza.

## Funzioni sul quoziente
D: Come sottolineato a lezione, qual è la prima domanda davanti a una funzione definita "sulla classe di x" da una formula?
R: Se il risultato dipende dal rappresentante scelto. A lezione è stato indicato come il punto concettualmente più difficile.

## Funzioni: immagine e controimmagine
D: Definisci f(S) e f⁻¹(T) per S ⊆ A e T ⊆ B.
R: f(S) = {f(s) | s ∈ S} ⊆ B; f⁻¹(T) = {a ∈ A | f(a) ∈ T} ⊆ A.

## Funzioni: immagine e controimmagine
D: Cos'è la fibra di b ∈ B? E cosa significa la notazione f⁻¹(b)?
R: f⁻¹(b) = {a ∈ A | f(a) = b}, un insieme (non un elemento). Esiste per ogni funzione, anche non invertibile.

## Funzioni: immagine e controimmagine
D: Vero o falso? "Se S ≠ ∅ allora f(S) ≠ ∅, e se T ≠ ∅ allora f⁻¹(T) ≠ ∅." Perché?
R: La prima è vera. La seconda è falsa: f⁻¹(T) è vuota se nessun elemento di A va in T.

## Funzioni: immagine e controimmagine
D: f: ℝ → ℝ, f(x) = x². Calcola f⁻¹(9), f⁻¹(0) e f⁻¹(−4).
R: f⁻¹(9) = {−3, 3}, f⁻¹(0) = {0}, f⁻¹(−4) = ∅ (nessun reale ha quadrato negativo).

## Funzioni: immagine e controimmagine
D: f: ℝ → ℝ, f(x) = x². Calcola f⁻¹([0, 4]) e f⁻¹([−1, 4]).
R: Entrambe uguali a [−2, 2]: la parte [−1, 0) non viene mai raggiunta, quindi non aggiunge nulla.

## Funzioni: immagine e controimmagine
D: f: ℝ → ℝ, f(x) = x². Calcola f([−2, 3]) e f({−1, 0, 2}).
R: f([−2, 3]) = [0, 9] (il minimo 0 è raggiunto in 0, il massimo 9 in 3); f({−1, 0, 2}) = {0, 1, 4}.

## Funzioni: immagine e controimmagine
D: Con f(a)=f(b)=2, f(c)=3, f(d)=1 su A = {a,b,c,d}, calcola f⁻¹(2) e f⁻¹(1).
R: f⁻¹(2) = {a, b} e f⁻¹(1) = {d}. La controimmagine di un elemento può avere più elementi.

## Funzioni: immagine e controimmagine
D: Perché calcolare una controimmagine è più difficile che calcolare un'immagine?
R: L'immagine si ottiene sostituendo; la controimmagine richiede di risolvere f(x) = y nell'incognita x, a volte impossibile in forma esplicita.

## Funzioni: iniettiva, suriettiva, biettiva
D: Definisci f suriettiva in due modi equivalenti (con f(A) e con le fibre).
R: f(A) = B, ovvero ∀b ∈ B ∃a ∈ A con f(a) = b; equivalentemente ∀b ∈ B vale f⁻¹(b) ≠ ∅.

## Funzioni: iniettiva, suriettiva, biettiva
D: Definisci f iniettiva a parole, con le implicazioni e con le fibre.
R: Elementi distinti hanno immagini distinte: a₁ ≠ a₂ ⟹ f(a₁) ≠ f(a₂); equivalentemente |f⁻¹(b)| ≤ 1 per ogni b ∈ B.

## Funzioni: iniettiva, suriettiva, biettiva
D: Come si dimostra che f NON è iniettiva? E che non è suriettiva?
R: Iniettiva: basta un controesempio, a₁ ≠ a₂ con f(a₁) = f(a₂). Suriettiva: basta un b ∈ B senza controimmagine.

## Funzioni: iniettiva, suriettiva, biettiva
D: Definisci f biettiva con le fibre.
R: È iniettiva e suriettiva, cioè |f⁻¹(b)| = 1 per ogni b ∈ B: ogni elemento del codominio ha esattamente una controimmagine.

## Funzioni: iniettiva, suriettiva, biettiva
D: f(x) = x² da ℝ in ℝ è iniettiva? Suriettiva? Motiva con numeri.
R: Né l'una né l'altra: f(−1) = f(1) = 1 e f⁻¹(−4) = ∅, quindi Im(f) = [0, +∞) ≠ ℝ.

## Funzioni: iniettiva, suriettiva, biettiva
D: Come sottolineato a lezione, cosa si deve fare prima di dire se f è iniettiva o suriettiva?
R: Leggere con cura dominio e codominio: la stessa espressione può essere suriettiva o no secondo l'insieme di arrivo, iniettiva o no secondo quello di partenza.

## Funzioni: iniettiva, suriettiva, biettiva
D: h: ℤ → ℤ, h(n) = 2n + 1: iniettiva? suriettiva? Perché?
R: Iniettiva (2n₁+1 = 2n₂+1 ⟹ n₁ = n₂). Non suriettiva: l'immagine sono i dispari, quindi h⁻¹(2) = ∅.

## Funzioni: iniettiva, suriettiva, biettiva
D: La prima proiezione p1: A × B → A (B non vuoto) è iniettiva? Suriettiva?
R: Suriettiva (dato a si prende (a, b) con b ∈ B qualsiasi). Non iniettiva, es. (1,2) ≠ (1,5) ma p1 = 1; lo è solo se |B| = 1.

## Funzioni: iniettiva, suriettiva, biettiva
D: Perché f(x) = ax + b (a ≠ 0) è biettiva su ℝ, mentre f(x) = 2x + 1 non è suriettiva su ℤ?
R: Su ℝ x = (y − b)/a risolve f(x) = y. Su ℤ la divisione per a esce dagli interi: 2x + 1 è sempre dispari, quindi 2 non è raggiunto.

## Funzioni: rendere biettiva
D: Come si rende biettiva f(x) = x² partendo da ℝ → ℝ?
R: Codominio ridotto a [0, +∞) (diventa suriettiva), poi dominio ristretto a [0, +∞) (iniettiva): q: ℝ≥0 → ℝ≥0 è biettiva.

## Funzioni: rendere biettiva
D: Come sottolineato a lezione, come va scelta la parte di dominio da scartare per ottenere l'iniettività?
R: La scelta è convenzionale ma va fatta in modo consistente (es. tutte le soluzioni negative), non scartando elementi a caso.

## Funzioni: composizione e inverse
D: Definisci g ∘ f e in che ordine si applicano le funzioni. Quando è definita?
R: (g ∘ f)(a) = g(f(a)): prima f, poi g. Serve che il codominio di f coincida con il dominio di g.

## Funzioni: composizione e inverse
D: Con f(x) = x² e g(x) = x + 1 su ℝ, calcola g ∘ f e f ∘ g in x = 1. Cosa dimostra?
R: (g ∘ f)(1) = 1² + 1 = 2, (f ∘ g)(1) = (1 + 1)² = 4: la composizione non è commutativa.

## Funzioni: composizione e inverse
D: Quali proprietà ha la composizione rispetto ad associatività e identità?
R: Associativa: h ∘ (g ∘ f) = (h ∘ g) ∘ f. Neutro: f ∘ id_A = f = id_B ∘ f. Non è commutativa.

## Funzioni: composizione e inverse
D: Se f: A → B e g: B → A con A ≠ B, g ∘ f e f ∘ g sono la stessa funzione?
R: No: g ∘ f è una funzione da A in A, f ∘ g da B in B; hanno dominio e codominio diversi.

## Funzioni: composizione e inverse
D: Cosa si conserva componendo funzioni iniettive o suriettive?
R: Se f e g sono iniettive, g ∘ f è iniettiva; se f e g sono suriettive, g ∘ f è suriettiva.

## Funzioni: composizione e inverse
D: Se g ∘ f è iniettiva (suriettiva), cosa si deduce?
R: Se g ∘ f è iniettiva, f è iniettiva (la prima). Se g ∘ f è suriettiva, g è suriettiva (la seconda).

## Funzioni: composizione e inverse
D: Se g ∘ f è biettiva, f e g lo sono? Controesempio.
R: No: f è iniettiva e g suriettiva. Es. f: {0} → {0,1}, f(0) = 0, g: {0,1} → {0} costante: g ∘ f biettiva, f non suriettiva, g non iniettiva.

## Funzioni: composizione e inverse
D: Quando f: A → B è invertibile e cosa dice il teorema fondamentale?
R: Se esiste g: B → A con g ∘ f = id_A e f ∘ g = id_B. f è invertibile se e solo se è biettiva; allora g = f⁻¹ è unica.

## Funzioni: composizione e inverse
D: Trabocchetto: differenza tra f⁻¹ funzione inversa e f⁻¹(T) controimmagine.
R: f⁻¹(T) esiste per ogni funzione e dà un sottoinsieme di A; la funzione inversa f⁻¹ esiste solo se f è biettiva.

## Funzioni: composizione e inverse
D: Qual è l'inversa di k(x) = x³ da ℝ in ℝ? E h(n) = 2n + 1 da ℤ in ℤ è invertibile?
R: k è biettiva e k⁻¹(x) = ∛x. h non è suriettiva, quindi non è biettiva e non è invertibile.
