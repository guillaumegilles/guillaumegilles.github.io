## Introduction et diagnostic

### Intuition économique

Choisissez une option, sans calculer, et justifiez votre choix :

- **Option A** : recevoir **10 000 €** aujourd’hui
- **Option B** : recevoir **11 000 €** dans un an
- **Option C** : recevoir **12 500 €** dans deux ans

Ce choix simple fait émerger les concepts qui structurent toute la finance :

> Pourquoi un euro aujourd’hui vaut-il plus qu’un euro demain ?

Quatre raisons fondamentales :

1.  **Préférence pour le présent :** nous préférons disposer d’une somme maintenant plutôt que de l’attendre.
2.  **Coût d’opportunité :** 10 000 € aujourd’hui peuvent être placés et produire des intérêts.
3.  **Inflation :** 11 000 € dans un an achèteront peut-être moins que 10 000 € aujourd’hui si les prix augmentent.
4.  **Risque :** une somme future est incertaine ; une somme présente est certaine.

Ces quatre raisons se condensent en un seul paramètre : le **taux d’actualisation**.

Toute la finance repose sur une idée simple mais fondamentale : **un euro aujourd’hui vaut plus qu’un euro demain**. Comprendre cette notion de *valeur temps de l’argent*, c’est comprendre pourquoi on ne compare jamais directement des montants situés à des dates différentes. Il faut d’abord les ramener à une date commune. C’est le fondement de toutes les décisions financières, de l’épargne à l’investissement en passant par le crédit.

## Intérêts simples et intérêts composés

> **IMPORTANT:**
>
> Un placement est à **intérêts simples** lorsque les intérêts de chaque période sont calculés sur le seul capital initial \\C_0\\. Il est à **intérêts composés** lorsque les intérêts de chaque période sont ajoutés au capital et portent eux-mêmes intérêt aux périodes suivantes (capital courant \\C\_{t-1}\\).

Léa vient de recevoir une prime de **10 000 €** dont elle n’aura pas besoin avant **10 ans**. Sa banque lui propose deux placements au même taux de **3 % par an**. Le livret « Simple » verse chaque année 3 % de la somme de départ, soit 300 €, que Léa garde de côté sans les replacer. Le compte à terme « Cumul » ajoute chaque année les intérêts au capital, si bien que l’année suivante les 3 % portent sur un montant plus élevé. Le conseiller assure que « c’est le même taux, donc à peu près le même résultat ».

**Quelle offre Léa doit-elle choisir, et quel écart cela représente-t-il au bout de 10 ans ?**

### Exploration numérique

Suivons les deux placements année par année. Avec le livret « Simple », Léa reçoit toujours 300 € (3 % de 10 000 €) : on **ajoute** 300 € chaque année. Avec le compte « Cumul », on **multiplie** chaque année le solde de l’année précédente par 1,03 : la première année, 10 000 × 1,03 = 10 300 € ; la deuxième, 10 300 × 1,03 = 10 609 € ; et ainsi de suite.

| Année | « Simple » (€) | « Cumul » (€) | Écart (€) |
|------:|---------------:|--------------:|----------:|
|     0 |         10 000 |        10 000 |         0 |
|     1 |         10 300 |        10 300 |         0 |
|     2 |         10 600 |        10 609 |         9 |
|     3 |         10 900 |        10 927 |        27 |
|     4 |         11 200 |        11 255 |        55 |
|     5 |         11 500 |        11 593 |        93 |
|     6 |         11 800 |        11 941 |       141 |
|     7 |         12 100 |        12 299 |       199 |
|     8 |         12 400 |        12 668 |       268 |
|     9 |         12 700 |        13 048 |       348 |
|    10 |         13 000 |        13 439 |       439 |

*Valeurs arrondies à l’euro.*

#### Réponse à Léa

Au bout de 10 ans, le compte « Cumul » lui rapporte **13 439 €** contre **13 000 €** pour le livret « Simple », soit **439 €** de plus. Le conseiller se trompe : même taux ne veut pas dire même résultat. Léa a intérêt à choisir « Cumul », et l’écart se creuse d’année en année.

- La colonne « Simple » augmente toujours du **même montant** (+300 €) : on part de 10 000 € et on ajoute \\t\\ fois 300 €, soit \\10\\000 \times (1 + t \times 0{,}03)\\.
- La colonne « Cumul » est multipliée chaque année par le **même facteur** (× 1,03) : après \\t\\ années, on a multiplié \\t\\ fois par 1,03, soit \\10\\000 \times 1{,}03^t\\.
- L’écart grandit de plus en plus vite : chaque année, les intérêts déjà gagnés **produisent à leur tour des intérêts**.

#### Visualisation des intérêts « simples » et « cumulés »

``` js
viewof C0_s2 = Inputs.range([1000, 50000], {
  value: 10000, step: 500,
  label: "Capital initial C₀ (€)"
})
viewof i_s2 = Inputs.range([0.01, 0.15], {
  value: 0.03, step: 0.005,
  label: "Taux d'intérêt i (par période)"
})
viewof n_s2 = Inputs.range([2, 30], {
  value: 10, step: 1,
  label: "Durée maximale n (périodes)"
})

data_s2 = Array.from({length: n_s2 + 1}, (_, t) => [
  {t, valeur: C0_s2 * (1 + i_s2 * t), serie: "Intérêts simples"},
  {t, valeur: C0_s2 * (1 + i_s2) ** t, serie: "Intérêts composés"}
]).flat()

Plot.plot({
  title: "Simple (linéaire) vs composé (exponentiel)",
  marks: [
    Plot.line(data_s2, {x: "t", y: "valeur", stroke: "serie", tip: true}),
    Plot.dot(data_s2, {x: "t", y: "valeur", fill: "serie", tip: true}),
    Plot.ruleY([C0_s2], {stroke: "gray", strokeDasharray: "4", label: "C₀"})
  ],
  color: {legend: true},
  x: {label: "Période t", tickFormat: d => `t=${d}`},
  y: {label: "Capital (€)", grid: true},
  marginBottom: 40
})
```

### Intérêts simples

En intérêts simples, les intérêts sont calculés **uniquement sur le capital initial**, à chaque période, sans jamais être réinvestis. Si vous placez 10 000 € à 3 % par an, vous touchez 300 € chaque année et ce sera toujours 300 € dix ans plus tard, quelle que soit la durée. La formule est linéaire : \\C_n = C_0(1 + ni)\\. Ce régime est intuitif mais peu réaliste sur le long terme : il revient à garder les intérêts « de côté » sans qu’ils ne travaillent eux-mêmes, ce qui sous-estime le véritable rendement d’un placement.

Prenons quelques valeurs abstraites :

- \\C_0\\ : le capital initial ;
- \\n\\ : le nombre de périodes ;
- \\i\\ : le taux d’intérêt.

#### À la fin de la période 1

les intérêts valent \\C_0 \cdot i\\, on les ajoute au capital :

\\C_1 = C_0 + C_0 \cdot i\\ \\C_1 = C_0(1 + i)\\

#### À la fin de la période 2

les intérêts sont à nouveau calculés sur le seul capital initial, donc toujours \\C_0 \cdot i\\ :

\\C_2 = C_1 + C_0 \cdot i\\ \\C_2 = C_0(1 + i) + C_0 \cdot i\\ \\C_2 = C_0(1 + 2i)\\

#### À la fin de la période \\n\\

**Le point clé :** en intérêts simples, on ajoute **toujours le même montant** \\C_0 \cdot i\\ à chaque période, car la base de calcul reste le capital initial \\C_0\\ (et non le capital courant \\C\_{t-1}\\ comme en intérêts composés).

\\C_n = C_0 + \underbrace{C_0 \cdot i + C_0 \cdot i + \cdots + C_0 \cdot i}\_{n \text{ fois}}\\ \\C_n = C_0 + n \cdot C_0 \cdot i\\ \\\boxed{C_n = C_0(1 + ni)}\\

#### Total des intérêts simple générés

On peut déterminer rapidement ce que le placement rapporte, au-delà du capital. avec quelques valeurs abstraites :

