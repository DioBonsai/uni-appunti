# 03A_scambio variabili

<!-- pagina 1 -->
Programmazione I
Teoria
Elvio Amparore
A.A. 2026/27
Canale B
DIPARTIMENTO DI 
INFORMATICA
 
CORSO DI LAUREA 
TRIENNALE
Scambiare variabili
Uso delle variabili temporanee

<!-- pagina 2 -->
Contenuto, spazio, limiti
• Abbiamo due tazze: una contiene tè verde, l’altra tè nero.
• Vogliamo scambiarne il contenuto, ma non possiamo 
versare direttamente dall’una all’altra: i liquidi si 
mescolerebbero e il risultato sarebbe confuso.
2
• versiamo il tè verde nella prima tazza vuota
• versiamo il tè nero nella seconda tazza vuota
Questa soluzione funziona ma non è efﬁciente (usa 
il doppio dello spazio). Possiamo fare di meglio.
• inﬁne dalle tue tazze intermedie procediamo a 
completare lo scambio
X
Y
X
Y
A
B
Possiamo farlo con altre due tazze:

<!-- pagina 3 -->
Contenuto, spazio, limiti
• Abbiamo due tazze: una contiene tè verde, l’altra tè nero.
• Vogliamo scambiarne il contenuto, ma non possiamo 
versare direttamente dall’una all’altra: i liquidi si 
mescolerebbero e il risultato sarebbe confuso.
3
X
Y
A
Possiamo farlo con una sola tazza ausiliaria:
1
[1] versiamo il tè verde nella tazza vuota
[2] versiamo il tè nero nella tazza che era del tè verde
[3] versiamo inﬁne il tè verde dalla tazza vuota 
      nella tazza che era del tè nero
2
3

<!-- pagina 4 -->
Contenuto, spazio, limiti
• Abbiamo due tazze: una contiene tè verde, l’altra tè nero.
• Vogliamo scambiarne il contenuto, ma non possiamo 
versare direttamente dall’una all’altra: i liquidi si 
mescolerebbero e il risultato sarebbe confuso.
4
Questa soluzione funziona ed è efﬁciente, ma la 
sequenza dei travasi deve avvenire nell’ordine giusto.
X
Y
X
Y
Possiamo farlo con una sola tazza ausiliaria:
[1] versiamo il tè verde nella tazza vuota
[2] versiamo il tè nero nella tazza che era del tè verde
[3] versiamo inﬁne il tè verde dalla tazza vuota 
      nella tazza che era del tè nero

<!-- pagina 5 -->
Scambio di variabili
●Lo scambio dei valori di due variabili (swap) è un’operazione 
fondamentale in programmazione, usata in molti algoritmi 
come ad esempio il bubble sort. Vediamo perché il metodo 
più ovvio ed intuitivo non funziona e come correggerlo.
●Proviamo a deﬁnire due variabili x ed y, e a scambiare il 
contenuto di queste due variabili x e y in modo naïve, ad 
esempio: 
x = y; // Assegniamo il contenuto di y ad x
y = x; // Assegniamo il contenuto di x ad y
●Problema: dopo x = y; il valore originale di x è perso.
5

<!-- pagina 6 -->
Scambio di variabili
int main(void) {
    int x = 5;
▶   int y = 2;
    x = y;
    y = x;
    printf("Le var x, y valgono %d, %d\n", 
           x, y) ;
}
Area codice
FP
5
x
2
y
SP
Indirizzi di memoria crescenti
$ ./ swap_1 
32 bit, 4 bytes

<!-- pagina 7 -->
int main(void) {
    int x = 5;
    int y = 2;
▶   x = y;
    y = x;
    printf("Le var x, y valgono %d, %d\n", 
           x, y) ;
}
Scambio di variabili
Area codice
FP
5 2
x
2
y
SP
Indirizzi di memoria crescenti
$ ./swap_1 
32 bit, 4 bytes
Valore in y 
copiato in x

