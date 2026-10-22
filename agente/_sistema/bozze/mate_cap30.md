# 30. La Formula di Stiefel e il Triangolo di Tartaglia
## L'enunciato
**Formula di Stiefel.** Per n ≥ 1 e 1 ≤ k ≤ n vale
(n − 1 su k − 1) + (n − 1 su k) = (n su k).

(In parole povere: un coefficiente binomiale si ottiene sommando due coefficienti della «riga» di sopra: quello sulla stessa posizione e quello subito prima.)

Come sottolineato a lezione, la formula dice che i coefficienti binomiali soddisfano una relazione **ricorsiva**: se si conoscono tutti i coefficienti con n − 1 sopra, si ricavano subito quelli con n. Un esempio numerico: (11 su 4) + (11 su 5) = (12 su 5), cioè 330 + 462 = 792.

## Dimostrazione con le formule
Si scrive il lato sinistro con i fattoriali. Il primo addendo è (n − 1)!/((k − 1)! (n − k)!), perché (n − 1) − (k − 1) = n − k; il secondo è (n − 1)!/(k! (n − 1 − k)!). Per sommare due frazioni si cerca un denominatore comune: si può prendere k! (n − k)!, perché k! è un multiplo di (k − 1)! (si ha k! = k · (k − 1)!) e (n − k)! è un multiplo di (n − 1 − k)! (si ha (n − k)! = (n − k) · (n − 1 − k)!). I numeratori vanno quindi moltiplicati per i fattori mancanti:

(n − 1)!/((k − 1)!(n − k)!) + (n − 1)!/(k!(n − 1 − k)!) = [ k · (n − 1)! + (n − k) · (n − 1)! ] / (k! (n − k)!).

Si raccoglie (n − 1)!: il fattore k + (n − k) = n, e n · (n − 1)! = n!. Resta n!/(k!(n − k)!) = (n su k). Questo calcolo vale per 1 ≤ k ≤ n − 1; nel caso k = n il secondo addendo (n − 1 su n) non ha senso con i fattoriali, ma si intende uguale a 0 (un insieme di n − 1 elementi non ha sottoinsiemi di n elementi), e la formula si riduce a (n − 1 su n − 1) = 1 = (n su n).

Come sottolineato a lezione, è un calcolo e basta: non si capisce perché la formula valga.

## Dimostrazione combinatoria
I coefficienti contano sottoinsiemi, e conviene ragionare così. Sia A un insieme con |A| = n, e si fissa un suo elemento x. Sia B = C_{A}({x}) = A ∖ {x} l'insieme di tutti gli altri elementi: |B| = n − 1. Il lato destro, (n su k), conta i sottoinsiemi di A con k elementi; i due addendi di sinistra contano sottoinsiemi di B, che ha un elemento in meno. Per collegarli si dividono i sottoinsiemi di A (con k elementi) in **due tipi**:
1. quelli che **contengono** x;
2. quelli che **non contengono** x.

![I sottoinsiemi di A con k elementi si dividono in due tipi, secondo che contengano x oppure no.](figure/mate/stiefel_tipi.png|10)

I due tipi non hanno sottoinsiemi in comune (un sottoinsieme o contiene x o non lo contiene) e insieme esauriscono tutti i sottoinsiemi di A (non c'è una terza possibilità). Quindi i sottoinsiemi di A con k elementi sono quelli del primo tipo più quelli del secondo, e per contarli si sommano i due numeri: è il caso più facile del principio di inclusione-esclusione, quando l'intersezione è vuota (cap. 21).

**Primo tipo.** Sia S un sottoinsieme con k elementi che contiene x. Togliendo x si ottiene un sottoinsieme S′ di B con k − 1 elementi. Viceversa, se si parte da un sottoinsieme S′ di B con k − 1 elementi e si aggiunge x (che non era in B), si ottiene un sottoinsieme di A con k elementi che contiene x. Le due operazioni sono una l'inversa dell'altra, quindi i sottoinsiemi del primo tipo sono tanti quanti i sottoinsiemi di k − 1 elementi di B, cioè (n − 1 su k − 1).

**Secondo tipo.** Se x non sta in S, allora S è un sottoinsieme di B con k elementi. I sottoinsiemi del secondo tipo sono quindi tutti e soli i sottoinsiemi di B con k elementi: sono (n − 1 su k).

Sommando, (n su k) = (n − 1 su k − 1) + (n − 1 su k). ∎

(In parole povere: per formare una squadra di k persone da n, si guarda una persona in particolare, x: o è in squadra, e allora si scelgono gli altri k − 1 dalle n − 1 rimaste; o non lo è, e allora tutti e k vengono scelti dalle n − 1 rimaste.)

## Il triangolo di Tartaglia
Grazie alla formula di Stiefel si possono calcolare i coefficienti binomiali in modo ricorsivo e metterli in tabella, almeno per valori non troppo grandi. Si dispongono su righe, una per ogni valore di n, e le posizioni lungo la riga sono i valori di k (da 0 a n). Per n = 0 c'è solo (0 su 0) = 1; per n = 1 ci sono (1 su 0) e (1 su 1), entrambi uguali a 1. In generale ogni riga comincia e finisce con 1 (per k = 0 e per k = n, cap. 29) e, per la simmetria, è uguale letta da sinistra a destra e da destra a sinistra. Ogni numero interno è la somma dei due numeri che ha sopra, per la formula di Stiefel.

![Il triangolo di Tartaglia fino a n = 6; in verde due numeri che sommati danno quello sotto.](figure/mate/tartaglia.png|11)

Così si ottengono le righe 1; 1 1; 1 2 1; 1 3 3 1; 1 4 6 4 1; 1 5 10 10 5 1; 1 6 15 20 15 6 1, e si può continuare quanto si vuole. Come sottolineato a lezione, il nome dipende da dove ci si trova: oltre le Alpi si chiama **triangolo di Pascal**, in Italia **triangolo di Tartaglia**; Tartaglia è un matematico italiano, e il nome è in realtà un soprannome che gli è rimasto. Permette di calcolare rapidamente i coefficienti se n e k non sono troppo grandi.

Il capitolo successivo mostra che questi stessi numeri compaiono anche quando si calcolano le potenze di una somma.
