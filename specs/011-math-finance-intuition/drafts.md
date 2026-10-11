# Working Drafts: 011-math-finance-intuition

Working file for T006 (and later T038, T048, T059). Not rendered by Quarto
(lives under `specs/`).

The 13 concrete-case narratives are written directly into the module files
(T007-T019, `## Situation concrète` callouts). This file holds the **verified
numbers** each scenario carries through the ladder (US2) and the
**13 Erreur fréquente callouts**, ready to paste.

Numbers verified with Python on 2026-10-11 (rounded to the euro unless noted).

---

## Scenario numbers (to reuse in US2 numerical exploration)

| Section | Scenario | Key numbers | Answer revealed in US2 |
|---------|----------|-------------|------------------------|
| M1 S2 | Léa, 10 000 €, 10 ans, 3 % | Simple : 10 000 × (1 + 10 × 0,03) = 13 000 € ; composé : 10 000 × 1,03^10 = 13 439 € | « Cumul », +439 € (intérêts sur intérêts) |
| M1 S3 | 1 000 € auj. vs 1 100 € dans 1 an, 5 % | 1 000 × 1,05 = 1 050 € < 1 100 € ; 1 100 / 1,05 = 1 048 € > 1 000 € | Accepter 1 100 € dans un an |
| M1 S4 | 10 000 €, A 9 %/an vs B 0,75 %/mois | A : 10 900 € ; B : 10 000 × 1,0075^12 = 10 938 € (taux annuel équivalent 9,38 %) | B coûte 38 € de plus |
| M1 S5 | Thomas, 5 × 5 000 € à 3 %, objectif 30 000 € | Valeur acquise = 5 000 × (1,03^5 − 1)/0,03 = 26 546 € ; versement nécessaire = 5 651 €/an | Non, il manque 3 454 € |
| M2 S2 | PME, 60 000 €, 3 ans, 5 % | A = 22 033 € ; intérêts totaux = 6 098 € ; tableau : (I 3 000 / Am 19 033 / CRD 40 967), (2 048 / 19 984 / 20 983), (1 049 / 20 983 / 0) | Annuité 22 033 €, 6 098 € d'intérêts |
| M2 S3 | Même prêt, 3 modalités | Échéance année 1 : constante 22 033 € ; amort. constant 20 000 + 3 000 = 23 000 € ; in fine 3 000 € (puis 63 000 € en année 3) ; intérêts totaux : 6 098 € / 6 000 € / 9 000 € | In fine soulage l'année 1, mais concentre le risque à la fin |
| M2 S4 | 50 000 €, 4 ans ; A 4,0 % + 1 500 € frais vs B 4,5 % | A : annuité 13 775 €, montant net reçu 48 500 €, taux actuariel ≈ 5,30 % ; B : annuité 13 937 €, taux actuariel 4,50 % | B est moins chère |
| M2 S5 | Obligation 1 000 €, coupon 50 €, 3 ans, marché 6 % | Prix = 50/1,06 + 50/1,06² + 1 050/1,06³ = 973 € | ≈ 973 € (décote de 27 €) |
| M2 S6a | Z (zéro-coupon) vs K (coupon 80 €), 5 ans, r = 5 % | Z : prix 784 €, D_M = 5 ans ; K : prix 1 130 €, VA des flux 76 / 73 / 69 / 66 / 846 €, poids 6,7 % / 6,4 % / 6,1 % / 5,8 % / 74,9 %, D_M = 4,36 ans, D* = 4,15 | K récupère en moyenne en 4,36 ans ; Z est plus exposée (+1 pt : Z −4,6 %, K −4,0 %) |
| M2 S6b | K, choc +1 pt et +3 pts | +1 pt : exact −4,04 %, approx. duration −4,15 % ; +3 pts : exact −11,50 %, approx. −12,45 % | Non proportionnelle : la convexité amortit la perte |
| M3 S2 | Machine 50 000 €, 15 000 €/an, 5 ans, k = 8 % | VA des flux = 15 000 × 3,9927 = 59 891 € ; VAN = 9 891 € | Oui, VAN > 0 |
| M3 S3 | Même machine | VAN : 8 % → 9 891 € ; 12 % → 4 072 € ; 16 % → −886 € ; 20 % → −5 141 € ; TRI ≈ 15,24 % | Intéressant tant que le taux exigé < 15,2 % |
| M3 S4 | 40 000 € ; Rapide 20 000/20 000/5 000 vs Durable 12 000 × 6, k = 8 % | DRS : Rapide 2 ans, Durable 3,33 ans ; VA cumulées Rapide 18 519 / 35 665 / 39 634 (jamais récupéré en actualisé) ; Durable 11 111 / 21 399 / 30 925 / 39 746 / 47 913 (DRA ≈ 4,03 ans) ; VAN : Rapide −366 €, Durable +15 475 € | Non : Durable crée de la valeur, Rapide en détruit |
| M3 S5 | Machine, 2 000 pièces/an | Hypothèse de décomposition à expliciter en US2 : marge unitaire 12 €, charges fixes 9 000 €/an → 2 000 × 12 − 9 000 = 15 000 € ; ventes −20 % (1 600 pièces) : flux 10 200 €, VAN = −9 274 € ; volume seuil ≈ 1 794 pièces (−10 %) | Non : le projet ne supporte qu'environ −10 % |

