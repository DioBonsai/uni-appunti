# 27. Esempi con Quantificatori Annidati e Leggi di De Morgan
## Minimo e massimo si esprimono con ∃∀
**Esiste un minimo: ∃x ∀y (x ≤ y).** La formula dice che c'è un x minore o uguale a ogni y: cioè il dominio ha un valore minimo. Dipende dal dominio:
- sugli **interi positivi** è **vera**: il minimo è 1, e ogni y è almeno 1;
- sui **reali** è **falsa**: comunque si scelga x, basta prendere y = x − 1, che è ancora un reale, e x ≤ x − 1 è falso.

**Esiste un massimo: ∃x ∀y (x ≥ y).** Sugli **interi positivi** è **falsa**: per ogni x si può scegliere y = x + 1, e x ≥ x + 1 è falso; chiunque dica «x è il massimo» viene smentito da x + 1. Sui reali, per lo stesso motivo, è falsa. Su un **insieme finito** come {1, 2, …, 10} è invece **vera**: basta prendere x = 10, e tutti gli altri valori sono minori o uguali. Lo stesso per un intervallo [a, b] dei reali, dove x = b è il massimo.

Queste formule non descrivono numeri ma **proprietà di un insieme di numeri**: insiemi diversi hanno proprietà diverse, quindi lo stesso enunciato può essere vero su un dominio e falso su un altro.

Confrontando con il cap. 25: ∀x ∃y (x > y) dice «non c'è un minimo», mentre ∃x ∀y (x ≤ y) dice «c'è un minimo»; sono l'una la negazione dell'altra, come si vede sotto.

## Numeri composti e numeri primi
Si consideri ∃x ∃y ((x > 1) ∧ (y > 1) ∧ (xy = 6)), con dominio ℤ⁺ × ℤ⁺. È **vera**: x = 2 e y = 3 sono entrambi maggiori di 1 e il loro prodotto è 6. L'enunciato dice che 6 ha una **scomposizione propria**, cioè che si scrive come prodotto di due interi entrambi maggiori di 1 (e quindi entrambi minori di 6: se uno valesse 6, l'altro sarebbe 1); in altre parole, che 6 è un **numero composto**.

Con 7 al posto di 6, ∃x ∃y ((x > 1) ∧ (y > 1) ∧ (xy = 7)) è **falsa**: nessuna coppia di interi maggiori di 1 ha prodotto 7 (si controlla: 2, 3, 4, 5 e 6 non vanno bene). Infatti 7 è un **numero primo**: si può scrivere come prodotto solo con i divisori banali, 1 e 7.

**In parole povere:** un numero è composto se si spezza in due fattori «veri», cioè diversi da 1; è primo se non si spezza così.
Come sottolineato a lezione, queste proprietà dei numeri primi sono importanti anche in informatica: la crittografia a chiave pubblica, oggi la più usata, si basa sulla difficoltà di trovare la scomposizione in fattori primi di un numero molto grande, anche se esistono algoritmi molto rapidi per decidere se un numero ha o no una scomposizione propria.

## Le leggi di De Morgan con più quantificatori
Le leggi di De Morgan del cap. 22 valgono anche per i quantificatori annidati, e si applicano a **un quantificatore per volta**, dall'esterno verso l'interno: ¬∀ diventa ∃¬, ¬∃ diventa ∀¬, un ¬ davanti a un'implicazione si toglie riscrivendola (cap. 18), davanti a una congiunzione o a una disgiunzione si applicano le leggi ordinarie, e due ¬ consecutivi si cancellano. Si continua finché tutte le negazioni si trovano **soltanto davanti ai predicati**. Come sottolineato a lezione, questo è importante per la deduzione automatica: significa meno connettivi di cui occuparsi. Se per un predicato si conosce anche l'opposto (per esempio ¬(x > y) equivale a x ≤ y), le negazioni possono sparire del tutto.

**Negare ∀x ∃y P(x, y).**
¬∀x ∃y P(x, y) ≡ ∃x ¬(∃y P(x, y)) ≡ **∃x ∀y ¬P(x, y)**.
Il ¬ passa un quantificatore alla volta e ogni volta ∀ e ∃ si scambiano.

**In parole povere:** per negare una formula con quantificatori si scambiano tutti i ∀ con ∃ (e viceversa) e si nega alla fine il predicato.

**Esempio: negare «non c'è un minimo».** La formula ∀x ∃y (x > y) significa che non c'è un minimo. La sua negazione è
¬∀x ∃y (x > y) ≡ ∃x ¬(∃y (x > y)) ≡ ∃x ∀y ¬(x > y) ≡ ∃x ∀y (x ≤ y).
Qui si è usato che negare «x maggiore di y» vuol dire che è vero il minore o uguale: ci sono tre possibilità (x > y, x = y, x < y), e togliendo la prima restano le altre due, che si dicono insieme con x ≤ y, equivalente a (x < y) ∨ (x = y). Il risultato dice «esiste un minimo», proprio il contrario di «non c'è un minimo». Come sottolineato a lezione, è logico: se si nega un'affermazione si ottiene l'opposto, e negando due volte si torna alla forma di partenza. Il simbolo giusto fra le due formule è l'equivalenza (≡) e non l'uguaglianza.

## Un esercizio: ∃x ∀y (xy < 1)
È vera o falsa? Dipende dal dominio. Si può ragionare così.
- Con dominio **ℝ × ℝ** è **vera**: si sceglie x = 0, e allora xy = 0 < 1 per ogni y. Con questo solo valore di x è vera.
- Se si toglie lo zero, con dominio **ℝ∖{0} × ℝ∖{0}** (i reali non nulli) o con dominio **i reali positivi**, è **falsa**. Per dimostrarlo si calcola la negazione con De Morgan: ¬∃x ∀y (xy < 1) ≡ ∀x ∃y (xy ≥ 1). Questa formula è **vera** scegliendo y = 1/x, perché allora xy = 1 ≥ 1. L'unico caso in cui il tentativo non riuscirebbe è x = 0, perché non si divide per zero; nei reali non nulli o nei positivi lo zero non c'è, e 1/x è ancora nel dominio (un reale positivo ha un reciproco positivo). Dunque la negazione è vera e la formula di partenza è falsa. In sostanza si dimostra che ∀x ∃y (xy = 1).
