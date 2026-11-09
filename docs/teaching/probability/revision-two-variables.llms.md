[📍 Retour à la carte du cours](index.llms.md) · [📝 Feuille d’exercices](exercises-two-variables.llms.md)

> Cette fiche résume les cinq chapitres de la partie **Deux variables**. L’objectif est simple : savoir identifier l’objet étudié, choisir la bonne formule et enchaîner les calculs sans confusion.

## 1 Vue d’ensemble des 5 chapitres

| Chapitre | À retenir | Réflexe de calcul |
|----|----|----|
| [Statistiques bivariées](bivariate.llms.md) | Tableau de contingence, marginales, conditionnelles, indépendance, test du \\\chi^2\\ | Additionner par lignes/colonnes, comparer profils et effectifs théoriques |
| [Intégrales sur \\\mathbb{R}^2\\](double-integrals-over-r2.llms.md) | Tonelli/Fubini, description du domaine, ordre d’intégration | Commencer par dessiner le domaine |
| [Loi conjointe d’un couple continu](pair-continuous-rv-joint-distribution.llms.md) | Densité conjointe \\f(x,y)\\, support, probabilités sur une région | Vérifier \\f\ge 0\\ et \\\iint f = 1\\ |
| [Lois marginales](pair-continuous-rv-marginal-distribution.llms.md) | Marginalisation, densités conditionnelles, indépendance | Intégrer selon l’autre variable |
| [Couples de variables à densité](joint-continuous-random-variables.llms.md) | Covariance, corrélation, convolution, vision d’ensemble | Passer de la loi conjointe aux grandeurs numériques |

## 2 1. Statistiques bivariées

Quand on observe deux caractères sur une même population, l’information centrale est la **distribution conjointe** :

\\ n\_{ij} = \text{effectif du couple } (x_i,y_j), \qquad f\_{ij}=\frac{n\_{ij}}{n}. \\

On en déduit les **marginales** :

\\ n\_{i\cdot}=\sum_j n\_{ij}, \qquad n\_{\cdot j}=\sum_i n\_{ij}, \qquad f\_{i\cdot}=\frac{n\_{i\cdot}}{n}, \qquad f\_{\cdot j}=\frac{n\_{\cdot j}}{n}. \\

Les **fréquences conditionnelles** mesurent le profil d’une variable quand l’autre est fixée :

\\ f\_{y_j\mid x_i}=\frac{n\_{ij}}{n\_{i\cdot}}, \qquad f\_{x_i\mid y_j}=\frac{n\_{ij}}{n\_{\cdot j}}. \\

> **IMPORTANT:**
>
> 1.  Construire ou compléter le tableau de contingence.
> 2.  Calculer les marginales.
> 3.  Comparer les distributions conditionnelles.
> 4.  Conclure : profils semblables \\\Rightarrow\\ possible indépendance ; profils différents \\\Rightarrow\\ dépendance probable.

Pour le **test du \\\chi^2\\ d’indépendance**, on compare les effectifs observés \\n\_{ij}\\ aux effectifs théoriques

\\ e\_{ij}=\frac{n\_{i\cdot}n\_{\cdot j}}{n}, \\

et la statistique vaut

\\ \chi^2=\sum_i\sum_j \frac{(n\_{ij}-e\_{ij})^2}{e\_{ij}}, \qquad \text{ddl}=(p-1)(q-1). \\

## 3 2. Intégrales doubles sur \\\mathbb{R}^2\\

En probabilité continue à deux variables, toute probabilité devient une **intégrale double** sur une région du plan :

\\ P\bigl((X,Y)\in D\bigr)=\iint_D f(x,y)\\dx\\dy. \\

Les théorèmes de **Tonelli/Fubini** autorisent le calcul par intégrales successives :

\\ \iint_D f(x,y)\\dx\\dy = \int \left(\int f(x,y)\\dy\right)dx = \int \left(\int f(x,y)\\dx\right)dy. \\

Le point clé n’est pas la formule mais la **description correcte du domaine** \\D\\.

> **NOTE:**
>
> 1.  Dessiner le support ou la région demandée.
> 2.  Choisir l’ordre d’intégration le plus simple.
> 3.  Traduire le domaine par des bornes.
> 4.  Intégrer proprement.

Pièges classiques :

- oublier que les bornes intérieures dépendent souvent de la variable extérieure ;
- intégrer sur tout \\\mathbb{R}^2\\ alors que la densité est nulle hors du support ;
- ne pas vérifier la normalisation avant de calculer des probabilités.

## 4 3. Loi conjointe d’un couple continu

Un couple continu \\(X,Y)\\ est décrit par une **densité conjointe** \\f\\ telle que :

\\ f(x,y)\ge 0, \qquad \iint\_{\mathbb{R}^2} f(x,y)\\dx\\dy=1. \\

La probabilité d’une région \\D\\ est :

\\ P\bigl((X,Y)\in D\bigr)=\iint_D f(x,y)\\dx\\dy. \\

La fonction de répartition conjointe s’écrit :

\\ F(x,y)=P(X\le x,\\ Y\le y). \\

En pratique, il faut toujours commencer par identifier le **support** :

\\ S=\\(x,y)\in\mathbb{R}^2 : f(x,y)\>0\\. \\

Le support donne immédiatement :

