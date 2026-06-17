# Format standard d'un skill marketing

> Spécification v1.0 — Toute contribution à `marketing-skills` doit suivre ce format.

## Objectif

Un skill est un bloc de compétence autonome et actionnable. Il ne décrit pas une théorie : il donne une méthode. Un lecteur doit pouvoir l'appliquer immédiatement après l'avoir lu.

## Structure obligatoire

Chaque skill est dans un dossier `skills/<nom-du-skill>/` et contient :

```
skills/<nom-du-skill>/
├── SKILL.md           ← obligatoire : le skill lui-même
├── exemples/          ← obligatoire : au moins un exemple concret
│   └── exemple-1.md
└── references/        ← optionnel : ressources complémentaires
    └── outil.md
```

## Contenu du SKILL.md

```markdown
# <Nom du skill>

> Une phrase qui résume la promesse du skill.

## Principe

Pourquoi ce skill fonctionne. La logique sous-jacente. Max 5 phrases.

## Quand l'utiliser

Liste de situations déclencheuses. Format : "Quand..." ou "Si...".

## Méthode

Étapes numérotées et actionnables. Chaque étape doit être vérifiable (le lecteur sait quand il a fini).

1. **Nom de l'étape** — ce qu'il faut faire et pourquoi. Inclure des critères de succès.
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

## Contraintes de style

- **Français uniquement** — pas de mélange fr/en
- **Tutoiement** — cohérent avec le ton Nodiris
- **Phrases courtes** — max 25 mots
- **Exemples concrets** — pas de cas théoriques
- **Pas de jargon inutile** — expliquer les termes techniques la première fois

## Checklist de publication

Avant de soumettre une PR, vérifier :

- [ ] Le skill a un titre clair et une promesse en une phrase
- [ ] La méthode est numérotée et chaque étape est vérifiable
- [ ] Au moins un exemple concret dans `exemples/`
- [ ] La section Pièges liste 3+ erreurs réelles
- [ ] Le français est correct (pas d'anglicismes, pas d'IA slop)
- [ ] Le skill est autonome (pas besoin de lire autre chose pour comprendre)
