# Audit fattuale Algebra lineare, capitoli 1-6

Data: 2026-10-08. Sola lettura (Word non modificato). Metodo: confronto riga per riga con dispense_MDAG.md (cap. 1-3), L1_appunti_30set.md, L2_appunti_5ott.md, L1_nota.md; trascrizione audio L1 (`trascrizioni/small_scartate/algebra_L1.small.txt`, fiducia minima) solo come controllo secondario; calcoli rifatti con SymPy.

**Numerazione dei paragrafi:** indice 1-based di `Document.paragraphs` (paragrafi vuoti inclusi), cioè il primo numero stampato dallo script.

## Riepilogo

| Gravità | N. problemi |
|---|---|
| alta | 0 |
| media | 5 |
| bassa | 8 |
| **Totale** | **13** |

## Capitoli controllati

- Cap. 1 Introduzione (par. 1-12): 4 problemi (1 media, 3 basse).
- Cap. 2 Insiemi numerici e campo (par. 13-45): 5 problemi (2 media, 3 basse; uno dei media tocca anche il par. 49 del cap. 3).
- Cap. 3 Numeri complessi, definizione (par. 47-65): 2 problemi (1 media, 1 bassa).
- Cap. 4 Proprietà e campo ℂ (par. 67-89): 1 problema (media), più l'incoerenza di etichetta del par. 80 trattata nel problema del par. 36.
- Cap. 5 Coniugato, modulo, inverso (par. 91-123): nessun problema. Verificati con SymPy: z·z̄ = a²+b², z⁻¹ = z̄/|z|², inverso di 2+5i = 2/29 − (5/29)i (|z|² = 29, z·z⁻¹ = 1), tutte le definizioni di Re, Im, coniugio, modulo.
- Cap. 6 Piano di Argand-Gauss (par. 125-140): 1 problema (bassa). Corretti: identificazione z↔(a,b), parallelogramma, riflessione rispetto all'asse reale, modulo come distanza, (a,b)·(c,d) = (ac−bd, ad+bc), «moduli si moltiplicano, angoli si sommano». Il nome «Argand-Gauss» non compare nelle fonti (che dicono «piano complesso») ma è la denominazione italiana corretta: non è un errore.

Nota: i superscript (x², i², a⁻¹ ecc.) sono formattati come apice nel Word e nell'estrazione testo appaiono senza apice (es. «x2», «i2», «a−1»): non sono errori.

Verificato corretto, senza problemi: definizioni di ℕ, ℤ, ℚ, ℝ (classi di equivalenza di successioni di Cauchy), √2 ∉ ℚ, esempio 2^π con esponenti razionali, contenuto delle 9 proprietà, ℕ e ℤ non campi, ℚ ℝ ℂ campi, mancanza di ordine in ℂ (argomento i² = −1 e quadrati positivi), somma e prodotto complessi, ℝ ⊂ ℂ, immaginario puro. L'affermazione del par. 16 su ℕ (definizione complessa, teoria degli insiemi e classi di equivalenza) è coerente con la lezione audio (ℕ come classi di insiemi finiti modulo biiezione), anche se le dispense dicono solo «concetto primitivo»: non segnalata.

---

## Problemi

### [GRAVITÀ: media] Capitolo 3, paragrafo 56
**Testo attuale:** «chiamati rispettivamente parte reale e coefficiente della parte immaginaria»
**Problema:** Nelle fonti b è la parte immaginaria Im(z) (numero reale, senza i); «coefficiente della parte immaginaria» suggerisce che la parte immaginaria sia bi, in contraddizione con il cap. 5 (par. 95-96) e con l'avvertenza di L2.
**Correzione proposta:** «chiamati rispettivamente parte reale (a = Re(z)) e parte immaginaria (b = Im(z)); la parte immaginaria è il numero reale b, non bi».
**Fonte/verifica:** dispense_MDAG.md, 2.C («a e b sono detti rispettivamente la parte reale e la parte immaginaria di z. Scriviamo a = Re(z) e b = Im(z)»); L2_appunti_5ott.md, Def. Re/Im («Im(z) ∈ ℝ», «NON 3i»).

