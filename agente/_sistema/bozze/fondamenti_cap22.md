# 22. Il Quantificatore Esistenziale e le Leggi di De Morgan per i Quantificatori
## La definizione
Il secondo quantificatore è l'**esistenziale**. Un enunciato della forma «esiste x tale che P(x)» si dice **enunciato quantificato esistenzialmente**; il simbolo ∃ significa «esiste» e si chiama **quantificatore esistenziale**: l'enunciato si scrive ∃x P(x).

**Definizione.** Sia P una funzione proposizionale con dominio D. L'enunciato ∃x P(x) è **vero** se P(x) è vera per almeno un x ∈ D. È **falso** se P(x) è falsa per ogni x ∈ D.

È la definizione esattamente **duale** di quella dell'universale: basta scambiare il vero con il falso. Il quantificatore universale è vero quando tutti i valori sono veri e falso se anche uno solo è falso; l'esistenziale è falso quando tutti i valori sono falsi e vero se anche uno solo è vero. In inglese si può dire «there exists», «for some», «for at least one»; il simbolo ∃ si legge in tutti questi modi. Non si chiede che il valore sia unico: l'esistenziale è vero se P(x) vale per un solo valore, per due, per un numero qualunque di valori, anche infiniti, e anche per tutti.

## Esempi
**Un esistenziale vero.** ∃x (x/(x² + 1) = 2/5), con dominio ℝ. È vero: basta un numero reale per cui valga l'uguaglianza, e x = 2 funziona, perché 2/(2² + 1) = 2/5. Non vale per ogni x (con x = 1 si ha 1/2, e 1/2 ≠ 2/5). Un secondo valore che la soddisfa è x = 1/2 (il motivo è che l'equazione ottenuta è di secondo grado con il termine di secondo grado e il termine noto uguali, e questo fa sì che a ogni radice corrisponda quella inversa); non era richiesto, perché un solo valore basta.

**Un altro esistenziale vero.** «Per qualche n, se n è primo allora n + 1, n + 2, n + 3 e n + 4 non sono primi», con dominio ℤ⁺. Basta trovare un n che renda vera l'implicazione, per esempio n = 23: l'ipotesi «23 è primo» e la conclusione «24, 25, 26 e 27 non sono primi» sono entrambe vere. Alcuni valori rendono l'implicazione vera (n = 23, n = 4, n = 47) e altri la rendono falsa (n = 2, n = 101): conta il fatto che se ne sia trovato **uno**.

**Un esistenziale falso.** ∃x (1/(x² + 1) > 1), con dominio ℝ. Per mostrare che è falso bisogna dimostrare che la disuguaglianza è falsa per **ogni** x reale, cioè che per ogni x vale 1/(x² + 1) ≤ 1. Sia x un reale qualunque. Poiché x² ≥ 0, si può aggiungere 1 a entrambi i lati e ottenere 1 ≤ x² + 1; dividendo entrambi i lati per x² + 1 (positivo) si ottiene 1/(x² + 1) ≤ 1. Quindi la disuguaglianza di partenza è falsa per ogni x e l'esistenziale è falso. (Mostrare che P(x) è falsa per un valore particolare **non** basta.)

## Un algoritmo per decidere ∃x P(x) su un dominio finito
Si può usare la stessa idea del capitolo 21: la soluzione si ottiene **scambiando dappertutto vero e falso**. Con il dominio D = {d₁, …, d_{n}}:

```
for i = 1 to n
    if (P(d_i))
        return true
return false
```

Il ciclo esamina i d_{i} uno a uno. Se trova un d_{i} per cui P(d_{i}) è vera, restituisce **true** e termina: ne basta uno. Se P(d_{i}) è falsa per ogni d_{i}, il ciclo arriva alla fine e il programma restituisce **false**. Quindi se ∃x P(x) è vero il ciclo si ferma appena trova un elemento che rende P vera; se è falso deve controllare tutti gli elementi.

Anche qui valgono gli errori del capitolo precedente, duali. Scrivere `if (¬P(d_i)) return false` è sbagliato: se P(d₁) è falsa non si può concludere che l'esistenziale sia falso, perché potrebbe essere vero per il settimo elemento. Si deve restituire **true** al primo vero, e il `return false` va **fuori dal ciclo**, allineato con il `for`. Il programma funziona come test: per esempio si può provare a scriverlo per cercare in un vettore di numeri se c'è almeno un numero pari, oppure se sono tutti pari.

