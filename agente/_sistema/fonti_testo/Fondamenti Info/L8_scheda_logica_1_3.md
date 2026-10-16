# L8_scheda_logica_1_3

<!-- pagina 1 -->
SCHEDA DI STUDIO APPROFONDITA
Capitolo 1.3 (Parte 2): Proposizioni Condizionali ed Equivalenza
Logica
Corso di Fondamenti di Informatica — Testo: R. Johnsonbaugh, Discrete Mathematics
Questa scheda costituisce un supporto completo per lo studio teorico e pratico della Sezione 1.3 (Lezione del 15
Ottobre 2026). Contiene definizioni formali, traduzioni dal linguaggio naturale, tabelle di verit`a, forme correlate
(conversa, contrapposta, bicondizionale) ed equivalenze fondamentali con dimostrazioni dettagliate.
—
1. La Proposizione Condizionale (Implicazione Logica: p →q)
1.3.1 Definizione Formale di Proposizione Condizionale
Siano p e q due proposizioni. La proposizione ”se p, allora q”, indicata simbolicamente con
p −→q
`e chiamata proposizione condizionale (o implicazione logica).
 p (Antecedente o Ipotesi): La condizione da cui si parte.
 q (Conseguente o Conclusione): Il risultato che consegue dall’ipotesi.
