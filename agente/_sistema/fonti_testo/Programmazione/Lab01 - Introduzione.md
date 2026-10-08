# Lab01 - Introduzione

<!-- pagina 1 -->
A.A. 2026/27
Canale B
Programmazione I
Laboratorio
DIPARTIMENTO DI 
INFORMATICA
CORSO DI LAUREA 
TRIENNALE
Introduzione
Lezione nº 1

<!-- pagina 2 -->
Outline
• Come è organizzato il laboratorio
–
Introduzione
–
Come accedere ai PC del laboratorio Turing
• L’interfaccia a riga di comando
–
Cos’è e come funziona
–
Comandi
–
Percorsi dei file
• Programmare con il linguaggio C
–
Installazione del compilatore C
–
Editare un semplice programma
–
Come si compila un programma C
–
Leggere e scrivere con il terminale
–
Esercizi
2

<!-- pagina 3 -->
Informazioni sul corso di Laboratorio
• 30 ore / 10 lezioni
• Docente Teoria:
–
Elvio Amparore (Teoria) elviogilberto.amparore@unito.it
• Docenti Laboratorio:
–
Valerio Basile
valerio.basile@unito.it
–
Elisa Marengo
elisa.marengo@unito.it
• Informazioni su lezioni e orari: via pagina Moodle
• Ricevimento studenti: scrivere via mail, oppure usare forum 
Moodle. Usate solo la posta elettronica di ateneo: 
nome.cognome123@edu.unito.it . Trovate gli indirizzi email 
dei docenti sulle pagine Moodle del corso. 
• Supporto al laboratorio: saranno presenti due assistenti 
(studenti/studentesse secondo/terzo anno) durante le lezioni 
di laboratorio, per supporto.
3

<!-- pagina 4 -->
Accesso alle macchine del laboratorio
Per il laboratorio Turing:
•
Accesso con il login di Ateneo:
Lo stesso login che usate per accedere a www.unito.it e 
per la posta elettronica nome.cognome@edu.unito.it
•
Potete avviare l’ambiente Windows o Linux.
Tasto di 
Accensione
4
•
Attenzione al layout della 
tastiera e ai caratteri speciali nella 
password!
•
Trovate già l’ambiente C installato, con 
un editor di testo.
•
Potete anche usare un vostro portatile 
(ma dovrete installare l’ambiente C). 
username:  nome.cognome
password:  *********

<!-- pagina 5 -->
Come funzionano i PC del laboratorio
• Ogni volta che accedete alle macchine del laboratorio 
Turing con il vostro login, il PC riparte da una 
configurazione di partenza, senza modifiche e senza dati.
•
I file che scrivete vengono persi al logout!
• Ricordatevi di salvare i file che vi servono prima del 
logout - potete usare ad esempio il vostro Drive Google.
• Non potete spegnere i PC, per uscire dovete 
Disconnettervi.
5
Disconnetti

<!-- pagina 6 -->
Norme
•
Durante le esercitazioni in laboratorio è vietato scattare fotografie, 
girare video, registrare suoni ed in generale avere comportamenti 
non adeguati al contesto (si può dormire ma non russare).
•
Si ricorda che tutto il materiale prodotto è protetto da diritto 
d'autore; può essere utilizzato per finalità di studio e di ricerca a uso 
individuale e non può essere utilizzato per finalità commerciali, per 
finalità di lucro anche indiretto (per es. non può essere condiviso su 
piattaforme online a pagamento o comunque su servizi erogati a 
scopo di lucro o su siti che guadagnano con introiti pubblicitari). 
•
È inoltre vietata la condivisione su qualsiasi social media di 
materiale coperto da diritto d'autore, salvo materiale coperto da 
licenze Creative Commons. 
•
Si richiama l'attenzione degli/delle studenti/studentesse a un uso 
consapevole e corretto dei materiali resi disponibili dalla comunità 
universitaria, nel rispetto delle disposizioni del codice etico di 
Ateneo.
6

