# 28. De Morgan con Più Quantificatori e Perché un Quantificatore è un Lavoro Infinito
## Nota sulla fonte
La Lezione 13 del 2026 (lunedì 26 ottobre) è una lezione di chiusura del capitolo 1 della Parte 2: esercizi sulle lezioni 07-12 (connettivi, quantificatori, regole logiche). La registrazione 2026 non è disponibile; i capitoli 28-30 si basano sulla registrazione della stessa lezione dell'anno precedente (16 ottobre 2025, stesso docente e stesso programma) e sulle pagine del testo del docente che compaiono nel video.

## Portare le negazioni all'interno
Davanti a una formula con più quantificatori si può usare la legge di De Morgan, esattamente come si fa davanti a una formula con congiunzioni e disgiunzioni: si porta la negazione sempre più all'interno. Regole, ricordate a lezione:
- ogni volta che la negazione **scavalca una disgiunzione**, questa diventa una congiunzione, e viceversa;
- quando due negazioni si toccano, si cancellano (doppia negazione);
- quando si arriva a una **formula atomica** (una formula le cui parti non sono più formule, per esempio x·y < 1; in parole povere: una formula che non si può più spezzare in formule più semplici), si può usare la negazione «opposta» del confronto;
- ogni volta che la negazione **scavalca un quantificatore**, il quantificatore cambia: ∀ diventa ∃ e ∃ diventa ∀.

(In parole povere: la negazione «attraversa» i quantificatori e li capovolge, e a ogni passo la formula resta equivalente, cioè non cambia il suo valore di verità.)

Il motivo per cui conviene eliminare le negazioni è che per noi è difficile capire il significato di un «non»: è già faticoso immaginare quando succede qualcosa, e ancora di più quando non succede.

Le leggi di De Morgan per i quantificatori annidati sono:
- ¬(∀x∃y P(x, y)) ≡ ∃x¬(∃y P(x, y)) ≡ ∃x∀y ¬P(x, y);
- ¬(∃x∀y P(x, y)) ≡ ∀x¬(∀y P(x, y)) ≡ ∀x∃y ¬P(x, y).

## Un esempio completo
Si parte da **∃x∀y (xy < 1)**, con x e y numeri reali. È **vera**: basta scegliere x = 0, perché allora 0 · y = 0 < 1 per ogni y.

Si nega: ¬(∃x∀y(xy < 1)). Passo per passo:
1. la negazione scavalca ∃x e diventa ∀x¬(∀y(xy < 1));
2. scavalca ∀y e diventa ∀x∃y¬(xy < 1);
3. si arriva alla formula atomica: ¬(xy < 1) si scrive **xy ≥ 1**.

Si ottiene **∀x∃y(xy ≥ 1)**, che è **falsa**, perché equivalente alla negazione di una formula vera. Ed è facile vederlo anche direttamente: se la formula fosse vera per tutti gli x lo sarebbe anche per x = 0, ma in quel caso bisognerebbe trovare un y con 0 · y ≥ 1, cioè 0 ≥ 1, che è falso. Quindi x = 0 è un **controesempio** per la quantificazione universale: è lo stesso valore di x che rende vera la formula di partenza.

## La negazione di un confronto
Attenzione a come si nega un confronto. Dati due numeri a e b, i casi possibili sono tre: a < b, a = b, a > b. Se si nega a < b, restano gli altri due: a = b oppure a > b, cioè **a ≥ b**. Quindi **la negazione di «minore» è «maggiore o uguale»**, non «maggiore». Analogamente:
- ¬(a < b) è a ≥ b;
- ¬(a > b) è a ≤ b;
- ¬(a ≤ b) è a > b;
- ¬(a ≥ b) è a < b.

Questa operazione ha la proprietà che, applicata due volte, riporta alla formula di partenza (si dice **involutiva**: «involvere» vuol dire tornare indietro). Come aveva osservato il docente, la negazione fa comparire l'uguale oppure lo toglie; è un'osservazione semplice ma utile anche in programmazione, quando si deve scrivere il test opposto di uno dei sei test di base (uguale, diverso, minore, maggiore, minore o uguale, maggiore o uguale).

