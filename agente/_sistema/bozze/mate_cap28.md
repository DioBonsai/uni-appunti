# 28. Le Combinazioni con Ripetizione
## Il quarto tipo di scelta
Si sono visti gli ordinamenti, le disposizioni semplici e con ripetizione e le combinazioni semplici. Manca l'ultimo caso, le **combinazioni con ripetizione**: scelte non ordinate in cui lo stesso elemento si può scegliere più volte. Un esempio già incontrato è una pasticceria con un certo numero di tipi di pasticcini, da cui si vuole un vassoio con un certo numero di pezzi: l'ordine in cui si mettono i pasticcini non conta, ma lo stesso tipo si può prendere sei o sette volte. Un esempio più matematico sono i monomi.

Sia A un insieme con n ≥ 1 elementi e si devono fare k scelte in A, non ordinate e possibilmente ripetute. Una **combinazione con ripetizione** di ordine k in A è una scelta di questo tipo; il loro numero si indica con C^{r}_{n,k}, dove la r sta per «ripetizione» (non è un esponente). Il numero k è qualunque: non è detto che debba essere minore di n, come si vede sotto.

(In parole povere: è la scelta di un vassoio di pasticcini, in cui non conta l'ordine in cui li metti dentro ma conta quanti ne prendi di ogni tipo. Puoi prendere il tipo preferito anche cinque volte, e puoi prenderne più di quanti siano i tipi.)

## Contare i monomi
Un **monomio** in più variabili è un'espressione fatta di variabili elevate a un certo esponente. Il suo **grado** è la **somma degli esponenti**. Per esempio x³ y² z⁵ è un monomio in tre variabili x, y, z, e ha grado 3 + 2 + 5 = 10. Per semplicità si considerano solo monomi con coefficiente 1.

(In parole povere: un monomio è una "parola" fatta di lettere ripetute, per esempio x x x y y z z z z z, che si scrive in breve x³ y² z⁵. Il grado è quante lettere ci sono in tutto: qui 3 + 2 + 5 = 10.)

La domanda è: quanti sono i monomi diversi di grado 10 in tre variabili? Se ne possono scrivere moltissimi, a cominciare da x¹⁰ (una variabile può comparire con esponente 0), poi x⁹ y, x⁹ z, x⁸ y² e così via. Si può saperlo senza elencarli tutti?

Si osserva che si sta facendo una scelta in un insieme (le variabili x, y, z) e che è **non ordinata**: x² · x · y² · z³ · z² e x · x² · z² · y² · z³ sono lo stesso monomio x³ y² z⁵: scritti con i fattori in un altro ordine, sono uguali, perché il prodotto è commutativo e si possono raggruppare tutte le x, tutte le y e tutte le z. Quindi l'ordine di scelta non conta. A differenza delle combinazioni semplici però qui gli elementi si scelgono **più volte**: nel monomio x³ y² z⁵ si sono scelte 3 volte la x, 2 volte la y e 5 volte la z, per un totale di 10 scelte, cioè il grado.

## Il trucco delle caselle e dei separatori
Per contarli si rappresenta ogni monomio con una riga di 10 caselle, ognuna delle quali è la scelta di una variabile. Per comodità si dispongono in ordine tutte le x, poi le y, poi le z: il monomio x³ y² z⁵ diventa x x x y y z z z z z. Per un altro monomio, per esempio x⁴ y³ z³, si cambiano solo i punti in cui si passa da una variabile all'altra.

Il passo cruciale è che **tutta l'informazione sta nei punti di cambiamento**, non in che cosa c'è nelle caselle. Se si decide dove la x diventa y e dove la y diventa z, il monomio è determinato. Con tre variabili ci sono due punti di cambiamento (con sei variabili sarebbero cinque, e in generale una in meno del numero di variabili). Quindi contare i monomi equivale a contare in quanti modi si possono inserire due «sbarrette» di separazione nella riga.

![Il monomio x³ y² z⁵ in 10 caselle, e nella versione a 12 caselle in cui le due separazioni occupano una casella ciascuna; sotto, il caso x² z⁸, in cui mancando la y i separatori sono vicini ma in caselle distinte.](figure/mate/ch28_caselle_separatori.png|13)

Qui c'è però una complicazione. Per un monomio come x² z⁸, in cui manca la y, le due sbarrette finiscono nello stesso punto (la zona delle y si restringe a zero), e lo stesso accade se manca la prima o l'ultima variabile, per esempio x¹⁰ o z¹⁰. Bisogna quindi tenere conto che le due sbarrette possono cadere nello stesso posto, e questo complica il conteggio. Si risolve con un trucco: invece di mettere le separazioni **fra** le caselle, si prende una striscia di **12 caselle**, cioè le 10 di prima più 2, e si **riservano due caselle** alle separazioni. Si riscrive per esempio x x x • y y • z z z z z, dove i due punti segnano le separazioni.

Non si è persa informazione: da questa striscia si ricava il monomio cancellando le due caselle di separazione, e viceversa dal monomio si ricostruisce la striscia. Il vantaggio è che ora le due separazioni occupano **caselle distinte**, e si possono scegliere in modo del tutto arbitrario: per x² z⁸ la striscia è x x • • z z z z z z z z, con le separazioni vicine ma non sovrapposte.

## Il conteggio
I monomi di grado 10 in tre variabili sono quindi tanti quanti i modi di scegliere 2 caselle (le separazioni) fra 12. Scegliere 2 caselle su 12 è una combinazione semplice di ordine 2 sulle 12, e quindi

C^{r}_{3,10} = C_{12,2} = 12! / (2! · 10!) = (12 · 11)/2 = 66.

Ci sono 66 monomi di grado 10 in tre variabili.

(In parole povere: invece di contare i monomi direttamente, si conta una cosa più facile che corrisponde esattamente a loro, cioè quante coppie di caselle si possono scegliere per mettere le separazioni. Dato che da una striscia si ricava un monomio e viceversa, i due conteggi coincidono.)

## La formula generale
Questo metodo non dipende dal problema particolare: le variabili x, y, z sono semplicemente gli elementi di un insieme da cui si sceglie. Il 2 che compare nel risultato è il numero delle separazioni, cioè il numero degli oggetti meno 1, perché per separare n oggetti servono n − 1 sbarrette (con un solo oggetto non servono separazioni, con due ne basta una, con tre ne servono due). Il 12 è invece il numero delle scelte originali, 10, più le caselle di separazione, 2.

In generale, con A insieme di n elementi e k scelte (anche ripetute):
- le separazioni sono n − 1;
- la striscia ha k + (n − 1) = k + n − 1 caselle;
- si scelgono le n − 1 caselle delle separazioni fra le k + n − 1.

**Proposizione.** Il numero delle combinazioni con ripetizione di k elementi scelti fra n è

C^{r}_{n,k} = C_{k+n−1, n−1} = (k + n − 1)! / ((n − 1)! · k!).

Nella formula, la differenza (k + n − 1) − (n − 1) è proprio k, ed è per questo che al denominatore compare k!. Con n = 3 e k = 10 si ritrova C_{12,2} = 66. È un risultato curioso e interessante: il calcolo delle combinazioni con ripetizione si è ricondotto a un problema già risolto, quello delle combinazioni semplici, in una situazione non identica ma strettamente imparentata, in cui cambiano soltanto i numeri.

## I pasticcini
La formula serve anche per il problema della pasticceria. Una pasticceria ha 20 tipi di pasticcini e si vuole un vassoio con 30 pasticcini. Poiché lo stesso tipo si può scegliere più volte, è un problema di combinazioni con ripetizione: 30 scelte (k = 30) fra 20 oggetti (n = 20). Si noti che le scelte sono più degli oggetti, e va bene lo stesso, perché la ripetizione è ammessa. Il numero è

C^{r}_{20,30} = C_{30+20−1, 20−1} = C_{49,19} = (49 su 19) = 49! / (19! · 30!).

Si può immaginare la striscia di caselle: le 30 caselle dei pasticcini più 19 caselle di separazione fra i 20 tipi, in totale 49; il numero è quello dei modi di scegliere le 19 caselle di separazione fra le 49. È un numero molto grande (circa 1,9 · 10¹³, cioè 18 851 684 897 584), molto più grande delle sestine del superenalotto, e come per gli altri problemi interessa soprattutto il procedimento.

## Il quadro completo dei conteggi
Con questo capitolo si completa il quadro delle scelte di k elementi in un insieme di n, che si distinguono con due domande, l'ordine conta? e le scelte si possono ripetere?:
- scelte ordinate, **con ripetizione**: disposizioni con ripetizione, D^{r}_{n,k} = n^{k};
- scelte ordinate, **senza ripetizione**: disposizioni semplici, D_{n,k} = n!/(n − k)!, e con k = n gli ordinamenti, n!;
- scelte non ordinate, **senza ripetizione**: combinazioni semplici, C_{n,k} = (n su k);
- scelte non ordinate, **con ripetizione**: combinazioni con ripetizione, C^{r}_{n,k} = C_{k+n−1, n−1}.

Queste sono le tecniche di base: con i problemi dei capitoli 26 e 27 si tratta poi di capire a quale tipo di scelta si riconduce il testo e di suddividere la scelta in passi.
