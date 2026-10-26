# 24. Verificare le Regole di Inferenza: Dimostrazione, Controesempio e Tavola di Verità
## Che cos'è una regola, in concreto
Una **regola di inferenza** (cap. 19) è fatta da alcune **premesse** (le ipotesi) e da una **conclusione**. Si scrive con il simbolo ⊢, che si legge «allora si ricava»: per esempio **p → r, r → q ⊢ q** vuol dire «dalle premesse p → r e r → q voglio ricavare q». Il quesito che si pone è sempre lo stesso: **la regola è valida?** cioè: partendo da premesse vere, si arriva sempre a una conclusione vera?

Un esempio con frasi normali. Premesse: «se piove, la strada è bagnata» e «se la strada è bagnata, il traffico rallenta». Conclusione: «se piove, il traffico rallenta». Qui la conclusione segue davvero dalle premesse: la regola è valida. Se invece la conclusione fosse «piove», non seguirebbe: il traffico può rallentare anche per altri motivi.

**Definizione.** Una regola di inferenza è **valida** se, **in ogni situazione in cui tutte le premesse sono vere, anche la conclusione è vera**. Come per l'implicazione (cap. 16), le situazioni in cui anche solo una premessa è falsa non contano: la regola è «buona per definizione» in quei casi, perché non promette niente.

**In parole povere:** una regola è valida se è «a prova di bomba»: se le premesse sono vere, la conclusione non può che essere vera. È **sbagliata** se si trova anche un solo caso in cui le premesse sono tutte vere e la conclusione è falsa; quel caso si chiama **controesempio**.

