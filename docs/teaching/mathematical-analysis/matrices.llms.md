# 1 Introduction

Ce module introduit les outils matriciels nécessaires à l’optimisation des fonctions bivariées.

Objectifs du module :

- Comprendre les notions de matrices
- Introduire la matrice hessienne et le déterminant
- Étudier l’optimisation des fonctions bivariées

# 2 Partie 1 - Matrices

## 2.1 Définition

Une matrice \\A\\ est un tableau rectangulaire de nombres.

- Taille \\n \times p\\ : \\n\\ lignes et \\p\\ colonnes
- Le coefficient situe à la ligne \\i\\ et la colonne \\j\\ est note \\a\_{i,j}\\

### 2.1.1 Exemples

\\ A= \begin{pmatrix} 2 & 1 \\ 0 & 3 \\ 1 & -2 \end{pmatrix} \\

\\A\\ est une matrice de taille \\3 \times 2\\.

\\ B=\begin{pmatrix}1 & 0 & -2\end{pmatrix} \\

Matrice ligne (vecteur ligne).

\\ C= \begin{pmatrix} 0 \\ 2 \\ -4 \end{pmatrix} \\

Matrice colonne (vecteur colonne).

## 2.2 Matrices particulières

- **Matrice carree** : même nombre de lignes et de colonnes
- **Matrice diagonale** : coefficients hors diagonale nuls
- **Matrice identite** : matrice diagonale avec des 1 sur la diagonale

Exemple de matrice identite :

\\ I_2= \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} \\

## 2.3 Matrice hessienne

Pour une fonction \\f(x,y)\\, la matrice hessienne est définie par :

\\ H_f(x,y)= \begin{pmatrix} f\_{xx} & f\_{xy} \\ f\_{yx} & f\_{yy} \end{pmatrix} \\

### 2.3.1 Exemple

Soit \\f(x,y)=2x^2+3y^2\\.

\\ H_f(x,y)= \begin{pmatrix} 4 & 0 \\ 0 & 6 \end{pmatrix} \\

## 2.4 Déterminant

Pour une matrice \\2 \times 2\\ :

\\ A= \begin{pmatrix} a & b \\ c & d \end{pmatrix} \\

Le déterminant est :

\\ \det(A)=ad-bc \\

# 3 Partie 2 - Optimisation

## 3.1 Recherche des extrema locaux

### 3.1.1 Étape 1 - Points critiques

Les points critiques sont les solutions du système :

\\ \begin{cases} f_x(x,y)=0 \\ f_y(x,y)=0 \end{cases} \\

### 3.1.2 Étape 2 - Hessienne

On calcule le déterminant de la matrice hessienne \\H_f(x,y)\\.

### 3.1.3 Étape 3 - Nature du point critique

Soit \\(a,b)\\ un point critique :

- \\\det(H_f(a,b))\>0\\ et \\f\_{xx}(a,b)\>0\\ : minimum local
- \\\det(H_f(a,b))\>0\\ et \\f\_{xx}(a,b)\<0\\ : maximum local
- \\\det(H_f(a,b))\<0\\ : point selle
- \\\det(H_f(a,b))=0\\ : indétermination

## 3.2 Exemple

Soit \\f(x,y)=(x-1)^2+(y-2)^2\\.

- Point critique : \\(1,2)\\
- \\H_f=\begin{pmatrix}2 & 0 \\ 0 & 2\end{pmatrix}\\
- \\\det(H_f)=4\>0\\ et \\f\_{xx}(1,2)=2\>0\\

Donc \\f\\ admet un **minimum local** en \\(1,2)\\.

# 4 Exercices

1.  \\f(x,y)=x^4+y^4-x^2-y^2\\
2.  \\g(x,y)=\ln(1+x^2+y^2)\\
3.  Déterminer la hessienne et son déterminant pour \\h(x,y)=x^2+4xy-\frac{3}{2}y^2\\.
4.  Pour chacune des matrices suivantes, préciser le type et calculer le déterminant lorsque c’est possible :
    - \\\begin{pmatrix}1 & 0 \\ 0 & 1\end{pmatrix}\\
    - \\\begin{pmatrix}2 & 0 \\ 0 & -1\end{pmatrix}\\
    - \\\begin{pmatrix}0 & 3 & 2 \\ 2 & 1 & 0\end{pmatrix}\\

## Citation

BibTeX citation:

``` quarto-appendix-bibtex
@online{gilles,
  author = {Gilles, Guillaume},
  title = {Optimisation d’une Fonction Bivariée},
  url = {https://ggilles.dev/teaching/mathematical-analysis/matrices.html},
  langid = {en}
}
```

For attribution, please cite this work as:

Gilles, Guillaume. n.d. “Optimisation d’une Fonction Bivariée.” <https://ggilles.dev/teaching/mathematical-analysis/matrices.html>.