---

## Erreur fréquente callouts (paste into US2 tasks T021-T033)

### M1 S2 — Intérêts simples et composés

```markdown
::: {.callout-warning}
## Erreur fréquente

**L'intuition piège** : « 3 % par an pendant 10 ans, cela fait 30 % de gain,
quel que soit le placement. »

**Pourquoi c'est faux** : ce calcul additionne les taux, ce qui n'est vrai
qu'en intérêts simples ; en intérêts composés, chaque année les 3 % portent
sur un capital déjà augmenté des intérêts passés.

**Le bon raisonnement** : en composé, on multiplie le capital par 1,03 chaque
année, soit 1,03 puissance 10 ≈ 1,344 au bout de 10 ans, donc un gain de
34,4 % et non 30 %.

**Astuce mémo** : en composé, on multiplie, on n'additionne pas.
:::
```

### M1 S3 — Actualisation et équivalence

```markdown
::: {.callout-warning}
## Erreur fréquente

**L'intuition piège** : « 1 100 € dans un an, c'est plus que 1 000 €
aujourd'hui, donc c'est forcément mieux. »

**Pourquoi c'est faux** : on compare deux montants qui ne sont pas exprimés à
la même date ; un euro disponible aujourd'hui peut être placé et vaut donc
plus qu'un euro futur.

**Le bon raisonnement** : ramener les deux montants à une date commune
(actualiser 1 100 € à aujourd'hui ou capitaliser 1 000 € dans un an) avant de
les comparer.

**Astuce mémo** : on ne compare et on n'additionne que des euros de même date.
:::
```

### M1 S4 — Taux proportionnels et équivalents

```markdown
::: {.callout-warning}
## Erreur fréquente

**L'intuition piège** : « 9 % par an, c'est 0,75 % par mois : il suffit de
diviser par 12. »

**Pourquoi c'est faux** : diviser par 12 donne le taux proportionnel, qui
ignore que les intérêts mensuels produisent eux-mêmes des intérêts les mois
suivants ; 0,75 % par mois capitalisé donne en réalité 9,38 % sur l'année.

**Le bon raisonnement** : pour obtenir le même résultat sur un an, le taux
mensuel doit vérifier « (1 + taux mensuel) puissance 12 = 1 + taux annuel »,
ce qui donne le taux équivalent.

**Astuce mémo** : diviser donne le proportionnel, la racine donne
l'équivalent.
:::
```

### M1 S5 — Annuités constantes

