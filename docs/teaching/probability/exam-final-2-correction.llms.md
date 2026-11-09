------------------------------------------------------------------------

## 1 Exercice 1 — Analyse financière bivariée (30 points)

### 1.1 Partie A — Profil investisseur et performance

**1.** *(3 pts)* **Fréquences marginales et distribution conditionnelle.**

- **Ancienneté :** 100/200 = **50 %** Junior et **50 %** Senior.
- **Performance :** Perte = 40/200 = **20 %**, Neutre = 80/200 = **40 %**, Gain = 80/200 = **40 %**.

Distribution conditionnelle de la performance pour les gérants **Juniors** :

|        |       Perte       |      Neutre       |       Gain        |
|:-------|:-----------------:|:-----------------:|:-----------------:|
| Junior | 26/100 = **26 %** | 43/100 = **43 %** | 31/100 = **31 %** |
| Senior | 14/100 = **14 %** | 37/100 = **37 %** | 49/100 = **49 %** |

Les gérants Juniors obtiennent plus souvent des pertes (26 % vs 14 %) et moins souvent des gains (31 % vs 49 %) que les Seniors, ce qui suggère un lien entre ancienneté et performance.

------------------------------------------------------------------------

**2.** *(3 pts)* **Probabilités conditionnelles et marginales.**

\\P(\text{Perte} \mid \text{Junior}) = \frac{26}{100} = \boxed{0{,}26}\\

\\P(\text{Gain}) = \frac{80}{200} = \boxed{0{,}40}\\

\\P(\text{Senior} \mid \text{Gain}) = \frac{49}{80} = \boxed{0{,}6125}\\

------------------------------------------------------------------------

**3.** *(4 pts)* **Effectifs théoriques sous l’hypothèse d’indépendance.**

Formule : \\e\_{ij} = \dfrac{(\text{total ligne}\_i)\times(\text{total colonne}\_j)}{n}\\.

|  | Perte | Neutre | Gain |
|:---|:--:|:--:|:--:|
| Junior | \\\frac{100\times40}{200}=\mathbf{20}\\ | \\\frac{100\times80}{200}=\mathbf{40}\\ | \\\frac{100\times80}{200}=\mathbf{40}\\ |
| Senior | \\\frac{100\times40}{200}=\mathbf{20}\\ | \\\frac{100\times80}{200}=\mathbf{40}\\ | \\\frac{100\times80}{200}=\mathbf{40}\\ |

Tous les effectifs théoriques sont égaux à 20 ou 40, donc **tous ≥ 5** \\\checkmark\\. Les conditions d’application du test \\\chi^2\\ sont vérifiées.

------------------------------------------------------------------------

**4.** *(4 pts)* **Statistique du test \\\chi^2\\.**

Le tableau des termes \\(o\_{ij}-e\_{ij})^2/e\_{ij}\\ :

|  | Perte | Neutre | Gain |
|:---|:--:|:--:|:--:|
| Junior | \\(26-20)^2/20 = 36/20 = 1{,}800\\ | \\(43-40)^2/40 = 9/40 = 0{,}225\\ | \\(31-40)^2/40 = 81/40 = 2{,}025\\ |
| Senior | \\(14-20)^2/20 = 36/20 = 1{,}800\\ | \\(37-40)^2/40 = 9/40 = 0{,}225\\ | \\(49-40)^2/40 = 81/40 = 2{,}025\\ |

\\T = 2\times(1{,}800 + 0{,}225 + 2{,}025) = 2\times 4{,}050 = \boxed{8{,}1}\\

Le nombre de degrés de liberté est \\(2-1)(3-1) = 2\\. Comme \\T = 8{,}1 \> 5{,}991 = \chi^2\_{2\\;\\0{,}05}\\, on **rejette \\H_0\\** au seuil 5 % : il existe un lien significatif entre le profil du gérant et la performance.

La colonne **Gain** contribue le plus (\\2\times 2{,}025 = 4{,}05\\ soit 50 % du total), indiquant que les seniors surperforment les juniors sur ce critère.

------------------------------------------------------------------------

### 1.2 Partie B — Volatilité et rendement sectoriel

**5.** *(4 pts)* **Statistiques descriptives.**

\\\bar{x} = \frac{1+2+3+4+5}{5} = \boxed{3}, \qquad \bar{y} = \frac{3+5+8+10+14}{5} = \frac{40}{5} = \boxed{8}.\\

\\S\_{xx} = \sum x_i^2 - n\bar{x}^2 = 55 - 5\times 9 = 55 - 45 = \boxed{10}.\\

