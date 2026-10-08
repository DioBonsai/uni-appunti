# 8. Prodotto, Inverso e Coniugio in Forma Polare
## L'esponenziale complesso si comporta come un esponenziale
Alla fine del capitolo 6 avevamo osservato che il prodotto in coordinate cartesiane, (a, b) · (c, d) = (ac − bd, ad + bc), produce un risultato il cui legame geometrico con i due fattori resta oscuro. Con la rappresentazione polare il quadro cambia completamente. Il punto di partenza è la proprietà che giustifica la scelta della notazione e^{iθ}.

**Proposizione.** Per ogni coppia di angoli θ_{1} e θ_{2} vale e^{i(θ_{1} + θ_{2})} = e^{iθ_{1}} · e^{iθ_{2}}.

*Dimostrazione.* Si sviluppa il prodotto applicando la definizione di e^{iθ} e la proprietà distributiva, ricordando che i^{2} = −1:
1. e^{iθ_{1}} · e^{iθ_{2}} = (cos θ_{1} + i sen θ_{1}) (cos θ_{2} + i sen θ_{2}), per definizione di e^{iθ};
2. = (cos θ_{1} cos θ_{2} − sen θ_{1} sen θ_{2}) + i (cos θ_{1} sen θ_{2} + sen θ_{1} cos θ_{2}), sviluppando il prodotto e usando i^{2} = −1;
3. = cos(θ_{1} + θ_{2}) + i sen(θ_{1} + θ_{2}), perché le due parentesi sono proprio le formule di addizione di coseno e seno;
4. = e^{i(θ_{1} + θ_{2})}, di nuovo per definizione. ∎

## Il prodotto: i moduli si moltiplicano, gli angoli si sommano
Siano z_{1} = r_{1} e^{iθ_{1}} e z_{2} = r_{2} e^{iθ_{2}}. Grazie alla proposizione precedente il prodotto si calcola in una riga:

z_{1} z_{2} = r_{1} e^{iθ_{1}} · r_{2} e^{iθ_{2}} = (r_{1} r_{2}) e^{i(θ_{1} + θ_{2})}

Leggendo modulo e argomento del risultato si ottengono due regole molto comode:
- |z_{1} z_{2}| = r_{1} r_{2} = |z_{1}| · |z_{2}|, cioè il modulo del prodotto è il prodotto dei moduli;
- Arg(z_{1} z_{2}) = θ_{1} + θ_{2} = Arg(z_{1}) + Arg(z_{2}), cioè l'argomento del prodotto è la somma degli argomenti (sempre a meno di multipli di 2π).

**Significato geometrico.** Moltiplicare z_{1} per z_{2} equivale a **ruotare** z_{1} dell'angolo θ_{2} e a **riscalarne** la lunghezza del fattore r_{2}. È la spiegazione geometrica che cercavamo: la moltiplicazione complessa è una rotazione combinata con un ingrandimento (o una riduzione).

**Esempio.** Calcoliamo (1 + i) · (1 + i). Il numero 1 + i ha modulo √2 e argomento π/4, quindi 1 + i = √2 e^{iπ/4}. Elevando al quadrato:

(1 + i)^{2} = (√2)^{2} e^{iπ/2} = 2 e^{iπ/2} = 2i

Si può controllare con le coordinate cartesiane: (1 + i)^{2} = 1 + 2i + i^{2} = 2i.

## Coniugio e inverso
Per scrivere il coniugato in forma polare partiamo da z = a + bi = r e^{iθ}. Il coniugato z̄ = a − bi ha la stessa parte reale e parte immaginaria opposta: il punto viene riflesso rispetto all'asse reale, quindi mantiene il modulo e cambia segno all'angolo. Lo si verifica direttamente, perché cos(−θ) = cos θ e sen(−θ) = −sen θ:

z̄ = r e^{−iθ} = r cos θ − i r sen θ = a − bi

Nel capitolo 5 avevamo ricavato l'inverso di un numero z ≠ 0 come z^{-1} = z̄ / |z|^{2}. In forma polare il calcolo è immediato:

z^{-1} = z̄ / |z|^{2} = r e^{−iθ} / r^{2} = (1/r) e^{−iθ}

In parole: l'inverso ha **modulo inverso** (1/r) e **argomento opposto** (−θ). Come verifica, il prodotto z · z^{-1} = r · (1/r) · e^{i(θ − θ)} = e^{i·0} = cos 0 + i sen 0 = 1.

Combinando prodotto e inverso si ottiene anche la regola per la divisione, valida per z_{2} ≠ 0: z_{1} / z_{2} = z_{1} · z_{2}^{-1} = (r_{1} / r_{2}) e^{i(θ_{1} − θ_{2})}, cioè si dividono i moduli e si sottraggono gli argomenti.

Resta da vedere cosa succede quando lo stesso numero viene moltiplicato per se stesso più volte: è il tema del prossimo capitolo, che porterà alle potenze e alle radici n-esime.