```markdown
::: {.callout-warning}
## Erreur fréquente

**L'intuition piège** : « Il y a 5 versements, donc la formule d'annuité
s'applique telle quelle, que l'on verse en début ou en fin d'année. »

**Pourquoi c'est faux** : la formule standard suppose des versements en fin
de période ; si l'on verse en début de période, chaque versement travaille
une année de plus et la valeur acquise est multipliée par (1 + i).

**Le bon raisonnement** : tracer la ligne du temps, repérer la date du premier
et du dernier flux, puis choisir la formule (terme échu ou terme à échoir) et
la date d'évaluation correspondantes.

**Astuce mémo** : dessine la ligne du temps — où tombe le premier flux ?
:::
```

### M2 S2 — Emprunt amortissable

```markdown
::: {.callout-warning}
## Erreur fréquente

**L'intuition piège** : « L'échéance est constante, donc chaque année je
rembourse la même part de capital et je paie les mêmes intérêts. »

**Pourquoi c'est faux** : les intérêts sont calculés sur le capital restant
dû, qui diminue à chaque échéance ; la part d'intérêts baisse donc chaque
année, et la part d'amortissement augmente d'autant.

**Le bon raisonnement** : construire le tableau ligne par ligne — intérêts =
capital restant dû × taux, amortissement = annuité − intérêts, nouveau capital
restant dû = ancien − amortissement.

**Astuce mémo** : l'annuité est fixe, mais sa composition bascule des intérêts
vers le capital.
:::
```

### M2 S3 — Autres modalités de remboursement

```markdown
::: {.callout-warning}
## Erreur fréquente

**L'intuition piège** : « L'emprunt in fine fait payer 9 000 € d'intérêts
contre 6 000 € pour l'amortissement constant : il est donc toujours le plus
mauvais choix. »

**Pourquoi c'est faux** : au même taux, les trois modalités ont exactement le
même coût actuariel ; l'in fine paie plus d'intérêts uniquement parce que
l'entreprise garde le capital plus longtemps à sa disposition.

**Le bon raisonnement** : choisir la modalité selon le profil de trésorerie
et le risque de refinancement, et comparer des coûts actualisés plutôt que
des totaux d'intérêts en euros courants.

**Astuce mémo** : plus d'intérêts payés ne veut pas dire plus cher — cela
peut vouloir dire plus longtemps emprunté.
:::
```

### M2 S4 — Coût réel du crédit

```markdown
::: {.callout-warning}
## Erreur fréquente

**L'intuition piège** : « L'offre à 4,0 % est moins chère que l'offre à
4,5 %, puisque son taux est plus bas. »

**Pourquoi c'est faux** : le taux nominal ignore les frais ; avec 1 500 € de
frais, l'entreprise ne reçoit que 48 500 € mais rembourse comme si elle en
avait reçu 50 000, ce qui porte le coût réel à environ 5,3 %.

**Le bon raisonnement** : calculer le taux actuariel, c'est-à-dire le taux qui
égalise le montant net réellement reçu et la valeur actuelle de tout ce qui
sera versé, frais compris.

**Astuce mémo** : coût réel = ce que je reçois vraiment face à ce que je rends
vraiment.
:::
```

### M2 S5 — Introduction aux obligations

```markdown
::: {.callout-warning}
## Erreur fréquente

**L'intuition piège** : « Les taux montent, donc mon obligation rapporte
plus et vaut plus cher. »

**Pourquoi c'est faux** : le coupon d'une obligation à taux fixe ne change
pas ; quand les nouvelles obligations rapportent davantage, l'ancienne n'est
attractive que si son prix baisse.

**Le bon raisonnement** : le prix est la valeur actuelle des coupons et du
nominal au taux de marché ; un taux d'actualisation plus élevé réduit cette
valeur actuelle, donc le prix.

**Astuce mémo** : taux en haut, prix en bas — c'est une balançoire.
:::
```

### M2 S6 — Sensibilité obligataire

