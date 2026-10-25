# 25. I Quantificatori Annidati: Significato, Ordine e Dominio
## Più quantificatori in una formula
Finora si è usato un quantificatore alla volta. Per esprimere proprietà più ricche servono formule con **più quantificatori** (si dicono **annidati** quando uno sta dentro la zona d'azione dell'altro): per esempio «comunque si prendano due numeri reali x e y, se x > 0 e y > 0 allora anche x + y > 0» (la somma di due reali positivi è un reale positivo). In simboli si mettono due quantificatori in fila: ∀x ∀y ((x > 0 ∧ y > 0) → x + y > 0), con dominio ℝ × ℝ (il primo quantificatore ha dominio ℝ e il secondo pure). Il problema, qui, è che cosa serve spiegare a un computer per fargli capire una formula con due quantificatori.

**In parole povere:** quantificatori annidati vuol dire che un quantificatore è «dentro» l'altro, come in «per ogni x esiste un y tale che…»: il significato di y dipende da quale x è stato scelto.

**Quantificatori consecutivi dello stesso tipo.** Quando i due quantificatori sono uguali e adiacenti, la complessità non cresce: ∀x ∀y P(x, y) equivale a un unico «per ogni coppia (x, y)», e ∃x ∃y P(x, y) a un unico «esiste una coppia (x, y)».

**In parole povere:** due «per ogni» di seguito dicono «per ogni coppia»; due «esiste» di seguito dicono «esiste una coppia». Non c'è niente di nuovo da capire.
Il problema vero comincia quando i quantificatori sono **diversi**: «per ogni… esiste…» e «esiste… per ogni…» sono impegnativi da studiare. Come sottolineato a lezione, formule con tanti quantificatori diversi si usano nelle scienze (per esempio la definizione di continuità, che si vedrà in Analisi, ha tre quantificatori ciascuno diverso dal precedente), e se si vuole che una macchina le capisca bisogna prima capirle bene.

## Per ogni m esiste un n maggiore
Come si legge «∀m ∃n (m < n)»? A lezione il dominio è quello degli interi (nel libro l'esempio è scritto con dominio ℤ⁺ × ℤ⁺: il ragionamento vale in entrambi i casi); la formula dice che, dato un qualunque intero m, esiste un intero n più grande. È vera: basta prendere n = m + 1, che è positivo se lo è m. Come sottolineato a lezione, la formula esprime il fatto che **non c'è un massimo**: per ogni valore c'è un valore ancora più grande.

La verità della formula dipende però dal **dominio del discorso**:
- sugli interi, sugli interi positivi e sui reali è **vera**: dato m, il numero m + 1 è ancora nel dominio ed è più grande;
- su un insieme finito come {1, 2, …, 10} è **falsa**: per ogni valore da 1 a 9 c'è un valore più grande, ma per 10 non ce n'è;
- lo stesso vale per un intervallo [a, b] dei reali: per x = b non esiste nessun n più grande, perché sopra b non c'è niente.

## Dal linguaggio naturale alla formula
Il libro propone un esempio che cita una canzone: «**Everybody loves somebody**», cioè «ognuno ama qualcuno». Con il predicato L(x, y) = «x ama y», la frase diventa ∀x ∃y L(x, y). Come sottolineato a lezione, qui si fa il lavoro opposto di prima: si parte da una frase del linguaggio comune e la si traduce in un enunciato formale, combinando quantificatori, predicati e connettivi, in modo che anche una macchina lo possa capire.

## I quantificatori non commutano
Si scambia l'ordine dei quantificatori lasciando L(x, y) uguale:
- **∀x ∃y L(x, y)**: ogni persona ama qualcuno (non necessariamente la stessa);
- **∃x ∀y L(x, y)**: c'è una persona che ama tutti;
- scambiando i quantificatori e portandosi dietro le variabili, **∃y ∀x L(x, y)**: c'è qualcuno che è amato da tutti.

Sono tre affermazioni molto diverse. Come sottolineato a lezione, la prima non implica la seconda (ognuno potrebbe amare qualcuno senza che ci sia qualcuno che ama tutti) e la seconda non implica la prima (se una persona ama tutti, potrebbe esserci qualcun altro che non ama nessuno): le due affermazioni sono **indipendenti**, una può essere vera e l'altra falsa o viceversa. Basta cambiare pochissimo la formula perché il significato cambi radicalmente.

![Tre versioni di «x ama y»: ogni persona ama qualcuno; c'è qualcuno che ama tutti; c'è qualcuno amato da tutti.](figure/fond/amore_quantificatori.png|14)

**In parole povere:** nelle formule con più quantificatori l'ordine conta. «Per ogni persona c'è qualcuno» lascia che il «qualcuno» cambi da persona a persona; «c'è qualcuno per ogni persona» vuole un unico «qualcuno» valido per tutte.

## Esempi di verità e falsità
**Un universale doppio vero.** ∀x ∀y ((x > 0 ∧ y > 0) → x + y > 0): la somma di due positivi è positiva. Vale per i reali positivi e anche, per esempio, per gli interi.

**Un universale doppio falso.** Si consideri, su ℝ, la proprietà «per ogni x e per ogni y, se x è negativo e y è positivo, allora x + y ≠ 0». È falsa: basta una coppia che la smentisca, per esempio x = −1 e y = 1, la cui somma è 0. Per falsificare un universale basterebbe una coppia, ma qui ce ne sono infinite (qualunque x negativo, con y = −x). L'enunciato esatto è ricostruito da un tratto poco chiaro della registrazione; è comunque falso anche con i ruoli di x e y scambiati. Come sottolineato a lezione, l'esempio serve solo a esercitarsi nel significato dettagliato dei quantificatori.

**«Per ogni x esiste y con x + y = 0».** ∀x ∃y (x + y = 0). Sugli **interi positivi** è falsa: la somma di due interi positivi non è mai zero, quindi a maggior ragione non ne esiste uno per nessun x. Sui **reali** è vera: dato un reale qualunque x, si sceglie y = −x e si ottiene x + y = 0, qualunque sia x. Come sottolineato a lezione, per l'esistenziale non conta quanti y funzionano: se ne basta uno, anche unico, l'esistenziale è vero; qui l'y è proprio unico, ma questo non importa. La logica dei quantificatori semplifica la realtà, ma così si riescono a seguire i dettagli.

**«Per ogni x esiste y con x > y».** ∀x ∃y (x > y) significa che per ogni x c'è un y più piccolo, cioè **non c'è un minimo** (è la stessa affermazione dell'inizio, con l'ordine opposto). È vera sui reali e sugli interi (basta prendere y = x − 1), ma **falsa** sugli interi positivi, dove il minimo c'è ed è 1: per x = 1 non esiste nessun intero positivo più piccolo.

Il capitolo successivo mostra come si decide una formula con quantificatori annidati scrivendo un programma, su un dominio finito.
