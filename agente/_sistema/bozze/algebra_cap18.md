# 18. Zero, Opposto e Altri Esempi di Spazi Vettoriali
## Come trovare lo zero e l'opposto
Tra le proprietà di uno spazio vettoriale ce ne sono due che conviene ricordare: esiste sempre un elemento neutro per la somma, lo zero 0_{V}, e ogni vettore ammette un opposto. Saper calcolare lo zero di uno spazio vettoriale e l'opposto di un vettore è spesso importante, e c'è un modo semplice per farlo sempre.

**Proposizione.** Sia V uno spazio vettoriale su un campo 𝕂.
- Per ogni vettore v ∈ V si ha 0·v = 0_{V}: moltiplicando un qualunque vettore per lo scalare 0 si ottiene lo zero dello spazio.
- Per ogni vettore v ∈ V, (−1)·v è l'opposto di v, e si indica con −v.

Nell'enunciato il simbolo 0 compare in due ruoli diversi: nella formula 0·v = 0_{V} il primo 0 è lo zero del campo e il secondo è lo zero dello spazio vettoriale.

**Dimostrazione.**
1. Poiché 0 è l'elemento neutro della somma in 𝕂, si ha 0 = 0 + 0, quindi 0·v = (0 + 0)·v.
2. Per la proprietà 6, (0 + 0)·v = 0·v + 0·v. Si ha quindi 0·v = 0·v + 0·v.
3. Sommando a entrambi i membri l'opposto di 0·v (che esiste per la proprietà 3) si ottiene 0_{V} = 0·v + (−0·v) = (0·v + 0·v) + (−0·v) = 0·v + (0·v + (−0·v)) = 0·v + 0_{V} = 0·v, usando l'associatività e l'elemento neutro. È il passaggio che si indica come "semplificare".
4. Per l'opposto: v + (−1)·v = 1·v + (−1)·v = (1 + (−1))·v = 0·v = 0_{V}, usando la proprietà 8 e poi la proprietà 6. Dunque (−1)·v soddisfa la proprietà che definisce l'opposto di v. ∎

Il secondo punto si dimostra in due righe.

**Esempi.**
- In ℝ[x] lo zero è il **polinomio nullo** 0x^{n} + … + 0x + 0. Se non si riesce a "vederlo", si prende un polinomio qualunque, per esempio x + 1, e lo si moltiplica per 0: 0·(x + 1) = 0x + 0 = 0, il polinomio nullo. L'opposto di p(x) = a_{n}x^{n} + … + a_{1}x + a_{0} si ottiene moltiplicandolo per −1: è −p(x) = −a_{n}x^{n} − … − a_{1}x − a_{0}, cioè il polinomio con tutti i coefficienti cambiati di segno.
- In 𝕂^{n} lo zero è 0·(x_{1}, …, x_{n}) = (0·x_{1}, …, 0·x_{n}) = (0, …, 0), proprio quello trovato per ℝ^{n}.

## Ogni campo è uno spazio vettoriale su sé stesso
Nello spazio 𝕂^{n} il numero n è qualunque numero naturale maggiore di zero. Che cosa succede per n = 1? L'insieme 𝕂¹ è l'insieme delle "1-uple" (x), con x ∈ 𝕂, cioè semplicemente 𝕂. Quindi **ogni campo 𝕂 è uno spazio vettoriale su 𝕂 stesso**: la somma è la somma del campo, e la moltiplicazione per scalare è il prodotto del campo. Le proprietà della definizione seguono dalle proprietà del campo: (𝕂, +) è un gruppo commutativo perché lo è nella definizione di campo (proprietà 1-4), la 7 è la distributività del campo, la 6 segue dalla commutatività e dalla distributività, la 5 è l'associatività del prodotto e la 8 dice che 1 è l'elemento neutro per il prodotto. Ad esempio ℂ è uno spazio vettoriale su ℂ.

## Cambiare il campo degli scalari: ℂ su ℝ
Definire uno spazio vettoriale serve proprio a dire qual è l'insieme degli scalari per cui si può moltiplicare. L'esempio importante è ℂ: lo si può considerare come spazio vettoriale su ℂ, ma anche su ℝ, se si decide di moltiplicare i numeri complessi **solo per numeri reali**. L'insieme e la somma restano gli stessi (come gruppo con la somma ℂ è lo stesso), cambia soltanto il campo degli scalari. Con le operazioni di somma e di moltiplicazione per numeri reali, ℂ è dunque uno spazio vettoriale su ℝ.

Questo fatto è più generale: quando si hanno due campi e uno contiene l'altro, come ℝ dentro ℂ, il campo più grande si può sempre considerare uno spazio vettoriale sul campo più piccolo, moltiplicando solo per gli scalari del campo piccolo. Come sottolineato a lezione, non è un'osservazione casuale: è un concetto fondamentale di una teoria importante, la teoria di Galois.

Una cosa da ricordare: nella definizione di spazio vettoriale la somma non dipende dal campo scelto. Il campo entra in gioco solo nella seconda operazione, quando si decide per quali scalari si moltiplica. Per questo ℂ con gli scalari in ℂ e ℂ con gli scalari in ℝ sono due spazi vettoriali diversi, anche se l'insieme e la somma coincidono.

## Lo spazio delle funzioni
Consideriamo l'insieme V di tutte le funzioni f : ℝ → ℝ, quelle di cui si studiano i grafici alle superiori. In V si definiscono due operazioni **punto per punto**: per definire una funzione bisogna dire quanto vale in ogni x.
- La **somma** di due funzioni f e g è la funzione f + g il cui valore in x è (f + g)(x) = f(x) + g(x). Per esempio, se f(x) = eˣ e g(x) = sen x, la funzione f + g è eˣ + sen x: in ogni punto si calcolano prima eˣ e sen x e poi si somma.
- Il **prodotto per uno scalare** a ∈ ℝ è la funzione a·f il cui valore in x è (a·f)(x) = a·f(x). Per esempio 3·e^{x²} è la funzione che in ogni punto calcola e^{x²} e poi moltiplica per 3.

Con queste due operazioni V è uno spazio vettoriale su ℝ. Le dispense propongono lo stesso schema per le funzioni da [0, 1] in 𝕂 e per le successioni (x_{n}) di elementi di 𝕂, con somma e prodotto per scalare definiti componente per componente.

Gli spazi di questo tipo sono molto diversi da spazi come ℝ^{n}: più "selvaggi", mentre ℝ^{n} è più docile. Il concetto di **dimensione**, che si definirà più avanti, permetterà di quantificare questa differenza: spazi come ℝ^{n} hanno dimensione finita, mentre lo spazio di tutte le funzioni ha dimensione infinita.

## Un controesempio: i polinomi di grado esattamente k
L'esercizio 5.7 delle dispense chiede di controllare che l'insieme 𝕂_{k}[x] dei polinomi di grado **minore o uguale** a k è uno spazio vettoriale, e perché l'insieme dei polinomi di grado **esattamente** k non lo sia, se k ≥ 1. Il motivo è quello già visto nel capitolo 10: la somma può far diminuire il grado. Per esempio x² e −x² + x hanno entrambi grado 2, ma la loro somma è x, che ha grado 1, quindi la somma esce dall'insieme. Inoltre lo zero, il polinomio nullo, non ha grado k.
