# 9. Potenze e Radici n-esime di un Numero Complesso
## Le potenze in forma polare
Il prodotto in forma polare rende banale il calcolo delle potenze. Se z = r e^{iθ} e n ≥ 1 è un numero naturale, elevare z alla n significa moltiplicare r per se stesso n volte (si ottiene r^{n}) e sommare θ a se stesso n volte (si ottiene nθ):

z^{n} = (r e^{iθ})^{n} = r^{n} e^{inθ} = r^{n} (cos nθ + i sen nθ)

Questa è la **formula di De Moivre** (nei testi classici il nome indica il caso r = 1, ma la struttura è la stessa). Ne seguono due regole:
- |z^{n}| = |z|^{n}, cioè il modulo si eleva alla n;
- Arg(z^{n}) = n · Arg(z), cioè l'argomento si moltiplica per n (come sempre, a meno di multipli di 2π).

**Esempio.** Calcoliamo (1 + i)^{2000}, che in forma cartesiana sarebbe impraticabile. Poiché 1 + i = √2 e^{iπ/4}:

(1 + i)^{2000} = (√2)^{2000} e^{i · 2000π/4} = 2^{1000} e^{i · 500π}

Ora 500π = 250 · 2π è un multiplo intero di 2π, quindi e^{i · 500π} = 1 e il risultato è (1 + i)^{2000} = 2^{1000}.

## Le radici n-esime: il problema
Dato z_{0} ∈ ℂ, diciamo che w ∈ ℂ è una **radice n-esima** di z_{0} se w^{n} = z_{0}. Vedremo che, per z_{0} ≠ 0, le radici n-esime sono **esattamente n**, tutte distinte. (Per z_{0} = 0 l'unica radice è w = 0.)

## Come si trovano
Sia z_{0} = r_{0} e^{iθ_{0}} ≠ 0 e cerchiamo w = r e^{iθ} tale che w^{n} = z_{0}. Per la formula delle potenze l'equazione diventa:

r^{n} e^{inθ} = r_{0} e^{iθ_{0}}

Per quanto visto nel capitolo 7, due forme polari rappresentano lo stesso numero se e solo se hanno lo stesso modulo e angoli che differiscono per un multiplo di 2π. Si ottengono quindi due condizioni:
- sul modulo, r^{n} = r_{0}, da cui r = ⁿ√r_{0}, dove con il simbolo ⁿ√r_{0} si intende la radice reale positiva del numero reale positivo r_{0};
- sull'angolo, nθ = θ_{0} + 2kπ per qualche k ∈ ℤ, da cui θ = θ_{0}/n + 2kπ/n.

Al variare di k gli angoli crescono ogni volta di 2π/n. Le soluzioni distinte sono esattamente quelle con k = 0, 1, …, n − 1, per due motivi:
- due indici diversi j ≠ k in {0, …, n − 1} danno angoli che differiscono di 2π(j − k)/n, e poiché 0 < |j − k| < n questa differenza non è un multiplo intero di 2π: i numeri ottenuti sono diversi;
- ogni altro intero k si scrive come k = qn + s con 0 ≤ s < n, e l'angolo corrispondente è quello di s più q giri completi: si ritrova quindi la radice con indice s.

Le radici sono dunque le n soluzioni:

w_{k} = ⁿ√r_{0} · e^{i(θ_{0}/n + 2kπ/n)}, per k = 0, 1, …, n − 1

**Interpretazione geometrica.** Le n radici hanno tutte lo stesso modulo ⁿ√r_{0}, quindi stanno su una circonferenza centrata nell'origine, e i loro angoli sono equidistanziati di 2π/n. Sono quindi i **vertici di un poligono regolare** con n lati.

## Esempi
**Radici terze di 8.** Qui z_{0} = 8 = 8 e^{i·0}, quindi r_{0} = 8, θ_{0} = 0 e n = 3. Il modulo delle radici è ³√8 = 2 e gli angoli sono 2kπ/3:
- k = 0: w_{0} = 2 e^{i·0} = 2;
- k = 1: w_{1} = 2 e^{i2π/3} = 2 (−1/2 + i √3/2) = −1 + i√3;
- k = 2: w_{2} = 2 e^{i4π/3} = 2 (−1/2 − i √3/2) = −1 − i√3.

Sul piano complesso sono i vertici di un triangolo equilatero inscritto nella circonferenza di raggio 2, con un vertice nel punto (2, 0).

**Soluzioni di z^{3} = −8.** Si ha −8 = 8 e^{iπ}, quindi r_{0} = 8, θ_{0} = π e n = 3. Il modulo delle radici è ³√8 = 2 e gli angoli sono π/3 + 2kπ/3, cioè π/3, π e 5π/3. Le tre soluzioni sono:
- 2 e^{iπ/3} = 2 (1/2 + i √3/2) = 1 + i√3;
- 2 e^{iπ} = −2;
- 2 e^{i5π/3} = 2 (1/2 − i √3/2) = 1 − i√3.

**Radici n-esime dell'unità.** L'equazione z^{n} = 1 ha come soluzioni z_{k} = e^{i·2kπ/n} per k = 0, 1, …, n − 1: sono i vertici di un poligono regolare di raggio 1 con n lati, che ha 1 come vertice.

## Trabocchetti d'Esame
- In ℂ la scrittura "radice n-esima di z" non indica un numero solo, ma l'insieme delle n soluzioni dell'equazione w^{n} = z. Quando si risolve un'equazione di questo tipo bisogna sempre elencarle tutte.
- Non si può calcolare la radice di un numero complesso "per componenti": in generale ⁿ√(a + bi) è diverso da ⁿ√a + i ⁿ√b. Si passa sempre dalla forma polare.
- Ricavando θ da a e b, attenzione al quadrante: quando a < 0 il solo arctan(b/a) dà l'angolo sbagliato (si veda il capitolo 7).

Le radici e le potenze che abbiamo imparato a calcolare torneranno utili nel prossimo argomento del corso, i polinomi, dove si vedrà quante soluzioni può avere un'equazione algebrica nel campo dei numeri complessi.
