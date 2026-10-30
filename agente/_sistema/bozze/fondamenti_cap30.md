# 30. Il Mondo di Tarski: Quantificatori su un Mondo Finito
## Che cos'è il mondo di Tarski
A fine lezione il docente ha mostrato un software sviluppato dall'Università di Stanford per l'insegnamento della logica (non accessibile agli studenti perché a pagamento: gli esempi sono stati ricopiati nelle dispense del docente). Il nome viene da **Alfred Tarski**, un logico del secolo scorso che ha studiato il **valore di verità** delle formule.

Un **mondo di Tarski** è un **dominio finito di oggetti** che si costruisce a piacere: nell'applicazione è una **scacchiera 8 × 8** su cui si dispongono dei solidi geometrici: **cubi**, **tetraedri** (le piramidi viola a base triangolare) e **dodecaedri** (solidi a 12 facce), di tre dimensioni (piccolo, medio, grande). Si scrivono poi delle formule che descrivono la situazione, e il programma dice se ciascuna è vera o falsa.

(In parole povere: è un mondo giocattolo in cui si può controllare, con una macchina, se una descrizione scritta con i quantificatori corrisponde davvero alla scena.)

Come ha osservato il docente, l'esempio è insignificante di per sé, ma è il «germe» di un problema vero: far vedere a una macchina una situazione, fornirle una descrizione e chiederle di controllarla. Il vero problema, trovare una descrizione significativa, è ancora molto lontano; qui la descrizione la dà l'utente e la macchina la controlla usando la definizione dei quantificatori, cosa facile in un mondo finito e piccolo.

## Le quattro formule
Le formule usate nell'esempio usano i predicati Cube (cubo), Tet (tetraedro), LeftOf (a sinistra di), FrontOf (davanti a), Dodec (dodecaedro) e Large (grande). Sono:
1. ∀x (Cube(x) → ∃y (Tet(y) ∧ LeftOf(x, y)));
2. ∀x (Cube(x) → ∃y (Tet(y) ∧ LeftOf(x, y) ∧ FrontOf(x, y)));
3. ∀x (Dodec(x) → Large(x));
4. ∃x (Dodec(x) ∧ Large(x)).

**LeftOf(x, y)** vuol dire che x si trova in una colonna più vicina al bordo sinistro della scacchiera rispetto a y, cioè **x sta a sinistra di y**. **FrontOf(x, y)** vuol dire che x si trova su una riga più vicina al bordo inferiore (cioè «più vicina alla nostra fronte», se si guarda la scacchiera da quel lato) rispetto a y.

(In parole povere: LeftOf guarda le colonne da sinistra, FrontOf guarda le righe dal bordo inferiore.)

## Formula 1: ogni cubo ha una piramide alla sua destra
Per controllare la formula 1 si prende **ogni cubo** (quantificazione universale: devono andare bene tutti) e si cerca almeno una piramide (∃) in una colonna più a destra. Nell'esempio, il primo cubo sta nella seconda colonna da sinistra e una piramide sta nella terza; per l'altro cubo, nella quarta colonna, c'è una piramide nella quinta. Quindi la formula è **vera**. Notare che non è richiesto che il cubo stia a sinistra di **tutte** le piramidi: basta che ne esista una per ciascun cubo, e può anche essere la stessa piramide per entrambi i cubi.

