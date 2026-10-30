# 35. La Dimostrazione della Scomposizione in Cicli e Come Trovare il Tipo
## L'idea della dimostrazione
Si dimostra il teorema del capitolo precedente: ogni permutazione π ≠ id si scrive come composizione di cicli a due a due disgiunti. La dimostrazione è esattamente la generalizzazione del procedimento a «frecce» visto nel capitolo 33: si parte da un numero, si seguono le frecce e si osserva che il percorso si richiude.

**Passo 1: trovare un primo ciclo.** Si considera l'insieme T dei numeri che la permutazione **sposta effettivamente**:
T = { x ∈ {1, …, n} : π(x) ≠ x }.
Non si guardano i numeri lasciati fermi. Poiché π non è l'identità, c'è almeno un x con π(x) ≠ x, quindi **T non è vuoto**; inoltre è finito, perché è un sottoinsieme di {1, …, n}.

Si sceglie a piacere un elemento di T e lo si chiama t₁. Si segue il suo percorso: t₂ = π(t₁), t₃ = π(t₂), e così via. Si può andare avanti all'infinito incontrando sempre numeri nuovi? No: i numeri sono solo n, quindi a un certo punto si incontra un numero già incontrato prima; sia t_j il primo elemento che si ripete. Ora, dove si può richiudere il percorso? Se fosse j > 1, il numero t_j sarebbe immagine di due elementi diversi (il suo predecessore t_{j−1} e l'elemento che lo ha raggiunto la seconda volta, che è diverso da t_{j−1} perché t_j è il primo che si ripete), ma questo è impossibile perché **π è iniettiva**. Quindi il percorso si può richiudere solo nell'**unico elemento che finora non ha ricevuto nessuna freccia, cioè t₁**. Dunque a un certo punto la freccia torna a t₁, e si ottiene un ciclo C₁ = (t₁ t₂ … t_ℓ) «dentro» π. Il passaggio usa in modo essenziale che π sia iniettiva.

**Passo 2: gli altri cicli.** Dall'insieme T si tolgono tutti gli elementi del ciclo trovato, ottenendo T \ {t₁, …, t_ℓ}. Possono succedere due cose.
- Se questo insieme è **vuoto**, gli unici elementi spostati da π sono quelli di C₁, quindi **π = C₁** e il teorema è dimostrato.
- Se **non è vuoto**, si sceglie un elemento s₁ di quell'insieme e si ripete lo stesso discorso: si segue s₁, π(s₁) = s₂, π(s₂) = s₃, … e il percorso si richiude su s₁, dando un secondo ciclo C₂.

**Il secondo ciclo è disgiunto dal primo.** Sia s_j il primo elemento del percorso che cade in C₁ (j > 1, perché s₁ è stato scelto fuori da C₁) e sia s_j = t_i. Allora s_{j−1} non sta in C₁, mentre t_{i−1} sta in C₁ (con t₀ := t_ℓ): sono due elementi diversi con la stessa immagine, e questo è impossibile per l'iniettività.

**Passo 3: il procedimento finisce.** Si toglie anche C₂ e si riprende: se l'insieme resta non vuoto, si trova un terzo ciclo C₃, e così via. Perché si arriva alla fine? Si ponga T₁ = T \ {t₁, …, t_ℓ}, poi T₂ = T₁ \ {s₁, s₂, …}, e così via. Il numero di elementi dell'insieme ancora da considerare **diminuisce davvero a ogni passo**: |T| > |T₁| > |T₂| > …, e un numero naturale non può decrescere per sempre. Dopo un numero finito di passi l'insieme diventa vuoto, e a quel punto ogni elemento di T sta in uno e un solo ciclo costruito, e i cicli sono a due a due disgiunti. Quindi la loro composizione manda ogni x ∈ T in π(x) e lascia fermi gli altri numeri, cioè coincide con π. ∎