\\S\_{xy} = \sum x_iy_i - n\bar{x}\bar{y} = 147 - 5\times 3\times 8 = 147 - 120 = \boxed{27}.\\

\\S\_{yy} = \sum y_i^2 - n\bar{y}^2 = 394 - 5\times 64 = 394 - 320 = \boxed{74}.\\

------------------------------------------------------------------------

**6.** *(4 pts)* **Droite de régression.**

\\\hat{b} = \frac{S\_{xy}}{S\_{xx}} = \frac{27}{10} = \boxed{2{,}7}.\\

\\\hat{a} = \bar{y} - \hat{b}\\\bar{x} = 8 - 2{,}7\times 3 = 8 - 8{,}1 = \boxed{-0{,}1}.\\

\\\boxed{\hat{y} = -0{,}1 + 2{,}7\\x}\\

**Interprétation :** chaque point de volatilité supplémentaire est associé en moyenne à une augmentation de **2,7 points de pourcentage** du rendement sectoriel.

------------------------------------------------------------------------

**7.** *(4 pts)* **Coefficient de corrélation et coefficient de détermination.**

\\r = \frac{S\_{xy}}{\sqrt{S\_{xx}\\S\_{yy}}} = \frac{27}{\sqrt{10\times 74}} = \frac{27}{\sqrt{740}} \approx \frac{27}{27{,}203} \approx \boxed{0{,}9925}.\\

\\r^2 = \frac{729}{740} \approx \boxed{0{,}985}.\\

Le coefficient de détermination \\r^2 \approx 98{,}5\\\\\\ indique que le modèle linéaire explique **98,5 %** de la variance du rendement : l’ajustement est excellent.

------------------------------------------------------------------------

**8.** *(4 pts)* **Prédiction pour \\x = 6\\\\\\.**

\\\hat{y}(6) = -0{,}1 + 2{,}7\times 6 = -0{,}1 + 16{,}2 = \boxed{16{,}1\\\\}.\\

**Discussion :** \\x = 6\\ est légèrement en dehors de l’intervalle d’observation \\\[1;5\]\\ — c’est une **extrapolation**. Le modèle reste vraisemblable à cette échelle (très proche de la plage observée), mais il faut utiliser cette prédiction avec prudence.

------------------------------------------------------------------------

## 2 Exercice 2 — Couple de variables aléatoires continues (40 points)

La densité conjointe est \\f(x,y) = 2\\ sur le domaine \\\mathcal{D} = \\0 \leq x \leq y \leq 1\\\\, triangle de sommets \\(0,0)\\, \\(0,1)\\, \\(1,1)\\, d’aire \\1/2\\.

**1.** *(2 pts)* **Normalisation.**

\\\iint\_{\mathcal{D}} 2\\dx\\dy = 2 \times \text{Aire}(\mathcal{D}) = 2 \times \frac{1}{2} = \boxed{1} \quad \checkmark\\

On peut aussi calculer directement : \\\int_0^1 \int_0^y 2\\dx\\dy = \int_0^1 2y\\dy = \bigl\[y^2\bigr\]\_0^1 = 1. \quad \checkmark\\

------------------------------------------------------------------------

**2.** *(6 pts)* **Densités marginales.**

**Pour \\X\\**, \\x\\ est fixé dans \\\[0,1\]\\ et \\y\\ varie de \\x\\ à \\1\\ : \\f_X(x) = \int_x^1 2\\dy = 2(1-x), \quad x \in \[0,1\].\\

Vérification : \\\displaystyle\int_0^1 2(1-x)\\dx = 2\bigl\[x - \tfrac{x^2}{2}\bigr\]\_0^1 = 2\times\tfrac{1}{2} = 1\\. \\\checkmark\\

**Pour \\Y\\**, \\y\\ est fixé dans \\\[0,1\]\\ et \\x\\ varie de \\0\\ à \\y\\ : \\f_Y(y) = \int_0^y 2\\dx = 2y, \quad y \in \[0,1\].\\

Vérification : \\\displaystyle\int_0^1 2y\\dy = \bigl\[y^2\bigr\]\_0^1 = 1\\. \\\checkmark\\

\\\boxed{f_X(x) = 2(1-x), \quad f_Y(y) = 2y.}\\

------------------------------------------------------------------------

**3.** *(3 pts)* **Non-indépendance.**

Si \\X\\ et \\Y\\ étaient indépendantes, on aurait \\f(x,y) = f_X(x)\\f_Y(y)\\ pour tout \\(x,y)\\.

