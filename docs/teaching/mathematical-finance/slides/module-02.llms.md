``` js
fmt = (x, d = 0) =>
  x.toLocaleString("fr-FR", {minimumFractionDigits: d, maximumFractionDigits: d})
pct = (x, d = 2) => fmt(100 * x, d) + " %"
pvFlows = (flows, r) => flows.reduce((s, f, k) => s + f / (1 + r) ** (k + 1), 0)
```

## 0.1 Quelle offre choisir ?

Sans calculer — votez à main levée, puis justifiez.

Une entreprise emprunte **50 000 €** sur **4 ans**, échéances annuelles constantes.

BANQUE A

4,0 %

\+ 1 500 € de frais de dossier

BANQUE B

4,5 %

aucun frais

Le taux affiché le plus bas n’est pas forcément le moins cher. **Nous trancherons en Séquence 4.**

Vote à main levée (2 min). Noter la répartition A/B au tableau : on y revient en Séquence 4 avec le taux actuariel (A ≈ 5,30 %, B = 4,50 %).

## 0.2 Objectifs de la journée

À la fin de cette journée, vous saurez :

1.  construire un **tableau d’amortissement** (annuités constantes, amortissement constant) ;
2.  distinguer **intérêt, amortissement et annuité** à chaque échéance ;
3.  comparer des **modalités de remboursement** : coût, trésorerie, risque ;
4.  calculer le **taux actuariel** d’un emprunt avec frais ;
5.  **valoriser une obligation** à taux fixe ;
6.  mesurer sa **sensibilité aux taux** (duration de Macaulay, duration modifiée).

## 0.3 Programme de la journée

### 0.3.1 Matin — 3 h

| Séquence                |       Durée |
|-------------------------|------------:|
| 1 · Réactivation        |      20 min |
| 2 · Annuités constantes |      60 min |
| 3 · Autres modalités    |      45 min |
| 4 · Taux actuariel      |      55 min |
| **Total**               | **180 min** |

### 0.3.2 Après-midi — 3 h

| Séquence             |       Durée |
|----------------------|------------:|
| 5 · Obligations      |      50 min |
| 6 · Sensibilité      |      45 min |
| 7 · Étude de cas     |      60 min |
| Exercices & synthèse |      25 min |
| **Total**            | **180 min** |

6 h de face-à-face. Pauses non comptées : à prendre sur le temps de discussion des séquences 3 et 6 si nécessaire.

Si le groupe prend du retard : la démonstration interactive de la Séquence 3 et la vérification de la Séquence 5 sont compressibles (5 min chacune). Le niveau 3 des exercices est prévu en travail personnel.

## 0.4 La règle d’or

✏️ La **ligne du temps** avant toute formule.

\+ C₀\
reçu

t = 0

← actualiser

− A

t = 1

 

− A

t = 2

…

− A

t = n

1.  Placez **chaque flux** (emprunt, échéance, frais, coupon, nominal) **à sa date**.
2.  Notez son **sens** : reçu (+) ou versé (−).
3.  *Ensuite seulement* : ramenez tout à **une même date**.

Insister : frais oubliés, décalage d’une période, nominal omis… toutes les erreurs de la journée se voient sur ce schéma.

1 Séquence 1\
Réactivation des acquis
=======================

Les outils du Module 1 sont-ils encore là ?

20 min : quiz 8 min (autonomie), correction 7 min, erreurs fréquentes 5 min.

## 1.1 Quiz de réactivation ⚡

Ordre de grandeur suffisant

| Question | Réponse |
|----|----|
| 10 000 € placés 3 ans à 4 % valent… | $10\,000 \times 1{,}04^3 \approx 11\,249$ € |
| Valeur actuelle de 12 000 € reçus dans 2 ans à 6 % ? | $12\,000 / 1{,}06^2 \approx 10\,680$ € |
| Taux mensuel équivalent à 6 % annuel ? | $1{,}06^{1/12} - 1 \approx 0{,}487\,\%$ (≈ 0,5 %) |
| Perpétuité de 500 €/an au taux de 5 % ? | $500 / 0{,}05 = 10\,000$ € |

Capitaliser, actualiser, convertir un taux, valoriser une rente : **toute la journée s’appuie sur ces quatre gestes.**

## 1.2 Erreurs à corriger avant de continuer

1.  **Capitalisation ≠ actualisation** — capitaliser va vers le futur ($C_n = C_0(1+i)^n$), actualiser revient au présent ($V_0 = V_n/(1+i)^n$).
2.  **Convertir le taux** — échéances trimestrielles + taux annuel → taux trimestriel *équivalent*.
3.  **Décalage d’une période** — premier versement en début ou en fin de période ?
4.  **Pourcentage non converti** — $i = 5\,\%$ → $0{,}05$, *pas* $5$.

2 Séquence 2\
Emprunt à annuités constantes
=============================

Quelle part de chaque échéance rembourse vraiment la dette ?

60 min : situation + exploration 20 min, formule et structure 15 min, exemple résolu 15 min, piège + vérification 10 min.

## 2.1 Le camion de la PME

Une PME de livraison emprunte **60 000 €** pour un camion frigorifique : **3 ans**, **5 % par an**, **échéance identique chaque année**.

La gérante veut savoir combien elle versera, et quelle part de chaque versement réduit sa dette plutôt que de rémunérer la banque.

Combien d’intérêts paiera-t-elle au total ?

Votre pronostic   ① 3 000 €   ② ≈ 6 100 €   ③ 9 000 €   ④ 15 000 €

## 2.2 Une échéance, deux fonctions

### 2.2.1 Payer les intérêts

Intérêts de l’année = **dette restant due** en début d’année × taux

### 2.2.2 Rembourser la dette

Ce qui reste de l’échéance **après** les intérêts rembourse le capital

La banque calcule une échéance de **22 032,51 €** : le seul montant constant qui ramène la dette **exactement à zéro** en 3 ans. (D’où vient-il ? Réponse dans quelques minutes.)

## 2.3 Le prêt, année par année

| Année | Dette début | Intérêts (× 5 %) | Remboursement |  Échéance | Dette fin |
|------:|------------:|-----------------:|--------------:|----------:|----------:|
|     1 |   60 000,00 |         3 000,00 |     19 032,51 | 22 032,51 | 40 967,49 |
|     2 |   40 967,49 |         2 048,37 |     19 984,14 | 22 032,51 | 20 983,35 |
|     3 |   20 983,35 |         1 049,17 |     20 983,35 | 22 032,51 |      0,00 |

