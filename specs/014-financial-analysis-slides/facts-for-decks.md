# Facts for decks (F1–F15)

Final values and source-line wording for the deck agents. Checked on 2026-10-18. Details and URLs are in `coverage-map.md` ("Verified facts"). Where this file and `research.md` differ, **this file wins**.

## Changes versus research.md (read these first)

1. **F3 eligibility changed.** The BdF *Guide de référence* (update September 2026) says refinancing eligibility is **1+ à 2-**. The temporary 3+ to 4+ window ended on **16/12/2024** (BdF newsletter, Dec. 2024). Do **not** write "éligible 1+ à 4+" except as "jusqu'au 16/12/2024, un dispositif exceptionnel a accepté 3+ à 4+".
2. **F11 resolved: 23 mois** (cote X = exercice clos depuis plus de 23 mois), BdF *Guide de référence* (update September 2026). The 20-month and 21-month values are older.
3. **Cote d'activité table changed in H and J.** Current guide: H ≥ 1,25 et < 1,5 M€ · J ≥ 0,50 et < 1,25 M€ (older: H 0,75–1,5, J 0,5–0,75). Full table: A ≥ 750 · B ≥ 150 et < 750 · C ≥ 50 et < 150 · D ≥ 30 et < 50 · E ≥ 15 et < 30 · F ≥ 7,5 et < 15 · G ≥ 1,5 et < 7,5 · H ≥ 1,25 et < 1,5 · J ≥ 0,50 et < 1,25 · K ≥ 0,25 et < 0,50 · L ≥ 0,10 et < 0,25 · M < 0,10 · N non significatif · X inconnu ou trop ancien. Letters skip I (H → J). Unit: M€ of chiffre d'affaires.
4. **F6 updated:** 322 504 entreprises cotées au 31/12/2024 (not 325 105). Per-grade counts below.
5. **F15 found**, **F13 URL found**, **F9 verdict: yes** (see table).
6. **Rule "FP < ½ capital ⇒ at best 5+"** (T037, PPT 101, about *filiales*): the 2026 guide has no such sentence. It gives "fonds propres inférieurs à la moitié du capital social" as an example for cote **4-** when mitigated by positive information, and "perte de plus de la moitié du capital social depuis plus de 36 mois" as a possible trigger for a degraded cote. Word it as: « FP < ½ capital = signal d'alerte : le Guide cite cet exemple pour une cote 4- atténuée par des éléments positifs ; la méthode de l'ancien support retenait « au mieux 5+ » pour les filiales »; do not present "5+" as an official rule.
7. **Case data**: ConcoursMania SA accounts were found (no FR-017a fallback). Archives consolidées (`exr-archives-consolidees`): the slide must state the 20 % margin assumption on the intragroup stock (see `answer-keys-25pct.md` §6).
8. **Day-plan wording**: block 2.2 says "eligibility 1+–4+": use 1+ à 2- (item 1).

## Table

