# 24. Verificare le Regole di Inferenza: Dimostrazione, Controesempio e Tavola di Verità
## Quando una regola è valida
Una **regola di inferenza** ha delle ipotesi (le premesse) e una conclusione (cap. 19). Come per la definizione dell'implicazione (cap. 16), la regola è **valida** se, **ogni volta che tutte le ipotesi sono vere**, lo è anche la conclusione. Come sottolineato a lezione, i casi in cui anche solo una premessa è falsa non contano: si considerano «buoni per definizione». Gli unici casi rilevanti sono quelli in cui tutte le premesse sono vere.

**In parole povere:** una regola è un «se… allora…» tra le premesse messe insieme e la conclusione. È sbagliata se si riesce a trovare anche un solo caso in cui le premesse sono tutte vere e la conclusione è falsa; è giusta se un caso simile non esiste.

Per decidere si possono usare quattro strade, mostrate a lezione su cinque regole (numerate come nell'esercizio). Non sempre la dimostrazione è semplice: quando ci si blocca, i valori di verità che si stanno considerando danno un suggerimento su dove la regola può fallire.

## Strada 1: dimostrare con le regole note
Si **assumono** le ipotesi e si cerca di arrivare alla conclusione usando le regole solite (come il modus ponens).

**Regola 1.** Premesse: p → r e p → q. Conclusione: p → (r ∧ q).
Per dimostrare un'implicazione si assume l'ipotesi: si assume anche p. Si hanno tre assunzioni (p → r, p → q e p) e bisogna provare r ∧ q. Per provare una congiunzione bisogna provare entrambi i membri:
1. da p e p → r, per modus ponens, si ottiene r;
2. da p e p → q, per modus ponens, si ottiene q;
3. da r e q si ottiene r ∧ q.

La regola è valida. Come sottolineato a lezione, questa è una deduzione «meccanica»: nessun essere umano scende a questo livello di dettaglio, ma è il livello a cui lavorerebbe una macchina.

**Regola 5.** Premesse: p → r, r → q e p. Conclusione: q. Si parte da p, con il modus ponens si va a r, poi con un altro modus ponens a q: sono passi che «trasportano la verità». È la **transitività dell'implicazione**, ed è valida.

## Strada 2: cercare un controesempio
Se la dimostrazione si blocca, il fallimento è un **indizio** che la regola possa essere falsa: conviene cercare un caso in cui le premesse sono vere e la conclusione è falsa. In alternativa si fanno tutti gli otto casi di una tavola di verità con tre variabili, e si arriva con certezza alla risposta.

**Regola 2.** Premesse: p → (r ∨ q) e r → ¬q. Conclusione: p → r.
Assumendo p, per il modus ponens si ottiene r ∨ q: ma questo non basta per ottenere r, perché potrebbe essere vera solo q. Si usa r → ¬q solo se r è vera, e se r è falsa non dice nulla. Ci si è arenati nel caso p vera, r falsa, q vera. Lo si controlla: con p = V, r = F, q = V:
- p → (r ∨ q) = V → (F ∨ V) = V → V = V;
- r → ¬q = F → F = V (ipotesi falsa, implicazione vera);
- p → r = V → F = F.

Le due premesse sono vere e la conclusione è falsa: **la regola non è valida**. Come detto a lezione rispondendo a una domanda, cercare il controesempio è il primo passo di una tecnica che si chiama **ragionamento per contraddizione**: invece di dimostrare che la regola è vera, la si suppone falsa e si guarda se si arriva a una situazione impossibile; se ci si arriva, la regola è valida. Qui invece si trova un caso reale, e quindi la regola non è valida. La tecnica verrà ripresa più avanti nel corso.

**Regola 3.** Premesse: p → r e r → q. Conclusione: q.
Somiglia alla transitività, ma c'è un dettaglio: **p non c'è tra le premesse**. Si cerca allora un caso in cui le premesse sono vere e la conclusione è falsa, ragionando all'indietro:
1. q è falsa (la conclusione deve essere falsa);
2. da r → q con q falsa si ricava che r è falsa;
3. da p → r con r falsa si ricava che p è falsa.

Il contrapositivo (cap. 17) lo permette: normalmente si legge l'implicazione dalla verità alla verità, ma per la contrapposta vale la direzione opposta e **la falsità si sposta da destra a sinistra**, mentre la verità si sposta da sinistra a destra. Con p, q, r tutte false: p → r = F → F = V, r → q = F → F = V (ipotesi falsa, implicazione vera) e q è falsa. Le premesse sono vere, la conclusione è falsa: **la regola non è valida**. Su otto casi ne basta uno, e qui con p, q, r tutte false (il «triplo zero», in ordine di tavola di verità) la regola fallisce; è anche l'unico, perché partendo dall'ipotesi che la regola fosse falsa si è arrivati a questa unica scelta dei valori. Come sottolineato a lezione, il ragionamento automatico usa quasi solo la deduzione, perché solo sui casi piccoli si riesce a usare la tavola di verità; se però ci si trova meglio con la tavola, la si usa pure: è importante sapere che esistono anche le scorciatoie.

## Strada 3: la tavola di verità
**Regola 4.** Premesse: ¬r → ¬p e r. Conclusione: p.
Con la tavola, in cui p e r sono le sole variabili (q non compare), si guardano soltanto le righe in cui **tutte le premesse sono vere** e si controlla che lo sia anche la conclusione:
- la premessa r è vera solo nelle righe con r = 1;
- con r = 1 la premessa ¬r → ¬p ha ipotesi falsa, quindi è sempre vera;
- le righe rilevanti sono allora p = 1, r = 1 (conclusione p vera: va bene) e p = 0, r = 1 (conclusione p **falsa**: la regola fallisce).

Una riga che fa fallire la regola basta: **la regola non è valida**.

La tavola di verità è più lenta ma sicura, ed è la scelta migliore quando le formule sono poche e brevi.

## Strada 4: riscrivere la regola in una forma più semplice
La stessa regola 4 si può verificare senza tavola. Il **contrapositivo** dice che ¬r → ¬p è uguale a p → r: si scambiano gli argomenti e si negano entrambi, e le due negazioni della seconda forma si cancellano (doppia negazione). La regola diventa allora: da p → r e r si conclude p. Questa è la fallacia dell'**affermazione della conclusione** (cap. 19): l'implicazione non è invertibile, perché da p → r e r non si può dedurre p. Quindi la regola è falsa. Come sottolineato a lezione, è un altro modo di arrivare alla stessa conclusione, riconducendosi a un caso già noto.

## Riepilogo
In sintesi: la dimostrazione conviene quando la regola è valida e il percorso è breve; il controesempio quando la dimostrazione si blocca (si parte dalla conclusione falsa e si fa correre la falsità a sinistra); la tavola di verità quando le variabili sono poche; la riscrittura quando si riconosce una forma già vista, come il contrapositivo o la doppia negazione.

**In parole povere:** se la regola è giusta, una dimostrazione lo prova; se è sbagliata, basta un caso in cui le premesse sono vere e la conclusione no. Un fallimento nella dimostrazione suggerisce dove cercare quel caso.

Nel capitolo successivo le regole di inferenza vengono estese agli enunciati quantificati.