6 097,54 €

d’intérêts au total (réponse ②)

- La part **intérêts fond** : 3 000 → 1 049 €.
- La part **remboursement grossit** : 19 033 → 20 983 €.

Faire calculer la ligne 1 par les étudiants avant de révéler. Les trois gestes : intérêts = dette × taux ; remboursement = échéance − intérêts ; nouvelle dette = ancienne − remboursement.

## 2.4 D’où vient 22 032,51 € ?

Les 60 000 € reçus aujourd’hui = **valeur actuelle** des 3 échéances futures.

\+ 60 000

t = 0

÷ 1,05

− A

t = 1

÷ 1,05

− A

t = 2

÷ 1,05

− A

t = 3

$$60\,000 = \frac{A}{1{,}05} + \frac{A}{1{,}05^2} + \frac{A}{1{,}05^3}
= A \cdot \frac{1 - 1{,}05^{-3}}{0{,}05}$$

$$A = 60\,000 \times \frac{0{,}05}{1 - 1{,}05^{-3}} \approx 22\,032{,}51\ €$$

## 2.5 La formule de l’annuité constante

$$A = C_0 \cdot \frac{i}{1-(1+i)^{-n}}$$

$C_0$ montant emprunté · $i$ taux **par période** · $n$ nombre d’échéances · $A$ échéance constante de **fin** de période

C’est l’**inversion** de la valeur actuelle d’une suite d’annuités (Module 1) : $C_0 = A \cdot \dfrac{1-(1+i)^{-n}}{i}$.

Si $n$ augmente → $A$ baisse… mais le total des intérêts **augmente**.

## 2.6 Structure d’une échéance

À la période $t$, avec $CRD_0 = C_0$ et $CRD_n = 0$ :

| Composante                 | Formule              |
|----------------------------|----------------------|
| Intérêts $I_t$             | $CRD_{t-1} \times i$ |
| Amortissement $Am_t$       | $A - I_t$            |
| Capital restant dû $CRD_t$ | $CRD_{t-1} - Am_t$   |

Annuité **fixe**, composition **qui bascule** des intérêts vers le capital.

## 2.7 Exemple résolu — Tableau d’amortissement

> **100 000 €** sur **5 ans** à **4 %**, annuités constantes.

$$A = 100\,000 \times \frac{0{,}04}{1-1{,}04^{-5}} = 100\,000 \times \frac{0{,}04}{0{,}17807} \approx 22\,463\ €$$

| Période | CRD début | Intérêts | Amortissement | Annuité | CRD fin |
|--------:|----------:|---------:|--------------:|--------:|--------:|
|       1 |   100 000 |    4 000 |        18 463 |  22 463 |  81 537 |
|       2 |    81 537 |    3 261 |        19 202 |  22 463 |  62 335 |
|       3 |    62 335 |    2 493 |        19 970 |  22 463 |  42 365 |
|       4 |    42 365 |    1 695 |        20 768 |  22 463 |  21 597 |
|       5 |    21 597 |      864 |        21 599 |  22 463 |     0\* |

\*Écart de 2 € dû à l’arrondi de l’annuité : on ajuste la dernière échéance.

Coût total des intérêts : $22\,463 \times 5 - 100\,000 =$ **12 315 €**

## 2.8 Lire le tableau

- **Début d’emprunt** : intérêts élevés (base = capital total), amortissement faible.
- **Fin d’emprunt** : intérêts faibles (CRD réduit), l’amortissement fait presque toute l’annuité.
- **Si la durée change, le coût change** :

| Prêt de 60 000 € à 5 % |     Annuité | Intérêts totaux |
|------------------------|------------:|----------------:|
| sur 3 ans              | 22 032,51 € |      6 097,54 € |
| sur 4 ans              | 16 920,71 € |      7 682,84 € |

## 2.9 🪤 Le piège

« L’échéance est constante, donc chaque année je rembourse la même part de capital et je paie les mêmes intérêts. »

Les intérêts portent sur le **capital restant dû**, qui diminue à chaque échéance : la part d’intérêts baisse, la part d’amortissement augmente d’autant.

L’annuité est fixe, sa composition bascule.

## 2.10 🧠 Vérifiez votre compréhension

> **10 000 €** sur **2 ans** à **6 %**, annuités constantes. Annuité ? Intérêts et amortissement de chaque année ?

$A = 10\,000 \times \dfrac{0{,}06}{1 - 1{,}06^{-2}} \approx$ **5 454,37 €**

| Année | Intérêts | Amortissement |  CRD fin |
|------:|---------:|--------------:|---------:|
|     1 |   600,00 |      4 854,37 | 5 145,63 |
|     2 |   308,74 |      5 145,63 |     0,00 |

3 Séquence 3\
Autres modalités de remboursement
=================================

Quand la première année est la plus difficile…

45 min : situation + tableau 12 min, démo 5 min, formules 10 min, exemple résolu 8 min, comparaison + piège + vérification 10 min.

## 3.1 Trois formules pour le même prêt

Même prêt : **60 000 €**, **3 ans**, **5 %**. Le banquier propose :

- **échéances identiques** chaque année ;
- **capital par tiers** (20 000 €/an) + intérêts ;
- **intérêts seuls** pendant 3 ans, capital remboursé **en une fois** à la fin.

La première année, la trésorerie est tendue : le camion doit d’abord trouver ses clients.

Quelle formule choisir, et à quel prix ?

Votre choix

## 3.2 Ce que la PME décaisse

| Année | Échéances identiques | Capital par tiers + intérêts | Intérêts seuls, capital à la fin |
|---:|---:|---:|---:|
| 1 | 22 032,51 | 20 000 + 3 000 = **23 000** | **3 000** |
| 2 | 22 032,51 | 20 000 + 2 000 = 22 000 | 3 000 |
| 3 | 22 032,51 | 20 000 + 1 000 = 21 000 | 60 000 + 3 000 = **63 000** |
| **Total versé** | 66 097,54 | 66 000 | 69 000 |
| **dont intérêts** | 6 097,54 | 6 000 | 9 000 |

Actualisons chaque colonne à 5 % :

$$\frac{3\,000}{1{,}05} + \frac{3\,000}{1{,}05^2} + \frac{63\,000}{1{,}05^3} = 60\,000\ €$$

Les trois colonnes valent **exactement 60 000 €** : même coût actuariel.

