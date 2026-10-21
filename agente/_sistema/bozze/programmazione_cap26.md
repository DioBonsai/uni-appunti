# Capitolo 26: Le Stringhe: Caratteri, Terminatore e Lettura da Input
## Il testo come array di caratteri
In C il testo è un array di elementi di tipo `char`. Lettere, cifre e simboli sono rappresentati come unità elementari dette **caratteri**; il tipo `char` rappresenta un singolo carattere e un array di caratteri forma una **stringa** di testo. I caratteri corrispondono a codici numerici convenzionali descritti da alcuni standard; il fondamentale è l'**ASCII** (~American Standard Code for Information Interchange~). Abbiamo già usato il testo sotto forma di **letterali stringa** (~string literals~), non modificabili, scrivendo i caratteri tra doppi apici ("…").

(In parole povere: una stringa è una fila di caselle, ognuna con una lettera; dietro ogni lettera c'è un numero, il suo codice.)

L'ASCII definisce 128 caratteri, codificati a 7 bit. Alcuni caratteri speciali si scrivono con una sequenza di escape, per esempio: il **terminatore** NUL con `'\0'`, il ~line feed~ (a capo) con `'\n'`, il ~tab~ orizzontale con `'\t'` e il ~carriage return~ con `'\r'`.

## Da ASCII a Unicode (cenni)
La codifica del testo ha una storia che spiega le scelte del C.

(In parole povere: all'inizio ogni carattere stava in 7 bit e bastava per l'inglese; poi, per scrivere tutte le lingue del mondo, si è passati a Unicode, che dà un codice a ogni carattere, e a codifiche come UTF-8 che ne decidono il numero di byte.)

- **1963, ASCII**: 7 bit, permette di codificare a malapena gli alfabeti latini; non basta per greco, cirillico, arabo, per gli alfabeti ideografici (cinese, giapponese, coreano) né per molti simboli.
- **Anni '70-'80, codepage**: si usano i 128 caratteri aggiuntivi di un set a 8 bit scelto con un flag di sistema, ma non più di uno alla volta; un file di testo si interpreta correttamente solo conoscendo la codepage per cui è stato pensato. Ne sono state definite più di 1400; la più usata in Europa e Stati Uniti è la ISO/IEC 8859-1 (**Latin-1**), che aggiunge le lettere accentate.
- **1988, prima proposta di Unicode (versione 1.0)**: un sistema che non usa codepage ma unifica tutti i codici dei caratteri (detti **codepoint**), inizialmente a 16 bit; i primi 256 caratteri sono ASCII + Latin-1. 65.536 valori però non bastano (i soli ideogrammi unificati CJK sono 97.680).
- **1996, Unicode 2.0 e successivi**: nelle versioni più recenti si arriva a 149.813 caratteri definiti, con codepoint a 21 bit, organizzati in 161 alfabeti, includendo tutto il CJK. Unicode separa la **definizione** dalla **codifica**: ci sono codifiche ~wide-character~ (UCS-16, 16 bit per carattere, un sottoinsieme; UCS-32, 32 bit, completo ma molto costoso in spazio) e codifiche ~multi-byte~ come **UTF-8**, a 8 bit con un numero variabile di byte per carattere: efficiente ma più complesso da gestire.

Il C supporta tre codifiche per il testo: ~single-byte~ (`char`, va bene per ASCII e Latin-1), ~wide~ (`wchar_t`) e ~multi-byte~ (sempre `char`, con un'interpretazione più elaborata per riconoscere i caratteri). **In Programmazione 1 si usa solo il testo single-byte**, per semplicità.

## Il terminatore della stringa
Una stringa ha una differenza fondamentale rispetto agli array generici: per convenzione è sempre **terminata da un valore sentinella**, il carattere `'\0'`, detto anche **terminatore della stringa** o NUL. La stringa "ciao" è quindi un array di **5** elementi di tipo `char`: `'c'`, `'i'`, `'a'`, `'o'`, `'\0'`.

(In parole povere: il terminatore è il «punto finale» della stringa: dice a printf e alle altre funzioni dove il testo finisce. Poiché occupa una casella, una stringa di 4 lettere richiede un array di 5 caselle.)

![La stringa "ciao" in memoria: quattro caratteri più il terminatore '\0'.](figure/prog/stringa_terminatore.png|12)

Una stringa modificabile si può inizializzare come array (le due righe che seguono sono alternative, non vanno scritte insieme nello stesso blocco):

```c
char txt[] = { 'c', 'i', 'a', 'o', '\0' };
char txt[] = "ciao";    // il compilatore aggiunge il NUL
```

Si può anche fare riferimento a un letterale stringa tramite un puntatore:

```c
const char* txt = "ciao";    // il compilatore aggiunge il NUL
```

## Scandire una stringa: con l'indice o con il puntatore
Poiché una stringa è un array di `char` terminato da `'\0'`, la si può scorrere con un indice oppure con un puntatore. **Con l'array**, la condizione di terminazione è «ripeti fino al terminatore»:

```c
char parola[] = "ciao";

for (size_t i = 0; parola[i] != '\0'; i++) {
    printf("%c\n", parola[i]);
}
```

**Con un puntatore**: si imposta un puntatore al primo carattere (conversione di `parola` in puntatore al primo elemento, `&parola[0]`) e lo si incrementa un carattere alla volta finché non si trova il terminatore:

```c
char parola[] = "ciao";
char* p = parola;    // conversione di parola in puntatore al primo elemento

while (*p != '\0') {
    printf("%c\n", *p);
    p++;             // passa al carattere successivo
}
```

## Leggere una parola da input
Si può leggere una stringa con `scanf` e il formato `%s`, con due avvertenze: `%s` legge una «parola» e si ferma al primo spazio, tab o a capo (quindi non legge frasi con spazi); bisogna **limitare la lunghezza** per evitare il ~buffer overflow~ (si scrive `%19s` se l'array è di 20 caratteri).

```c
#include <stdio.h>

int main(void) {
    char nome[20];   // spazio per massimo 19 caratteri + '\0'
    printf("Inserisci il tuo nome: ");
    scanf("%19s", nome);   // legge una parola (senza spazi)
    printf("Ciao, %s!\n", nome);
}
```

Davanti a `nome` **non si scrive `&`**: nella chiamata l'espressione viene convertita automaticamente in un `char*` che punta a `nome[0]`.

## Leggere una frase con spazi: la maschera di scansione
(In parole povere: la maschera è una «ricetta» di `scanf` che dice quali caratteri accettare e quanti: qui «tutto fino alla fine della riga».)

Per leggere una stringa che contiene spazi (nome e cognome, frasi, titoli) si usa `scanf` con una **maschera di scansione**:

```c
char frase[50];
printf("Inserisci una frase: ");
scanf(" %49[^\n]", frase);
printf("Hai scritto: %s\n", frase);
```

La maschera `" %49[^\n]"` si interpreta così:
- lo spazio iniziale `" "` ignora eventuali spazi o a capo iniziali;
- `%` apre lo specificatore di formato;
- `49` è il numero massimo di caratteri letti (lascia spazio per il `'\0'`);
- `[^\n]` legge tutti i caratteri fino al ~newline~ (il `'\n'` non è incluso).

Se l'utente digita più di 49 caratteri, il resto rimane nel buffer di input. Per input più complessi o su più righe esiste la funzione `fgets()`, che non verrà trattata.

## Errori comuni con le stringhe
**1. Dimenticare il terminatore.**

```c
char nome[4] = {'A', 'n', 'n', 'a'};     // ERRORE: manca '\0'
printf("%s\n", nome);                     // comportamento indefinito
```

I modi corretti sono `char nome[5] = {'A', 'n', 'n', 'a', '\0'};` oppure `char nome[] = "Anna";` (il compilatore aggiunge `'\0'`). Tutte le operazioni sulle stringhe (`printf`, `scanf` e altre come `strlen`) assumono che la stringa sia terminata da `'\0'`: in assenza del terminatore scorrono la stringa **fuori dai suoi limiti**.

**2. Modificare un letterale stringa.** I letterali non sono modificabili: tentare di cambiarli dà comportamento indefinito.

```c
char* s = "ciao";
s[0] = 'm';    // ERRORE: comportamento indefinito
```

Sulle piattaforme di uso comune la modifica produce un errore a runtime. Se invece si inizializza un **array** di `char` si ottiene un array distinto e modificabile:

```c
char s[] = "ciao";
s[0] = 'm';    // ok: "miao"
```

**3. Usare male scanf.**

```c
char parola[20];
scanf("%s", &parola);    // ERRORE: & non necessario
```

Passato come argomento, `parola` viene convertito in un `char*` che punta al primo elemento; `&parola` ha invece tipo `char (*)[20]`, incompatibile. Il modo corretto è `scanf("%s", parola);`, inoltre è buona pratica indicare sempre la lunghezza massima, perché `scanf` non può conoscere la dimensione dell'array e potrebbe scrivere oltre i suoi limiti: `scanf("%19s", parola);` legge al massimo 19 caratteri più il `'\0'`.
