## Insiemi numerici
D: Perché si passa da ℕ a ℤ, da ℤ a ℚ, da ℚ a ℝ e da ℝ a ℂ?
R: ℤ per sottrarre, ℚ per dividere, ℝ per colmare i "buchi" dei razionali, ℂ per risolvere equazioni senza soluzioni reali come x² + 1 = 0.

## Insiemi numerici
D: Perché √2 mostra che ℚ non basta?
R: √2 (diagonale del quadrato di lato 1) non è un rapporto di interi, per assurdo: sulla retta ci sono "buchi" non coperti dai razionali.

## Insiemi numerici
D: Operativamente, come va inteso un numero reale irrazionale come π?
R: Come un processo: una successione di approssimazioni razionali sempre più precise. Es. 2^π si approssima con 2^3,1, 2^3,14, 2^3,141, …

## Campi
D: Quali sono le 9 proprietà che definiscono un campo?
R: Somma: commutativa, associativa, neutro 0, opposto. Prodotto: commutativo, associativo, neutro 1, inverso (se a ≠ 0). Più la distributività.

## Campi
D: Vero o falso? "ℤ è un campo." Perché?
R: Falso: ha gli opposti ma non gli inversi (2 ∈ ℤ ma 1/2 ∉ ℤ). ℕ non lo è per mancanza di opposti e inversi.

## Campi
D: Quali tra ℕ, ℤ, ℚ, ℝ, ℂ sono campi?
R: ℚ, ℝ e ℂ. ℕ e ℤ no. Gli elementi del campo 𝕂 sono gli scalari degli spazi vettoriali (nel corso di solito ℝ o ℂ).

## Numeri complessi
D: Cosa sono Re(z) e Im(z) per z = a + bi? Quanto valgono per z = 2 + 3i?
R: Re(z) = a, Im(z) = b, entrambi reali: la parte immaginaria non include i. Per z = 2 + 3i: Re = 2, Im = 3 (non 3i).

## Numeri complessi
D: Cos'è un immaginario puro e come stanno ℝ e ℂ?
R: z = bi con a = 0 e b ≠ 0. I reali sono i complessi con b = 0 (ℝ ⊂ ℂ).

## Numeri complessi
D: Calcola (2 + i)(3 − 2i) in forma algebrica.
R: (2·3 − 1·(−2)) + (2·(−2) + 1·3)i = 8 − i. Si usa (a+bi)(c+di) = (ac − bd) + (ad + bc)i.

## Numeri complessi
D: Vero o falso? "Si può dire che 3 + i > 2 + 5i." Perché?
R: Falso: ℂ non ha un ordine compatibile con le operazioni (servirebbe i² = −1 > 0). Si ordinano solo moduli o parti reali.

## Coniugato, modulo, inverso
D: Definisci il coniugato z̄ e dì come si comporta con z ∈ ℝ e con doppio coniugio.
R: z̄ = a − bi. Se z ∈ ℝ allora z̄ = z; applicando il coniugio due volte si torna a z.

## Coniugato, modulo, inverso
D: Definisci |z| e dì quando si annulla.
R: |z| = √(a² + b²), reale e ≥ 0; vale 0 se e solo se z = 0.

## Coniugato, modulo, inverso
D: Quanto vale z · z̄ e perché è utile?
R: z · z̄ = a² + b² = |z|², reale non negativo. Permette di ricavare l'inverso: z⁻¹ = z̄ / |z|².

## Coniugato, modulo, inverso
D: Calcola l'inverso di z = 2 + 5i.
R: |z|² = 4 + 25 = 29, quindi z⁻¹ = (2 − 5i)/29 = 2/29 − (5/29)i.

## Coniugato, modulo, inverso
D: Calcola |3 − 4i| e (3 − 4i)(3 + 4i).
R: |3 − 4i| = √(9 + 16) = 5 e il prodotto con il coniugato vale 25 = |z|².

## Piano di Argand-Gauss
D: Come si leggono nel piano di Argand-Gauss somma, coniugato e modulo?
R: Somma: regola del parallelogramma. Coniugato: riflessione rispetto all'asse reale. Modulo: distanza dall'origine.

## Piano di Argand-Gauss
D: Perché le coordinate cartesiane non spiegano il prodotto complesso?
R: (a,b)·(c,d) = (ac − bd, ad + bc) ha un legame geometrico oscuro con i fattori; in polari i moduli si moltiplicano e gli angoli si sommano.

## Forma polare
D: Scrivi z = a + bi in forma polare e dì cosa sono r e θ.
R: z = r(cos θ + i sen θ) = r e^{iθ}, con r = |z| = √(a²+b²) e θ = Arg(z), angolo dal semiasse reale positivo in senso antiorario.

