# 16. Le Proprietà di ℝ^{n} e i Gruppi
## Le otto proprietà di somma e prodotto
In ℝ^{n} la somma e la moltiplicazione per scalare hanno otto proprietà. Le prime quattro riguardano **solo la somma**, le altre quattro mettono insieme la somma e il prodotto per scalare. Per ogni u, v, w ∈ ℝ^{n} e per ogni a, b ∈ ℝ valgono:
1. **associatività** della somma: (u + v) + w = u + (v + w);
2. **elemento neutro**: esiste un vettore 0_{ℝⁿ} ∈ ℝ^{n} tale che 0_{ℝⁿ} + v = v + 0_{ℝⁿ} = v per ogni v;
3. **opposto**: per ogni v esiste un vettore u tale che v + u = u + v = 0_{ℝⁿ};
4. **commutatività** della somma: u + v = v + u;
5. a·(b·v) = (ab)·v;
6. (a + b)·v = a·v + b·v;
7. a·(v + w) = a·v + a·w;
8. 1·v = v.

Il vettore della proprietà 2 si scrive con il simbolo 0_{ℝⁿ} per non confonderlo con il numero zero: è il vettore con tutte le componenti nulle, cioè l'origine (0, …, 0). L'opposto della proprietà 3 di un vettore v = (x_{1}, …, x_{n}) è semplicemente u = (−x_{1}, …, −x_{n}), che si indica con −v.

Sulle ultime quattro proprietà conviene essere precisi sulle operazioni che compaiono, perché sono di tipi diversi:
- nella proprietà 5 il prodotto "ab" è un prodotto tra numeri, cioè una moltiplicazione **in ℝ**; tutte le altre moltiplicazioni sono moltiplicazioni per scalare. Dice che moltiplicare un vettore prima per b e poi per a dà lo stesso risultato che moltiplicarlo per il numero ab;
- nella proprietà 6 la somma a + b è una somma **di numeri reali**, mentre la somma a destra, a·v + b·v, è una somma di vettori;
- la proprietà 7 è un'altra distributività, in cui tutte le operazioni sono tra vettori o per scalare;
- nella proprietà 8 il numero 1 è l'elemento neutro del prodotto in ℝ (come in ogni campo, esiste un elemento neutro del prodotto); la proprietà dice che moltiplicare un vettore per 1 non lo cambia.

Perché la commutatività (la proprietà 4) è separata dall'associatività? Come spiegato a lezione, perché si vuole impostare tutto in modo da poterlo applicare a contesti più generali, in cui l'ordine dell'operazione può essere importante.

Queste proprietà andrebbero dimostrate verificandole una per una sulle componenti: non è difficile, ma non lo si fa a lezione. Non è una lista scritta per divertimento: queste sono proprio le proprietà che definiscono uno spazio vettoriale, come si vedrà nel capitolo 17.

## I gruppi
Le prime tre proprietà coinvolgono una sola operazione, la somma. Un insieme dotato di una operazione che soddisfa proprietà di questo tipo prende un nome.

**Definizione.** Un **gruppo** è un insieme G dotato di un'operazione binaria, cioè di una funzione che a ogni coppia di elementi (a, b) di G associa un elemento di G, indicato con a ⋆ b, in modo che siano soddisfatte tre proprietà:
1. **associatività**: (a ⋆ b) ⋆ c = a ⋆ (b ⋆ c) per ogni a, b, c;
2. **elemento neutro**: esiste e ∈ G con e ⋆ a = a ⋆ e = a per ogni a;
3. **inversi**: per ogni a esiste a′ ∈ G con a ⋆ a′ = a′ ⋆ a = e.

Il simbolo ⋆ (asterisco) è un nome astratto per l'operazione: nel caso di ℝ^{n} l'operazione è la somma, e si usa +. Quando l'operazione assomiglia a una moltiplicazione, l'elemento a′ si chiama **inverso**; nel caso speciale dell'addizione si chiama **opposto**.

Un gruppo si dice **commutativo** (o **abeliano**) se vale anche la commutatività: a ⋆ b = b ⋆ a per ogni a, b. Il docente ha osservato che in Matematica discreta si incontreranno gruppi molto importanti, come i gruppi di permutazioni, che non sono abeliani: in essi l'ordine dell'operazione conta.

**Esempi.** ℝ^{n} con la somma è un gruppo abeliano, perché valgono le proprietà 1-4. Anche l'insieme ℤ dei numeri interi con la somma è un gruppo commutativo, e lo stesso vale per ℚ, ℝ e ℂ con la somma. Gli insiemi ℚ ∖ {0}, ℝ ∖ {0} e ℂ ∖ {0} sono gruppi commutativi anche con la moltiplicazione. Non sono invece gruppi: ℕ con la somma, perché manca l'opposto (la proprietà 3), e ℤ con la moltiplicazione, perché manca l'inverso: per esempio 2 non ha inverso moltiplicativo in ℤ.

Con le definizioni di gruppo e di gruppo abeliano si può dire in breve che le proprietà 1-4 di ℝ^{n} equivalgono a dire che (ℝ^{n}, +) è un gruppo abeliano, e il capitolo successivo parte proprio da qui.
