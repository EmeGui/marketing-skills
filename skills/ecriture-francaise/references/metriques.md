# Les 7 métriques du slop IA en français

> Ressource du skill [Écriture française](../SKILL.md). Ces sept mesures stylométriques séparent, en français, un texte généré par LLM d'un texte rédigé (ou réécrit) par un humain qualifié. Elles servent à l'**Étape 1 : Mesurer**.

## Pourquoi mesurer

Le slop IA n'est pas qu'une impression. On peut le compter. Mesurer avant et après une correction t'évite deux erreurs : croire que tu as corrigé alors que tu as juste déplacé le problème, et sur-corriger jusqu'à casser le rythme naturel du texte.

Tu n'as pas besoin d'un outil : sur un extrait de 300 à 500 mots, un comptage à la main (ou demandé à un LLM) suffit pour situer le texte.

## Périmètre de mesure

**À inclure** : tous les paragraphes du corps, les intros sous les titres, les réponses de FAQ rédigées.

**À exclure** : les titres, les listes à puces pures, les blocs de code, les citations entre guillemets (elles reflètent la voix d'un tiers), les URLs, les noms propres, les tableaux. Ces zones fausseraient le calcul.

## Les 7 métriques

### 1. μ longueur de phrase (mots par phrase)

Moyenne du nombre de mots par phrase. Découpe sur `. ! ?` (attention aux abréviations : `M.`, `etc.`, `cf.`).

- **Cible FR premium** : 22-28 mots.
- **Signature LLM** : ~20, avec une régularité suspecte.

### 2. CV longueur de phrase (le marqueur clé)

Coefficient de variation : écart-type ÷ moyenne des longueurs de phrase. Mesure la **burstiness**, c'est-à-dire l'irrégularité du rythme. **C'est la métrique la plus discriminante.**

- **Cible FR premium** : > 0,60.
- **Signature LLM** : < 0,45 (les phrases font toutes la même taille).

Un humain alterne sans effort une phrase de six mots et une phrase de quarante. Un modèle, livré à lui-même, lisse tout autour de la moyenne.

### 3. Ratio virgules / points

Nombre de virgules ÷ nombre de points terminaux (`.`, `!`, `?`). Mesure la richesse des incises.

- **Cible FR premium** : 1,8-2,5.
- **Signature LLM** : < 1,5 (phrases courtes, peu d'incises, peu de subordination).

### 4. Point-virgules / 1000 mots

Densité du point-virgule, une ponctuation que les LLM n'emploient quasiment jamais et qu'un rédacteur français manie pour lier deux idées sans les couper.

- **Cible FR premium** : 3-8 pour 1000 mots.
- **Signature LLM** : ≈ 0.

### 5. Mots signature LLM (% du total)

Part du texte composée des mots listés dans [lexique-llm.md](lexique-llm.md) (verbes, adjectifs, transitions, hedging, anglicismes signatures).

- **Cible FR premium** : < 0,20 %.
- **Signature LLM** : > 0,80 %.

Concrètement, sur un article de 2000 mots : **moins de 4 occurrences** au total.

### 6. Hedging / 1000 mots

Densité d'expressions d'incertitude molle (« il semble que », « dans une certaine mesure », « potentiellement »).

- **Cible FR premium** : 4-8 pour 1000 mots.
- **Signature LLM** : > 15.

Le hedging dilue le propos. Le corriger, c'est forcer le texte à prendre position ou à citer une source.

### 7. μ longueur de paragraphe (mots)

Moyenne du nombre de mots par paragraphe. Découpe sur les lignes vides, exclut titres, listes et tableaux.

- **Cible FR premium** : 120-200 mots.
- **Signature LLM** : 80-100 (le modèle hache en paragraphes de deux phrases, comme des puces déguisées).

## Lecture combinée

Un texte qui coche les 7 cibles est très difficile à attribuer à un LLM brut. Les détecteurs grand public (GPTZero, Originality, Copyleaks) reposent à 70-80 % sur les métriques **1, 2, 4 et 5** : les corriger suffit souvent à faire basculer le score vers « humain ».

Mais c'est un effet de bord, pas l'objectif. Certains détecteurs à base d'embeddings (Pangram) restent insensibles à ces métriques. On ne vise pas l'invisibilité totale, on vise un français de qualité. L'un est un combat perdu d'avance ; l'autre est utile que le texte passe ou non sous un détecteur.

## Note sur l'idempotence

Repasse ton texte corrigé une seconde fois et recompte. Si les métriques restent stables (à ± 5 %), ta première passe était saine. Si elles bougent encore beaucoup, c'est le signe d'une sur-correction : tu as forcé le texte au lieu de l'ajuster.