<!-- pagina 7 -->
Curva di Apprendimento del corso
Questo corso introduce la programmazione partendo dalle basi, e 
non assumiamo che abbiate mai programmato.
• All’inizio, vedremo quindi argomenti che qualcuno di voi ha 
già visto. 
• Tuttavia, vedremo anche diversi argomenti avanzati che 
probabilmente anche chi ha già programmato (es. negli 
Istituti Tecnici) non ha visto oppure ha visto in modo diverso.
• Non sottovalutate quindi la curva di apprendimento: la 
complessità degli argomenti è incrementale.
7
Complessità
Progressione del Corso
Complessità
Progressione del Corso
Seguendo laboratorio e 
facendo esercizi
Senza seguire le lezioni 
facile, già 
visto
esame con 
preparazione 
incompleta

<!-- pagina 8 -->
L’interfaccia 
a riga di comando
Eseguire operazioni tramite 
comandi testuali
8

<!-- pagina 9 -->
La CLI
• Useremo la CLI (Command Line Interface) per 
eseguire manualmente tutti i passi necessari per 
costruire un programma partendo da un file di testo in 
linguaggio C.
• Vediamo quindi un breve riassunto di come funziona 
la CLI del sistema operativo.
• La CLI ha vari nomi:
Shell nei sistemi UNIX
(bash, sh, csh, zsh, …)
Command prompt in Windows
(cmd.exe, powershell)
9
ma anche  terminale, console, riga di comando (command line).

<!-- pagina 10 -->
Interagire tramite comandi testuali
• La CLI si presenta come una 
finestra dove l’utente vede un 
prompt lampeggiante, e può 
inserire dei comandi sotto 
forma di linee di testo.
• Ci sono regole specifiche per 
scrivere i comandi.
• Premendo INVIO, il sistema 
interpreta ed esegue il 
comando, stampando l’output 
(o gli eventuali errori).
10

<!-- pagina 11 -->
Sintassi dei comandi 
Un comando ha un nome, e può essere seguito da opzioni
ed argomenti.
nome_comando opzioni argomenti
• le opzioni definiscono modi alternativi nei quali un 
comando può operare
• gli argomenti sono i dati o i file sui quali il comando 
opera
11
Nella shell UNIX, le opzioni sono introdotte da un trattino '-', in Windows dallo slash '/'
> date /t
> systeminfo
> echo ciao, come stai
Prompt dei comandi (Windows)
$ date
$ uname -a
$ echo “ciao, come stai”
Shell dei comandi (Unix)

<!-- pagina 12 -->
Comandi integrati e comandi esterni
• Alcuni comandi, detti integrati (built-in), sono 
riconosciuti e implementati direttamente dalla 
shell/command-prompt.
• Tutti gli altri comandi sono programmi esterni, che 
vengono avviati per eseguire il comando inserito 
tramite CLI.
• Quando viene dato un comando esterno, la shell carica 
in memoria il programma corrispondente e lo esegue 
con gli argomenti e le opzioni indicate.
• La shell cerca il comando esterno seguendo il percorso 
dei comandi (PATH), memorizzato in una variabile 
d’ambiente.
12

<!-- pagina 13 -->
Esercizio: visualizzare il PATH
• Possiamo dare un comando per stampare il valore 
della variabile d’ambiente PATH:
> echo %PATH%
(Windows)
$ echo $PATH
(Unix)
13

<!-- pagina 14 -->
Nominare i file
Molti comandi operano specificando degli argomenti che 
sono nomi di file sul disco (sui quali effettuano delle 
operazioni).
Esempi:
$ rm importante.txt
$ cp file-su-storage-USB.mp3 lettore-portatile/
È essenziale poter referenziare i nomi dei file nel 
sistema delle cartelle in modo preciso.
• Il percorso (pathname) indica in modo preciso i file
14

<!-- pagina 15 -->
Percorsi assoluti
•
Il percorso assoluto di un file è il nome completo del file nel 
sistema delle cartelle. 
•
Si forma componendo in ordine i nomi delle cartelle da 
attraversare a partire dalla cartella radice del sistema per arrivare 
al file. Gli elementi vengono separati dal carattere slash / in Unix, 
o dal carattere backslash \ in Windows. 
Esempi:
UNIX →
/home/jon_snow$ rm /home/jon_snow/Documenti/cosedafare.txt
Windows →
C:\Users\jon_snow> del C:\Users\jon_snow\Documenti\cosedafare.txt 
Rimuove il file dal nome cosedafare.txt che si trova nella cartella 
Documenti dell’utente jon_snow.
15

