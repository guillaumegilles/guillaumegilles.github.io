``` js
fmt = (x, d = 0) =>
  x.toLocaleString("fr-FR", {minimumFractionDigits: d, maximumFractionDigits: d})
pct = (x, d = 2) => fmt(100 * x, d) + " %"
```

## 0.1 Que préférez-vous ?

Sans calculer — votez à main levée, puis justifiez.

OPTION A

10 000 €

aujourd'hui

OPTION B

11 000 €

dans 1 an

OPTION C

12 500 €

dans 2 ans

Le montant le plus élevé n’est pas forcément le meilleur. **Toute la journée tient dans cette question.**

Vote à main levée (2 min). Noter au tableau la répartition A/B/C. Demander 2-3 justifications : elles font émerger préférence pour le présent, placement possible, inflation, risque. On y reviendra en fin de Séquence 3 avec l’outil pour trancher.

## 0.2 Pourquoi 1 € aujourd’hui vaut plus que 1 € demain ?

- ⏳ **Préférence pour le présent** — on préfère disposer de l’argent maintenant.
- 💼 **Coût d’opportunité** — 10 000 € placés aujourd’hui produisent des intérêts.
- 📈 **Inflation** — 11 000 € dans un an achèteront peut-être moins.
- 🎲 **Risque** — une somme future est incertaine, une somme présente est certaine.

4 raisons → **1 seul paramètre** : le taux d’actualisation $i$

## 0.3 Objectifs de la journée

À la fin de cette journée, vous saurez :

1.  distinguer **capitalisation** et **actualisation** ;
2.  **convertir des taux** exprimés sur des périodicités différentes ;
3.  calculer la **valeur actuelle ou acquise** d’un capital isolé ;
4.  valoriser une suite d’**annuités constantes** (fin, début, différées, perpétuité) ;
5.  résoudre des problèmes d’**épargne et de constitution de capital**.

Plan : S2 intérêts simples/composés (1 h) · S3 actualisation (1 h) · S4 taux (1 h) · S5 annuités (1 h 15) · S6 cas pratique (1 h) · S7 synthèse (45 min) · S8 cas pratique de synthèse sur données réelles (2 h).

## 0.4 La règle d’or

✏️ La **ligne du temps** avant toute formule.

?

t = 0\
aujourd'hui

capitaliser →

t = 1

 

flux

t = n\
futur

1.  Placez **chaque flux à sa date**.
2.  Repérez la **date d’évaluation**.
3.  *Ensuite seulement* : capitaliser (→ futur) ou actualiser (← présent).

## 0.5 Diagnostic éclair ⚡

| Question | Réponse |
|----|----|
| $1{,}05^{10}$ ≈ ? | ≈ 1,629 |
| $1{,}03^{-5}$ ≈ ? | ≈ 0,863 (soit $1/1{,}03^5$) |
| Résoudre $x(1+i)^n = C$ | $x = C/(1+i)^n = C(1+i)^{-n}$ |
| Combien vaut 1 000 € dans 3 ans à 4 % ? | $1\,000 \times 1{,}04^3 ≈ 1\,124{,}86$ € |

Ces quatre gestes — puissances, puissances négatives, inversion, intuition — suffisent pour toute la journée.

Laisser 3-4 minutes en autonomie, calculatrice autorisée. Repérer les étudiants à l’aise avec les puissances négatives : ce sont eux qui suivront facilement l’actualisation.

1 Séquence 2\
Intérêts simples et intérêts composés
=====================================

Même taux, même durée… même résultat ?

## 1.1 La situation de Léa

Léa reçoit une prime de **10 000 €**, inutile avant **10 ans**. Deux placements à **3 % par an** :

- **« Simple »** — verse chaque année 3 % du capital de départ (300 €), mis de côté.
- **« Cumul »** — ajoute chaque année les intérêts au capital.

Le conseiller : *« C’est le même taux, donc à peu près le même résultat. »*

Quel écart au bout de 10 ans ?

Votre pronostic   ① 0 €   ② ≈ 50 €   ③ ≈ 450 €   ④ ≈ 2 000 €

## 1.2 Ajouter ou multiplier ?

### 1.2.1 « Simple » + 300 €

10 000 **+ 300** = 10 300

10 300 **+ 300** = 10 600

10 600 **+ 300** = 10 900

On **ajoute** toujours le même montant.

### 1.2.2 « Cumul » × 1,03

10 000 **× 1,03** = 10 300

10 300 **× 1,03** = 10 609

10 609 **× 1,03** = 10 927

On **multiplie** toujours par le même facteur.

Dès l’année 2, les intérêts **produisent des intérêts**.

## 1.3 L’écart se creuse… de plus en plus vite

|  Année | « Simple » |  « Cumul » |   Écart |
|-------:|-----------:|-----------:|--------:|
|      0 |     10 000 |     10 000 |       0 |
|      1 |     10 300 |     10 300 |       0 |
|      2 |     10 600 |     10 609 |       9 |
|      3 |     10 900 |     10 927 |      27 |
|      5 |     11 500 |     11 593 |      93 |
|      8 |     12 400 |     12 668 |     268 |
| **10** | **13 000** | **13 439** | **439** |

Valeurs en €, arrondies.

- 439 €

en faveur de « Cumul » après 10 ans

\

Le conseiller **se trompe** : même taux ≠ même résultat.

Sur **20 ans** : 18 061 € contre 16 000 €, soit un écart de **2 061 €**. Durée × 2 → écart × 4,7

## 1.4 À vous de jouer 🎛️ — Simple vs composé

``` js
viewof taux_s2 = Inputs.range([0.01, 0.12], {value: 0.03, step: 0.005, label: "Taux annuel i"})
viewof duree_s2 = Inputs.range([1, 40], {value: 10, step: 1, label: "Durée n (années)"})
```

``` js
data_s2 = Array.from({length: duree_s2 + 1}, (_, t) => [
  {t, valeur: 10000 * (1 + t * taux_s2), regime: "Intérêts simples"},
  {t, valeur: 10000 * (1 + taux_s2) ** t, regime: "Intérêts composés"}
]).flat()

Plot.plot({
  width: 900, height: 300, marginLeft: 70,
  color: {domain: ["Intérêts simples", "Intérêts composés"], range: ["#5b9bdb", "#5bdb6d"], legend: true},
  x: {label: "Années →"},
  y: {label: "↑ Capital (€)", grid: true, tickFormat: d => fmt(d)},
  marks: [
    Plot.lineY(data_s2, {x: "t", y: "valeur", stroke: "regime", strokeWidth: 3}),
    Plot.ruleY([10000], {stroke: "#8b8f9c", strokeDasharray: "4"}),
    Plot.tip(data_s2, Plot.pointerX({x: "t", y: "valeur", stroke: "regime"}))
  ]
})
```

``` js
md`<div class="ojs-result">Après **${duree_s2} ans** : simple **${fmt(10000 * (1 + duree_s2 * taux_s2))} €** · composé **${fmt(10000 * (1 + taux_s2) ** duree_s2)} €** · écart <span class="orange">**${fmt(10000 * ((1 + taux_s2) ** duree_s2 - 1 - duree_s2 * taux_s2))} €**</span></div>`
```

Faire tester : doubler la durée (10 → 20 ans), puis doubler le taux (3 % → 6 %). Faire verbaliser : la droite (simple) contre la courbe (composé). Question : à quel moment l’écart dépasse-t-il le capital initial ?

