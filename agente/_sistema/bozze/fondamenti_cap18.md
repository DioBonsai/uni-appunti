# 18. Il Bicondizionale, l'Equivalenza e le Riscritture dell'Implicazione
## L'equivalenza logica
Due formule sono **logicamente equivalenti** quando hanno la stessa tavola di verità (capitolo 15); si scrive P ≡ Q. Il **bicondizionale**, già incontrato come "equivalenza" nel capitolo 13, è il connettivo che dà 1 quando due valori sono uguali: p ↔ q (si legge "p se e solo se q", in inglese *iff*, o anche "doppia freccia") è vera quando i due valori di verità sono **uguali** (entrambi veri o entrambi falsi) ed è falsa quando sono diversi. È dunque il **test di uguaglianza** tra due valori di verità, ed è legato alla relazione ≡ tra formule: P ≡ Q vale proprio quando P ↔ Q è una tautologia.

## Il bicondizionale e le due implicazioni
Si chiama bicondizionale perché è fatto di due condizionali opposti, l'implicazione da sinistra a destra e quella da destra a sinistra: **p ↔ q ≡ (p → q) ∧ (q → p)**. In parole, p è condizione necessaria **e** sufficiente per q.

![La tavola di verità del bicondizionale: coincide con quella della congiunzione delle due implicazioni.](figure/fond/logica_bicondizionale.png|12.5)

Lo si può provare con una tavola di verità, come in figura, oppure con un ragionamento. Poiché p → q equivale a "il valore di p è minore o uguale al valore di q", la congiunzione (p → q) ∧ (q → p) dice che p ≤ q e q ≤ p. Per una proprietà degli ordini (l'antisimmetria), se p ≤ q e q ≤ p allora p e q sono uguali: quindi la congiunzione è il test di uguaglianza, cioè il bicondizionale. Quale dei due modi sia la definizione e quale la proprietà dipende da come si è definito il bicondizionale: se lo si definisce con la tavola di verità, si osserva che vale 1 con due valori uguali e 0 con due diversi, e poi si mostra l'equivalenza con le due implicazioni.

## L'implicazione si può scrivere con altri connettivi
Non è necessario avere l'implicazione come connettivo (o come circuito): se si sa realizzare la negazione e la congiunzione, si può realizzare anche l'implicazione. Vediamo come.

**La negazione dell'implicazione.** L'implicazione è falsa in un solo caso: ipotesi vera e tesi falsa. Quindi ¬(p → q) è vera esattamente quando p è vera e q è falsa:

¬(p → q) ≡ p ∧ ¬q.

La negazione di un'implicazione non è un'altra implicazione, ma una congiunzione. Attenzione al modo in cui si nega un'implicazione: p → ¬q oppure ¬p → ¬q non sono corrette; la negazione giusta è p ∧ ¬q. Per esempio, la negazione di "se Jerry riceve una borsa di studio, allora va al college" è "Jerry riceve la borsa di studio e non va al college".

**La doppia negazione.** Serve una legge banale ma importante: negare due volte equivale ad affermare, ¬¬p ≡ p. Basta guardare la tavola: se p è vera, ¬p è falsa e ¬¬p torna vera; se p è falsa, ¬p è vera e ¬¬p torna falsa. Nel linguaggio naturale non è così: dire che qualcosa "non è proprio falso" intende di solito qualcosa di più debole di "è vero". Nel linguaggio semplificato della logica, dove si guardano solo i valori di verità, non c'è alcuna differenza.

**L'implicazione con negazione e disgiunzione.** Si parte dalla legge precedente e si aggiunge una doppia negazione:

p → q ≡ ¬¬(p → q) ≡ ¬(p ∧ ¬q).

Sono già tre connettivi (due negazioni e una congiunzione) che ci permettono di scrivere l'implicazione. Con la legge di **De Morgan**, di cui nel capitolo 15 si è visto il caso della disgiunzione e di cui subito sotto si giustifica la versione duale per la congiunzione, si può ridurre. La legge dice che negare una congiunzione equivale a disgiungere le negazioni degli argomenti: ¬(a ∧ b) ≡ ¬a ∨ ¬b. Applicata a ¬(p ∧ ¬q) dà ¬p ∨ ¬¬q, e per la doppia negazione si arriva a

**p → q ≡ ¬p ∨ q.**

![Le colonne di p → q e di ¬p ∨ q coincidono.](figure/fond/logica_implicazione_disgiunzione.png|10.5)

È la definizione più usata dell'implicazione, e dice che un'implicazione è vera se e solo se l'ipotesi è falsa **oppure** la tesi è vera: sono esattamente i tre casi veri della tavola, quelli con la tesi vera (due righe) e quelli con l'ipotesi falsa (due righe), con una sovrapposizione, perché con ipotesi falsa e tesi vera l'implicazione è vera per due motivi indipendenti. Si poteva arrivarci in un passo solo osservando la tavola; il passaggio per De Morgan mostra che le leggi si combinano.

Per questo, in un linguaggio come Java, l'implicazione non serve come operatore: p → q si scrive come `!p || q`.

## Le leggi di De Morgan e la dualità
Le leggi di De Morgan sono due:
- ¬(p ∧ q) ≡ ¬p ∨ ¬q: negando una congiunzione si disgiungono le negazioni;
- ¬(p ∨ q) ≡ ¬p ∧ ¬q: negando una disgiunzione si congiungono le negazioni (già vista nel capitolo 15).

Sono **duali**: se si scambiano vero e falso, congiunzione e disgiunzione e si lascia la negazione com'è (la negazione è auto-duale: scambiando vero e falso, la sua tavola resta la stessa), da una legge si ottiene l'altra. La logica proposizionale è duale in generale: non c'è un ruolo privilegiato per il vero o per il falso, e se si scambia ovunque vero con falso e congiunzione con disgiunzione, ogni equivalenza valida si trasforma nella sua duale, che è ancora un'equivalenza valida. Si può quindi dire che c'è **un'unica legge di De Morgan**, e l'altra è la sua duale.

Un'applicazione in Java: la condizione `x < 10 || x > 20` equivale a `!(x >= 10 && x <= 20)`. Questa seconda scrittura nega l'appartenenza all'intervallo tra 10 e 20 estremi compresi; applicando De Morgan si porta la negazione dentro le parentesi, scambiando la congiunzione con la disgiunzione, e arrivando ai predicati di base (uguale, diverso, minore, maggiore, minore o uguale, maggiore o uguale) si sostituisce ciascuno con il suo complementare: la negazione di `x >= 10` è `x < 10` e quella di `x <= 20` è `x > 20`. La prima forma si legge più facilmente: per questo si preferisce.

## Il limite delle tavole di verità
Le tavole di verità sono un buon metodo per provare un'equivalenza o una tautologia quando le proposizioni atomiche sono poche (come per p ↔ q e le due implicazioni), ma non funzionano su grande scala: con n proposizioni atomiche le righe sono 2^{n}, quindi il numero di passi cresce in modo esponenziale. Con cento proposizioni atomiche servirebbe una tavola di 2^{100} righe, circa 10^{30}, un numero che nessun computer di oggi riesce a percorrere. In questi casi servono metodi più rapidi, che però hanno altri difetti: non riescono a concludere in tutti i casi.