Questa dimostrazione costruisce la scrittura, cioè prova l'**esistenza**; l'unicità a lezione è stata solo enunciata.

(In parole povere: si prende un numero spostato e si segue il suo giro fino a chiuderlo; poi se ne prende uno fuori da quel giro e si fa lo stesso, e così via finché non restano più numeri spostati.)

## Un esempio con 12 elementi
Sia π la permutazione di {1, …, 12} (scritta a caso) definita da: π(1) = 7, π(2) = 9, π(3) = 11, π(4) = 1, π(5) = 6, π(6) = 2, π(7) = 5, π(8) = 4, π(9) = 12, π(10) = 3, π(11) = 10, π(12) = 8.

Si parte da 1 (uno qualsiasi va bene) e si seguono le frecce: 1 va in 7, 7 va in 5, 5 va in 6, 6 va in 2, 2 va in 9, 9 va in 12, 12 va in 8, 8 va in 4, 4 torna in 1. Primo ciclo: **(1 7 5 6 2 9 12 8 4)**, di lunghezza 9.

Si tolgono questi numeri: restano 3, 10, 11. Si parte da 3: 3 va in 11, 11 va in 10, 10 torna in 3. Secondo ciclo: **(3 11 10)**, di lunghezza 3.

Non resta niente da considerare, quindi π è la composizione di questi due cicli disgiunti, e ha **tipo (9, 3)**.

## Come si trova il tipo
Come si determina il tipo, quando la permutazione è data come composizione di cicli che non sono disgiunti? Il procedimento con la tabella (una riga per ogni ciclo, poi si cancellano le righe intermedie tenendo la prima e l'ultima) funziona sempre ma è lungo. C'è una **scorciatoia**, che richiede un po' di pratica: non si scrive nessuna tabella, ma si segue direttamente un numero attraverso tutte le funzioni, **da destra a sinistra**, perché si stanno componendo funzioni: si applica prima la funzione più a destra, poi quella alla sua sinistra, e così via. Si ottiene l'immagine di un numero, poi si riparte da quell'immagine per seguire il ciclo, finché non si richiude; poi si passa a un numero non ancora toccato.

**Esempio** (calcolato apposta per mostrare il metodo). Sia π = (1 2 3) ∘ (3 4 5) ∘ (1 5) in S₅: si applica prima (1 5), poi (3 4 5), poi (1 2 3).
- 1 → 5 (con (1 5)) → 3 (con (3 4 5)) → 1 (con (1 2 3)): π(1) = 1.
- 2 → 2 → 2 → 3: π(2) = 3.
- 3 → 3 → 4 → 4: π(3) = 4.
- 4 → 4 → 5 → 5: π(4) = 5.
- 5 → 1 → 1 → 2: π(5) = 2.

Quindi π = (2 3 4 5): un solo ciclo di lunghezza 4, con 1 fisso. Il tipo è **(4)**, anche se i cicli di partenza erano due di lunghezza 3 e uno di lunghezza 2 (e non erano disgiunti).

**Un altro esempio** (anche questo calcolato apposta). (1 3) ∘ (1 2 3): 1 → 2 → 2; 2 → 3 → 1; 3 → 1 → 3. Il risultato è (1 2): una composizione di un 3-ciclo e di un 2-ciclo che dà un 2-ciclo.

Come sottolineato a lezione, la situazione è molto «caotica»: si parte da cicli di certe lunghezze e si finisce con cicli di lunghezze del tutto diverse, e non c'è altro modo di trovare il tipo che fare il calcolo. Il tipo si legge sempre dalla scrittura in cicli **disgiunti**, non da quella di partenza. Nell'esempio fatto a lezione si partiva da tre cicli e si finiva con un ciclo di lunghezza 4 e uno di lunghezza 3, quindi con tipo (4, 3).

Anche nel calcolo conviene verificare sempre il risultato, perché è facile sbagliare.

Il capitolo successivo si chiede che cosa succede ripetendo più volte una stessa permutazione.