- \\I\\ : le total des intérêts perçus, de même montant à chaque période ;
- \\C_0\\ : la somme placée au départ, seule base de calcul des intérêts ;
- \\n\\ : le nombre de périodes pendant lesquelles l’argent reste placé ;
- \\i\\ : le taux d’intérêt par période, exprimé en décimal (0,03 pour 3 %).

\\I = C_n - C_0\\ \\I = C_0(1 + ni) - C_0\\ \\\boxed{I = C_0 \\ n \\ i}\\

### Intérêts composés

Les intérêts composés changent la donne : à chaque période, les intérêts sont **ajoutés au capital** et produisent eux-mêmes des intérêts pour les périodes suivantes. C’est l’effet « boule de neige » ou « intérêts sur intérêts ». La formule devient exponentielle : \\C_n = C_0(1+i)^n\\. Avec 10 000 € à 3 % sur 10 ans, on obtient 13 439 € en composé contre 13 000 € en simple. Cet écart peut sembler modeste, mais il s’amplifie considérablement avec la durée et le taux : c’est pourquoi commencer à épargner tôt est si puissant.

#### À la fin de la période 1

\\C_1 = C_0 + C_0 \cdot i\\ \\C_1 = C_0(1+i)\\

#### À la fin de la période 2

\\C_2 = C_1(1+i)\\ \\C_2 = C_0(1+i) \cdot (1+i)\\ \\C_2 = C_0(1+i)^2\\

#### À la fin de la période \\n\\

La clé est que la base de calcul des intérêts est le *capital courant* \\C\_{t-1}\\ etnon le capital initial, d’où l’exposant \\n\\.

\\C_n = C_0 \underbrace{(1+i) \cdot (1+i) \cdot \dots \cdot (1+i)}\_{\text{\$n\$ fois}}\\ \\\boxed{C_n = C_0(1+i)^n}\\

#### Total des intérêts composés générés

À chaque période, les intérêts s’ajoutent au capital et produisent eux-mêmes des intérêts lors des périodes suivantes. C’est l’effet des **intérêts composés** (ou « intérêts sur intérêts »).

**Intérêts produits :** \\I = C_0\left\[(1+i)^n - 1\right\]\\

> **WARNING:**
>
> Pour une même durée \\n\\ et un même taux \\i\\ :
>
> - **Pour \\n \< 1\\** (fraction d’année) : les intérêts simples donnent un montant *supérieur* aux intérêts composés.
> - **Pour \\n \> 1\\** : les intérêts composés donnent toujours un montant *supérieur*.
> - L’écart s’amplifie avec le taux et la durée.

### Exemple résolu

> Un capital de **20 000 €** est placé pendant **5 ans** au taux annuel de **4 %**.

**Intérêts simples :**

\\C_5 = 20\\000 \times (1 + 5 \times 0{,}04) = 20\\000 \times 1{,}20 = 24\\000 \text{ €}\\

**Intérêts composés :**

\\C_5 = 20\\000 \times (1{,}04)^5 = 20\\000 \times 1{,}21665 \approx 24\\333 \text{ €}\\

L’écart (333 €) représente les intérêts générés par les intérêts capitalisés.

> **NOTE:**
>
> Les intérêts composés récompensent la **patience** : plus l’argent reste placé longtemps, plus les intérêts sur intérêts pèsent dans le résultat. Si la durée double, l’écart fait bien plus que doubler : sur 20 ans à 3 %, les 10 000 € de Léa deviendraient 18 061 € en composé contre 16 000 € en simple, soit un écart d’environ 2 061 € (contre 439 € sur 10 ans). Pour un épargnant, il faut donc privilégier la capitalisation et commencer tôt ; pour un emprunteur, la même mécanique joue contre lui : une dette dont les intérêts ne sont pas payés grossit de plus en plus vite.

> **WARNING:**
>
> **L’intuition piège** : « 3 % par an pendant 10 ans, cela fait 30 % de gain, quel que soit le placement. »
>
> **Pourquoi c’est faux** : ce calcul additionne les taux, ce qui n’est vrai qu’en intérêts simples ; en intérêts composés, chaque année les 3 % portent sur un capital déjà augmenté des intérêts passés.
>
> **Le bon raisonnement** : en composé, on multiplie le capital par 1,03 chaque année, soit 1,03 puissance 10 ≈ 1,344 au bout de 10 ans, donc un gain de 34,4 % et non 30 %.
>
> **Astuce mémo** : en composé, on multiplie, on n’additionne pas.

> **IMPORTANT:**
>
> Avant d’appliquer une formule, vérifiez systématiquement :
>
> 1.  Le **taux exprimé** (\\i\\ en décimal, pas en pourcentage : \\0{,}04\\ et non \\4\\)
> 2.  La **durée** \\n\\ (en nombre de *périodes*, pas nécessairement en années)
> 3.  La **périodicité de calcul** (mensuelle, trimestrielle, annuelle…)
> 4.  La **fréquence de capitalisation** (combien de fois par an les intérêts sont-ils capitalisés ?)

## Actualisation et équivalence financière

> **NOTE:**
>
> Un client doit vous régler une facture et vous propose deux options : **1 000 € aujourd’hui** ou **1 100 € dans un an**. Les 100 € de plus sont tentants, mais il faut attendre. De votre côté, vous pouvez placer votre trésorerie sans risque à **5 % par an**. Le montant le plus élevé n’est donc pas forcément le meilleur : tout dépend de ce que vous pourriez faire de l’argent entre-temps.
>
> **Quelle offre devez-vous accepter ?**

### Intuition économique

Si la capitalisation répond à « combien vaut un capital *dans le futur* ? », l’actualisation répond à « combien vaut un capital futur *aujourd’hui* ? »

La **capitalisation** est donc l’opération qui projette un capital vers l’avenir : on multiplie le capital par \\(1+i)\\ autant de fois qu’il y a de périodes. C’est le mouvement naturel de l’épargne — chaque euro placé aujourd’hui grossit avec le temps — et le cœur de la constitution d’un capital, que ce soit pour un projet immobilier ou pour la retraite.

### Exploration numérique

