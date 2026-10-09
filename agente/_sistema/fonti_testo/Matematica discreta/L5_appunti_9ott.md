# Appunti a mano, 9 ottobre (Mate discreta, lezione 5) — trascrizione

## p.1 — Iniettività, suriettività, biettività (esempi)
f : A → B.
- Def: f si dice **iniettiva** se ∀ a₁, a₂ ∈ A: a₁ ≠ a₂ ⟹ f(a₁) ≠ f(a₂).
- Def: f si dice **biettiva** se è contemporaneamente iniettiva e suriettiva.

Esempi:
1. id_A : A → A, a ↦ a, è biettiva: a ≠ a′ ⟹ id_A(a) ≠ id_A(a′) (id_A(a) = a).
2. Proiezione p₁ : A × B → A, (a, b) ↦ a: NON iniettiva: (a, b) ≠ (a′, b′) non implica p₁(a, b) ≠ p₁(a′, b′) (si può avere la stessa a, "b qualsiasi"). Disegno: nel piano la proiezione sull'asse.
3. f : ℝ → ℝ, f(x) = ax + b con a, b costanti, a ≠ 0.
   - Iniettività: x, y con ax + b = ay + b ⟹ ax = ay ⟹ (a ≠ 0) x = y.
   - Suriettività: y ∈ ℝ; esiste x ∈ ℝ con f(x) = y? y = ax + b ⟹ x = (1/a)(y − b). **SUR**.
4. a, b ∈ ℤ, f : ℤ → ℤ, f(x) = 2x + 1: INI ✓. Non suriettiva: esiste x con f(x) = 2? Sarebbe x = 1/2, che non è un numero intero.
5. f : ℝ → ℝ, f(x) = x²: NO suriettiva, perché ad es. x² = −1 non ha soluzione.
6. f : ℝ → ℝ^{≥0}, f(x) = x²: SUR se y ≥ 0 (x² = y ha soluzione, ad es. x = √y). NO iniettiva perché ad es. (−1)² = 1² = 1.
7. S = ℝ^{≥0}, restrizione f|_S : ℝ^{≥0} → ℝ^{≥0}: **biettiva**. (Disegno della parabola con le rette orizzontali.)

## p.2 — Seno, composizione
- sen : ℝ → ℝ; sen : ℝ → [−1, 1]; sen : [−π/2, π/2] → [−1, 1] è **biettiva**.
- Composizione: A →f B →g C, a ↦ f(a) ↦ g(f(a)); (g ∘ f)(a) = g(f(a)).
- A →f B →g C →h D: a ↦ f(a) ↦ g(f(a)) ↦ h(g(f(a))): h ∘ g ∘ f. È vero che h ∘ (g ∘ f) = (h ∘ g) ∘ f? Prendo a ∈ A. Calcolo (h ∘ (g ∘ f))(a) = h((g ∘ f)(a)); ((h ∘ g) ∘ f)(a) = (h ∘ g)(f(a)). [Nota dell'autore: "COMPLETARE FOTO 10:06 circa" — la dimostrazione dell'associatività è incompleta negli appunti.]
- Esempio non commutatività: A = ℝ, f(x) = x², g(x) = x + 1: (g ∘ f)(x) = x² + 1; (f ∘ g)(x) = (x + 1)².
- Elemento neutro: f ∘ id_A = f perché (f ∘ id_A)(a) = f(id_A(a)) = f(a); id_B ∘ f = f perché (id_B ∘ f)(a) = id_B(f(a)) = f(a).

**Proposizione.** Siano f : A → B, g : B → C due funzioni.
1. Se f e g sono iniettive, allora g ∘ f è iniettiva.
2. Se f e g sono suriettive, allora g ∘ f è suriettiva.

Dimostrazione. g ∘ f : A → C.
1. Siano a₁ ≠ a₂ ∈ A. f(a₁) ≠ f(a₂) perché f è INI; g(f(a₁)) ≠ g(f(a₂)) perché g è INI; quindi (g ∘ f)(a₁) ≠ (g ∘ f)(a₂).
2. Devo controllare che ∀ y ∈ C ∃ x ∈ A t.c. g(f(x)) = (g ∘ f)(x) = y. So che g è SUR ⟹ ∃ b ∈ B t.c. g(b) = y. So che f è SUR ⟹ ∃ x ∈ A t.c. f(x) = b. Allora (g ∘ f)(x) = g(f(x)) = g(b) = y.

## p.3 — Proposizione inversa
**Prop.** Siano f : A → B, g : B → C due funzioni. Allora:
1. se g ∘ f è iniettiva, allora f è iniettiva;
2. se g ∘ f è suriettiva, allora g è suriettiva.

Dimostrazione.
1. Voglio vedere che se f NON è iniettiva allora g ∘ f non può essere iniettiva. f non INI ⟹ ∃ a₁ ≠ a₂ con f(a₁) = f(a₂). Allora g(f(a₁)) = g(f(a₂)), cioè (g ∘ f)(a₁) = (g ∘ f)(a₂).
2. Siccome g ∘ f è SUR: ∀ y ∈ C ∃ x t.c. (g ∘ f)(x) = y, cioè g(f(x)) = y. Chiamo b = f(x): g(b) = y. ✓

**Quindi:** se g ∘ f è biettiva, allora f è iniettiva e g è suriettiva. (∗)

Supponiamo di avere due funzioni A →f B →g A tali che g ∘ f = id_A e f ∘ g = id_B. Applico (∗):
- id_A biettiva ⟹ f è INI, g è SUR;
- id_B biettiva ⟹ f è SUR, g è INI.

**Quindi:** questa situazione può capitare solo se f e g sono entrambe biettive. Quando capita dirò che f e g sono **funzioni inverse** l'una dell'altra.
