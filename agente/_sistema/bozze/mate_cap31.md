# 31. La Formula del Binomio di Newton
## Una coincidenza da spiegare
Si è visto che i coefficienti binomiali compaiono nel triangolo di Tartaglia. Gli stessi numeri compaiono in una situazione che sembra totalmente diversa: le **potenze di a + b**, dove a e b sono due variabili. Si parte dai casi più semplici: (a + b)⁰ = 1 e (a + b)¹ = a + b. Dalle scuole medie si conosce poi il quadrato del binomio, (a + b)² = a² + 2ab + b², e il cubo, (a + b)³ = a³ + 3a²b + 3ab² + b³. Si guardano soltanto i coefficienti numerici: 1; 1, 1; 1, 2, 1; 1, 3, 3, 1. Sono le prime righe del triangolo.

Per la quarta potenza si può fare il quadrato del quadrato, oppure, più rapidamente, moltiplicare il cubo ancora una volta per a + b e usare la proprietà distributiva: (a + b)⁴ = (a³ + 3a²b + 3ab² + b³)(a + b). Si moltiplica tutto per a e tutto per b, si mettono in colonna i termini con le stesse potenze e si somma:

(a + b)⁴ = a⁴ + 4a³b + 6a²b² + 4ab³ + b⁴.

I coefficienti sono 1, 4, 6, 4, 1: ancora una riga del triangolo. Come sottolineato a lezione, controllare un numero finito di casi non è mai una dimostrazione: potrebbe essere una coincidenza. Per dimostrare la cosa in generale serve un argomento che valga per ogni n.

## L'enunciato
**Formula del binomio.** Per ogni n ≥ 0,
(a + b)^{n} = Σ_{k=0}^{n} (n su k) a^{n−k} b^{k}.

Scritta per esteso: (a + b)^{n} = a^{n} + (n su 1) a^{n−1} b + (n su 2) a^{n−2} b² + … + (n su n − 1) a b^{n−1} + b^{n}. La tradizione la attribuisce a Newton, ma, come detto a lezione, lui aveva studiato una cosa più generale: questo è un caso particolare molto semplice.

(In parole povere: Σ è una scorciatoia per dire «somma tutti questi termini, al variare di k».)

Il simbolo Σ (sigma maiuscola greca) indica una **sommatoria**: si fa la somma del termine generico al variare dell'indice. Qui l'indice è k, che va da 0 a n, e il termine generico è (n su k) a^{n−k} b^{k}. È un modo compatto di scrivere la lunga somma senza puntini di sospensione, e funziona quando si riesce a descrivere facilmente il termine generico. Come si vede, in ogni termine un esponente scende di uno e l'altro sale di uno, in modo che il grado totale sia sempre n.

(In parole povere: la formula dice che, sviluppando (a + b)^{n}, il coefficiente di a^{n−k} b^{k} è proprio (n su k), cioè il numero di modi di scegliere k oggetti fra n.)

## Perché vale: contare le scelte
Il legame fra un calcolo algebrico e il conteggio dei sottoinsiemi è questo. Fare la potenza n-esima vuol dire moltiplicare a + b per sé stesso n volte:
(a + b)^{n} = (a + b)(a + b) ⋯ (a + b)  con n fattori.

Per svolgere il prodotto di somme si prende, in tutti i modi possibili, **un addendo per ciascun fattore** (a oppure b), si moltiplicano gli addendi scelti e si sommano tutti i risultati. Per esempio, per n = 4: a⁴ si ottiene scegliendo a in tutti i fattori; il termine a³b si ottiene scegliendo b in un fattore e a nei tre rimanenti, e ci sono quattro modi (b nel primo, nel secondo, nel terzo o nel quarto fattore).

Si fissa k e ci si chiede quante volte compare il termine a^{n−k} b^{k}. Compare tutte le volte che si sceglie a in n − k fattori (e b nei restanti k). Con n = 2, il termine ab compare due volte: a dal primo e b dal secondo fattore, oppure b dal primo e a dal secondo. Con n = 3, il termine a²b compare tre volte: aab, aba, baa. In generale, i modi per scegliere gli n − k fattori da cui prendere a, fra gli n fattori disponibili, sono (n su n − k), che per la simmetria (cap. 29) è uguale a (n su k). Come sottolineato a lezione, è lo stesso numero se si decide di scegliere i k fattori da cui prendere b, perché scegliere quali fattori usare per a o per b è un'operazione complementare. Quindi il coefficiente di a^{n−k} b^{k} è (n su k). ∎

## La somma dei coefficienti: 2^{n}
Si sommano tutti i coefficienti binomiali di una stessa riga del triangolo: per n = 0, 1, 2, 3, 4, 5 si ottengono 1, 2, 4, 8, 16, 32. Sono le **potenze di 2**. Non è una sorpresa: per la formula di Stiefel ogni numero della riga n compare due volte nella somma dei numeri della riga n + 1 (una come «numero sopra a sinistra» e una come «numero sopra a destra»), quindi la somma raddoppia a ogni livello (i due 1 ai bordi della riga n + 1 valgono ciascuno come una copia di un 1 della riga n).

Un altro modo di dirlo è usare la formula del binomio, che è un'identità valida per qualunque a e b: ponendo a = b = 1 si ottiene (1 + 1)^{n} = 2^{n} = Σ_{k=0}^{n} (n su k).

(In parole povere: la somma di tutti i coefficienti binomiali di una riga è 2^{n}. Si può anche leggere così: poiché (n su k) conta i sottoinsiemi di k elementi, sommando per k da 0 a n si contano tutti i sottoinsiemi di un insieme di n elementi, che sono quindi 2^{n}.)
