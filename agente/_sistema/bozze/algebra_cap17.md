# 17. Gli Spazi Vettoriali su un Campo
## Il campo degli scalari
Un insieme che ha due operazioni, una somma e una moltiplicazione per scalare, con le stesse proprietà di ℝ^{n}, è uno **spazio vettoriale**. Prima di darne la definizione bisogna essere precisi su un punto: gli scalari sono elementi di un campo, ma **quale** campo? Va scelto a priori. L'ordine corretto per definire uno spazio vettoriale è quindi scegliere prima il campo degli scalari, cioè i numeri per cui si vuole poter moltiplicare, e solo dopo l'insieme e le sue operazioni.

Richiamiamo la definizione di campo del capitolo 2, riformulandola con il linguaggio dei gruppi: un **campo** è un insieme dotato di due operazioni, una somma e un prodotto, tali che l'insieme sia un gruppo commutativo con la somma (elemento neutro 0), che l'insieme privato dello 0 sia un gruppo commutativo con il prodotto (elemento neutro 1) e che valga la proprietà distributiva a·(b + c) = a·b + a·c. Sono campi ℚ, ℝ e ℂ, mentre ℤ non lo è, perché 2 non ha inverso moltiplicativo.

## La definizione
**Definizione.** Fissiamo un campo 𝕂. Uno **spazio vettoriale su 𝕂** è un insieme V, i cui elementi si chiamano **vettori**, con due operazioni:
- una **somma** + : V × V → V, che a due vettori v, w associa un vettore v + w;
- una **moltiplicazione per scalare** · : 𝕂 × V → V, che a uno scalare a e a un vettore v associa un vettore a·v,

tali che siano soddisfatte:
- le proprietà 1-4 del capitolo 16, cioè (V, +) è un gruppo abeliano;
- le proprietà 5-8, dove gli scalari sono elementi di 𝕂.

Nelle dispense questo si enuncia con cinque condizioni: (V, +) è un gruppo commutativo e valgono λ(v + w) = λv + λw, (λ + μ)v = λv + μv, (λμ)v = λ(μv) e 1v = v, per ogni v, w ∈ V e λ, μ ∈ 𝕂. Sono le stesse proprietà elencate a lezione, raggruppate in modo diverso: il gruppo commutativo corrisponde alle proprietà 1-4, λ(v + w) = λv + λw alla 7, (λ + μ)v = λv + μv alla 6, (λμ)v = λ(μv) alla 5 e 1v = v alla 8. Per noi il campo 𝕂 sarà di solito ℝ oppure ℂ, ma per la definizione può essere qualsiasi campo.

L'elemento neutro del gruppo (V, +) si indica con 0_{V}, o semplicemente con 0, ed è l'**origine** dello spazio vettoriale. Non va confuso con lo zero del campo 𝕂: il simbolo 0 può indicare cose diverse e il significato si capisce dal contesto.

## I quattro ingredienti
Come sottolineato a lezione, per comunicare uno spazio vettoriale, a un collega, a un computer o a chi legge, bisogna dire quattro cose:
1. l'**insieme** V;
2. il **campo degli scalari** 𝕂;
3. come è definita la **somma**;
4. come è definita la **moltiplicazione per scalare**.

Non sono informazioni che si possono ricavare: vanno specificate, e tutte e quattro. Ovviamente le due operazioni devono soddisfare le proprietà della definizione, ma a livello di comunicazione servono tutti e quattro gli ingredienti.

## Esempi
**ℝ^{n} su ℝ.** L'insieme è ℝ^{n}, il campo è ℝ, la somma è la somma termine a termine e il prodotto per scalare moltiplica ogni componente per un numero reale (capitolo 15).

**Lo spazio ℝ[x] dei polinomi.** L'insieme è quello dei polinomi a coefficienti reali, il campo è ℝ. La somma è la somma di polinomi già vista: si sommano termine a termine i coefficienti, (a_{n}x^{n} + … + a_{1}x + a_{0}) + (b_{n}x^{n} + … + b_{1}x + b_{0}) = (a_{n} + b_{n})x^{n} + … + (a_{1} + b_{1})x + (a_{0} + b_{0}) (se i due polinomi hanno gradi diversi, si completa quello di grado minore con coefficienti nulli). Il prodotto per uno scalare reale c moltiplica ogni coefficiente per c: c·(a_{n}x^{n} + … + a_{0}) = c a_{n}x^{n} + … + c a_{1}x + c a_{0}. Con queste operazioni ℝ[x] è uno spazio vettoriale su ℝ. Un esempio con i numeri: (x³ − 2x + 1) + (4x⁴ + x − 3) = 4x⁴ + x³ − x − 2, e 3·(x³ − 2x) = 3x³ − 6x.

**Lo spazio 𝕂^{n}.** Non c'è nulla di speciale nei numeri reali: per un qualsiasi campo 𝕂 si definisce 𝕂^{n} come l'insieme delle n-uple (x_{1}, …, x_{n}) con x_{1}, …, x_{n} ∈ 𝕂. Si possono considerare, per esempio, ℂ^{n} (n-uple di numeri complessi) o ℚ^{n}. Le operazioni sono le stesse di ℝ^{n}, con la differenza importante che lo scalare a vive ora nel campo 𝕂 scelto, e non più in ℝ. Con queste operazioni 𝕂^{n} è uno spazio vettoriale su 𝕂. Alcuni esempi in ℂ²: (1 + i, −2) + (3i, 1 − i) = (1 + 4i, −1 − i), e (2 + i)·(3, 1 − i) = (6 + 3i, 3 − i).

**Lo spazio 𝕂[x] dei polinomi.** Fissato un campo 𝕂, si indica con 𝕂[x] l'insieme dei polinomi con coefficienti in 𝕂. Valgono le stesse formule di ℝ[x], con la differenza che quando si moltiplica un polinomio per uno scalare, lo scalare deve essere in 𝕂. Con queste due operazioni 𝕂[x] è uno spazio vettoriale su 𝕂.

Resta da controllare che in tutti questi esempi valgano davvero le proprietà della definizione: si fa verificando le proprietà componente per componente (o coefficiente per coefficiente), usando le proprietà del campo. Per esempio, per la proprietà 7 in 𝕂^{n}: a·(v + w) ha come componenti a(x_{i} + y_{i}), che per la distributività nel campo diventano a x_{i} + a y_{i}, cioè le componenti di a·v + a·w.
