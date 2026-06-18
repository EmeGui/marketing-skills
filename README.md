# marketing-skills — des compétences marketing actionnables, pas des prompts

> Par [Nodiris](https://nodiris.ai), le stratège de contenu pour l'ère de l'IA. On aide les dirigeants de PME et ETI à être visibles là où se prennent les décisions : moteurs de recherche et modèles de langage.

**marketing-skills** est une bibliothèque ouverte de compétences marketing. Chaque skill est un bloc autonome : principe, méthode vérifiable, exemples concrets, pièges. Pas un prompt copié sur Twitter. Une méthode qu'on peut appliquer, mesurer et transmettre.

## Pourquoi ce repo

Les marketeurs collectionnent des prompts. Le problème : un prompt sans méthode ni critère de réussite ne donne pas de résultat fiable. Tu obtiens un texte, tu ne sais pas s'il est bon, tu recommences.

Un **skill**, c'est l'inverse :

- un **principe** clair (pourquoi ça marche) ;
- une **méthode** étape par étape, où chaque étape est vérifiable (tu sais quand tu as fini) ;
- des **exemples** réels (avant / après) ;
- les **pièges** qui font échouer.

Et il y a une raison de fond. Aujourd'hui, une part croissante du contenu passe par un modèle de langage. Quand tout le monde écrit avec les mêmes outils, deux choses redeviennent rares et chères : **une voix qu'on reconnaît** et **un français qu'une machine n'a pas visiblement écrit**. Les deux premiers skills attaquent exactement ça.

Ce repo rassemble des méthodes que Nodiris utilise sur le terrain, en PME et ETI. On les ouvre parce qu'une méthode ne vaut que si elle résiste à l'épreuve des autres.

## Contenu

| Skill | Ce qu'il fait |
|---|---|
| [Brand Voice](skills/brand-voice/SKILL.md) | Extraire, formaliser et rendre reproductible une voix de marque, sur une fiche d'une page. |
| [Écriture française](skills/ecriture-francaise/SKILL.md) | Rédiger en français sans slop IA : mesurer le rythme, purger le lexique signature, rétablir la typographie. |

D'autres skills suivront. On préfère deux skills aboutis à une liste de promesses.

## Comment utiliser ces skills

Trois façons, selon ton outillage :

**À la main.** Lis le `SKILL.md`, applique la méthode, coche les critères de réussite. Les références (canvas, lexique, métriques) sont des outils prêts à l'emploi.

**Avec un LLM.** Colle le contenu du `SKILL.md` en contexte de ton modèle (Claude, ChatGPT, autre), puis donne ta tâche : « Voici ma méthode de brand voice. Analyse ces 6 textes et produis la fiche. » Les skills contiennent aussi des **prompts d'injection** prêts à copier (Brand Voice étape 6, Écriture française étape 5).

**Comme skill Claude.** Chaque dossier suit le format [Agent Skill](https://code.claude.com/docs/en/skills) (frontmatter `name`, `description`, `argument-hint`). Copie le dossier dans `~/.claude/skills/` (Claude Code) ou importe-le depuis les réglages de Claude. Le nom du dossier devient la commande : appelle-la avec son argument (`/brand-voice https://exemple.com`), ou laisse le skill se déclencher quand ta demande correspond.

## Format d'un skill

Chaque skill suit la même structure :

1. **Principe** : la logique sous-jacente.
2. **Quand l'utiliser** : les déclencheurs.
3. **Méthode** : étapes vérifiables.
4. **Exemples** : avant / après, cas réels.
5. **Pièges** : les erreurs classiques.
6. **Pour aller plus loin** : références et skills connexes.

Spécification complète : [docs/skill-format.md](docs/skill-format.md).

## Contribuer

Les pull requests sont bienvenues. Avant de soumettre :

1. Vérifie que le skill n'existe pas déjà.
2. Suis le [format standard](docs/skill-format.md).
3. Fournis au moins un exemple concret.
4. Le repo est en **français**, contributions en français uniquement.

Détails dans [CONTRIBUTING.md](.github/CONTRIBUTING.md).

## Licence

MIT © Nodiris. Voir [LICENSE](LICENSE).

## À propos de Nodiris

[Nodiris](https://nodiris.ai) est le stratège de contenu pour l'ère de l'IA. On aide les dirigeants de PME et ETI à construire une présence éditoriale qui tient la route, visible autant dans les moteurs de recherche que dans les réponses des modèles de langage (GEO). Stratégie de contenu, positionnement, et pilotage par la donnée.
