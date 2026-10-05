# Feature Specification: Cours de Mathématiques Financières (M1)

**Feature Branch**: `009-math-finance-course`

**Created**: 2026-10-04

**Status**: Draft

**Input**: Construire le cours de mathématiques financières pour des étudiants de Master 1 en école de commerce à `fr/teaching/mathematical-finance/`, en s'appuyant sur le plan pédagogique détaillé de `teaching/mathematical-finance/index.qmd`.

---

## User Scenarios & Testing *(mandatory)*

### User Story 1 — Étudiant accède au syllabus et à la structure du cours (Priority: P1)

Un étudiant de M1 ouvre le cours de mathématiques financières depuis la barre de navigation du site. Il trouve un syllabus clair précisant les objectifs, le calendrier des trois journées et la bibliographie recommandée. Il peut ensuite naviguer directement vers chaque séquence depuis la page d'accueil du cours.

**Why this priority**: Sans syllabus et sans navigation fonctionnelle, aucune autre page du cours n'est accessible de façon structurée. C'est le point d'entrée de toute l'expérience pédagogique.

**Independent Test**: On peut tester cette histoire indépendamment en rendant uniquement `fr/teaching/mathematical-finance/index.qmd` et en vérifiant que le syllabus s'affiche, que la bibliographie est présente, et que les liens vers les journées fonctionnent (même si les pages cibles ne sont pas encore créées).

**Acceptance Scenarios**:

1. **Given** qu'un étudiant arrive sur `/fr/teaching/mathematical-finance/`, **When** il charge la page, **Then** il voit le titre du cours, les objectifs généraux, le calendrier des trois journées et la bibliographie recommandée.
2. **Given** que le syllabus est affiché, **When** l'étudiant clique sur un lien de journée dans le tableau de bord, **Then** il est redirigé vers la page correspondante dans la barre latérale.
3. **Given** que la constitution T-VIII s'applique, **When** la page index est rendue, **Then** une section « Bibliographie recommandée » est présente avec au minimum auteur(s), titre, édition et éditeur pour chaque référence.

---

### User Story 2 — Étudiant étudie la Journée 1 : valeur temps et annuités (Priority: P1)

Un étudiant consulte la page de la Journée 1 pour comprendre les intérêts simples et composés, la capitalisation, l'actualisation, la conversion de taux et les annuités constantes. Il lit la théorie, exécute les exemples résolus et s'entraîne sur les exercices avec solutions escamotables.

**Why this priority**: La Journée 1 fournit les fondations conceptuelles (valeur temps de l'argent, actualisation, annuités) sur lesquelles reposent entièrement les Journées 2 et 3. Elle représente le premier accès étudiant à du contenu substantiel.

**Independent Test**: Rendre `fr/teaching/mathematical-finance/module-01.qmd` seul et vérifier la présence de : théorie, formules LaTeX, exemples résolus, exercices avec solutions escamotables et au moins une démonstration interactive.

**Acceptance Scenarios**:

1. **Given** qu'un étudiant ouvre la page Journée 1, **When** il fait défiler la page, **Then** il trouve dans l'ordre : intuition économique, représentation sur ligne du temps, formalisation mathématique, décision managériale.
2. **Given** qu'un exercice est affiché, **When** l'étudiant clique sur « Voir la solution », **Then** la solution se déroule sans rechargement de page.
3. **Given** que la constitution T-IV s'applique, **When** la page est chargée, **Then** au moins une démonstration interactive (Shinylive ou OJS) est présente pour le concept prioritaire de la journée (capitalisation vs actualisation).
4. **Given** qu'une formule mathématique est introduite, **When** elle est affichée, **Then** une explication en langage courant l'accompagne immédiatement.

---

### User Story 3 — Étudiant étudie la Journée 2 : emprunts et obligations (Priority: P2)

Un étudiant consulte la page de la Journée 2 pour comprendre les tableaux d'amortissement, le coût actuariel d'un crédit et la valorisation des obligations. Il peut lire le cours, consulter les tableaux types et s'exercer sur les cas pratiques.

**Why this priority**: La Journée 2 constitue la deuxième brique thématique autonome (financement et dette). Elle peut être consultée indépendamment de la Journée 3, mais dépend de la maîtrise des annuités (Journée 1).

**Independent Test**: Rendre `fr/teaching/mathematical-finance/module-02.qmd` et vérifier : tableau d'amortissement à annuités constantes construit pas-à-pas, section coût actuariel, section obligations avec formule de valorisation, exercices avec solutions escamotables.

**Acceptance Scenarios**:

1. **Given** qu'un étudiant ouvre la page Journée 2, **When** il consulte la section « Tableau d'amortissement », **Then** il voit un tableau structuré (Période / Capital initial / Intérêts / Amortissement / Annuité / Capital restant dû) avec un exemple numérique complet.
2. **Given** que la relation prix-taux des obligations est exposée, **When** l'étudiant lit la section, **Then** il trouve une formule de valorisation obligataire et une explication de la relation inverse prix / taux de marché.
3. **Given** qu'une démonstration interactive est requise (T-IV), **When** la page est chargée, **Then** au moins un widget interactif illustre l'impact de la variation du taux sur le prix d'une obligation.

---

### User Story 4 — Étudiant étudie la Journée 3 : VAN, TRI et risque (Priority: P2)

Un étudiant consulte la page de la Journée 3 pour apprendre à construire des flux de trésorerie, calculer la VAN et le TRI, mener une analyse de sensibilité et formuler une recommandation d'investissement.

**Why this priority**: La Journée 3 représente l'aboutissement du cours (décision d'investissement). Elle dépend des Journées 1 et 2 mais peut être évaluée indépendamment si les pages amont existent.