## 1.5 Les deux formules

### 1.5.1 Intérêts simples

$$C_n = C_0\,(1 + n\,i)$$

Intérêts : $I = C_0\,n\,i$

Base de calcul : **capital initial** $C_0$

Croissance **linéaire**

### 1.5.2 Intérêts composés

$$C_n = C_0\,(1 + i)^n$$

Intérêts : $I = C_0\left[(1+i)^n - 1\right]$

Base de calcul : **capital courant** $C_{t-1}$

Croissance **exponentielle**

$C_0$ capital placé · $i$ taux **par période** (en décimal) · $n$ nombre de **périodes**

## 1.6 Pourquoi $(1+i)^n$ ?

$$C_1 = C_0 + C_0\,i = C_0(1+i)$$

$$C_2 = C_1(1+i) = C_0(1+i)^2$$

$$C_3 = C_2(1+i) = C_0(1+i)^3$$

$$\vdots \qquad\qquad \boxed{C_n = C_0(1+i)^n}$$

C₀

t = 0

× (1+i)

t = 1

× (1+i)

t = 2

…

Cₙ

t = n

## 1.7 Exemple résolu

> **20 000 €** placés **5 ans** à **4 %** par an.

**Simples**

$$20\,000 \times (1 + 5 \times 0{,}04)$$ $$= 20\,000 \times 1{,}20$$ $$= \mathbf{24\,000\ €}$$

**Composés**

$$20\,000 \times 1{,}04^5$$ $$= 20\,000 \times 1{,}21665$$ $$\approx \mathbf{24\,333\ €}$$

L’écart de **333 €** = les intérêts produits par les intérêts capitalisés.

Nuance : pour $n < 1$ (fraction d’année), les intérêts simples donnent *plus* ; pour $n > 1$, les composés l’emportent toujours.

## 1.8 🪤 Le piège

« 3 % par an pendant 10 ans, cela fait **30 %** de gain, quel que soit le placement. »

En composé, on multiplie 10 fois par 1,03 : $1{,}03^{10} \approx 1{,}344$, soit **+ 34,4 %**, et non 30 %.

En composé, on **multiplie**, on n’additionne pas.

## 1.9 Points de vigilance

Avant d’appliquer une formule, vérifiez :

1.  Le **taux** est en décimal : $0{,}04$ et non $4$.
2.  La **durée** $n$ est un nombre de *périodes*, pas forcément d’années.
3.  La **périodicité** du taux (mensuelle, trimestrielle, annuelle…).
4.  La **fréquence de capitalisation** des intérêts.

## 1.10 🧠 Vérifiez votre compréhension

> 1 000 € placés **2 ans** à **10 %**. Valeur acquise en simple ? En composé ? D’où vient l’écart ?

- Simple : $1\,000 \times 1{,}20 = 1\,200$ €
- Composé : $1\,000 \times 1{,}1^2 = 1\,210$ €

L’écart de **10 €** = 10 % des 100 € d’intérêts de la 1^(re) année : **l’intérêt de l’intérêt**.

2 Séquence 3\
Actualisation et équivalence financière
=======================================

Combien vaut aujourd’hui une somme future ?

## 2.1 Une facture, deux options

Un client propose de vous régler :

- **1 000 €** aujourd’hui,
- ou **1 100 €** dans un an.

Vous pouvez placer votre trésorerie sans risque à **5 % par an**.

Quelle offre accepter ?

Votre choix

Capitalisation : « combien vaut un capital **dans le futur** ? »\
Actualisation : « combien vaut un capital futur **aujourd’hui** ? »

## 2.2 Deux façons de comparer… à la même date

### 2.2.1 Avancer → (capitaliser)

1 000

t = 0

× 1,05

1 050

t = 1

1 050 € **\<** 1 100 €

### 2.2.2 ← Reculer (actualiser)

1 047,62

t = 0

÷ 1,05

1 100

t = 1

1 047,62 € **\>** 1 000 €

✅ Même conclusion : **accepter 1 100 € dans un an**. Seuil : il faudrait un placement à plus de 10 % (1 100 / 1 000) pour inverser la décision.

## 2.3 Et si c’était dans **deux** ans ?

On recule **deux fois** :

$$1\,100 \div 1{,}05 \div 1{,}05 = \frac{1\,100}{1{,}05^2} \approx 997{,}73\ €$$

997,73 € \< 1 000 €

Les mêmes 1 100 € deviennent **moins intéressants** que 1 000 € immédiats.

Diviser par $(1+i)^n$, c’est **remonter le temps**.

## 2.4 La formule d’actualisation

$$V_0 = \frac{V_n}{(1+i)^n} = V_n\,(1+i)^{-n}$$

V₀\
valeur actuelle

t = 0

÷ (1+i)

t = 1

…

Vₙ\
valeur future

t = n

- Facteur d’actualisation $(1+i)^{-n}$ **toujours \< 1** : une somme future vaut moins aujourd’hui.
- Si $i$ ↑ ou $n$ ↑ → $V_0$ ↓ : l’attente coûte plus cher.

## 2.5 Capitaliser ⇄ actualiser : un miroir

**Capitaliser** →

$$C_n = C_0 \times (1+i)^n$$

← **Actualiser**

$$V_0 = V_n \div (1+i)^n$$

Même calcul, **sens opposé**.

**Équivalence financière** — deux capitaux sont équivalents s’ils ont la **même valeur à une date commune**, au même taux.

## 2.6 Exemple résolu — Payer maintenant ou plus tard ?

> Payer **48 000 €** immédiatement, ou **52 000 €** dans 2 ans ? Taux : **5 %**.

$$VA = \frac{52\,000}{1{,}05^2} = \frac{52\,000}{1{,}1025} \approx 47\,166\ €$$

COMPTANT

48 000 €

valeur à t = 0

DIFFÉRÉ

47 166 €

valeur à t = 0

Le paiement différé coûte **moins cher** en valeur actuelle : il est financièrement préférable (toutes choses égales par ailleurs).

## 2.7 Le taux n’est jamais neutre 🎛️

``` js
viewof taux_s3 = Inputs.range([0.01, 0.15], {value: 0.05, step: 0.005, label: "Taux d'actualisation i"})
```

``` js
data_s3 = [0.02, taux_s3, 0.10].flatMap((r, k) =>
  Array.from({length: 31}, (_, n) => ({
    n, va: 1000 / (1 + r) ** n,
    courbe: k === 1 ? `Votre taux : ${pct(r, 1)}` : (k === 0 ? "Référence 2 %" : "Référence 10 %")
  }))
)

Plot.plot({
  width: 900, height: 300, marginLeft: 60,
  color: {legend: true, range: ["#8b8f9c", "#f0a500", "#555a68"]},
  x: {label: "Date du flux (années) →"},
  y: {label: "↑ Valeur actuelle de 1 000 € (€)", grid: true, domain: [0, 1000]},
  marks: [
    Plot.lineY(data_s3, {x: "n", y: "va", stroke: "courbe", strokeWidth: d => d.courbe.startsWith("Votre") ? 4 : 1.5}),
    Plot.tip(data_s3.filter(d => d.courbe.startsWith("Votre")), Plot.pointerX({x: "n", y: "va"}))
  ]
})
```

