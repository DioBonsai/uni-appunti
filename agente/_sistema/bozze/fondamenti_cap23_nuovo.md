# 23. Quantificatori su Domini Concreti: Ripasso, Divisori e Insiemi Annidati
## Ripasso: dualità e leggi di De Morgan
La lezione riprende i quantificatori dei capitoli 20-22 (definizione di ∃ e ∀ su un dominio, dualità, leggi di De Morgan per i quantificatori, dominio finito) e li usa su esempi concreti. Qui si richiamano solo i punti che servono e si aggiungono alcune osservazioni nuove.

Come sottolineato a lezione, la definizione dell'esistenziale è «molto brusca»: tutti falsi, e basta un solo x vero per rendere vero l'enunciato; non ci sono sfumature, si può dire solo vero o falso. Ogni quantificatore è sempre legato a un dominio del discorso, anche quando per brevità non lo si scrive.

**In parole povere:** ∃ chiede «ne basta uno» e ∀ chiede «devono essere tutti». Una definizione si trasforma nell'altra scambiando vero e falso, sia in P(x) sia nel valore finale.

I due quantificatori sono **duali** l'uno dell'altro, come la congiunzione e la disgiunzione (cap. 22). La **negazione** invece è **autoduale**: se nella sua definizione si scambia il vero con il falso, si riottiene la negazione stessa. Come sottolineato a lezione, è importante ricordarlo perché, quando due connettivi (o due quantificatori) sono duali, **soddisfano le leggi di De Morgan**: negare uno equivale ad affermare l'altro e a negare i suoi argomenti.

**In parole povere:** «duale» vuol dire «specchio»: ∀ è lo specchio di ∃, ∧ è lo specchio di ∨, e la negazione è uno specchio di sé stessa.

Le due leggi, ¬∀x P(x) = ∃x ¬P(x) e ¬∃x P(x) = ∀x ¬P(x), sono quelle del cap. 22. Dette a parole sembrano ovvie: se non è vero che P(x) vale per ogni x, c'è almeno un x per cui è falsa; se non esiste nemmeno un x con P(x), allora per ogni x vale ¬P(x). Come sottolineato a lezione, è però importante osservare che **si giustificano a partire dalle definizioni**: non sono affermazioni nuove. La seconda si ottiene dalla prima scambiando i quantificatori, oppure direttamente partendo dal lato sinistro e facendo sparire la negazione con la doppia negazione. Si ricordi anche che la negazione lega più strettamente degli altri connettivi, per questo le parentesi non si scrivono sempre.

## La quantificazione è una congiunzione (o disgiunzione) generalizzata
Se il dominio sono gli interi positivi, «per ogni x P(x)» è come dire P(1) ∧ P(2) ∧ P(3) ∧ … all'infinito, e «esiste x P(x)» è come P(1) ∨ P(2) ∨ P(3) ∨ …; un'espressione infinita non si può scrivere, ma l'idea è questa. Se il dominio è **finito** l'analogia diventa una coincidenza perfetta: per D = {1, 2, 3, 4}, ∀x ∈ D P(x) è esattamente P(1) ∧ P(2) ∧ P(3) ∧ P(4), e ∃x ∈ D P(x) è P(1) ∨ P(2) ∨ P(3) ∨ P(4).

Come sottolineato a lezione, la quantificazione è più **sintetica** (con cento elementi si scrive una sola volta ciò che richiederebbe una pagina di congiunzioni), ma a livello di equivalenza logica le due scritture sono la stessa cosa. Per questo le leggi di De Morgan per i quantificatori si possono dedurre da quelle dei connettivi, sostituendo il quantificatore universale con la congiunzione e quello esistenziale con la disgiunzione.

**In parole povere:** su un dominio piccolo si può sostituire «per ogni» con una lunga catena di «e», e «esiste» con una lunga catena di «o». Il simbolo del quantificatore è solo un'abbreviazione di quella catena.

