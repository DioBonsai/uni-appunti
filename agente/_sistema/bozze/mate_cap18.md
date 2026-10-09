# 18. La Composizione di Funzioni: Ordine, Associatività e Identità
## Costruire una nuova funzione
Siano f : A → B e g : B → C due funzioni. Dato un elemento a ∈ A possiamo calcolare la sua immagine f(a) ∈ B; questo elemento sta nel dominio di g, quindi possiamo calcolare g(f(a)) ∈ C. Dimenticando il passaggio intermedio abbiamo costruito una funzione con dominio A e codominio C: è la **composizione** di f e g, indicata con g ∘ f, e vale

(g ∘ f)(a) = g(f(a)).

Gli insiemi A, B, C possono essere diversi, ma nulla esclude che alcuni di essi, o tutti, coincidano. La definizione è già nel capitolo 15; qui si vedono le proprietà con le dimostrazioni.

## L'ordine di scrittura
Questo è un punto che all'inizio confonde: **la funzione che si applica per prima si scrive per seconda**. In g ∘ f si calcola prima f e poi g, perché nell'espressione g(f(a)) la funzione più vicina all'elemento a è f. Si legge "g composto f", oppure "g tondino f".

La composizione si può fare solo se c'è **concordanza** tra il codominio della prima funzione e il dominio della seconda (a lezione si prende il caso in cui coincidono): l'elemento f(a) deve appartenere al dominio di g, altrimenti non sappiamo dove calcolare g.

## Più di due funzioni e associatività
Se la situazione lo permette si possono concatenare più funzioni, per esempio f : A → B, g : B → C, h : C → D: si porta a in f(a), poi in g(f(a)), poi in h(g(f(a))). Ma l'operazione di base è sempre tra due funzioni, quindi per scrivere h ∘ g ∘ f senza parentesi bisogna verificare la **proprietà associativa**:

h ∘ (g ∘ f) = (h ∘ g) ∘ f.

È la stessa esigenza che si ha sommando tre numeri: si sommano due alla volta, e perché la somma sia ben posta il risultato non deve dipendere da quali due si sommano per primi. Due funzioni sono uguali quando hanno stesso dominio, stesso codominio e stesso grafico (capitolo 10). Qui il dominio è A e il codominio è D per entrambe le scritture; resta da controllare che su ogni a ∈ A diano lo stesso valore.

**Dimostrazione** (passaggi ricostruiti dalla spiegazione a voce). Sia a ∈ A.
1. (h ∘ (g ∘ f))(a) = h((g ∘ f)(a)), perché h ∘ (g ∘ f) è la composizione di g ∘ f (prima funzione) e h (seconda).
2. (g ∘ f)(a) = g(f(a)), quindi il risultato è h(g(f(a))).
3. ((h ∘ g) ∘ f)(a) = (h ∘ g)(f(a)), perché si compone f (prima funzione) con h ∘ g (seconda), calcolata sull'immagine di a tramite f.
4. (h ∘ g)(f(a)) = h(g(f(a))).

I due risultati coincidono per ogni a, quindi le due funzioni sono uguali. L'associatività permette di comporre a coppie come si preferisce, purché si **rispetti l'ordine**: in generale scambiando l'ordine viene a mancare la concordanza tra codominio della prima e dominio della seconda.

## Quando alcuni insiemi coincidono
I casi più interessanti sono quelli in cui gli insiemi coincidono.
- Se f : A → B e g : B → A (cioè C = A), la composizione g ∘ f è una funzione da A in A, mentre f ∘ g, che si può fare lo stesso, è una funzione da B in B. Se A ≠ B sono funzioni **diverse**, perché hanno dominio e codominio diversi.
- Se A = B = C, cioè f e g vanno entrambe da A in A, si possono fare sia g ∘ f sia f ∘ g, e sono entrambe funzioni da A in A. Sono la stessa funzione?

## La composizione non è commutativa
In generale **no**. Su ℝ prendiamo f(x) = x² e g(x) = x + 1, entrambe da ℝ in ℝ:
- (g ∘ f)(x) = g(f(x)) = x² + 1: prima si eleva al quadrato, poi si somma 1;
- (f ∘ g)(x) = f(g(x)) = (x + 1)²: prima si somma 1, poi si eleva al quadrato.

Sono funzioni diverse: per x = 1 la prima dà 2, la seconda dà 4. Anche se la composizione si può fare in entrambi i modi, e le due funzioni hanno stesso dominio e codominio, il risultato **dipende dall'ordine**.

Questo è forse il primo esempio di operazione non commutativa che si incontra: il vecchio detto "l'ordine dei fattori non cambia il prodotto" vale per i numeri, ma non per oggetti di natura diversa come le funzioni. Nel corso di Algebra e Geometria compariranno altri oggetti che si possono moltiplicare ma con un'operazione non commutativa.

## L'identità è l'elemento neutro
Sia f : A → B e consideriamo le due composizioni con le identità: f ∘ id_{A} e id_{B} ∘ f. Entrambe hanno dominio A e codominio B, come f. Calcoliamole su a ∈ A:
- (f ∘ id_{A})(a) = f(id_{A}(a)) = f(a), perché l'identità non cambia l'elemento;
- (id_{B} ∘ f)(a) = id_{B}(f(a)) = f(a), per lo stesso motivo.

Dunque f ∘ id_{A} = f e id_{B} ∘ f = f: le identità si possono cancellare da una composizione, esattamente come 1 è neutro per la moltiplicazione e 0 per l'addizione. Le funzioni identità sono **neutre** rispetto alla composizione.

Resta da capire come si comportano iniettività e suriettività quando si compongono funzioni.
