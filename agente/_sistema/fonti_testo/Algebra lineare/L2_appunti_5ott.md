# Algebra lineare, lezione 2 (5 ottobre 2026): appunti a mano su quaderno
(trascrizione dell'appunto manoscritto, prof. Reto Buzano; fonte: L2_appunti_5ott.pdf, 4 pagine)

ℕ ⊊ ℤ ⊊ ℚ ⊊ ℝ ⊊ ℂ

## 2. Numeri complessi (ℂ)
**Def.** Un numero complesso z è un oggetto algebrico che si scrive come z = a + bi, dove a, b sono numeri reali. i = unità immaginaria.
Es.: 2+3i, −7+11i, √2+πi, √3 (= √3 + 0·i), −7i (= 0 − 7i).

★ L'unica regola nuova da aggiungere per fare i calcoli è: **i² = i·i = −1**.

- (a+bi) + (c+di) = (a+c) + (b+d)i
- (a+bi)·(c+di) = ac + adi + bci + bdi² = (ac − bd) + (ad + bc)i
- Ex.: z = 1 − 2i, w = 2 + 3i. z+w = 3 + i. zw = (1−2i)(2+3i) = 2 + 3i − 4i − 6i² = 8 − i.

## Proposizione (proprietà in ℂ)
1. esiste l'elemento neutro 0 per l'addizione: z+0 = 0+z = z (0 = 0+0i)
2. vale la commutativa: z+w = w+z
3. vale l'associativa: (z+w)+v = z+(w+v)
4. esiste l'opposto (−z) per ogni z ∈ ℂ: z+(−z) = 0
5. esiste l'elemento neutro 1 per la moltiplicazione: z·1 = 1·z = z (1 = 1+0·i)
6. vale la commutativa: zw = wz
7. vale l'associativa: (zw)v = z(wv)
8. esiste l'inverso z⁻¹ per ogni **z ≠ 0**: z·z⁻¹ = z⁻¹·z = 1
(+ distributiva). Dimostrazione dell'inverso → coniugio, modulo, inverso.

**Def.** Se z = a + bi ∈ ℂ, allora a = Re(z) è la parte reale e b = Im(z) è la parte immaginaria (⚠ Im(z) ∈ ℝ). Ex.: 2 + 3i = z, Re(z) = 2, Im(z) = 3 (NON 3i).

**Def.** Il coniugio (o coniugato) di z = a + bi è z̄ = a − bi. Re(z̄) = Re(z), Im(z̄) = −Im(z).
Notiamo: per z ∈ ℂ vale z ∈ ℝ ⟺ Im(z) = 0 ⟺ z̄ = z.

**Def.** Il modulo di z = a + bi ∈ ℂ è |z| = √(a²+b²) ≥ 0 (∈ ℝ).
Notiamo: z·z̄ = (a+bi)(a−bi) = a² − b²i² = a² + b² = |z|².

**Def.** L'inverso di z = a + bi ∈ ℂ è z⁻¹ = z̄/|z|² = (a−bi)/(a²+b²) = a/(a²+b²) + (−b)/(a²+b²) i.
z⁻¹ è veramente l'inverso: z·z⁻¹ = z·z̄/|z|² = |z|²/|z|² = 1.
Ex.: z = 2+5i → z⁻¹ = (2−5i)/|2+5i|² = (2−5i)/(4+25) = 2/29 − (5/29)i.

## Il piano complesso
Possiamo identificare z = a + bi ∈ ℂ con il punto di coordinate (a, b) ∈ ℝ² = {(x,y) | x,y ∈ ℝ}. (a,b) + (c,d) = (a+c, b+d): **regola del parallelogramma**.
(a,b)·(c,d) = (ac − bd, ad + bc).
Es.: (3,1)·(2,2) = (3+i)(2+2i) = 6 + 8i + 2i² (i² = −1) = 4 + 8i = (4,8). (verifica: 6 + 6i + 2i + 2i² = 4 + 8i; nel quaderno il passaggio intermedio è cancellato e riscritto)

Ex.: calcolare la parte reale e immaginaria di (2−i)/(3−2i), (2+i)⁴, 2−8i, (2+8i)/(2i).