Or pour \\(x,y) = (0{,}5,\\0{,}5) \in \mathcal{D}\\ : \\f_X(0{,}5)\\f_Y(0{,}5) = 2(1-0{,}5)\times 2\times 0{,}5 = 1\times 1 = 1 \neq 2 = f(0{,}5,\\0{,}5).\\

Donc \\X\\ et \\Y\\ **ne sont pas indépendantes**.

------------------------------------------------------------------------

**4.** *(8 pts)* **Moments et variances.**

\\\mathbb{E}\[X\] = \int_0^1 x\cdot 2(1-x)\\dx = 2\int_0^1(x - x^2)\\dx = 2\Bigl\[\frac{x^2}{2}-\frac{x^3}{3}\Bigr\]\_0^1 = 2\Bigl(\frac{1}{2}-\frac{1}{3}\Bigr) = 2\times\frac{1}{6} = \boxed{\frac{1}{3}}.\\

\\\mathbb{E}\[X^2\] = \int_0^1 x^2\cdot 2(1-x)\\dx = 2\Bigl\[\frac{x^3}{3}-\frac{x^4}{4}\Bigr\]\_0^1 = 2\Bigl(\frac{1}{3}-\frac{1}{4}\Bigr) = \frac{1}{6}.\\

\\\mathrm{Var}(X) = \mathbb{E}\[X^2\] - \bigl(\mathbb{E}\[X\]\bigr)^2 = \frac{1}{6} - \frac{1}{9} = \frac{3-2}{18} = \boxed{\frac{1}{18}}.\\

\\\mathbb{E}\[Y\] = \int_0^1 y\cdot 2y\\dy = 2\int_0^1 y^2\\dy = 2\times\frac{1}{3} = \boxed{\frac{2}{3}}.\\

\\\mathbb{E}\[Y^2\] = \int_0^1 y^2\cdot 2y\\dy = 2\int_0^1 y^3\\dy = 2\times\frac{1}{4} = \frac{1}{2}.\\

\\\mathrm{Var}(Y) = \frac{1}{2} - \frac{4}{9} = \frac{9-8}{18} = \boxed{\frac{1}{18}}.\\

------------------------------------------------------------------------

**5.** *(6 pts)* **Covariance et corrélation.**

\\\mathbb{E}\[XY\] = \int_0^1\int_0^y xy\cdot 2\\dx\\dy = 2\int_0^1 y\Bigl\[\frac{x^2}{2}\Bigr\]\_0^y\\dy = \int_0^1 y^3\\dy = \frac{1}{4}.\\

\\\mathrm{Cov}(X,Y) = \mathbb{E}\[XY\] - \mathbb{E}\[X\]\\\mathbb{E}\[Y\] = \frac{1}{4} - \frac{1}{3}\times\frac{2}{3} = \frac{1}{4} - \frac{2}{9} = \frac{9-8}{36} = \boxed{\frac{1}{36}}.\\

\\\rho(X,Y) = \frac{\mathrm{Cov}(X,Y)}{\sqrt{\mathrm{Var}(X)}\sqrt{\mathrm{Var}(Y)}} = \frac{1/36}{\sqrt{1/18}\times\sqrt{1/18}} = \frac{1/36}{1/18} = \boxed{+\frac{1}{2}}.\\

**Interprétation :** \\\rho = +1/2 \> 0\\ traduit une corrélation positive modérée entre \\X\\ et \\Y\\. Sur le domaine \\\\x \leq y\\\\, une valeur élevée de \\X\\ ne peut coexister qu’avec une valeur encore plus grande de \\Y\\, ce qui explique la tendance à évoluer dans le même sens.

------------------------------------------------------------------------

**6.** *(5 pts)* **Densité conditionnelle de \\Y\\ sachant \\X = x\\.**

Pour \\x \in (0,1)\\ fixé, \\y\\ varie dans \\\[x,1\]\\ : \\f\_{Y\mid X=x}(y) = \frac{f(x,y)}{f_X(x)} = \frac{2}{2(1-x)} = \frac{1}{1-x}, \quad y \in \[x,1\].\\

C’est la densité d’une loi uniforme sur \\\[x,1\]\\ : \\\boxed{Y \mid X = x \\\sim\\ \mathcal{U}\bigl(\[x,\\1\]\bigr).}\\

Vérification : \\\displaystyle\int_x^1 \frac{1}{1-x}\\dy = \frac{1-x}{1-x} = 1\\. \\\checkmark\\

------------------------------------------------------------------------

**7.** *(10 pts)* **Probabilités.**

