# 13. Quante Radici Ha un Polinomio: Induzione, Grado 2 e Teorema Fondamentale dell'Algebra
## Al massimo n radici
**Proposizione.** Un polinomio di grado n ≥ 1 ha al massimo n radici, contate con molteplicità.

Nell'ultimo esempio del capitolo 12 un polinomio di grado 3 aveva 3 radici contate con molteplicità (1 doppia e 0 semplice): non può averne 4 o 5, ne può avere al massimo 3, e potrebbe averne di meno.

## Un richiamo sull'induzione
La dimostrazione usa l'**induzione**, che il docente ha spiegato prima di usarla. Si vuole dimostrare che una proprietà vale per **tutti** i numeri naturali, qui per tutti i gradi n ≥ 1. Farlo grado per grado non finirebbe mai. Si dimostrano invece due cose:
1. la proprietà vale per n = 1 (il caso base);
2. se vale per un n qualsiasi, allora vale anche per n + 1 (il passo induttivo).

Il passo 2 si applica a ripetizione: dal caso base 1 si arriva a 2, da 2 a 3, da 3 a 4, e così via fino a qualunque grado.

## La dimostrazione
**Caso base, n = 1.** Un polinomio di grado 1 è del tipo ax + b (con a ≠ 0; i coefficienti possono essere reali, come in 7x + 13, o complessi). Si ha ax + b = 0 se e solo se ax = −b, cioè x = −b/a: c'è **esattamente una** radice, quindi al massimo una.

**Passo induttivo.** Si assume che la proposizione valga per un certo n e si dimostra per n + 1. Sia p(x) un polinomio di grado n + 1. Ci sono due possibilità.
1. p non ha nessuna radice. Non c'è nulla da dimostrare, perché "al massimo n + 1" ammette anche zero radici.
2. p ha almeno una radice a. Per la proposizione del capitolo 12, (x − a) divide p, cioè p(x) = (x − a)q(x), e q(x) ha grado n. Per l'ipotesi induttiva q ha al massimo n radici contate con molteplicità. Ma p(x) = 0 vale solo quando uno dei due fattori è zero (un prodotto è nullo se e solo se lo è uno dei fattori): o x = a, o x è una radice di q. Le radici di p, contate con molteplicità, sono esattamente quelle di q più a: in tutto al massimo n + 1.

Il grado zero è escluso dall'enunciato: un polinomio di grado 0 è un numero; se non è zero non ha radici, ma il polinomio zero ha infinite radici (ogni valore è una radice).

## Equazioni di secondo grado
Sia p(x) = ax² + bx + c con a, b, c reali e a ≠ 0. Con il **discriminante** Δ = b² − 4ac:
- se Δ > 0, p ha due radici reali distinte x = (−b ± √Δ)/(2a);
- se Δ = 0, p ha una sola radice x = −b/(2a), con molteplicità 2;
- se Δ < 0, p non ha radici reali.

Ci sono dunque polinomi senza radici reali. Per questo si sono introdotti i numeri complessi: in ℂ si può calcolare la radice quadrata di qualsiasi numero, anche negativo o complesso. Per Δ ≠ 0 i due valori ±√Δ sono i due numeri complessi distinti che risolvono z² = Δ (basta la radice quadrata, tra le radici n-esime del capitolo 9); per Δ = 0 coincidono e la radice è doppia. Quindi un polinomio di grado 2 ha **sempre due radici complesse**: possono essere due reali distinte, due uguali o due complessi non reali.

## Il teorema fondamentale dell'algebra
**Teorema (fondamentale dell'algebra).** Un polinomio p(x) a coefficienti complessi di grado n ≥ 1 ha **esattamente** n radici complesse, contate con molteplicità.

Il docente non lo dimostra: le dimostrazioni accessibili usano strumenti di analisi più avanzati, quindi nel corso si enuncia soltanto. Esempio: x² + 1 non ha radici reali, ma ha le due radici complesse i e −i, perché i² = −1 e (−i)² = −1, e in entrambi i casi si ottiene p = 0. È il motivo principale per cui si sono introdotti i numeri complessi: studiando i polinomi si vogliono sempre trovare **tutte** le radici, e il numero giusto di radici (il grado) si ottiene solo con i numeri complessi.

## Due complementi (non svolti a lezione)
Sono due risultati che non sono stati trattati in aula.

**Radici complesse di un polinomio di grado 2.** Per ax² + bx + c la formula x = (−b ± √Δ)/(2a) vale anche con i complessi, dove ±√Δ indica le due radici quadrate complesse di Δ. Esempio: le radici di x² + (1 − i)x − i hanno Δ = (1 − i)² + 4i = 2i, con radici quadrate ±(1 + i), quindi x = (−(1 − i) ± (1 + i))/2, cioè x₊ = i e x₋ = −1.

**Polinomi a coefficienti reali.** Se p(x) ha coefficienti reali e z è una radice complessa, allora anche il coniugato z̄ è una radice. Dimostrazione: da p(z) = a_{n}zⁿ + … + a_{1}z + a_{0} = 0, applicando il coniugio a entrambi i membri si ottiene a_{n}z̄ⁿ + … + a_{1}z̄ + a_{0} = 0, perché il coniugio rispetta somme e prodotti (e quindi le potenze, capitolo 5) e i coefficienti, essendo reali, coincidono con i loro coniugati. Dunque p(z̄) = 0.

Con questo si chiude la parte sui polinomi; il corso passa agli spazi vettoriali.