### [GRAVITÀ: media] Capitolo 2, paragrafo 41 (e struttura dei par. 26-37 e 70-81)
**Testo attuale:** «mancano sia gli opposti (proprietà 4) sia gli inversi.»
**Problema:** Nel Word le proprietà non hanno numeri 1-9: la numerazione automatica numera solo le intestazioni («1. Proprietà della Somma», «2. Proprietà del Prodotto», «3. Proprietà di Anello/Legame») e le singole proprietà sono pallini; «proprietà 4» non ha quindi riferimento visibile. L'ordine usato (somma 1-4, prodotto 5-8, distributiva 9) coincide con L1 ma non con dispense/L2 (neutro, commutativa, associativa, opposto, ...): solo 4, 8, 9 coincidono nei due ordini. Gli inversi sono citati senza numero.
**Correzione proposta:** numerare esplicitamente 1-9 nel testo di entrambi i capitoli (ordine L1: 1 comm. +, 2 assoc. +, 3 neutro 0, 4 opposto, 5 comm. ·, 6 assoc. ·, 7 neutro 1, 8 inverso, 9 distributiva) e scrivere «ℕ NON è un campo: mancano gli opposti (proprietà 4) e gli inversi (proprietà 8)». Aggiungere: «Nelle dispense l'ordine è diverso (0, comm., assoc., opposto, 1, comm., assoc., inverso, distributiva); opposto, inverso e distributiva restano 4, 8, 9».
**Fonte/verifica:** L1_appunti_30set.md, «Proprietà di + e ·» (1-9); dispense_MDAG.md, Prop. 1.5 e Prop. 2.2; L2_appunti_5ott.md, Proposizione; ispezione di numbering.xml del docx (numId 15 e 19: livello 0 decimale, livello 1 pallino).

### [GRAVITÀ: media] Capitolo 4, paragrafo 89
**Testo attuale:** «Gli unici confronti ammessi tra numeri complessi riguardano la loro eventuale uguaglianza (z1 = z2) o diversità (z1 ≠ z2).»
**Problema:** Troppo forte: non si possono ordinare i numeri complessi, ma si possono confrontare i loro moduli |z1| < |z2| e le loro parti reale/immaginaria, che sono numeri reali.
**Correzione proposta:** «Tra numeri complessi non ha senso scrivere z1 > z2; si possono invece confrontare per uguaglianza o diversità (z1 = z2, z1 ≠ z2), oppure confrontare grandezze reali associate, come |z1| < |z2| o Re(z1) < Re(z2).»
**Fonte/verifica:** dispense_MDAG.md, 2.B («C non è ordinato: non esiste una nozione di maggiore e minore fra numeri complessi»); il modulo è un numero reale (2.C), quindi ordinabile.

