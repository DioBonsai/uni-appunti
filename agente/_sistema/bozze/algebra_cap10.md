# 10. Polinomi: Monomi, Grado e Insiemi di Polinomi
## I monomi
I **polinomi** sono tipi particolarmente semplici di funzioni, ottenute combinando numeri e variabili con le sole operazioni di somma, differenza e prodotto. Si parte dai monomi: un **monomio** è un'espressione algebrica con una **parte numerica** (il coefficiente) e una **parte letterale** (le variabili), in cui sulle variabili si usano solo le operazioni di somma, sottrazione e moltiplicazione (le potenze con esponente naturale sono moltiplicazioni ripetute). Esempi di monomi sono 4x, −2xy² e √5·x⁴. L'esponente 4 in x⁴ è soltanto una notazione per x·x·x·x, quindi si usa ancora solo la moltiplicazione.

Non sono invece monomi sin(x), x/y e √x, perché sulle variabili compaiono operazioni diverse da somma, sottrazione e moltiplicazione. Come ha sottolineato il docente, la radice in √5·x⁴ non è un problema: √5 è semplicemente un numero (un 2,23… scritto in modo poco comodo) e fa parte del coefficiente, mentre una radice **sulla parte letterale**, come in √x, non va bene.

## Il grado
Il **grado di un monomio** è la somma degli esponenti delle sue variabili. L'esponente 1 non si scrive, quindi:
- 4x ha grado 1;
- −2xy² ha grado 1 + 2 = 3;
- √5·x⁴ ha grado 4.

Un monomio di grado zero è semplicemente un numero.

## I polinomi
Un **polinomio** è una somma di monomi, e il suo **grado** è il massimo dei gradi dei suoi monomi. Per esempio 4x − 2xy² + √5·x⁴ ha monomi di grado 1, 3 e 4, quindi è un polinomio di grado 4. Un polinomio può avere un numero qualsiasi di variabili (anche 113), ma in questo corso interessano soprattutto i polinomi in **una sola variabile**, che indichiamo con x e scriviamo p(x), o più semplicemente p.

## Polinomi in una variabile
Se compare solo la variabile x, in ogni monomio c'è x con qualche esponente (oppure nessuna x). Si possono quindi riunire i monomi con la stessa potenza di x e ordinarli dalla potenza più alta alla più bassa:

p(x) = a_{n}x^{n} + a_{n−1}x^{n−1} + … + a_{1}x + a_{0}, con a_{n} ≠ 0.

In questo caso p ha grado n, perché n è il massimo grado dei monomi. Gli esempi sono x³ − 2x + 5 (grado 3) e 4x² − 7 (grado 2). Un polinomio di grado zero è semplicemente un numero a_{0}.

C'è una sola eccezione: il **polinomio zero**, per il quale non esiste nessun coefficiente a_{n} diverso da zero. Lo si scrive p(x) ≡ 0, con tre barre: è un'identità tra funzioni, perché a sinistra c'è un'espressione che in generale dipenderebbe da x, mentre a destra il valore è 0 per ogni x.

## Gli insiemi di polinomi
Si indica con **ℝ[x]** l'insieme di tutti i polinomi nella variabile x con **coefficienti reali**, e con **ℂ[x]** l'analogo con coefficienti complessi. Con **ℝ_{k}[x]** si indica l'insieme dei polinomi di ℝ[x] di grado **minore o uguale a k** (e analogamente ℂ_{k}[x]).

Perché "≤ k" e non "= k"? Perché con "≤ k" vale una proprietà importante: **se p e q appartengono a ℝ_{k}[x], anche p + q appartiene a ℝ_{k}[x]**. Con "= k" la proprietà si perderebbe. Un esempio: p(x) = 2x² − x + 2 e q(x) = −2x² + 3x − 1 hanno entrambi grado 2, ma

p(x) + q(x) = (2x² − 2x²) + (−x + 3x) + (2 − 1) = 2x + 1,

che ha grado 1: i termini di grado 2 si cancellano. Nella somma il grado può quindi **diminuire**, ma non può mai aumentare: il risultato resta in ℝ₂[x] (e anche nel sottoinsieme più piccolo ℝ₁[x]), senza che possa comparire un polinomio di grado 3 o 7.

Il prossimo capitolo parte da una proprietà che i polinomi condividono con i numeri interi: la divisione con resto.
