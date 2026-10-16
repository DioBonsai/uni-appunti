# 17. Conversa, Contrapposta, Condizioni Necessarie e Sufficienti
## Le forme correlate a un'implicazione
Da un'implicazione se ne possono costruire altre, scambiando i due argomenti o anche negandoli. Data p → q, si definiscono due proposizioni correlate:
- la **conversa** (o **reciproco**, in inglese *converse*): q → p, che scambia i ruoli di ipotesi e tesi;
- la **contrapposta** (in inglese *contrapositive*): ¬q → ¬p, che scambia i ruoli **e** nega entrambi gli argomenti.

## La conversa non è equivalente
Un'implicazione e la sua conversa **non sono equivalenti**. Un esempio: sia p la proposizione "1 > 2", che è falsa, e q la proposizione "4 < 8", che è vera. L'implicazione p → q ha l'ipotesi falsa, quindi è vera per difetto. La conversa q → p ha l'ipotesi vera e la tesi falsa, quindi è **falsa**. Esistono dunque valori di p e q per cui p → q e q → p hanno valori di verità diversi: succede quando p e q sono diversi.

Se si cambia la direzione di un'implicazione, il valore di verità cambia in due casi su quattro; quando p e q sono entrambe vere, o entrambe false, resta lo stesso (vera per entrambe). Un altro esempio: "se Jerry vince la lotteria, allora va al college" può essere vera, mentre la conversa "se Jerry va al college, allora ha vinto la lotteria" è falsa, perché potrebbe andarci con i suoi risparmi. L'errore più frequente è appunto scambiare un'implicazione con la sua conversa.

## La contrapposta è equivalente
Con la contrapposta le cose vanno diversamente: p → q e ¬q → ¬p hanno la stessa tavola di verità.

![Le tavole di verità di p → q e della sua contrapposta ¬q → ¬p: le colonne coincidono.](figure/fond/logica_contrapposta.png|11.5)

Anche con un ragionamento: p → q dice che tutte le volte che p è vera lo è anche q; allora se q è falsa dovrà essere falsa anche p. Quindi da p → q segue ¬q → ¬p. Applicando la stessa legge un'altra volta a ¬q → ¬p si ottiene ¬¬p → ¬¬q, e per la legge della doppia negazione (negare due volte equivale ad affermare: ¬¬p ≡ p, come si vede subito dalla tavola) si ritorna a p → q. Ciascuna delle due implicazioni si ottiene dall'altra, e sono quindi equivalenti.

## Condizioni necessarie e condizioni sufficienti
Nei corsi di matematica le implicazioni si esprimono spesso con le parole "condizione necessaria" e "condizione sufficiente". Non c'è un concetto nuovo: sono solo abbreviazioni per le due direzioni di un'implicazione, e vanno conosciute.
- **A è una condizione necessaria per B** significa che, quando B è vera, è necessario che lo sia anche A: B → A. Il "necessario" è la parte implicata.
- **A è una condizione sufficiente per B** significa A → B: se A è vera, basta questo perché lo sia B. Il "sufficiente" è l'ipotesi.

La condizione necessaria è la direzione "difficile", quella da destra a sinistra rispetto al modo in cui di solito scriviamo; la condizione sufficiente è quella che ci viene più naturale, da sinistra a destra: è semplicemente l'implicazione scritta nell'ordine consueto, mentre il necessario è il reciproco.

Che cosa si può dedurre? Basta rileggere la tavola di verità con questa terminologia.

Se **A è necessaria per B** (B → A):
- se A è vera, su B non si sa nulla (la condizione non è stata smentita, ma da sola non basta);
- se A è falsa, allora anche B è falsa: se una condizione necessaria fallisce, fallisce ciò di cui è condizione;
- se B è vera, allora A è vera: la verità di un fatto implica la verità di tutte le sue condizioni necessarie;
- se B è falsa, su A non si sa nulla: può essere falsa proprio per questa condizione o per un'altra.

Se **A è sufficiente per B** (A → B):
- se A è vera, allora B è vera;
- se A è falsa, su B non si sa nulla;
- se B è vera, su A non si sa nulla, perché quando la tesi è vera l'implicazione è vera comunque;
- se B è falsa, allora anche A è falsa: se fosse vera, anche B dovrebbe esserlo.

Un esempio che non richiede conoscenze particolari: "se Maria va alla Tour Eiffel, allora visita la Francia". Andare alla Tour Eiffel è una condizione **sufficiente** per visitare la Francia, ma non è necessaria: Maria potrebbe andare a Les Invalides, al Louvre o in Normandia, e ognuna di queste scelte sarebbe sufficiente a visitare la Francia. Invece visitare la Francia è una condizione **necessaria** per vedere la Tour Eiffel (se non è in Francia, non può raggiungerla), ma non basta: dipende da dove va esattamente in Francia.

## Come si traduce dal linguaggio naturale
Nei quesiti d'esame l'implicazione p → q non compare sempre nella forma "se p, allora q". Le formulazioni seguenti equivalgono tutte a p → q:
- "se p, allora q" e "p implica q";
- "q se p" (p, dopo il "se", è l'ipotesi);
- "p solo se q" (attenzione: non q → p; il "solo se" introduce la condizione necessaria, cioè la tesi);
- "p è condizione sufficiente per q";
- "q è condizione necessaria per p".

Riassumendo: l'ipotesi è la condizione sufficiente, la tesi è la condizione necessaria; la conversa, quella con i ruoli scambiati, non è equivalente all'implicazione di partenza, mentre la contrapposta lo è.