### [GRAVITÀ: media] Capitolo 1, paragrafo 11
**Testo attuale:** «i parametri o "pesi" appresi dal sistema durante l'addestramento non sono altro che trasformazioni e mappe lineari.»
**Problema:** Falso alla lettera: i pesi sono i coefficienti (matrici) di mappe lineari, ma una rete neurale contiene anche funzioni di attivazione non lineari e nel complesso non è una mappa lineare. Inoltre «ChatGPT» e «veicoli autonomi» non sono negli appunti manoscritti L1 (compaiono solo nell'audio).
**Correzione proposta:** «i parametri o "pesi" appresi durante l'addestramento sono i coefficienti di mappe lineari, alternate a funzioni non lineari; l'algebra lineare è quindi una componente fondamentale di questi modelli.»
**Fonte/verifica:** L1_appunti_30set.md («probabilmente da mappe lineari», nessun cenno a reti neurali); trascrizione audio L1 [12:16] («utilizza trasformazioni lineari in maniera fondamentale», detto in modo discorsivo); conoscenza standard sulle reti neurali.

### [GRAVITÀ: media] Capitolo 2, paragrafi 15 (e 49 del cap. 3)
**Testo attuale:** «ciascun passaggio nasce dall'esigenza algebrica di risolvere un problema o un'operatore non consentito nell'insieme precedente» (par. 15); «ogni ampliamento nasce dall'esigenza algebrica di risolvere problemi ed equazioni che non trovano soluzione nell'insieme precedente» (par. 49).
**Problema:** Non vale per ℚ → ℝ: i reali si costruiscono per completezza (successioni di Cauchy che non convergono in ℚ, i «buchi»), non per risolvere equazioni; ℝ contiene numeri non algebrici (π, e). È in tensione con i par. 20-21 dello stesso capitolo.
**Correzione proposta:** par. 15: «ℤ nasce per poter sottrarre, ℚ per poter dividere, ℝ per colmare i buchi di ℚ (completezza) e ℂ per risolvere equazioni come x² + 1 = 0». Par. 49: «Come ℤ e ℚ nascono da esigenze algebriche (sottrazione, divisione) e ℝ da un'esigenza di completezza (i "buchi" di ℚ, per cui ad esempio x² = 2 diventa risolvibile), ℂ risponde alla necessità di risolvere equazioni prive di soluzioni reali».
**Fonte/verifica:** dispense_MDAG.md, 1.B (ℝ completamento di ℚ, «tappato tutti i buchi», «ℝ è completo»); 2.A («ampliamento ... per ottenere migliori proprietà algebriche»); L1_appunti_30set.md.

### [GRAVITÀ: bassa] Capitolo 2, paragrafo 36 (e capitolo 4, paragrafo 80)
**Testo attuale:** «Proprietà di Anello/Legame:» (cap. 2) contro «Proprietà Distributiva:» (cap. 4)
**Problema:** «di Anello» è un'etichetta impropria (un anello richiede più assiomi e qui c'è una sola proprietà), assente nelle fonti, e le due intestazioni della stessa 9ª proprietà sono incoerenti tra i capitoli.
**Correzione proposta:** in entrambi i capitoli «Proprietà distributiva (lega somma e prodotto):».
**Fonte/verifica:** dispense_MDAG.md, Prop. 1.5 punto 9 e Def. 5.3 punto 3; L1_appunti_30set.md, proprietà 9 («+ e ·) distributiva»).

### [GRAVITÀ: bassa] Capitolo 2, paragrafo 45
**Testo attuale:** «sarà quasi sempre ℝ (o ℂ per la parte sui numeri complessi)»
**Problema:** Il campo degli scalari è K = ℝ oppure K = ℂ in generale (spazi vettoriali complessi, autovalori), non solo nella «parte sui numeri complessi»; per definizione K può essere qualsiasi campo.
**Correzione proposta:** «sarà generalmente K = ℝ oppure K = ℂ (la definizione vale però per qualsiasi campo)».
**Fonte/verifica:** dispense_MDAG.md, Def. 5.4 («generalmente o il campo K = R ... o K = C ... per la definizione può essere qualsiasi campo»).

### [GRAVITÀ: bassa] Capitolo 2, paragrafo 20
**Testo attuale:** «già nell'antica Grecia con la scuola pitagorica si scoprì che la diagonale di un quadrato di lato 1 ha lunghezza pari a √2.»
**Problema:** Presentato come fatto storico certo; nella lezione è raccontato come «leggenda», e non è né nelle dispense né negli appunti scritti.
**Correzione proposta:** «secondo la tradizione, nell'antica Grecia un membro della scuola pitagorica si accorse che la diagonale di un quadrato di lato 1, lunga √2, non è commensurabile con il lato.»
**Fonte/verifica:** trascrizione audio L1 [34:06] («una leggenda, uno studente di questa scuola pitagorica»); dispense_MDAG.md Prop. 1.4 (solo la dimostrazione per assurdo, nessuna storia).