**Independent Test**: Rendre `fr/teaching/mathematical-finance/module-03.qmd` et vérifier : construction de flux pas-à-pas, formule VAN, limites du TRI, analyse de sensibilité, tableau de scénarios, note de recommandation modèle.

**Acceptance Scenarios**:

1. **Given** qu'un étudiant ouvre la page Journée 3, **When** il lit la section sur les flux de trésorerie, **Then** il trouve la distinction claire entre résultat comptable et flux de trésorerie, le traitement du BFR et de la valeur résiduelle.
2. **Given** que la VAN est présentée, **When** l'étudiant lit la règle de décision, **Then** les trois cas (VAN > 0, VAN = 0, VAN < 0) sont expliqués avec leur interprétation économique.
3. **Given** qu'une démonstration interactive est requise (T-IV), **When** la page est chargée, **Then** un widget permet de faire varier au moins une hypothèse (taux, flux, durée) et d'observer l'impact sur la VAN.

---

### User Story 5 — Étudiant consulte le glossaire (Priority: P3)

Un étudiant recherche la définition d'un terme ou d'un symbole rencontré dans le cours. Il accède au glossaire depuis la barre latérale et trouve chaque terme avec sa notation, sa définition en langage courant et, pour les lettres grecques, une aide à la prononciation.

**Why this priority**: Le glossaire est obligatoire par la constitution (T-V) mais ne bloque pas la consultation des pages de cours si absent. Il améliore l'expérience sans être un prérequis au contenu.

**Independent Test**: Rendre `fr/teaching/mathematical-finance/glossaire.qmd` et vérifier que tous les symboles introduits dans les journées sont listés avec notation + définition.

**Acceptance Scenarios**:

1. **Given** qu'un étudiant clique sur « Glossaire » dans la barre latérale, **When** la page se charge, **Then** tous les symboles et termes définis dans les trois journées sont présents.
2. **Given** qu'un terme est listé, **When** l'étudiant le lit, **Then** il trouve au minimum : notation, définition en français courant, contexte d'utilisation.

---

### Edge Cases