## Duali, congiunzione e disgiunzione
Poiché la definizione dell'uno diventa quella dell'altro scambiando dappertutto il vero con il falso, ∀ e ∃ si dicono **quantificatori duali**; è lo stesso legame che c'è tra congiunzione e disgiunzione. Per questo, come per quelli, valgono le leggi di De Morgan. In effetti un enunciato universale generalizza la congiunzione P₁ ∧ P₂ ∧ … ∧ P_{n}: al posto delle singole proposizioni P₁, …, P_{n} si ha una famiglia P(x), con x nel dominio, e ∀x P(x) è vero se e solo se P(x) è vera per ogni x. Se il dominio è {−1, 0, 1}, ∀x P(x) equivale a P(−1) ∧ P(0) ∧ P(1). Allo stesso modo ∃x P(x) generalizza la disgiunzione P₁ ∨ P₂ ∨ … ∨ P_{n}: con dominio {1, 2, 3, 4}, ∃x P(x) equivale a P(1) ∨ P(2) ∨ P(3) ∨ P(4).

## Le leggi di De Morgan per i quantificatori
**Teorema (leggi di De Morgan generalizzate).** Se P è una funzione proposizionale, ciascuna delle due coppie di enunciati seguenti ha gli stessi valori di verità (sono entrambi veri o entrambi falsi):
- ¬(∀x P(x)) e ∃x ¬P(x): non è vero che per ogni x vale P(x) se e solo se c'è un x per cui non vale P(x);
- ¬(∃x P(x)) e ∀x ¬P(x): non è vero che esiste un x per cui vale P(x) se e solo se per ogni x non vale P(x).

Sono esattamente le leggi di De Morgan dei capitoli 15 e 18, in cui la negazione di una congiunzione è la disgiunzione delle negazioni e viceversa.

**Dimostrazione della prima legge.** Se ¬(∀x P(x)) è vera, allora ∀x P(x) è falso; per la definizione di universale, questo succede esattamente quando P(x) è falsa per almeno un x del dominio. Ma se P(x) è falsa per almeno un x, allora ¬P(x) è vera per almeno un x, e per la definizione di esistenziale ∃x ¬P(x) è vero. Il ragionamento inverso mostra che se ¬(∀x P(x)) è falsa lo è anche ∃x ¬P(x). La seconda legge si dimostra in modo simile (è un esercizio del libro).

Un altro modo di riconoscerle: portare il «non» dentro il quantificatore scambia il vero con il falso sia nel valore del predicato sia nel valore della proposizione finale, e sappiamo che questo doppio scambio trasforma il «per ogni» in «esiste» e viceversa.

La seconda legge spiega anche un modo di smentire un esistenziale: per mostrare che ∃x P(x) è falso si dimostra che ∀x ¬P(x) è vero, come si è fatto sopra per 1/(x² + 1) > 1.

## La negazione nel linguaggio naturale
Per negare un enunciato quantificato si applicano le leggi precedenti.
- «Ogni tifoso del rock ama gli U2» si scrive ∀x P(x), con P(x) = «x ama gli U2» e dominio i tifosi del rock. La sua negazione ¬(∀x P(x)) equivale a ∃x ¬P(x): «esiste un tifoso del rock che non ama gli U2».
- «Alcuni uccelli non volano» si scrive ∃x ¬P(x), con P(x) = «x vola» (o anche ∃x Q(x) con Q(x) = «x non vola»). La negazione ¬(∃x ¬P(x)) equivale a ∀x ¬¬P(x), cioè ∀x P(x): «ogni uccello vola».

Gli enunciati a parole possono avere più interpretazioni. «Tutto ciò che luccica non è oro» (dal *Mercante di Venezia*) si può leggere come «ogni oggetto che luccica non è oro», cioè ∀x (P(x) → ¬Q(x)), con P(x) = «x luccica» e Q(x) = «x è oro»; ma ciò che Shakespeare intendeva è «qualche oggetto che luccica non è oro», cioè ∃x (P(x) ∧ ¬Q(x)), che per De Morgan e per le equivalenze del capitolo 18 equivale a ¬(∀x (P(x) → Q(x))). L'ambiguità dipende da dove si applica la negazione: a Q(x) oppure all'intero enunciato.

Nel linguaggio naturale, negli enunciati positivi «ogni», «tutti», «ciascuno» e «qualunque» hanno lo stesso significato; negli enunciati negativi la situazione cambia. «Non tutti gli x soddisfano P(x)», «non ogni x» e «non ciascun x» significano ∃x ¬P(x), mentre «nessun x soddisfa P(x)» e «non esiste alcun x che soddisfi P(x)» significano ∀x ¬P(x).