Tabella di Verit`a dell’Implicazione Logica
L’implicazione p →q afferma che se l’ipotesi p `e vera, allora la conclusione q deve necessariamente essere vera.
Un’implicazione viene infranta (FALSA) esclusivamente quando l’ipotesi p `e VERA e la conclusione q `e
FALSA. In tutti gli altri tre casi l’implicazione `e considerata VERA.
p (Ipotesi)
q (Conclusione)
p →q
Spiegazione e Interpretazione
T
T
T
Ipotesi vera e promessa mantenuta.
T
F
F
UNICO CASO DI FALSIT`A: Ipotesi vera ma la promessa `e infranta!
F
T
T
Vera per difetto (Vacuously True): L’ipotesi non si `e verificata.
F
F
T
Vera per difetto (Vacuously True): L’ipotesi non si `e verificata.
1.3.2 Concetto di ”Vera per Difetto” (Vacuously True / True by Default)
Quando l’ipotesi p `e FALSA, la proposizione condizionale p →q `e automaticamente **VERA**, indipen-
dentemente dal valore di verit`a di q.
 Esempio formale: ”Se la Terra ha 6 lune, allora 1 < 3.”
 Poich´e la Terra non ha 6 lune (p `e Falsa), l’intera affermazione `e VERA per difetto.
 Motivazione matematica: Se stabiliamo il teorema ∀x ∈R, (x > 0 →x2 > 0), quando x = −2 l’ipotesi
−2 > 0 `e Falsa. Perch´e il teorema rimanga valido universale per ogni numero reale, l’implicazione F →T
deve valere T.
—
2. Traduzione dal Linguaggio Naturale all’Implicazione
Nel linguaggio naturale e nei quesiti d’esame, l’implicazione p →q non compare sempre nella forma classica ”Se
p, allora q”. Le seguenti formulazioni sono **completamente equivalenti a p →q**:
1

<!-- pagina 2 -->
Espressione nel Linguaggio Naturale
Formulazione Simbolica
Identificazione Ipotesi/Conclusione
”Se p, allora q”
p →q
p = Ipotesi, q = Conclusione
”p implica q”
p →q
p = Ipotesi, q = Conclusione
”q se p”
p →q
p (dopo il ”se”) = Ipotesi, q = Conclusione
”p solo se q”
p →q
ATTENZIONE: p = Ipotesi, q = Conclusione
”p `e condizione sufficiente per q”
p →q
p `e la Condizione Sufficiente (Ipotesi)
”q `e condizione necessaria per p”
p →q
q `e la Condizione Necessaria (Conclusione)
”Quando p, allora q”
p →q
p = Ipotesi, q = Conclusione
—
3. Forme Proposizionali Correlate: Conversa e Contrapposta
A partire da un’implicazione primaria p →q, si definiscono tre proposizioni derivate fondanti:
Proposizioni Derivate
1. Proposizione Condizionale Originaria: p −→q
2. Conversa (Converse): q −→p (Inverte il ruolo di ipotesi e conclusione).
3. Contrapposta (Contrapositive / Transposition): ¬q −→¬p (Inverte i ruoli E nega entrambe le
componenti).
Distinzione Critica: La Conversa NON `e Equivalente all’Implicazione!
Un’implicazione p →q e la sua conversa q →p NON hanno lo stesso valore di verit`a.
 Esempio:
– Implicazione (p →q): ”Se Jerry vince la lotteria (p), allora va al college (q).” (VERO)
– Conversa (q →p): ”Se Jerry va al college (q), allora ha vinto la lotteria (p).” (FALSO: potrebbe
andarci con i suoi risparmi!).
—
4. La Proposizione Bicondizionale (p ↔q)
1.3.8 Definizione di Proposizione Bicondizionale
Se p e q sono due proposizioni, la proposizione ”p se e solo se q” (in inglese ”p if and only if q”, abbreviato
in ”p iff q”) `e detta proposizione bicondizionale ed `e indicata con:
p ←→q
Regola del Valore di Verit`a: p ↔q `e VERA quando p e q hanno lo STESSO valore di verit`a
(entrambe vere o entrambe false). `E FALSA quando hanno valori discordi.
Tabella di Verit`a del Bicondizionale e Relazione con l’Implicazione Doppia
p
q
p →q
q →p
(p →q) ∧(q →p)
p ↔q
T
T
T
T
T
T
T
F
F
T
F
F
F
T
T
F
F
F
F
F
T
T
T
T
2

<!-- pagina 3 -->
Equivalenza Fondamentale del Bicondizionale
Dalla tabella di verit`a sopra si evince chiaramente l’equivalenza:
p ←→q
≡
(p →q) ∧(q →p)
Traduzione in linguaggio naturale: ”p `e condizione necessaria e sufficiente per q”.
—
5. Equivalenza Logica (P ≡Q)
1.3.10 Definizione di Equivalenza Logica
Due proposizioni composte P e Q formate dai medesimi atomi p1, p2, . . . , pn si dicono logicamente equiv-
alenti (e si scrive P ≡Q o P ⇐⇒Q) se e solo se producono la medesima colonna finale nella tabella
di verit`a per qualsiasi combinazione dei valori di verit`a degli atomi.
Teoremi e Leggi di Equivalenza Fondamentali della Sezione 1.3
5.1.1
A. Teorema di Equivalenza della Contrapposta (Theorem 1.3.18)
La proposizione condizionale p →q `e **logicamente equivalente** alla sua contrapposta ¬q →¬p:
p →q
≡
¬q →¬p
Dimostrazione tramite Tabella di Verit`a:
p
q
¬p
¬q
p →q
¬q →¬p
Risultato
T
T
F
F
T
T
Identici
T
F
F
T
F
F
Identici
F
T
T
F
T
T
Identici
F
F
T
T
T
T
Identici
5.1.2
B. Negazione dell’Implicazione (Example 1.3.13)
La negazione di un’implicazione NON `e un’altra implicazione, ma una congiunzione:
¬(p →q)
≡
p ∧¬q
Esempio del Libro
 Proposizione originaria (p →q): ”Se Jerry riceve una borsa di studio, allora va al college.”
 Negazione (¬(p →q)): ”Jerry riceve la borsa di studio E non va al college.” (p ∧¬q).
5.1.3
C. Riscrittura dell’Implicazione come Disgiunzione (Exercise 80)
L’operatore di implicazione pu`o essere completamente eliminato usando negazione e disgiunzione:
p →q
≡
¬p ∨q
5.1.4
D. Leggi di De Morgan per la Logica Proposizionale (Example 1.3.11)
¬(p ∨q)
≡
¬p ∧¬q
¬(p ∧q)
≡
¬p ∨¬q
—
3

<!-- pagina 4 -->
6. Sintesi dei Trabocchetti Classici da Esame (Sezione 1.3)
4 Errori Frequenti da Evitare Assolutamente
1. Scambiare Implicazione e Conversa: Credere che p →q implichi q →p. Ricorda l’esempio del college!
2. Tradurre Erroneamente ”Solo Se”: L’espressione ”p solo se q” significa p →q e NON q →p. Il ”solo
se” introduce la condizione necessaria (il conseguente).
3. Negare l’Implicazione in Modo Errato: Scrivere la negazione di p →q come p →¬q o ¬p →¬q. La
negazione corretta `e p ∧¬q.
4. Dimenticare la Precedenza: Nell’ordine degli operatori, l’implicazione (→) ha la precedenza **pi`u
bassa di tutte** (dopo ¬, ∧, ∨).
Espressione: p ∨q →¬r
=⇒
Interpretazione: (p ∨q) →(¬r)
4