- Que se passe-t-il si un étudiant accède directement à la Journée 2 ou 3 sans avoir consulté les journées précédentes ? → Chaque page doit être autonome avec des prérequis explicitement mentionnés en début de page.
- Comment le site gère-t-il la navigation entre la version anglaise (`/teaching/mathematical-finance/`) et la version française (`/fr/teaching/mathematical-finance/`) ? → Le sélecteur de langue dans la navbar doit lier les deux versions conformément au principe VI de la constitution.
- Que se passe-t-il si une démonstration interactive (Shinylive) échoue à charger ? → Un message de repli (`.callout-important` avec `TODO:` ou message d'erreur lisible) doit indiquer à l'étudiant comment accéder au contenu alternatif.

---

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: Le site DOIT disposer d'une page `fr/teaching/mathematical-finance/index.qmd` servant de syllabus du cours, incluant objectifs, calendrier des trois journées et bibliographie recommandée (constitution T-VIII).
- **FR-002**: Le cours DOIT être structuré en trois pages de journée distinctes (`module-01.qmd`, `module-02.qmd`, `module-03.qmd`) dans `fr/teaching/mathematical-finance/`.
- **FR-003**: Le cours DOIT disposer d'un glossaire central (`glossaire.qmd`) listant tous les symboles et termes mathématiques introduits (constitution T-V).
- **FR-004**: Chaque page de journée DOIT suivre la séquence pédagogique : intuition économique → représentation → formalisation mathématique → décision managériale (constitution T-II).
- **FR-005**: Chaque page de journée DOIT inclure au moins une démonstration interactive (Shinylive Python ou Observable JS) pour le concept prioritaire de la journée (constitution T-IV).
- **FR-006**: Chaque formule mathématique DOIT être accompagnée d'une explication en langage courant (constitution T-III).
- **FR-007**: Les exercices DOIT être présentés en trois niveaux de difficulté croissante, avec solutions dans des blocs escamotables (`.callout-caution collapse="true"`).
- **FR-008**: Chaque page de journée DOIT inclure au moins une preuve ou dérivation formelle collapsible pour le théorème ou la formule centrale de la séquence (constitution T-VI).
- **FR-009**: Toutes les pages DOIVENT déclarer `lang: fr` dans leur front matter Quarto.
- **FR-010**: Les pages du cours français DOIVENT être enregistrées dans un bloc `website.sidebar` dédié dans `_quarto.yml` (constitution II).
- **FR-011**: Le cours français DOIT avoir une page symétrique anglaise publiée ou un stub avec mention « traduction en cours » (constitution VI).
- **FR-012**: Tout le contenu LaTeX DOIT utiliser la syntaxe standard `$...$` / `$$...$$` (constitution V).
- **FR-013**: Aucun style inline (`style=`) ni bloc `<style>` DOIT apparaître dans les fichiers `.qmd` ; tout le CSS personnalisé va dans `assets/dark.scss` (constitution V).
- **FR-014**: La Journée 1 DOIT couvrir : intérêts simples et composés, capitalisation, actualisation, taux proportionnels et équivalents, annuités constantes (fin/début de période), annuités différées, perpétuités.
- **FR-015**: La Journée 2 DOIT couvrir : emprunt à annuités constantes, amortissement constant, emprunt in fine, différé d'amortissement, coût actuariel, valorisation obligataire, duration de Macaulay, duration modifiée.
- **FR-016**: La Journée 3 DOIT couvrir : construction des flux de trésorerie différentiels (BFR, valeur résiduelle, traitement fiscal), VAN, TRI (avec limites), indice de profitabilité, délai de récupération (simple et actualisé), annuité équivalente, analyse de sensibilité, analyse par scénarios.
- **FR-017**: Un formulaire de référence DOIT être intégré (en annexe ou page dédiée) listant toutes les formules essentielles du cours.

### Key Entities

- **Journée** : unité d'enseignement de 6 heures ; contient plusieurs séquences pédagogiques ; correspond à un fichier `.qmd` dédié.
- **Séquence** : bloc thématique au sein d'une journée ; contient intuition, représentation, formalisation, application.
- **Exercice** : problème à résoudre ; classé par niveau (N1 application directe, N2 problème contextualisé, N3 étude de cas) ; solution escamotable.
- **Démonstration interactive** : widget Shinylive ou OJS illustrant un concept clé ; obligatoire par journée.
- **Glossaire** : fichier centralisé listant tous les symboles et termes du cours.
- **Syllabus** : `index.qmd` du cours ; point d'entrée ; contient la bibliographie recommandée.

---

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Les cinq pages du cours (`index.qmd`, `module-1.qmd`, `module-2.qmd`, `module-3.qmd`, `glossaire.qmd`) sont rendues sans erreur par `quarto render` et accessibles depuis la barre latérale.
- **SC-002**: Chaque page de journée contient au minimum une démonstration interactive fonctionnelle (chargement sans erreur en prévisualisation locale).
- **SC-003**: L'ensemble des formules LaTeX du formulaire de référence (10 formules essentielles) est présent et rendu correctement dans au moins une page du cours.
- **SC-004**: Le glossaire recense 100 % des symboles et termes introduits dans les trois journées (vérifiable par recherche croisée).
- **SC-005**: La navigation barre latérale → page de journée → glossaire fonctionne sans lien cassé.
- **SC-006**: La version française et la version anglaise du cours sont toutes deux accessibles depuis le sélecteur de langue dans la navbar (ou un stub de redirection est en place).
- **SC-007**: Chaque page de journée propose des exercices sur les trois niveaux de difficulté avec solutions escamotables.
- **SC-008**: `quarto render` termine avec exit code 0 après l'ajout de l'ensemble des fichiers du cours.

---

## Assumptions

- Le contenu pédagogique source est le plan détaillé dans `teaching/mathematical-finance/index.qmd` ; il constitue la référence de fond (théorie, exemples, exercices) à transposer dans des pages Quarto structurées.
- Une version anglaise du cours (`teaching/mathematical-finance/`) existe ou sera créée en parallèle ; si elle est absente au moment de la livraison, un stub de redirection suffit pour satisfaire le principe VI.
- Les démonstrations interactives prioritaires sont : (J1) capitalisation vs actualisation interactive, (J2) impact taux / prix obligation, (J3) sensibilité VAN à un paramètre — les autres peuvent être marquées `TODO:` dans un `.callout-important`.
- Les exercices et cas pratiques Excel mentionnés dans le plan sont traduits en exercices Quarto ; les fichiers Excel de référence ne font pas partie du périmètre de cette spec (livraison optionnelle).
- La périodicité pédagogique (exercices de niveau 1, 2, 3) est interprétée comme : N1 = application directe d'une formule, N2 = problème contextualisé nécessitant le choix de la formule, N3 = étude de cas multi-étapes avec recommandation.
- Le cours cible des étudiants francophones de M1 en école de commerce ; le niveau de langage est volontairement accessible (principe T-III) sans jargon non défini.
- Aucune dépendance à une API externe ou à un service tiers n'est requise pour le rendu du cours.
- Le formulaire de référence (10 formules essentielles) sera intégré soit en annexe de `index.qmd`, soit dans une page dédiée `formulaire.qmd`.
