# 7. Coordinate Polari e Forma Esponenziale dei Numeri Complessi
## Dalle coordinate cartesiane alle coordinate polari
Nel capitolo precedente abbiamo identificato ogni numero complesso z = a + bi con il punto P = (a, b) del piano di Argand-Gauss. Per un punto diverso dall'origine O esiste però un secondo modo, del tutto equivalente, di indicarne la posizione: invece di dire "di quanto ci si sposta in orizzontale e in verticale", si dice **a che distanza dall'origine** si trova il punto e **in quale direzione**. Si ottengono così le **coordinate polari** (r, θ), definite da:
- r è la lunghezza del segmento OP, cioè la distanza di P dall'origine O;
- θ (la lettera greca *theta*) è l'angolo, misurato in radianti, che il segmento OP forma con il semiasse positivo delle ascisse, contando le rotazioni in senso antiorario.

Il legame con le coordinate cartesiane passa per le funzioni seno e coseno, che si interpretano sulla circonferenza di raggio 1: se un punto sulla circonferenza forma un angolo θ con il semiasse positivo delle x, il suo coseno è l'ascissa e il suo seno è l'ordinata. Un punto a distanza r dall'origine ha quindi coordinate r volte più grandi:
- dalle polari alle cartesiane: a = r cos θ, b = r sen θ;
- dalle cartesiane alle polari: r = √(a^{2} + b^{2}), cos θ = a / r, sen θ = b / r.

## Modulo e argomento
Applicando queste formule a un numero complesso z = a + bi ≠ 0 lo si può scrivere in coordinate polari come:

z = r (cos θ + i sen θ)

Il numero r = |z| è il **modulo** di z, già incontrato come distanza dall'origine (e per z = 0 vale |z| = 0). L'angolo θ si chiama **argomento** (o *fase*) di z e si indica con Arg(z). Due precisazioni importanti:
- l'argomento **non è unico**: aggiungendo o togliendo un giro completo si torna nello stesso punto, quindi θ è definito a meno di multipli di 2π. Per fissare una scelta si prende di solito θ ∈ [0, 2π), oppure θ ∈ (−π, π]: l'importante è dichiarare quale convenzione si usa;
- per z = 0 l'argomento **non è definito**, perché l'origine non ha una direzione: ogni angolo va bene.

**Trabocchetto d'Esame: ricavare θ da a e b.** Non basta calcolare arctan(b/a). Questa funzione restituisce solo angoli tra −π/2 e π/2, quindi bisogna distinguere i casi (qui con la convenzione θ ∈ [0, 2π)):
- se a > 0 e b ≥ 0 (primo quadrante e semiasse reale positivo): θ = arctan(b/a);
- se a > 0 e b < 0 (quarto quadrante): θ = arctan(b/a) + 2π, perché arctan(b/a) è negativo;
- se a < 0 (secondo e terzo quadrante): θ = arctan(b/a) + π;
- se a = 0 il rapporto b/a non esiste: θ = π/2 per b > 0 e θ = 3π/2 per b < 0.

In caso di dubbio conviene sempre controllare con un disegno in quale quadrante si trova il punto. Per esempio, per z = −1 + i si ha r = √2 e arctan(1/(−1)) = −π/4; poiché a < 0 si aggiunge π e si ottiene θ = 3π/4, coerente con il fatto che il punto sta nel secondo quadrante.

## La notazione esponenziale
La scrittura in coordinate polari si può rendere molto più compatta introducendo la notazione:

e^{iθ} = cos θ + i sen θ

Con questa scelta ogni numero complesso z ≠ 0 diventa:

z = r e^{iθ}

che si chiama **rappresentazione polare** (o *esponenziale*) di z. Il motivo profondo per cui compare proprio il numero e riguarda lo sviluppo in serie di potenze delle funzioni e^{x}, sen x e cos x, e va oltre gli obiettivi del corso: per il momento basta considerare e^{iθ} come un simbolo che *significa* cos θ + i sen θ. È un simbolo ben scelto, perché si comporta come un vero esponenziale (lo dimostriamo nel prossimo capitolo).

I numeri e^{iθ}, al variare di θ, sono esattamente i punti della **circonferenza unitaria**, cioè quelli con modulo 1. Due valori particolari sono molto noti:
- per θ = π si ottiene e^{iπ} = cos π + i sen π = −1, da cui la celebre **identità di Eulero** e^{iπ} + 1 = 0;
- per θ = 2π si ottiene e^{2πi} = 1: dopo un giro completo si torna al punto di partenza.

## Due esempi
**Dalla forma cartesiana a quella polare.** Vogliamo scrivere z = −5 in forma polare. Il punto sta sul semiasse reale negativo, a distanza 5 dall'origine, quindi r = 5, e l'angolo formato con il semiasse positivo è mezzo giro, θ = π. Dunque −5 = 5 e^{iπ}.

**Dalla forma polare a quella cartesiana.** Dato z = 2 e^{iπ/4}, si ha:

z = 2 (cos(π/4) + i sen(π/4)) = 2 (√2/2 + i √2/2) = √2 + i √2

## Quando due forme polari rappresentano lo stesso numero
Poiché l'argomento è definito solo a meno di giri completi, due scritture r_{1} e^{iθ_{1}} e r_{2} e^{iθ_{2}} rappresentano lo stesso numero complesso se e solo se valgono entrambe le condizioni:
- r_{1} = r_{2}, cioè hanno lo stesso modulo;
- θ_{2} = θ_{1} + 2kπ per qualche k ∈ ℤ, cioè gli angoli differiscono per un multiplo di 2π.

È un dettaglio facile da trascurare, ma sarà indispensabile quando risolveremo le equazioni con le radici n-esime: due coppie (r, θ) diverse possono indicare lo stesso punto, e l'equazione va trattata tenendo conto di tutte. Nel prossimo capitolo vedremo però il vantaggio principale della rappresentazione polare: rende molto semplice il prodotto di due numeri complessi.