Réponse : l’in fine soulage le plus l’année 1. Son « prix » n’est pas un taux plus élevé mais un risque de refinancement concentré sur l’année 3 (63 000 €).

## 3.3 Comparer les modalités 🎛️

``` js
viewof mod_C = Inputs.range([10000, 200000], {value: 60000, step: 5000, label: "Montant emprunté C₀ (€)"})
viewof mod_i = Inputs.range([0.01, 0.10], {value: 0.05, step: 0.005, label: "Taux annuel i"})
viewof mod_n = Inputs.range([2, 10], {value: 3, step: 1, label: "Durée n (années)"})
```

``` js
mod_names = ["Annuités constantes", "Amortissement constant", "In fine"]
mod_A = mod_C * mod_i / (1 - (1 + mod_i) ** -mod_n)
mod_data = Array.from({length: mod_n}, (_, k) => [
  {t: k + 1, modalite: mod_names[0], echeance: mod_A},
  {t: k + 1, modalite: mod_names[1], echeance: mod_C / mod_n + mod_C * (1 - k / mod_n) * mod_i},
  {t: k + 1, modalite: mod_names[2], echeance: mod_C * mod_i + (k + 1 === mod_n ? mod_C : 0)}
]).flat()
mod_int = (m) => d3.sum(mod_data.filter(d => d.modalite === m), d => d.echeance) - mod_C

Plot.plot({
  width: 900, height: 280, marginLeft: 70,
  fx: {label: "Année →"},
  x: {axis: null, domain: mod_names},
  y: {label: "↑ Échéance (€)", grid: true, tickFormat: d => fmt(d)},
  color: {domain: mod_names, range: ["#5bdb6d", "#5b9bdb", "#f0a500"], legend: true},
  marks: [
    Plot.barY(mod_data, {fx: "t", x: "modalite", y: "echeance", fill: "modalite", tip: true})
  ]
})
```

``` js
md`<div class="ojs-result">Intérêts totaux : annuités constantes **${fmt(mod_int(mod_names[0]))} €** · amortissement constant **${fmt(mod_int(mod_names[1]))} €** · in fine <span class="orange">**${fmt(mod_int(mod_names[2]))} €**</span></div>`
```

Faire tester : allonger la durée (3 → 10 ans). L’écart d’intérêts en euros se creuse, mais au même taux les trois ont le même coût actuariel. Observer la « falaise » de l’in fine à la dernière année.

## 3.4 Trois règles de remboursement

### 3.4.1 Amortissement constant

$$Am = \frac{C_0}{n}$$

$A_t = \dfrac{C_0}{n} + CRD_{t-1} \times i$

Échéances **décroissantes**

### 3.4.2 In fine

$$I_t = C_0 \times i$$

Dernière échéance : $C_0 \times i + C_0 = C_0(1+i)$

**Falaise** finale

### 3.4.3 Différé

**Partiel** : on paie les intérêts, on n’amortit pas.

**Total** : aucun flux ; le capital devient $C_0(1+i)^d$.

Dans tous les cas : échéance = $Am_t + CRD_{t-1} \times i$, avec $\sum Am_t = C_0$. Seul change le **rythme** de remboursement du capital.

## 3.5 Exemple résolu — 90 000 € sur 3 ans à 4 %

**Amortissement constant** : $Am = 90\,000 / 3 = 30\,000$ €

| Période | CRD début | Intérêts | Amort. | Échéance |
|--------:|----------:|---------:|-------:|---------:|
|       1 |    90 000 |    3 600 | 30 000 |   33 600 |
|       2 |    60 000 |    2 400 | 30 000 |   32 400 |
|       3 |    30 000 |    1 200 | 30 000 |   31 200 |

Intérêts : **7 200 €**

**In fine**

- Années 1 et 2 : $90\,000 \times 0{,}04 = 3\,600$ €
- Année 3 : $90\,000 \times 1{,}04 = 93\,600$ €

Intérêts : **10 800 €**

**Annuités constantes** (pour comparer)

$A \approx 32\,431$ € · intérêts ≈ **7 294 €**

## 3.6 Avantages et risques

| Modalité | Avantage principal | Inconvénient principal |
|----|----|----|
| Annuités constantes | Stabilité budgétaire | Intérêts élevés en début de prêt |
| Amortissement constant | Intérêts totaux plus faibles | Premières échéances plus lourdes |
| In fine | Faibles sorties de trésorerie pendant le prêt | Risque élevé à l’échéance |
| Différé | Soulage la trésorerie initiale | Augmente souvent le coût total |

Choisir une modalité, c’est d’abord **aligner les sorties de cash** sur la capacité de l’entreprise à les financer.

## 3.7 🪤 Le piège

« L’in fine fait payer 9 000 € d’intérêts contre 6 000 € pour l’amortissement constant : c’est toujours le plus mauvais choix. »

Au même taux, les trois modalités ont **le même coût actuariel**. L’in fine paie plus d’intérêts parce que l’entreprise **garde le capital plus longtemps**. Comparez des valeurs **actualisées**, pas des totaux en euros courants.

Plus d’intérêts ≠ plus cher. Peut-être juste plus longtemps emprunté.

## 3.8 🧠 Vérifiez votre compréhension

> **120 000 €** in fine sur **4 ans** à **5 %**. Flux des années 1 à 3 ? Flux de l’année 4 ? Intérêts totaux ?

- Années 1 à 3 : $120\,000 \times 0{,}05 =$ **6 000 €**
- Année 4 : $6\,000 + 120\,000 =$ **126 000 €**
- Intérêts totaux : $4 \times 6\,000 =$ **24 000 €**

Quelle question poser à l’emprunteur avant de signer ? → « D’où viendront les 120 000 € en année 4 ? »

4 Séquence 4\
Coût réel du crédit et taux actuariel
=====================================

Le taux affiché dit-il tout ?

55 min : situation + échéances 10 min, recherche du taux 15 min, définition + Excel 12 min, exemple résolu 10 min, piège + vérification 8 min.

## 4.1 Retour à la question d’ouverture

**50 000 €** sur **4 ans**, échéances annuelles constantes.

- **Banque A** : 4,0 % mais **1 500 € de frais** prélevés au déblocage.
- **Banque B** : 4,5 %, sans frais.

Avec A, l’entreprise ne reçoit que **48 500 €**, mais rembourse comme si elle en avait reçu 50 000.

Laquelle est réellement la moins chère ?

