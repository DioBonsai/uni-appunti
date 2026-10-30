# 29. Esercizi di Ripasso sui Quantificatori Annidati: Domini e Ordine
## Prima di tutto il dominio
Il valore di verità di una formula con quantificatori dipende dal **dominio del discorso** (in parole povere: dall'insieme di valori che le variabili possono assumere): bisogna sempre fissarlo prima di rispondere. Gli esercizi seguenti sono quiz di ripasso (sui quantificatori annidati e sulle lezioni precedenti) e sono, come ha detto il docente, un pretesto per controllare di ricordare bene la definizione di verità.

## Quiz 1: x² + y² = 9 e x² + y² ≥ 0, con x e y reali
Siano x e y numeri reali (positivi, nulli o negativi, con cifre decimali finite o infinite).
- **∀x∀y(x² + y² = 9)** è **falsa**: con x = 100 si ha 10000 + y² ≥ 10000, che non è 9.
- **∀x∃y(x² + y² = 9)** è **falsa**: con x = 100 non esiste nessun y reale tale che 10000 + y² = 9. Sarebbe vera nei numeri complessi (y = √(9 − x²), che per x grande è un numero complesso), ma non nei reali, dove 9 − x² può essere negativo.
- **∃x∀y(x² + y² = 9)** è **falsa**: con y = 100 si ottiene lo stesso problema.
- **∃x∃y(x² + y² = 9)** è **vera**: per esempio x = 0 e y = 3 (0 + 9 = 9). In realtà ci sono infiniti valori reali che la rendono vera: sono tutti e soli i punti di una circonferenza di raggio 3 con centro nell'origine, ma alla domanda bastava trovarne uno.
- **∀x∀y(x² + y² ≥ 0)** è **vera**: la somma di due quadrati non è mai negativa.
- **∀x∃y(x² + y² ≥ 0)** è **vera**: è implicata dalla precedente.
- **∃x∀y(x² + y² ≥ 0)** è **vera**: per esempio con x = 0 si ottiene y² ≥ 0 per ogni y; anzi, qualunque x va bene.
- **∃x∃y(x² + y² ≥ 0)** è **vera**.

(In parole povere: con il quadrato si ottiene sempre un numero non negativo, quindi la proprietà «≥ 0» vale sempre, mentre «= 9» richiede di colpire proprio il valore 9.)

## Quiz 2: x² < y + 1
- **∀x∀y(x² < y + 1)** è **falsa**: con x = 10 e y = 0 si ottiene 100 < 1, che è falso.
- **∀x∃y(x² < y + 1)** è **vera**: basta scegliere y molto grande, per esempio y = x² (si ottiene x² < x² + 1).
- **∃x∀y(x² < y + 1)** è **falsa**: scegliendo y = −1 si ha y + 1 = 0, quindi si dovrebbe avere x² < 0, ma i quadrati sono maggiori o uguali a 0. Il controesempio y = −1 funziona **indipendentemente da x**.
- **∃x∃y(x² < y + 1)** è **vera**.
- **∃y∀x(x² < y + 1)** è **falsa**: per ogni y si può scegliere x molto grande, per esempio x = max(1, y + 1): allora x² ≥ x ≥ y + 1, e x² < y + 1 non vale.
- **∀y∃x(x² < y + 1)** è **falsa**: con y = −1 servirebbe x² < 0.

Notare che questi ragionamenti non si possono verificare provando tutti i valori, perché sono infiniti: servono controesempi e argomentazioni.

## Il quiz sul quadrato: ∀x∃y(x = y²)
**∀x∃y(x = y²)** dice che ogni x ha una radice quadrata. È vera o falsa **a seconda del dominio**:
- nei **numeri reali positivi** (R⁺) è vera: la radice quadrata esiste sempre (e c'è un algoritmo per calcolarla);
- nei **numeri reali** (R) è falsa: −1 non ha radice quadrata reale;
- nei **numeri complessi** è vera: la radice di −1 è l'unità immaginaria i;
- negli **interi** è falsa: la radice di 2 non è un intero;
- nei **razionali** (Q) e nei **razionali positivi** (Q⁺) è falsa: √2 esiste, ma non è un numero razionale (nessuna frazione è la radice esatta di 2; si possono dare approssimazioni quanto si vuole, ma mai il risultato esatto);
- nei razionali con segno anche −1 non ha radice razionale.

Quindi, nell'esempio con i domini R⁺ × R⁺, R × R, Q⁺ × Q⁺ e Q × Q, le risposte corrette sono rispettivamente Vera, Falsa, Falsa, Falsa. Il significato di «x ha una radice quadrata» che sembra così ovvio nasce da dettagli di cui non siamo consapevoli, e una macchina deve fare un lavoro molto più grande per rispondere.

Una nota sulla notazione: quando si scrive un «+» in alto a destra su un insieme di numeri (Q⁺, R⁺, Z⁺) si intendono i soli valori **positivi**, senza lo zero; non tutti i libri rispettano questa convenzione.

## L'ordine dei quantificatori
La stessa formula con i quantificatori scambiati può cambiare completamente significato.
- **∀x∃y(y > x)** (su interi) è **vera**: dato x basta prendere il successore, y = x + 1.
- **∃y∀x(y > x)** è **falsa**: bisognerebbe scegliere y **prima** di sapere con quale x verrà confrontato; ma, qualunque y si scelga, basta prendere x = y + 1 per rendere falso y > x.

**Regola.** La scelta fatta **dopo** sfrutta i dati forniti prima; la scelta fatta **prima** deve andare bene qualunque siano le scelte fatte dopo.

(In parole povere: in ∀x∃y il valore di y può dipendere da x; in ∃y∀x un solo y deve andare bene per tutti gli x.)

Un esempio con la formula x² < y + 1: «per ogni x c'è un y» è vera (y si sceglie guardando prima quanto è grande x²), ma «c'è un y per ogni x» è falsa: bisogna scegliere y senza conoscere x, e per quanto grande sia, se x è abbastanza grande la disuguaglianza non vale. Anche un valore molto grande, come un miliardo, non va bene se x vale il doppio.

Come ha detto il docente, il significato di una formula è molto fragile: basta cambiare un dettaglio e cambia tutto. Con y > x: ∀x∃y(y > x) è vera; scambiando solo l'ordine dei quantificatori si ottiene ∃y∀x(y > x), falsa; tenendo fisso l'ordine delle variabili e scambiando i quantificatori si ottiene ∃x∀y(y > x), falsa anche scegliendo y = x. In ogni caso il significato cambia, ma in modo diverso.

Nel capitolo seguente le stesse idee si applicano a un piccolo mondo di figure geometriche, il mondo di Tarski.
