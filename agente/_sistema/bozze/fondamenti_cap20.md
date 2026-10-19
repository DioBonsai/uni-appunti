# 20. Predicati, Dominio del Discorso e Variabili
## Perché non basta la logica proposizionale
Dopo la logica proposizionale (capitoli 12-19) si passa alla **logica dei quantificatori**. Come sottolineato a lezione, la si tratta con più dettaglio di quanto facciano i corsi di matematica, ma per un motivo diverso: lo scopo è preparare alla possibilità di **meccanizzare il ragionamento**, cioè insegnare a un computer a controllare una dimostrazione e a cercare delle verità. Per questo bisogna conoscere con precisione le definizioni di connettivo, di quantificatore e le regole di inferenza, più di quanto servirebbe per capire una dimostrazione di matematica; gli esempi di prove che si fanno sono volutamente troppo semplici per un corso di matematica, ma servono a capire che cos'è una prova e come si controlla se è corretta.

La logica delle sezioni 1.2 e 1.3 non basta a descrivere la maggior parte degli enunciati della matematica e dell'informatica. Si prenda l'affermazione «n è un intero dispari»: non è una proposizione, perché è vera o falsa a seconda del valore di n (è vera per n = 103 e falsa per n = 8). Siccome quasi tutti gli enunciati usano variabili, bisogna estendere la logica per includerle.

## Funzione proposizionale (o predicato)
**Definizione.** Sia P(x) un enunciato che contiene la variabile x e sia D un insieme. P si chiama **funzione proposizionale** o **predicato** (rispetto a D) se per ogni x ∈ D l'enunciato P(x) è una proposizione. L'insieme D si chiama **dominio del discorso** di P e specifica i valori ammessi per x.

Un predicato da solo non è né vero né falso: lo diventano le singole proposizioni P(x) quando alla variabile si assegna un valore del dominio. Si può pensare al predicato come a una **famiglia di proposizioni**, una per ogni elemento del dominio: se D = ℤ⁺ (gli interi positivi: ℤ è il nome degli interi, ℤ⁺ è riservato a 1, 2, 3, …) si ottiene la famiglia P(1), P(2), …, e ciascuna è vera o falsa ma non entrambe.

Il dominio serve perché certe sostituzioni non avrebbero senso: «π è un numero dispari» non significa nulla, perché si parla di interi. Un predicato può anche avere **più variabili**, come una funzione può avere più argomenti: il test di uguaglianza tra due stringhe, che si incontra in programmazione, è un predicato a due variabili sull'insieme delle sequenze di caratteri.

**Esempio.** Sia P(n) = «n è un intero dispari», con dominio ℤ⁺. Allora P(1) = «1 è dispari» è vera e P(2) = «2 è dispari» è falsa.

In programmazione succede lo stesso: l'affermazione x < y non è né vera né falsa finché non si assegnano valori a x e a y; con x = 3 e y = 2 diventa 3 < 2, che è falsa. Come in logica proposizionale, si possono quindi scrivere anche enunciati falsi (come «2 è un numero primo dispari»): servono proprio perché si vuole insegnare a un computer a distinguere tra vero e falso, a dare una garanzia quando un'affermazione è vera o a smentire una convinzione sbagliata.

Esempi di funzioni proposizionali, con il loro dominio:
- n² + 2n è dispari (dominio ℤ⁺);
- x² − x − 6 = 0 (dominio ℝ);
- «il giocatore ha battuto sopra .300 nel 2015» (dominio: i giocatori di baseball);
- «il film ha una valutazione superiore al 20% su Rotten Tomatoes», con la scala da 0% a 100% (dominio: i film valutati dal sito).

Negli ultimi due la variabile è «giocatore» o «film»: sostituendo un giocatore o un film particolare si ottiene una proposizione (vera con Spectre, che ha il 64%; falsa con Blended, che ha il 14%). Ciò che è un parametro con valore già assegnato, come il 20% o il nome del sito, non è la variabile: cambiando sito o soglia cambia la funzione, ma resta una funzione proposizionale nella sola variabile film.

Un predicato può essere **sempre vero**, **sempre falso**, oppure vero in qualche caso e falso in altri. Per x² − x − 6 = 0 su ℝ basta risolvere l'equazione di secondo grado: le radici sono 3 e −2, quindi il predicato è vero solo per x = 3 e x = −2 e falso in tutti gli altri casi (con x = 10 si ha 100 − 10 − 6 = 84).

## Variabile libera e variabile legata
Si chiama **variabile libera** una variabile non ancora assegnata (è «libera» di spaziare su tutto il dominio), e **variabile legata** una variabile a cui è stato assegnato un valore oppure che compare dentro un quantificatore, nel qual caso si intende che prende tutti i valori del dominio.

Una funzione proposizionale non ha un valore di verità. Un enunciato con variabili libere **non è una proposizione**; un enunciato senza variabili libere (tutte legate) **è una proposizione**, e ha un valore di verità.

Due esempi di enunciati senza variabili libere: «per ogni triangolo T, la somma degli angoli di T è 180°» (un teorema di geometria euclidea) e «esiste un programma P il cui output è P stesso» (in informatica; ne sono un esempio i virus, che devono saper produrre in output sé stessi per riprodursi, cosa più facile in un linguaggio a basso livello dove si sa in quali celle sta il programma). Per dare un significato a enunciati di questo tipo si dovrebbero prendere tutti i triangoli, o tutti i programmi, e controllarli: un metodo puramente ideale, perché sono infiniti. Sono esempi di **quantificazione**, introdotta nei capitoli seguenti: il capitolo 21 tratta «per ogni», il capitolo 22 tratta «esiste».
