# 19. Composizione, Iniettività e Suriettività: le Funzioni Inverse
## Che cosa si conserva componendo
Se si compongono funzioni di un certo tipo, si ottiene ancora una funzione dello stesso tipo? Per iniettività e suriettività la risposta è sì.

**Proposizione 1.** Siano f : A → B e g : B → C due funzioni.
- Se f e g sono iniettive, allora g ∘ f è iniettiva.
- Se f e g sono suriettive, allora g ∘ f è suriettiva.

**Dimostrazione (iniettività).** Siano a₁ ≠ a₂ in A.
1. Poiché f è iniettiva, f(a₁) ≠ f(a₂).
2. Poiché g è iniettiva e f(a₁), f(a₂) sono due elementi diversi di B, g(f(a₁)) ≠ g(f(a₂)).
3. Quindi (g ∘ f)(a₁) ≠ (g ∘ f)(a₂).

**Dimostrazione (suriettività).** Bisogna controllare che per ogni y ∈ C esista x ∈ A con (g ∘ f)(x) = g(f(x)) = y.
1. Poiché g è suriettiva, esiste b ∈ B con g(b) = y.
2. Poiché f è suriettiva, esiste x ∈ A con f(x) = b.
3. Allora (g ∘ f)(x) = g(f(x)) = g(b) = y.

## Il viceversa: che cosa si deduce da g ∘ f
Se invece si sa qualcosa della composta, si può dedurre qualcosa su una delle due funzioni: l'iniettività sulla prima, la suriettività sulla seconda.

**Proposizione 2.** Siano f : A → B e g : B → C due funzioni.
- Se g ∘ f è iniettiva, allora f è iniettiva.
- Se g ∘ f è suriettiva, allora g è suriettiva.

**Dimostrazione (iniettività).** Si dimostra che se f **non** è iniettiva allora g ∘ f non può essere iniettiva.
1. Se f non è iniettiva esistono a₁ ≠ a₂ in A con f(a₁) = f(a₂).
2. Applicando g si ottiene g(f(a₁)) = g(f(a₂)), cioè (g ∘ f)(a₁) = (g ∘ f)(a₂).
3. Quindi g ∘ f non è iniettiva.

**Dimostrazione (suriettività).**
1. Poiché g ∘ f è suriettiva, per ogni y ∈ C esiste x ∈ A con (g ∘ f)(x) = g(f(x)) = y.
2. Posto b = f(x) ∈ B, si ha g(b) = y.
3. Quindi ogni y ∈ C è immagine tramite g di un elemento di B: g è suriettiva.

**Conseguenza (∗).** Se g ∘ f è biettiva, allora f è iniettiva e g è suriettiva.

Non si può dire di più: con f : {0} → {0, 1}, f(0) = 0 e g : {0, 1} → {0} costante, g ∘ f è biettiva ma g non è iniettiva e f non è suriettiva.

## Le funzioni inverse
Supponiamo di avere due funzioni f : A → B e g : B → A tali che

g ∘ f = id_{A} e f ∘ g = id_{B}.

Applichiamo (∗) a ciascuna delle due uguaglianze:
- id_{A} è biettiva, quindi (∗) dà: f è iniettiva e g è suriettiva;
- id_{B} è biettiva, quindi (∗) applicata a f ∘ g dà: g è iniettiva (è la funzione che si applica per prima) e f è suriettiva.

Dunque f e g sono entrambe iniettive e suriettive: **questa situazione può capitare solo se f e g sono entrambe biettive**. Quando capita si dice che f e g sono **funzioni inverse** l'una dell'altra.

Questo spiega il teorema del capitolo 15: una funzione invertibile è necessariamente biettiva. Il verso opposto (una funzione biettiva è sempre invertibile) è enunciato nel capitolo 15; qui sopra è dimostrata solo la necessità della biettività.