Le taux nominal ignore : frais de dossier · commissions de garantie · assurance emprunteur · points · pénalités de remboursement anticipé.

## 4.2 Étape 1 — Les échéances

Calculées sur les **50 000 €** empruntés (formule de la Séquence 2) :

13 774,50 €

Offre A (4,0 %) · 4 ans

13 937,18 €

Offre B (4,5 %) · 4 ans

**Offre B** : on reçoit 50 000 € et les 4 échéances actualisées à 4,5 % valent exactement 50 000 € → coût réel **4,5 %**.

**Offre A** : la ligne du temps change à $t = 0$ !

\+ 48 500\
reçu net

t = 0

 

− 13 774,50

t = 1

…

− 13 774,50

t = 4

## 4.3 Étape 2 — Tester l’offre A à 4,5 %

|     Année | Échéance A | Facteur $1/1{,}045^t$ | Valeur actuelle |
|----------:|-----------:|----------------------:|----------------:|
|         1 |  13 774,50 |                0,9569 |       13 181,34 |
|         2 |  13 774,50 |                0,9157 |       12 613,72 |
|         3 |  13 774,50 |                0,8763 |       12 070,55 |
|         4 |  13 774,50 |                0,8386 |       11 550,77 |
| **Total** |            |                       |   **49 416,38** |

À 4,5 %, ce que l’entreprise rend vaut **49 416 €** \> **48 500 €** reçus.

L’offre A coûte donc **plus de 4,5 %**.

## 4.4 Étape 3 — Chercher le taux d’équilibre

| Taux d’actualisation | VA des échéances de A | Comparée à 48 500 € |
|---------------------:|----------------------:|---------------------|
|                4,5 % |             49 416,38 | trop haute          |
|                5,0 % |             48 843,70 | trop haute          |
|                5,3 % |             48 505,24 | ≈ égale             |
|                5,5 % |             48 281,70 | trop basse          |

A ≈ 5,30 %

B = 4,50 %

Malgré son taux affiché plus bas, **A est la plus chère**. Revenez sur votre vote !

## 4.5 Le taux actuariel (TAEG)

$$\text{Montant net reçu} = \sum_{t=1}^{n} \frac{Flux_t}{(1+r)^t}$$

Le taux $r$ qui égalise ce que je **reçois vraiment** aujourd’hui et la valeur actuelle de **tout ce que je rendrai** (échéances, frais, assurance).

- Sans frais : $r$ = taux affiché.
- Frais ↑ → montant net reçu ↓, échéances inchangées → $r$ ↑.
- Durée courte → des frais fixes pèsent **plus lourd** dans $r$.

## 4.6 Calcul pratique — Excel

| Besoin | Fonction Excel | Argument clé |
|----|----|----|
| Valeur actuelle | `VA(taux;npm;vpm)` | Convention de signe |
| Valeur future | `VC(taux;npm;vpm)` | Idem |
| Annuité | `VPM(taux;npm;va)` | `va` = montant emprunté |
| Taux actuariel | `TAUX(npm;vpm;va)` | `va` = montant **net** reçu |
| VAN générale | `VAN(taux;flux1:fluxn)` + flux initial | Exclure le flux à $t=0$ |
| TRI | `TRI(flux0:fluxn)` | Inclure le flux à $t=0$ |

**Signes** : entrées (montant reçu) **positives**, sorties (remboursements) **négatives**. Une seule convention dans tout le modèle.

Offre A : `=TAUX(4;-13774,50;48500)` → **5,30 %**

## 4.7 Exemple résolu — Taux actuariel avec frais

> **100 000 €**, taux facial **4 %**, **5 ans**, frais de dossier **2 000 €** à l’origine.

- Montant net reçu : $100\,000 - 2\,000 = 98\,000$ €
- Annuité inchangée (calculée sur 100 000 €) : $A \approx 22\,463$ €

$$98\,000 = 22\,463 \cdot \frac{1-(1+r)^{-5}}{r}$$

`=TAUX(5;-22463;98000)` →

r ≈ 4,72 %

contre 4 % affichés : les frais réduisent le montant disponible, pas les remboursements

## 4.8 🪤 Le piège

« L’offre à 4,0 % est moins chère que l’offre à 4,5 %, puisque son taux est plus bas. »

Avec 1 500 € de frais, l’entreprise reçoit 48 500 € mais rembourse comme si elle en avait reçu 50 000 : coût réel ≈ **5,3 %**. Seul le **taux actuariel** permet de comparer des offres aux frais différents.

Coût réel = ce que je reçois vraiment face à ce que je rends vraiment.

## 4.9 🧠 Vérifiez votre compréhension

> Deux offres identiques (même taux, mêmes frais de 1 000 €), l’une sur **3 ans**, l’autre sur **15 ans**. Laquelle a le TAEG le plus élevé ?

Celle sur **3 ans** : les frais fixes sont amortis sur moins d’années, ils pèsent davantage dans le taux.

> Un prêt sans aucun frais affiche 3,9 %. Son taux actuariel ?

**3,9 %** : sans frais, le montant net reçu égale le montant emprunté.

# 5 Pause déjeuner 🍽️

Reprise : Séquence 5 — Introduction aux obligations.

6 Séquence 5\
Introduction aux obligations
============================

Combien vaut une dette… quand les taux changent ?

50 min : situation + vocabulaire 10 min, exploration 10 min, formule + exemple 12 min, relation prix/taux + zéro-coupon 5 min, démo 8 min, piège + vérification 5 min.

## 6.1 L’obligation de Sarah

Sarah a acheté **1 000 €** une obligation qui verse **50 €/an** (5 %) et rembourse 1 000 € dans **3 ans**.

Aujourd’hui, les obligations de même risque rapportent **6 %** (60 €/an pour 1 000 €). Sarah veut revendre.

Combien un investisseur acceptera-t-il de payer ?

Votre pronostic   ① 1 060 €   ② 1 000 €   ③ ≈ 973 €   ④ ≈ 833 €

## 6.2 Vocabulaire obligataire

| Terme | Définition |
|----|----|
| Valeur nominale $N$ | Capital de référence sur lequel sont calculés les coupons |
| Coupon $C$ | Intérêt versé chaque période : $C = N \times$ taux facial |
| Taux facial | Taux d’intérêt nominal de l’obligation (fixe) |
| Maturité $n$ | Durée restant jusqu’au remboursement |
| Prix d’émission / de remboursement | Prix payé à l’émission / montant rendu à l’échéance (souvent $N$) |
| Rendement actuariel $r$ | Taux qui égalise le prix et la valeur actuelle des flux |
| Prime / Décote | Prix $> N$ : prime (surcote) · Prix $< N$ : décote |