<!-- pagina 16 -->
Percorsi relativi
• Il pathname assoluto è uno schema preciso, ma lungo e 
prolisso da scrivere. In molti contesti si può abbreviare 
facendo leva sul concetto di percorso relativo alla 
cartella di lavoro (working directory).
• In Windows la working directory viene indicata prima 
del simbolo '>' nel prompt dei comandi (prima del '$' 
nella shell Unix).
16
C:\Users\jon_snow> cd Documenti
C:\Users\jon_snow\Documenti>
Prompt dei comandi (Windows)
jon_snow@linux:\home\jon_snow$ cd Documenti
jon_snow@linux:\home\jon_snow\Documenti$ 
Shell dei comandi (Unix)
NOTA: cd = change directory

<!-- pagina 17 -->
Percorsi relativi
• Il prompt dei comandi ha sempre una cartella di lavoro. 
• I nomi dei file passati come argomenti ai comandi possono 
essere relativi alla cartella di lavoro, oppure assoluti.
• Percorso relativo: è simile al nome assoluto del file ma la 
cartella iniziale è la cartella di lavoro. 
Esempio:
se C:\Users\jon_snow è la cartella di lavoro, allora il seguente 
comando:
C:\Users\jon_snow> del Documenti\cosedafare.txt
è equivalente a 
C:\Users\jon_snow> del
C:\Users\jon_snow\Documenti\cosedafare.txt
17

<!-- pagina 18 -->
Cartelle in Laboratorio
In Windows le lettere (seguite dal due punti ‘:’) indicano i dischi
• C: disco locale dove trovare i programmi (compilatore, editor)
• D: o altri nomi: altri volumi che avete sul vostro PC 
(in laboratorio Turing abbiamo solo C:) 
Per andare nella nostra cartella Documenti, scriviamo:
cd C:\Users\nome_utente\Documents
18

<!-- pagina 19 -->
19
cd dir
Cambia la working directory in dir
cd ..
Cambia la working directory con la directory superiore
cd
Mostra la working directory attuale
dir
Elenca il contenuto della working directory
dir path
Elenca il contenuto della directory path
mkdir dirA
Crea una nuova directory dirA vuota
rmdir dirA
Rimuove la directory dirA (deve essere vuota)
copy fileA fileB
Copia il contenuto del fileA nel nuovo fileB
copy NUL fileA
Crea un file vuoto di nome fileA
ren fileA fileB
Cambia il nome del fileA in fileB
move pathToA
pathToB
Sposta il file pathToA nella nuova posizione pathToB
del fileA
Elimina il fileA
type fileA
Stampa il contenuto del file fileA nel terminale
start notepad++ fileA
Apre il fileA con il programma Notepad++
C: D: X:
Cambia il disco attivo (radice del filesystem)
Comandi per il command prompt di Windows

<!-- pagina 20 -->
20
cd dir
Cambia la working directory in dir
cd ..
Cambia la working directory con la directory superiore
pwd
Mostra la working directory attuale
ls
Elenca il contenuto della working directory
ls path
Elenca il contenuto della directory path
mkdir dirA
Crea una nuova directory dirA vuota
rmdir dirA
Rimuove la directory dirA (deve essere vuota)
cp fileA fileB
Copia il contenuto del fileA nel nuovo fileB
touch fileA
Crea un file vuoto di nome fileA
mv fileA fileB
Cambia il nome del fileA in fileB
mv pathToA pathToB
Sposta il file pathToA nella nuova posizione pathToB
rm fileA
Elimina il fileA
cat fileA
Stampa il contenuto del file fileA nel terminale
open fileA
xdg-open fileA (Linux)
Apre il fileA con un editor di testo.
Comandi per la shell Unix

<!-- pagina 21 -->
Alcuni dettagli sui comandi
Ci sono due percorsi speciali che si possono usare:
• Il percorso “.” è la cartella di lavoro
Esempio: supponiamo che la cartella di lavoro sia Documenti
I due comandi seguenti sono del tutto equivalenti:
> del .\verbale.txt
(Windows)
> del verbale.txt 
(Windows)
21

<!-- pagina 22 -->
Alcuni dettagli sui comandi
• Il percorso “..” è la cartella che contiene la cartella di lavoro, e 
si usa per risalire la gerarchia delle cartelle
22
Esempio: 
• Supponiamo che la cartella di 
lavoro sia Documenti, e che questa 
sia contenuta nella cartella
jon_snow\
• Si vuole copiare in Documenti il file 
pippo.jpg memorizzato nella 
cartella shared\foto\ dell’utente 
topolino\
Allora possiamo usare il seguente comando:
C:\Users\jon_snow\Documenti> copy ..\..\topolino\shared\foto\pippo.jpg .
C:\
Users\
jon_snow\
Documenti\
topolino\
shared\
foto\
pippo.jpg