``` js
md`<div class="ojs-result">1 000 € reçus dans **10 ans** valent aujourd'hui <span class="orange">**${fmt(1000 / (1 + taux_s3) ** 10)} €**</span> · dans **30 ans** : <span class="orange">**${fmt(1000 / (1 + taux_s3) ** 30)} €**</span></div>`
```

Le taux reflète : coût du capital, risque, inflation, liquidité. Faire constater qu’un taux élevé « écrase » les flux lointains : c’est pourquoi les projets de long terme (climat, infrastructures) sont si sensibles au choix du taux.

## 2.8 🪤 Le piège

« 1 100 € dans un an, c’est plus que 1 000 € aujourd’hui, donc c’est forcément mieux. »

On compare deux montants **à des dates différentes**. Il faut d’abord les ramener à une **date commune** (actualiser ou capitaliser), puis comparer.

On ne compare et on n’additionne que des **euros de même date**.

## 2.9 🧠 Vérifiez votre compréhension

> Combien valent aujourd’hui **2 000 €** reçus dans **3 ans**, au taux de **4 %** ?

$$V_0 = \frac{2\,000}{1{,}04^3} \approx 1\,777{,}99\ €$$

Boucler avec le vote d’ouverture : comparer avec la répartition notée au tableau. Souligner que la réponse dépend du taux : à 15 %, A redevient la meilleure (B ≈ 9 565 €, C ≈ 9 452 €).

3 Séquence 4\
Taux proportionnels et taux équivalents
=======================================

« 0,75 % par mois, c’est 9 % par an. » Vraiment ?

## 3.1 Deux offres de crédit

Vous empruntez **10 000 €**, remboursés en une fois dans **un an**.

- **Organisme A** : **9 % par an**, intérêts calculés une fois en fin d’année.
- **Organisme B** : **0,75 % par mois**, intérêts ajoutés à la dette chaque mois.

Le commercial de B : *« 0,75 % × 12 = 9 %, c’est exactement pareil. »*

Ces deux offres coûtent-elles vraiment la même chose ?

Votre avis   Oui · B coûte plus cher · B coûte moins cher

## 3.2 La dette chez B, mois par mois

|   Mois | Dette chez B (×1,0075) | Si +75 €/mois |
|-------:|-----------------------:|--------------:|
|      0 |              10 000,00 |        10 000 |
|      1 |              10 075,00 |        10 075 |
|      2 |              10 150,56 |        10 150 |
|      3 |              10 226,69 |        10 225 |
|      6 |              10 458,52 |        10 450 |
|      9 |              10 695,61 |        10 675 |
| **12** |          **10 938,07** |    **10 900** |

Les intérêts mensuels passent de **75 €** (mois 1) à **81,42 €** (mois 12).

9,38 %

coût annuel réel chez B, et non 9 %

B coûte environ **38 € de plus** que A.

## 3.3 Diviser ou prendre la racine ?

### 3.3.1 Proportionnel

$$i_m = \frac{i_a}{12}$$

$9\,\% / 12 = 0{,}75\,\%$

❌ Ignore les intérêts sur intérêts.

### 3.3.2 Équivalent

$$(1 + i_m)^{12} = 1 + i_a$$

$1{,}09^{1/12} - 1 \approx 0{,}721\,\%$

✅ Donne *exactement* 9 % sur un an.

**Diviser** donne le proportionnel, la **racine** donne l’équivalent.

## 3.4 Formules générales

Pour $m$ sous-périodes par an :

**Annuel → sous-période**

$$i_p = (1 + i_a)^{1/m} - 1$$

**Sous-période → annuel (taux effectif, TAEG)**

$$i_a = (1 + i_p)^{m} - 1$$

**Exemple** — un taux mensuel de **0,5 %** :

$$i_a = 1{,}005^{12} - 1 \approx \mathbf{6{,}17\,\%} \quad \text{(et non } 6\,\% \text{)}$$

Les 0,17 point = l’effet de la capitalisation mensuelle.

## 3.5 Même taux affiché, coût réel différent 🎛️

``` js
viewof taux_s4 = Inputs.range([0.01, 0.20], {value: 0.09, step: 0.005, label: "Taux annuel affiché"})
```

``` js
freqs_s4 = [
  {f: "Annuelle", m: 1}, {f: "Semestrielle", m: 2}, {f: "Trimestrielle", m: 4},
  {f: "Mensuelle", m: 12}, {f: "Hebdomadaire", m: 52}, {f: "Quotidienne", m: 365}
].map(d => ({...d, eff: (1 + taux_s4 / d.m) ** d.m - 1}))