## 6.3 Ce que vaut le titre à 6 %

− P₀\
prix ?

t = 0

÷ 1,06ᵗ

\+ 50

t = 1

 

\+ 50

t = 2

 

\+ 1 050

t = 3

|     Année |  Flux | $1/1{,}06^t$ |         VA |
|----------:|------:|-------------:|-----------:|
|         1 |    50 |       0,9434 |      47,17 |
|         2 |    50 |       0,8900 |      44,50 |
|         3 | 1 050 |       0,8396 |     881,60 |
| **Total** |       |              | **973,27** |

≈ 973 €

décote de ≈ 27 € (réponse ③)

Contrôle : à 5 %, la même somme donne **1 000 €**, le prix d’origine.

## 6.4 Le prix d’une obligation à taux fixe

$$P_0 = \underbrace{C \cdot \frac{1-(1+r)^{-n}}{r}}_{\text{rente de coupons}} + \underbrace{\frac{N}{(1+r)^n}}_{\text{nominal}}$$

$C$ coupon · $N$ nominal · $n$ maturité · $r$ **taux de marché** (rendement exigé)

Les flux sont **figés** ; c’est le **prix** qui s’ajuste pour que le rendement colle au marché.

**Zéro-coupon** : aucun coupon, seul $N$ est versé à maturité → $P_0 = \dfrac{N}{(1+r)^n}$

## 6.5 Exemple résolu — Obligation avec prime

> Nominal **1 000 €**, coupon **4 %** (40 €/an), maturité **4 ans**, taux de marché **3 %**.

$$P_0 = 40 \times \frac{1-1{,}03^{-4}}{0{,}03} + \frac{1\,000}{1{,}03^4}$$

$$\approx 148{,}68 + 888{,}49 = 1\,037{,}17\ €$$

Taux de marché (3 %) \< taux facial (4 %) → l’obligation cote **au-dessus du pair** : prime d’environ **37 €**.

## 6.6 Taux en haut, prix en bas

| Situation                       | Effet sur le prix       |
|---------------------------------|-------------------------|
| Taux de marché $r$ **augmente** | Prix $P_0$ **diminue**  |
| Taux de marché $r$ **diminue**  | Prix $P_0$ **augmente** |
| $r$ = taux facial               | $P_0 = N$ (au pair)     |
| $r$ \< taux facial              | $P_0 > N$ (prime)       |
| $r$ \> taux facial              | $P_0 < N$ (décote)      |

La relation est **convexe** : −1 point de taux fait monter le prix *plus* que +1 point ne le fait baisser.

## 6.7 Prix et taux de marché 🎛️

``` js
viewof obl_coupon = Inputs.range([0, 100], {value: 50, step: 5, label: "Coupon annuel C (€) — nominal 1 000 €"})
viewof obl_n = Inputs.range([1, 20], {value: 3, step: 1, label: "Maturité n (années)"})
viewof obl_r = Inputs.range([0.01, 0.12], {value: 0.06, step: 0.0025, label: "Taux de marché r"})
```

``` js
obl_price = (r) => pvFlows(Array.from({length: obl_n}, (_, k) => obl_coupon + (k + 1 === obl_n ? 1000 : 0)), r)
obl_curve = Array.from({length: 111}, (_, k) => ({r: 0.01 + k * 0.001, prix: obl_price(0.01 + k * 0.001)}))
obl_P0 = obl_price(obl_r)

Plot.plot({
  width: 900, height: 280, marginLeft: 70,
  x: {label: "Taux de marché r →", tickFormat: d => pct(d, 0)},
  y: {label: "↑ Prix P₀ (€)", grid: true, tickFormat: d => fmt(d)},
  marks: [
    Plot.ruleY([1000], {stroke: "#8b8f9c", strokeDasharray: "4"}),
    Plot.ruleX([obl_coupon / 1000].filter(x => x >= 0.01), {stroke: "#f0a500", strokeDasharray: "4"}),
    Plot.lineY(obl_curve, {x: "r", y: "prix", stroke: "#5b9bdb", strokeWidth: 3}),
    Plot.dot([{r: obl_r, prix: obl_P0}], {x: "r", y: "prix", fill: "#db5b5b", r: 7})
  ]
})
```

``` js
obl_status = Math.abs(obl_P0 - 1000) < 0.5 ? "au pair" : obl_P0 > 1000 ? `prime de ${fmt(obl_P0 - 1000)} €` : `décote de ${fmt(1000 - obl_P0)} €`
md`<div class="ojs-result">Prix **${fmt(obl_P0, 2)} €** au taux ${pct(obl_r)} — *${obl_status}* · taux facial <span class="orange">${pct(obl_coupon / 1000)}</span></div>`
```

Réglages par défaut = obligation de Sarah (973,27 €). Faire tester : r = taux facial (au pair), puis allonger la maturité (3 → 20 ans) : la courbe devient plus pentue, le titre plus sensible aux taux. Transition vers S6.

## 6.8 🪤 Le piège

« Les taux montent, donc mon obligation rapporte plus et vaut plus cher. »

Le coupon d’une obligation à taux fixe **ne change pas**. Quand les nouvelles obligations rapportent davantage, l’ancienne n’est attractive que si son **prix baisse**.

Taux en haut, prix en bas : c’est une balançoire.

## 6.9 🧠 Vérifiez votre compréhension

> Coupon **5 %**, nominal 1 000 €, 7 ans, taux de marché **5 %**. Prix ?

**1 000 €** : taux de marché = taux facial → au pair, sans calcul.

> Zéro-coupon de nominal **1 000 €**, maturité **10 ans**, taux de marché **4 %**. Prix ?

$P_0 = 1\,000 / 1{,}04^{10} \approx$ **675,56 €**

7 Séquence 6\
Sensibilité obligataire
=======================

« 5 ans » veut-il dire la même chose pour deux obligations à 5 ans ?

45 min : situation + table K 12 min, démo duration 5 min, duration modifiée et convexité 15 min, exemple résolu 8 min, piège + vérification 5 min.

## 7.1 Deux obligations à 5 ans

Nominal **1 000 €**, **5 ans**, taux de marché **5 %** :