<!-- pagina 23 -->
Esercizio
Tramite CLI eseguire i seguenti comandi:
1. Cambiare la cartella di lavoro in 
C:\Users\nome_utente\Documents
2. Creare una nuova cartella PROVA, e al suo interno creare un 
nuovo file importante.txt vuoto
3. Rinominare il file in rilevante.txt
4. Fare una copia di rilevante.txt (usando pathname assoluto e 
poi relativo)
5. Cancellare la copia
6. Impostare la cartella di lavoro sulla cartella che contiene 
PROVA
7. Editare il file rilevante.txt con notepad++
8. Passare ad un altro disco (C: o Z:, se disponibile) (solo 
Windows)
9. Rientrare nella cartella PROVA
23

<!-- pagina 24 -->
Programmare 
con il linguaggio C
Introduzione alla compilazione di 
un programma
24

<!-- pagina 25 -->
Il linguaggio C
Il linguaggio C (in inglese si pronuncia /si:/) è un linguaggio di 
programmazione:
• Procedurale imperativo
–
Si descrivono esplicitamente le istruzioni che devono 
essere eseguite ed il loro ordine. Queste sono organizzate 
in funzioni.
• Strutturato
–
Si impiegano costrutti di flusso di controllo strutturati 
(come cicli, costrutti if/else)
• Supporto alla ricorsione
• Tipato (typed) o tipizzato
• Vicino all’hardware
25

<!-- pagina 26 -->
Risorse online
Vi sono molte risorse online che documentano gli aspetti 
del linguaggio C e della sua libreria.
Tra i più rilevanti:
• C Standard Library header files
https://en.cppreference.com/w/c/header
• C Programming/Standard library reference
https://en.wikibooks.org/wiki/C_Programming/Standard_library_reference
https://en.wikipedia.org/wiki/C_standard_library
• C Language Library
https://cplusplus.com/reference/clibrary/
26

<!-- pagina 27 -->
Popolarità del linguaggio C
TIOBE 2026
(indice di popolarità dei linguaggi 
basato su motori di ricerca)
Stack Overflow Developer 
Survey 2025
(il più recente a oggi)
27
https://www.tiobe.com/tiobe-index/
https://survey.stackoverflow.co/2025/technology#1-programming-
scripting-and-markup-languages

<!-- pagina 28 -->
Quale compilatore C usare
28
• Esistono molti compilatori per il linguaggio C.
• Alcuni esistono da decenni. Si tratta di software di 
notevole importanza e molto sviluppato e testato.
• Il software di sistema mondiale si poggia sulla 
solidità e sull’affidabilità dei compilatori per il 
linguaggio C!
• Noi useremo un compilatore che si chiama gcc
(ma le indicazioni che vedremo sono valide 
sostanzialmente per tutti i compilatori C disponibili)

<!-- pagina 29 -->
Installare il compilatore C
Windows: usiamo MinGW
• Porting nativo su Windows del compilatore gcc
• Versione manutenuta e aggiornata di gcc
• Download da: https://github.com/niXman/mingw-builds-
binaries/releases
Link diretto: https://github.com/niXman/mingw-builds-
binaries/releases/download/15.2.0-rt_v13-rev0/x86_64-15.2.0-release-win32-
seh-msvcrt-rt_v13-rev0.7z
Linux: installare il pacchetto gcc
• sudo apt install build-essential
[Debian]
• sudo dnf install gcc make
[Fedora]
macOS: installare XCode command line tools
(da AppStore o sito apple)
29

<!-- pagina 30 -->
Scaricare MinGW-W64 (Windows)
• Download da:
https://github.com/niXman/mingw-builds-
binaries/releases/download/15.2.0-rt_v13-
rev0/x86_64-15.2.0-release-win32-seh-msvcrt-
rt_v13-rev0.7z
• Estrai l’archivio scaricato in una cartella di tua scelta, 
ad esempio 
–
C:\Users\<Nome Utente>\Documents\mingw64.
30