La lezione ha mostrato come verificare cinque regole, usando quattro strade diverse. Le regole (le numeriamo come nell'esercizio):

- **Regola 1**: premesse p → r e p → q; conclusione p → (r ∧ q). **Valida.**
- **Regola 2**: premesse p → (r ∨ q) e r → ¬q; conclusione p → r. **Non valida.**
- **Regola 3**: premesse p → r e r → q; conclusione q. **Non valida.**
- **Regola 4**: premesse ¬r → ¬p e r; conclusione p. **Non valida.**
- **Regola 5**: premesse p → r, r → q e p; conclusione q. **Valida.**

(Nel seguito si spiega perché, una alla volta.)

## Strada 1: la tavola di verità (la più sicura)
È il metodo meccanico e sicuro: si scrivono tutte le possibili combinazioni di vero/falso per le lettere (con tre lettere sono 8 righe, con due 4), si calcolano le premesse e la conclusione riga per riga, e poi **si guardano solo le righe in cui tutte le premesse sono vere**: in ognuna di esse deve esserlo anche la conclusione. Se c'è una sola riga in cui non lo è, la regola non è valida.

**Regola 4: ¬r → ¬p, r ⊢ p.** Qui le lettere sono solo p e r (la q non compare). Le righe sono 4 (per ciascuna si scrivono i valori di ¬r → ¬p, r e p):

- p = V, r = V: ¬r → ¬p = V, r = V, p = V. Premesse vere, conclusione **vera**: va bene.
- p = V, r = F: ¬r → ¬p = F, r = F, p = V. Una premessa è falsa: la riga non conta.
- **p = F, r = V**: ¬r → ¬p = V, r = V, p = **F**. Premesse vere, conclusione **falsa**.
- p = F, r = F: ¬r → ¬p = V, r = F, p = F. Una premessa è falsa: la riga non conta.

Le premesse sono tutte e due vere solo nella prima e nella terza riga. Nella prima la conclusione p è vera, ma nella **terza** (p falsa, r vera) è **falsa**: ecco il controesempio. Basta una riga così: **la regola 4 non è valida**.

Perché ¬r → ¬p è vera nella terza riga? Con r = V la sua ipotesi ¬r è falsa, e un'implicazione con ipotesi falsa è vera (cap. 16).

![A sinistra la tavola della regola 3, a destra quella della regola 4: in rosso la riga con premesse vere e conclusione falsa.](figure/fond/regole_tavole.png|15)

Come sottolineato a lezione, la tavola di verità è più lenta ma sicura, ed è la scelta migliore quando le lettere e le formule sono poche. Con molte lettere le righe diventano troppe (2 elevato al numero delle lettere) e conviene usare gli altri metodi.

## Strada 2: la dimostrazione
Per le regole **valide** c'è un'alternativa alla tavola: **dimostrare** la conclusione, partendo dalle premesse e usando le regole già note, in particolare il **modus ponens** (da p → q e p si ricava q).

**Regola 5: p → r, r → q, p ⊢ q.** Si parte da p. Per il modus ponens con p → r si ricava r. Poi, per il modus ponens con r → q, si ricava q. Sono due passi che «trasportano la verità» lungo le frecce, come in un gioco enigmistico in cui si segue il percorso p → r → q. Questa è la **transitività dell'implicazione**, e la regola è valida.

**Regola 1: p → r, p → q ⊢ p → (r ∧ q).** La conclusione è un'implicazione. Per dimostrare un'implicazione la si assume come ipotesi: si **assume anche p**. Ora si hanno tre assunzioni: p → r, p → q e p, e bisogna ricavare r ∧ q. Per ricavare una congiunzione bisogna ricavare **tutti e due** i pezzi:
1. da p e p → r, per modus ponens, si ricava r;
2. da p e p → q, per modus ponens, si ricava q;
3. da r e q si ricava r ∧ q.

La regola è valida. Come sottolineato a lezione, questa è una deduzione «meccanica»: nessun essere umano scende a questo livello di dettaglio, ma è il livello a cui lavorerebbe una macchina.

**In parole povere:** dimostrare una regola vuol dire costruire un percorso logico dalle premesse alla conclusione, un passo alla volta, dove ogni passo è una regola già nota. Se il percorso esiste, la regola è valida.

## Strada 3: cercare un controesempio
Se la dimostrazione si blocca, **il blocco è un indizio**: forse la regola non è valida. Allora, invece di insistere, si prova a cercare un controesempio, cioè una scelta di valori di verità per cui **le premesse sono vere e la conclusione è falsa**. Come detto a lezione, il fallimento di un tentativo di dimostrazione suggerisce proprio dove cercare.

**Regola 2: p → (r ∨ q), r → ¬q ⊢ p → r.** Si assume p e si prova a ricavare r. Dalla prima premessa e p, per modus ponens, si ricava r ∨ q: ma questo non basta, perché potrebbe essere vera solo q. La seconda premessa, r → ¬q, entra in gioco solo se r è vera; se r è falsa non dice nulla. Ci si è arenati proprio nel caso **p vera, r falsa, q vera**. Lo si controlla:
- p → (r ∨ q) = V → (F ∨ V) = V → V = **V**;
- r → ¬q = F → F = **V** (ipotesi falsa, quindi implicazione vera);
- p → r = V → F = **F**.

Le due premesse sono vere e la conclusione è falsa: ecco il controesempio. **La regola 2 non è valida.**

Come detto a lezione rispondendo a una domanda, cercare il controesempio è il primo passo di una tecnica che si chiama **ragionamento per contraddizione**: invece di dimostrare che la regola è vera, la si **suppone falsa** e si vede dove si arriva. Se si arrivasse a una situazione impossibile, la regola sarebbe valida (la tecnica verrà ripresa più avanti nel corso); qui invece si trova una situazione possibile, e quindi la regola non è valida.

**Regola 3: p → r, r → q ⊢ q.** Somiglia alla transitività, ma c'è una differenza: **manca la premessa p**. Per il modus ponens servirebbe una verità di partenza, e qui non c'è. Per trovare il controesempio si ragiona **all'indietro**, a partire dalla conclusione, che deve essere falsa:
1. si vuole q **falsa**;
2. la premessa r → q deve essere vera. Se r fosse vera, allora per il modus ponens q sarebbe vera, ma si è scelto q falsa: quindi **r deve essere falsa**;
3. la premessa p → r deve essere vera con r falsa. Se p fosse vera, allora r sarebbe vera: quindi **p deve essere falsa**.

(In parole povere: se una freccia «A → B» è vera e B è falso, allora A non può essere vero. Quindi la **falsità si sposta da destra a sinistra**, mentre la verità si sposta da sinistra a destra: è l'idea del contrapositivo, cap. 17.)

Si ottiene p, r, q tutte false. Si controlla: p → r = F → F = V, r → q = F → F = V, e q = F. Le premesse sono vere e la conclusione è falsa: **la regola 3 non è valida**. Su 8 righe di tavola ne basta una, e questa è anche l'unica: partendo dall'ipotesi che la regola fosse falsa si è arrivati a un'unica scelta dei valori (il «triplo zero», nell'ordine con cui si scrive la tavola, che parte da tutti V e finisce con tutti F).

Come sottolineato a lezione, per formule grandi il ragionamento automatico usa quasi solo la deduzione, perché solo sui casi piccoli si riesce a usare la tavola di verità; se però ci si trova meglio con la tavola, la si usa: è importante sapere che esistono anche le scorciatoie.

## Strada 4: riscrivere la regola in una forma più semplice
Una regola si può anche **trasformare in un'altra equivalente**, già nota. Si riprende la regola 4: ¬r → ¬p, r ⊢ p. Per il **contrapositivo** (cap. 17) ¬r → ¬p è equivalente a p → r: si scambiano ipotesi e conclusione e si negano entrambe, e le due negazioni della seconda forma si cancellano. La regola diventa allora: **p → r, r ⊢ p**, cioè «da p → r e r ricavo p». Questa è la fallacia dell'**affermazione della conclusione** (cap. 19): l'implicazione non si può invertire, perché r può essere vera anche quando p è falsa. Quindi la regola non è valida. Come sottolineato a lezione, è un altro modo di arrivare alla stessa conclusione, riconducendosi a un caso già noto.

## Come scegliere
In sintesi, i quattro metodi:
- **Tavola di verità**: sicura e meccanica, ma lunga; la scelta migliore con poche lettere.
- **Dimostrazione**: per le regole valide, quando si vede un percorso fatto di modus ponens e regole note.
- **Controesempio**: quando la dimostrazione si blocca; si ragiona all'indietro (conclusione falsa, falsità verso sinistra) e si verifica il risultato.
- **Riscrittura**: quando si riconosce una forma già vista, come il contrapositivo o la doppia negazione.

**In parole povere:** se la regola è giusta, una dimostrazione lo prova; se è sbagliata, basta un caso in cui le premesse sono vere e la conclusione no. Un blocco nella dimostrazione è il segnale per cercare quel caso.

I capitoli successivi tornano ai quantificatori, ora con più quantificatori nella stessa formula.
