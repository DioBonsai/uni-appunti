# 12. Funzioni sull'Insieme Quoziente e Dipendenza dal Rappresentante
## Il problema
Come visto nel capitolo 9, una relazione di equivalenza R su un insieme A divide A in classi di equivalenza e dà l'**insieme quoziente** Q, i cui elementi sono le classi. Un elemento x ∈ A individua la sua classe, che indichiamo con [x] oppure con x̄ (a volte anche C_{x}): sono modi alternativi di scrivere la stessa cosa, e le notazioni semplici contano, perché scegliere il simbolismo giusto aiuta a capire.

Questa situazione è molto frequente in matematica e porta a una questione delicata, che a lezione è stata indicata come forse il punto concettualmente più difficile del corso. Supponiamo di voler definire una funzione da Q in Q, cioè di associare a ogni classe un'altra classe, e di farlo dicendo "alla classe di x associo la classe di una certa espressione in x".

## Il difetto: molti modi per scrivere la stessa classe
Una classe si può scrivere in tanti modi, uno per ogni suo rappresentante, e nessuno è privilegiato: per esempio, nell'esempio qui sotto [3] = [5] = [7]. Ma una funzione deve assumere **un solo valore ben specificato** su ciascun elemento del dominio. Se la regola usa il rappresentante scelto, il risultato **non deve dipendere dal modo in cui si scrive la classe**: altrimenti, scrivendo la stessa classe in due modi, si otterrebbero due valori diversi e non si avrebbe una funzione.

## Un esempio che non funziona
Sia A = ℕ e dividiamolo in classi mettendo insieme i numeri che in notazione decimale hanno lo stesso numero di cifre: {0, …, 9} (una cifra), {10, …, 99} (due cifre), {100, …, 999} (tre cifre) e così via. Allora [3] = {0, …, 9} e [2026] è l'insieme dei numeri con quattro cifre, da 1000 a 9999. Due numeri sono equivalenti quando si scrivono con lo stesso numero di cifre.

Proviamo a definire F : Q → Q con la regola F([x]) = [2x]: alla classe di 2 associo quella di 4, alla classe di 15 quella di 30, e così via. Questa regola non definisce una funzione. Infatti 3 e 8 hanno una cifra, quindi [3] = [8], ma:
- F([3]) = [6] (una cifra);
- F([8]) = [16] (due cifre).

Dato che [6] ≠ [16], la stessa classe verrebbe mandata in due classi diverse. Il motivo è che 3 ∼ 8 non implica 2·3 ∼ 2·8: raddoppiare non rispetta l'equivalenza.

## Che cosa bisogna verificare
Quando si definisce una funzione su un insieme quoziente tramite i rappresentanti bisogna sempre controllare che la regola sia **ben definita** (termine usuale): se x ∼ y, la regola deve dare lo stesso risultato su x e su y, cioè la classe di arrivo non deve cambiare cambiando rappresentante. Il tema tornerà verso la fine del corso con casi concreti, dove la verifica diventa un vero problema da risolvere.

**Come sottolineato a lezione:** quando una funzione è definita "sulla classe di x" tramite una formula in x, la prima domanda è sempre se il risultato dipende dal rappresentante.