(In parole povere: negare un confronto vuol dire prendere tutti i casi in cui il confronto è falso, uguaglianza compresa.)

## Perché un quantificatore è un lavoro infinito
Il corso non dimostra risultati importanti per l'algebra lineare o per l'intelligenza artificiale: si occupa di esempi molto semplici per capire che difficoltà incontra una macchina nello stabilire la verità di un'affermazione, specialmente con i quantificatori, che **non si possono verificare direttamente quando il dominio è infinito**.

Per esempio, un controesempio basta per rendere falsa un'affermazione universale, ma se fosse vera bisognerebbe controllare infiniti casi. Altro esempio: per controllare che **non** esistano x e y maggiori di 1 con prodotto 7 (cioè che 7 sia primo) bisognerebbe, in linea di principio, provare tutti i numeri naturali. Con un ragionamento semplice si riduce il lavoro a un lavoro finito: basta guardare i numeri minori di 7, perché una scomposizione è fatta da due numeri entrambi più piccoli del numero dato. Ma ci vuole comunque **un ragionamento**: finché non si sa qualcosa di più sull'affermazione, un quantificatore richiede un lavoro infinito.

(In parole povere: una macchina non può provare tutti i numeri a uno a uno, e per questo servono dei ragionamenti che dimostrino la verità in tutti i casi insieme.)

## Le macchine possono ragionare con rigore?
A lezione il docente ha fatto qualche cenno di curiosità, senza dimostrazioni. Il ragionamento logico rigoroso, senza errori, è molto più difficile da far fare a una macchina dei ragionamenti informali con una certa percentuale di errori, che oggi si sanno far fare con una certa facilità.

Una prova che usa esplicitamente le regole logiche si chiama **prova formale** (in parole povere: una prova scritta con tutti i passaggi, senza saltare nulla); le prove della matematica di tutti i giorni non lo sono, e le prove formali sono molto più lunghe. Il rapporto fra la lunghezza della versione formale e quella della prova informale originaria si chiama **De Bruijn loss factor**. Circa 45 anni fa, quando si è cominciato a far fare queste prove a una macchina, era di circa 10-20; per le immagini, invece, il rapporto fra la rappresentazione completa e ciò di cui siamo consapevoli è enorme: un'immagine di circa un milione di punti, con tre byte per punto (rosso, verde e blu), occupa circa 24 milioni di cifre binarie, mentre noi la riassumiamo in una frase. Nel libro del docente si riporta che negli anni recenti (circa cinque anni fa, secondo il docente) il fattore è sceso a circa 4: con un fattore così piccolo le prove diventano quasi trattabili.

Per l'informatica interessano soprattutto le prove di **correttezza di programmi** (per esempio di un ciclo), che sono prove piccole. I **proof assistant** sono programmi che aiutano a controllare queste prove (in parole povere: assistenti che verificano che ogni passaggio della prova sia valido). Gli esempi citati sono **Frama-C**, che serve a controllare che un programma C non abbia errori a tempo di esecuzione né deviazioni dalla specifica, e **Dafny**, accennato nel corso di Programmazione I e usato davvero nel corso di Metodi Formali dell'Informatica; il docente ha detto di non averli usati personalmente.

Perché si fanno queste prove? Provare un programma su molti esempi, anche miliardi di esempi casuali, non basta: alcuni errori si manifestano in situazioni che nessuno ha ancora immaginato. L'unico modo per essere sicuri che il programma funzioni in tutti i casi è un ragionamento che valga per tutti gli infiniti casi, cioè un ragionamento con quantificatori, e si vorrebbe delegarlo il più possibile a una macchina. Gli errori nei programmi non si possono tollerare, perché possono costare molto (il docente ha ricordato il blocco del canale di Suez causato dalla guida automatica di una nave).

Nei capitoli seguenti si fanno esercizi di ripasso: quiz con domini diversi e un esempio costruito con il «mondo di Tarski».