```markdown
::: {.callout-warning}
## Erreur fréquente

**L'intuition piège** : « Une obligation à 5 ans a une duration de 5 ans, et
la duration permet de calculer la perte pour n'importe quel choc de taux. »

**Pourquoi c'est faux** : la duration est la date moyenne de récupération des
flux pondérée par leurs valeurs actuelles — elle est inférieure à la maturité
dès qu'il y a des coupons ; et l'approximation par la duration est une
tangente, valable seulement pour de petites variations de taux.

**Le bon raisonnement** : calculer la duration à partir des flux actualisés ;
pour un choc important (plusieurs points), recalculer le prix exactement ou
ajouter la correction de convexité.

**Astuce mémo** : duration = centre de gravité des flux ; pour les grands
chocs, pense convexité.
:::
```

### M3 S2 — VAN

```markdown
::: {.callout-warning}
## Erreur fréquente

**L'intuition piège** : « La machine rapporte 5 × 15 000 = 75 000 € pour
50 000 € investis : elle est rentable, inutile de calculer davantage. »

**Pourquoi c'est faux** : on additionne des euros reçus à des dates
différentes comme s'ils valaient tous autant que les 50 000 € dépensés
aujourd'hui, ce qui ignore le rendement exigé par les associés.

**Le bon raisonnement** : actualiser chaque flux au coût du capital, puis
comparer la somme obtenue à l'investissement ; c'est le signe de la VAN qui
tranche.

**Astuce mémo** : un euro de demain n'est pas un euro d'aujourd'hui —
actualise d'abord.
:::
```

### M3 S3 — TRI (from research.md R5)

```markdown
::: {.callout-warning}
## Erreur fréquente

**L'intuition piège** : « Le TRI est le rendement du projet, donc si le TRI
dépasse le taux exigé, le projet est bon — pas besoin de regarder la VAN. »

**Pourquoi c'est faux** : le TRI suppose que les flux sont réinvestis au TRI
lui-même, ce qui est rarement réaliste, et il peut classer à tort deux projets
de tailles différentes ; la VAN actualise au coût du capital, qui reflète le
vrai coût d'opportunité.

**Le bon raisonnement** : décider sur la VAN ; le TRI est un indicateur
complémentaire, pas un substitut, et en cas de conflit entre projets
mutuellement exclusifs, la VAN tranche.

**Astuce mémo** : VAN pour décider, TRI pour communiquer.
:::
```

### M3 S4 — Délai de récupération

```markdown
::: {.callout-warning}
## Erreur fréquente

**L'intuition piège** : « Le projet qui rembourse la mise le plus vite est le
meilleur, puisqu'il est le moins risqué. »

**Pourquoi c'est faux** : le délai de récupération ignore tout ce qui se passe
après le remboursement ; ici, le projet Rapide récupère en 2 ans mais détruit
de la valeur, alors que le projet Durable crée plus de 15 000 € de valeur.

**Le bon raisonnement** : utiliser le délai comme indicateur de liquidité et
de risque, mais décider sur la VAN (ou l'annuité équivalente si les durées
diffèrent).

**Astuce mémo** : le délai mesure la liquidité, pas la création de valeur.
:::
```

### M3 S5 — Analyse du risque

```markdown
::: {.callout-warning}
## Erreur fréquente

**L'intuition piège** : « La VAN espérée est positive, donc le projet est
sûr. »

**Pourquoi c'est faux** : l'espérance est une moyenne ; deux projets de même
VAN espérée peuvent avoir des dispersions très différentes, et un scénario
pessimiste peut suffire à mettre l'entreprise en difficulté.

**Le bon raisonnement** : compléter la VAN espérée par l'écart-type, la VAN du
scénario pessimiste et les valeurs seuils des hypothèses clés.

**Astuce mémo** : regarde la moyenne ET la dispersion.
:::
```

---

## T038 — Audit: formula box → explanation

Generated from the module files on 2026-10-11. Each row is a formula-bearing
box; the next callout is the `Explication en langage clair`.

