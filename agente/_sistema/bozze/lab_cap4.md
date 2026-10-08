# Capitolo 4: La Compilazione di un Programma C
## Gli strumenti e i file coinvolti
Per costruire e ispezionare un programma usiamo tre strumenti: il **compilatore C**, il **collegatore** (~linker~) e il **disassemblatore**. Si gestiscono vari tipi di file:
- i **file sorgente** in C (estensioni .c e .h);
- i **file oggetto** (estensione .o oppure .obj);
- i **programmi compilati** (estensione .exe oppure nessuna).

In realtà dietro il comando gcc lavorano più programmi in sequenza: il preprocessore (cpp), il compilatore (cc), l'assemblatore (as) e il linker (ld).

## Come funziona la compilazione
Il processo parte dai **file sorgente**, cioè il codice del programma in forma testuale: sono le **unità di compilazione**. A questi si aggiungono i **file di intestazione**, con le definizioni comuni, inclusi con `#include`. Il preprocessore, il compilatore e l'assemblatore li trasformano in **file oggetto**: unità di compilazione in linguaggio macchina. Il **collegatore** (~linker~) unisce poi i file oggetto in un unico **programma eseguibile**, compilato in linguaggio macchina.

## Compilare: dal sorgente al file oggetto
gcc è il comando del compilatore e traduce il programma C in forma testuale in un file oggetto. Con l'opzione `-c` esegue preprocessing, compilazione vera e propria e assemblamento; l'opzione `-o` indica il nome del file di output:

```
Unix:     gcc -c sorgente.c -o oggetto.o
Windows:  gcc -c sorgente.c -o oggetto.obj
```

## Collegare: dai file oggetto all'eseguibile
Il linker prende i file oggetto e li unisce in un unico eseguibile. È lo stesso comando gcc, ma **senza l'opzione -c**:

```
Unix:     gcc oggetto1.o oggetto2.o -o eseguibile
Windows:  gcc oggetto1.obj oggetto2.obj -o eseguibile.exe
```

## Compilare e collegare in un solo passo
Per programmi semplici, per esempio con un solo file sorgente, si possono fare le due cose insieme:

```
Unix:     gcc sorgente.c -o eseguibile
Windows:  gcc sorgente.c -o eseguibile.exe
```

## Individuare i problemi: gli avvertimenti
I **warnings** sono messaggi diagnostici visualizzati per certi costrutti che non sono intrinsecamente errati, ma sono potenzialmente sbagliati o indizi di errori nel codice. Per abilitarli ci sono due opzioni:
- `-Wall` riporta gli avvertimenti;
- `-Werror` fa sì che, se ci sono avvertimenti, il programma non venga compilato.

Si usano insieme, per esempio con `gcc -Wall -Werror sorgente.c -o eseguibile` (su Windows con `-o eseguibile.exe`). **In sede di esame si usano le opzioni -Wall -Werror**, quindi conviene abituarsi da subito.

## Eseguire il programma dalla CLI
Una volta ottenuto l'eseguibile, lo si avvia dalla riga di comando:

```
C:\Users\jon_snow> buongiorno                (Windows)
Buongiorno!

jon_snow@linux:/home/jon_snow$ ./buongiorno  (Unix)
Buongiorno!
```

In Unix i comandi che si trovano nella stessa directory si avviano aggiungendo `./` come prefisso al nome del comando.

## Disassemblare un programma
Il **disassemblatore** mostra una versione testuale del programma compilato. Attenzione: viene visualizzato il formato **assembly** dell'eseguibile, non il testo in C da cui si è partiti. I comandi sono:

```
Linux:    objdump -d eseguibile
macOS:    otool -tv eseguibile
Windows:  objdump -d eseguibile.exe
```

Ora che sappiamo compilare, possiamo scrivere i primi programmi che interagiscono con il terminale.