<!-- pagina 8 -->
Scambio di variabili
Area codice
FP
2
x
2
y
SP
Indirizzi di memoria crescenti
$ ./ swap_1 
32 bit, 4 bytes
Il vecchio 
valore di x è 
perso
int main(void) {
    int x = 5;
    int y = 2;
▶   x = y;
    y = x;
    printf("Le var x, y valgono %d, %d\n", 
           x, y) ;
}

<!-- pagina 9 -->
Scambio di variabili
Area codice
FP
2
x
2 2
y
SP
Indirizzi di memoria crescenti
$ ./swap_1 
32 bit, 4 bytes
Sovrascrivo y 
con y stessa
int main(void) {
    int x = 5;
    int y = 2;
    x = y;
▶   y = x;
    printf("Le var x, y valgono %d, %d\n", 
           x, y) ;
}

<!-- pagina 10 -->
Scambio di variabili
Area codice
FP
2
x
2
y
SP
Indirizzi di memoria crescenti
$ ./swap_1
Le var x, y  valgono 2, 2
32 bit, 4 bytes
int main(void) {
    int x = 5;
    int y = 2;
    x = y;
    y = x;
▶   printf("Le var x, y valgono %d, %d\n", 
           x, y) ;
}

<!-- pagina 11 -->
Scambio corretto con variabile d’appoggio
• Per scambiare correttamente i valori di due variabili x e y, è 
necessario introdurre una terza variabile di supporto, dello 
stesso tipo, che conservi temporaneamente uno dei valori.
• Questo metodo prende il nome di scambio con variabile 
temporanea (o variabile d’appoggio).
a. Salvo il valore di x nella variabile di appoggio.
b. Copio il valore di y in x.
c. Copio il valore della variabile di appoggio in y.
• Nomi tipici di queste variabili:
temp, aux, prevX, savedX, backup
11
y
temp
x
1
2
3

<!-- pagina 12 -->
Scambio di variabili
int main(void) {
    int x = 5;
    int y = 2;
▶   int temp;
    temp = x;
    x = y;
    y = temp;
    printf("Le var x, y valgono %d, %d\n",
           x, y) ;
}
Area codice
FP
5
x
2
y
SP
Indirizzi di memoria crescenti
$ ./swap_2
32 bit, 4 bytes
?
temp

<!-- pagina 13 -->
Scambio di variabili
Area codice
FP
5
x
2
y
SP
Indirizzi di memoria crescenti
$ ./swap_2
32 bit, 4 bytes
? 5
temp
y
temp
x
1
int main(void) {
    int x = 5;
    int y = 2;
    int temp;
▶   temp = x;
    x = y;
    y = temp;
    printf("Le var x, y valgono %d, %d\n",
           x, y) ;
}

<!-- pagina 14 -->
Scambio di variabili
Area codice
FP
5 2
x
2
y
SP
Indirizzi di memoria crescenti
$ ./swap_2
32 bit, 4 bytes
5
temp
y
temp
x
1
2
int main(void) {
    int x = 5;
    int y = 2;
    int temp;
    temp = x;
▶   x = y;
    y = temp;
    printf("Le var x, y valgono %d, %d\n",
           x, y) ;
}

<!-- pagina 15 -->
Scambio di variabili
Area codice
FP
2
x
2 5
y
SP
Indirizzi di memoria crescenti
$ ./swap_2
32 bit, 4 bytes
5
temp
y
temp
x
1
2
3
int main(void) {
    int x = 5;
    int y = 2;
    int temp;
    temp = x;
    x = y;
▶   y = temp;
    printf("Le var x, y valgono %d, %d\n",
           x, y) ;
}

<!-- pagina 16 -->
Scambio di variabili
Area codice
FP
2
x
5
y
SP
Indirizzi di memoria crescenti
$ ./swap_2
Le var x, y  e valgono 2, 5
32 bit, 4 bytes
5
temp
y
temp
x
int main(void) {
    int x = 5;
    int y = 2;
    int temp;
    temp = x;
    x = y;
    y = temp;
▶   printf("Le var x, y valgono %d, %d\n",
           x, y) ;
}