| Module | Séquence | Formula box | Explanation follows |
|--------|----------|-------------|---------------------|
| 01 | S2 | Formule — Capitalisation en intérêts simples | ✓ |
| 01 | S2 | Formule — Capitalisation en intérêts composés | ✓ |
| 01 | S3 | Formule — Actualisation | ✓ |
| 01 | S4 | Définition — Taux proportionnel | ✓ |
| 01 | S4 | Formule — Taux équivalent | ✓ |
| 01 | S5 | Formules — Annuités de fin de période | ✓ |
| 01 | S5 | Formules — Annuités de début de période | ✓ |
| 01 | S5 | Formules — Perpétuités | ✓ |
| 02 | S2 | Formule — Annuité d'un emprunt à annuités constantes | ✓ |
| 02 | S3 | Formule — Amortissement constant | ✓ |
| 02 | S4 | Définition — Taux actuariel (ou TAEG) | ✓ |
| 02 | S5 | Formule — Prix d'une obligation | ✓ |
| 02 | S6 | Définition — Duration de Macaulay $D_M$ | ✓ |
| 02 | S6 | Formule — Duration modifiée $D^*$ | ✓ |
| 03 | S1 | Formules — Flux de trésorerie d'exploitation | ✓ |
| 03 | S2 | Formule — Valeur actuelle nette | ✓ |
| 03 | S2 | Définition — Indice de profitabilité (IP) | ✓ |
| 03 | S3 | Définition — Taux de rentabilité interne | ✓ |
| 03 | S4 | Définition — Délai de récupération | ✓ |
| 03 | S4 | Formule — Annuité équivalente (AE) | ✓ |
| 03 | S5 | Formules — VAN espérée et dispersion | ✓ |

**Total explanations: 21.** Formal definitions that contain no formula (e.g.
*Définition — Équivalence financière*, *Définition — Valeur seuil*) carry no
explanation by design.

---

## T048 — Shinylive app code (as embedded in `module-03.qmd`)

Logic tested with `.venv/bin/python` on 2026-10-11: TRI ≈ 21,6753 %,
VAN(TRI) ≈ 5·10⁻⁷ €; VAN(10 %) = 3 219,91 € (same as the former OJS demo).
Sensitivity app: base VAN = 9 890,65 €, volume −20 % → −9 274,36 €,
break-even volume ≈ 1 793,6 pièces, E(VAN) = 8 692,84 €, σ = 11 918,09 €.

### VAN–TRI (T048 → T050, M3 S3)