<!-- pagina 31 -->
Aggiungere il comando gcc.exe al $PATH
• Per utilizzare ‘gcc’ da qualsiasi directory, è necessario 
aggiungere il percorso dell’eseguibile alla variabile di ambiente 
PATH:
-
Apri le Impostazioni di Sistema.
-
Naviga su Sistema →Impostazioni Avanzate di Sistema
-
Clicca su Variabili d’Ambiente
31

<!-- pagina 32 -->
Aggiungere il comando gcc.exe al $PATH
• Procedi con l’aggiornamento della variabile PATH:
-
Nella sezione Variabili utente, seleziona Path e clicca su 
Modifica.
32

<!-- pagina 33 -->
Aggiungere il comando gcc.exe al $PATH
• Completa l’aggiunta del percorso:
-
Clicca su Nuovo e inserisci il percorso della cartella ‘bin‘ di 
MinGW, ad esempio 
C:\Users\<Nome_Utente>\Documents\mingw64\bin.
-
Clicca su OK per confermare le modifiche.
33

<!-- pagina 34 -->
C:\Users\jon_snow> where gcc
C:\MinGW\bin\gcc.exe
C:\Users\jon_snow>
Prompt dei comandi (Windows)
C:\Users\jon_snow> where gcc
INFORMAZIONI: Impossibile trovare i 
file corrispondenti ai criteri di ricerca 
indicati.
C:\Users\jon_snow>
Prompt dei comandi (Windows)
Verifica di installazione
Per verificare che l'installazione sia andata a buon fine, 
apriamo il prompt dei comandi e scriviamo:
> where gcc
oppure
> gcc –version
34

<!-- pagina 35 -->
Scrivere il codice C
Serve un editor di testo semplice, ma che sia adatto alla scrittura 
di codice. Notepad non va bene per questo scopo.
Editor suggerito:
• Notepad++ (Windows)
• … ma ve ne sono molti altri (gedit, Sublime, Atom, etc.)
Non useremo un ambiente di sviluppo integrato (IDE).
Se proprio volete usarli, vi consigliamo di disabilitare strumenti 
avanzati (es: Copilot) che auto-completano gli esercizi che vi 
proponiamo. L’obiettivo è che impariate voi a programmare!
NOTA: all’esame userete una piattaforma web (che vedremo più 
avanti), che vi fornisce un editor di testo semplice.
35

<!-- pagina 36 -->
File di codice in C: estensione .c
• I file di testo che contengono il programma in linguaggio 
C devono avere:
– estensione .c
(unità di compilazione) 
– estensione .h
(file di intestazione)
Suggerimento: in Windows disabilitare 
l’opzione che nasconde le estensioni dei 
nomi  dei file per i file di formato 
“conosciuto”. In questo modo verifichiamo 
che i file di codice che andremo a scrivere 
abbiano effettivamente estensione .c
36

<!-- pagina 37 -->
Creiamo un file .c da compilare
Creiamo un semplice file 
sorgente di prova in 
linguaggio C con nome:
buongiorno.c
37
#include <stdio.h>
int main(void) {   
printf("Buongiorno!\n");
return 0; 
}
buongiorno.c
Scriviamo il testo in 
linguaggio C con un 
editor appropriato.

<!-- pagina 38 -->
Cosa ci serve per compilare
Gli strumenti che useremo:
• Il compilatore C
• Il collegatore (linker)
• Il disassemblatore
Gestiremo vari tipi di file:
• I file sorgente in C (estensioni .c e .h)
• I file oggetto (estensione .o oppure .obj)
• I programmi compilati (estensione .exe o nessuna)
38
preprocessore (cpp)
compilatore (cc)
assemblatore (as)
linker (ld)

<!-- pagina 39 -->
Come funziona la compilazione con il C
39
File di 
intestazione
definizioni comuni
File sorgente
codice del programma 
in forma testuale
Sono le unità di compilazione
File oggetto
unità di compilazione 
in linguaggio macchina
programma 
eseguibile
compilato in 
linguaggio macchina
#include
preprocessore +
compilatore + 
assemblatore
collegatore 
(linker)

<!-- pagina 40 -->
Compilare in C
gcc è il comando del compilatore, e traduce il programma C 
in forma testuale in un file oggetto.
NOTA: stiamo facendo preprocessing, compilazione vera e propria, 
ed assemblamento.
Unix:  
gcc -c sorgente.c -o oggetto.o
Windows:  
gcc -c sorgente.c -o oggetto.obj
40
File oggetto

