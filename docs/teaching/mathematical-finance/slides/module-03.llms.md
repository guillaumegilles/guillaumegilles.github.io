``` js
fmt = (x, d = 0) =>
  x.toLocaleString("fr-FR", {minimumFractionDigits: d, maximumFractionDigits: d})
pct = (x, d = 2) => fmt(100 * x, d) + " %"
eur = x => {
  const r = Math.round(Math.abs(x)).toString().replace(/\B(?=(\d{3})+(?!\d))/g, " ");
  return (x < 0 && Math.round(Math.abs(x)) !== 0 ? "−" : "") + r + " €";
}
van = (I0, flows, k) => -I0 + flows.reduce((s, cf, t) => s + cf / (1 + k) ** (t + 1), 0)
```

## 0.1 Faut-il acheter cette machine ?

Sans calculer — votez à main levée, puis justifiez.

Un atelier de menuiserie hésite à acheter une machine à commande numérique.

MACHINE

50 000 €

aujourd'hui

EN RETOUR

15 000 €/an

pendant 5 ans = 75 000 €

EXIGENCE

8 %/an

rendement minimum exigé

75 000 € \> 50 000 €… mais les 75 000 € arrivent **au fil des années**. **Toute la journée tient dans cette question.**

Vote à main levée (2 min). Noter la répartition oui/non au tableau. Demander 2-3 justifications : elles font émerger la valeur temps de l’argent, le coût d’opportunité, le risque. On tranchera en Séquence 2 avec la VAN.

## 0.2 Objectifs de la journée

À la fin de cette journée, vous serez capables de :

1.  construire les **flux de trésorerie différentiels** d’un projet ;
2.  calculer et interpréter la **VAN** ;
3.  calculer le **TRI** et discuter ses limites ;
4.  utiliser le **délai de récupération** simple et actualisé ;
5.  **comparer des projets** de durées différentes (annuité équivalente) ;
6.  mener une **analyse de sensibilité** et raisonner par **scénarios** ;
7.  formuler une **recommandation d’investissement** argumentée.

## 0.3 Programme de la journée

### 0.3.1 Matin — 3 h

| Séquence               |       Durée |
|------------------------|------------:|
| 1 · Flux de trésorerie |      45 min |
| 2 · VAN                |      60 min |
| 3 · TRI                |      60 min |
| Pause                  |      15 min |
| **Total**              | **180 min** |

### 0.3.2 Après-midi — 3 h

| Séquence                 |       Durée |
|--------------------------|------------:|
| 4 · Délais & comparaison |      45 min |
| 5 · Analyse du risque    |      75 min |
| 6 · Cas intégrateur      |      45 min |
| 7 · Synthèse & exercices |      15 min |
| **Total**                | **180 min** |

6 h de face-à-face. Le classeur Excel est disponible dans le cours pour reproduire tous les calculs.

Si le groupe prend du retard : la démonstration interactive de la Séquence 4 (délais) est compressible. Le cas intégrateur (S6) peut être traité en démonstration magistrale plutôt qu’en travail de groupe.

## 0.4 La règle d’or

✏️ La **ligne du temps** avant toute formule.

− I₀

t = 0\
investissement

 

CF₁

t = 1

 

CF₂

t = 2

…

CFₙ+VR

t = n\
flux terminal

1.  Placez **chaque flux à sa date**, avec son **sens** (+ reçu / − versé).
2.  Repérez la **date d’évaluation** (aujourd’hui, $t = 0$).
3.  *Ensuite seulement* : actualisez tout à cette date.

Insister : amortissements oubliés, BFR ignoré, double comptage de l’investissement… les pièges de la Séquence 1 se voient tous sur ce schéma.

1 Séquence 1\
Construction des flux de trésorerie
===================================

Quels flux réels le projet génère-t-il ?

## 1.1 Flux comptables ≠ flux de trésorerie

- 📊 Le **résultat comptable** inclut des charges **non décaissées** (amortissements).
- 💶 Seuls les **flux réels** comptent pour la décision financière.
- 🔄 On **réintègre** les dotations aux amortissements : elles ont réduit l’impôt sans sortir d’argent.

