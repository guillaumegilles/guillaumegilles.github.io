Une entreprise de streaming musical envisage de lancer une offre premium au prix mensuel \\p\\ (en euros, €).

Les analyses marketing prévoient que la demande mensuelle (en milliers d’abonnés) suit la fonction :

\\ Q(p) = 600 - 20p \\

Et le coût total mensuel (en milliers d’euros) est donné par :

\\ C(p) = 1000 + 5Q(p) \\

Le chiffre d’affaires est :

\\ R(p) = p \times Q(p) \\

Finalement, le profit est :

\\ \pi(p) = R(p) - C(p) \\

## 1 Énoncé

Une entreprise de streaming musical lance une offre premium au prix mensuel \\p\\ (en EUR).

La demande mensuelle (en milliers d’abonnés) est :

\\ Q(p)=600-20p \\

Le coût total mensuel (en milliers d’EUR) est :

\\ C(p)=1000+5Q(p) \\

Le chiffre d’affaires est :

\\ R(p)=pQ(p) \\

Le profit est :

\\ \pi(p)=R(p)-C(p) \\

------------------------------------------------------------------------

## 2 Correction - Partie 1 (chiffre d’affaires)

### 2.1 1) Expression de \\R(p)\\

\\ R(p)=p(600-20p)=600p-20p^2 \\

### 2.2 2) Dérivée de \\R\\

\\ R'(p)=600-40p \\

### 2.3 3) Prix optimal pour maximiser \\R\\

\\ R'(p)=0 \Longleftrightarrow 600-40p=0 \Longleftrightarrow p_0=15 \\

\\ R''(p)=-40\<0 \\

Donc \\p_0=15\\ donne un maximum de chiffre d’affaires.

### 2.4 4) Valeurs de \\R(10)\\, \\R(15)\\, \\R(20)\\

\\ R(10)=4000,\quad R(15)=4500,\quad R(20)=4000 \\

Le CA augmente jusqu’a \\p=15\\ puis diminue.

### 2.5 5) Élasticité de \\R\\ en \\p=10\\

\\ E_R(p)=R'(p)\frac{p}{R(p)} \\

Pour \\p=10\\ :

\\ E_R(10)=\left(600-40\cdot 10\right)\frac{10}{4000}=0.5 \\

Donc le CA est inélastique à ce point.

------------------------------------------------------------------------

## 3 Correction - Partie 2 (profit)

### 3.1 1) Expression de \\\pi(p)\\

\\ \pi(p)=(600p-20p^2)-\left(1000+5(600-20p)\right) \\

\\ \pi(p)=-20p^2+700p-4000 \\

### 3.2 2) Resolution de \\\pi'(p)=0\\

\\ \pi'(p)=-40p+700 \\

\\ \pi'(p)=0 \Longleftrightarrow p_0=17.5 \\

### 3.3 3) Nature du point critique

\\ \pi''(p)=-40\<0 \\

Donc \\p_0=17.5\\ est un maximum.

### 3.4 4) Profit maximal

\\ \pi(17.5)=2125 \\

### 3.5 5) Si le prix depasse le prix optimal

Le profit diminue : la fonction est une parabole concave (coefficient de \\p^2\\ négatif) et son sommet est atteint en \\p_0=17.5\\.

## Citation

BibTeX citation:

``` quarto-appendix-bibtex
@online{gilles,
  author = {Gilles, Guillaume},
  title = {Examen Intermédiaire},
  url = {https://ggilles.dev/teaching/mathematical-analysis/revision-midterm.html},
  langid = {en}
}
```

For attribution, please cite this work as:

Gilles, Guillaume. n.d. “Examen Intermédiaire.” <https://ggilles.dev/teaching/mathematical-analysis/revision-midterm.html>.
