---
name: ecriture-francaise
description: Rédiger, corriger et relire du français pour éliminer le slop IA, ce style artificiel des LLM qui écrivent le français avec un accent américain. Utiliser ce skill quand un texte français généré ou assisté par IA sonne faux, pour humaniser un contenu, mesurer sa qualité stylistique (burstiness, lexique signature, typographie), purger les anglicismes et tics de langage, ou cadrer un prompt de rédaction FR en amont. Couvre 7 métriques stylométriques, un lexique de purge et les règles de typographie française. NE PAS utiliser pour définir une voix de marque (voir le skill brand-voice).
argument-hint: "[chemin du fichier ou texte à corriger]"
license: MIT
---

# Écriture française — Rédiger en français sans slop IA

> Les modèles de langage écrivent le français avec un accent américain. Ce skill t'apprend à le mesurer, le corriger et le prévenir, sans tomber dans la chasse aux détecteurs.

## Principe

Les grands modèles sont entraînés majoritairement sur de l'anglais. Quand ils écrivent en français, ils gardent des réflexes anglo-saxons : calques, passifs en excès, connecteurs pauvres, rythme haché, vocabulaire interchangeable. Le résultat est grammaticalement correct mais stylistiquement **étranger**. On sent que ce n'est pas un francophone qui l'a écrit. C'est le **slop IA**.

Position de ce skill : **la qualité d'abord, l'indétectabilité ensuite.** Le but n'est pas de tromper un détecteur, c'est d'écrire un français qui se tient. L'effet de bord, c'est que les détecteurs grand public (GPTZero, Originality) basculent au passage. Mais si tu vises l'indétectabilité pour elle-même, tu produis du texte tortueux : tu auras un mauvais score *et* un mauvais texte.

Le slop n'est pas une impression. Il se **mesure**. Sept métriques stylométriques séparent en français un texte LLM brut d'un texte rédigé par un humain qualifié (voir [references/metriques.md](references/metriques.md)). On ne corrige pas au feeling : on mesure avant, on mesure après.

Le traitement a trois temps :
1. **Mesurer** le slop (les 7 métriques).
2. **Corriger** un texte déjà généré (rythme, lexique, typographie).
3. **Prévenir** en cadrant le prompt en amont.

## Quand l'utiliser

- Tu fais rédiger un article ou une page par un LLM et le résultat sonne faux.
- Tu relis un texte généré et tu sens que « quelque chose cloche » sans pouvoir le nommer.
- Tu veux outiller une équipe ou un assistant de rédaction pour produire du français naturel à l'échelle.
- Tu publies en français et ta crédibilité dépend de la qualité de la langue.

## Méthode

**Entrée.** Le skill s'active sur un fichier ou un texte : `/ecriture-francaise article.md`, ou colle le texte directement. Si `$ARGUMENTS` pointe un fichier, lis-le et rends la version corrigée ; sinon, traite le texte fourni.

### Étape 1 — Mesurer : les 7 marqueurs du slop

Avant de toucher au texte, calcule (ou estime) ces sept métriques. Elles te disent **où** le texte trahit la machine, pas seulement *qu'il* la trahit.

| # | Métrique | Cible FR premium | Signature LLM |
|---|---|---|---|
| 1 | μ longueur de phrase (mots) | 22-28 | ~20 (uniforme) |
| 2 | **CV longueur de phrase** (burstiness) | > 0,60 | < 0,45 (trop régulier) |
| 3 | Ratio virgules / points | 1,8-2,5 | < 1,5 |
| 4 | Point-virgules / 1000 mots | 3-8 | ≈ 0 |
| 5 | Mots signature LLM (% du total) | < 0,20 % | > 0,80 % |
| 6 | Hedging / 1000 mots | 4-8 | > 15 |
| 7 | μ longueur de paragraphe (mots) | 120-200 | 80-100 (haché) |

La métrique la plus discriminante est la **n°2, le coefficient de variation de la longueur de phrase** (la *burstiness*). Un humain alterne sans y penser des phrases de cinq mots et des phrases de quarante. Un LLM produit des phrases qui font toutes la même taille. C'est le tell le plus fort, et le plus simple à corriger.

> Détail complet du calcul de chaque métrique dans [references/metriques.md](references/metriques.md).

### Étape 2 — Casser l'uniformité (burstiness)

Objectif : faire monter le CV au-dessus de 0,60 et varier le rythme.

- **Alterne les longueurs.** Dans chaque paragraphe, glisse au moins une phrase courte (< 10 mots) et une phrase longue (> 30 mots) quand le sens le permet. Une phrase de trois mots après une longue, c'est un coup de cymbale.
- **Fusionne les phrases hachées.** Deux phrases courtes plates deviennent une phrase plus riche avec une incise, un point-virgule, une subordonnée.
- **Coupe les phrases au-delà de 45 mots.** Personne ne respire à 50 mots.
- **Injecte la ponctuation que les LLM n'utilisent pas** : le point-virgule (3 à 8 pour 1000 mots), les parenthèses (un aparté, une précision), les deux-points (annoncer, expliciter).
- **Casse les triplets mécaniques** : « X, Y et Z » répété trois paragraphes d'affilée. Varie la forme, passe-en un en prose.
- **Réintègre les fausses listes à puces** : si trois items tiennent en une phrase, écris la phrase.

### Étape 3 — Purger le lexique signature

Objectif : faire tomber les mots signature LLM sous 0,20 % du total.

Les modèles ont des tics lexicaux en français. Pris isolément, aucun de ces mots n'est interdit. C'est leur **densité** qui trahit la machine. La liste complète, avec les remplacements contextuels, est dans [references/lexique-llm.md](references/lexique-llm.md). Les familles à traiter en priorité :

