from pathlib import Path
B = Path(__file__).resolve().parent.parent / "bozze"


def ed(f, pairs):
    p = B / f
    t = p.read_text(encoding="utf-8")
    for a, b in pairs:
        assert a in t, (f, a[:60])
        t = t.replace(a, b, 1)
    p.write_text(t, encoding="utf-8")


# ---- cap 30
ed("fondamenti_cap30.md", [
    ("Se c'è un dodecaedro piccolo è **falsa**;", "Se c'è un dodecaedro non grande (piccolo o medio) è **falsa**;"),
    ("Quando c'è un solo oggetto non c'è differenza tra ∀ e ∃: dire che c'è un oggetto con la proprietà o che tutti ce l'hanno vuol dire sempre la stessa cosa riferita a quell'unico oggetto. In generale il ∀ è una richiesta molto più forte dell'∃, ma con un solo oggetto coincidono.",
     "Quando c'è un solo dodecaedro non c'è differenza tra ∀ e ∃ riferiti ai dodecaedri: dire che c'è un oggetto con la proprietà o che tutti ce l'hanno vuol dire sempre la stessa cosa riferita a quell'unico oggetto. In generale, quando ci sono oggetti, il ∀ è una richiesta molto più forte dell'∃, ma con un solo oggetto coincidono."),
    ("2. **Due o più dodecaedri, di cui uno piccolo**: la 3 è falsa e la 4 vera, perché per la 4 basta che ce ne sia uno grande.",
     "2. **Due o più dodecaedri, di cui almeno uno grande e almeno uno non grande**: la 3 è falsa e la 4 vera, perché per la 4 basta che ce ne sia uno grande. Se invece nessuno è grande, anche la 4 è falsa."),
    ("Le formule usate nell'esempio (con predicati **Cube(x)**, **Tet(y)**, **LeftOf(x, y)**, **FrontOf(x, y)**, **Dodec(x)**, **Large(x)**) sono:",
     "Le formule usate nell'esempio usano i predicati Cube (cubo), Tet (tetraedro), LeftOf (a sinistra di), FrontOf (davanti a), Dodec (dodecaedro) e Large (grande). Sono:"),
    ("**FrontOf(x, y)** vuol dire che x si trova su una riga più vicina al bordo inferiore (cioè «più vicina alla nostra fronte», se si guarda la scacchiera da quel lato) rispetto a y.",
     "**FrontOf(x, y)** vuol dire che x si trova su una riga più vicina al bordo inferiore (cioè «più vicina alla nostra fronte», se si guarda la scacchiera da quel lato) rispetto a y.\n\n(In parole povere: LeftOf guarda le colonne da sinistra, FrontOf guarda le righe dal bordo inferiore.)"),
    ("e il docente ha detto di preferire la prima (questione di stile).", "e il docente preferisce presentarla come negazione di una congiunzione (questione di stile)."),
    ("Con questo si chiude il capitolo 1 della Parte 2. Il capitolo successivo inizia con i metodi di prova.", "Con questo si chiude il capitolo 1 della Parte 2."),
    ("- come la **negazione di una congiunzione**: ¬(A ∧ ¬B), cioè «non è vero che l'ipotesi è vera e la tesi è falsa» (esclude l'unico caso che smentisce l'implicazione);",
     "- come la **negazione di una congiunzione**: ¬(A ∧ ¬B), cioè «non è vero che l'ipotesi è vera e la tesi è falsa» (esclude l'unico caso che smentisce l'implicazione; in parole povere: l'implicazione fallisce solo quando A è vera e B è falsa);"),
])

# ---- cap 29
ed("fondamenti_cap29.md", [
    ("Sia dato x e y numeri reali", "Siano x e y numeri reali"),
    ("Il valore di verità di una formula con quantificatori dipende dal **dominio del discorso**: bisogna sempre fissarlo prima di rispondere.",
     "Il valore di verità di una formula con quantificatori dipende dal **dominio del discorso** (in parole povere: dall'insieme di valori che le variabili possono assumere): bisogna sempre fissarlo prima di rispondere."),
    ("(«Lezione 12: Quantificatori annidati» e «Lezione 13: ripasso lezioni 07-11»)", "(sui quantificatori annidati e sulle lezioni precedenti)"),
    ("Come ha detto il docente a proposito di una variante, mantenendo le variabili legate ai quantificatori come prima e scambiando solo l'ordine, oppure scambiando le variabili tenendo l'ordine, il significato cambia comunque: la formula è un oggetto molto «fragile».",
     "Come ha detto il docente, il significato di una formula è molto fragile: basta cambiare un dettaglio e cambia tutto. Con y > x: ∀x∃y(y > x) è vera; scambiando solo l'ordine dei quantificatori si ottiene ∃y∀x(y > x), falsa; tenendo fisso l'ordine delle variabili e scambiando i quantificatori si ottiene ∃x∀y(y > x), falsa anche scegliendo y = x. In ogni caso il significato cambia, ma in modo diverso."),
])