**Se si toglie una piramide** la formula può restare vera: se resta una piramide che sta alla destra di tutti i cubi, vale una proprietà più forte (c'è una piramide che va bene per tutti i cubi). **Se si toglie quella che serviva al secondo cubo**, la formula diventa **falsa**: quel cubo non ha più nessuna piramide alla sua destra.

## Formula 2: a destra e davanti
La formula 2 chiede di più: per ogni cubo ci deve essere una piramide che stia alla sua destra **e anche** più indietro (cioè il cubo sta davanti alla piramide). Geometricamente, per ogni cubo la piramide deve cadere nel **rettangolo** formato dalle colonne più a destra e dalle righe più lontane dal bordo inferiore.
- Nell'esempio iniziale è **vera**: per ogni cubo c'è una piramide in quel rettangolo.
- Togliendo la piramide di sinistra, la formula 1 resta vera, ma la formula 2 diventa **falsa**: uno dei due cubi resta «spaiato», perché non c'è più una piramide nel suo rettangolo, e non esiste una sola piramide che vada bene per tutti e due i cubi.
- **Spostando** la piramide rimasta in un punto che cada nel rettangolo di entrambi i cubi, la formula 2 torna **vera**: ora esiste un y che va bene per tutti gli x. Rimettendola dov'era, torna falsa.

Come ha ricordato il docente, è il problema già incontrato: trovare un y che vada bene per **tutti** gli x a volte è possibile, a volte no.

Un'osservazione ulteriore: una formula più forte (formula 2) richiede più della più debole (formula 1). Se già la formula 1 è falsa (per esempio perché un cubo non ha piramidi a destra), anche la 2 lo è.

## Formule 3 e 4: i dodecaedri, e che cosa succede con pochi oggetti
- La formula 3 dice che **tutti i dodecaedri sono grandi**. Se c'è un dodecaedro non grande (piccolo o medio) è **falsa**; aggiungere un nuovo dodecaedro grande non la rende vera (la percentuale di grandi aumenta, ma la formula chiede proprio tutti).
- La formula 4 dice che **c'è un dodecaedro grande**. È molto più facile da rendere vera: basta uno.

Si possono fare tre esperimenti.
1. **Un solo dodecaedro** (grande): le formule 3 e 4 sono **entrambe vere**. Quando c'è un solo dodecaedro non c'è differenza tra ∀ e ∃ riferiti ai dodecaedri: dire che c'è un oggetto con la proprietà o che tutti ce l'hanno vuol dire sempre la stessa cosa riferita a quell'unico oggetto. In generale, quando ci sono oggetti, il ∀ è una richiesta molto più forte dell'∃, ma con un solo oggetto coincidono.
2. **Due o più dodecaedri, di cui almeno uno grande e almeno uno non grande**: la 3 è falsa e la 4 vera, perché per la 4 basta che ce ne sia uno grande. Se invece nessuno è grande, anche la 4 è falsa.
3. **Nessun dodecaedro**: la 3 è **vera** (paradossalmente) e la 4 è **falsa**. Perché la 3 sia falsa servirebbe un dodecaedro non grande, ma se non ci sono dodecaedri non ce n'è nessuno che possa smentire l'affermazione universale; l'esistenziale invece è falso perché non c'è nulla. La logica assegna comunque un valore di verità a ogni affermazione, anche quelle che nel linguaggio quotidiano diremmo «prive di senso», e questo valore, qui, è **vero**. Quindi ∀x(Dodec(x) → Large(x)) è vera mentre ∃x(Dodec(x) ∧ Large(x)) è falsa: **il ∀ non implica l'∃** quando l'insieme è vuoto.

(In parole povere: se non c'è niente, «tutto ciò che c'è soddisfa la proprietà» è vero per vuoto, mentre «esiste qualcosa che la soddisfa» è falso.)

Notare anche che le formule 1 e 2 parlano solo di cubi e tetraedri: eliminare o spostare dodecaedri non le influenza.

## L'implicazione si può riscrivere
Un'ultima osservazione, a chiusura della lezione: l'implicazione A → B si può vedere in due modi equivalenti (per De Morgan):
- come la **negazione di una congiunzione**: ¬(A ∧ ¬B), cioè «non è vero che l'ipotesi è vera e la tesi è falsa» (esclude l'unico caso che smentisce l'implicazione; in parole povere: l'implicazione fallisce solo quando A è vera e B è falsa);
- come una **disgiunzione**: ¬A ∨ B, cioè «l'ipotesi è falsa oppure la tesi è vera», che elenca i tre casi in cui l'implicazione è vera (ipotesi falsa e tesi falsa; ipotesi falsa e tesi vera; ipotesi vera e tesi vera).

Le due scritture sono equivalenti, e il docente preferisce presentarla come negazione di una congiunzione (questione di stile).

(In parole povere: «se A allora B» vuol dire «non può succedere che A sia vero e B falso», oppure «A è falso, oppure B è vero».)

Con questo si chiude il capitolo 1 della Parte 2.
