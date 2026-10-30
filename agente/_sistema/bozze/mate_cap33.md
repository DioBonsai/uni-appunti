# 33. I Cicli e i Cicli Disgiunti
## Seguire i numeri con le frecce
Per capire meglio la «dinamica» di una permutazione si disegna un diagramma: si scrivono i numeri da 1 a 7 sparsi sulla lavagna (non in fila, perché così la struttura si vede meglio) e per la permutazione
**π**: prima riga 1 2 3 4 5 6 7; seconda riga 3 5 7 6 4 2 1 (una nuova permutazione, diversa dalla π del capitolo precedente)
si traccia una freccia da ogni numero alla sua immagine: 1 → 3, 2 → 5, 3 → 7, 4 → 6, 5 → 4, 6 → 2, 7 → 1.

Il fatto che π sia biettiva si legge nel diagramma: **non ci sono due frecce che arrivano nello stesso punto** (iniettività) e **ogni elemento è raggiunto da una freccia** (suriettività).

Se ora si parte da un numero e si «cammina» seguendo le frecce, si scopre una struttura: partendo da 1 si va in 3, poi in 7, poi si torna in 1, formando un giro chiuso; partendo da 2 si va in 5, poi in 4, poi in 6, poi di nuovo in 2. Il diagramma contiene quindi **due circuiti**: uno formato da 1, 3, 7 e uno formato da 2, 5, 4, 6, e i due circuiti **non si toccano mai**.

Ci si chiede subito se sia una particolarità di questa permutazione o se tutte le permutazioni abbiano una struttura così.

## Scomporre π in due permutazioni più semplici
Si isola ciascun circuito in una permutazione a parte. Sia **C₁** la permutazione che segue il primo circuito e lascia fermi tutti gli altri numeri: 1 → 3, 3 → 7, 7 → 1, con 2, 4, 5, 6 fissi. Sia **C₂** quella che segue il secondo: 2 → 5, 5 → 4, 4 → 6, 6 → 2, con 1, 3, 7 fissi.

