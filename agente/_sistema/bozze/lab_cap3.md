# Capitolo 3: Preparare l'Ambiente per Programmare in C
## Il linguaggio C
Il linguaggio C (in inglese si pronuncia /si:/) è un linguaggio di programmazione:
- **procedurale imperativo**: si descrivono esplicitamente le istruzioni da eseguire e il loro ordine, organizzate in funzioni;
- **strutturato**: si usano costrutti di flusso di controllo strutturati, come cicli e if/else;
- con **supporto alla ricorsione**;
- **tipato** (o tipizzato);
- **vicino all'hardware**.

Sul web esistono molte risorse che documentano il linguaggio e la sua libreria; tra le più rilevanti ci sono i riferimenti di cppreference.com (~C Standard Library header files~), il wikibook ~C Programming/Standard library reference~ e cplusplus.com (~C Language Library~).

## Quale compilatore usare
Esistono molti compilatori per il C, alcuni attivi da decenni: sono software di notevole importanza, molto sviluppato e testato, e il software di sistema mondiale si poggia sulla loro solidità e affidabilità. Le slide ne mostrano la popolarità con l'indice TIOBE 2026 e lo Stack Overflow Developer Survey 2025. Nel corso si usa **gcc**, ma le indicazioni valgono sostanzialmente per tutti i compilatori C.

## Installare il compilatore
- **Windows**: si usa **MinGW**, il porting nativo di gcc su Windows, in una versione manutenuta e aggiornata, scaricabile da GitHub (progetto ~mingw-builds-binaries~). Si scarica l'archivio .7z (nelle slide è la versione 15.2.0) e lo si estrae in una cartella a scelta, ad esempio C:\Users\<Nome_Utente>\Documents\mingw64.
- **Linux**: si installa il pacchetto gcc, ad esempio con `sudo apt install build-essential` (Debian) oppure `sudo dnf install gcc make` (Fedora).
- **macOS**: si installano gli ~Xcode command line tools~ (dall'App Store o dal sito Apple).

## Aggiungere gcc al PATH (Windows)
Per usare `gcc` da qualsiasi cartella bisogna aggiungere il percorso dell'eseguibile alla variabile d'ambiente PATH, già incontrata nel capitolo 2:
1. aprire le Impostazioni di Sistema e andare su Impostazioni avanzate di sistema;
2. cliccare su ~Variabili d'ambiente~;
3. nella sezione ~Variabili utente~ selezionare Path e cliccare su ~Modifica~;
4. cliccare su ~Nuovo~ e inserire il percorso della cartella bin di MinGW, ad esempio C:\Users\<Nome_Utente>\Documents\mingw64\bin;
5. cliccare su OK per confermare.

Per verificare che l'installazione sia riuscita si apre il prompt dei comandi (cmd) e si scrive `where gcc` (che mostra il percorso di gcc.exe se è stato trovato, altrimenti segnala che non trova i file) oppure `gcc --version`.

## L'editor per il codice
Per scrivere il codice serve un **editor di testo semplice ma adatto al codice**: Notepad non va bene. Quello suggerito su Windows è **Notepad++**, ma ve ne sono molti altri (gedit, Sublime, Atom, …). Nel corso **non si usa un ambiente di sviluppo integrato (IDE)**: chi proprio vuole usarlo è invitato a disabilitare gli strumenti che auto-completano gli esercizi (come Copilot), perché l'obiettivo è imparare a programmare da soli. All'esame si userà una piattaforma web, che fornisce un editor di testo semplice.

## I file di codice: estensioni .c e .h
I file di testo con il programma in C devono avere estensione **.c** (le ~unità di compilazione~) oppure **.h** (i ~file di intestazione~). In Windows conviene disabilitare l'opzione che nasconde le estensioni dei file di formato "conosciuto", così si verifica che i file scritti abbiano davvero l'estensione .c.

## Un primo file sorgente
Come prova creiamo con un editor appropriato un file di nome **buongiorno.c**:

```c
#include <stdio.h>
int main(void) {
    printf("Buongiorno!\n");
    return 0;
}
```

Nel prossimo capitolo vediamo come trasformare questo testo in un programma eseguibile.