## Forma polare
D: Perché l'argomento non è unico e per quale z non è definito?
R: Si può aggiungere un giro completo: θ è definito a meno di multipli di 2π. Per z = 0 non è definito (ogni angolo va bene).

## Forma polare
D: Trabocchetto: perché θ = arctan(b/a) non basta? Cosa si fa se a < 0?
R: arctan dà solo angoli in (−π/2, π/2). Se a < 0 si aggiunge π; se a > 0 e b < 0 si aggiunge 2π (convenzione [0, 2π)).

## Forma polare
D: Scrivi z = −1 + i in forma polare.
R: r = √2, arctan(−1) = −π/4, a < 0 quindi si aggiunge π: θ = 3π/4. Dunque z = √2 e^{i3π/4}.

## Forma polare
D: Scrivi −5 in forma polare.
R: Sta sul semiasse reale negativo a distanza 5: −5 = 5e^{iπ}.

## Forma polare
D: Scrivi z = 2e^{iπ/4} in forma algebrica.
R: 2(cos π/4 + i sen π/4) = 2(√2/2 + i√2/2) = √2 + i√2.

## Forma polare
D: Quando r₁e^{iθ₁} = r₂e^{iθ₂}?
R: Se e solo se r₁ = r₂ e θ₂ = θ₁ + 2kπ per qualche k ∈ ℤ.

## Forma polare
D: Quanto valgono e^{iπ} e e^{2πi}? E cosa sono i numeri e^{iθ}?
R: e^{iπ} = −1 (identità di Eulero e^{iπ} + 1 = 0), e^{2πi} = 1. I numeri e^{iθ} sono i punti della circonferenza di raggio 1.

## Prodotto in forma polare
D: Regola del prodotto in forma polare e suo significato geometrico.
R: z₁z₂ = r₁r₂ e^{i(θ₁+θ₂)}: moduli moltiplicati, argomenti sommati. Equivale a ruotare z₁ di θ₂ e scalarlo di r₂.

## Prodotto in forma polare
D: Calcola (1 + i)² in forma polare e controlla in cartesiane.
R: 1 + i = √2 e^{iπ/4}, quindi (1+i)² = 2e^{iπ/2} = 2i. In cartesiane: 1 + 2i + i² = 2i.

## Prodotto in forma polare
D: Come sono coniugato e inverso di z = r e^{iθ} in forma polare?
R: z̄ = r e^{−iθ} (stesso modulo, angolo opposto); z⁻¹ = (1/r) e^{−iθ}. Divisione: z₁/z₂ = (r₁/r₂) e^{i(θ₁−θ₂)}.

## Potenze e radici
D: Enuncia la formula di De Moivre per zⁿ con z = r e^{iθ}.
R: zⁿ = rⁿ e^{inθ} = rⁿ(cos nθ + i sen nθ): |zⁿ| = |z|ⁿ e Arg(zⁿ) = n·Arg(z) (a meno di 2π).

## Potenze e radici
D: Calcola (1 + i)²⁰⁰⁰.
R: 1 + i = √2 e^{iπ/4}, quindi = 2¹⁰⁰⁰ e^{i500π}; 500π = 250 giri completi, e^{i500π} = 1: il risultato è 2¹⁰⁰⁰.

## Potenze e radici
D: Quante radici n-esime ha z₀ ≠ 0 e che formula le dà?
R: Esattamente n, distinte: wₖ = ⁿ√r₀ · e^{i(θ₀/n + 2kπ/n)}, k = 0, 1, …, n−1.

## Potenze e radici
D: Come sono disposte nel piano le radici n-esime di z₀?
R: Sulla circonferenza di raggio ⁿ√r₀, con angoli equidistanziati di 2π/n: vertici di un poligono regolare di n lati.

## Potenze e radici
D: Trova le radici terze di 8.
R: Modulo ³√8 = 2, angoli 2kπ/3: 2, −1 + i√3, −1 − i√3 (triangolo equilatero di raggio 2).

## Potenze e radici
D: Risolvi z³ = −8.
R: −8 = 8e^{iπ}, angoli π/3 + 2kπ/3: 1 + i√3, −2, 1 − i√3.

## Potenze e radici
D: Quali sono le soluzioni di zⁿ = 1?
R: z_k = e^{i2kπ/n}, k = 0, …, n−1: vertici del poligono regolare di raggio 1 con n lati, con un vertice in 1.

## Potenze e radici
D: Trabocchetti: la radice n-esima di un complesso è un solo numero? Si può fare per componenti?
R: No: sono n soluzioni da elencare tutte. E ⁿ√(a+bi) ≠ ⁿ√a + i ⁿ√b in generale: si passa dalla forma polare.