*Règle d’or : tracez d’abord la ligne du temps (voir [Règle d’or](#rule-ligne-temps)).*

Les deux montants ne sont pas disponibles à la même date : pour les comparer, il faut les placer sur la même date. On peut le faire de deux façons.

**Façon 1 — Avancer dans le temps (dans un an).** Si vous acceptez 1 000 € aujourd’hui et les placez à 5 % :

\\1\\000 \times 1{,}05 = 1\\050 \text{ € dans un an}\\

1 050 € \< 1 100 € : attendre le paiement du client rapporte 50 € de plus.

**Façon 2 — Reculer dans le temps (aujourd’hui).** Quelle somme faudrait-il placer aujourd’hui à 5 % pour obtenir 1 100 € dans un an ? On fait le chemin inverse, en divisant au lieu de multiplier :

\\1\\100 \div 1{,}05 \approx 1\\047{,}62 \text{ € aujourd'hui}\\

1 047,62 € \> 1 000 € : la promesse de 1 100 € vaut davantage, aujourd’hui, que les 1 000 € proposés.

| Comparaison | 1 000 € aujourd’hui | 1 100 € dans un an | Meilleure offre |
|----|---:|---:|----|
| À la date 1 (capitaliser) | 1 050,00 € | 1 100,00 € | 1 100 € dans un an |
| À la date 0 (actualiser) | 1 000,00 € | 1 047,62 € | 1 100 € dans un an |

**Réponse :** les deux méthodes donnent la même conclusion — il faut **accepter 1 100 € dans un an**. Attention, ce résultat dépend du taux : il faudrait un placement à plus de 10 % (1 100 / 1 000 = 1,10) pour que les 1 000 € immédiats deviennent préférables.

> **TIP:**
>
> - Avancer d’un an, c’est **multiplier** par 1,05 ; reculer d’un an, c’est **diviser** par 1,05 : l’actualisation est l’opération inverse de la capitalisation.
> - Si les 1 100 € étaient versés dans **deux** ans, il faudrait reculer deux fois : \\1\\100 \div 1{,}05 \div 1{,}05 = 1\\100 / 1{,}05^2 \approx 997{,}73\\ €, et l’offre deviendrait moins intéressante que 1 000 € aujourd’hui.
> - Plus généralement, ramener aujourd’hui une somme \\V_n\\ disponible dans \\n\\ années revient à diviser \\n\\ fois par \\(1+i)\\ : diviser par \\(1+i)^n\\, c’est **remonter le temps**.

### Représentation (ligne du temps)

``` mermaid
flowchart RL
    t0["t = 0<br/>V₀<br/>(valeur actuelle)"]
    t1["t = 1"]
    tn["t = n<br/>Vₙ<br/>(valeur future)"]
    tn -->|"/ (1+i)"| t1
    t1 -->|"/ (1+i)"| t0
```

### A. Valeur actuelle

> **TIP:**
>
> \\V_0 = \frac{V_n}{(1+i)^n} = V_n \cdot (1+i)^{-n}\\
>
> **Facteur d’actualisation :** \\a_n = (1+i)^{-n}\\
>
> **Lecture :** \\V_0\\ est la valeur *aujourd’hui* d’une somme \\V_n\\ disponible dans \\n\\ périodes. Le facteur \\(1+i)^{-n}\\ est toujours inférieur à 1 : une somme future vaut moins aujourd’hui.

> **NOTE:**
>
> **Ce que calcule cette formule** : ce que vaut aujourd’hui une somme qui ne sera disponible que dans `n` périodes.
>
> **Rôle de chaque paramètre** :
>
> - `V_0` : la valeur actuelle, c’est-à-dire la somme qu’il faudrait placer aujourd’hui pour obtenir `V_n` à l’échéance.
> - `V_n` : le montant futur, encaissé ou payé à la date `n`.
> - `i` : le taux d’actualisation par période, qui mesure le coût d’opportunité de l’attente.
> - `n` : le nombre de périodes qui séparent aujourd’hui de la date du flux.
> - `a_n` : le facteur d’actualisation, inférieur à 1, par lequel on multiplie `V_n` pour obtenir `V_0`.
>
> **Ce que signifie le résultat** : `V_0` est le prix équitable aujourd’hui d’un flux futur ; dans la situation concrète, 1 100 € dans un an valent environ 1 047,62 € aujourd’hui au taux de 5 %.
>
> **Intuition directionnelle** : si le taux `i` ou la durée `n` augmente, la valeur actuelle `V_0` diminue, car l’attente coûte plus cher.

L’**actualisation** est l’opération inverse de la capitalisation : au lieu de faire voyager l’argent vers le futur, on le ramène vers le présent. « Que vaut aujourd’hui une promesse de 1 100 € dans un an, si je peux placer à 5 % ? » On divise alors par \\(1+i)^n\\ : \\V_0 = V_n / (1+i)^n\\. Le facteur \\(1+i)^{-n}\\, toujours inférieur à 1, traduit l’idée que l’attente a un coût. L’actualisation est l’outil indispensable pour comparer des offres de paiement échelonné, valoriser un projet d’investissement ou calculer le prix « juste » d’un actif financier.

### B. Équivalence financière

> **NOTE:**
>
> Deux capitaux sont **financièrement équivalents** s’ils ont la même valeur actualisée à une date de référence commune, au même taux.
>
> Pour comparer \\C_1\\ versé à la date \\n_1\\ et \\C_2\\ versé à la date \\n_2\\, on les ramène tous deux à une date commune (souvent \\t = 0\\).

Deux capitaux sont **financièrement équivalents** lorsqu’ils ont la même valeur à une date commune, au même taux. Dire que 1 000 € aujourd’hui équivaut à 1 050 € dans un an à 5 %, c’est exactement la même chose que de dire que 1 050 € dans un an actualisés valent 1 000 € aujourd’hui. Ce concept permet de remplacer un flux futur par un flux présent (ou l’inverse) sans changer la richesse : c’est la base de tous les arbitrages financiers, qu’il s’agisse de choisir entre payer comptant ou à crédit, ou d’accepter un paiement immédiat ou différé.

### Exemple résolu — Décision d’arbitrage

> Une entreprise doit choisir entre :
>
> - payer **48 000 €** immédiatement ;
> - payer **52 000 €** dans deux ans.
>
> Le taux d’actualisation est **5 %**.

**Valeur actuelle du paiement différé :**

\\VA = \frac{52\\000}{(1{,}05)^2} = \frac{52\\000}{1{,}1025} \approx 47\\166 \text{ €}\\

\\47\\166 \< 48\\000\\ : le paiement différé a une valeur actuelle *inférieure*. Toutes choses égales par ailleurs, il est financièrement préférable.

> **NOTE:**
>
> Le taux d’actualisation mesure ce que l’argent pourrait rapporter ailleurs : c’est le **coût d’opportunité** de l’attente. Si ce taux augmente, la valeur actuelle des sommes futures baisse, et les paiements immédiats deviennent relativement plus attractifs : avec un placement à plus de 10 %, il faudrait, dans la situation concrète, préférer les 1 000 € immédiats. Pour décider (encaisser tôt ou tard, payer comptant ou à crédit), un gestionnaire ramène donc toujours les flux à une même date, au taux qui reflète son propre coût de l’argent.

> **WARNING:**
>
> **L’intuition piège** : « 1 100 € dans un an, c’est plus que 1 000 € aujourd’hui, donc c’est forcément mieux. »
>
> **Pourquoi c’est faux** : on compare deux montants qui ne sont pas exprimés à la même date ; un euro disponible aujourd’hui peut être placé et vaut donc plus qu’un euro futur.
>
> **Le bon raisonnement** : ramener les deux montants à une date commune (actualiser 1 100 € à aujourd’hui ou capitaliser 1 000 € dans un an) avant de les comparer.
>
> **Astuce mémo** : on ne compare et on n’additionne que des euros de même date.

> **WARNING:**
>
> Le choix du taux \\i\\ reflète :
>
> - le **coût du capital** (le rendement minimum exigé par les investisseurs) ;
> - le **risque** (un projet risqué exige un taux plus élevé) ;
> - l’**inflation** attendue ;
> - la **liquidité** requise.
>
> Un taux plus élevé pénalise davantage les flux éloignés dans le temps.

### Démonstration interactive — Capitalisation vs Actualisation

``` js
viewof C0_s3 = Inputs.range([100, 20000], {
  value: 1000, step: 100,
  label: "Capital initial C₀ (€)"
})
viewof i_s3 = Inputs.range([0.01, 0.20], {
  value: 0.05, step: 0.001,
  label: "Taux d'intérêt i (annuel)"
})
viewof n_s3 = Inputs.range([1, 20], {
  value: 1, step: 1,
  label: "Nombre de périodes n"
})

data_s3 = Array.from({length: n_s3 + 1}, (_, t) => [
  {t, valeur: C0_s3 * (1 + i_s3) ** t,                          serie: "Capitalisation (Cₙ)"},
  {t, valeur: C0_s3 * (1 + i_s3) ** n_s3 / (1 + i_s3) ** (n_s3 - t), serie: "Actualisation (V₀)"}
]).flat()

Plot.plot({
  title: "Valeur du capital selon la perspective choisie",
  marks: [
    Plot.barY(data_s3, Plot.groupX({y: "first"}, {
      x: "t", y: "valeur", fill: "serie",
      tip: true
    })),
    Plot.ruleY([C0_s3], {stroke: "gray", strokeDasharray: "4",
      label: "C₀"}),
    Plot.ruleY([0])
  ],
  color: {legend: true},
  x: {label: "Période t", tickFormat: d => `t=${d}`},
  y: {label: "Valeur (€)", grid: true},
  marginBottom: 40
})
```

> **NOTE:**
>
> - La barre **bleue** (Capitalisation) montre \\C_n = C_0(1+i)^t\\ : le capital *croit* avec le temps.
> - La barre **orange** (Actualisation) montre \\V_0 = C_n / (1+i)^{n-t}\\ : vue depuis la date \\n\\, la valeur *actuelle* d’un flux futur *décroît* plus on s’éloigne dans le temps.
> - La ligne pointillée indique \\C_0\\ de départ.
>
> Choix technique (T-IV) : OJS, car il s’agit d’arithmétique pure et la réponse est instantanée.

------------------------------------------------------------------------

## Séquence 4 — Taux proportionnels et taux équivalents

> *Durée : 1 heure*

> **NOTE:**
>
> Vous financez un véhicule utilitaire de **10 000 €** remboursable en une seule fois au bout d’un an. L’organisme A affiche un taux de **9 % par an**, les intérêts étant calculés une seule fois, en fin d’année. L’organisme B affiche **0,75 % par mois**, les intérêts étant ajoutés à la dette chaque mois. Le commercial de B vous rassure : « 0,75 % fois 12, cela fait 9 %, c’est exactement la même chose ».
>
> **Ces deux offres vous coûteront-elles vraiment le même montant ?**

### Intuition économique

Un même taux peut s’exprimer sur des périodicités différentes (mensuelle, trimestrielle, annuelle…). Deux conventions existent, avec des implications très différentes.

### Exploration numérique

*Règle d’or : tracez d’abord la ligne du temps (voir [Règle d’or](#rule-ligne-temps)).*

Suivons la dette chez l’organisme B mois par mois. Chaque mois, on ajoute 0,75 % à la dette : on la **multiplie par 1,0075**. Le premier mois, les intérêts valent 10 000 × 0,0075 = 75 € ; le deuxième, ils portent sur 10 075 € et valent déjà 75,56 €. À titre de comparaison, la dernière colonne indique la dette si l’on ajoutait seulement 75 € par mois, sans intérêts sur les intérêts (c’est ce qu’affirme le commercial).

| Mois | Dette chez B, intérêts capitalisés (€) | Dette si +75 € par mois (€) |
|-----:|---------------------------------------:|----------------------------:|
|    0 |                              10 000,00 |                      10 000 |
|    1 |                              10 075,00 |                      10 075 |
|    2 |                              10 150,56 |                      10 150 |
|    3 |                              10 226,69 |                      10 225 |
|    4 |                              10 303,39 |                      10 300 |
|    5 |                              10 380,67 |                      10 375 |
|    6 |                              10 458,52 |                      10 450 |
|    7 |                              10 536,96 |                      10 525 |
|    8 |                              10 615,99 |                      10 600 |
|    9 |                              10 695,61 |                      10 675 |
|   10 |                              10 775,83 |                      10 750 |
|   11 |                              10 856,64 |                      10 825 |
|   12 |                              10 938,07 |                      10 900 |

Le douzième mois, les intérêts atteignent 81,42 € (contre 75 € le premier mois), car ils portent sur une dette déjà gonflée des intérêts précédents.

**Réponse :** au bout d’un an, vous devrez **10 938,07 €** à l’organisme B, contre **10 900 €** à l’organisme A. L’offre B coûte environ **38 € de plus** : les deux offres ne sont pas équivalentes. En réalité, 0,75 % par mois correspond à un coût annuel de 938,07 / 10 000 ≈ **9,38 %**, et non 9 %.

> **TIP:**
>
> - Multiplier 12 fois par 1,0075 revient à multiplier par \\1{,}0075^{12} \approx 1{,}0938\\ : le taux annuel réellement subi est \\1{,}0075^{12} - 1 \approx 9{,}38\\\\\\.
> - Multiplier 0,75 % par 12 (le calcul du commercial) donne 9 % : cela correspond à la colonne « +75 € par mois », qui **oublie** les intérêts sur les intérêts.
> - Pour qu’un taux mensuel \\i_m\\ donne *exactement* 9 % sur un an, il faudrait donc \\(1 + i_m)^{12} = 1{,}09\\, c’est-à-dire \\i_m = 1{,}09^{1/12} - 1 \approx 0{,}721\\\\\\ : on prend la **racine douzième**, on ne divise pas par 12.
>
> La division par 12 définit le taux *proportionnel* ; la racine définit le taux *équivalent*. Ce sont les deux conventions formalisées ci-dessous.

### A. Taux proportionnel

> **NOTE:**
>
> Le taux mensuel **proportionnel** au taux annuel \\i_a\\ est :
>
> \\i_m = \frac{i_a}{12}\\
>
> **Logique :** on divise simplement le taux annuel par le nombre de périodes. Cette convention *ignore* la capitalisation infra-annuelle.

> **NOTE:**
>
> **Ce que calcule cette formule** : un taux mensuel obtenu en divisant simplement le taux annuel par 12.
>
> **Rôle de chaque paramètre** :
>
> - `i_m` : le taux mensuel proportionnel, appliqué chaque mois.
> - `i_a` : le taux annuel affiché par le prêteur ou la banque.
> - `12` : le nombre de mois dans l’année, par lequel on divise le taux annuel.
>
> **Ce que signifie le résultat** : `i_m` est un taux de convention qui ne redonne le taux annuel affiché que si les intérêts mensuels ne sont pas capitalisés (0,75 % par mois pour 9 % par an).
>
> **Intuition directionnelle** : si le taux annuel `i_a` augmente, `i_m` augmente dans la même proportion, mais l’écart avec le coût réel des intérêts capitalisés chaque mois se creuse aussi.

Lorsqu’un taux annuel de 9 % est « converti » en mensuel en divisant simplement par 12 (soit 0,75 % par mois), on obtient un **taux proportionnel**. Cette convention est linéaire et intuitive, mais elle a un défaut majeur : elle ignore que les intérêts mensuels, une fois capitalisés, produisent eux-mêmes des intérêts. En réalité, 0,75 % par mois capitalisé sur 12 mois donne un coût annuel de 9,38 %, et non 9 %. Le taux proportionnel n’est donc qu’une approximation, utilisée surtout pour des durées inférieures à un an ou dans des conventions simplifiées.

### B. Taux équivalent

> **TIP:**
>
> Le taux mensuel **équivalent** au taux annuel \\i_a\\ vérifie :
>
> \\(1 + i_m)^{12} = 1 + i_a\\
>
> Donc :
>
> \\i_m = (1 + i_a)^{1/12} - 1\\
>
> De façon générale, pour \\m\\ sous-périodes par an :
>
> \\i_p = (1 + i_a)^{1/m} - 1\\
>
> **Lecture :** placer au taux mensuel équivalent pendant 12 mois donne *exactement* le même résultat que placer au taux annuel \\i_a\\ pendant 1 an.

> **NOTE:**
>
> **Ce que calcule cette formule** : le taux par sous-période qui, capitalisé sur toute l’année, donne exactement le même résultat que le taux annuel.
>
> **Rôle de chaque paramètre** :
>
> - `i_m` : le taux mensuel équivalent, appliqué et capitalisé chaque mois.
> - `i_a` : le taux annuel de référence que l’on veut reproduire.
> - `i_p` : le taux équivalent pour une sous-période quelconque (mois, trimestre, semestre).
> - `m` : le nombre de sous-périodes dans l’année, qui vaut 12 dans les deux premières égalités (mois) et 4 pour des trimestres.
>
> **Ce que signifie le résultat** : `i_p` est le seul taux par sous-période qui rend deux offres réellement comparables, puisque 9 % par an équivaut à environ 0,721 % par mois, et non 0,75 %.
>
> **Intuition directionnelle** : si le nombre de sous-périodes `m` augmente, le taux équivalent `i_p` devient un peu plus petit que la simple division par `m`, car des intérêts capitalisés plus souvent produisent davantage d’intérêts.

Le **taux équivalent** est le seul qui permette une comparaison honnête entre des offres exprimées sur des périodicités différentes. Il répond à la question : « quel taux mensuel, capitalisé chaque mois, donne exactement le même résultat qu’un taux annuel de 9 % sur un an ? » La réponse s’obtient en prenant la racine douzième : \\i_m = (1+i_a)^{1/12} - 1\\, soit environ 0,721 % pour 9 % annuel. Deux taux sont équivalents quand \\(1+i_p)^m = 1+i_a\\ : c’est la définition même de l’équivalence actuarielle, et c’est toujours le taux équivalent qu’il faut utiliser pour comparer des prêts ou des placements réels.

> **CAUTION:**
>
> On cherche \\i_p\\ tel que placer \\C_0\\ pendant \\m\\ sous-périodes au taux \\i_p\\ donne le même résultat que placer \\C_0\\ pendant 1 an au taux \\i_a\\ :
>
> \\C_0(1 + i_p)^m = C_0(1 + i_a)\\
>
> \\\Rightarrow \quad i_p = (1 + i_a)^{1/m} - 1\\
>
> Pour \\m = 12\\ (mensuel) : \\i_m = (1 + i_a)^{1/12} - 1\\
>
> Pour \\m = 4\\ (trimestriel) : \\i_t = (1 + i_a)^{1/4} - 1\\

> **IMPORTANT:**
>
> Deux taux relatifs à des périodes différentes sont **équivalents** lorsque, appliqués en intérêts composés au même capital pendant la même durée, ils produisent la même valeur acquise : \\(1 + i_p)^m = 1 + i_a\\, où \\m\\ est le nombre de sous-périodes dans l’année.

### C. Taux annuel effectif global (TAEG)

À partir d’un taux périodique \\i_p\\ et de \\m\\ périodes par an :

\\i\_{\text{annuel effectif}} = (1 + i_p)^m - 1\\

### Exemple résolu

> Pour un taux mensuel de **0,5 %** :

\\i_a = (1{,}005)^{12} - 1 \approx 0{,}0617 = 6{,}17\\\\\\

Le taux annuel effectif est **6,17 %**, et non 6 % (qui serait le taux proportionnel \\0{,}5\\ \times 12\\). L’écart (0,17 point) représente l’effet de la capitalisation mensuelle.

> **NOTE:**
>
> Un taux affiché ne dit rien du coût réel tant que l’on ne connaît pas la fréquence de capitalisation. Si les intérêts sont capitalisés plus souvent (chaque mois, chaque jour), le coût annuel effectif augmente, à taux affiché identique ; l’écart grandit aussi avec le niveau du taux. Pour comparer deux offres de crédit ou de placement, il faut donc les convertir sur une même période avec des taux **équivalents** — c’est précisément le rôle du TAEG que les prêteurs doivent afficher : dans la situation concrète, 9,38 % pour B contre 9 % pour A.

Le **TAEG** (taux annuel effectif global) est tout simplement le taux annuel effectif correspondant à un taux périodique donné, calculé par \\(1+i_p)^m - 1\\. Si une banque applique 0,5 % par mois, le TAEG est de \\(1{,}005)^{12} - 1 \approx 6{,}17\\\\\\, et non 6 %. En France, la loi oblige les prêteurs à afficher le TAEG précisément pour que l’emprunteur puisse comparer le coût réel de différentes offres de crédit, indépendamment de la fréquence de capitalisation affichée.

> **WARNING:**
>
> **L’intuition piège** : « 9 % par an, c’est 0,75 % par mois : il suffit de diviser par 12. »
>
> **Pourquoi c’est faux** : diviser par 12 donne le taux proportionnel, qui ignore que les intérêts mensuels produisent eux-mêmes des intérêts les mois suivants ; 0,75 % par mois capitalisé donne en réalité 9,38 % sur l’année.
>
> **Le bon raisonnement** : pour obtenir le même résultat sur un an, le taux mensuel doit vérifier « (1 + taux mensuel) puissance 12 = 1 + taux annuel », ce qui donne le taux équivalent.
>
> **Astuce mémo** : diviser donne le proportionnel, la racine donne l’équivalent.

> **IMPORTANT:**
>
> | Conversion | Formule | Prend en compte la capitalisation ? |
> |----|----|----|
> | Proportionnel | \\i_p = i_a / m\\ | ❌ Non |
> | Équivalent | \\i_p = (1+i_a)^{1/m} - 1\\ | ✅ Oui |
>
> En finance exacte (prêts immobiliers, obligations), on utilise toujours les taux **équivalents**. Le taux proportionnel n’est utilisé que dans des conventions simplifiées ou pour des durées inférieures à 1 an.

------------------------------------------------------------------------

## Séquence 5 — Annuités constantes

> *Durée : 1 heure 15*

> **NOTE:**
>
> Thomas veut réunir **30 000 €** d’apport pour acheter un appartement dans **5 ans**. Il peut mettre de côté **5 000 € par an**, versés à la fin de chaque année sur un placement rémunéré à **3 %**. Cinq versements de 5 000 € font 25 000 € : il lui manque 5 000 € sur le papier, mais les intérêts vont travailler pour lui. Reste à savoir s’ils suffiront à combler l’écart.
>
> **Les versements de Thomas lui permettront-ils d’atteindre son objectif ?**

### Intuition économique

Une **annuité** est un flux financier constant (versement ou encaissement) répété à intervalles réguliers. La question est : quelle est la valeur *totale* de ces flux, ramenée à une date commune ?

> **IMPORTANT:**
>
> Avant d’appliquer une formule d’annuités, tracez *systématiquement* la ligne du temps et répondez à ces cinq questions :
>
> 1.  Quelle est la **date d’évaluation** souhaitée (\\t = 0\\ ou \\t = n\\) ?
> 2.  Les flux sont-ils en **début** ou en **fin de période** ?
> 3.  Y a-t-il un **différé** (les flux commencent après plusieurs périodes) ?
> 4.  Le taux et les flux sont-ils sur la **même périodicité** ?
> 5.  Doit-on **capitaliser** (aller vers le futur) ou **actualiser** (revenir vers le présent) ?

Avant toute formule, le réflexe absolu consiste à **tracer la ligne du temps** : placer chaque flux à sa date, repérer la date d’évaluation, vérifier si les versements sont en début ou en fin de période, s’il y a un différé, et si le taux et les flux partagent la même périodicité. Cinq questions simples qui, une fois posées, déterminent automatiquement la bonne formule à utiliser. Cette habitude visuelle évite la grande majorité des erreurs de décalage d’une période — l’erreur la plus fréquente en calcul financier.

### Exploration numérique

*Règle d’or : tracez d’abord la ligne du temps (voir [Règle d’or](#rule-ligne-temps)).*

Appliquons la règle d’or au projet de Thomas : date d’évaluation \\t = 5\\ (le jour de l’achat), versements en **fin** d’année, pas de différé, taux et versements annuels, et l’on **capitalise** vers le futur.

**Année par année.** Chaque année, le solde rapporte 3 %, puis Thomas ajoute 5 000 €.

| Année | Solde en début d’année (€) | Intérêts à 3 % (€) | Versement (€) | Solde en fin d’année (€) |
|---:|---:|---:|---:|---:|
| 1 | 0,00 | 0,00 | 5 000 | 5 000,00 |
| 2 | 5 000,00 | 150,00 | 5 000 | 10 150,00 |
| 3 | 10 150,00 | 304,50 | 5 000 | 15 454,50 |
| 4 | 15 454,50 | 463,64 | 5 000 | 20 918,14 |
| 5 | 20 918,14 | 627,54 | 5 000 | 26 545,68 |

**Versement par versement.** On peut aussi suivre chaque versement jusqu’à \\t = 5\\ : le premier travaille 4 ans, le deuxième 3 ans… le dernier, versé le jour même, ne travaille pas du tout.

| Versement | Années de placement | Valeur à \\t = 5\\ (€) |
|----|---:|---:|
| Fin d’année 1 | 4 | 5 000 × 1,03 × 1,03 × 1,03 × 1,03 = 5 627,54 |
| Fin d’année 2 | 3 | 5 000 × 1,03 × 1,03 × 1,03 = 5 463,64 |
| Fin d’année 3 | 2 | 5 000 × 1,03 × 1,03 = 5 304,50 |
| Fin d’année 4 | 1 | 5 000 × 1,03 = 5 150,00 |
| Fin d’année 5 | 0 | 5 000,00 |
| **Total** |  | **26 545,68** |

**Réponse à Thomas :** non, ses versements ne suffisent pas. Il disposera de **26 545,68 €**, soit environ **3 454 € de moins** que les 30 000 € visés : les intérêts (1 545,68 €) ne comblent qu’une partie de l’écart. Comme le total est proportionnel au versement, il devrait verser 30 000 / 26 545,68 × 5 000 ≈ **5 650,64 € par an** pour atteindre son objectif.

``` mermaid
flowchart LR
  V0["t = 0 : valeur actuelle V0 = 22 898,54 EUR"]
  F1["t = 1 : versement 5 000 EUR"]
  F2["t = 2 : versement 5 000 EUR"]
  F3["t = 3 : versement 5 000 EUR"]
  F4["t = 4 : versement 5 000 EUR"]
  F5["t = 5 : versement 5 000 EUR"]
  VN["t = 5 : valeur acquise Vn = 26 545,68 EUR"]
  V0 <-.->|"/ 1,03^1"| F1
  V0 <-.->|"/ 1,03^2"| F2
  V0 <-.->|"/ 1,03^3"| F3
  V0 <-.->|"/ 1,03^4"| F4
  V0 <-.->|"/ 1,03^5"| F5
  F1 -->|"x 1,03^4"| VN
  F2 -->|"x 1,03^3"| VN
  F3 -->|"x 1,03^2"| VN
  F4 -->|"x 1,03^1"| VN
  F5 -->|"x 1,03^0"| VN
```

*Ligne du temps des versements de Thomas : les cinq versements de 5 000 € (dates 1 à 5) sont capitalisés jusqu’à la date 5, où ils valent 26 545,68 €, ou actualisés jusqu’à la date 0, où ils valent 5 000 × (1 − 1,03^−5) / 0,03 ≈ 22 898,54 €.*

> **TIP:**
>
> - Les deux tableaux donnent le même total : la valeur acquise est la **somme des valeurs capitalisées** de chaque versement.
> - Chaque ligne du second tableau est la précédente multipliée (ou divisée) par 1,03 : le total est une **somme géométrique**.
>
> \\5\\000 \times \left(1 + 1{,}03 + 1{,}03^2 + 1{,}03^3 + 1{,}03^4\right) = 5\\000 \times 5{,}30914 \approx 26\\545{,}68 \text{ €}\\
>
> - Une somme géométrique de raison \\1{,}03\\ et de 5 termes se calcule en une seule opération : \\\dfrac{1{,}03^5 - 1}{0{,}03} \approx 5{,}30914\\.
>
> En remplaçant 5 000 € par un versement \\A\\, 3 % par un taux \\i\\ et 5 par \\n\\, on obtient la formule de la valeur acquise des annuités de fin de période.

### A. Annuités de fin de période (terme échu)

``` mermaid
flowchart LR
    t0["t = 0"]
    t1["t = 1<br/>A"]
    t2["t = 2<br/>A"]
    tn_1["t = n-1<br/>A"]
    tn["t = n<br/>A"]
    t0 --> t1
    t1 --> t2
    t2 -.-> tn_1
    tn_1 --> tn
```

Les versements ont lieu aux dates \\t = 1, 2, \dots, n\\ (fin de période).

> **TIP:**
>
> **Valeur acquise** (à la date \\n\\) :
>
> \\V_n = A \cdot \frac{(1+i)^n - 1}{i}\\
>
> **Valeur actuelle** (à la date \\0\\) :
>
> \\V_0 = A \cdot \frac{1 - (1+i)^{-n}}{i}\\
>
> **Lecture :** \\A\\ est le montant de chaque versement, \\i\\ le taux périodique, \\n\\ le nombre de versements. Les formules donnent la valeur *équivalente* de tous les versements à la date choisie.

> **NOTE:**
>
> **Ce que calcule cette formule** : la valeur totale d’une suite de versements identiques en fin de période, soit à la date du dernier versement (`V_n`), soit une période avant le premier (`V_0`).
>
> **Rôle de chaque paramètre** :
>
> - `V_n` : la valeur acquise, somme de tous les versements capitalisés jusqu’à la date `n`.
> - `V_0` : la valeur actuelle, somme de tous les versements actualisés à la date 0.
> - `A` : le montant constant de chaque versement.
> - `i` : le taux par période, de même périodicité que les versements.
> - `n` : le nombre de versements, égal au nombre de périodes.
>
> **Ce que signifie le résultat** : `V_n` est le capital constitué (26 545,68 € pour Thomas) et `V_0` le montant unique d’aujourd’hui équivalent à tous les versements (22 898,54 € pour Thomas).
>
> **Intuition directionnelle** : si le taux `i` augmente, la valeur acquise `V_n` augmente tandis que la valeur actuelle `V_0` diminue.

Une **annuité** est une suite de versements identiques et réguliers. Lorsqu’ils ont lieu en **fin de période** (terme échu) — par exemple 5 000 € chaque 31 décembre — chaque versement est capitalisé jusqu’à la date d’évaluation. La valeur acquise à la date du dernier versement est \\V_n = A \cdot \frac{(1+i)^n - 1}{i}\\, et la valeur actuelle (un an avant le premier versement) est \\V_0 = A \cdot \frac{1-(1+i)^{-n}}{i}\\. Ces formules condensent en une seule opération ce qui serait autrement un long tableau de capitalisation année par année.

> **CAUTION:**
>
> La valeur actuelle est la somme des valeurs actuelles de chaque versement :
>
> \\V_0 = \frac{A}{(1+i)^1} + \frac{A}{(1+i)^2} + \cdots + \frac{A}{(1+i)^n}\\
>
> C’est une suite géométrique de premier terme \\A/(1+i)\\, de raison \\1/(1+i)\\, avec \\n\\ termes. Sa somme vaut :
>
> \\V_0 = \frac{A}{1+i} \cdot \frac{1 - (1/(1+i))^n}{1 - 1/(1+i)} = A \cdot \frac{1 - (1+i)^{-n}}{i}\\

> **IMPORTANT:**
>
> Une suite d’**annuités constantes de fin de période** (terme échu) est une suite de \\n\\ flux de même montant \\A\\, versés aux dates \\t = 1, 2, \dots, n\\, la période des flux étant celle du taux \\i\\. Sa **valeur acquise** \\V_n\\ est évaluée à la date du dernier flux ; sa **valeur actuelle** \\V_0\\, une période avant le premier flux.

### Exemple résolu

> Une PME s’engage à verser **2 000 €** à la fin de chaque année pendant **4 ans**. Le taux est de **5 %**.

**Valeur actuelle** (ce que représente l’engagement aujourd’hui) :

\\V_0 = 2\\000 \times \frac{1 - 1{,}05^{-4}}{0{,}05} = 2\\000 \times 3{,}54595 \approx 7\\091{,}90 \text{ €}\\

**Valeur acquise** (à la date du dernier versement) :

\\V_4 = 2\\000 \times \frac{1{,}05^{4} - 1}{0{,}05} = 2\\000 \times 4{,}31013 \approx 8\\620{,}25 \text{ €}\\

Vérification : \\7\\091{,}90 \times 1{,}05^4 \approx 8\\620{,}25\\ €. Les deux valeurs décrivent les mêmes flux, vus à deux dates différentes.

> **NOTE:**
>
> Une annuité transforme un effort régulier en un capital (valeur acquise) ou résume une suite d’engagements en un montant unique d’aujourd’hui (valeur actuelle). Pour Thomas, les intérêts ne représentent que 1 545,68 € sur 26 545,68 € : sur une durée courte et à taux faible, c’est surtout l’épargne qui fait le capital. Si la durée s’allonge, la valeur acquise augmente plus vite que le nombre de versements : avec un sixième versement de 5 000 €, il atteindrait environ 32 342 €. Pour décider, il dispose donc de trois leviers : verser davantage (environ 5 651 € par an), attendre plus longtemps, ou trouver un meilleur taux.

> **WARNING:**
>
> **L’intuition piège** : « Il y a 5 versements, donc la formule d’annuité s’applique telle quelle, que l’on verse en début ou en fin d’année. »
>
> **Pourquoi c’est faux** : la formule standard suppose des versements en fin de période ; si l’on verse en début de période, chaque versement travaille une année de plus et la valeur acquise est multipliée par (1 + i).
>
> **Le bon raisonnement** : tracer la ligne du temps, repérer la date du premier et du dernier flux, puis choisir la formule (terme échu ou terme à échoir) et la date d’évaluation correspondantes.
>
> **Astuce mémo** : dessine la ligne du temps — où tombe le premier flux ?

### B. Annuités de début de période (terme à échoir)

``` mermaid
flowchart LR
    t0["t = 0<br/>A"]
    t1["t = 1<br/>A"]
    t2["t = 2<br/>A"]
    tn_1["t = n-1<br/>A"]
    tn["t = n"]
    t0 --> t1
    t1 --> t2
    t2 -.-> tn_1
    tn_1 --> tn
```

Les versements ont lieu aux dates \\t = 0, 1, \dots, n-1\\ (début de période).

Chaque versement est avancé d’une période par rapport au cas précédent, donc il bénéficie d’une période de capitalisation supplémentaire.

> **TIP:**
>
> \\V_n = A \cdot \frac{(1+i)^n - 1}{i} \cdot (1+i)\\
>
> \\V_0 = A \cdot \frac{1 - (1+i)^{-n}}{i} \cdot (1+i)\\
>
> **Lecture :** il suffit de multiplier les formules de fin de période par \\(1+i)\\ pour obtenir celles de début de période.

> **NOTE:**
>
> **Ce que calcule cette formule** : la valeur totale d’une suite de versements identiques effectués en début de période, chaque versement travaillant une période de plus qu’en fin de période.
>
> **Rôle de chaque paramètre** :
>
> - `V_n` : la valeur acquise, évaluée à la date `n`, une période après le dernier versement.
> - `V_0` : la valeur actuelle, évaluée à la date du premier versement.
> - `A` : le montant constant de chaque versement.
> - `i` : le taux par période, de même périodicité que les versements.
> - `n` : le nombre de versements.
> - `(1 + i)` : le facteur qui ajoute la période de capitalisation supplémentaire gagnée par chaque versement.
>
> **Ce que signifie le résultat** : le résultat est toujours supérieur à celui des versements de fin de période ; si Thomas versait en début d’année, il disposerait de 26 545,68 × 1,03 ≈ 27 342 € au bout de 5 ans.
>
> **Intuition directionnelle** : si le taux `i` augmente, l’avantage de verser en début de période augmente, car la période de capitalisation supplémentaire rapporte davantage.

Si les versements ont lieu en **début de période** (terme à échoir) — par exemple 5 000 € chaque 1er janvier — chaque flux bénéficie d’une période de capitalisation supplémentaire. Il suffit donc de multiplier les formules du terme échu par \\(1+i)\\ : la valeur acquise devient \\V_n = A \cdot \frac{(1+i)^n - 1}{i} \cdot (1+i)\\. Concrètement, verser en début d’année plutôt qu’en fin d’année rapporte toujours plus, à effort égal — un avantage que la ligne du temps permet de visualiser immédiatement.

### C. Annuités différées

Si les versements commencent après \\d\\ périodes de différé :

1.  Calculer \\V\_{d}\\ : la valeur *juste avant le premier versement* (à \\t = d\\) à l’aide des formules habituelles.
2.  Actualiser \\V\_{d}\\ jusqu’à la date souhaitée : \\V_0 = V\_{d} \cdot (1+i)^{-d}\\.

Une annuité est **différée** lorsque les versements ne commencent qu’après un certain délai \\d\\. La méthode est en deux temps : on calcule d’abord la valeur de l’annuité à la date du premier versement (comme si elle commençait à \\t = d\\), puis on actualise ce montant jusqu’à la date d’évaluation souhaitée en le divisant par \\(1+i)^d\\. Cette double étape — évaluer à la date de début, puis ramener à aujourd’hui — est un schéma général que l’on retrouve dans de nombreux problèmes de finance.

### D. Perpétuités

> **TIP:**
>
> **Perpétuité constante** (versements infinis et constants) :
>
> \\V_0 = \frac{A}{i}\\
>
> **Perpétuité croissante** au taux \\g\\ (\\i \> g\\) :
>
> \\V_0 = \frac{A_1}{i - g}\\
>
> **Lecture :** quand \\n \to \infty\\, le facteur \\1-(1+i)^{-n} \to 1\\, donc \\V_0 \to A/i\\. La perpétuité croissante correspond au modèle de Gordon-Shapiro utilisé en évaluation d’actions.

> **NOTE:**
>
> **Ce que calcule cette formule** : la valeur actuelle d’une suite infinie de versements, constants ou croissant à un rythme régulier.
>
> **Rôle de chaque paramètre** :
>
> - `V_0` : la valeur actuelle de tous les versements futurs, évaluée une période avant le premier.
> - `A` : le montant constant de chaque versement de la perpétuité constante.
> - `i` : le taux d’actualisation par période.
> - `A_1` : le premier versement de la perpétuité croissante, reçu à la fin de la première période.
> - `g` : le taux de croissance des versements, qui doit rester inférieur à `i`.
>
> **Ce que signifie le résultat** : `V_0` est le prix maximal à payer aujourd’hui pour un revenu sans fin ; par exemple, 1 000 € par an à 4 % valent 25 000 €.
>
> **Intuition directionnelle** : si le taux `i` augmente ou si la croissance `g` diminue, la valeur `V_0` baisse, et elle explose lorsque `g` se rapproche de `i`.

Une **perpetuité** est une annuité qui ne s’arrête jamais : des versements de montant constant \\A\\ à l’infini. Quand \\n\\ tend vers l’infini dans la formule de valeur actuelle, le terme \\(1+i)^{-n}\\ tend vers 0, et il reste simplement \\V_0 = A / i\\. Ainsi, recevoir 1 000 € par an à perpétuité au taux de 4 % « vaut » 25 000 € aujourd’hui. La perpétuité croissante (modèle de Gordon-Shapiro, \\V_0 = A_1/(i-g)\\) est le fondement de l’évaluation de nombreuses actions : elle valorise un dividende qui croît régulièrement avec le temps.

------------------------------------------------------------------------

## Séquence 6 — Cas pratique : constituer un capital

> *Durée : 1 heure*

> **NOTE:**
>
> Une entreprise souhaite constituer dans **8 ans** une réserve de **500 000 €** destinée au remplacement de son système d’information.
>
> Les versements sont effectués en **fin d’année**. Le placement rapporte **3,5 %** par an.

*Règle d’or : tracez d’abord la ligne du temps (voir [Règle d’or](#rule-ligne-temps)).*

### Étape 1 — Calcul de l’annuité nécessaire (question principale)

On cherche \\A\\ tel que \\V_n = 500\\000\\ avec \\n = 8\\ et \\i = 0{,}035\\.

On inverse la formule de valeur acquise des annuités de fin de période :

\\A = V_n \times \frac{i}{(1+i)^n - 1}\\

\\A = 500\\000 \times \frac{0{,}035}{(1{,}035)^8 - 1} = 500\\000 \times \frac{0{,}035}{0{,}316809} \approx 55\\238 \text{ €}\\

> **IMPORTANT:**
>
> Vérifiez que \\55\\238 \times \frac{(1{,}035)^8 - 1}{0{,}035} \approx 500\\000\\. Tout modèle Excel doit comporter ce type de cellule de contrôle.

### Étape 2 — Tester les variantes (questions subsidiaires)

**Q2 — Versements en début d’année :**

\\A\_{\text{début}} = V_n \times \frac{i}{(1+i)^n - 1} \times \frac{1}{1+i} \approx 55\\238 / 1{,}035 \approx 53\\370 \text{ €}\\

Verser en début d’année permet d’économiser environ 1 868 € par an.

**Q3 — Taux limité à 2 % :**

\\A = 500\\000 \times \frac{0{,}02}{(1{,}02)^8 - 1} \approx 58\\255 \text{ €}\\

Un taux plus faible impose des versements plus élevés (la capitalisation travaille moins).

**Q4 — Versements fixes de 50 000 € :**

\\V_8 = 50\\000 \times \frac{(1{,}035)^8 - 1}{0{,}035} \approx 452\\584 \text{ €}\\

Ces versements ne suffisent pas : il manquerait environ 47 416 €.

> **IMPORTANT:**
>
> - **Si** l’objectif est un capital futur à une date fixe, **alors** on inverse la formule de valeur acquise pour trouver le versement périodique \\A\\.
> - **Si** les versements peuvent être effectués en début de période, **alors** chaque versement travaille une période de plus et l’effort annuel est divisé par \\(1+i)\\.
> - **Si** le taux de placement baisse, **alors** l’effort d’épargne augmente : il faut prévoir une marge de sécurité sur le taux retenu.
> - **Si** le versement est imposé par la trésorerie, **alors** on calcule la valeur acquise, on la compare à l’objectif et l’on comble l’écart en allongeant la durée ou en augmentant les versements.
> - **Si** un montant est retenu, **alors** on le contrôle par la formule inverse avant de le présenter.

------------------------------------------------------------------------

## Séquence 7 — Synthèse et erreurs fréquentes

> *Durée : 45 minutes*

### Carte mentale du cours

``` mermaid
mindmap
  root((Valeur temps<br/>de l'argent))
    Capitalisation
      C_n = C_0(1+i)^n
    Actualisation
      V_0 = V_n/(1+i)^n
    Taux
      Proportionnel
        i_p = i_a / m
      Équivalent
        i_p = (1+i_a)^(1/m) - 1
    Annuités
      Fin de période
        V_0 = A·(1-(1+i)^-n)/i
      Début de période
        V_0 = A·(1-(1+i)^-n)/i · (1+i)
      Perpétuité
        V_0 = A/i
```

> **WARNING:**
>
> **Erreurs mathématiques**
>
> - Utiliser \\5\\ au lieu de \\0{,}05\\ pour un taux de 5 %.
> - Mélanger un taux mensuel avec une durée exprimée en années (sans conversion).
> - Oublier les intérêts composés (utiliser la formule simple quand la période \> 1 an) — [voir Séquence 2](#err-s2).
> - Décaler les flux d’une période (erreur de ±1 dans l’exposant) — [voir Séquence 5](#err-s5).
> - Confondre taux proportionnel et taux équivalent — [voir Séquence 4](#err-s4).
>
> **Erreurs de raisonnement**
>
> - Additionner directement des flux de dates différentes — [voir Séquence 3](#err-s3).
> - Ne pas tracer la ligne du temps avant de calculer.
> - Oublier de vérifier la cohérence entre la périodicité du taux et celle des flux.

> **TIP:**
>
> 1.  **Tracer la ligne du temps** avant toute formule.
> 2.  **Vérifier la cohérence** entre taux et périodicité des flux.
> 3.  **Actualiser à une date commune** avant de comparer des flux.
> 4.  **Interpréter le résultat** (que signifie cette VAN de 120 000 € ?).
> 5.  **Contrôler** le calcul par une formule inverse.

------------------------------------------------------------------------

## Exercices

### Niveau 1 — Application directe

**Exercice 1.1** — Un capital de **15 000 €** est placé pendant **6 ans** au taux annuel de **3 %** en intérêts composés. Calculez la valeur acquise \\C_6\\.

> **CAUTION:**
>
> \\C_6 = 15\\000 \times (1{,}03)^6 = 15\\000 \times 1{,}1941 \approx 17\\911 \text{ €}\\

**Exercice 1.2** — Quelle somme faut-il placer aujourd’hui pour obtenir **25 000 €** dans **4 ans**, si le taux annuel est **4,5 %** ?

> **CAUTION:**
>
> \\V_0 = \frac{25\\000}{(1{,}045)^4} = \frac{25\\000}{1{,}192519} \approx 20\\964 \text{ €}\\

**Exercice 1.3** — Un taux mensuel de **0,8 %** correspond à quel taux annuel effectif ?

> **CAUTION:**
>
> \\i_a = (1{,}008)^{12} - 1 \approx 0{,}1003 = 10{,}03\\\\\\
>
> (Et non \\0{,}8\\ \times 12 = 9{,}6\\\\\\ qui serait le taux proportionnel.)

------------------------------------------------------------------------

### Niveau 2 — Problème contextualisé

**Exercice 2.1** — Comparer les trois offres de placement suivantes sur une base annuelle effective :

| Offre | Taux affiché | Périodicité               |
|-------|--------------|---------------------------|
| A     | 4,8 %        | Mensuel proportionnel     |
| B     | 4,7 %        | Annuel                    |
| C     | 4,6 %        | Trimestriel proportionnel |

Quelle offre est la plus avantageuse ?

> **CAUTION:**
>
> **Offre A** — taux mensuel proportionnel \\4{,}8\\ / 12 = 0{,}4\\\\\\
>
> Taux annuel effectif : \\i_A = (1{,}004)^{12} - 1 \approx 4{,}91\\\\\\
>
> **Offre B** — déjà sur base annuelle : \\i_B = 4{,}70\\\\\\
>
> **Offre C** — taux trimestriel proportionnel \\4{,}6\\\\ / 4 = 1{,}15\\\\\\
>
> Taux annuel effectif : \\i_C = (1{,}0115)^{4} - 1 \approx 4{,}67\\\\\\
>
> Classement : **A (4,91 %) \> B (4,70 %) \> C (4,67 %)**
>
> L’offre A est la plus avantageuse malgré un taux affiché inférieur à B, parce que sa capitalisation mensuelle génère un taux effectif plus élevé.

------------------------------------------------------------------------

### Niveau 3 — Étude de cas

**Cas — Plan d’épargne retraite**

Un cadre de 35 ans souhaite constituer un complément de retraite. Il envisage de verser **800 €/mois en fin de mois** pendant **30 ans** sur un contrat d’assurance-vie rémunéré à **3 % par an** (taux équivalent mensuel à calculer).

1.  Calculez le taux mensuel équivalent au taux annuel de 3 %.
2.  Calculez le capital constitué à 65 ans.
3.  Si ce capital sert ensuite à financer une rente mensuelle pendant 20 ans (même taux), calculez le montant de la rente mensuelle.
4.  Quel serait l’impact d’une hausse du taux à 4 % annuel sur le capital final ?
5.  Rédigez une recommandation d’une phrase.

> **CAUTION:**
>
> **1. Taux mensuel équivalent :** \\i_m = (1{,}03)^{1/12} - 1 \approx 0{,}2466\\\\\\
>
> **2. Capital à 65 ans (\\n = 360\\ mois) :** \\V\_{360} = 800 \times \frac{(1{,}002466)^{360} - 1}{0{,}002466} \approx 800 \times 578{,}71 \approx 462\\970 \text{ €}\\
>
> **3. Rente mensuelle pendant 20 ans (\\n = 240\\ mois) :** \\A = 462\\970 \times \frac{0{,}002466}{1 - (1{,}002466)^{-240}} \approx 462\\970 \times 0{,}005526 \approx 2\\558 \text{ €/mois}\\
>
> **4. Impact d’un taux de 4 % :** \\i_m = (1{,}04)^{1/12} - 1 \approx 0{,}3274\\\\\\ \\V\_{360} \approx 800 \times \frac{(1{,}003274)^{360} - 1}{0{,}003274} \approx 800 \times 685{,}27 \approx 548\\216 \text{ €}\\
>
> Soit un gain d’environ +85 246 € par rapport au scénario à 3 %.
>
> **5. Recommandation :** À 3 % de rendement annuel et 800 €/mois de versement, le plan permet de constituer environ 463 000 € en 30 ans, générant une rente d’environ 2 560 €/mois pendant 20 ans ; une hausse d’un point de taux augmenterait ce capital d’environ 85 000 € (près de 20 %), ce qui justifie d’arbitrer vers des supports plus dynamiques si le profil de risque le permet.

## Citation

BibTeX

``` quarto-appendix-bibtex
@online{gilles,
  author = {Gilles, Guillaume},
  title = {1️⃣ Valeur temps de l’argent},
  url = {https://ggilles.dev/fr/teaching/mathematical-finance/valeur-temps-argent.html},
  langid = {fr},
  abstract = {**À la fin de cette journée, vous saurez :** - distinguer
    capitalisation et actualisation\,; - convertir des taux exprimés sur
    des périodicités différentes\,; - calculer la valeur actuelle ou
    acquise d’un capital isolé\,; - valoriser une suite d’annuités
    constantes (fin, début, différées, perpétuité)\,; - résoudre des
    problèmes d’épargne et de constitution de capital.}
}
```

Veuillez citer ce travail comme suit :

Gilles, Guillaume. n.d. “1️⃣ Valeur temps de l’argent.” <https://ggilles.dev/fr/teaching/mathematical-finance/valeur-temps-argent.html>.