Componendole (si applica prima C₂ e poi C₁, o viceversa: l'ordine, come si vedrà, non conta) si trova esattamente la seconda riga 3 5 7 6 4 2 1, cioè **π = C₁ ∘ C₂**. Come esercizio si lascia da verificare che anche C₂ ∘ C₁ dà π.

**In parole povere:** invece di descrivere π tutta insieme, la si spezza in due «giri» indipendenti, ciascuno dei quali sposta solo i suoi numeri.

Come sottolineato a lezione, in generale la composizione non è commutativa, ma questo non vuol dire che non lo sia **mai**: vuol dire che esistono esempi in cui non vale. Qui, per C₁ e C₂, vale.

## La definizione di ciclo
**Definizione.** Una permutazione C ∈ S_{n} si chiama **ciclo** se esiste un sottoinsieme {i₁, i₂, …, i_{ℓ}} ⊆ I_{n} tale che
- C(i₁) = i₂, C(i₂) = i₃, …, C(i_{ℓ−1}) = i_{ℓ}, C(i_{ℓ}) = i₁;
- C(k) = k **per ogni k che non appartiene a quel sottoinsieme**.

(In parole povere: un ciclo manda ogni elemento nel successivo, l'ultimo nel primo, e lascia fermi tutti gli altri.)

Il numero ℓ degli elementi mossi si chiama **lunghezza** del ciclo: si parla di 2-ciclo, di 3-ciclo e in generale di ℓ-ciclo. Un 2-ciclo è uno **scambio** (cap. 32). Nell'esempio, C₁ è un ciclo di lunghezza 3 e C₂ un ciclo di lunghezza 4.

## La notazione compatta
Un ciclo si può scrivere in modo molto più compatto che con la tabella a due righe: basta elencare **gli elementi mossi, nell'ordine in cui vengono mandati l'uno nell'altro**. Si scrive, senza virgole (solo spazi):
- C₁ = (1 3 7);
- C₂ = (2 5 4 6);
- in generale (i₁ i₂ … i_{ℓ}).

Il simbolo vuol dire che i₁ va in i₂, i₂ va in i₃, …, e l'ultimo torna in i₁, mentre tutti gli altri elementi restano fermi.

**Non è una scrittura unica.** La struttura è circolare, quindi si può partire da qualunque punto: (1 3 7), (3 7 1) e (7 1 3) rappresentano lo stesso ciclo. L'unica cosa importante è fare tutto il giro e **mantenere la relazione fra un elemento e il suo successivo**. Un ciclo di lunghezza ℓ si può quindi scrivere in **ℓ modi diversi**, uno per ogni possibile punto di partenza.

**L'inverso di un ciclo.** Invertire una permutazione vuol dire scambiare immagine e controimmagine, cioè nel diagramma **invertire le frecce**. Per un ciclo basta scrivere gli stessi numeri **in ordine inverso**: l'inverso di (2 5 4 6) è (6 4 5 2), che si può anche scrivere (5 2 6 4) o in altri modi equivalenti.

## Cicli disgiunti
Si prendano due cicli C₁ e C₂ in S_{n}. A ciascuno corrisponde l'insieme degli elementi che muove: {i₁, …, i_{ℓ}} per C₁ e {j₁, …, j_{k}} per C₂ (ognuno con la sua lunghezza, che può essere diversa).

**Definizione.** I due cicli C₁ e C₂ si dicono **disgiunti** se i due insiemi di elementi mossi **non hanno elementi in comune**: {i₁, …, i_{ℓ}} ∩ {j₁, …, j_{k}} = ∅.

(In parole povere: due cicli sono disgiunti se muovono numeri completamente diversi, cioè se nel diagramma i due giri non si incrociano mai.)

Il concetto riguarda **due** cicli messi a confronto: non ha senso dire che un ciclo da solo è «disgiunto».

**Esempi, con n = 9.**
- C₁ = (3 2 6 9 1 4) e C₂ = (5 7 6 8) **non sono disgiunti**, perché il 6 compare in entrambi: i due insiemi hanno un elemento in comune, e nel diagramma i due circuiti si incrociano.
- C₁ = (3 6 2 9) e C₂ = (1 4 7 5) sono **disgiunti**: nessun numero compare in entrambi.

## Due cicli disgiunti commutano
**Proposizione.** Siano C₁ e C₂ due cicli disgiunti in S_{n}. Allora **C₁ ∘ C₂ = C₂ ∘ C₁**.

**Idea.** È intuitivamente chiara: se sul tavolo ci sono degli oggetti, un ciclo ne sposta alcuni (per esempio quelli a destra) e l'altro ne sposta altri (quelli a sinistra), senza elementi in comune: muovere prima quelli di destra e poi quelli di sinistra dà lo stesso effetto del contrario, perché si muovono cose diverse.

**Dimostrazione.** Si scrivono i due cicli con la notazione compatta: C₁ = (i₁ … i_{ℓ}) e C₂ = (j₁ … j_{k}), con i due insiemi disgiunti. Si vuole mostrare che le due composizioni, che sono funzioni da I_{n} a I_{n}, sono uguali: hanno lo stesso dominio e lo stesso codominio, quindi basta controllare che mandino ogni elemento nello stesso elemento. Un elemento di I_{n} può essere di tre tipi: uno degli i_{r}, uno dei j_{s}, oppure un elemento t che non compare in nessuno dei due.
- **Elemento i_{r}.** C₂ lo lascia fermo (non è di tipo j) e C₁ lo manda nel successivo i_{r+1} (con i_{ℓ+1} = i₁). Nell'altro ordine, C₁ lo manda subito in i_{r+1}, che C₂ lascia fermo. Stesso risultato: i_{r+1}.
- **Elemento j_{s}.** Analogamente, in tutti e due gli ordini finisce in j_{s+1} (con j_{k+1} = j₁).
- **Elemento t.** Nessuno dei due cicli lo muove, quindi resta t in entrambi i casi.

Le due funzioni hanno la stessa immagine per ogni elemento, quindi sono uguali. ∎

**In parole povere:** i cicli disgiunti agiscono su numeri diversi, quindi non si «intralciano» e l'ordine in cui li si applica non conta.

A lezione ci si è fermati qui: ci si chiede ora se **ogni** permutazione si possa scrivere come composizione di cicli disgiunti, domanda a cui si risponde nella lezione successiva (cap. 34).