**— Calcul de \\P\\\bigl(Y - X \> 1/2\bigr)\\.** En conditionnant sur \\X = x\\ et en utilisant la loi \\Y \mid X=x \sim \mathcal{U}(\[x,1\])\\ :

\\P\\\Bigl(Y - X \> \frac{1}{2}\\\Bigm\|\\X = x\Bigr) = P\\\Bigl(Y \> x + \frac{1}{2}\\\Bigm\|\\X=x\Bigr).\\

Si \\x \in \[1/2,1\]\\ : \\x + 1/2 \geq 1\\ donc cette probabilité est \\0\\.

Si \\x \in \[0,1/2)\\ : comme \\Y \sim \mathcal{U}(\[x,1\])\\, \\P\\\Bigl(Y \> x+\frac{1}{2}\\\Bigm\|\\X=x\Bigr) = \frac{1-(x+1/2)}{1-x} = \frac{1/2-x}{1-x}.\\

Par la formule des probabilités totales : \\P\\\Bigl(Y-X\>\frac{1}{2}\Bigr) = \int_0^{1/2} \frac{1/2-x}{1-x}\cdot 2(1-x)\\dx = 2\int_0^{1/2}\Bigl(\frac{1}{2}-x\Bigr)dx.\\ \\= 2\Bigl\[\frac{x}{2} - \frac{x^2}{2}\Bigr\]\_0^{1/2} = 2\Bigl(\frac{1}{4} - \frac{1}{8}\Bigr) = 2\times\frac{1}{8} = \boxed{\frac{1}{4}}.\\

**— Calcul de \\P\\\bigl(Y \> 3/4\bigr)\\.**

\\P\\\Bigl(Y \> \frac{3}{4}\Bigr) = \int\_{3/4}^1 2y\\dy = \bigl\[y^2\bigr\]\_{3/4}^1 = 1 - \frac{9}{16} = \boxed{\frac{7}{16}}.\\

**— Calcul de \\P\\\bigl(X \< 1/4 \mid Y = 3/4\bigr)\\.**

On utilise \\f\_{X\mid Y=3/4}(x) = 1/(3/4) = 4/3\\ pour \\x \in \[0,3/4\]\\ *(loi \\\mathcal{U}(\[0,3/4\])\\, admis)* :

\\P\\\Bigl(X \< \frac{1}{4}\\\Bigm\|\\Y = \frac{3}{4}\Bigr) = \int_0^{1/4} \frac{4}{3}\\dx = \frac{4}{3}\times\frac{1}{4} = \boxed{\frac{1}{3}}.\\

------------------------------------------------------------------------

## 3 Exercice 3 — Convergence et inférence statistique (30 points)

### 3.1 Partie A — Inégalités de concentration

**1.** *(2 pts)* **Inégalité de Markov.**

\\P(X \geq 15) \leq \frac{\mathbb{E}\[X\]}{15} = \frac{5}{15} = \boxed{\frac{1}{3}}.\\

------------------------------------------------------------------------

**2.** *(3 pts)* **Inégalité de Bienaymé-Tchebychev.**

Pour \\\varepsilon = 4\\ : \\\\1 \< X \< 9\\ = \\\|X - 5\| \< 4\\\\, donc \\\\\|X-5\|\geq 4\\\\ est le complémentaire.

\\P(\|X-5\| \geq 4) \leq \frac{\mathrm{Var}(X)}{4^2} = \frac{4}{16} = \frac{1}{4}.\\

Par complémentarité : \\P(1 \< X \< 9) = 1 - P(\|X-5\|\geq 4) \geq 1 - \frac{1}{4} = \boxed{\frac{3}{4}}.\\

------------------------------------------------------------------------

**3.** *(3 pts)* **Calcul exact sous \\\mathcal{N}(5,4)\\ (écart-type = 2).**

\\P(1 \< X \< 9) = P\\\Bigl(\frac{1-5}{2} \< Z \< \frac{9-5}{2}\Bigr) = P(-2 \< Z \< 2) = 2\Phi(2) - 1.\\

La table donne \\\Phi(2) = 0{,}9772\\, donc : \\P(1 \< X \< 9) = 2\times 0{,}9772 - 1 = \boxed{0{,}9544}.\\

**Commentaire :** la valeur exacte 0,9544 est bien supérieure à la borne 3/4 = 0,75 obtenue par Bienaymé-Tchebychev. L’inégalité est une borne universelle (valable pour toute loi), donc très conservative. Connaître la loi exacte permet d’obtenir une valeur bien plus précise.

------------------------------------------------------------------------

### 3.2 Partie B — Maximum de vraisemblance

**4.** *(4 pts)* **Vraisemblance et log-vraisemblance.**