```python
#| standalone: true
#| components: [viewer]
#| viewerHeight: 500

from shiny import App, render, ui
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

BG = '#1C2E22'
FG = '#D2CCC0'

I0 = 10000
FLUX = [3000, 3500, 4000, 4000, 3000]


def van(k):
    return -I0 + sum(cf / (1 + k) ** t for t, cf in enumerate(FLUX, start=1))


def tri(lo=0.0, hi=1.0, tol=1e-10):
    # Bissection : VAN(lo) > 0 > VAN(hi) ; on coupe l'intervalle en deux
    # jusqu'à encadrer le taux qui annule la VAN (pas de formule fermée).
    for _ in range(200):
        mid = (lo + hi) / 2
        if van(mid) > 0:
            lo = mid
        else:
            hi = mid
        if hi - lo < tol:
            break
    return (lo + hi) / 2


def eur(x):
    return f"{x:,.0f}".replace(",", "\u202f").replace("-", "\u2212") + " €"


TRI = tri()


def draw(k):
    ks = [i * 0.005 for i in range(101)]
    xs = [x * 100 for x in ks]
    vs = [van(x) for x in ks]
    fig, ax = plt.subplots(figsize=(7, 4))
    fig.patch.set_facecolor(BG)
    ax.set_facecolor(BG)
    for spine in ax.spines.values():
        spine.set_edgecolor(FG)
    ax.tick_params(colors=FG)
    ax.plot(xs, vs, color='steelblue', lw=2, label="VAN(k)")
    ax.axhline(0, color='gray', lw=1)
    ax.fill_between(xs, vs, 0, where=[v >= 0 for v in vs],
                    color='steelblue', alpha=0.15)
    ax.axvline(TRI * 100, color='tomato', ls='--', lw=1)
    ax.plot([TRI * 100], [0], 'o', color='tomato', ms=9,
            label=f"TRI ≈ {TRI * 100:.2f} % (VAN = 0)")
    ax.plot([k * 100], [van(k)], 'o', color='gold', ms=7,
            label=f"k = {k * 100:.1f} %")
    ax.set_xlabel("Taux d'actualisation k (%)", color=FG)
    ax.set_ylabel("VAN (€)", color=FG)
    ax.set_title("Le TRI est l'abscisse où la courbe coupe l'axe", color=FG)
    ax.grid(alpha=0.15, color=FG)
    leg = ax.legend(facecolor=BG, edgecolor=FG)
    for text in leg.get_texts():
        text.set_color(FG)
    fig.tight_layout()
    return fig


app_ui = ui.page_fluid(
    ui.tags.style(f"""
        body {{ background-color: {BG}; color: {FG}; padding: 12px;
               font-family: sans-serif; margin: 0; }}
        .form-label, label {{ color: {FG} !important; }}
        .info-box {{ background: #152119; border-radius: 6px;
                    padding: 10px 14px; margin: 8px 0;
                    border-left: 3px solid steelblue;
                    font-family: monospace; font-size: 0.9em; }}
    """),
    ui.h5("Profil VAN(k) — I0 = 10 000 €, flux 3 000 / 3 500 / 4 000 / "
          "4 000 / 3 000 €", style=f"color:{FG}"),
    ui.input_slider("k", "Taux d'actualisation k (%)",
                    min=0, max=50, value=10, step=0.5),
    ui.output_ui("info"),
    ui.output_plot("plot", height="340px"),
)


def server(input, output, session):

    @output
    @render.ui
    def info():
        k = input.k() / 100
        v = van(k)
        verdict = "projet acceptable" if v >= 0 else "projet rejeté"
        return ui.div(
            ui.HTML(
                f"VAN à {input.k():.1f} % = <b>{eur(v)}</b> ({verdict})"
                f"<br>TRI (bissection) ≈ <b>{TRI * 100:.2f} %</b>"
                f" — contrôle : VAN(TRI) = {eur(round(van(TRI)))}"
            ),
            class_="info-box",
        )

    @output
    @render.plot
    def plot():
        return draw(input.k() / 100)


app = App(app_ui, server)
```

### Sensibilité de la VAN (T051, M3 S5)

