# Capitolo 2: L'Interfaccia a Riga di Comando
## Che cos'è la CLI
In laboratorio si usa la **CLI** (~Command Line Interface~) per eseguire manualmente tutti i passi necessari a costruire un programma, partendo da un file di testo in linguaggio C. La CLI ha vari nomi: nei sistemi UNIX si chiama **shell** (bash, sh, csh, zsh, …), in Windows **prompt dei comandi** (cmd.exe, powershell), ma si parla anche di terminale, console o riga di comando.

Si presenta come una finestra in cui l'utente vede un **prompt lampeggiante** e scrive comandi sotto forma di linee di testo. Premendo INVIO il sistema interpreta ed esegue il comando, stampando l'output (o gli eventuali errori). Esistono regole specifiche per scrivere i comandi. I comandi Windows riportati in questo capitolo sono quelli del prompt dei comandi cmd.exe: in PowerShell alcuni (come `echo %PATH%`) si comportano diversamente.

## La sintassi dei comandi
Un comando ha un nome e può essere seguito da opzioni e argomenti:

```
nome_comando opzioni argomenti
```

- le **opzioni** definiscono modi alternativi in cui il comando può operare;
- gli **argomenti** sono i dati o i file su cui il comando opera.

Nella shell UNIX le opzioni sono introdotte da un trattino `-`, in Windows dallo slash `/`. Qualche esempio:

```
> date /t                      (Windows)
> systeminfo
> echo ciao, come stai

$ date                         (Unix)
$ uname -a
$ echo "ciao, come stai"
```

## Comandi integrati e comandi esterni
Alcuni comandi, detti **integrati** (~built-in~), sono riconosciuti e implementati direttamente dalla shell o dal prompt dei comandi. Tutti gli altri sono **programmi esterni**: quando se ne dà uno, la shell carica in memoria il programma corrispondente e lo esegue con gli argomenti e le opzioni indicate. Per trovarlo la shell segue il **percorso dei comandi (PATH)**, memorizzato in una ~variabile d'ambiente~. Per stamparne il valore:

```
> echo %PATH%      (Windows)
$ echo $PATH       (Unix)
```

## Nominare i file: percorsi assoluti e relativi
Molti comandi hanno come argomenti nomi di file sul disco (per esempio `rm importante.txt` oppure `cp file-su-storage-USB.mp3 lettore-portatile/`), quindi è essenziale poterli referenziare in modo preciso nel sistema delle cartelle: lo fa il **percorso** (~pathname~).

Il **percorso assoluto** è il nome completo del file nel sistema delle cartelle: si forma componendo in ordine i nomi delle cartelle da attraversare, a partire dalla cartella radice, fino al file. Gli elementi sono separati dallo slash `/` in Unix e dal backslash `\` in Windows:

```
/home/jon_snow$ rm /home/jon_snow/Documenti/cosedafare.txt          (Unix)
C:\Users\jon_snow> del C:\Users\jon_snow\Documenti\cosedafare.txt   (Windows)
```

Entrambi rimuovono il file cosedafare.txt che si trova nella cartella Documenti dell'utente jon_snow.

Il percorso assoluto è preciso ma lungo da scrivere, per questo si usa spesso il **percorso relativo** alla **cartella di lavoro** (~working directory~): il prompt dei comandi ha sempre una cartella di lavoro, indicata prima del simbolo `>` in Windows e prima del `$` nella shell Unix. Un percorso relativo è come quello assoluto, ma parte dalla cartella di lavoro. Per cambiare cartella si usa `cd` (~change directory~):

```
C:\Users\jon_snow> cd Documenti
C:\Users\jon_snow\Documenti>
```

Con C:\Users\jon_snow come cartella di lavoro, il comando `del Documenti\cosedafare.txt` è equivalente a `del C:\Users\jon_snow\Documenti\cosedafare.txt`.

Esistono due percorsi speciali:
- `.` è la cartella di lavoro: se la cartella di lavoro è Documenti, `del .\verbale.txt` e `del verbale.txt` sono equivalenti;
- `..` è la cartella che contiene la cartella di lavoro, e serve per risalire la gerarchia. Per copiare in Documenti (dentro jon_snow) il file pippo.jpg che sta in shared\foto\ dell'utente topolino si può scrivere:

```
C:\Users\jon_snow\Documenti> copy ..\..\topolino\shared\foto\pippo.jpg .
```

In Windows le lettere seguite dai due punti (C:, D:) indicano i dischi: C: è il disco locale dove si trovano i programmi (compilatore, editor), D: o altri nomi sono altri volumi. Nel laboratorio Turing c'è solo C:. Per andare nella cartella Documenti si scrive `cd C:\Users\nome_utente\Documents` (negli esempi di jon_snow la cartella si chiama Documenti, mentre in quella reale del laboratorio Windows è Documents).

## I comandi principali
Nel prompt dei comandi di **Windows**:
- `cd dir`: cambia la working directory in dir; `cd ..`: sale alla directory superiore; `cd` da solo: mostra la working directory attuale;
- `dir`: elenca il contenuto della working directory (`dir path` quello di path);
- `mkdir dirA` crea una directory vuota; `rmdir dirA` la rimuove (deve essere vuota);
- `copy fileA fileB` copia il contenuto di fileA nel nuovo fileB; `copy NUL fileA` crea un file vuoto;
- `ren fileA fileB` rinomina fileA in fileB; `move pathToA pathToB` sposta il file; `del fileA` lo elimina;
- `type fileA` stampa il contenuto del file nel terminale; `start notepad++ fileA` lo apre con Notepad++;
- `C:`, `D:`, `X:` cambia il disco attivo.

Nella shell **Unix**:
- `cd dir`, `cd ..` come sopra; `pwd` mostra la working directory; `ls` (o `ls path`) elenca il contenuto;
- `mkdir dirA` e `rmdir dirA` come in Windows;
- `cp fileA fileB` copia; `touch fileA` crea un file vuoto; `mv fileA fileB` rinomina; `mv pathToA pathToB` sposta; `rm fileA` elimina;
- `cat fileA` stampa il contenuto; `open fileA` (macOS) o `xdg-open fileA` (Linux) apre il file con un programma adatto.

## Esercizio
Tramite CLI eseguire in ordine questi comandi:
1. cambiare la cartella di lavoro in C:\Users\nome_utente\Documents;
2. creare una nuova cartella PROVA e, al suo interno, un nuovo file vuoto importante.txt;
3. rinominare il file in rilevante.txt;
4. fare una copia di rilevante.txt (usando prima un percorso assoluto e poi uno relativo);
5. cancellare la copia;
6. impostare la cartella di lavoro sulla cartella che contiene PROVA;
7. editare rilevante.txt con notepad++;
8. passare a un altro disco (C: o Z:, se disponibile; solo Windows);
9. rientrare nella cartella PROVA.

Con la CLI sappiamo muoverci tra file e cartelle: nel prossimo capitolo la usiamo per compilare un programma in C.