- **Z** ne verse rien pendant 5 ans, puis rembourse tout ;
- **K** verse **80 €/an** (8 %) puis rend les 1 000 € à la fin.

Avec K, une partie de l’argent revient bien avant l’année 5.

En moyenne, quand récupère-t-on son argent ? Laquelle craint le plus une hausse des taux ?

Votre pronostic   ① Z   ② K   ③ autant l’une que l’autre

## 7.2 La date moyenne de récupération

| Année $t$ |  Flux |     VA à 5 % | Poids dans le prix | $t$ × poids |
|----------:|------:|-------------:|-------------------:|------------:|
|         1 |    80 |        76,19 |             6,74 % |       0,067 |
|         2 |    80 |        72,56 |             6,42 % |       0,128 |
|         3 |    80 |        69,11 |             6,12 % |       0,184 |
|         4 |    80 |        65,82 |             5,83 % |       0,233 |
|         5 | 1 080 |       846,21 |            74,89 % |       3,745 |
| **Total** |       | **1 129,88** |          **100 %** |    **4,36** |

K : 4,36 ans

Z : 5 ans

un seul flux, prix $1\,000/1{,}05^5 = 783{,}53$ €

Pour +1 point de taux : Z perd **4,63 %**, K perd **4,04 %** → Z est la plus exposée (réponse ①).

## 7.3 Le centre de gravité des flux 🎛️

``` js
viewof dur_coupon = Inputs.range([0, 150], {value: 80, step: 10, label: "Coupon annuel (€) — nominal 1 000 €, 5 ans, r = 5 %"})
```

``` js
dur_flows = Array.from({length: 5}, (_, k) => {
  const t = k + 1
  const cf = dur_coupon + (t === 5 ? 1000 : 0)
  return {t, cf, va: cf / 1.05 ** t}
})
dur_P = d3.sum(dur_flows, d => d.va)
dur_D = d3.sum(dur_flows, d => d.t * d.va) / dur_P

Plot.plot({
  width: 900, height: 280, marginLeft: 70,
  x: {label: "Date t (années) →", domain: [0, 5.6], ticks: [1, 2, 3, 4, 5]},
  y: {label: "↑ Valeur actuelle du flux (€)", grid: true, tickFormat: d => fmt(d)},
  marks: [
    Plot.rect(dur_flows, {x1: d => d.t - 0.3, x2: d => d.t + 0.3, y1: 0, y2: "va", fill: "#5bdb6d"}),
    Plot.ruleX([dur_D], {stroke: "#f0a500", strokeWidth: 3}),
    Plot.text([dur_D], {x: d => d, frameAnchor: "top", dy: 6, text: d => `D = ${fmt(d, 2)} ans`, fill: "#f0a500", fontSize: 16, textAnchor: "end", dx: -6})
  ]
})
```

``` js
md`<div class="ojs-result">Prix **${fmt(dur_P, 2)} €** · duration de Macaulay <span class="orange">**${fmt(dur_D, 2)} ans**</span> · duration modifiée **${fmt(dur_D / 1.05, 2)}**</div>`
```

Coupon 80 € = obligation K (4,36 ans). Coupon 0 = Z (5 ans exactement). Faire verbaliser : plus le coupon est élevé, plus le centre de gravité se rapproche du présent.

## 7.4 Duration de Macaulay

$$D_M = \frac{\displaystyle\sum_{t=1}^{n} t \cdot \frac{CF_t}{(1+r)^t}}{P_0}$$

Moyenne des dates $t$, pondérée par la part de chaque flux actualisé dans le prix $P_0$.

- Exprimée en **années**.
- Zéro-coupon : $D_M = n$. Avec coupons : $D_M < n$.
- Coupons ↑ → argent récupéré plus tôt → $D_M$ ↓.

## 7.5 Quand le choc de taux grossit

Le trésorier détient K à 5 %. Le comité de risque demande la perte pour **+1 point**, puis **+3 points**. Un collègue : *« ≈ 4 % pour 1 point, donc 12 % pour 3 points. »*

La perte est-elle proportionnelle au choc ?

|   Choc | Nouveau taux | Prix exact | Variation exacte | Règle de trois (4,15 %/pt) |
|-------:|-------------:|-----------:|-----------------:|---------------------------:|
|      0 |          5 % |   1 129,88 |                — |                          — |
|  +1 pt |          6 % |   1 084,25 |          −4,04 % |                    −4,15 % |
| +3 pts |          8 % |   1 000,00 |         −11,50 % |                   −12,45 % |

**Non** : la règle linéaire est fiable pour un petit choc, **trop pessimiste** pour un grand.

## 7.6 Duration modifiée

$$D^* = \frac{D_M}{1 + r} \qquad\qquad \frac{\Delta P}{P} \approx -D^* \cdot \Delta r$$

$\Delta r$ en décimal : 1 point = 0,01

Pour K : $D^* = 4{,}36 / 1{,}05 \approx 4{,}15$ → +1 point ≈ **−4,15 %**.

**Pourquoi ?** $P(r) = \sum CF_t(1+r)^{-t}$, donc

$$\frac{dP}{dr} = -\frac{1}{1+r}\sum_{t=1}^{n} t \cdot \frac{CF_t}{(1+r)^t} = -\frac{D_M}{1+r}\,P = -D^* \cdot P$$

$D^*$ est la **pente relative** de la courbe prix-taux : une tangente.

## 7.7 Tangente et convexité 🎛️

``` js
viewof cvx_choc = Inputs.range([-3, 4], {value: 3, step: 0.25, label: "Choc de taux Δr (points), obligation K à partir de 5 %"})
```

``` js
cvx_flows = [80, 80, 80, 80, 1080]
cvx_P0 = pvFlows(cvx_flows, 0.05)
cvx_Ds = cvx_flows.reduce((s, f, k) => s + (k + 1) * f / 1.05 ** (k + 1), 0) / cvx_P0 / 1.05
cvx_curve = Array.from({length: 91}, (_, k) => {
  const r = 0.01 + k * 0.001
  return [
    {r, prix: pvFlows(cvx_flows, r), courbe: "Prix exact"},
    {r, prix: cvx_P0 * (1 - cvx_Ds * (r - 0.05)), courbe: "Approximation par la duration"}
  ]
}).flat()
cvx_r1 = 0.05 + cvx_choc / 100
cvx_exact = pvFlows(cvx_flows, cvx_r1)
cvx_approx = cvx_P0 * (1 - cvx_Ds * (cvx_r1 - 0.05))

Plot.plot({
  width: 900, height: 280, marginLeft: 70,
  color: {domain: ["Prix exact", "Approximation par la duration"], range: ["#5b9bdb", "#f0a500"], legend: true},
  x: {label: "Taux de marché r →", tickFormat: d => pct(d, 0)},
  y: {label: "↑ Prix (€)", grid: true, tickFormat: d => fmt(d)},
  marks: [
    Plot.lineY(cvx_curve, {x: "r", y: "prix", stroke: "courbe", strokeWidth: 3}),
    Plot.ruleX([cvx_r1], {stroke: "#8b8f9c", strokeDasharray: "4"}),
    Plot.dot([{r: cvx_r1, prix: cvx_exact}, {r: cvx_r1, prix: cvx_approx}], {x: "r", y: "prix", fill: "#db5b5b", r: 6})
  ]
})
```

