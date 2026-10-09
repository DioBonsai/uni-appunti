# 15. Composizione e Invertibilità
## La funzione composta
Siano f : A → B e g : B → C due funzioni, in modo che il codominio di f coincida con il dominio di g (in generale basta che il codominio di f sia contenuto nel dominio di g). La **composizione** è la funzione g ∘ f : A → C definita da

(g ∘ f)(a) = g(f(a)) per ogni a ∈ A.

Prima si applica f, poi g: la scrittura va letta da destra a sinistra.

Proprietà:
- **associatività**: se h : C → D, allora h ∘ (g ∘ f) = (h ∘ g) ∘ f;
- **elemento neutro**: f ∘ id_{A} = f e id_{B} ∘ f = f;
- **non commutatività**: in generale g ∘ f ≠ f ∘ g, e spesso f ∘ g non è nemmeno definibile.

Un esempio: con f(x) = x² e g(x) = x + 1 da ℝ in ℝ si ha (g ∘ f)(x) = x² + 1, mentre (f ∘ g)(x) = (x + 1)² = x² + 2x + 1, che sono funzioni diverse.

## Funzione invertibile
Una funzione f : A → B è **invertibile** se esiste g : B → A tale che g ∘ f = id_{A} e f ∘ g = id_{B}. Vale il teorema fondamentale:

**f è invertibile se e solo se f è biettiva.**

Se f è biettiva, la funzione g è unica; si chiama **funzione inversa**, si indica con f^{-1} : B → A ed è definita da f^{-1}(b) = a ⟺ f(a) = b. Per esempio k(x) = x³ da ℝ in ℝ è biettiva e la sua inversa è k^{-1}(x) = ∛x, mentre h(n) = 2n + 1 da ℤ in ℤ non è biettiva (non è suriettiva), quindi non è invertibile.

Non va confusa la funzione inversa f^{-1} (che esiste solo se f è biettiva) con la controimmagine f^{-1}(T) del capitolo 13, che si può calcolare per qualunque funzione.
