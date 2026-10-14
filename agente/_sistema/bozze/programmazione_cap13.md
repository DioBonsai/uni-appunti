# Capitolo 13: Scambio di Variabili e Variabile Temporanea
## Il problema dello scambio
Lo **scambio** (in inglese ~swap~) dei valori di due variabili è un'operazione fondamentale in programmazione, usata in molti algoritmi, per esempio nel bubble sort. Sembra banale, ma il metodo più ovvio e intuitivo non funziona, e capire perché è un buon modo per fissare che cosa fa davvero un assegnamento.

Per introdurre il problema si usa un'analogia. Abbiamo due tazze (le chiameremo X e Y), una con tè verde e una con tè nero, e vogliamo scambiarne il contenuto. Non possiamo versare direttamente una tazza nell'altra, perché i due tè si mescolerebbero. Una soluzione c'è: usare altre due tazze vuote, travasarci i due tè e poi rimetterli ciascuno nella tazza opposta. Funziona, ma non è efficiente, perché usa il doppio dello spazio. Si può fare meglio con **una sola tazza ausiliaria** A:
1. si versa il tè verde nella tazza vuota;
2. si versa il tè nero nella tazza che era del tè verde;
3. si versa infine il tè verde, che aspettava nella tazza ausiliaria, nella tazza che era del tè nero.

Questa soluzione funziona ed è efficiente, ma la sequenza dei travasi deve avvenire nell'ordine giusto: con un ordine diverso uno dei due tè andrebbe perso. Con le variabili vale lo stesso, e la tazza ausiliaria diventerà una variabile d'appoggio.

![Lo scambio delle tazze con una sola tazza ausiliaria (in rosso le tazze il cui contenuto è cambiato).](figure/prog/ch13_tazze.png|12.5)

## Il metodo ovvio non funziona
Definiamo due variabili intere x e y e proviamo a scambiarle nel modo più intuitivo: assegniamo a x il contenuto di y e poi a y il contenuto di x.

```c
int main(void) {
    int x = 5;
    int y = 2;
    x = y;   // assegniamo il contenuto di y ad x
    y = x;   // assegniamo il contenuto di x ad y
    printf("Le var x, y valgono %d, %d\n", x, y);
}
```

Il problema è che un assegnamento **copia** il valore dell'espressione di destra nella cella della variabile di sinistra, e il valore che la cella conteneva prima va perso (si ricordi il capitolo 8: la cella dell'Lvalue viene sovrascritta). Seguiamo l'esecuzione sullo stack, dove x vale 5 e y vale 2. Dopo `x = y;` il valore di y è stato copiato in x, che ora vale 2: **il vecchio valore di x è perso**. Con `y = x;` si copia in y il contenuto di x, che però ormai è 2, quindi y viene sovrascritta con il suo stesso valore. Alla fine le due variabili valgono entrambe 2 e il programma stampa `Le var x, y valgono 2, 2`.

![Esecuzione di x = y; y = x;: dopo il primo assegnamento il valore 5 non esiste più (in rosso le celle il cui valore è cambiato).](figure/prog/ch13_swap_ovvio.png|10)

## Lo scambio con variabile temporanea
Per scambiare correttamente i valori di due variabili serve una terza variabile di supporto, dello stesso tipo, che conservi temporaneamente uno dei due valori. Questo metodo si chiama **scambio con variabile temporanea** (o variabile d'appoggio) ed è l'esatto equivalente della tazza ausiliaria. I passi sono tre:
1. si salva il valore di x nella variabile d'appoggio;
2. si copia il valore di y in x;
3. si copia in y il valore conservato nella variabile d'appoggio.

I nomi tipici delle variabili d'appoggio sono `temp`, `aux`, `prevX`, `savedX`, `backup`.

```c
int main(void) {
    int x = 5;
    int y = 2;
    int temp;
    temp = x;   // 1: salvo il vecchio valore di x
    x = y;      // 2: ora posso sovrascrivere x
    y = temp;   // 3: recupero il valore salvato
    printf("Le var x, y valgono %d, %d\n", x, y);
}
```

Sullo stack, la dichiarazione `int temp;` alloca altri 4 byte con valore indeterminato (il simbolo "?" con cui si indica un contenuto indeterminato, come visto nel capitolo 7). Poi, passo per passo:
- `temp = x;` copia 5 in temp: ora il valore originale di x esiste in due celle;
- `x = y;` sovrascrive x con 2, ma questa volta nessuna informazione è persa, perché il 5 è al sicuro in temp;
- `y = temp;` copia in y il 5 salvato.

Il programma stampa `Le var x, y valgono 2, 5`: i valori sono stati scambiati.

![Scambio con variabile temporanea: il 5 resta al sicuro in temp finché y non lo riceve (in rosso le celle il cui valore è cambiato).](figure/prog/ch13_swap_temp.png|12.5)

## Perché l'ordine conta
Come nell'esempio delle tazze, la sequenza dei tre assegnamenti non si può cambiare a piacere: ogni assegnamento deve avvenire quando il valore che sta per essere sovrascritto è già stato salvato altrove. Per esempio, scrivendo `x = y; temp = x; y = temp;` si copia in temp un valore di x che è già stato sovrascritto, e alla fine x, y e temp valgono tutti 2: il 5 è stato perso proprio come nel metodo ovvio.

Il prezzo della soluzione corretta è piccolo: una sola variabile in più, cioè 4 byte per degli int, a fronte di un'operazione che il metodo ovvio non sa fare. Lo scambio con variabile temporanea sarà utile ogni volta che un algoritmo dovrà riordinare dei valori; nel prossimo capitolo passiamo invece ai numeri reali, con i tipi float e double.