Plot.plot({
  width: 900, height: 300, marginLeft: 60,
  x: {label: null, domain: freqs_s4.map(d => d.f)},
  y: {label: "↑ Taux annuel effectif", tickFormat: d => pct(d, 1), grid: true,
      domain: [taux_s4 * 0.97, (Math.exp(taux_s4) - 1) * 1.01]},
  marks: [
    Plot.barY(freqs_s4, {x: "f", y1: taux_s4 * 0.97, y2: "eff", fill: "#5bdb6d", fillOpacity: 0.8}),
    Plot.text(freqs_s4, {x: "f", y: "eff", text: d => pct(d.eff), dy: -10, fill: "currentColor", fontSize: 14}),
    Plot.ruleY([taux_s4], {stroke: "#f0a500", strokeDasharray: "4"})
  ]
})
```

Taux proportionnel $i_a/m$ capitalisé $m$ fois par an. Pointillés : taux affiché.

Plus la capitalisation est fréquente, plus le coût réel s’élève à taux affiché identique — et l’écart grandit avec le niveau du taux (tester 3 % puis 18 %). C’est précisément pourquoi la loi impose l’affichage du TAEG pour les crédits.

## 3.6 Proportionnel ≠ équivalent

| Conversion    | Formule                   | Capitalisation prise en compte ? |
|---------------|---------------------------|:--------------------------------:|
| Proportionnel | $i_p = i_a / m$           |                ❌                |
| Équivalent    | $i_p = (1+i_a)^{1/m} - 1$ |                ✅                |

- En **finance exacte** (prêts immobiliers, obligations) : taux **équivalents**.
- Le proportionnel : conventions simplifiées ou durées \< 1 an.
- Pour comparer deux offres : convertir sur **la même période**, en taux équivalents.

## 3.7 🧠 Vérifiez votre compréhension

> Quel est le taux **trimestriel équivalent** à **8 % par an** ?

$$i_t = 1{,}08^{1/4} - 1 \approx 1{,}943\,\%$$

…et non $8\,\% / 4 = 2\,\%$, qui est le taux proportionnel. Capitalisé 4 fois, 2 % par trimestre donnerait 8,24 % sur l’année.

4 Séquence 5\
Annuités constantes
===================

Que vaut une suite de versements réguliers ?

## 4.1 Le projet de Thomas

Thomas veut un apport de **30 000 €** dans **5 ans**. Il peut épargner **5 000 € par an**, en **fin** d’année, à **3 %**.

5 × 5 000 = 25 000 € : il manque 5 000 € *sur le papier*… mais les intérêts travaillent.

Atteindra-t-il son objectif ?

Votre pronostic   Oui, largement · Oui, de justesse · Non

## 4.2 La règle d’or, version annuités

| Question | Pour Thomas |
|----|----|
| 1\. Quelle **date d’évaluation** ? | $t = 5$, le jour de l’achat |
| 2\. Flux en **début** ou en **fin** de période ? | Fin d’année |
| 3\. Y a-t-il un **différé** ? | Non |
| 4\. Taux et flux sur la **même périodicité** ? | Oui, annuels |
| 5\. **Capitaliser** ou **actualiser** ? | Capitaliser (vers le futur) |

t = 0

 

5 000

t = 1

 

5 000

t = 2

 

5 000

t = 3

 

5 000

t = 4

 

5 000

t = 5\
évaluation

## 4.3 Chaque versement travaille… plus ou moins longtemps

Fin d'année 1

5 627,54 €

Fin d'année 2

5 463,64 €

Fin d'année 3

5 304,50 €

Fin d'année 4

5 150,00 €

Fin d'année 5

5 000,00 €

Total

26 545,68 €

Barre = durée de placement : 4 ans, 3 ans, 2 ans, 1 an, 0 an. Valeur = $5\,000 \times 1{,}03^{\text{durée}}$.

❌ **Objectif manqué de 3 454 €.** Les intérêts (1 545,68 €) ne comblent qu’une partie de l’écart. Il faudrait verser $30\,000 / 26\,545{,}68 \times 5\,000 \approx$ **5 650,64 € par an**.

## 4.4 D’une somme géométrique… à une formule

$$5\,000 \times \left(1 + 1{,}03 + 1{,}03^2 + 1{,}03^3 + 1{,}03^4\right)$$

Une somme géométrique de raison $1{,}03$ et de 5 termes vaut :

$$\frac{1{,}03^5 - 1}{0{,}03} \approx 5{,}30914 \quad\Rightarrow\quad 5\,000 \times 5{,}30914 \approx 26\,545{,}68\ €$$

On remplace $5\,000 \to A$, $3\,\% \to i$, $5 \to n$ :

$$V_n = A \cdot \frac{(1+i)^n - 1}{i}$$

## 4.5 Annuités de fin de période (terme échu)

V₀

t = 0

 

A

t = 1

 

A

t = 2

…

A\
Vₙ

t = n

**Valeur acquise** (à $t = n$)

$$V_n = A \cdot \frac{(1+i)^n - 1}{i}$$

Thomas : **26 545,68 €**

**Valeur actuelle** (à $t = 0$)

$$V_0 = A \cdot \frac{1 - (1+i)^{-n}}{i}$$

Thomas : **22 898,54 €**

Si $i$ ↑ : $V_n$ ↑ mais $V_0$ ↓.

## 4.6 Pourquoi cette formule pour $V_0$ ?

On actualise chaque versement, puis on additionne :

$$V_0 = \frac{A}{(1+i)} + \frac{A}{(1+i)^2} + \cdots + \frac{A}{(1+i)^n}$$

Suite géométrique : 1^(er) terme $\dfrac{A}{1+i}$, raison $\dfrac{1}{1+i}$, $n$ termes.

$$V_0 = \frac{A}{1+i} \cdot \frac{1 - (1+i)^{-n}}{1 - \frac{1}{1+i}}
= \boxed{A \cdot \frac{1 - (1+i)^{-n}}{i}}$$

✔️ Contrôle : $V_n = V_0 \times (1+i)^n$ — **mêmes flux, vus à deux dates**.

## 4.7 Exemple résolu — L’engagement d’une PME

> Verser **2 000 €** en fin d’année pendant **4 ans**, au taux de **5 %**.

**Valeur actuelle**

$$2\,000 \times \frac{1 - 1{,}05^{-4}}{0{,}05}$$ $$= 2\,000 \times 3{,}54595 \approx \mathbf{7\,091{,}90\ €}$$

**Valeur acquise**

$$2\,000 \times \frac{1{,}05^{4} - 1}{0{,}05}$$ $$= 2\,000 \times 4{,}31013 \approx \mathbf{8\,620{,}25\ €}$$

Vérification : $7\,091{,}90 \times 1{,}05^4 \approx 8\,620{,}25$ € ✔️

## 4.8 Qui fait le capital : l’épargne ou les intérêts ? 🎛️

``` js
viewof A_s5 = Inputs.range([100, 10000], {value: 5000, step: 100, label: "Versement annuel A (€)"})
viewof i_s5 = Inputs.range([0, 0.10], {value: 0.03, step: 0.005, label: "Taux i"})
viewof n_s5 = Inputs.range([1, 40], {value: 5, step: 1, label: "Nombre de versements n"})
```

``` js
data_s5 = Array.from({length: n_s5}, (_, k) => {
  const t = k + 1
  const total = i_s5 === 0 ? A_s5 * t : A_s5 * ((1 + i_s5) ** t - 1) / i_s5
  return [
    {t, part: "Versements cumulés", montant: A_s5 * t},
    {t, part: "Intérêts cumulés", montant: total - A_s5 * t}
  ]
}).flat()