```python
#| standalone: true
#| components: [viewer]
#| viewerHeight: 720

from shiny import App, render, ui
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

BG = '#1C2E22'
FG = '#D2CCC0'

# Cas central : machine de l'atelier (Séquences 2 à 5)
BASE = {
    'volume': 2000,     # pièces vendues par an
    'marge': 12.0,      # marge unitaire (€ par pièce)
    'fixes': 9000.0,    # charges fixes annuelles (€)
    'I0': 50000.0,      # investissement initial (€)
    'k': 0.08,          # taux exigé
}
N = 5
LABELS = {
    'volume': "Volume vendu",
    'marge': "Marge unitaire (prix)",
    'fixes': "Charges fixes",
    'I0': "Investissement I0",
    'k': "Taux exigé k",
}
SCENARIOS = [            # (nom, multiplicateur du volume, probabilité)
    ("Pessimiste", 0.80, 0.25),
    ("Central", 1.00, 0.50),
    ("Optimiste", 1.15, 0.25),
]


def facteur(k):
    return sum(1 / (1 + k) ** t for t in range(1, N + 1))


def van(p):
    flux = p['volume'] * p['marge'] - p['fixes']
    return -p['I0'] + flux * facteur(p['k'])


def ajuste(base, variations):
    return {key: base[key] * (1 + variations.get(key, 0.0)) for key in base}


def volume_seuil(p):
    return (p['I0'] / facteur(p['k']) + p['fixes']) / p['marge']


def tornado(p, choc=0.20):
    # ΔVAN quand on fait varier un seul facteur de −20 % puis +20 %
    v0 = van(p)
    lignes = []
    for key in LABELS:
        bas = van(ajuste(p, {key: -choc})) - v0
        haut = van(ajuste(p, {key: +choc})) - v0
        lignes.append((key, bas, haut))
    lignes.sort(key=lambda r: max(abs(r[1]), abs(r[2])))
    return lignes


def scenarios(p):
    lignes = []
    for nom, mult, proba in SCENARIOS:
        lignes.append((nom, p['volume'] * mult,
                       van(ajuste(p, {'volume': mult - 1})), proba))
    esp = sum(v * pr for _, _, v, pr in lignes)
    ecart = sum(pr * (v - esp) ** 2 for _, _, v, pr in lignes) ** 0.5
    return lignes, esp, ecart


def eur(x):
    return f"{x:,.0f}".replace(",", "\u202f").replace("-", "\u2212") + " €"


def draw_tornado(p):
    lignes = tornado(p)
    fig, ax = plt.subplots(figsize=(7, 3.4))
    fig.patch.set_facecolor(BG)
    ax.set_facecolor(BG)
    for spine in ax.spines.values():
        spine.set_edgecolor(FG)
    ax.tick_params(colors=FG)
    y = list(range(len(lignes)))
    ax.barh(y, [r[1] for r in lignes], color='tomato', label="facteur −20 %")
    ax.barh(y, [r[2] for r in lignes], color='steelblue',
            label="facteur +20 %")
    ax.set_yticks(y)
    ax.set_yticklabels([LABELS[r[0]] for r in lignes], color=FG)
    ax.axvline(0, color=FG, lw=1)
    ax.set_xlabel("Variation de la VAN (€) autour du scénario affiché",
                  color=FG)
    ax.set_title("Diagramme en tornade : quel facteur pèse le plus ?",
                 color=FG)
    ax.grid(alpha=0.15, color=FG, axis='x')
    leg = ax.legend(facecolor=BG, edgecolor=FG, loc='lower right')
    for text in leg.get_texts():
        text.set_color(FG)
    fig.tight_layout()
    return fig


def slider(key, label):
    return ui.input_slider(key, label, min=-30, max=30, value=0, step=1,
                           post=" %")


app_ui = ui.page_fluid(
    ui.tags.style(f"""
        body {{ background-color: {BG}; color: {FG}; padding: 12px;
               font-family: sans-serif; margin: 0; }}
        .form-label, label {{ color: {FG} !important; }}
        .info-box {{ background: #152119; border-radius: 6px;
                    padding: 10px 14px; margin: 8px 0;
                    border-left: 3px solid steelblue;
                    font-family: monospace; font-size: 0.9em; }}
        table.sc {{ border-collapse: collapse; width: 100%; color: {FG};
                    font-size: 0.9em; }}
        table.sc td, table.sc th {{ border-bottom: 1px solid #2f4a37;
                                    padding: 3px 6px; text-align: right; }}
        table.sc td:first-child, table.sc th:first-child {{
            text-align: left; }}
    """),
    ui.h5("Analyse de sensibilité — machine à 50 000 €, 2 000 pièces × 12 € "
          "− 9 000 €, 5 ans, k = 8 %", style=f"color:{FG}"),
    ui.row(
        ui.column(
            4,
            slider("d_volume", "Volume vendu"),
            slider("d_marge", "Marge unitaire (prix)"),
            slider("d_fixes", "Charges fixes"),
            slider("d_I0", "Investissement I0"),
            slider("d_k", "Taux exigé k (en % de 8 %)"),
        ),
        ui.column(
            8,
            ui.output_ui("info"),
            ui.output_ui("table"),
        ),
    ),
    ui.output_plot("plot", height="300px"),
)


def server(input, output, session):

    def params():
        return ajuste(BASE, {
            'volume': input.d_volume() / 100,
            'marge': input.d_marge() / 100,
            'fixes': input.d_fixes() / 100,
            'I0': input.d_I0() / 100,
            'k': input.d_k() / 100,
        })

    @output
    @render.ui
    def info():
        p = params()
        v = van(p)
        flux = p['volume'] * p['marge'] - p['fixes']
        seuil = volume_seuil(p)
        marge_secu = 1 - seuil / p['volume']
        verdict = "crée de la valeur" if v >= 0 else "détruit de la valeur"
        seuil_txt = f"{seuil:,.0f}".replace(",", "\u202f")
        return ui.div(
            ui.HTML(
                f"Flux annuel = {p['volume']:.0f} × {p['marge']:.2f} € − "
                f"{eur(p['fixes'])} = <b>{eur(flux)}</b>"
                f"<br>k = {p['k'] * 100:.2f} % — VAN = <b>{eur(v)}</b>"
                f" ({verdict})"
                f"<br>Volume seuil (VAN = 0) ≈ <b>{seuil_txt} pièces</b>"
                f" — marge de sécurité {marge_secu * 100:.1f} %"
            ),
            class_="info-box",
        )

    @output
    @render.ui
    def table():
        lignes, esp, ecart = scenarios(params())
        rows = "".join(
            f"<tr><td>{nom}</td><td>{vol:.0f}</td><td>{eur(v)}</td>"
            f"<td>{pr:.2f}</td></tr>"
            for nom, vol, v, pr in lignes
        )
        return ui.HTML(
            "<table class='sc'><tr><th>Scénario</th><th>Volume</th>"
            "<th>VAN</th><th>Proba.</th></tr>" + rows +
            f"<tr><td><b>E(VAN)</b></td><td></td><td><b>{eur(esp)}</b></td>"
            "<td></td></tr>"
            f"<tr><td><b>σ(VAN)</b></td><td></td><td><b>{eur(ecart)}</b></td>"
            "<td></td></tr>"
            "</table>"
        )

    @output
    @render.plot
    def plot():
        return draw_tornado(params())


app = App(app_ui, server)
```