- où il faut intégrer ;
- quelles valeurs sont impossibles ;
- si l’indépendance est plausible ou non.

## 5 4. Lois marginales, conditionnelles et indépendance

À partir de la densité conjointe, on récupère les densités marginales :

\\ f_X(x)=\int\_{\mathbb{R}} f(x,y)\\dy, \qquad f_Y(y)=\int\_{\mathbb{R}} f(x,y)\\dx. \\

Puis, si \\f_X(x)\>0\\, la densité conditionnelle vaut :

\\ f\_{Y\mid X}(y\mid x)=\frac{f(x,y)}{f_X(x)}. \\

L’idée fondamentale est la suivante :

- la **marginale** oublie l’autre variable ;
- la **conditionnelle** garde l’information fournie par l’autre variable.

Deux variables continues sont **indépendantes** si et seulement si

\\ f(x,y)=f_X(x)f_Y(y) \\

sur tout le support.

> **WARNING:**
>
> Un support rectangulaire est une condition **nécessaire**, mais pas **suffisante**, pour l’indépendance. La seule preuve fiable est la **factorisation** de la densité.

## 6 5. Covariance, corrélation et convolution

Les grandeurs numériques d’un couple se calculent à partir de la loi conjointe :

\\ E(X)=\iint\_{\mathbb{R}^2} x\\f(x,y)\\dx\\dy, \qquad E(Y)=\iint\_{\mathbb{R}^2} y\\f(x,y)\\dx\\dy, \\

\\ E(XY)=\iint\_{\mathbb{R}^2} xy\\f(x,y)\\dx\\dy. \\

La **covariance** mesure la liaison linéaire :

\\ \operatorname{Cov}(X,Y)=E(XY)-E(X)E(Y). \\

Le **coefficient de corrélation** est la version normalisée :

\\ \rho(X,Y)=\frac{\operatorname{Cov}(X,Y)}{\sigma_X\sigma_Y}. \\

À connaître absolument :

- indépendance \\\Rightarrow \operatorname{Cov}(X,Y)=0\\ ;
- la réciproque est fausse en général ;
- \\\rho\\ mesure une liaison **linéaire**, pas toute forme de dépendance.

Si \\X\\ et \\Y\\ sont indépendantes, la densité de la somme \\S=X+Y\\ est donnée par la **convolution** :

\\ f_S(t)=\int\_{\mathbb{R}} f_X(x)\\f_Y(t-x)\\dx. \\

Cette formule apparaît dès qu’on demande la loi d’une somme de deux variables continues indépendantes.

## 7 Checklist de résolution

> **IMPORTANT:**
>
> 1.  Identifier si le problème est **statistique bivarié** (tableau) ou **probabiliste continu** (densité).
> 2.  Déterminer le support ou la table conjointe.
> 3.  Vérifier les conditions de validité : somme \\=1\\ ou intégrale \\=1\\.
> 4.  Calculer les marginales.
> 5.  Si nécessaire, calculer une conditionnelle ou tester l’indépendance.
> 6.  Terminer avec la grandeur demandée : probabilité, espérance, covariance, loi d’une somme, statistique du \\\chi^2\\.

## 8 Erreurs fréquentes à éviter

- confondre **marginale** et **conditionnelle** ;
- oublier qu’une probabilité continue sur un point exact vaut \\0\\ ;
- conclure trop vite à l’indépendance parce que \\\operatorname{Cov}(X,Y)=0\\ ;
- mal décrire le domaine d’intégration ;
- utiliser la convolution sans indépendance.

## 9 Formulaire minimal à mémoriser

\\ P\bigl((X,Y)\in D\bigr)=\iint_D f(x,y)\\dx\\dy \\

\\ f_X(x)=\int\_{\mathbb{R}} f(x,y)\\dy, \qquad f_Y(y)=\int\_{\mathbb{R}} f(x,y)\\dx \\

\\ f\_{Y\mid X}(y\mid x)=\frac{f(x,y)}{f_X(x)} \\

\\ X \perp Y \iff f(x,y)=f_X(x)f_Y(y) \\

\\ \operatorname{Cov}(X,Y)=E(XY)-E(X)E(Y) \\

\\ f\_{X+Y}(t)=\int\_{\mathbb{R}} f_X(x)f_Y(t-x)\\dx \\

## Citation

BibTeX citation:

``` quarto-appendix-bibtex
@online{gilles,
  author = {Gilles, Guillaume},
  title = {Révision — {Probabilités} Et Statistiques à Deux Variables},
  url = {https://ggilles.dev/teaching/probability/revision-two-variables.html},
  langid = {en},
  abstract = {Cette fiche de révision synthétise les **cinq chapitres**
    consacrés aux phénomènes à **deux variables** dans le cours de
    probabilités et statistiques : statistiques bivariées, intégrales
    doubles, loi conjointe d’un couple continu, lois marginales et
    conditionnelles, puis couples de variables à densité (indépendance,
    covariance, convolution). Elle met l’accent sur les **formules à
    connaître**, les **méthodes de calcul** et les **pièges
    classiques**.}
}
```

For attribution, please cite this work as:

Gilles, Guillaume. n.d. “Révision — Probabilités Et Statistiques à Deux Variables.” <https://ggilles.dev/teaching/probability/revision-two-variables.html>.