Plot.plot({
  width: 900, height: 260, marginLeft: 70,
  color: {domain: ["Versements cumulés", "Intérêts cumulés"], range: ["#5b9bdb", "#5bdb6d"], legend: true},
  x: {label: "Année →"},
  y: {label: "↑ Valeur acquise (€)", grid: true, tickFormat: d => fmt(d)},
  marks: [
    Plot.barY(data_s5, {x: "t", y: "montant", fill: "part", tip: true}),
    Plot.ruleY([0])
  ]
})
```

``` js
Vn_s5 = i_s5 === 0 ? A_s5 * n_s5 : A_s5 * ((1 + i_s5) ** n_s5 - 1) / i_s5
md`<div class="ojs-result">Valeur acquise : **${fmt(Vn_s5, 2)} €** · dont intérêts : <span class="green">**${fmt(Vn_s5 - A_s5 * n_s5)} €** (${pct((Vn_s5 - A_s5 * n_s5) / Vn_s5, 0)} du total)</span></div>`
```

Avec les paramètres de Thomas (5 000 €, 3 %, 5 ans), les intérêts ne pèsent que 6 % : c’est l’épargne qui fait le capital. Passer à 30 ans : les intérêts dépassent les versements. Trois leviers : verser plus, attendre plus longtemps, trouver un meilleur taux.

## 4.9 Annuités de début de période (terme à échoir)

A\
V₀

t = 0

 

A

t = 1

…

A

t = n−1

 

Vₙ

t = n

Chaque versement est **avancé d’une période** → il travaille une période de plus.

$$V_n^{\text{début}} = V_n^{\text{fin}} \times (1+i) \qquad V_0^{\text{début}} = V_0^{\text{fin}} \times (1+i)$$

Thomas, s’il versait en **début** d’année : $26\,545{,}68 \times 1{,}03 \approx$ **27 342 €**

## 4.10 🪤 Le piège

« Il y a 5 versements, donc la formule s’applique telle quelle, que l’on verse en début ou en fin d’année. »

La formule standard suppose des versements **en fin de période**. En début de période, chaque versement travaille une année de plus : on multiplie par $(1+i)$.

Dessine la ligne du temps : **où tombe le premier flux ?**

## 4.11 Annuités différées et perpétuités

### 4.11.1 Différées

Les versements commencent après $d$ périodes :

1.  Calculer $V_d$ avec les formules habituelles ;
2.  Actualiser : $V_0 = V_d\,(1+i)^{-d}$.

Deux étapes, une ligne du temps.

### 4.11.2 Perpétuités

Quand $n \to \infty$, $(1+i)^{-n} \to 0$ :

$$V_0 = \frac{A}{i}$$

Croissante au taux $g < i$ : $V_0 = \dfrac{A_1}{i - g}$ (Gordon-Shapiro)

**Exemple** : 1 000 € par an pour toujours, à 4 % → $1\,000 / 0{,}04 =$ **25 000 €**. Si $g \to i$, la valeur explose.

## 4.12 🧠 Vérifiez votre compréhension

> Un bien rapporte un loyer de **600 € par an**, pour toujours. Au taux de **3 %**, quel prix maximal payer aujourd’hui ?

$$V_0 = \frac{600}{0{,}03} = 20\,000\ €$$

> Une PME verse 2 000 € pendant 4 ans, mais **en début d’année**. Valeur actuelle ?

$$7\,091{,}90 \times 1{,}05 \approx 7\,446{,}50\ €$$

5 Séquence 6\
Cas pratique : constituer un capital
====================================

De la formule à la décision.

## 5.1 Le contexte

Une entreprise veut disposer de **500 000 €** dans **8 ans** pour remplacer son système d’information. Versements en **fin d’année**, placement à **3,5 %**.

Quel versement annuel prévoir ?

t = 0

 

A

t = 1

 

A

t = 2

…

A\
500 000 €

t = 8

Faire tracer la ligne du temps par les étudiants AVANT d’afficher la suite. Laisser 5 minutes en binôme pour poser l’équation.

## 5.2 Étape 1 — Inverser la formule

On cherche $A$ tel que $V_8 = 500\,000$ :

$$A = V_n \times \frac{i}{(1+i)^n - 1}$$

$$A = 500\,000 \times \frac{0{,}035}{1{,}035^8 - 1} = 500\,000 \times \frac{0{,}035}{0{,}316809}$$

≈ 55 238 € / an

✔️ **Contrôle** : $55\,238 \times \dfrac{1{,}035^8 - 1}{0{,}035} \approx 500\,000$ €. Tout modèle Excel doit avoir sa cellule de contrôle.

## 5.3 Étape 2 — Tester les variantes

| Scénario | Calcul | Résultat |
|----|----|---:|
| Référence (fin d’année, 3,5 %) | $500\,000 \times \frac{0{,}035}{1{,}035^8 - 1}$ | **55 238 €/an** |
| Versements en **début** d’année | $55\,238 / 1{,}035$ | **53 370 €/an** (− 1 868 €) |
| Taux limité à **2 %** | $500\,000 \times \frac{0{,}02}{1{,}02^8 - 1}$ | **58 255 €/an** (+ 3 017 €) |
| Versement imposé : **50 000 €** | $50\,000 \times \frac{1{,}035^8 - 1}{0{,}035}$ | **452 584 €** (manque 47 416 €) |

## 5.4 Cadre de décision

- **Si** l’objectif est un capital futur à date fixe → **inverser** la formule de valeur acquise pour trouver $A$.
- **Si** on peut verser en début de période → l’effort annuel est **divisé par** $(1+i)$.
- **Si** le taux baisse → l’effort augmente : prévoir une **marge de sécurité** sur le taux.
- **Si** le versement est imposé par la trésorerie → calculer $V_n$, comparer à l’objectif, combler l’écart (durée ou montant).
- **Si** un montant est retenu → le **contrôler** par la formule inverse avant de le présenter.

6 Séquence 7\
Synthèse
=============

Ce qu’il faut retenir.

## 6.1 Carte mentale du cours

#### → Capitalisation

$C_n = C_0(1+i)^n$

On multiplie par $(1+i)$ à chaque période.

#### ← Actualisation

$V_0 = V_n\,(1+i)^{-n}$

On divise par $(1+i)$ à chaque période.

#### % Taux

Proportionnel : $i_p = i_a/m$

Équivalent : $i_p = (1+i_a)^{1/m} - 1$

#### Σ Annuités

Fin : $V_0 = A\,\frac{1-(1+i)^{-n}}{i}$

Début : $\times (1+i)$ · Perpétuité : $A/i$

## 6.2 Les erreurs qui coûtent cher

### 6.2.1 Mathématiques

- Écrire $5$ au lieu de $0{,}05$.
- Mélanger taux mensuel et durée en années.
- Oublier les intérêts composés *(S2)*.
- Décaler les flux d’une période : ±1 dans l’exposant *(S5)*.
- Confondre proportionnel et équivalent *(S4)*.

### 6.2.2 Raisonnement

- Additionner des flux de dates différentes *(S3)*.
- Calculer sans tracer la ligne du temps.
- Ne pas vérifier la cohérence entre la périodicité du taux et celle des flux.

## 6.3 Cinq réflexes à acquérir

1.  ✏️ **Tracer la ligne du temps** avant toute formule.
2.  🔁 **Vérifier la cohérence** entre taux et périodicité des flux.
3.  📍 **Ramener à une date commune** avant de comparer.
4.  💬 **Interpréter** le résultat : que signifie ce montant pour la décision ?
5.  ✔️ **Contrôler** par la formule inverse.

# 7 Exercices

Du plus direct au plus ouvert.

## 7.1 Niveau 1 — Application directe

**1.1** — 15 000 € placés 6 ans à 3 % (composés). Valeur acquise ?

$C_6 = 15\,000 \times 1{,}03^6 \approx$ **17 911 €**

**1.2** — Quelle somme placer aujourd’hui pour obtenir 25 000 € dans 4 ans à 4,5 % ?

$V_0 = 25\,000 / 1{,}045^4 \approx$ **20 964 €**

**1.3** — Taux annuel effectif d’un taux mensuel de 0,8 % ?

$i_a = 1{,}008^{12} - 1 \approx$ **10,03 %** (et non 9,6 %, taux proportionnel)

## 7.2 Niveau 2 — Comparer trois placements

| Offre | Taux affiché | Capitalisation                                   |
|-------|-------------:|--------------------------------------------------|
| A     |        4,8 % | mensuelle, taux proportionnel (0,4 %/mois)       |
| B     |        4,7 % | annuelle                                         |
| C     |        4,6 % | trimestrielle, taux proportionnel (1,15 %/trim.) |

Quelle offre est la plus avantageuse ?

- A : $1{,}004^{12} - 1 \approx$ **4,91 %**
- B : **4,70 %**
- C : $1{,}0115^{4} - 1 \approx$ **4,67 %**

🏆 **A \> B \> C** — A l’emporte malgré un taux affiché inférieur à B, grâce à sa capitalisation mensuelle.

## 7.3 Niveau 3 — Plan d’épargne retraite

Un cadre de 35 ans verse **800 €/mois en fin de mois** pendant **30 ans**, à **3 % par an**.

1.  Taux mensuel équivalent ?
2.  Capital constitué à 65 ans ?
3.  Rente mensuelle sur 20 ans (même taux) ?
4.  Impact d’un taux de 4 % ?
5.  Recommandation en une phrase.

1.  $i_m = 1{,}03^{1/12} - 1 \approx 0{,}2466\,\%$

2.  $V_{360} = 800 \times \frac{1{,}002466^{360} - 1}{0{,}002466} \approx$ **462 970 €**

3.  $A = 462\,970 \times \frac{0{,}002466}{1 - 1{,}002466^{-240}} \approx$ **2 558 €/mois**

4.  $i_m \approx 0{,}3274\,\%$ → $V_{360} \approx$ **548 216 €** (+ 85 246 €)

5.  *Un point de rendement en plus sur 30 ans augmente le capital de près de 20 % : il est justifié d’arbitrer vers des supports plus dynamiques si le profil de risque le permet.*

8 Séquence 8\
Cas pratique de synthèse : six décisions réelles
================================================

2 heures, six dossiers réels, un seul outil : la ligne du temps.

Séance de 2 h en binômes. Chaque atelier mobilise une ou plusieurs séquences du module, à partir de produits et d’événements réels (Livret A, escompte fournisseur, crédit immobilier, EuroDreams, War Loan britannique, épargne retraite). Projeter la situation, laisser chercher, puis dévoiler la correction fragment par fragment. Les données de marché sont datées : les rappeler comme telles et inviter les étudiants à les actualiser.

## 8.1 Le dossier de Camille

Camille, **30 ans**, est graphiste indépendante. Elle a un peu d’épargne, une micro-entreprise qui achète du matériel, un projet d’achat immobilier… et elle joue de temps en temps à la loterie.

En un an, elle doit prendre **six décisions financières**. Toutes reposent sur la même question : *que vaut une somme d’argent, à quelle date ?*

Votre mission : l’aider à décider, chiffres à l’appui.

**Livrable par atelier** : ① la ligne du temps · ② la formule · ③ le résultat · ④ la décision en **une phrase**.

## 8.2 Organisation de la séance

|  | Dossier réel | Notions mobilisées | Durée |
|----|----|----|---:|
| — | Lancement, constitution des binômes |  | 5 min |
| 1 | Le Livret A | Intérêts simples et composés *(S2)* | 15 min |
| 2 | L’escompte fournisseur | Actualisation, taux équivalent *(S3, S4)* | 15 min |
| 3 | Le crédit immobilier | Taux proportionnel, TAEG, annuités *(S4, S5)* | 20 min |
| 4 | Le gain EuroDreams | Valeur actuelle d’une rente *(S4, S5)* | 20 min |
| 5 | Le War Loan britannique | Perpétuité *(S5)* | 15 min |
| 6 | La retraite de Camille | Annuité différée, constituer un capital *(S5, S6)* | 20 min |
| — | Débrief collectif |  | 10 min |

Calculatrice ou tableur autorisés. Toute réponse sans ligne du temps est considérée comme incomplète.

## 8.3 Atelier 1 — Le Livret A de Camille

Au **1^(er) janvier 2024**, Camille a **10 000 €** sur son Livret A, rémunéré **3 %** toute l’année 2024. Elle dépose **2 000 €** le **10 mars** et retire **1 000 €** le **20 septembre**.

Combien d’intérêts touchera-t-elle au 31 décembre 2024 ?

**Les règles réelles du Livret A** :

- les intérêts sont calculés **par quinzaine** (du 1^(er) au 15, du 16 à la fin du mois) ;
- un dépôt rapporte à partir du **1^(er) ou du 16 qui suit** ;
- un retrait cesse de rapporter à partir du **1^(er) ou du 16 qui précède** ;
- les intérêts sont versés le **31 décembre** puis **ajoutés au capital**.

Données réelles : taux de 3 % du 1^(er) février 2023 au 31 janvier 2025, puis 2,4 % au 1^(er) février 2025 et 1,7 % au 1^(er) août 2025.

Questions : (1) intérêts 2024 ; (2) solde au 1er janvier 2025 ; (3) intérêts 2025 sans mouvement, sachant les trois taux de 2025 ; (4) pourquoi parle-t-on d’intérêts simples dans l’année et composés d’une année sur l’autre ? (5) taux réel 2024, avec une inflation moyenne d’environ 2 % (Insee).

## 8.4 Atelier 1 — Correction

Taux par quinzaine : $3\,\% / 24 = 0{,}125\,\%$, en **intérêts simples** dans l’année.

| Mouvement | Date de valeur | Quinzaines | Intérêts 2024 |
|----|----|---:|---:|
| Solde initial 10 000 € | 1^(er) janvier | 24 | $10\,000 \times 3\,\% = 300{,}00$ € |
| Dépôt + 2 000 € | 16 mars | 19 | $2\,000 \times 3\,\% \times \frac{19}{24} = 47{,}50$ € |
| Retrait − 1 000 € | 16 septembre | 7 | $-1\,000 \times 3\,\% \times \frac{7}{24} = -8{,}75$ € |
| **Total** |  |  | **338,75 €** |

Solde au 1^(er) janvier 2025 : $11\,000 + 338{,}75 =$ **11 338,75 €**. En 2025 (3 % en janvier, 2,4 % de février à juillet, 1,7 % d’août à décembre), le taux moyen vaut $\frac{1 \times 3 + 6 \times 2{,}4 + 5 \times 1{,}7}{12} \approx 2{,}158\,\%$ :

$$11\,338{,}75 \times 2{,}158\,\% \approx 244{,}73\ € \quad \text{dont } 338{,}75 \times 2{,}158\,\% \approx \mathbf{7{,}31\ €}\ \text{d'intérêts sur intérêts}$$

✔️ **Simples** dans l’année, **composés** d’une année sur l’autre. Taux réel 2024 : $\frac{1{,}03}{1{,}02} - 1 \approx$ **0,98 %**. Le pouvoir d’achat n’a progressé que d’environ 1 %.

## 8.5 Atelier 2 — Payer comptant ou à 60 jours ?

L’atelier de Camille reçoit une facture fournisseur de **12 000 € HT**, payable à **60 jours**. La facture précise : *« Escompte de 2 % pour paiement comptant. »*

Sa trésorerie dort sur un Livret A à **2,4 %**. À défaut, elle peut utiliser son découvert autorisé à **8 % par an**.

Faut-il payer tout de suite 11 760 € ou 12 000 € dans 60 jours ?

11 760 €

t = 0\
comptant

60 jours

12 000 €

t = 60 j\
échéance

Cadre réel : délai de paiement plafonné à 60 jours après la date de facture (art. L441-10 du Code de commerce) ; les conditions d’escompte sont une mention obligatoire de la facture (art. L441-9).

## 8.6 Atelier 2 — Correction

**Taux implicite sur 60 jours**

$$r_{60} = \frac{12\,000}{11\,760} - 1 \approx 2{,}041\,\%$$

**Taux annuel équivalent** (base 365 j)

$$(1{,}020408)^{365/60} - 1 \approx \mathbf{13{,}08\,\%}$$

Le taux proportionnel donnerait 12,41 % : il sous-estime l’avantage.

**Vérification par actualisation**

Valeur actuelle de 12 000 € dans 60 jours :

- au Livret A (2,4 %) : $12\,000 \times 1{,}024^{-60/365} \approx 11\,953$ € ;
- au découvert (8 %) : $12\,000 \times 1{,}08^{-60/365} \approx 11\,849$ €.

Dans les deux cas, **plus que 11 760 €**.

2 % de remise pour 60 jours d’avance = un placement à **13 % par an**. On paie comptant.

Gain en payant comptant avec la trésorerie du Livret : environ 193 €. Même financé par découvert à 8 %, le gain reste d’environ 89 €. Ouvrir la discussion : pourquoi le fournisseur accepte-t-il de « payer » 13 % ? Il se finance, réduit son risque d’impayé et son besoin en fonds de roulement.

## 8.7 Atelier 3 — Le crédit immobilier

Camille emprunte **200 000 €** sur **20 ans** au **taux nominal de 3,20 %**, remboursables par **mensualités constantes** (fin de mois). Assurance : **50 €/mois**. Frais de dossier et de garantie : **3 000 €**. Revenus nets : **3 500 €/mois**.

Quelle mensualité ? Quel coût réel ? Le dossier passe-t-il ?

**Convention bancaire réelle** : taux mensuel = taux nominal / 12 (taux **proportionnel**).

**Règle du HCSF** : taux d’effort ≤ **35 %** (assurance comprise), durée ≤ **25 ans**.

Données réelles (Observatoire Crédit Logement/CSA, ordres de grandeur) : taux moyen ≈ 1,1 % fin 2021, ≈ 4,2 % fin 2023, ≈ 3,2 % en 2025.

## 8.8 Atelier 3 — Correction

**Mensualité** ($i_m = 0{,}032/12$, $n = 240$)

$$M = 200\,000 \times \frac{i_m}{1 - (1+i_m)^{-240}} \approx \mathbf{1\,129{,}33\ €}$$

**Coût des intérêts** : $1\,129{,}33 \times 240 - 200\,000 \approx$ **71 038 €**

**Taux d’effort** : $\frac{1\,129{,}33 + 50}{3\,500} \approx$ **33,7 %** ✔️

**Taux actuariel** (équivalent) du nominal : $\left(1 + \frac{0{,}032}{12}\right)^{12} - 1 \approx 3{,}25\,\%$

**TAEG** : on cherche le taux mensuel $x$ qui égalise ce que Camille *reçoit réellement* et ce qu’elle *paie* :

$$197\,000 = 1\,179{,}33 \times \frac{1 - (1+x)^{-240}}{x}$$

$x \approx 0{,}3217\,\%$ → TAEG $= (1+x)^{12} - 1 \approx$ **3,93 %**

Tableur : `=TAUX(240;-1179,33;197000)` puis on passe à l’année.

Nominal 3,20 % → actuariel 3,25 % → **TAEG 3,93 %**. Seul le TAEG permet de comparer deux offres : c’est pour cela que la loi impose de l’afficher.

## 8.9 Atelier 3 — Le choc des taux de 2022-2023

| Pour 200 000 € sur 20 ans                 | Fin 2021 (1,1 %) |  2025 (3,2 %) |
|-------------------------------------------|-----------------:|--------------:|
| Mensualité                                |         928,74 € |    1 129,33 € |
| Coût total des intérêts                   |         22 897 € |      71 038 € |
| Capacité d’emprunt avec **928,74 €/mois** |        200 000 € | **164 477 €** |

Capacité = valeur actuelle de la mensualité : $928{,}74 \times \frac{1 - (1+i_m)^{-240}}{i_m}$ avec $i_m = 0{,}032/12$.

Même budget mensuel, **18 % de pouvoir d’achat immobilier en moins**.

C’est exactement ce qu’ont vécu les acheteurs entre 2022 et 2023 : la capacité d’emprunt a fondu, les transactions ont chuté et les prix ont dû s’ajuster. Faire le lien avec S3 : quand le taux monte, la valeur actuelle d’un même flux baisse.

## 8.10 Simulateur de crédit 🎛️

``` js
viewof C_cp = Inputs.range([50000, 500000], {value: 200000, step: 5000, label: "Capital emprunté (€)"})
viewof t_cp = Inputs.range([0.005, 0.06], {value: 0.032, step: 0.001, label: "Taux nominal annuel"})
viewof n_cp = Inputs.range([10, 25], {value: 20, step: 1, label: "Durée (années)"})
```

``` js
im_cp = t_cp / 12
M_cp = C_cp * im_cp / (1 - (1 + im_cp) ** (-12 * n_cp))
ech_cp = {
  let crd = C_cp
  const rows = []
  for (let an = 1; an <= n_cp; an++) {
    let interets = 0, capital = 0
    for (let m = 0; m < 12; m++) {
      const it = crd * im_cp
      interets += it
      capital += M_cp - it
      crd -= M_cp - it
    }
    rows.push({an, part: "Capital remboursé", montant: capital},
              {an, part: "Intérêts", montant: interets})
  }
  return rows
}

