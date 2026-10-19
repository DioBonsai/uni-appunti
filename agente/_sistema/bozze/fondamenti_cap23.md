# 23. Regole di Inferenza per gli Enunciati Quantificati
## Dal capitolo 19 ai quantificatori
Si chiude la sezione sui quantificatori vedendo come si estendono le regole di inferenza del capitolo 19 agli enunciati con ∀ e ∃, e come si combinano con quelle per le proposizioni.

Si supponga che ∀x P(x) sia vero. Per la definizione di universale, P(x) è vera per ogni x del dominio D; quindi, per un particolare d ∈ D, P(d) è vera. L'argomento ∀x P(x) / ∴ P(d) con d ∈ D è perciò valido, e la regola si chiama **istanziazione universale**. Con ragionamenti simili si giustificano le altre tre regole della tabella.

![Le regole di inferenza per gli enunciati quantificati.](figure/fond/logica_regole_quantificatori.png|12.5)

- **Istanziazione universale**: da ∀x P(x) si ricava P(d), per ogni d ∈ D.
- **Generalizzazione universale**: se P(d) è vera per ogni d ∈ D, si ricava ∀x P(x). Si usa con un elemento arbitrario, come nel capitolo 21.
- **Istanziazione esistenziale**: da ∃x P(x) si ricava P(d) per qualche d ∈ D (un elemento di cui si sa solo che esiste).
- **Generalizzazione esistenziale**: se P(d) è vera per qualche d ∈ D, si ricava ∃x P(x).

## Esempi
**Istanziazione universale.** Si sa che «per ogni intero positivo n, n² ≥ n» è vero. Poiché 54 è un intero positivo, cioè un elemento del dominio, per istanziazione universale si conclude che 54² ≥ 54.

**Generalizzazione esistenziale.** Sia P(x) = «x possiede un computer portatile», con dominio gli studenti di MATH 201 (matematica discreta). Se Taylor, che frequenta il corso, possiede un portatile, in simboli P(Taylor) è vera, e per generalizzazione esistenziale si conclude che ∃x P(x) è vero.

**Modus tollens universale.** Si consideri l'argomento: «per ogni numero reale x, se x è un intero allora x è razionale. Il numero √2 non è razionale. Quindi √2 non è un intero». Con P(x) = «x è un intero» e Q(x) = «x è razionale», l'argomento è
∀x ∈ ℝ (P(x) → Q(x)), ¬Q(√2) / ∴ ¬P(√2).
Poiché √2 ∈ ℝ, per istanziazione universale si ottiene P(√2) → Q(√2); insieme a ¬Q(√2), per il modus tollens (capitolo 19) si conclude ¬P(√2). L'argomento è valido e si chiama **modus tollens universale**.

**Sillogismo disgiuntivo con un quantificatore.** Si hanno le ipotesi: «tutti amano Microsoft o Apple» e «Lynn non ama Microsoft». Si vuole mostrare che «Lynn ama Apple». Con P(x) = «x ama Microsoft» e Q(x) = «x ama Apple», la prima ipotesi è ∀x (P(x) ∨ Q(x)); per istanziazione universale si ha P(Lynn) ∨ Q(Lynn). La seconda ipotesi è ¬P(Lynn): il sillogismo disgiuntivo dà Q(Lynn), cioè «Lynn ama Apple». La conclusione segue dalle ipotesi.

## Riepilogo: come si prova o si smentisce un quantificatore
Le regole pratiche per dimostrare e smentire enunciati quantificati sono quattro, e conviene averle chiare perché sono il punto più usato negli esercizi.
- Per provare che ∀x P(x) è **vero**, bisogna mostrare che P(x) è vera per **ogni** x del dominio. Mostrare che P(x) è vera per un valore particolare **non** basta.
- Per provare che ∃x P(x) è **vero**, basta trovare **un** valore di x del dominio per cui P(x) è vera.
- Per provare che ∀x P(x) è **falso**, basta trovare **un** valore di x (un controesempio) per cui P(x) è falsa.
- Per provare che ∃x P(x) è **falso**, bisogna mostrare che P(x) è falsa per **ogni** x del dominio. Mostrare che P(x) è falsa per un valore particolare **non** basta.
