# 26. Decidere i Quantificatori Annidati con un Programma
## Il problema, su un dominio finito
Come si decide il valore di verità di una formula con due quantificatori? Come sottolineato a lezione, si considera il caso di un **dominio finito** D = {d₁, …, dₙ}: se il dominio fosse infinito un programma potrebbe non finire mai, e bisognerebbe ricorrere alla deduzione automatica, che qui non si tratta. Anche i capitoli 21-22 si fermavano ai domini finiti.

Un problema di questo tipo non è astratto. Si immagini una **matrice di dati**, per esempio 10 filiali di un'azienda e, per ogni filiale, 1000 oggetti prodotti e sottoposti a un test: sono 10 × 1000 = 10.000 test. Sia P(x, y) = «il test della filiale x sull'oggetto y è andato a buon fine». La domanda «hanno passato il test tutti gli oggetti di tutte le filiali?» è ∀x ∀y P(x, y).

## Due universali: ∀x ∀y P(x, y)
Per un solo quantificatore universale (cap. 21) si usava un ciclo: se P(dᵢ) è falsa si restituisce falso; altrimenti non si fa niente, perché il test superato da un oggetto non dice nulla sugli altri; solo **all'uscita dal ciclo**, se non si è mai trovato un controesempio, si restituisce vero. Qui, invece di una riga di dati, c'è un quadrato di dati: il primo `for` percorre le righe, e per ogni riga serve un secondo `for` per percorrere tutte le colonne, con dentro il test. Come si parla di quantificatori annidati, si parla di **for annidati**: un ciclo si trova dentro la parte di programma controllata da un altro ciclo, come il quantificatore ∀y sta dentro la zona d'azione di ∀x.

Per semplicità il codice assume che i due indici percorrano lo stesso dominio D = {d₁, …, dₙ} (n righe e n colonne), come nel libro; con una matrice m × n basta cambiare l'estremo del primo ciclo.

```
for i = 1 to n
  for j = 1 to n
    if (P(d_i, d_j) = false) then return false;
// se il doppio for non ha dato false:
return true;
```

Come sottolineato a lezione, per il `return` valgono le stesse regole di prima: **`return false`** appena si trova una coppia con P falsa (basta un controesempio per rendere falso l'universale); **`return true`** solo **fuori dai due cicli**, dopo averli percorsi per intero senza trovare falsi. Mettere un `return true` dentro il ciclo sarebbe sbagliato: finché si trovano valori veri potrebbe esserci una coppia falsa che non si è ancora vista. Con una matrice 1000 × 1000 ci sono un milione di controlli: sono programmi che si possono fare, ma costosi.

**In parole povere:** per verificare che «tutti» soddisfino una proprietà si guarda ogni singola casella e ci si ferma subito se si trova un caso negativo; si può dire «sì» solo dopo aver guardato proprio tutto.
## Il caso difficile: ∀x ∃y P(x, y)
Come sottolineato a lezione, il caso difficile è «per ogni… esiste…»: su ogni riga bisogna trovare una colonna in cui la proprietà vale, e finita una riga bisogna passare alla successiva e cercare di nuovo. Se si fallisce in **una sola** riga, la formula è falsa; se si ha successo in **tutte** le righe, è vera.

**Un tentativo sbagliato.** L'idea naturale è questa: per ogni riga i, cercare una colonna j in cui P(dᵢ, dⱼ) è vera, e restituire vero appena la si trova:

```
for i = 1 to n
  for j = 1 to n
    if (P(d_i, d_j) = true) then return true;   // NO!!
```

Il codice non fa quello che si vuole. Il `return` non esce dal ciclo interno per passare alla riga successiva: **esce da tutto il programma**. Il codice restituisce quindi vero non appena trova la prima riga con una colonna in cui P è vera, senza guardare le altre righe: risolve il problema ∃x ∃y P(x, y), cioè un problema completamente diverso.

**La soluzione modulare.** Si usa la scomposizione: **∀x ∃y P(x, y) ≡ ∀x Q(x)**, dove **Q(x) = ∃y P(x, y)**. Nell'enunciato Q(x) la variabile y è **legata** (la gestisce il quantificatore ∃, che le fa assumere tutti i valori del dominio), mentre la x è l'unica variabile libera: si può pensare che x abbia già un valore. Si decide prima Q(x) con un ciclo, poi si decide ∀x Q(x) con un altro ciclo che usa il primo.

**In parole povere:** in Q(x) la x è «già scelta» (variabile libera) e la y è gestita dall'∃ (variabile legata): perciò Q si può decidere da sola, per ogni x fissato.

Per «mettere un pezzo di codice dentro un altro» si usa una **funzione**: così il `return` esce solo dalla funzione, e non dal programma intero. Prima il decisore di Q (qui x e y indicano la posizione nel dominio, come i e j sopra):

```
ex(x) {
  for y = 1 to n
    if (P(x, y) = true)
      return true;
  return false;
}
```

La funzione `ex(x)` controlla la riga x: prova tutti i valori di y; se anche uno solo rende P vera, restituisce vero; se sono tutti falsi, restituisce falso. Poi la soluzione completa, per l'universale:

```
for x = 1 to n
  if (ex(x) = false)
    return false;
return true;
```

Se per qualche riga `ex(x)` è falsa si esce con falso; solo se **tutte** le righe hanno almeno una colonna con P vera si restituisce vero.

**In parole povere:** per «per ogni riga esiste una casella buona» si controlla riga per riga, e per ciascuna si cerca una casella buona; se una riga non ne ha, la risposta è no; la funzione serve a far finire la ricerca nella riga corrente senza interrompere il controllo di tutte le altre righe.
Come sottolineato a lezione, nel libro lo stesso risultato si ottiene con una funzione locale al ciclo e con la condizione scritta come ¬exists(dᵢ) invece di exists = falso: è la stessa cosa. Si tratta di un pezzo di logica «meccanizzata» che in Programmazione non capita spesso di scrivere. A lezione si è fatto l'esempio di una matrice con la storia di tanti tentativi di riavviare una macchina (un'ipotesi di lettura: controllare che in ogni riga ci sia stato almeno un tentativo andato a buon fine); il caso di «tutti i tentativi riusciti», cioè ∀∀, è invece quello più semplice.

## Più quantificatori
In linea di principio la stessa tecnica si estende a qualunque formula con più quantificatori su un dominio finito: si risolve un quantificatore alla volta, dall'interno verso l'esterno. Il costo però cresce molto: con k quantificatori annidati su un dominio di n elementi i controlli sono nᵏ, e a lezione si è detto che l'algoritmo diventa **esponenziale** nella dimensione della formula. Si sa quindi che un modo per decidere esiste, ma non è quello che si usa in pratica.

Il capitolo successivo usa i quantificatori annidati su domini concreti e ne studia la negazione con le leggi di De Morgan.