Plot.plot({
  width: 900, height: 250, marginLeft: 70,
  color: {domain: ["Capital remboursé", "Intérêts"], range: ["#5b9bdb", "#db5b5b"], legend: true},
  x: {label: "Année →"},
  y: {label: "↑ Remboursé dans l'année (€)", grid: true, tickFormat: d => fmt(d)},
  marks: [
    Plot.barY(ech_cp, {x: "an", y: "montant", fill: "part", tip: true}),
    Plot.ruleY([0])
  ]
})
```

``` js
md`<div class="ojs-result">Mensualité : **${fmt(M_cp, 2)} €** · coût des intérêts : <span class="red">**${fmt(M_cp * 12 * n_cp - C_cp)} €**</span> · taux actuariel : **${pct((1 + im_cp) ** 12 - 1)}**</div>`
```

Faire observer : en début de crédit, l’essentiel de la mensualité paie des intérêts (rouge) ; la part de capital (bleu) grandit chaque année. Tester 25 ans contre 20 ans : la mensualité baisse, mais le coût total explose.

## 8.11 Atelier 4 — « Je suis multimillionnaire ! »

Le premier rang d’**EuroDreams** (FDJ, depuis novembre 2023) ne verse pas un capital mais une **rente : 20 000 € par mois pendant 30 ans**.

Un gagnant s’exclame : *« 20 000 × 360 = 7,2 millions d’euros, je suis multimillionnaire ! »*

Que vaut réellement ce gain aujourd’hui ?

**Hypothèses** : premier versement dans un mois (fin de période), taux d’actualisation de **3 % par an**.

V₀ ?

aujourd'hui

 

20 000

mois 1

 

20 000

mois 2

…

20 000

mois 360

Questions : (1) taux mensuel équivalent ; (2) valeur actuelle à 3 % ; (3) à 5 % ; (4) un intermédiaire propose 4 M€ comptant contre la rente : accepter ? (5) que change un premier versement immédiat ?

## 8.12 Atelier 4 — Correction

**Taux mensuel équivalent** : $i_m = 1{,}03^{1/12} - 1 \approx 0{,}2466\,\%$ (et non 3 %/12 = 0,25 %)

**À 3 %**

$$V_0 = 20\,000 \times \frac{1 - 1{,}03^{-30}}{0{,}002466} \approx \mathbf{4\,768\,442\ €}$$

soit 66 % du nominal

**À 5 %** ($i_m \approx 0{,}4074\,\%$)

$$V_0 \approx \mathbf{3\,773\,192\ €}$$

soit 52 % du nominal

**Offre de 4 M€ comptant** : à refuser si l’on place à 3 % (4,77 M€ \> 4 M€), à accepter si l’on sait placer à 5 % (3,77 M€ \< 4 M€). **C’est le taux d’actualisation qui tranche.**

Premier versement immédiat (terme à échoir) : $\times (1 + i_m)$ → **4 780 202 €** à 3 %. Avec le taux proportionnel (0,25 %), on trouverait 4 743 788 € : **près de 25 000 € d’erreur**.

## 8.13 Le même dilemme, version Powerball 🇺🇸

Octobre 2023, loterie américaine **Powerball** : jackpot affiché de **1,765 milliard de dollars**, versé en **30 annuités** (une immédiate, puis 29 annuelles) **croissant de 5 % par an**, ou **774,1 millions comptant**.

Pourquoi l’option « comptant » ne vaut-elle que 44 % du jackpot ?

1^(er) versement : $P_1 = \dfrac{1\,765}{\sum_{k=0}^{29} 1{,}05^k} = \dfrac{1\,765}{66{,}44} \approx 26{,}6$ M\$

Si l’on actualise à **5 %**, la croissance compense exactement l’actualisation : chaque versement vaut $P_1$ aujourd’hui, soit $30 \times 26{,}6 \approx 797$ M\$.

Le montant comptant correspond à un taux d’actualisation implicite d’environ **5,2 %**, proche des taux longs américains de l’époque. Le « jackpot » est une somme de flux de dates différentes, pas une valeur.

Slide bonus, à traiter si le temps le permet. Le taux implicite s’obtient numériquement (valeur cible ou solveur du tableur) : il n’y a pas de formule fermée pour isoler le taux.

## 8.14 Atelier 5 — Le prêt de guerre perpétuel

En **1917**, le Royaume-Uni émet le *5 % War Loan* pour financer la guerre. En **1932**, il est converti en **3½ % War Loan** : un titre **sans échéance** qui verse **3,50 £ par an** pour 100 £ de nominal, que l’État peut rembourser **au pair (100 £)** quand il le souhaite.

En **décembre 2014**, le Trésor britannique annonce son remboursement, effectif en **mars 2015**.

Pourquoi rembourser, presque un siècle plus tard ?

Questions : (1) valeur du titre, considéré comme une perpétuité, pour des taux de marché de 5 %, 3,5 %, 2,5 % et 2 % ; (2) intérêt de l’État à rembourser en 2015, quand les taux longs britanniques tournent autour de 2,5 % ; (3) point de vue du porteur ; (4) ce qu’a représenté la conversion de 1932 pour les porteurs.

## 8.15 Atelier 5 — Correction

$$V_0 = \frac{A}{i} = \frac{3{,}50}{i}$$

| Taux de marché $i$ | Valeur du titre |
|-------------------:|----------------:|
|                5 % |            70 £ |
|              3,5 % |           100 £ |
|              2,5 % |       **140 £** |
|                2 % |       **175 £** |

**L’État** rembourse 100 £ et se refinance vers 2,5 % : il paie 2,50 £ au lieu de 3,50 £ par an, soit **29 % d’intérêts en moins**.

**Le porteur** récupère 100 £ pour un flux qui en vaudrait 140 sans clause de remboursement : il a vendu une **option** à l’État.

**En 1932**, la conversion de 5 % à 3,5 % a réduit de **30 %** le revenu des porteurs.

Une perpétuité est **ultra-sensible au taux** : diviser $i$ par deux double sa valeur.

## 8.16 Atelier 6 — La retraite de Camille

Camille veut un **complément de 500 € par mois pendant 25 ans** à partir de **64 ans**. Elle épargne chaque mois sur un **plan d’épargne retraite** (fin de mois) de 30 à 64 ans. Rendement net : **3 % par an**.

Combien doit-elle verser chaque mois ? Et si elle attend 40 ans ?

début

30 ans

A / mois · 408 mois

capital V₆₄

64 ans

500 € / mois · 300 mois

fin

89 ans

Questions : (1) capital nécessaire à 64 ans ; (2) versement mensuel de 30 à 64 ans ; (3) versement si elle commence à 40 ans ; (4) somme unique à placer aujourd’hui (annuité différée) ; (5) avec 2 % d’inflation par an, que valent 500 € d’aujourd’hui dans 34 ans ? Insister : deux phases, deux formules, raccordées à la date pivot de 64 ans.

## 8.17 Atelier 6 — Correction

$i_m = 1{,}03^{1/12} - 1 \approx 0{,}2466\,\%$

**① Capital à 64 ans** (valeur actuelle de la rente)

$$V_{64} = 500 \times \frac{1 - 1{,}03^{-25}}{i_m} \approx \mathbf{105\,908\ €}$$

**② Versement de 30 à 64 ans** (408 mois)

$$A = 105\,908 \times \frac{i_m}{(1+i_m)^{408} - 1} \approx \mathbf{150{,}81\ €/\text{mois}}$$

Versé : 61 533 € · intérêts : 44 375 € (42 % du capital)

**③ Si elle commence à 40 ans** (288 mois)

$A \approx$ **252,90 €/mois** (+ 68 %), pour 72 836 € versés.

**④ Somme unique aujourd’hui** (annuité différée de 34 ans)

$105\,908 \times 1{,}03^{-34} \approx$ **38 767 €**

**⑤ Inflation à 2 %** : 500 € d’aujourd’hui = $500 \times 1{,}02^{34} \approx$ **980 €** à 64 ans. Pour préserver le pouvoir d’achat, il faudrait environ **207 650 €** de capital.

Dix ans de retard coûtent **68 % d’effort mensuel en plus** : le temps est le premier levier.

## 8.18 Débrief — Une méthode, six décisions

| Dossier | Question réelle | Outil clé | Décision |
|----|----|----|----|
| Livret A | Combien rapporte mon épargne ? | Intérêts simples par quinzaine, capitalisation annuelle | 338,75 € ; taux réel ≈ 1 % |
| Escompte | Payer maintenant ou plus tard ? | Actualisation, taux équivalent | Payer comptant (≈ 13 %/an) |
| Crédit | Que coûte vraiment mon prêt ? | Annuités, proportionnel → TAEG | 1 129,33 €/mois ; TAEG 3,93 % |
| EuroDreams | Que vaut une rente ? | Valeur actuelle, taux mensuel équivalent | ≈ 4,77 M€, pas 7,2 M€ |
| War Loan | Pourquoi rembourser ? | Perpétuité $A/i$ | Refinancer quand $i$ baisse |
| Retraite | Combien épargner ? | Annuité différée, inversion | 150,81 €/mois dès 30 ans |

Débrief de 10 minutes : faire présenter une décision par binôme, en une phrase, puis dégager les leçons de la diapositive suivante.

## 8.19 Ce que les cas réels nous apprennent

- 🧾 **Chaque produit a sa convention** (quinzaines, taux proportionnel, TAEG actuariel) : l’identifier avant de calculer.
- ⚖️ **Le taux d’actualisation tranche** : EuroDreams, Powerball et War Loan changent de valeur avec lui.
- 🔍 **Une petite remise peut cacher un gros taux** : toujours annualiser.
- ⏳ **Le temps est le levier le plus puissant** : commencer tôt divise l’effort.
- 📅 **Un montant nominal n’est pas une valeur** : 7,2 M€ ou 1,765 Md\$ sont des sommes de flux à des dates différentes.

Ligne du temps → date commune → formule → **décision**.

## 8.20 📖 Pour aller plus loin

Théorie complète, démonstrations, exemples et corrections détaillées :

[→ Module 1 : Valeur temps de l’argent](../module-01.qmd)

[→ Formulaire](../../../teaching/mathematical-finance/formulaire.llms.md) · [→ Glossaire](../../../teaching/mathematical-finance/glossaire.llms.md)

Un euro n’a de valeur qu’**à une date donnée**.

## Citation

BibTeX citation:

``` quarto-appendix-bibtex
@online{gilles,
  author = {Gilles, Guillaume},
  title = {Valeur Temps de l’argent},
  url = {https://ggilles.dev/teaching/mathematical-finance/slides/module-01.html},
  langid = {en}
}
```

For attribution, please cite this work as:

Gilles, Guillaume. n.d. “Valeur Temps de l’argent.” <https://ggilles.dev/teaching/mathematical-finance/slides/module-01.html>.
