# 19. Argomenti e Regole di Inferenza
## Il ragionamento deduttivo
Si parte da un esempio. Supponiamo di sapere tre cose: il bug è nel modulo 17 oppure nel modulo 81; il bug è un errore numerico; il modulo 81 non contiene errori numerici. Assumendo che queste affermazioni siano vere, è ragionevole concludere che il bug è nel modulo 17.

Questo processo, in cui da una sequenza di proposizioni si trae una conclusione, si chiama **ragionamento deduttivo**. Le proposizioni di partenza si chiamano **ipotesi** (o **premesse**), la proposizione che ne segue si chiama **conclusione**, e l'insieme di ipotesi più conclusione è un **argomento** (deduttivo). Molte dimostrazioni di matematica e di informatica sono argomenti deduttivi.

Un argomento ha sempre la stessa forma: «se p₁ e p₂ e … e p_{n}, allora q». È la forma di un'implicazione, e questo collegamento con i capitoli 16-18 è la chiave per capire quando un argomento «funziona».

## Argomento valido
**Definizione.** Un **argomento** è una successione di proposizioni p₁, p₂, …, p_{n} (le ipotesi) seguita da una proposizione q (la conclusione), che si scrive con le ipotesi una sotto l'altra e la conclusione sotto una riga, preceduta dal simbolo ∴ («quindi»), oppure in una riga sola come p₁, p₂, …, p_{n} / ∴ q. L'argomento si dice **valido** se, ogni volta che p₁ e p₂ e … e p_{n} sono tutte vere, anche q è vera; altrimenti si dice **non valido** (o una **fallacia**).

In un argomento valido si dice che la conclusione segue dalle ipotesi, ma bisogna capirsi su che cosa si afferma: **non** si dice che la conclusione è vera, ma solo che se si accettano le ipotesi si deve accettare anche la conclusione. Un argomento è valido per la sua **forma** e non per il suo contenuto: due argomenti con la stessa forma sono entrambi validi o entrambi non validi, anche se parlano di cose completamente diverse.

In termini dei capitoli precedenti, dire che l'argomento è valido equivale a dire che l'implicazione (p₁ ∧ p₂ ∧ … ∧ p_{n}) → q non è mai falsa: ipotesi tutte vere e conclusione falsa è l'unico caso che la renderebbe falsa.

Un argomento più lungo si costruisce a passi, e ciascun passo deve produrre una conclusione intermedia valida. Le **regole di inferenza** sono, in breve, argomenti validi già noti, che si usano come mattoni all'interno di un argomento più grande.

## Come si verifica la validità
Il primo metodo è la **tavola di verità**: si scrivono i valori di tutte le proposizioni coinvolte e si controlla che in ogni riga in cui le ipotesi sono vere lo sia anche la conclusione. Il secondo metodo è un **ragionamento diretto**, che evita la tavola: si suppone che le ipotesi siano vere e si verifica che la conclusione non può essere falsa.

Esempio. Si vuole stabilire se è valido l'argomento p → q, p / ∴ q.

![A sinistra la tavola del modus ponens: nell'unica riga con le due ipotesi vere (riquadro verde) lo è anche la conclusione. A destra la tavola dell'argomento p → q, q / ∴ p: nella terza riga le ipotesi sono vere e la conclusione è falsa.](figure/fond/logica_argomenti_tavole.png|14.5)

Con la tavola (a sinistra nella figura) si osserva che ogni volta che p → q e p sono entrambe vere, lo è anche q: l'argomento è valido. Con il ragionamento diretto: si suppone che p → q e p siano vere; allora q deve essere vera, perché altrimenti p → q sarebbe falsa (ipotesi vera e tesi falsa). Questo argomento è usato continuamente e si chiama **modus ponens** o **legge del distacco**.

## Le regole di inferenza per le proposizioni
Esistono diverse regole utili, ognuna verificabile con una tavola di verità; le principali sono nella figura.

![Le regole di inferenza per le proposizioni: premesse sopra la riga, conclusione sotto.](figure/fond/logica_regole_inferenza.png|13)