## Esempio: i divisori di 10
Sia P(n) la funzione proposizionale «n divide 10», con dominio gli interi positivi. I divisori di 10 sono 1, 2, 5 e 10: sono solo quattro. Il predicato non ha restrizioni, quindi anche i divisori banali, 1 e 10, valgono, e 10 = 2 · 5 ha esattamente quattro divisori. Si valutano alcuni enunciati.
- **∃n P(n)** è vero: basta un caso, per esempio P(1).
- **∀n P(n)** è falso: non tutti gli n dividono 10. Per esempio 3 non divide 10, quindi P(3) è falsa; i casi in cui P(n) è falsa sono infiniti (3, 4, 6, 7, 8, 9 e poi tutti da 11 in poi), ma per rendere falso un ∀ ne basta uno.
- **¬∃n P(n)** è falso, perché ∃n P(n) è vero. Per la seconda legge di De Morgan è uguale a ∀n ¬P(n), che è falso perché ¬P(1) è falsa (1 divide 10).
- **¬∀n P(n)** è vero: è la negazione di un enunciato falso. Per la prima legge di De Morgan è uguale a ∃n ¬P(n), che è vero: si prende il primo non divisore, 3.

Ci sono due modi di arrivare alla stessa risposta: si valutano direttamente le definizioni, oppure si trasforma l'enunciato con De Morgan e si ricade su un caso già noto.

## Esempio: tre insiemi uno dentro l'altro
Sia D l'insieme degli studenti iscritti a un'università italiana. Sia Q(x) il predicato «x è iscritto a Torino» e P(x) il predicato «x è iscritto a Informatica a Torino». Gli studenti che soddisfano P sono un sottoinsieme di quelli che soddisfano Q, che a loro volta sono un sottoinsieme di D: tre insiemi uno dentro l'altro.

![Gli iscritti a Informatica a Torino (P) sono contenuti negli iscritti a Torino (Q), a loro volta contenuti negli iscritti a un'università italiana (D).](figure/fond/insiemi_annidati.png|9)

Valori di verità, con D come dominio:
- **∀x (P(x) → Q(x))** è vera: chiunque sia iscritto a Informatica a Torino è anche iscritto a Torino, perché P è incluso in Q. In altre parole P è incluso in Q (insiemisticamente). A lezione l'esempio si apre con **∃x (P(x) → Q(x))**, che è vera: nel dominio ci sono molti studenti e per ciascuno l'implicazione vale, quindi ne basta uno.
- **∀x (Q(x) → P(x))** è falsa: uno studente iscritto a Legge a Torino rende vera Q e falsa P, quindi l'implicazione è falsa per lui.
- **∀x (P(x) ∨ Q(x))** è falsa: uno studente iscritto a Milano rende false entrambe.
- **∃x (P(x) ∧ Q(x))** è vera: uno studente di Informatica a Torino rende vere entrambe.
- **∃x (P(x) ∨ Q(x))** è vera: basta lo stesso studente.

**In parole povere:** per smentire un «per ogni» basta trovare un solo controesempio (qui lo studente di Legge o quello di Milano); per confermare un «esiste» basta trovare un solo esempio (uno studente di Informatica a Torino). Il dominio conta: lo studente di Milano è nel dominio D, e questo è ciò che rende falso ∀x (P(x) ∨ Q(x)).

## Un errore tipico nel pseudocodice
A lezione si è commentato un pseudocodice che avrebbe dovuto decidere un quantificatore universale su un dominio finito (si veda il capitolo 21), ma conteneva l'errore più comune: restituire il risultato **dentro** il ciclo. Con un'istruzione `return` che scatta già al primo elemento il ciclo diventa «degenere»: si guarda solo P(d₁), e se P(d₁) è falsa si restituisce falso, altrimenti vero, ricopiando il valore di verità del primo elemento. Come sottolineato a lezione, il codice corretto per ∀ restituisce **falso** non appena trova un elemento con P falsa, e restituisce **vero solo dopo aver percorso l'intero ciclo** senza trovare falsi: il `return true` deve stare fuori dal `for`. Il motivo è che per ∀ un valore falso è un'informazione sufficiente per fermarsi, mentre un valore vero non lo è, perché l'ultimo elemento potrebbe essere falso.

Il capitolo successivo passa dai quantificatori alle regole di inferenza e alla loro verifica.
