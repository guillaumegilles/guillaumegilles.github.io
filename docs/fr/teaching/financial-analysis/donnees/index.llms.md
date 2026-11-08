> **Données fictives — usage pédagogique uniquement.** Le Groupe AUBÉPINE (SIREN fictif 999 888 777), ses filiales et tous leurs chiffres sont inventés pour le cours. Aucune société réelle ne correspond à ces données.

## Le fil rouge du cours

Toutes les études de cas du cours d’analyse financière s’appuient sur les **comptes consolidés du Groupe AUBÉPINE**, en normes françaises (PCG, règlement CRC 99-02), pour trois exercices : **2023 (N-2), 2024 (N-1) et 2025 (N)**. Les montants sont en **k€**.

- [Bilan consolidé](../../../../fr/teaching/financial-analysis/donnees/bilan-consolide.llms.md)
- [Compte de résultat consolidé](../../../../fr/teaching/financial-analysis/donnees/compte-de-resultat.llms.md)
- [Annexe](../../../../fr/teaching/financial-analysis/donnees/annexe.llms.md) (périmètre, écarts d’acquisition, opérations intragroupe, intérêts minoritaires)
- [Tableau des flux de trésorerie](../../../../fr/teaching/financial-analysis/donnees/flux-tresorerie.llms.md)
- [Téléchargements](../../../../fr/teaching/financial-analysis/donnees/telechargements.llms.md) (Excel et PDF)

## Périmètre de consolidation

| Entité                 | Forme | % d’intérêt | Méthode | CP à l’acquisition (k€) |
|------------------------|-------|-------------|---------|-------------------------|
| AUBÉPINE SA            | SA    | —           | Mère    | —                       |
| AUBÉPINE NORD SAS      | SAS   | 75 %        | IG      | 600                     |
| AUBÉPINE SUD SAS       | SAS   | 80 %        | IG      | 400                     |
| VERGER Export SARL     | SARL  | 60 %        | IG      | 350                     |
| TERROIR PARTENAIRES SA | SA    | 30 %        | MEE     | 300                     |

AUBÉPINE SA consolide ses trois filiales en **intégration globale** et comptabilise sa participation dans TERROIR PARTENAIRES SA en **mise en équivalence** (quote-part de résultat au compte de résultat consolidé).

## Démo interactive : calculer un ratio du cours

Choisissez un ratio : il est recalculé ici, dans votre navigateur, à partir des comptes consolidés publiés (bilan et compte de résultat ci-dessus).

```` numberSource
```{ojs}
//| echo: false
const dr_data = {
  2023: {ca: 6100, rex: 1260, rn: 817, rn_pg: 680, capital: 2000, reserves: 1054, mino_b: 740, emprunts: 3430, dettes_fourn: 1190, immo_brut: 4600, dap: -1310, eaq: 1327, titres_mee: 107, stocks: 1235, creances: 1230, dispo: 1905},
  2024: {ca: 6600, rex: 1420, rn: 943, rn_pg: 784, capital: 2000, reserves: 1348, mino_b: 852, emprunts: 3160, dettes_fourn: 1260, immo_brut: 5180, dap: -1670, eaq: 1042, titres_mee: 124, stocks: 1335, creances: 1330, dispo: 2063},
  2025: {ca: 7100, rex: 1580, rn: 1071, rn_pg: 890, capital: 2000, reserves: 1690, mino_b: 985, emprunts: 2870, dettes_fourn: 1330, immo_brut: 5760, dap: -2030, eaq: 700, titres_mee: 143, stocks: 1435, creances: 1430, dispo: 2327}
}
const dr_defs = {
  "Marge nette (%)": d => 100 * d.rn / d.ca,
  "ROE — rentabilité financière (%)": d => 100 * d.rn_pg / (d.capital + d.reserves + d.rn_pg),
  "ROCE — rentabilité économique (%)": d => 100 * d.rex / (d.capital + d.reserves + d.rn_pg + d.mino_b + d.emprunts - d.dispo),
  "Taux d'endettement (%)": d => 100 * d.emprunts / (d.capital + d.reserves + d.rn_pg + d.mino_b),
  "FRNG (k€)": d => d.capital + d.reserves + d.rn_pg + d.mino_b + d.emprunts - (d.immo_brut + d.dap + d.eaq + d.titres_mee),
  "BFR (k€)": d => d.stocks + d.creances - d.dettes_fourn,
  "Trésorerie nette (k€)": d => d.dispo
}
viewof dr_choix = Inputs.select(Object.keys(dr_defs), {label: "Ratio à calculer"})
```
````

> **IMPORTANT:**

```` numberSource
```{ojs}
//| echo: false
const dr_f = dr_defs[dr_choix]
const dr_lignes = Object.keys(dr_data).map(y => ({exercice: y, valeur: +dr_f(dr_data[y]).toFixed(2)}))
Plot.plot({
  style: {background: "transparent", color: "currentColor"},
  x: {label: "Exercice"},
  y: {label: dr_choix, grid: true},
  marks: [Plot.barY(dr_lignes, {x: "exercice", y: "valeur", fill: "currentColor"})]
})
```
````

> **IMPORTANT:**

## Usage de l’IA générative

Ce jeu de données est un support de cours, pas un devoir à rendre tel quel. Pour les travaux notés individuels, l’enseignant peut distribuer des **variantes individuelles** du jeu de données (chiffres légèrement modifiés, générées à partir de votre identifiant étudiant) : le travail rendu doit correspondre à votre propre variante et être accompagné du fichier de travail (tableur avec les formules). Les restitutions orales s’appliquent normalement. Cette politique est affichée ici volontairement : rien n’est caché dans ces pages.

> **CAUTION:**
>
> Chaque écriture d’élimination de consolidation débite et crédite le **même montant** : l’élimination des titres (crédit) est compensée par le débit des capitaux propres de la filiale, de l’écart d’acquisition et des intérêts minoritaires ; l’élimination d’un prêt intragroupe touche une créance à l’actif et une dette au passif du même montant. Comme le bilan agrégé vérifie \\A = D + K\\, et que chaque écriture conserve cette égalité, le bilan consolidé s’équilibre toujours. Un bilan consolidé qui ne s’équilibre pas révèle une écriture unilatérale (par exemple une dette non comptabilisée par l’une des sociétés du groupe).