- **Modus ponens**: da p → q e p si ricava q.
- **Modus tollens**: da p → q e ¬q si ricava ¬p.
- **Addizione**: da p si ricava p ∨ q.
- **Semplificazione**: da p ∧ q si ricava p.
- **Congiunzione**: da p e da q si ricava p ∧ q.
- **Sillogismo ipotetico**: da p → q e q → r si ricava p → r.
- **Sillogismo disgiuntivo**: da p ∨ q e ¬p si ricava q.

Per riconoscere la regola in un argomento scritto a parole bisogna prima tradurlo in simboli, come nell'esempio seguente. «Se il computer ha un gigabyte di memoria, allora può eseguire il programma. Se può eseguire il programma, allora la grafica sarà d'effetto. Quindi, se il computer ha un gigabyte di memoria, la grafica sarà d'effetto.» Con p = «il computer ha un gigabyte di memoria», q = «può eseguire il programma» e r = «la grafica sarà d'effetto», l'argomento è p → q, q → r / ∴ p → r: la regola usata è il **sillogismo ipotetico**.

## Una fallacia frequente: affermare la conclusione
Non tutti gli argomenti che «sembrano» validi lo sono. Si consideri: «Se 2 = 3, allora ho mangiato il cappello. Ho mangiato il cappello. Quindi 2 = 3.» Con p = «2 = 3» e q = «ho mangiato il cappello», l'argomento è p → q, q / ∴ p.

Se fosse valido, ogni volta che p → q e q sono vere dovrebbe esserlo anche p. Ma questo non succede: con p falsa e q vera, l'implicazione p → q è vera per difetto (ipotesi falsa), q è vera, e la conclusione p è falsa. L'argomento **non è valido**. Questa fallacia si chiama **affermazione della conclusione** (in inglese *fallacy of affirming the conclusion*): è lo stesso errore, già visto nel capitolo 17, di scambiare un'implicazione con la sua conversa. Si arriva alla stessa conclusione guardando la tavola (a destra nella figura): nella terza riga le ipotesi sono vere e la conclusione è falsa.

## Argomenti in più passaggi
Quando un argomento non coincide con una sola regola, si procede a passi, applicando una regola alla volta e usando le conclusioni intermedie come nuove ipotesi.

**Il bug nei moduli.** Si ripete l'argomento d'apertura con p = «il bug è nel modulo 17», q = «il bug è nel modulo 81» e r = «il bug è un errore numerico». Le ipotesi sono p ∨ q, r e r → ¬q (il modulo 81 non ha errori numerici, quindi se il bug è numerico non è nel 81). Da r → ¬q e r, per il modus ponens si ricava ¬q. Da p ∨ q e ¬q, per il sillogismo disgiuntivo, si ricava p: il bug è nel modulo 17. L'argomento è valido.

**La squadra.** Sono date le ipotesi: se la squadra prende un buon difensore, può battere la prima avversaria; se può battere la prima, può battere la seconda; se può battere la prima, può battere la terza; la squadra prende un buon difensore. Si vuole mostrare che ne segue che la squadra può battere la seconda e la terza. Con p = «prende un buon difensore», q = «batte la prima», r = «batte la seconda» e s = «batte la terza», le ipotesi sono p → q, q → r, q → s e p.
1. Da p → q e q → r, per il sillogismo ipotetico, p → r.
2. Da p → r e p, per il modus ponens, r.
3. Da p → q e q → s, per il sillogismo ipotetico, p → s.
4. Da p → s e p, per il modus ponens, s.
5. Da r e s, per la congiunzione, r ∧ s.
Poiché r ∧ s dice che la squadra batte la seconda e la terza, la conclusione segue dalle ipotesi.

## Un consiglio pratico
La validità di un argomento molto breve si può verificare con una tavola di verità, ma, nella pratica, argomenti e dimostrazioni usano le regole di inferenza: le tavole crescono in modo esponenziale con il numero di proposizioni (capitolo 18), mentre una catena di regole resta corta e leggibile.
