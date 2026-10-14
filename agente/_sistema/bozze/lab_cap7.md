# Capitolo 7: Laboratorio 2: Tipi, Documentazione ed Esercizi di Sintesi
## La tabella dei tipi e degli specificatori
La seconda parte del laboratorio 2 riguarda i tipi del C. Il laboratorio riporta due tabelle con la dimensione di ogni tipo (in byte e in bit), l'intervallo dei valori e lo specificatore di conversione, per CPU a 32 e a 64 bit, e approfondiscono quanto visto sui tipi nel capitolo 6 della teoria. Gli intervalli dei tipi interi con segno vanno da −2^{N−1} a 2^{N−1} − 1, dove N è il numero di bit (per esempio da −2^{31} a 2^{31} − 1 per un int).

I **tipi con segno** e i loro specificatori sono:
- char (1 byte): %c;
- short (2 byte): %hd;
- int (4 byte): %d;
- long (4 byte su CPU a 32 bit, 8 su 64): %ld;
- long long (8 byte): %lld;
- ptrdiff_t (4 byte a 32 bit, 8 a 64): %t nella tabella del corso (lo specificatore completo in C è %td);
- float (4 byte, intervallo da circa 10^{-38} a 10^{38}): %f;
- double (8 byte, da circa 10^{-308} a 10^{308}): %lf nella tabella, anche se in printf %f va bene per entrambi i tipi (capitolo 14 della teoria).

I **tipi senza segno** sono unsigned char (%hhu), unsigned short (%hu), unsigned int (%u), unsigned long (%lu), unsigned long long (%llu) e size_t (%zu); i loro valori vanno da 0 a 2^{N} − 1, dove N è il numero di bit del tipo. Due precisazioni: le dimensioni sono indicative, perché dipendono dal sistema in uso (come per long int: per esempio su Windows a 64 bit con gcc un long occupa 4 byte), e **non serve imparare a memoria queste tabelle**.

## Le dimensioni dei tipi
L'esercizio sul programma **dim_tipi.c** chiede di leggerlo, compilarlo e provarlo, e di rispondere a una domanda: quale caratteristica hanno le dimensioni dei tipi puntatore, e perché. La risposta si trova nel capitolo 12 della teoria: un puntatore occupa la stessa quantità di memoria qualunque sia il tipo della variabile a cui punta (per esempio 8 byte su una piattaforma a 64 bit), perché contiene sempre e solo un indirizzo, la cui dimensione dipende dalla piattaforma e non dal tipo puntato.

## La documentazione del linguaggio
Si può usare una versione **offline** della documentazione del linguaggio e della libreria del C:
1. accedere a https://en.cppreference.com/w/c;
2. andare su "Offline version" in fondo alla pagina e scaricare la versione più recente (Unofficial Release);
3. aprire la pagina `html-book/reference/en/c.html`;
4. cercare nella sezione degli header la documentazione di `<stdio.h>` e leggere la documentazione completa di printf.

Il laboratorio avverte che la documentazione di riferimento è molto più elaborata di quanto visto finora, ma serve per imparare a cercare le informazioni di cui si ha bisogno (come visto nel capitolo 15 della teoria).

## Esercizio: il mercato
L'esercizio **mercato.c** chiede di calcolare la spesa al supermercato: 3 pacchi di orecchiette, a 1,50 euro al pacco, e 1 kg e mezzo di pomodori, a 2,50 euro al kg. La funzione main deve calcolare e visualizzare la spesa totale. I suggerimenti sono di modellare il problema con variabili dichiarate con tipi adeguati, usare una variabile anche per il totale, indentare e commentare il programma.

Poiché i prezzi e il peso dei pomodori non sono interi servono dei tipi reali (float o double), e il totale è 3 × 1,50 + 1,5 × 2,50 = 4,50 + 3,75 = **8,25 euro**. Infine il programma va modificato per far inserire le quantità da tastiera, invece di fissarle nel codice, con scanf: ricordando che per leggere un double si usa %lf (capitolo 14 della teoria). Nel codice i decimali si scrivono con il punto (1.50), non con la virgola.

## Esercizio: scambio di quattro variabili
L'esercizio sullo scambio parte dal programma **scambio.c**, simile a quello visto a lezione (capitolo 13 della teoria), da leggere, compilare e provare. Poi bisogna scrivere **scambio4.c**, con quattro variabili intere v1, v2, v3 e v4, inizializzate a piacere, da scambiare in modo che v1 prenda il valore di v2, v2 quello di v3, v3 quello di v4 e v4 quello originale di v1. I valori vanno stampati prima e dopo lo scambio.

L'idea è quella della variabile temporanea: il valore di v1 va salvato prima di essere sovrascritto. Con una variabile d'appoggio temp:

```c
temp = v1;
v1 = v2;
v2 = v3;
v3 = v4;
v4 = temp;
```

Con v1, v2, v3 e v4 uguali a 1, 2, 3 e 4 il risultato è 2, 3, 4, 1. Anche qui l'ordine è essenziale: ogni assegnamento deve avvenire quando il valore che sta per essere sovrascritto è già stato copiato altrove.
