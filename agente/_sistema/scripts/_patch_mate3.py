from pathlib import Path
B = Path(__file__).resolve().parent.parent / "bozze"


def ed(f, pairs):
    p = B / f
    t = p.read_text(encoding="utf-8")
    for a, b in pairs:
        assert a in t, (f, a[:60])
        t = t.replace(a, b, 1)
    p.write_text(t, encoding="utf-8")


ed("mate_cap34.md", [
    ("tale che la sua immagine di i₁ è i₂, quella", "tale che l'immagine di i₁ è i₂, quella"),
    ("{i₁, …, i_ℓ} dei primi n numeri tale", "{i₁, …, i_ℓ} (con ℓ ≥ 2) dei primi n numeri tale"),
    ("Il numero ℓ di elementi mossi è la **lunghezza** del ciclo: questo è un ciclo di lunghezza 4.",
     "Il numero ℓ di elementi mossi è la **lunghezza** del ciclo (in parole povere: quanti numeri il ciclo sposta): questo è un ciclo di lunghezza 4."),
    ("e due cicli disgiunti **commutano**",
     "(in parole povere: due cicli sono disgiunti se muovono numeri completamente diversi) e due cicli disgiunti **commutano**"),
    ("quindi **non** sono a due a due disgiunti.",
     "quindi **non** sono a due a due disgiunti. (In parole povere: comunque si prendano due cicli, non devono avere nessun numero in comune.)"),
    ("Una considerazione marginale",
     "(In parole povere: «essenzialmente unica» vuol dire che i cicli sono sempre gli stessi, e cambia al massimo l'ordine in cui si scrivono.)\n\nUna considerazione marginale"),
    ("(Controllo nostro: le permutazioni di questi tipi sono rispettivamente 6, 8, 3, 6 e 1, che sommate danno 24 = 4!, tutte le permutazioni di S₄.)",
     "Si può verificare che le permutazioni di questi tipi sono rispettivamente 6, 8, 3, 6 e 1, che sommate danno 24 = 4!, cioè tutte le permutazioni di S₄."),
    ("Queste scritture si chiamano **partizioni** di n.",
     "Queste scritture si chiamano **partizioni** di n (in parole povere: i modi di spezzare n in addendi)."),
    ("**In parole povere:** un ciclo è un «giro» in cui ogni numero passa al posto del successivo e l'ultimo torna al posto del primo.",
     "(In parole povere: un ciclo è un «giro» in cui ogni numero passa al posto del successivo e l'ultimo torna al posto del primo.)"),
    ("**In parole povere:** ogni permutazione (che non sia l'identità) si può spezzare in cicli che non si toccano, e la spezzatura è praticamente una sola.",
     "(In parole povere: ogni permutazione che non sia l'identità si può spezzare in cicli che non si toccano, e la spezzatura è praticamente una sola.)"),
    ("**In parole povere:** il tipo è la lista, dalla più lunga alla più corta, delle lunghezze dei cicli di cui è fatta la permutazione.",
     "(In parole povere: il tipo è la lista, dalla più lunga alla più corta, delle lunghezze dei cicli di cui è fatta la permutazione.)"),
])

