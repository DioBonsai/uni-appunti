# 10. Funzioni: Definizione, Rappresentazioni e Uguaglianza
## Dare una funzione significa dare tre oggetti
Come visto nel capitolo 9, una **funzione** (o **applicazione**) ha un **dominio** A, un **codominio** B e un **grafico** Γ ⊆ A × B con la condizione di esistenza e unicità ∀ a ∈ A, ∃! b ∈ B tale che (a, b) ∈ Γ; dare una funzione significa dare la tripla (A, B, Γ). Quando (a, b) ∈ Γ si scrive f(a) = b, e le due scritture sono equivalenti. Lettere come f, g, h sono la scelta abituale per i nomi delle funzioni, ma non c'è alcun obbligo. Va notato che A e B possono anche essere lo stesso insieme: fa parte della definizione e capiterà spesso, con lo stesso insieme che una volta gioca da dominio e una volta da codominio.

## Un esempio completo su insiemi piccoli
Prendiamo A = {a, b, c, d} e B = {1, 2, 3}. Il prodotto cartesiano A × B si può disegnare come una piccola scacchiera di 4 × 3 caselle, ciascuna delle quali è una coppia (per esempio una casella rappresenta (c, 2), un'altra (a, 3)). Assegnare un grafico significa scegliere quali caselle appartengono a Γ.

Se segniamo le caselle (a, 2), (b, 2), (c, 3), (d, 1), sopra ogni elemento di A c'è esattamente una casella segnata: Γ definisce una funzione, con f(a) = 2, f(b) = 2, f(c) = 3, f(d) = 1. Si noti che 2 compare due volte come valore, e non è un problema: la definizione chiede un solo valore per ogni elemento del dominio, non valori diversi.

Questa descrizione a scacchiera serve a capire la definizione, ma nella pratica non si scrive così: se non c'è una formula che esprima la funzione, il modo più rapido è assegnare direttamente a ogni elemento del dominio il suo valore.

## Cosa NON è una funzione
Sulla scacchiera la condizione di esistenza e unicità può fallire in due modi: se sopra un elemento di A non c'è nessuna casella segnata manca l'esistenza, se ce ne sono due o più manca l'unicità. Nell'esempio precedente, se avessimo segnato due caselle sopra l'elemento b, il valore di f in b sarebbe ambiguo e Γ non definirebbe una funzione.

## Differenza rispetto alla funzione di analisi
Chi è abituato alle funzioni reali di variabile reale parte sempre dal calcolare il dominio come insieme dei punti in cui l'espressione ha senso (denominatore diverso da zero, radicando maggiore o uguale a zero e così via). Qui questo passo non esiste: il dominio **viene assegnato** insieme alla funzione, e si richiede che il valore f(a) esista per ogni a del dominio scelto. Dire "f(a) = b" deve essere sempre possibile, qualunque sia a ∈ A.

## Le notazioni a freccia
Una funzione si scrive quasi sempre f : A → B, che dice in un colpo solo dominio e codominio. Il nome si può anche mettere sopra la freccia, A →(f) B: è comodo quando si hanno più funzioni nello stesso diagramma, per esempio due funzioni f e g entrambe da A in B. Per questo motivo si parla spesso di **freccia** (o di **mappa**) per indicare una funzione.

Per descrivere il singolo elemento si usa la freccia con il trattino, x ↦ f(x), che si legge "x va in f(x)": per esempio n ↦ a_{n} associa a ogni naturale n un numero reale.

## Rappresentazione con i diagrammi di Venn
Una funzione si può rappresentare con due ovali, uno per A e uno per B, e una freccia da ogni punto x del dominio al punto y = f(x) del codominio. Anche quando A = B conviene **disegnare due copie separate** dell'insieme, una come dominio e una come codominio. Un modo intuitivo di pensare a una funzione è come a una scatola con un'entrata e un'uscita: dentro entra un elemento del dominio e ne esce uno del codominio.

## Quando due funzioni sono uguali
Dare una funzione significa dare tutti e tre gli oggetti (A, B, Γ), quindi f = (A, B, Γ) e g = (A′, B′, Γ′) sono **uguali** se e solo se coincidono tutti e tre: A = A′, B = B′ e Γ = Γ′. Non basta avere la stessa espressione, e non basta nemmeno avere gli stessi valori: servono anche lo stesso dominio e lo stesso codominio.

Un esempio fa vedere l'effetto contrario. Sull'insieme {0, 1, 2} (con codominio ℝ) consideriamo f(x) = 3x² − 1 e g(x) = x³ + 2x − 1. Le due espressioni sono diverse, ma:
- f(0) = −1 e g(0) = −1;
- f(1) = 2 e g(1) = 2;
- f(2) = 11 e g(2) = 8 + 4 − 1 = 11.

Hanno lo stesso dominio, lo stesso codominio e lo stesso grafico, quindi **f = g** pur essendo scritte con espressioni diverse. A lezione è stato accennato che fenomeni di questo tipo si incontrano nello studio dei campi finiti in crittografia.

**Trabocchetto d'esame:** assegnare una funzione dando solo un'espressione da calcolare non è abbastanza preciso. Se si vogliono studiare proprietà come iniettività e suriettività bisogna sempre specificare dominio e codominio, perché cambiandoli la stessa espressione può dare funzioni con proprietà diverse (lo vedremo nel capitolo 14).

Dopo l'uguaglianza vediamo le funzioni che compaiono di continuo, e due costruzioni elementari: successioni e restrizioni.
