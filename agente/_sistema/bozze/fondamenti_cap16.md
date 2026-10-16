# 16. L'Implicazione (Condizionale)
## Da dove si riparte
Dopo i connettivi and, or, not, xor ed equivalenza, la logica proposizionale continua con l'**implicazione**, che nel libro è la sezione 1.3 della seconda parte. È anche il connettivo più delicato, perché il significato che gli si dà in logica proposizionale è diverso, e più povero, di quello che ha nel linguaggio comune.

## Il significato dell'implicazione: materiale e non causale
Un esempio dal libro: "se il Dipartimento di Matematica ottiene 60 mila dollari di finanziamento extra, assumerà un nuovo professore". Nel linguaggio comune "se… allora" suggerisce innanzitutto una **relazione di causa**: quel denaro verrà usato proprio per assumere qualcuno. In logica proposizionale di questa relazione non c'è alcuna traccia. Si lavora soltanto con i **valori di verità** (vero e falso), e le tavole di verità sono troppo povere per esprimere un concetto complesso come la causalità. Per questo si dice che l'implicazione della logica è **materiale**: usa soltanto i valori di verità dei due argomenti e non le relazioni tra le due parti.

La seconda differenza riguarda i casi in cui l'ipotesi non si verifica. Nel linguaggio comune, se il Dipartimento non ottiene il finanziamento, l'affermazione resta di fatto **indefinita**: non è né vera né falsa. In matematica avere affermazioni prive di valore di verità è molto svantaggioso, perché si potrebbe scrivere una dimostrazione senza accorgersi che è priva di senso. Per questo si decide di dare un significato a tutte le implicazioni, anche quando l'ipotesi è falsa.

## La notazione e la tavola di verità
L'implicazione si scrive con una freccia: p → q si legge "p implica q". La proposizione p si chiama **ipotesi** o **antecedente**, la proposizione q si chiama **tesi**, **conclusione** o **conseguente**. La tavola di verità, con l'ordine del libro (prima il vero, 1, poi il falso, 0), è:

![La tavola di verità dell'implicazione: l'unica riga falsa è quella con ipotesi vera e tesi falsa.](figure/fond/logica_implicazione.png|8)

L'implicazione è **falsa in un solo caso**: quando l'ipotesi è vera e la tesi è falsa. Contano le due righe con ipotesi vera: si prende l'ipotesi vera e si controlla che sia vera anche la tesi. Se lo è, l'implicazione è vera; se non lo è, è falsa. Nelle altre due righe, quelle con ipotesi falsa, l'implicazione è vera senza nemmeno guardare la tesi.

## Vero per difetto
Quando l'ipotesi è falsa l'implicazione è **vera**, qualunque sia la tesi. Si dice che è **vera per difetto** (in inglese *vacuously true*; si può dire anche "banalmente vera"). È una **convenzione**: bisognava dare un valore di verità a questi casi, e quello che per esperienza dà meno fastidio quando si scrivono le dimostrazioni è considerare l'implicazione come provata. Quando non ci sono le condizioni per usare l'implicazione, la si prende per buona e ci si concentra sui casi in cui l'ipotesi è vera.

Il motivo per cui la convenzione è comoda si vede con un esempio di matematica: "se x è positivo, allora x · x è positivo", cioè x > 0 → x · x > 0, che si vuole vera per ogni x.
- Con x = 3: 3 > 0 è vera e 9 > 0 è vera, quindi l'implicazione è vera.
- Con x = 1: 1 > 0 e 1 > 0 sono vere, e l'implicazione è vera.
- Con x = 0: 0 > 0 è falsa e 0 · 0 > 0 è falsa. L'ipotesi è falsa, quindi l'implicazione è vera per difetto.
- Con x = −1: −1 > 0 è falsa, ma (−1) · (−1) = 1 > 0 è vera. Anche qui l'ipotesi è falsa e l'implicazione è vera, senza che interessi che la tesi lo sia.

Nel linguaggio comune qualcuno direbbe che "se 0 > 0…" non ha senso. Ma in matematica, se sostituendo un valore al posto di x l'enunciato perdesse significato, un enunciato sensato diventerebbe privo di senso. Con la tavola di verità dell'implicazione l'enunciato ha invece sempre un valore: è vero per ogni x.