$$CF_t = \text{Résultat d'exploitation après impôt} + \text{Dotation aux amortissements}$$

Ou à partir de l’EBE :

$$CF_t = EBE - \text{Impôt théorique} - \Delta BFR_t - \text{Investissements complémentaires}$$

## 1.2 La ligne du temps d’un projet

−I₀\
prix + frais\
+ ΔBFR₀

t = 0

 

CF₁

t = 1

 

CF₂

t = 2

…

CFₙ + VR\
+ BFR récupéré

t = n

### 1.2.1 Flux initial ($t = 0$)

- Prix d’acquisition
- Frais d’installation
- Coûts de formation
- − Produit de cession (si remplacement)
- - ΔBFR₀

### 1.2.2 Flux terminal ($t = n$)

- Valeur résiduelle nette
- − Imposition sur plus-value
- - Récupération du BFR
- − Coûts de fermeture

## 1.3 🪤 Cinq pièges classiques

1.  **Amortissements en sortie** — ce ne sont pas des décaissements.
2.  **BFR oublié** — toute hausse d’activité immobilise de la trésorerie.
3.  **Double comptage** — ne pas inclure les intérêts si le taux reflète déjà le coût du financement.
4.  **Valeur résiduelle omise** — l’actif a souvent encore de la valeur en fin de projet.
5.  **Sunk costs** — les coûts déjà engagés et irrécupérables n’apparaissent jamais.

Décision sur flux **différentiels**, jamais sur le résultat comptable seul.

2 Séquence 2\
Valeur actuelle nette (VAN)
===========================

Combien vaut aujourd’hui la machine de la menuiserie ?

## 2.1 Retour à la question d’ouverture

Machine à **50 000 €**, **15 000 €/an** pendant **5 ans**, taux exigé **8 %**. Le comptable : *« 5 × 15 000 = 75 000 € \> 50 000 €, c’est rentable. »*

Faut-il acheter la machine ?

Votre pronostic   ① Oui, largement   ② Oui, de justesse   ③ Non

## 2.2 Actualisons chaque flux

| Année $t$ | Flux         | Facteur $1/1{,}08^t$ | Valeur d’aujourd’hui |
|-----------|--------------|----------------------|----------------------|
| 1         | 15 000 €     | 0,9259               | 13 888,89 €          |
| 2         | 15 000 €     | 0,8573               | 12 860,08 €          |
| 3         | 15 000 €     | 0,7938               | 11 907,48 €          |
| 4         | 15 000 €     | 0,7350               | 11 025,45 €          |
| 5         | 15 000 €     | 0,6806               | 10 208,75 €          |
| **Total** | **75 000 €** |                      | **59 890,65 €**      |

$$59\,890{,}65 - 50\,000 = \mathbf{+9\,890{,}65\ €}$$

## 2.3 La formule et la règle de décision

$$VAN = -I_0 + \sum_{t=1}^{n} \frac{CF_t}{(1+k)^t}$$

| Résultat  | Interprétation                          | Décision        |
|-----------|-----------------------------------------|-----------------|
| $VAN > 0$ | Crée de la valeur au-delà du taux exigé | ✅ **Accepter** |
| $VAN = 0$ | Rémunère exactement au taux exigé       | ➖ Indifférent  |
| $VAN < 0$ | Ne couvre pas le rendement exigé        | ❌ **Rejeter**  |

VAN\
+9 891 €

t = 0\
évaluation

÷ 1,08

15 000

t = 1

÷ 1,08²

15 000

t = 2

…

15 000

t = 5

## 2.4 VAN(k) : plus le taux monte, moins ça vaut 🎛️

``` js
viewof s2_k = Inputs.range([0, 30], {value: 8, step: 0.5, label: "Taux d'actualisation k (%)"})
```

``` js
{
  const flows = [15000, 15000, 15000, 15000, 15000];
  const pts = Array.from({length: 121}, (_, i) => ({
    x: i * 0.25,
    v: van(50000, flows, i * 0.0025)
  }));
  const k = s2_k / 100;
  const v = van(50000, flows, k);
  return Plot.plot({
    width: 900, height: 300, marginLeft: 70,
    style: {background: "transparent", color: "currentColor"},
    x: {label: "Taux k (%)", domain: [0, 30]},
    y: {label: "↑ VAN (€)", grid: true, tickFormat: d => fmt(d)},
    marks: [
      Plot.areaY(pts, {x: "x", y1: 0, y2: d => Math.max(d.v, 0), fill: "#5bdb6d", fillOpacity: 0.15}),
      Plot.areaY(pts, {x: "x", y1: d => Math.min(d.v, 0), y2: 0, fill: "#db5b5b", fillOpacity: 0.15}),
      Plot.ruleY([0], {stroke: "#8b8f9c"}),
      Plot.line(pts, {x: "x", y: "v", stroke: "#5b9bdb", strokeWidth: 3}),
      Plot.dot([{x: s2_k, y: v}], {x: "x", y: "y", r: 8, fill: v >= 0 ? "#5bdb6d" : "#db5b5b", stroke: "white", strokeWidth: 2}),
      Plot.text([{x: s2_k, y: v}], {x: "x", y: "y", text: () => eur(v), dy: -16, fontSize: 14, fontWeight: "bold", fill: "currentColor"})
    ]
  });
}
```

``` js
{
  const k = s2_k / 100;
  const v = van(50000, [15000,15000,15000,15000,15000], k);
  return md`<div class="ojs-result">À k = **${pct(k, 1)}** : VAN = <span class="${v >= 0 ? "green" : "red"}">**${eur(v)}**</span> → ${v >= 0 ? "**accepter**" : "**rejeter**"}</div>`;
}
```

Faire constater : la VAN décroît quand k monte. À 8 % : +9 891 €. À 12 % : encore positif (+4 072 €). Au-delà de ~15,2 % (le TRI, Séquence 3), la VAN devient négative. Zone verte = zone d’acceptation.

## 2.5 Deux leviers de la VAN 🎛️

``` js
viewof s2_mult = Inputs.range([50, 150], {value: 100, step: 1, label: "Niveau des flux CF (% du cas central)"})
```

``` js
{
  const k = s2_k / 100;
  const mult = s2_mult / 100;
  const base = [15000, 15000, 15000, 15000, 15000];

  // Panneau gauche : VAN(k)
  const ptsK = Array.from({length: 121}, (_, i) => ({x: i * 0.25, v: van(50000, base.map(c => c * mult), i * 0.0025)}));
  const plotK = Plot.plot({
    width: 430, height: 280, marginLeft: 60,
    style: {background: "transparent", color: "currentColor"},
    x: {label: "Taux k (%)", domain: [0, 30]},
    y: {label: "VAN (€)", grid: true, tickFormat: d => fmt(d)},
    title: "↑ k  →  ↓ VAN",
    marks: [
      Plot.ruleY([0], {stroke: "#8b8f9c"}),
      Plot.line(ptsK, {x: "x", y: "v", stroke: "#5b9bdb", strokeWidth: 2.5}),
      Plot.dot([{x: s2_k, y: van(50000, base.map(c => c * mult), k)}], {x: "x", y: "y", r: 7, fill: "#5b9bdb", stroke: "white", strokeWidth: 1.5})
    ]
  });

  // Panneau droit : VAN(flux)
  const ptsCF = Array.from({length: 101}, (_, i) => ({x: 50 + i, v: van(50000, base.map(c => c * (50 + i) / 100), k)}));
  const plotCF = Plot.plot({
    width: 430, height: 280, marginLeft: 60,
    style: {background: "transparent", color: "currentColor"},
    x: {label: "Flux CF (%)", domain: [50, 150]},
    y: {label: "VAN (€)", grid: true, tickFormat: d => fmt(d)},
    title: "↑ CF  →  ↑ VAN",
    marks: [
      Plot.ruleY([0], {stroke: "#8b8f9c"}),
      Plot.line(ptsCF, {x: "x", y: "v", stroke: "#5bdb6d", strokeWidth: 2.5}),
      Plot.dot([{x: s2_mult, y: van(50000, base.map(c => c * mult), k)}], {x: "x", y: "y", r: 7, fill: "#5bdb6d", stroke: "white", strokeWidth: 1.5})
    ]
  });

  return html`<div style="display:flex; gap:16px; flex-wrap:wrap; justify-content:center;">
    <div>${plotK}</div><div>${plotCF}</div>
  </div>`;
}
```

``` js
{
  const k = s2_k / 100, mult = s2_mult / 100;
  const v = van(50000, [15000,15000,15000,15000,15000].map(c => c * mult), k);
  return md`<div class="ojs-result">k = **${pct(k, 1)}** · flux × **${s2_mult} %** → VAN = <span class="${v >= 0 ? "green" : "red"}">**${eur(v)}**</span></div>`;
}
```

## 2.6 Exemple résolu — La presse de l’imprimerie

> Presse à **30 000 €**, flux de **10 000 / 12 000 / 14 000 €** sur 3 ans, $k = 10\,\%$.

$$VAN = -30\,000 + \frac{10\,000}{1{,}10} + \frac{12\,000}{1{,}10^2} + \frac{14\,000}{1{,}10^3}$$ $$= -30\,000 + 9\,090{,}91 + 9\,917{,}36 + 10\,518{,}41$$

−473,33 €

VAN \< 0 → on rejette la presse

La somme brute (36 000 €) dépasse la mise, mais actualisée elle ne vaut que 29 527 €.

## 2.7 Indice de profitabilité (IP)

$$IP = \frac{\text{VA des flux futurs}}{I_0} = 1 + \frac{VAN}{I_0}$$

- IP \> 1 ⇔ VAN \> 0. Mesure la valeur créée **par euro investi**.
- Utile quand le **budget est contraint** : hiérarchiser des projets de tailles différentes.

⚠️ Pour des projets **mutuellement exclusifs**, c’est la **VAN absolue** qui prime — elle mesure l’enrichissement total, pas la rentabilité relative.

## 2.8 🪤 Le piège

« 5 × 15 000 = 75 000 € pour 50 000 € investis : rentable, inutile de calculer. »

On additionne des euros de **dates différentes** comme s’ils valaient tous autant que les 50 000 € d’aujourd’hui. Il faut **actualiser d’abord**.

Un euro de demain n’est pas un euro d’aujourd’hui.

## 2.9 🧠 Vérifiez votre compréhension

> Projet à 80 000 €, flux 30 000 / 35 000 / 40 000 € sur 3 ans, k = 10 %. VAN ?

$$VAN = -80\,000 + \frac{30\,000}{1{,}1} + \frac{35\,000}{1{,}1^2} + \frac{40\,000}{1{,}1^3} \approx \mathbf{+6\,252\ €}$$

✅ VAN \> 0 → projet acceptable.

3 Séquence 3\
Taux de rentabilité interne (TRI)
=================================

Jusqu’où le taux exigé peut-il monter ?

## 3.1 La machine, à plusieurs taux

| Taux exigé | VA des 5 flux |          VAN |
|------------|--------------:|-------------:|
| 8 %        |      59 891 € | **+9 891 €** |
| 12 %       |      54 072 € | **+4 072 €** |
| 16 %       |      49 114 € |   **−886 €** |
| 20 %       |      44 859 € | **−5 141 €** |

La VAN change de signe entre 12 % et 16 % → interpolation : $12\,\% + 4\,\% \times \frac{4\,072}{4\,072 + 886} \approx$ **15,3 %**

Calcul exact : **TRI = 15,24 %**

## 3.2 Définition et règle de décision

$$0 = -I_0 + \sum_{t=1}^{n} \frac{CF_t}{(1+r)^t} \qquad \text{le TRI est le taux } r \text{ qui annule la VAN}$$

| Comparaison | Décision       |
|-------------|----------------|
| $TRI > k$   | ✅ Accepter    |
| $TRI = k$   | ➖ Indifférent |
| $TRI < k$   | ❌ Rejeter     |

Le TRI ne dépend **que des flux du projet**, pas de l’opinion des associés. C’est le **taux exigé maximal** que le projet peut supporter.

## 3.3 Profil VAN(k) — le TRI est le point de croisement 🎛️

``` js
viewof s3_k = Inputs.range([0, 50], {value: 10, step: 0.5, label: "Taux d'actualisation k (%)"})
```

``` js
{
  const flows = [3000, 3500, 4000, 4000, 3000];
  const I0 = 10000;

  // Bissection pour trouver le TRI
  let lo = 0, hi = 1;
  for (let i = 0; i < 200; i++) {
    const mid = (lo + hi) / 2;
    if (van(I0, flows, mid) > 0) lo = mid; else hi = mid;
  }
  const tri = (lo + hi) / 2;

  const pts = Array.from({length: 101}, (_, i) => ({x: i * 0.5, v: van(I0, flows, i * 0.005)}));
  const k = s3_k / 100;
  const v = van(I0, flows, k);

  return Plot.plot({
    width: 900, height: 320, marginLeft: 70,
    style: {background: "transparent", color: "currentColor"},
    x: {label: "Taux k (%)", domain: [0, 50]},
    y: {label: "↑ VAN (€)", grid: true, tickFormat: d => fmt(d)},
    title: "Le TRI est l'abscisse où la courbe coupe l'axe",
    marks: [
      Plot.areaY(pts, {x: "x", y1: 0, y2: d => Math.max(d.v, 0), fill: "#5b9bdb", fillOpacity: 0.15}),
      Plot.ruleY([0], {stroke: "#8b8f9c"}),
      Plot.line(pts, {x: "x", y: "v", stroke: "#5b9bdb", strokeWidth: 2.5}),
      Plot.ruleX([tri * 100], {stroke: "#f0a500", strokeDasharray: "4,3"}),
      Plot.dot([{x: tri * 100, y: 0}], {x: "x", y: "y", r: 7, fill: "#f0a500"}),
      Plot.text([{x: tri * 100, y: 0}], {x: "x", y: "y", text: () => `TRI ≈ ${pct(tri)}`, dx: 10, fontSize: 13, fontWeight: "bold", fill: "#f0a500"}),
      Plot.dot([{x: s3_k, y: v}], {x: "x", y: "y", r: 6, fill: "#5bdb6d", stroke: "white", strokeWidth: 1.5}),
      Plot.text([{x: s3_k, y: v}], {x: "x", y: "y", text: () => eur(v), dy: -14, fontSize: 12, fill: "currentColor"})
    ]
  });
}
```

``` js
{
  const flows = [3000, 3500, 4000, 4000, 3000];
  let lo = 0, hi = 1;
  for (let i = 0; i < 200; i++) {
    const mid = (lo + hi) / 2;
    if (van(10000, flows, mid) > 0) lo = mid; else hi = mid;
  }
  const tri = (lo + hi) / 2;
  return md`<div class="ojs-result">TRI ≈ **${pct(tri)}** · à k = ${pct(s3_k / 100, 1)} : VAN = <span class="${van(10000, flows, s3_k/100) >= 0 ? "green" : "red"}">**${eur(van(10000, flows, s3_k/100))}**</span> → ${van(10000, flows, s3_k/100) >= 0 ? "accepter" : "rejeter"}</div>`;
}
```

## 3.4 Exemple résolu — Le food-truck

> Food-truck à **10 000 €**, **6 000 €/an** pendant **2 ans**.

| Taux testé |       VAN |
|-----------:|----------:|
|       12 % | +140,31 € |
|       14 % | −120,04 € |

$$TRI \approx 12\,\% + 2\,\% \times \frac{140{,}31}{140{,}31 + 120{,}04} \approx \mathbf{13{,}08\,\%}$$

Si $k = 10\,\%$ : $TRI > k$ → ✅ projet acceptable.

## 3.5 Quatre limites du TRI

1.  **Plusieurs TRI possibles** — si les flux changent de signe plus d’une fois.

2.  **Absence de TRI** — certains profils de flux n’ont pas de solution.

3.  **Conflit VAN / TRI** — projets mutuellement exclusifs de tailles différentes :

    | Projet | VAN à 10 % |  TRI |
    |--------|-----------:|-----:|
    | A      |   80 000 € | 25 % |
    | B      |  120 000 € | 18 % |

    La VAN choisit B, le TRI choisit A.

4.  **Hypothèse de réinvestissement** — le TRI suppose réinvestir au taux $r$ lui-même (irréaliste si $r$ est élevé). La VAN suppose réinvestir au coût du capital $k$ (plus réaliste).

En cas de conflit : la **VAN est prioritaire** — elle mesure l’enrichissement absolu.

## 3.6 🪤 Le piège

« Le TRI dépasse le taux exigé, donc le projet est bon — pas besoin de la VAN. »

Le TRI suppose un réinvestissement au TRI même et peut classer à tort deux projets de tailles différentes. La VAN actualise au coût du capital.

VAN pour décider, TRI pour communiquer.

## 3.7 🧠 Vérifiez votre compréhension

> Machine à 50 000 €, 15 000 €/an × 5 ans. À k = 12 %, que vaut la VAN ? Le projet est-il acceptable ? Et à k = 18 % ?

- k = 12 % : VAN ≈ **+4 072 €** → ✅ (TRI = 15,24 % \> 12 %)
- k = 18 % : VAN ≈ **−2 700 €** → ❌ (TRI \< 18 %)

4 Séquence 4\
Délai de récupération et comparaison de projets
===============================================

Récupérer vite = gagner plus ?

## 4.1 Rapide ou Durable ?

Une PME dispose de **40 000 €**. Deux projets :

- **Rapide** : 20 000 €/an × 2 ans, puis 5 000 € en an 3.
- **Durable** : 12 000 €/an × 6 ans.

Le banquier : *« Prenez celui qui rend la mise le plus vite, c’est le moins risqué. »*

Faut-il suivre le banquier ?

Votre pronostic   ① Rapide   ② Durable   ③ Égal

## 4.2 Cumul des flux

| Année | Rapide : flux | Rapide : cumul | Durable : flux | Durable : cumul |
|-------|--------------:|---------------:|---------------:|----------------:|
| 1     |      20 000 € |       20 000 € |       12 000 € |        12 000 € |
| 2     |      20 000 € |   **40 000 €** |       12 000 € |        24 000 € |
| 3     |       5 000 € |       45 000 € |       12 000 € |        36 000 € |
| 4     |             — |              — |       12 000 € |    **48 000 €** |
| 5     |             — |              — |       12 000 € |        60 000 € |
| 6     |             — |              — |       12 000 € |        72 000 € |

- DRS Rapide = **2 ans** pile.
- DRS Durable ≈ **3,33 ans**.

## 4.3 …mais en euros d’aujourd’hui (k = 8 %)

| Année | Rapide : VA cumulée | Durable : VA cumulée |
|-------|--------------------:|---------------------:|
| 1     |            18 519 € |             11 111 € |
| 2     |            35 665 € |             21 399 € |
| 3     |            39 634 € |             30 925 € |
| 4     |                   — |             39 746 € |
| 5     |                   — |         **47 913 €** |
| 6     |                   — |             55 475 € |

- Rapide **ne récupère jamais** ses 40 000 € : $VAN = -366$ € ❌
- Durable franchit le seuil en **≈ 4,03 ans** (DRA) : $VAN = +15\,475$ € ✅

## 4.4 DRS et DRA

### 4.4.1 Délai de récupération simple

$$DRS : \sum_{t=1}^{DRS} CF_t \geq I_0$$

Cumule les flux **tels quels**.

### 4.4.2 Délai de récupération actualisé

$$DRA : \sum_{t=1}^{DRA} \frac{CF_t}{(1+k)^t} \geq I_0$$

Cumule les flux **actualisés**. Toujours ≥ DRS.

| Critère | Intérêt | Limite |
|----|----|----|
| DRS / DRA | Mesure la **liquidité**, pertinent en environnement risqué | Ignore les flux **après** le délai ; ne mesure pas la création de valeur |

:::

## 4.5 Comparer des projets de durées différentes

Quand deux projets ont des durées différentes, la VAN brute n’est pas comparable directement → **annuité équivalente (AE)** :

$$AE = VAN \times \frac{k}{1-(1+k)^{-n}}$$

L’AE est la **rente annuelle constante** équivalente à la VAN du projet.

**Exemple** — Rapide vs Durable à 8 % : AE ≈ **−142 €/an** contre **+3 347 €/an**. → Durable crée de la valeur **par an**.

## 4.6 🪤 Le piège

« Le projet qui rembourse le plus vite est le meilleur, puisqu’il est le moins risqué. »

Le délai ignore tout ce qui se passe **après** le remboursement. Ici, Rapide récupère en 2 ans mais **détruit** de la valeur.

Le délai mesure la **liquidité**, pas la création de valeur.

## 4.7 🧠 Vérifiez votre compréhension

> Projet à 10 000 €, flux 4 000 / 5 000 / 6 000 €, k = 10 %. DRS et DRA ?

- DRS = 2 + (10 000 − 9 000)/6 000 ≈ **2,17 ans**
- DRA = 2 + (10 000 − 7 768,60)/4 507,89 ≈ **2,50 ans**

Le délai actualisé est plus long : actualiser réduit le poids des flux.

# 5 Pause déjeuner 🍽️

6 Séquence 5\
Analyse du risque
=================

Jusqu’où les ventes peuvent-elles baisser ?

## 6.1 La machine, face à l’incertitude

Les **15 000 €/an** de la machine reposent sur **2 000 pièces vendues** à **12 € de marge**, moins **9 000 € de charges fixes**.

Un concurrent vient d’ouvrir. **Si les ventes baissaient de 20 %, le projet tiendrait-il encore ?**

Votre pronostic   ① Oui, largement   ② De justesse   ③ Non

## 6.2 Ventes −20 % : effet de levier des charges fixes

$$2\,000 \times 12 - 9\,000 = 15\,000\ € \quad\longrightarrow\quad 1\,600 \times 12 - 9\,000 = 10\,200\ €$$

| Volume               | Flux annuel | VAN (k = 8 %) |
|----------------------|------------:|--------------:|
| 2 000 pièces (prévu) |    15 000 € |  **+9 891 €** |
| 1 600 pièces (−20 %) |    10 200 € |  **−9 274 €** |

Une baisse de 20 % des ventes fait chuter le flux de **32 %** et fait basculer la VAN dans le négatif.

## 6.3 Valeur seuil (break-even)

Quel flux annuel rend la VAN nulle ?

$$\text{flux seuil} = \frac{50\,000}{3{,}9927} \approx 12\,523\ €
\quad\Rightarrow\quad \text{volume seuil} \approx \mathbf{1\,794\ pièces}$$

≈ 10 %

marge de sécurité sur le volume — le projet ne supporte qu’une baisse de ~10 %

## 6.4 Trois outils, trois questions 🎛️

``` js
viewof s5_vol = Inputs.range([-30, 30], {value: 0, step: 1, label: "Volume vendu (%)"})
viewof s5_marge = Inputs.range([-30, 30], {value: 0, step: 1, label: "Marge unitaire (%)"})
viewof s5_fixes = Inputs.range([-30, 30], {value: 0, step: 1, label: "Charges fixes (%)"})
```

``` js
{
  const base = {vol: 2000, marge: 12, fixes: 9000, I0: 50000, k: 0.08, n: 5};
  const p = {
    vol: base.vol * (1 + s5_vol / 100),
    marge: base.marge * (1 + s5_marge / 100),
    fixes: base.fixes * (1 + s5_fixes / 100),
    ...base
  };
  const flux = p.vol * p.marge - p.fixes;
  const facteur = (1 - Math.pow(1 + p.k, -p.n)) / p.k;
  const v = -p.I0 + flux * facteur;
  const seuil = (p.I0 / facteur + p.fixes) / p.marge;
  const margeSecu = 1 - seuil / p.vol;

  // Tornade
  const v0 = v;
  const facteurs = [
    {label: "Volume", bas: van(p.I0, Array(p.n).fill(base.vol * (1 - 0.2) * p.marge - p.fixes), p.k) - (-p.I0 + flux * facteur), haut: van(p.I0, Array(p.n).fill(base.vol * (1 + 0.2) * p.marge - p.fixes), p.k) - (-p.I0 + flux * facteur)},
    {label: "Marge", bas: van(p.I0, Array(p.n).fill(p.vol * base.marge * 0.8 - p.fixes), p.k) - (-p.I0 + flux * facteur), haut: van(p.I0, Array(p.n).fill(p.vol * base.marge * 1.2 - p.fixes), p.k) - (-p.I0 + flux * facteur)},
    {label: "Charges fixes", bas: van(p.I0, Array(p.n).fill(p.vol * p.marge - base.fixes * 0.8), p.k) - (-p.I0 + flux * facteur), haut: van(p.I0, Array(p.n).fill(p.vol * p.marge - base.fixes * 1.2), p.k) - (-p.I0 + flux * facteur)}
  ].sort((a, b) => Math.max(Math.abs(a.bas), Math.abs(a.haut)) - Math.max(Math.abs(b.bas), Math.abs(b.haut)));

  const ordre = facteurs.map(f => f.label).reverse();
  const tornado = Plot.plot({
    width: 900, height: 180, marginLeft: 120,
    style: {background: "transparent", color: "currentColor"},
    x: {label: "Δ VAN (€) autour du cas affiché", grid: true, tickFormat: d => fmt(d)},
    y: {domain: ordre},
    marks: [
      Plot.barX(facteurs, {y: "label", x1: 0, x2: "bas", fill: "#db5b5b", fillOpacity: 0.8}),
      Plot.barX(facteurs, {y: "label", x1: 0, x2: "haut", fill: "#5bdb6d", fillOpacity: 0.8}),
      Plot.ruleX([0], {stroke: "currentColor"})
    ]
  });

  return html`<div>
    <div style="border-left:4px solid #5b9bdb; padding:8px 14px; margin:8px 0; font-size:0.85em;">
      Flux annuel = ${fmt(p.vol)} × ${fmt(p.marge, 2)} € − ${fmt(p.fixes)} € = <b>${eur(flux)}</b><br>
      VAN = <b class="${v >= 0 ? "green" : "red"}">${eur(v)}</b> ·
      Volume seuil ≈ <b>${fmt(seuil)} pièces</b> ·
      Marge de sécurité <b>${pct(margeSecu * 100, 1)}</b>
    </div>
    ${tornado}
  </div>`;
}
```

Le diagramme en tornade fait varier un seul facteur à ±20 % : les barres les plus longues = les hypothèses à sécuriser en priorité. Ici volume et marge pèsent autant (leur produit = la recette).

## 6.5 Analyse par scénarios

| Scénario   | Volume | Flux annuel |       VAN | Proba. |
|------------|-------:|------------:|----------:|-------:|
| Pessimiste |  1 600 |    10 200 € |  −9 274 € |   0,25 |
| Central    |  2 000 |    15 000 € |  +9 891 € |   0,50 |
| Optimiste  |  2 300 |    18 600 € | +24 264 € |   0,25 |

$$E(VAN) = \sum p_s \cdot VAN_s \approx \mathbf{8\,693\ €} \qquad
\sigma(VAN) = \sqrt{\sum p_s (VAN_s - E(VAN))^2} \approx \mathbf{11\,918\ €}$$

La VAN espérée est positive, mais **l’écart-type dépasse la moyenne** et la probabilité de VAN négative est de **25 %**.

## 6.6 Limites de l’espérance

« La VAN espérée est positive, donc le projet est sûr. »

L’espérance est une **moyenne** : deux projets de même VAN espérée peuvent avoir des dispersions très différentes. Toujours regarder : - le **scénario défavorable** (perte maximale), - la **probabilité de VAN \< 0**, - la **capacité financière** à absorber un échec.

Regarde la moyenne **ET** la dispersion.

7 Séquence 6\
Cas intégrateur : automatisation logistique
===========================================

Une recommandation complète, de la donnée à la décision.

## 7.1 Le contexte

Automatisation d’une partie du processus logistique.

| Paramètre                          |       Valeur |
|------------------------------------|-------------:|
| Investissement (robots + logiciel) |    850 000 € |
| Frais d’installation               |     50 000 € |
| Hausse initiale du BFR             |     40 000 € |
| Durée                              |        5 ans |
| Économies annuelles                | 280 000 €/an |
| Maintenance                        |  30 000 €/an |
| Valeur résiduelle nette            |     60 000 € |
| CMPC                               |          8 % |
| IS                                 |         25 % |

## 7.2 Étape 1 — Les flux

- $I_0 = 850\,000 + 50\,000 + 40\,000 = \mathbf{940\,000\ €}$
- Dotation = $900\,000 / 5 = 180\,000$ €/an
- RE = $(280\,000 - 30\,000) - 180\,000 = 70\,000$ € → IS = 17 500 € → RN = 52 500 €
- $CF_t = 52\,500 + 180\,000 = \mathbf{232\,500\ €}$/an
- $CF_5^{total} = 232\,500 + 60\,000 + 40\,000 = \mathbf{332\,500\ €}$

## 7.3 Étape 2 — Évaluation

| Indicateur |                Valeur |
|------------|----------------------:|
| **VAN**    |      **+56 363 €** ✅ |
| IP         |                 1,060 |
| TRI        | ≈ 9,5 % (\> CMPC 8 %) |
| DRS        |            ≈ 4,04 ans |

## 7.4 Étape 3 — Risque

| Scénario   | Économies |        VAN | Proba. |
|------------|----------:|-----------:|-------:|
| Pessimiste | 200 000 € | −138 000 € |   25 % |
| Central    | 280 000 € |  +56 000 € |   50 % |
| Optimiste  | 360 000 € | +250 000 € |   25 % |

$E(VAN) = 55\,000$ € · $\sigma(VAN) \approx 136\,000$ € · Proba. VAN \< 0 ≈ **25 %**

**Variable critique** : les économies réalisées. Une baisse de 30 % fait basculer la VAN en négatif.

## 7.5 Étape 4 — Recommandation

**Investir, sous réserve de sécuriser l’hypothèse d’économies sur l’année 1** (pilote sur un entrepôt avant déploiement complet).

- ✅ VAN centrale positive, TRI \> CMPC, VAN espérée positive
- ⚠️ Marge de sécurité mince (TRI 9,5 % vs CMPC 8 %)
- ⚠️ Scénario pessimiste négatif → vérifier la capacité d’absorption
- 🎯 Sécuriser **l’hypothèse clé** avant engagement (bench fournisseur, visites de référence)

8 Séquence 7\
Synthèse et évaluation
======================

Les 8 réflexes d’une décision financière robuste.

## 8.1 La grille de décision

| \#  | Réflexe                                                         |
|-----|-----------------------------------------------------------------|
| 1   | **Identifier les flux différentiels** (entrées/sorties réelles) |
| 2   | **Positionner les flux dans le temps** (ligne du temps)         |
| 3   | **Choisir un taux cohérent** (CMPC, taux exigé…)                |
| 4   | **Actualiser tous les flux** à la date de référence             |
| 5   | **Calculer plusieurs indicateurs** (VAN, TRI, DRS, IP)          |
| 6   | **Tester les hypothèses** (sensibilité, scénarios, seuils)      |
| 7   | **Apprécier les risques non quantifiés**                        |
| 8   | **Formuler une recommandation** claire et argumentée            |

Pourquoi aucun indicateur unique ne suffit ?

## 8.2 Carte mentale du cours

#### 💰 VAN

$VAN = -I_0 + \sum \frac{CF_t}{(1+k)^t}$

Enrichissement **absolu**.

#### 📈 TRI

Taux qui annule la VAN.

Rendement **relatif** — limites connues.

#### ⏱️ Délai

DRS / DRA.

Mesure la **liquidité**, pas la valeur.

#### 🎲 Risque

Sensibilité · seuils · scénarios.

E(VAN) **et** σ(VAN).

## 8.3 Les erreurs qui coûtent cher

### 8.3.1 Construction des flux

- Amortissements comptés en **sortie de trésorerie**
- **BFR oublié** au démarrage
- **Double comptage** de l’investissement
- Valeur résiduelle **omise**
- Sunk costs dans les flux **futurs**

### 8.3.2 Décision

- Comparer des flux de **dates différentes** sans actualiser
- Décider sur le **TRI seul** pour des projets de tailles différentes
- Confondre **VAN espérée positive** et projet « sûr »
- Oublier de **tester les hypothèses critiques**

## 8.4 Cinq réflexes à acquérir

1.  ✏️ **Tracer la ligne du temps** avant toute formule.
2.  💶 **Ne compter que les flux différentiels réels**.
3.  📊 **Décider sur la VAN** — le TRI et le délai sont des compléments.
4.  🎲 **Tester les hypothèses** : sensibilité, seuils, scénarios.
5.  📝 **Formuler une recommandation** chiffrée et nuancée.

# 9 Exercices

Du plus direct au plus ouvert. Classeur Excel disponible dans le cours.

## 9.1 Niveau 1 — Application directe

**1.1** — Projet à **80 000 €**, flux 30 000 / 35 000 / 40 000 € sur 3 ans, k = 10 %. Calculez la VAN et le DRS.

- VAN = −80 000 + 27 273 + 28 926 + 30 053 ≈ **+6 252 €** ✅
- DRS = 2 + (80 000 − 65 000)/40 000 = **2,375 ans**

## 9.2 Niveau 2 — Projet A vs Projet B

Deux projets mutuellement exclusifs, k = 12 %.

|  An |   Projet A |   Projet B |
|----:|-----------:|-----------:|
|   0 | −100 000 € | −150 000 € |
|   1 |   50 000 € |   40 000 € |
|   2 |   50 000 € |   60 000 € |
|   3 |   50 000 € |   80 000 € |
|   4 |          — |   60 000 € |

- VAN A ≈ **+20 090 €** · AE A ≈ 8 360 €/an
- VAN B ≈ **+28 643 €** · AE B ≈ 9 431 €/an
- 🏆 **Projet B** (VAN et AE toutes deux supérieures)

## 9.3 Niveau 3 — Ligne d’embouteillage (étude de cas)

PME agroalimentaire, ligne à **500 000 €** + 20 000 € installation + 30 000 € BFR. 6 ans, revenus 180 000 €/an, coûts variables 60 000 €/an, VR 40 000 €, IS 25 %, k = 9 %.

Scénarios : pessimiste 140 000 € (30 %) · central 180 000 € (50 %) · optimiste 220 000 € (20 %).

**Travail** : flux → VAN/TRI/DRS central → VAN des 3 scénarios → E(VAN) et σ(VAN) → valeur seuil → note de recommandation (10 lignes max).

- VAN centrale ≈ **−7 389 €** · TRI ≈ 8,4 % \< 9 % · E(VAN) ≈ **−18 300 €**
- Proba. VAN \< 0 = 80 % → **ne pas investir** en l’état (ou renégocier \< 543 000 €)

## 9.4 📖 Pour aller plus loin

Théorie complète, démonstrations interactives, classeur Excel et corrections détaillées :

[→ Module 3 : Choix d’investissement](../module-03.qmd)

[→ Classeur Excel](../modele-choix-investissement.xlsx) · [→ Formulaire](../../../teaching/mathematical-finance/formulaire.llms.md) · [→ Glossaire](../../../teaching/mathematical-finance/glossaire.llms.md)

Décider, c’est comparer des flux de dates différentes — ramenés à aujourd’hui, testés, puis assumés.

## Citation

BibTeX citation:

``` quarto-appendix-bibtex
@online{gilles,
  author = {Gilles, Guillaume},
  title = {Choix d’investissement},
  url = {https://ggilles.dev/teaching/mathematical-finance/slides/module-03.html},
  langid = {en}
}
```

For attribution, please cite this work as:

Gilles, Guillaume. n.d. “Choix d’investissement.” <https://ggilles.dev/teaching/mathematical-finance/slides/module-03.html>.