| # | Value to use on slides | Source line to cite |
|---|---|---|
| F1 | Seuil de cotation : CA ≥ **1 250 K€** (1,25 M€) depuis le **12/01/2025** (750 K€ auparavant, inchangé depuis plus de 40 ans) | Source : Banque de France, *Évaluation des performances de la cotation 2024*, sept. 2025, encadré 1 ; *Guide de référence de la cotation* (sept. 2026). |
| F2 | Horizon : « un à trois ans » (page officielle) ; 3 ans = référence des statistiques de défaut | Source : Banque de France, « Comprendre la cotation et l'indicateur dirigeant » ; *Guide de référence de la cotation* (sept. 2026). |
| F3 | Cote de crédit : **22 positions** 1+, 1, 1-, 2+, 2, 2-, 3+, 3, 3-, 4+, 4, 4-, 5+, 5, 5-, 6+, 6, 6-, 7, 8, P, 0. **Éligibles au refinancement Eurosystème : 1+ à 2-** (3+ à 4+ : dispositif exceptionnel terminé le 16/12/2024). Ancienne échelle 3++ … 9 = « échelle avant 2022 » | Source : Banque de France, *Guide de référence de la cotation* (sept. 2026) ; lettre d'information BdF, déc. 2024. |
| F3b | Libellés (guide sept. 2026) : 1+ excellente++ · 1 excellente+ · 1- excellente · 2+ très satisfaisante++ · 2 très satisfaisante+ · 2- très satisfaisante · 3 forte+ · 3- forte · 4+ bonne+ · 4 bonne · 4- intermédiaire+ · 5+ intermédiaire– · 5 fragile · 5- assez faible · 6+ très faible · 6 menacée · 6- compromise · 7 très compromise · 8 fortement compromise · P défaillante · 0 non significative. Pour 3+ : libellé « forte++ » (déduit, non imprimé dans l'extrait lu) | idem |
| F4 | Défaut à 1 an (firmes cotées au 31/12/2023, observé en 2024), en % : 1+ 0,00 · 1 0,02 · 1- 0,02 · 2+ 0,06 · 2 0,03 · 2- 0,10 · 3+ 0,22 · 3 0,18 · 3- 0,30 · 4+ 0,51 · 4 1,26 · 4- 1,90 · 5+ 2,82 · 5 5,21 · 5- 3,89 · 6+ 5,63 · 6 8,17 · 6- 15,03 · 7 20,02 · 8 27,42 · total 1,75 % | Source : Banque de France, *Évaluation des performances de la cotation 2024*, annexe 2 (reproduction autorisée avec mention de la source). |
| F5 | Taux de défaut global : **1,75 %** à 1 an · **3,22 %** à 2 ans · **3,68 %** à 3 ans | Source : Banque de France, *Évaluation des performances de la cotation 2024*, §2.1. |
| F6 | **322 504** entreprises cotées au 31/12/2024 (dont 320 604 cotes 1+ à 8, 1 900 cotes P). Par cote : 1+ 13 168 · 1 11 408 · 1- 31 752 · 2+ 31 204 · 2 22 361 · 2- 16 463 · 3+ 25 762 · 3 14 956 · 3- 13 958 · 4+ 23 148 · 4 40 033 · 4- 18 133 · 5+ 7 933 · 5 13 422 · 5- 9 556 · 6+ 5 281 · 6 13 894 · 6- 4 365 · 7 2 528 · 8 1 279 · P 1 900. (31/12/2023 : 325 105.) Le seuil a été relevé le 12/01/2025 : le chiffre à fin 2025 sera plus bas | Source : Banque de France, *Cotation – chiffres clés au 31 décembre 2024* (07/2025). |
| F7 | Seuils de consolidation obligatoire : **30 M€ de bilan / 60 M€ de CA / 250 salariés**, pour les exercices ouverts à compter du 01/01/2025 (24 / 48 / 250 avant) | Source : décret n° 2024-152 ; art. L.233-17 et D.230-2 C. com. |
| F8 | Règles de consolidation : **ANC 2020-01** (abroge CRC 99-02 ; exercices ouverts à compter du 01/01/2021) | Source : ANC, règlement n° 2020-01. |
| F9 | **Intégration proportionnelle : toujours en vigueur en normes françaises** pour les entités sous **contrôle conjoint** (art. **221-1** et **221-3** du règlement ANC 2020-01, Livre II, Titre II, ch. I). Supprimée en IFRS depuis IFRS 11 (2013). Wording: « IP : contrôle conjoint, normes françaises (ANC 2020-01, art. 221-3) ; interdite en IFRS » | Source : ANC, règlement n° 2020-01 (version au 1er janvier 2026), art. 221-1 et 221-3. |
| F10 | Taux d'IS normal : **25 %** | Source : CGI art. 219. |
| F11 | Cote X : **23 mois** (exercice clos depuis plus de 23 mois) | Source : Banque de France, *Guide de référence de la cotation* (sept. 2026), §2.2. |
| F12 | DPEF → **CSRD**, transposée par l'ordonnance n° 2023-1142 | Source : ordonnance n° 2023-1142 ; décret n° 2023-1394. |
| F13 | IFRS 18 *Presentation and Disclosure in Financial Statements* : remplace IAS 1, applicable aux exercices ouverts à compter du **01/01/2027** ; deux sous-totaux obligatoires (résultat opérationnel ; résultat avant financement et impôts) ; mesures de performance définies par la direction (MPM) à documenter. URL : https://www.ifrs.org/issued-standards/list-of-standards/ifrs-18-presentation-and-disclosure-in-financial-statements/ | Source : IFRS Foundation, IFRS 18 (avril 2024). |
| F14 | Vidéo « Qu'est-ce que la cotation ? \| Banque de France » : https://www.youtube.com/watch?v=VHvdDBbcSn4 | Source : Banque de France (chaîne YouTube). |
| F15 | Vidéo BdF « Quelles sont nos missions ? \| Banque de France » (2 min 23 s, même durée que `Cest quoi la BDF.mp4` du dossier) : https://www.youtube.com/watch?v=N_z1nhTETuk . À présenter comme « vidéo de présentation des missions de la Banque de France » (le titre officiel n'est pas « C'est quoi la BDF ») | Source : Banque de France (chaîne YouTube). |

## Case data (Jour 1, `#exr-concoursmania-lectra-a/b`)

- **ConcoursMania SA, exercice 2016 (comptes sociaux, en euros)** : trouvés, original scanné. `specs/014-financial-analysis-slides/case-data-concoursmania-2016.md`. Source line: « Source : Groupe ConcoursMania SA, comptes annuels 2016 (rapport du commissaire aux comptes, 28/04/2017), Klarsen – information réglementée, https://www.klarsen.com/2021/01/01/information-reglementee-archives/ ». Les totaux (RE −414, RCAI −421, RN −812, FRNG 1 959, BFR −749, TN 2 705) **réconcilient avec le corrigé**. Ne pas confondre avec les comptes **consolidés** du groupe (RCAI −115,9 K€, RN −473,2 K€). Statut : verified, pas besoin de la phrase de repli FR-017a.
- **Lectra SA, exercice 2016 (comptes de la société mère, en K€)** : `specs/014-financial-analysis-slides/case-data-lectra-2016.md`. Source line: « Source : Lectra, *Rapport financier 2016*, « Comptes de la société mère », p. 154-155 (publié dans le dossier de l'AGO du 28/04/2017), https://www.lectra.com/sites/default/files/2021-06/20170428_dossierdactionnaires_agoe.pdf ». Bilan et totaux (RE 15 712, RCAI 18 943, RN 15 468, FRNG 69 282, TN 48 853) **réconcilient**. Les lignes de détail du corrigé (marchandises/production vendue, subventions, transferts) viennent de la liasse fiscale, **non publiée** : le fichier donne le tableau publié (par nature) et le tableau du corrigé, à utiliser pour l'énoncé avec la mention « détail de la liasse, d'après le corrigé du cours ».

## Open items

See the "Open items" section at the end of `coverage-map.md`.
