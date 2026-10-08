# Audit fattuale: Matematica discreta (Word "Appunti matematica discreta.docx")

**Esito: 12 problemi** (alta: 1, media: 4, bassa: 7). Il numero di paragrafo è quello dello script python-docx (indice dei paragrafi del documento, da 1, inclusi i vuoti).

Capitoli controllati: 1-9 (tutti).
- Cap. 1 (insiemi, vuoto, sottoinsieme, doppia inclusione): 2 problemi (par. 38 media, par. 33 bassa).
- Cap. 2 (∈ vs ⊆, scatole cinesi): 1 problema (par. 60 media).
- Cap. 3 (operazioni, prodotto cartesiano): nessun problema. Distributività (par. 78-82) assente dagli appunti ma corretta.
- Cap. 4 (differenza, complementare, De Morgan, insieme delle parti): 2 problemi (par. 106, 107/150, basse). Dimostrazioni di De Morgan e cardinalità corrette.
- Cap. 5 (Peano, induzione): 3 problemi (par. 170 alta, par. 157 media, par. 189/167 bassa). Le due dimostrazioni per induzione (somma dei quadrati e |P(A)|=2^n) sono corrette; ricalcolate con Python/SymPy.
- Cap. 6 (ricoprimenti, partizioni): 3 problemi (par. 216 media per notazione 𝒫; par. 206-207 e 212 basse).
- Cap. 7 (insiemi numerici, partizioni, quoziente): nessun errore proprio (vedi la nota sulla notazione 𝒫 al Cap. 6, che tocca anche i par. 252, 262).
- Cap. 8 (relazioni): nessun problema. Divisibilità ℕ vs ℤ corretta (1 | -1 e -1 | 1 in ℤ; antisimmetrica in ℕ).
- Cap. 9 (classi di equivalenza, teorema fondamentale, funzioni): 1 problema (par. 358, bassa). Dimostrazione del teorema corretta.

Verifiche Python: somma dei quadrati verificata per n=1..49; identità algebrica del passo induttivo (differenza simbolica = 0); 2n²+7n+6=(n+2)(2n+3); |P(A)|=2^n per n=0..5 (enumerazione); ricoprimento di ℕ con A1,A2,A3 verificato su 0..20000. Gli apici (10^9, 2^n ecc.) sono presenti nel file: non sono errori di estrazione.

---