``` js
md`<div class="ojs-result">Choc ${cvx_choc > 0 ? "+" : ""}${fmt(cvx_choc, 2)} pt : exact **${pct(cvx_exact / cvx_P0 - 1)}** · duration <span class="orange">**${pct(cvx_approx / cvx_P0 - 1)}**</span> · écart (convexité) <span class="green">**${fmt(cvx_exact - cvx_approx, 2)} €**</span></div>`
```

La courbe exacte est toujours au-dessus de la tangente : l’écart, toujours favorable au porteur, c’est la convexité. Tester un choc négatif : le prix monte plus que la duration ne le prévoit.

## 7.8 Exemple résolu — Obligation au pair

> Nominal **1 000 €**, coupon **6 %** (60 €), **3 ans**, taux de marché **6 %** (prix 1 000 €).

|       $t$ | $CF_t$ | $CF_t/1{,}06^t$ | $t \cdot CF_t/1{,}06^t$ |
|----------:|-------:|----------------:|------------------------:|
|         1 |     60 |           56,60 |                   56,60 |
|         2 |     60 |           53,40 |                  106,80 |
|         3 |  1 060 |          890,00 |                2 669,99 |
| **Total** |        |    **1 000,00** |            **2 833,39** |

$D_M = 2\,833{,}39 / 1\,000 \approx$ **2,83 ans**

$D^* = 2{,}83 / 1{,}06 \approx$ **2,67**

Hausse de **0,5 point** :

$\Delta P/P \approx -2{,}67 \times 0{,}005 \approx$ **−1,34 %**

Recalcul exact à 6,5 % : **986,76 €**, soit **−1,32 %**.

Petit choc → approximation très bonne.

## 7.9 🪤 Le piège

« Une obligation à 5 ans a une duration de 5 ans, et la duration donne la perte pour n’importe quel choc de taux. »

La duration est **inférieure à la maturité** dès qu’il y a des coupons. Et c’est une **tangente** : valable pour de petits chocs. Pour plusieurs points, recalculez le prix exactement ou ajoutez la convexité.

Duration = centre de gravité des flux. Grand choc → pensez convexité.

## 7.10 🧠 Vérifiez votre compréhension

> Un portefeuille a une duration modifiée de **6**. Les taux montent de **0,5 point**.

$\Delta P / P \approx -6 \times 0{,}005 =$ **−3 %**

> Le trésorier anticipe une **hausse des taux**. Allonge-t-il ou raccourcit-il la duration de son portefeuille ?

Il la **raccourcit** : maturités plus courtes, coupons plus élevés.

8 Séquence 7\
Étude de cas : choisir un financement
=====================================

De la formule à la recommandation.

60 min : contexte 5 min, travail en binômes 35 min (étape 1 : 15 min, étape 2 : 10 min, étape 3 : 10 min), correction 15 min, cadre de décision 5 min.

## 8.1 Le contexte

Une PME finance un équipement industriel de **600 000 €**. Trois offres sur **7 ans** :

- **Banque A** : annuités constantes, **3,8 %** ;
- **Banque B** : amortissement constant, **3,5 %** ;
- **Banque C** : in fine, **3,2 %**, mais **6 000 €** de frais initiaux.

Quelle offre recommander ?

Votre intuition   ① A   ② B   ③ C

## 8.2 Travail demandé

Pour chaque financement :

1.  Échéance de la **première** et de la **dernière** année.
2.  **Coût total des intérêts** sur la durée.
3.  Banque C : **taux actuariel** intégrant les frais.
4.  **Pression sur la trésorerie** en année 1 et en année 7.
5.  **Risques** propres à chaque modalité.
6.  **Recommandation** argumentée (une page).

| Étape | Questions | Outil | Durée |
|----|----|----|---:|
| 1 | 1 et 2 | Annuité (S2), $C_0/n$ + intérêts sur CRD (S3), $C_0 \times i$ (S3) | 15 min |
| 2 | 3 | Taux actuariel sur 594 000 € nets (S4) | 10 min |
| 3 | 4 à 6 | Comparer année 1 / année 7, risques, profil de trésorerie | 10 min |

✏️ Une ligne du temps par banque avant tout calcul.

## 8.3 Correction — Étapes 1 et 2

|                  | Banque A |  Banque B |                  Banque C |
|------------------|---------:|----------:|--------------------------:|
| Échéance année 1 | 99 228 € | 106 714 € |                  19 200 € |
| Échéance année 7 | 99 228 € |  88 714 € |                 619 200 € |
| Intérêts totaux  | 94 597 € |  84 000 € | 134 400 € + 6 000 € frais |
| Taux actuariel   |    3,8 % |     3,5 % |                **3,36 %** |

**A** : $A = 600\,000 \times \dfrac{0{,}038}{1 - 1{,}038^{-7}} = 600\,000 \times \dfrac{0{,}038}{0{,}229773} \approx 99\,228$ €

**B** : $Am = 600\,000/7 \approx 85\,714$ € · $A_1 = 85\,714 + 21\,000$ · $A_7 = 85\,714 \times 1{,}035$ · $\sum I_t = 0{,}035 \times 600\,000 \times \frac{7+1}{2}$

**C** : $594\,000 = 19\,200 \cdot \dfrac{1-(1+r)^{-7}}{r} + \dfrac{600\,000}{(1+r)^7}$ → $r \approx 3{,}36\,\%$

## 8.4 Correction — Étape 3