---

## T059 — Compliance table (contract checklist)

Concept sections, checked by script against `contracts/pedagogical-contract.md`
(✓ = element present in the section; last column = `Situation concrète`
appears before the first `$$`).

| Section | Situation | Explo | Schéma | Formule | Explic | Déf | Exemple | Interp | Erreur | Règle | #Err | Cas avant 1re formule |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 01 S2 Intérêts simples et intérêts composés | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 1 | ✓ |
| 01 S3 Actualisation et équivalence financièr | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 1 | ✓ |
| 01 S4 Taux proportionnels et taux équivalent | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 1 | ✓ |
| 01 S5 Annuités constantes | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 1 | ✓ |
| 02 S2 Emprunt amortissable à annuités consta | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 1 | ✓ |
| 02 S3 Autres modalités de remboursement | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 1 | ✓ |
| 02 S4 Coût réel du crédit et taux actuariel | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 1 | ✓ |
| 02 S5 Introduction aux obligations | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 1 | ✓ |
| 02 S6 Sensibilité obligataire | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 1 | ✓ |
| 03 S2 Valeur actuelle nette (VAN) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 1 | ✓ |
| 03 S3 Taux de rentabilité interne (TRI) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 1 | ✓ |
| 03 S4 Délai de récupération et comparaison d | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 1 | ✓ |
| 03 S5 Analyse du risque | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | 1 | ✓ |

Synthesis sections (M1 S6, M2 S7, M3 S6): `Contexte` (`.callout-note`) →
`### Étape N — …` → `Cadre de décision` (`.callout-important`); Règle d'or
reminder present; no `Erreur fréquente` (✓ all three).

Title harmonisation: all 13 concept sections use `Situation concrète`,
`Observez le schéma`, `Formule(s) — …`, `Explication en langage clair`,
`Définition — …`, `Exemple résolu[ — …]`, `Interprétation économique[ — …]`
and `Erreur fréquente`. Fixed during T059: M1 S3 `### Exemple décisionnel`
→ `### Exemple résolu — Décision d'arbitrage`; M3 S2 `## Interprétation
économique de la VAN` → `## Interprétation économique — Que mesure la VAN ?`
(no anchor links pointed to either heading).

Known deviations left as-is (existing content, out of scope): the Taux
actuariel and Duration de Macaulay definition boxes use `.callout-note`
rather than `.callout-important`; M2 S6 has two `Situation concrète`
callouts by design (spec Edge Cases).