<!-- pagina 41 -->
Cosa ci serve per collegare (linking)
Il linker prende i file oggetto e li unisce in un unico eseguibile.
Il linker è lo stesso comando gcc, ma senza l’opzione -c
Unix:  
gcc oggetto1.o oggetto2.o -o eseguibile
Windows:  
gcc oggetto1.obj oggetto2.obj -o eseguibile.exe
41
File eseguibile

<!-- pagina 42 -->
Compilare e collegare in un solo passo
Per programmi semplici (es. con un solo file sorgente), è 
possibile anche compilare e collegare in un solo passo:
Unix:  
gcc sorgente.c -o eseguibile
Windows:  
gcc sorgente.c -o eseguibile.exe
42
File eseguibile

<!-- pagina 43 -->
Identificare problemi con gcc
Gli avvertimenti del compilatore (warnings) sono messaggi 
diagnostici visualizzati per certi costrutti che non sono 
inerentemente errati, ma che sono potenzialmente sbagliati 
o indici di errori nel codice.
Per abilitare i warnings, abbiamo due opzioni:
• -Wall
riporta gli avvertimenti
• -Werror se ci sono avvertimenti il programma 
non viene compilato.
43
NOTA: in sede di esame useremo:  -Wall -Werror

<!-- pagina 44 -->
Compilare e collegare con analisi errori
Per abilitare la visualizzazione dei messaggi diagnostici 
aggiuntivi (che aiutano ad individuare errori comuni), 
aggiungiamo le opzioni -Wall -Werror
Unix:  
gcc -Wall -Werror sorgente.c -o eseguibile
Windows:
gcc -Wall -Werror sorgente.c -o eseguibile.exe
44

<!-- pagina 45 -->
Eseguire il programma dalla CLI
Una volta che abbiamo il nostro programma compilato 
come eseguibile, lo possiamo avviare dalla linea di 
comando. Scriviamo:
45
C:\Users\jon_snow> buongiorno
Buongiorno!
C:\Users\jon_snow>
Prompt dei comandi (Windows)
jon_snow@linux:\home\jon_snow$ ./buongiorno
Buongiorno!
jon_snow@linux:\home\jon_snow$ 
Shell dei comandi (Unix)
NOTA: In Unix i comandi che si trovano nella stessa directory si 
avviano aggiungendo ./ come prefisso al nome del comando.

<!-- pagina 46 -->
Come disassemblare un programma C
Il disassembler ci mostra una versione testuale del 
programma compilato. 
Attenzione: viene visualizzato il formato assembly 
dell’eseguibile, non il testo in linguaggio C da cui siamo partiti!
Linux: 
objdump -d eseguibile
macOS:
otool -tv eseguibile
Windows:  
objdump -d eseguibile.exe
46

<!-- pagina 47 -->
Primi esercizi con il linguaggio C
Scriviamo i programmi con un 
editor di testo semplice (ma adatto 
alla programmazione), ed 
eseguiamo manualmente i passi 
che servono per la compilazione.
47

<!-- pagina 48 -->
Leggere e scrivere con il terminale
#include <stdio.h>
int main(void) {
int number;
printf("Scrivi un numero intero: ");
// leggi il numero inserito
scanf("%d", &number);
// mostra il numero a video
printf("Hai scritto: %d\n", number);
return 0;
}
48
scrivi_intero.c

<!-- pagina 49 -->
Tabella delle moltiplicazioni
#include <stdio.h>
int main(void) {
int n;
printf("Scrivi un numero intero: ");
scanf("%d", &n);
// stampa i primi 10 multipli di n
for (int i = 1; i <= 10; ++i) {
printf("%d * %d = %d \n", n, i, n * i);
}
return 0;
}
49
tabella_moltiplicazioni.c

<!-- pagina 50 -->
Esercizi
• Stampa due righe usando due chiamate a printf
• Stampa due righe usando una singola chiamata a 
printf
• Chiedi due numeri, e poi stampali a video
• Stampa la somma di due numeri
• Dichiara tre numeri interi x, y e z, inizializzati con 
valori 5, 8 e 11, e stampa il loro prodotto usando 
printf
• Leggere gli errori di compilazione
50
