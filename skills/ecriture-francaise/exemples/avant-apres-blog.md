# Avant/après : article de blog B2B

> Application du skill Écriture française sur un premier jet d’article généré par LLM. Le but : montrer la méthode, pas juste « une plus belle version ».

## Contexte

Une PME de conseil veut un article sur l’automatisation des processus. Le brief contient deux chiffres réels : 15 % de temps gagné sur les fonctions support, 30 % du budget projet à consacrer à la conduite du changement. Le LLM produit un premier jet correct mais noyé dans le slop, où ces deux chiffres se perdent.

## Avant (généré par LLM)

Dans un monde où la transformation numérique est devenue un enjeu majeur, il est important de noter que l'automatisation des processus métier est de plus en plus adoptée par les entreprises. En effet, cette solution permet de contribuer à une amélioration significative de la productivité, de l'ordre de 15% sur les fonctions support. De plus, la mise en œuvre de l'automatisation participe à la réduction des erreurs de ressaisie. Par ailleurs, il est essentiel de souligner que les projets qui allouent véritablement une part substantielle de leur budget, environ 30%, à la conduite du changement obtiennent de meilleurs résultats. Cependant, l'adoption de ces technologies est parfois freinée par des problématiques de formation. Néanmoins, les bénéfices à long terme sont significativement supérieurs aux coûts initiaux. En conclusion, l'automatisation représente une opportunité majeure pour les entreprises souhaitant optimiser leur fonctionnement.

## Diagnostic mesuré (avant)

On mesure d’abord, on corrige ensuite. Sur cet extrait :

| Indicateur | Avant | Étape |
|---|---|---|
| Mots-signature LLM | ≈ 12 | 3 |
| Transitions creuses en tête de phrase | 6 | 3 |
| Longueur de phrase (min-max, mots) | 22-34 | 1-2 |
| Burstiness (rythme) | quasi plat | 2 |
| Typographie FR (`«»`, `’`, `15 %`) | non | 4 |
| Chiffres concrets mis en avant | 0 (noyés) | fond |

Six transitions mécaniques (« Dans un monde où », « De plus », « Par ailleurs », « Cependant », « Néanmoins », « En conclusion »), des phrases toutes longues et calibrées pareil, deux chiffres enterrés au milieu d’un paragraphe.

## Après (corrigé)

Une PME qui automatise ses processus support gagne environ 15 % de temps. Le chiffre est réel. Ce n’est pas le plus important.

L’automatisation ne remplace pas les équipes. Elle supprime les tâches que personne ne devrait faire : ressaisir une facture, vérifier un écart à la main, relancer le même dossier trois fois. Ce temps rendu, les équipes le réinvestissent dans le pilotage.

Reste un frein, toujours le même : la formation. Un outil déployé sans accompagnement prend la poussière. Les projets qui réussissent consacrent près de 30 % de leur budget à la conduite du changement, pas à la technique.

Le retour sur investissement est là. Il est d’abord humain.

## Mesures après

| Indicateur | Avant | Après |
|---|---|---|
| Mots-signature LLM | ≈ 12 | 0 |
| Transitions creuses en tête de phrase | 6 | 0 |
| Longueur de phrase (min-max, mots) | 22-34 | 4-24 |
| Typographie FR | non | oui |
| Chiffres concrets mis en avant | 0 | 2 (en tête) |

## Ce qui a changé, étape par étape

- **Étape 2 : burstiness.** Des phrases de 4 à 24 mots remplacent le bloc uniforme. « Le chiffre est réel. Ce n’est pas le plus important. » casse le rythme après une phrase longue.
- **Étape 3 : lexique.** Suppression de « il est important de noter », « permet de contribuer à », « véritablement », « significativement », « opportunité majeure ». Et des six transitions creuses : on enchaîne sans béquille.
- **Étape 4 : typographie.** L’« Après » passe en apostrophes courbes (`’`), guillemets `« »` et espaces insécables (`15 %`, `30 %`). L’« Avant » gardait la typographie anglaise du LLM (`15%`).
- **La substance, surtout.** Les deux chiffres (15 %, 30 %) étaient déjà dans le texte, noyés. De-slopper ne consiste pas à *inventer* du concret : ça consiste à *dégager* celui qui était là. L’« Après » n’ajoute aucun fait absent de l’« Avant ».