Pour un échantillon \\t_1,\ldots,t_n\\ : \\L(\lambda) = \prod\_{i=1}^n \lambda e^{-\lambda t_i} = \lambda^n\\\exp\\\Bigl(-\lambda\sum\_{i=1}^n t_i\Bigr).\\

\\\ell(\lambda) = \ln L(\lambda) = n\ln\lambda - \lambda\sum\_{i=1}^n t_i = \boxed{n\ln\lambda - n\bar{t}\\\lambda}.\\

------------------------------------------------------------------------

**5.** *(4 pts)* **Estimateur du maximum de vraisemblance.**

\\\frac{d\ell}{d\lambda} = \frac{n}{\lambda} - n\bar{t} = 0 \\\Longrightarrow\\ \lambda = \frac{1}{\bar{t}}.\\

\\\frac{d^2\ell}{d\lambda^2} = -\frac{n}{\lambda^2} \< 0 \quad \text{(maximum)} \quad \checkmark\\

\\\boxed{\hat{\lambda} = \frac{1}{\bar{t}}.}\\

------------------------------------------------------------------------

**6.** *(2 pts)* **Application numérique.**

\\\hat{\lambda} = \frac{1}{3{,}0} = \boxed{\frac{1}{3} \approx 0{,}333 \text{ ms}^{-1}}.\\

L’estimation de la durée moyenne de traitement est \\1/\hat{\lambda} = \bar{t} = \mathbf{3{,}0}\\ **ms**.

------------------------------------------------------------------------

### 3.3 Partie C — Intervalle de confiance pour une moyenne

**7.** *(2 pts)* **Justification et loi de \\\bar{X}\_{64}\\.**

On dispose de \\n = 64\\ observations indépendantes. Par le **théorème central limite**, la moyenne \\\bar{X}\_n\\ suit approximativement une loi normale : \\\bar{X}\_{64} \\\overset{\text{approx}}{\sim}\\ \mathcal{N}\\\left(\mu,\\\frac{\sigma^2}{n}\right), \quad \text{avec } \frac{s}{\sqrt{n}} = \frac{24}{\sqrt{64}} = \frac{24}{8} = 3 \text{ ms}.\\

------------------------------------------------------------------------

**8.** *(3 pts)* **Intervalle de confiance à 95 %.**

\\\mu \in \left\[\bar{x} - z\_{0{,}025}\\\frac{s}{\sqrt{n}};\\\bar{x} + z\_{0{,}025}\\\frac{s}{\sqrt{n}}\right\] = \left\[210 - 1{,}96\times 3;\\210 + 1{,}96\times 3\right\].\\

\\\boxed{IC\_{95\\} = \[204{,}12\\;\\215{,}88\]\text{ ms}.}\\

------------------------------------------------------------------------

**9.** *(3 pts)* **Intervalle de confiance à 99 %.**

\\IC\_{99\\} = \left\[210 - 2{,}58\times 3;\\210 + 2{,}58\times 3\right\] = \left\[202{,}26;\\217{,}74\right\].\\

\\\boxed{IC\_{99\\} = \[202{,}26\\;\\217{,}74\]\text{ ms}.}\\

------------------------------------------------------------------------

**10.** *(4 pts)* **Effectif minimal pour une demi-largeur \\\leq 3\\ ms.**

La demi-largeur de l’IC à 95 % est \\z\_{0{,}025}\\\sigma/\sqrt{n}\\. On cherche le plus petit entier \\n\\ tel que : \\1{,}96\times\frac{24}{\sqrt{n}} \leq 3 \\\Longrightarrow\\ \sqrt{n} \geq \frac{1{,}96\times 24}{3} = \frac{47{,}04}{3} = 15{,}68.\\

\\n \geq (15{,}68)^2 = 245{,}86\ldots\\

\\\boxed{n\_{\min} = 246.}\\

------------------------------------------------------------------------

**Fin du corrigé.**

## Citation

BibTeX citation:

``` quarto-appendix-bibtex
@online{gilles,
  author = {Gilles, Guillaume},
  title = {Correction — {Examen} {Final}},
  url = {https://ggilles.dev/teaching/probability/exam-final-2-correction.html},
  langid = {en},
  abstract = {Corrigé complet de l’examen `exam-final-2`. Toutes les
    étapes de calcul sont détaillées\,; les réponses encadrées
    correspondent aux valeurs à retenir.}
}
```

For attribution, please cite this work as:

Gilles, Guillaume. n.d. “Correction — Examen Final.” <https://ggilles.dev/teaching/probability/exam-final-2-correction.html>.