ed("mate_cap35.md", [
    ("Si può andare avanti all'infinito incontrando sempre numeri nuovi? No: i numeri sono solo n, quindi a un certo punto si incontra un numero già incontrato prima. Ora, dove si può richiudere il percorso? Se si tornasse su un numero t_j con j > 1, tale numero sarebbe immagine di due elementi diversi (del suo predecessore nel percorso e di quello che lo ha raggiunto per la seconda volta), ma questo è impossibile perché **π è iniettiva**.",
     "Si può andare avanti all'infinito incontrando sempre numeri nuovi? No: i numeri sono solo n, quindi a un certo punto si incontra un numero già incontrato prima; sia t_j il primo elemento che si ripete. Ora, dove si può richiudere il percorso? Se fosse j > 1, il numero t_j sarebbe immagine di due elementi diversi (il suo predecessore t_{j−1} e l'elemento che lo ha raggiunto la seconda volta, che è diverso da t_{j−1} perché t_j è il primo che si ripete), ma questo è impossibile perché **π è iniettiva**."),
    ("**Il secondo ciclo è disgiunto dal primo.** Se un elemento s_j coincidesse con un t_i, quest'ultimo sarebbe immagine di due elementi diversi (di s_{j−1} e di t_{i−1}), e questo è impossibile per l'iniettività. Del resto C₂ è costruito partendo da numeri che sono stati tolti da T proprio per non appartenere al primo ciclo.",
     "**Il secondo ciclo è disgiunto dal primo.** Sia s_j il primo elemento del percorso che cade in C₁ (j > 1, perché s₁ è stato scelto fuori da C₁) e sia s_j = t_i. Allora s_{j−1} non sta in C₁, mentre t_{i−1} sta in C₁ (con t₀ := t_ℓ): sono due elementi diversi con la stessa immagine, e questo è impossibile per l'iniettività."),
    ("Perché si arriva alla fine? Perché il numero di elementi dell'insieme ancora da considerare **diminuisce davvero a ogni passo**: |T| > |T₁| > |T₂| > …,",
     "Perché si arriva alla fine? Si ponga T₁ = T \\ {t₁, …, t_ℓ}, poi T₂ = T₁ \\ {s₁, s₂, …}, e così via. Il numero di elementi dell'insieme ancora da considerare **diminuisce davvero a ogni passo**: |T| > |T₁| > |T₂| > …,"),
    ("a quel punto π è la composizione dei cicli costruiti, che sono a due a due disgiunti. ∎",
     "a quel punto ogni elemento di T sta in uno e un solo ciclo costruito, e i cicli sono a due a due disgiunti. Quindi la loro composizione manda ogni x ∈ T in π(x) e lascia fermi gli altri numeri, cioè coincide con π. ∎\n\nQuesta dimostrazione costruisce la scrittura, cioè prova l'**esistenza**; l'unicità a lezione è stata solo enunciata."),
    ("Il procedimento con le tabelle a tre righe funziona sempre ma è lungo.",
     "Il procedimento con la tabella (una riga per ogni ciclo, poi si cancellano le righe intermedie tenendo la prima e l'ultima) funziona sempre ma è lungo."),
    ("si applica la prima funzione, poi la seconda al risultato, e così via.",
     "si applica prima la funzione più a destra, poi quella alla sua sinistra, e così via."),
    ("**Un altro esempio.** (1 3)", "**Un altro esempio** (anche questo calcolato apposta). (1 3)"),
    ("**In parole povere:** si prende un numero spostato e si segue il suo giro fino a chiuderlo; poi si prende un numero spostato fuori da quel giro e si fa lo stesso, e così via finché non restano più numeri spostati.",
     "(In parole povere: si prende un numero spostato e si segue il suo giro fino a chiuderlo; poi se ne prende uno fuori da quel giro e si fa lo stesso, e così via finché non restano più numeri spostati.)"),
])

ed("mate_cap36.md", [
    ("**In parole povere:** la potenza π^k è la permutazione che si ottiene applicando k volte di seguito la stessa permutazione.",
     "(In parole povere: la potenza π^k è la permutazione che si ottiene applicando k volte di seguito la stessa permutazione.)"),
    ("**π^{N−m} = id**, con 0 < N − m < N.", "**π^{N−m} = id**, con 0 < N − m ≤ N."),
    ("Quindi, andando avanti con le potenze, prima di arrivare alla potenza N c'era già una ripetizione: l'identità. La prima ripetizione che capita è proprio quella dell'identità, e ci si ritrova così: id, π, π², …, fino a un certo π^{p−1}, tutte diverse, e al passo successivo π^p = id.",
     "Se N è il primo esponente per cui c'è una ripetizione, e fosse π^N = π^m con m ≥ 1, allora π^{N−m} = id = π⁰ sarebbe una ripetizione precedente: assurdo. Quindi m = 0: **la prima ripetizione che capita è proprio quella dell'identità**. La successione è fatta così: id, π, π², …, fino a un certo π^{p−1}, tutte diverse, e al passo successivo π^p = id. (Sono tutte diverse perché, se fosse π^i = π^j con 0 ≤ i < j < p, componendo con π^{−i} si avrebbe π^{j−i} = id con 0 < j − i < p, contro la minimalità di p.)"),
    ("Si può quindi estendere la successione con π⁻¹, π⁻², π⁻³, … e così via.",
     "Si può quindi estendere la successione con π⁻¹, π⁻², π⁻³, … e così via. (In parole povere: π⁻¹ è la permutazione che «disfa» π, e π⁻ᵏ è «disfare k volte».)"),
    ("Il tipo e la scomposizione in cicli disgiunti sono gli strumenti da usare, ma la risposta completa è rimandata alla lezione successiva.",
     "Probabilmente gli strumenti da usare sono il tipo e la scomposizione in cicli disgiunti, ma la risposta è rimandata alla lezione successiva."),
])
p = B / "mate_cap36.md"
t = p.read_text(encoding="utf-8")
a = t.index("Un'osservazione di verifica")
t = t[:a] + "Un'osservazione: per una permutazione che è un solo ciclo di lunghezza ℓ, il periodo è esattamente ℓ.\n"
p.write_text(t, encoding="utf-8")
print("ok")