- **Coût actuariel** : C (3,36 %) \< B (3,5 %) \< A (3,8 %). Les 134 400 € d’intérêts de C ne la rendent **pas** plus chère (piège de la Séquence 3).
- **B domine A** : taux plus bas, 10 600 € d’intérêts en moins… mais **+ 7 500 €** à décaisser en année 1.
- **C** : charge annuelle la plus légère, mais **600 000 €** à trouver en année 7 → risque de refinancement.

**Recommandation type** : B si les flux d’exploitation couvrent ~106 700 € dès l’année 1 ; A si la trésorerie initiale est la contrainte ; C seulement avec une source de remboursement identifiée à 7 ans (cession, épargne dédiée).

## 8.5 Cadre de décision

- **Si** les frais diffèrent → comparez par le **taux actuariel**, jamais par le taux affiché.
- **Si** la PME dégage des flux suffisants dès l’année 1 → l’**amortissement constant** minimise les intérêts payés.
- **Si** la trésorerie des premières années est la contrainte → **annuités constantes** : charge plus faible au départ et stable.
- **Si** le capital est remboursé en une fois (in fine) → exigez une **source de remboursement identifiée** à l’échéance.
- **Si** les coûts réels sont proches → tranchez sur le **profil de trésorerie** et le **risque de refinancement**.

# 9 Exercices & synthèse

Ce qu’il faut retenir, et le mettre en pratique.

25 min : carte mentale 3 min, niveau 1 en autonomie 8 min, niveau 2 en binômes 12 min, réflexes 2 min. Niveau 3 : travail personnel, correction dans le cours en ligne.

## 9.1 Carte mentale du cours

#### Σ Annuités constantes

$A = C_0 \dfrac{i}{1-(1+i)^{-n}}$

$I_t = CRD_{t-1} \times i$ · $Am_t = A - I_t$

#### ⇅ Modalités

Amort. constant : $Am = C_0/n$

In fine : $I_t = C_0\,i$, puis $C_0(1+i)$

#### % Taux actuariel

Net reçu $= \sum \dfrac{Flux_t}{(1+r)^t}$

Frais ↑ → $r$ ↑ · Excel `TAUX`

#### ⚖ Obligations

$P_0 = C\,\dfrac{1-(1+r)^{-n}}{r} + \dfrac{N}{(1+r)^n}$

$\dfrac{\Delta P}{P} \approx -\dfrac{D_M}{1+r}\,\Delta r$

## 9.2 Niveau 1 — Application directe

**1.1** — Annuité d’un emprunt de **50 000 €** sur **4 ans** à **5 %** ?

$A = 50\,000 \times \dfrac{0{,}05}{1 - 1{,}05^{-4}} = 50\,000 \times \dfrac{0{,}05}{0{,}17730} \approx$ **14 101 €**

**1.2** — Obligation de nominal **1 000 €**, coupon **40 €**, **3 ans**, taux de marché **6 %**. Prix ? Prime ou décote ?

$P_0 = 40 \times 2{,}6730 + 1\,000 / 1{,}06^3 = 106{,}92 + 839{,}62 =$ **946,54 €**

946,54 \< 1 000 → **décote** (taux de marché 6 % \> taux facial 4 %).

## 9.3 Niveau 2 — Prêt immobilier

**200 000 €** sur **20 ans**, mensualités constantes, taux **2,4 % annuel** (converti en taux mensuel équivalent). Frais de garantie : **1 500 €** à l’origine.

1.  Taux mensuel équivalent ?
2.  Mensualité ?
3.  Taux actuariel mensuel, puis annuel ?

1.  $i_m = 1{,}024^{1/12} - 1 \approx$ **0,1980 %**

2.  $A = 200\,000 \times \dfrac{0{,}001980}{1 - 1{,}001980^{-240}} \approx 200\,000 \times 0{,}005238 \approx$ **1 047,57 €/mois**

3.  $198\,500 = 1\,047{,}57 \times \dfrac{1-(1+r_m)^{-240}}{r_m}$ → $r_m \approx 0{,}2046\,\%$ → $r_a = 1{,}002046^{12} - 1 \approx$ **2,48 %**

Excel : =VPM(1,024^(1/12)-1;240;-200000) → 1 047,57 ; =TAUX(240;-1047,57;198500) → 0,2046 %.

## 9.4 Niveau 3 — Analyse obligataire

Obligation de nominal **5 000 €**, taux facial **3 %**, **8 ans**, achetée au pair. Les taux montent brusquement de **+150 points de base** (à 4,5 %).

1.  Nouveau prix de l’obligation ?
2.  Duration de Macaulay ? *(au pair :* $D_M = \frac{1+i}{i}\left(1-(1+i)^{-n}\right)$)
3.  Variation estimée par la duration modifiée, comparée à la variation réelle ?
4.  Que concluez-vous sur la convexité ?

Travail personnel — correction détaillée dans le cours en ligne.

Résultats pour l’enseignant : P = 4 505,31 € (−9,89 %) ; D_M ≈ 7,23 ans ; D\* ≈ 7,02 → −10,53 % (≈ −526 €) contre −495 € réels ; écart ≈ 32 € dû à la convexité, en faveur du porteur.

## 9.5 Cinq réflexes à acquérir

1.  ✏️ **Tracer la ligne du temps** avec le **sens** de chaque flux.
2.  🧾 **Décomposer chaque échéance** : intérêts sur le CRD + amortissement.
3.  💶 **Partir du montant net reçu** pour mesurer le coût réel.
4.  ⚖️ **Comparer des valeurs actualisées**, pas des totaux d’intérêts en euros.
5.  📉 **Taux ↑ → prix ↓**, d’autant plus que la duration est longue.

## 9.6 📖 Pour aller plus loin

Théorie complète, démonstrations, exemples et corrections détaillées :

[→ Module 2 : Emprunts et obligations](../module-02.qmd)

[→ Formulaire](../../../teaching/mathematical-finance/formulaire.llms.md) · [→ Glossaire](../../../teaching/mathematical-finance/glossaire.llms.md)

Une dette n’est qu’une suite de **flux datés** ramenés à **une même date**.

## Citation

BibTeX citation:

``` quarto-appendix-bibtex
@online{gilles,
  author = {Gilles, Guillaume},
  title = {Emprunts Et Obligations},
  url = {https://ggilles.dev/teaching/mathematical-finance/slides/module-02.html},
  langid = {en}
}
```

For attribution, please cite this work as:

Gilles, Guillaume. n.d. “Emprunts Et Obligations.” <https://ggilles.dev/teaching/mathematical-finance/slides/module-02.html>.