- **Verbes signature** : *souligner, mettre en lumière, s'inscrire dans, permettre de, constituer, témoigner de*. Souvent supprimables : reformule en action directe.
- **Adjectifs creux** : *véritable, crucial, robuste, incontournable, stratégique* (en intensif). « Un véritable enjeu » → « un enjeu ».
- **Transitions vides** : *il est important de noter que, par ailleurs, en outre, de surcroît, en effet, force est de constater*. Supprime d'abord, reformule ensuite.
- **Hedging** (incertitude molle) : *il semble que, on peut considérer que, dans une certaine mesure, potentiellement*. Prends position, ou cite la source. Cible : 4 à 8 pour 1000 mots, contre 15+ chez un LLM brut.
- **Anglicismes calqués** : *implémenter → mettre en œuvre, adresser → traiter, impacter → peser sur, digital → numérique* (voir aussi [references/anti-anglicismes.md](references/anti-anglicismes.md)).

> Règle de doublon : ne remplace pas un mot de la purge par un autre mot de la purge. « Par ailleurs » ne devient pas « de plus » : même famille, même problème.

### Étape 4 — Rétablir la typographie française

Un texte qui se veut français mais garde la typographie anglaise se trahit en une ligne. Applique systématiquement :

- **Espaces insécables** avant `: ; ? !` et `»`, après `«`.
- **Guillemets français** `« »` partout. Jamais de `" "` droits ni de guillemets anglais `"…"`.
- **Apostrophe typographique** `'` (U+2019) au lieu de l'apostrophe droite `'`.
- **Points de suspension** `…` (un seul caractère) au lieu de `...`.
- **Majuscules** : pas de Titre Avec Une Majuscule À Chaque Mot (c'est de l'anglais). Majuscule au premier mot et aux noms propres, point.

**Le cas du tiret cadratin `—`.** C'est le signal le plus sous-estimé. Beaucoup de lecteurs francophones associent désormais le `—` au style IA et perdent confiance en le voyant, même quand son usage est typographiquement correct. La consigne :

- **Supprime les `—` du corps de texte.** Remplace par une virgule, un point, deux-points, un point-virgule, ou réécris la phrase.
- **Ne remplace jamais un `—` par un `-` simple.** Le lecteur confond visuellement les deux : double perte.
- **Réduis aussi les `-` entourés d'espaces** (`mot - mot`), ces faux cadratins. En revanche, garde intacts les mots composés (*c'est-à-dire, peut-être, au-delà*), les listes à puces et les nombres composés.

> Ce point est contre-intuitif et c'est exactement pour ça qu'il compte : tout le monde nettoie les anglicismes, presque personne ne nettoie le cadratin.

### Étape 5 — Prévenir en amont

Corriger coûte plus cher que cadrer. Injecte ces consignes **avant** la génération :

```
Écris en français naturel. Règles non négociables :
1. Varie la longueur des phrases (de 5 à 40 mots, vraiment varié).
2. Jamais de passif inutile, voix active par défaut.
3. Jamais de « De plus », « En outre », « Par ailleurs », « Cependant » en tête de phrase.
4. Pas d'anglicismes : « mettre en œuvre » pas « implémenter », « numérique » pas « digital ».
5. Pas de tiret cadratin (—). Ponctue avec virgule, deux-points, point-virgule, parenthèses.
6. Chaque paragraphe avance une idée neuve, jamais un résumé du précédent.
7. Prends position : ne dis pas « certains pensent X, d'autres Y » sans trancher.
8. Supprime les évidences : si un lecteur de 15 ans le sait déjà, ne l'écris pas.
9. Guillemets français « » et apostrophes courbes.
```

## Exemples

- [Avant/après : article de blog B2B](exemples/avant-apres-blog.md) : un article généré puis dé-sloppé, avec le détail des corrections.
- [Avant/après : page « À propos »](exemples/avant-apres-a-propos.md) : une page institutionnelle remise sur ses pieds.

## Pièges

- ❌ **Viser le détecteur, pas le lecteur** : si tu optimises pour GPTZero, tu écris pour une machine et ça se voit. Vise la qualité ; le score suit.
- ❌ **Corriger mécaniquement** : appliquer la checklist sans relire à voix haute produit un texte propre mais sans souffle. La langue se vérifie à l'oreille.
- ❌ **Tout uniformiser** : la variété des longueurs *est* ce qui rend le texte humain. Une correction trop agressive aplatit le rythme et recrée du slop, en pire.
- ❌ **Supprimer tous les passifs / tous les adverbes** : certains sont légitimes. Le test : retire-le. Si la phrase ne perd rien, il était inutile. Sinon, garde-le.
- ❌ **Confondre slop IA et mauvais français** : un humain peut mal écrire. Le slop est spécifique : un français correct mais artificiel. Ce sont deux diagnostics différents.
- ❌ **Oublier l'idempotence** : repasse ton texte corrigé une seconde fois. Si tes métriques bougent encore beaucoup, c'est que la première passe a sur-corrigé.

## Pour aller plus loin

- [Lexique signature LLM](references/lexique-llm.md) : la liste complète des mots à purger, avec remplacements.
- [Les 7 métriques](references/metriques.md) : définitions et méthode de calcul.
- [Anti-anglicismes](references/anti-anglicismes.md) : table de remplacement pour le marketing B2B.
- [Brand Voice](../brand-voice/SKILL.md) : le skill complémentaire. Fixe d'abord la voix, puis nettoie le slop qui la pollue.


---

*Dernière mise à jour : 18/06/2026*