### [GRAVITÀ: bassa] Capitolo 1, paragrafo 9
**Testo attuale:** «il processo di elaborazione dei dati consiste prevalentemente nell'applicazione di mappe lineari.» (e «costituisce la struttura portante dell'informatica»)
**Problema:** Più forte degli appunti («probabilmente composta da mappe lineari», «fondamentale») e della lezione («soprattutto»); l'elaborazione dati in generale non è prevalentemente lineare.
**Correzione proposta:** «L'algebra lineare è fondamentale in informatica: input e output sono array, cioè vettori, e molte elaborazioni sono composte da mappe lineari.»
**Fonte/verifica:** L1_appunti_30set.md, «Oggetti fondamentali» («è composta probabilmente da mappe lineari»); L1_nota.md («fondamentale in informatica»).

### [GRAVITÀ: bassa] Capitolo 1, paragrafo 12
**Testo attuale:** «L'operazione necessaria per "ripulire" il segnale e recuperare l'informazione corretta si realizza proprio applicando un'opportuna mappa lineare.»
**Problema:** «necessaria»/«proprio» sono assoluti; l'appunto dice che la pulizia avviene tramite una mappa lineare, l'audio che «spesso» coinvolge una mappa lineare.
**Correzione proposta:** «Per "ripulire" il segnale e recuperare l'informazione si usa spesso un'opportuna mappa lineare.»
**Fonte/verifica:** L1_appunti_30set.md, «Segnali»; trascrizione L1 [16:22] («spesso questo coinvolge una mappa lineare»).

### [GRAVITÀ: bassa] Capitolo 1, paragrafo 6
**Testo attuale:** «che ha l'effetto di allungare, accorciare o invertire la direzione del vettore.»
**Problema:** Moltiplicare per un numero negativo inverte il verso, non la direzione (la retta di appartenenza resta la stessa).
**Correzione proposta:** «che ha l'effetto di allungare, accorciare o invertire il verso del vettore.»
**Fonte/verifica:** definizione geometrica standard (λv è parallelo a v); trascrizione L1 [04:08] (2v = freccia lunga il doppio).

### [GRAVITÀ: bassa] Capitolo 3, paragrafo 51
**Testo attuale:** «Come evidenziato a lezione, ... i numeri complessi costituiscono uno strumento indispensabile come passaggio intermedio in ambiti come la fisica e l'ingegneria, permettendo di risolvere problemi il cui risultato finale torna poi a essere una grandezza reale e misurabile.»
**Problema:** Affermazione non presente nelle fonti disponibili (da verificare); «proprietà algebriche superiori» è inoltre una formulazione non fedele (le dispense dicono «migliori»).
**Correzione proposta:** togliere la frase «Come evidenziato a lezione ... misurabile» salvo conferma dall'audio di L2; sostituire «proprietà algebriche superiori» con «proprietà algebriche migliori (ad esempio x² = −1 ha soluzione)».
**Fonte/verifica:** dispense_MDAG.md, 2.A; L2_appunti_5ott.md (nessun cenno); la trascrizione audio di L2 non è presente in `_sistema/trascrizioni`.

### [GRAVITÀ: bassa] Capitolo 6, paragrafo 130 (confronto con cap. 3, paragrafo 58)
**Testo attuale:** «ospita i numeri immaginari puri, corrispondenti ai complessi con parte reale nulla (0 + bi).»
**Problema:** Al par. 58 «immaginario puro» richiede b ≠ 0; qui l'asse immaginario è descritto con b qualsiasi, che include l'origine (0 + 0i), che è anche reale.
**Correzione proposta:** «ospita i numeri della forma bi, con b ∈ ℝ (immaginari puri per b ≠ 0, più l'origine)».
**Fonte/verifica:** dispense_MDAG.md, 2.D («L'asse immaginario consiste di tutti i numeri complessi del tipo bi al variare di b ∈ R»).