### [GRAVITÀ: alta] Capitolo 5, paragrafo 170
**Testo attuale:** «ad esempio, una sequenza infinita per i numeri pari seguita da una sequenza isolata per i dispari, da cui non si potrebbe mai raggiungere la seconda partendo da 0»
**Problema:** l'esempio è sbagliato: pari e dispari non formano catene separate rispetto al successore (S(0)=1 è dispari, S(1)=2 è pari), quindi da 0 si raggiungono entrambi; l'esempio non è nelle fonti.
**Correzione proposta:** «ad esempio, ℕ affiancato da una seconda catena infinita "separata" (una copia di ℤ: …, -1', 0', 1', …) i cui elementi non sono raggiungibili partendo da 0 con il successore; tale struttura soddisfa i primi quattro assiomi ma non il quinto.»
**Fonte/verifica:** assenza dell'esempio in L2_appunti_2ott.md (sez. Assiomi di Peano) e L2_scheda.md (§4); controllo logico: S(0)=1 collega pari e dispari.

### [GRAVITÀ: media] Capitolo 5, paragrafo 157
**Testo attuale:** «la scoperta di paradossi logici fondamentali (come il Paradosso di Russell …) fece crollare i tentativi di costruzione diretta e dimostrò la necessità di definire l'aritmetica mediante un sistema formale di assiomi.»
**Problema:** causalità storica falsa: gli assiomi di Peano (1889) precedono il paradosso di Russell (1901); non è nelle fonti.
**Correzione proposta:** «Gli assiomi di Peano (1889) caratterizzano i numeri naturali senza costruirli a partire dagli insiemi: si dà un elemento iniziale 0 e una funzione successore con proprietà precise. (Il paradosso di Russell, 1901, mostrò poi che la teoria ingenua degli insiemi va maneggiata con cautela.)»
**Fonte/verifica:** L2_appunti_2ott.md e L2_scheda.md §4 non contengono questa narrazione; date storiche (Peano 1889, Russell 1901).

### [GRAVITÀ: media] Capitolo 1, paragrafo 38
**Testo attuale:** «l'insieme vuoto ∅ e l'insieme A stesso sono detti sottoinsiemi banali (o impropri); qualsiasi altro sottoinsieme intermedio è detto proprio.»
**Problema:** contraddice il par. 34, dove "sottoinsieme proprio" significa contenuto e diverso dall'insieme (quindi ∅ sarebbe proprio); la terminologia banali/impropri/propri non è nelle fonti.
**Correzione proposta:** «Per un generico insieme non vuoto A, ∅ e A sono i sottoinsiemi banali; un sottoinsieme S ⊆ A con S ≠ A si dice proprio (definizione del par. 34). [Terminologia da verificare sul libro di Mori.]»
**Fonte/verifica:** L1_appunti_1ott.md e L1_scheda.md §2 non trattano propri/impropri; confronto interno par. 34 vs 38.

### [GRAVITÀ: media] Capitolo 2, paragrafo 60
**Testo attuale:** «gli elementi contenuti all'interno di un sotto-insieme non vengono ereditati automaticamente dall'insieme contenitore di livello superiore.»
**Problema:** formulazione falsa: gli elementi di un sottoinsieme appartengono sempre all'insieme contenitore; ciò che non vale è per un insieme che è elemento (A ∈ B non implica A ⊆ B, né che gli elementi di A stiano in B).
**Correzione proposta:** «gli elementi di un insieme che è a sua volta elemento di B (come A in B = {A, 3}) non sono automaticamente elementi di B: A ∈ B non implica A ⊆ B.»
**Fonte/verifica:** L1_appunti_1ott.md (⚠ A={1,2}, B={A,3}); L1_scheda.md §3 (trabocchetto).

### [GRAVITÀ: media] Capitolo 6, paragrafo 216 (e 252, 262, 265)
**Testo attuale:** «Una famiglia di sottoinsiemi 𝒫 = {Ai}i ∈ I è detta partizione dell'insieme S»
**Problema:** incoerenza di notazione: 𝒫 indica la partizione, ma nello stesso documento 𝒫(S) è l'insieme delle parti (par. 142, 265-266); con «S/𝒫» (par. 262) e «Q ⊆ 𝒫(S)» (par. 266) i due usi si confondono.
**Correzione proposta:** usare un altro simbolo per la partizione, per esempio «Π = {Ai}i∈I» (par. 216, 252, 262: «S/Π»), lasciando 𝒫(S) solo per l'insieme delle parti.
**Fonte/verifica:** L3_appunti_6ott.md e L3_scheda.md §1-2 non danno nome alla partizione (usano «{Ai}»); confronto interno par. 142 vs 216/252/262.

### [GRAVITÀ: bassa] Capitolo 5, paragrafo 189 (e 184)
**Testo attuale:** «la proprietà vale per ogni n ∈ ℕ.»
**Problema:** la base è n=1 e P(n) è enunciata per ∀ n ≥ 1 (par. 180), quindi la conclusione corretta è n ≥ 1, non n ∈ ℕ (che con ℕ = {0,1,…} include 0); inoltre al par. 184 compare «((n+1))» con doppia parentesi.
**Correzione proposta:** «la proprietà vale per ogni n ≥ 1.» (par. 184: «Raccoglimento parziale di (n+1)»).
**Fonte/verifica:** par. 180-181 del Word; L2_appunti_2ott.md (esempio: base n = 1); calcolo Python/SymPy: differenza tra (1/6)n(n+1)(2n+1)+(n+1)² e (1/6)(n+1)(n+2)(2n+3) = 0 e 2n²+7n+6=(n+2)(2n+3) (passaggi 183-188 corretti).

### [GRAVITÀ: bassa] Capitolo 1, paragrafo 33 (e Capitolo 5, paragrafo 167)
**Testo attuale:** «S ⊆ T ⟺ (∀ x ∈ S ⟹ x ∈ T)» e «∀ n ∈ U ⟹ S(n) ∈ U»
**Problema:** notazione mal formata: il quantificatore non regge direttamente un'implicazione (e al par. 33 la variabile differisce dalla fonte, z).
**Correzione proposta:** par. 33: «S ⊆ T ⟺ ∀ z ∈ S, z ∈ T»; par. 167: «∀ n ∈ ℕ, (n ∈ U ⟹ S(n) ∈ U)».
**Fonte/verifica:** L1_appunti_1ott.md («S ⊆ T ⟺ ∀z ∈ S, z ∈ T»); L2_appunti_2ott.md assioma 5.

### [GRAVITÀ: bassa] Capitolo 4, paragrafo 106
**Testo attuale:** «la differenza tra insiemi non gode della proprietà commutativa, ossia A ∖ B ≠ B ∖ A.»
**Problema:** imprecisione: A ∖ B = B ∖ A vale in alcuni casi (per esempio A = B), non è un "≠" universale.
**Correzione proposta:** «In generale la differenza non è commutativa: esistono insiemi per cui A ∖ B ≠ B ∖ A (per esempio A = {1,2}, B = {2,3}: A ∖ B = {1}, B ∖ A = {3}).»
**Fonte/verifica:** L2_appunti_2ott.md (cita A \ B e B \ A senza affermare ≠); controllo diretto sull'esempio.

### [GRAVITÀ: bassa] Capitolo 4, paragrafi 107 e 150
**Testo attuale:** «oppure Sc» e «il triletto {a, b, c}»
**Problema:** «Sc» non è nelle fonti ed è ambiguo (non indica l'universo A, da cui il complementare dipende); «triletto» non è terminologia standard (è l'insieme A stesso).
**Correzione proposta:** par. 107: eliminare «oppure Sc»; par. 150: «e l'insieme intero {a, b, c}».
**Fonte/verifica:** L2_appunti_2ott.md e L2_scheda.md §1 (solo 𝒞_A(B)); L2_appunti_2ott.md (𝒫({a,b,c}) con {a,b,c}).

### [GRAVITÀ: bassa] Capitolo 6, paragrafi 206-207
**Testo attuale:** «ℱ = {Ai}{i ∈ I}» e «⋃{i ∈ I} Ai = S»
**Problema:** notazione incoerente con il resto (par. 216 «{Ai}i ∈ I», 254 «⋃i ∈ I Ai»): graffe di troppo.
**Correzione proposta:** «ℱ = {Ai}i∈I» e «⋃i∈I Ai = S».
**Fonte/verifica:** confronto interno par. 206-207 vs 216, 253-254; L2_scheda.md §5.

### [GRAVITÀ: bassa] Capitolo 6, paragrafo 212
**Testo attuale:** «A3 = {n ∈ ℕ | n > 1000}»
**Problema:** diverso dall'esempio dell'appunto del docente (A3 = {n > 10000}); la tesi (ricoprimento ma non partizione) resta vera con entrambe le versioni, ma non coincide con la fonte.
**Correzione proposta:** «A3 = {n ∈ ℕ | n > 10000}»
**Fonte/verifica:** L2_appunti_2ott.md (sez. «Def. Ricoprimento e partizione»); verifica Python: unione = ℕ con soglia 1000 e 10000 (su 0..20000).

### [GRAVITÀ: bassa] Capitolo 9, paragrafo 358
**Testo attuale:** «(Cap. 2, Def. 2.1 Mori)»
**Problema:** riferimento bibliografico non presente in nessuna fonte (le schede citano solo Cap. 1 e Appendice A); non verificabile.
**Correzione proposta:** togliere il riferimento oppure scrivere «(rif. libro di Mori: da verificare)».
**Fonte/verifica:** L3_appunti_6ott.md (sez. Funzioni, solo accenno al grafico di f: ℝ → ℝ); L3_scheda.md (nessuna sezione sulle funzioni).

---

## Note: affermazioni non presenti nelle fonti (nessun errore matematico accertato, non da imparare a memoria)
- Cap. 1, par. 3-4, 6, 9, 25: la matematica discreta «non utilizza in alcun modo limite e continuità», Enigma/RSA «si basano interamente su strutture algebriche e aritmetiche discrete», «negli ultimi 120 anni», aneddoto Hardy/Ramanujan (il 1729 è l'esempio di numero "interessante", quindi citato qui in senso quasi opposto), «l'insieme vuoto è indispensabile per definire le basi dell'aritmetica». Contenuto di cornice assente da L1_appunti_1ott.md e L1_scheda.md.
- Cap. 7, par. 243-249 e Cap. 9, par. 352-354: richiami sugli insiemi numerici e sui limiti della definizione "formula" di funzione non compaiono nelle fonti; contenuto corretto.
- Cap. 3, par. 78-82: leggi distributive (corrette) non compaiono negli appunti di L1.