# ---- cap 28
t = (B / "fondamenti_cap28.md").read_text(encoding="utf-8")
i = t.index("## Le macchine possono ragionare con rigore?")
j = t.index("Nei capitoli seguenti")
nuovo = """## Le macchine possono ragionare con rigore?
A lezione il docente ha fatto qualche cenno di curiosità, senza dimostrazioni. Il ragionamento logico rigoroso, senza errori, è molto più difficile da far fare a una macchina dei ragionamenti informali con una certa percentuale di errori, che oggi si sanno far fare con una certa facilità.

Una prova che usa esplicitamente le regole logiche si chiama **prova formale** (in parole povere: una prova scritta con tutti i passaggi, senza saltare nulla); le prove della matematica di tutti i giorni non lo sono, e le prove formali sono molto più lunghe. Il rapporto fra la lunghezza della versione formale e quella della prova informale originaria si chiama **De Bruijn loss factor**. Circa 45 anni fa, quando si è cominciato a far fare queste prove a una macchina, era di circa 10-20; per le immagini, invece, il rapporto fra la rappresentazione completa e ciò di cui siamo consapevoli è enorme: un'immagine di circa un milione di punti, con tre byte per punto (rosso, verde e blu), occupa circa 24 milioni di cifre binarie, mentre noi la riassumiamo in una frase. Nel libro del docente si riporta che negli anni recenti (circa cinque anni fa, secondo il docente) il fattore è sceso a circa 4: con un fattore così piccolo le prove diventano quasi trattabili.

Per l'informatica interessano soprattutto le prove di **correttezza di programmi** (per esempio di un ciclo), che sono prove piccole. I **proof assistant** sono programmi che aiutano a controllare queste prove (in parole povere: assistenti che verificano che ogni passaggio della prova sia valido). Gli esempi citati sono **Frama-C**, che serve a controllare che un programma C non abbia errori a tempo di esecuzione né deviazioni dalla specifica, e **Dafny**, accennato nel corso di Programmazione I e usato davvero nel corso di Metodi Formali dell'Informatica; il docente ha detto di non averli usati personalmente.

Perché si fanno queste prove? Provare un programma su molti esempi, anche miliardi di esempi casuali, non basta: alcuni errori si manifestano in situazioni che nessuno ha ancora immaginato. L'unico modo per essere sicuri che il programma funzioni in tutti i casi è un ragionamento che valga per tutti gli infiniti casi, cioè un ragionamento con quantificatori, e si vorrebbe delegarlo il più possibile a una macchina. Gli errori nei programmi non si possono tollerare, perché possono costare molto (il docente ha ricordato il blocco del canale di Suez causato dalla guida automatica di una nave).

"""
t = t[:i] + nuovo + t[j:]
(B / "fondamenti_cap28.md").write_text(t, encoding="utf-8")
ed("fondamenti_cap28.md", [
    ("Le leggi per i quantificatori annidati (libro, sezione 1.6):\n- ¬(∀x∃y P(x, y)) ≡ ∃x¬(∃y P(x, y)) ≡ ∃x∀y ¬P(x, y).",
     "Le leggi di De Morgan per i quantificatori annidati sono:\n- ¬(∀x∃y P(x, y)) ≡ ∃x¬(∃y P(x, y)) ≡ ∃x∀y ¬P(x, y);\n- ¬(∃x∀y P(x, y)) ≡ ∀x¬(∀y P(x, y)) ≡ ∀x∃y ¬P(x, y)."),
    ("(in parole povere: la negazione «attraversa» i quantificatori e li capovolge, e a ogni passo la formula resta equivalente, cioè non cambia il suo valore di verità.)",
     "(in parole povere: la negazione «attraversa» i quantificatori e li capovolge, e a ogni passo la formula resta equivalente, cioè non cambia il suo valore di verità.)") if False else ("la negazione si sposta sempre più vicina agli argomenti" , "la negazione si sposta sempre più vicina agli argomenti") if False else ("(In parole povere: la negazione «attraversa» i quantificatori", "(In parole povere: la negazione «attraversa» i quantificatori"),
    ("(una formula le cui parti non sono più formule, per esempio x·y < 1)", "(una formula le cui parti non sono più formule, per esempio x·y < 1; in parole povere: una formula che non si può più spezzare in formule più semplici)"),
    ("(si dice **involutiva**, come ricordato dal libro: «involvere» vuol dire tornare indietro)", "(si dice **involutiva**: «involvere» vuol dire tornare indietro)"),
    ("lezione di chiusura del capitolo 1 della Parte 2: esercizi sulle lezioni 07-12", "lezione di chiusura del capitolo 1 della Parte 2: esercizi sulle lezioni 07-12"),
])
print("ok")
