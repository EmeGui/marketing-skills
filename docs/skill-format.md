# Format standard d'un skill marketing

> Spécification v1.0 : Toute contribution à `marketing-skills` doit suivre ce format.

## Objectif

Un skill est un bloc de compétence autonome et actionnable. Il ne décrit pas une théorie : il donne une méthode. Un lecteur doit pouvoir l'appliquer immédiatement après l'avoir lu.

## Structure obligatoire

Chaque skill est dans un dossier `skills/<nom-du-skill>/` et contient :

```
skills/<nom-du-skill>/
├── SKILL.md           ← obligatoire : frontmatter (name, description) + le skill
├── exemples/          ← obligatoire : au moins un exemple concret
│   └── exemple-1.md
└── references/        ← optionnel : ressources complémentaires
    └── outil.md
```

## Contenu du SKILL.md

Chaque `SKILL.md` s'ouvre sur un **frontmatter YAML** (le format Claude Agent Skill), suivi du corps en markdown.

```markdown
---
name: nom-du-skill
description: Ce que fait le skill ET quand l'utiliser. C'est ce champ qui déclenche le skill : reste précis, cite des situations concrètes, distingue-le des skills voisins. À la troisième personne, une à deux phrases.
license: MIT
---

# <Nom du skill>

> Une phrase qui résume la promesse du skill.

## Principe

Pourquoi ce skill fonctionne. La logique sous-jacente. Max 5 phrases.

## Quand l'utiliser

Liste de situations déclencheuses. Format : "Quand..." ou "Si...".

## Méthode

Étapes numérotées et actionnables. Chaque étape doit être vérifiable (le lecteur sait quand il a fini).

1. **Nom de l'étape** : ce qu'il faut faire et pourquoi. Inclure des critères de succès.
2. ...

## Exemples

Renvoyer vers les fichiers dans `exemples/`. Résumer chaque exemple en une phrase.

## Pièges

Les erreurs les plus fréquentes. Format : liste avec ❌ / ✅.

## Pour aller plus loin

- Ressources externes (articles, livres, outils)
- Skills connexes dans ce repo

---

*Dernière mise à jour : JJ/MM/AAAA*
```

### Le frontmatter en détail

- **`name`** : identique au nom du dossier, en minuscules avec tirets (`brand-voice`), sans accent ni espace. 64 caractères max.
- **`description`** : le champ le plus important. C'est lui qu'un assistant lit pour décider quand activer le skill. Dis ce que le skill fait *et* dans quelles situations l'employer, avec des déclencheurs concrets. 1024 caractères max, troisième personne.
- **`argument-hint`** : facultatif, pour un skill qui prend une entrée (une URL, un fichier). Indique l'argument attendu (`[url]`, `[fichier]`) ; le corps du skill le récupère via `$ARGUMENTS`.
- **`license`** : facultatif. `MIT` par défaut dans ce repo.

## Contraintes de style

- **Français uniquement** : pas de mélange fr/en
- **Tutoiement** : cohérent avec le ton Nodiris
- **Phrases de longueur variée** : alterner court et long (cf. le skill [Écriture française](../skills/ecriture-francaise/SKILL.md)) ; éviter le rythme uniforme qui trahit un texte généré
- **Exemples concrets** : pas de cas théoriques
- **Pas de jargon inutile** : expliquer les termes techniques la première fois

## Checklist de publication

Avant de soumettre une PR, vérifier :

- [ ] Le frontmatter contient `name` (= nom du dossier) et `description` (quoi + quand)
- [ ] Le skill a un titre clair et une promesse en une phrase
- [ ] La méthode est numérotée et chaque étape est vérifiable
- [ ] Au moins un exemple concret dans `exemples/`
- [ ] La section Pièges liste 3+ erreurs réelles
- [ ] Le français est correct (pas d'anglicismes, pas d'IA slop)
- [ ] Le skill est autonome (pas besoin de lire autre chose pour comprendre)