La tavola si può leggere anche così:
- se la tesi è vera, l'implicazione è vera, e si può ignorare l'ipotesi;
- se l'ipotesi è falsa, l'implicazione è vera, e si può ignorare la tesi;
- l'unico caso in cui i due valori sono entrambi rilevanti è quello con ipotesi vera e tesi falsa, in cui l'implicazione è falsa.

Come sottolineato a lezione, nel corso di Fondamenti (e in quelli di Matematica e di Programmazione) si usa sempre questa implicazione materiale: bisogna dimenticare il significato di "se… allora" del linguaggio comune.

## L'implicazione come test d'ordine
C'è un altro modo di descrivere la tavola. Scrivendo 0 al posto di falso e 1 al posto di vero, p → q vale 1 esattamente quando il valore di p è **minore o uguale** al valore di q: 1 ≤ 1, 0 ≤ 1 e 0 ≤ 0 danno 1, mentre l'unico caso in cui p ≤ q è falso è p = 1 e q = 0, che è proprio la riga falsa. L'implicazione si può quindi definire come il **test d'ordine tra valori booleani**.

Una conseguenza: la proposizione (p → q) ∨ (q → p) è **sempre vera**, qualunque siano i valori di p e di q. Nel linguaggio comune verrebbe da dire che è falsa, perché ci aspetteremmo che p sia causa di q oppure il contrario, mentre due eventi possono essere del tutto indipendenti. Ma tra due numeri uno dei due è sempre minore o uguale all'altro, e lo stesso vale per due valori di verità: se c'è almeno uno 0, il più piccolo è lo 0; se sono entrambi 1, sono uguali. Quindi una delle due implicazioni è vera, e la loro disgiunzione è sempre vera.

## La precedenza
Come in 2 + 3 · 5 la moltiplicazione si esegue prima della somma, così tra i connettivi c'è una convenzione: l'implicazione si valuta **per ultima**. Con una negazione, un or e un'implicazione senza parentesi si calcolano prima la negazione e l'or, e poi l'implicazione: p ∨ q → ¬r significa (p ∨ q) → (¬r). Chi non vuole ricordare le convenzioni può aggiungere parentesi in più, e questo non è mai sbagliato, anche se dopo un po' diventa fastidioso.

## Alcuni esempi di valutazione
Siano p vera, q falsa e r vera (p = 1, q = 0, r = 1). Valutiamo quattro formule.
- **(p ∧ q) → r**. La congiunzione p ∧ q è falsa, perché uno dei due lati (q) è falso. L'ipotesi è quindi falsa e l'implicazione è vera, senza guardare r. In generale, se una parte di una congiunzione è falsa, l'intera congiunzione è falsa, e un'implicazione che ha quella congiunzione come ipotesi è vera.
- **(p ∨ q) → ¬r**. La disgiunzione p ∨ q è vera (basta che un lato sia vero), mentre ¬r è falsa. Si ha 1 → 0, e l'implicazione è **falsa**.
- **p ∧ (q → r)**. L'implicazione q → r ha ipotesi falsa, quindi è vera per difetto; anche p è vera. La congiunzione è quindi vera.
- **p → (q → r)**. L'implicazione interna q → r è vera per difetto, quindi si ha 1 → 1, e l'intera formula è vera.

L'ultima formula si legge in modo naturale come "se vale p, allora (se vale q, allora vale r)", cioè come un'implicazione con **due ipotesi**: se p e q sono entrambe vere, allora è vera r. In generale, quando un'implicazione ha più ipotesi e anche una sola è falsa, l'implicazione è vera per difetto; se tutte le ipotesi sono vere bisogna controllare la tesi, e l'implicazione è falsa solo se la tesi è falsa. Le due scritture sono in effetti equivalenti: p → (q → r) e (p ∧ q) → r sono false soltanto quando p e q sono vere e r è falsa.

Il capitolo successivo parte dall'implicazione per costruire la sua conversa, la sua contrapposta e le espressioni "condizione necessaria" e "condizione sufficiente".
