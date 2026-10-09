# 16. Verificare Iniettività e Suriettività: Esempi
## Due condizioni indipendenti
Per le definizioni di funzione iniettiva, suriettiva e biettiva si veda il capitolo 14. Le due condizioni sono **indipendenti**: una funzione può non essere né iniettiva né suriettiva, può essere solo suriettiva, solo iniettiva oppure entrambe. Nell'ultimo caso è **biettiva**.

Vediamo alcuni esempi, dal più semplice al più istruttivo.

## L'identità è biettiva
Per id_{A} : A → A, id_{A}(a) = a, l'iniettività è immediata: se a ≠ a′ allora id_{A}(a) = a è diverso da id_{A}(a′) = a′. La suriettività è altrettanto semplice: ogni elemento a del codominio è immagine di sé stesso. Le uguaglianze si leggono in entrambi i versi: da sinistra a destra è la definizione di identità, da destra a sinistra dice che ogni elemento si scrive come immagine di qualcosa, cioè di sé stesso.

## La proiezione: suriettiva ma (in generale) non iniettiva
Consideriamo la prima proiezione p_{1} : A × B → A, p_{1}(a, b) = a, con B non vuoto.

**Non è iniettiva.** Iniettiva vorrebbe dire: se (a, b) ≠ (a′, b′) allora a ≠ a′. Ma due coppie sono uguali solo se coincidono **entrambe** le componenti, quindi sono diverse anche quando ne differisce una sola. Per esempio (1, 2) ≠ (1, 5) come coppie, eppure hanno la stessa prima componente e quindi la stessa immagine. Nel piano cartesiano sono due punti sulla stessa retta verticale, che la proiezione manda nello stesso punto dell'asse delle ascisse.

**È suriettiva.** Dato a ∈ A basta scegliere un qualsiasi elemento b ∈ B: la coppia (a, b) ha immagine a. Qui serve che B non sia vuoto (precisazione); l'elemento scelto in B è irrilevante, perché la proiezione lo ignora. Tutta la retta verticale sopra a viene mandata in a.

Esiste un solo caso in cui p_{1} diventa iniettiva: quando B ha **un solo elemento**. Allora non si possono scegliere due elementi diversi di B, quindi due coppie diverse differiscono necessariamente nella prima componente. A parte questo caso eccezionale, la proiezione è suriettiva ma non iniettiva.

## La funzione affine f(x) = ax + b su ℝ
Sia f : ℝ → ℝ, f(x) = ax + b, con a e b costanti e **a ≠ 0**. Graficamente è una retta, ma per esercizio la studiamo per via algebrica.

**Iniettività.** Si prendono due numeri x e y e si suppone che abbiano la stessa immagine, cioè ax + b = ay + b. Sottraendo b da entrambi i membri resta ax = ay; poiché a ≠ 0 si può dividere per a e si ottiene x = y. Dunque se due numeri hanno la stessa immagine sono lo stesso numero, e di conseguenza due numeri diversi hanno immagini diverse: f è iniettiva.

**Suriettività.** La verifica si traduce sempre nel risolvere un'equazione. Dato y ∈ ℝ ci chiediamo se esiste x ∈ ℝ con f(x) = y, cioè con ax + b = y. L'incognita è x, e isolandola si ottiene x = (1/a)(y − b). Qualunque sia y questa espressione dà un x tale che f(x) = y, quindi f è suriettiva, e quindi biettiva.

## Gli stessi calcoli su ℤ: la suriettività cade
Se a e b sono interi, la stessa espressione definisce una funzione f : ℤ → ℤ. È un'altra funzione, perché cambiano dominio e codominio. Che cosa resta valido? L'iniettività sì: le semplificazioni usate (sottrarre b, dividere per a ≠ 0) sono ancora lecite. La suriettività invece **no**: nella formula x = (1/a)(y − b) la divisione per a può portare fuori dagli interi.

Esempio: f(x) = 2x + 1. Esiste un x intero con f(x) = 2? Dalla formula x = (1/2)(2 − 1) = 1/2, che non è un intero, quindi 2 non è nell'immagine. In realtà un intero moltiplicato per 2 è pari e sommando 1 si ottiene sempre un **numero dispari**: i numeri pari non compaiono mai nell'immagine, e la funzione non è suriettiva. (Precisazione: per a = ±1 la divisione per a non porta fuori dagli interi e la funzione resta biettiva.)

Il prossimo capitolo mostra come si rimedia a questa situazione cambiando dominio e codominio.
