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

Les deux skills suivent le standard ouvert [Agent Skill](https://code.claude.com/docs/en/skills) : un dossier avec un `SKILL.md` (frontmatter `name`, `description`, `argument-hint`). Tu peux donc les brancher dans Claude, ou simplement t'en servir comme méthode.

### Dans Claude Code

**Le plus simple : le marketplace, en une commande.** Ce repo est un marketplace de plugins. Tu l'ajoutes, tu installes :

```
/plugin marketplace add EmeGui/marketing-skills
/plugin install marketing-skills@nodiris
```

En pur CLI (sans ouvrir Claude Code), c'est le même geste :

```bash
claude plugin marketplace add EmeGui/marketing-skills
claude plugin install marketing-skills@nodiris
```

Les commandes apparaissent, préfixées par le nom du plugin, et acceptent un argument :

```
/marketing-skills:brand-voice https://exemple.com
/marketing-skills:ecriture-francaise mon-article.md
```

Tu mets à jour avec `/plugin marketplace update`. Claude peut aussi déclencher un skill de lui-même quand ta demande correspond à sa description.

**Si tu préfères les commandes courtes** (`/brand-voice` sans préfixe), copie plutôt les dossiers dans tes skills personnels :

```bash
mkdir -p ~/.claude/skills
git clone --depth 1 https://github.com/EmeGui/marketing-skills /tmp/ms
cp -r /tmp/ms/skills/* ~/.claude/skills/ && rm -rf /tmp/ms
```

Tu obtiens directement `/brand-voice` et `/ecriture-francaise`. Contrepartie : pas de mise à jour automatique.

### Dans Claude Cowork

Cowork (l'app desktop agentique) lit le même standard Agent Skill. Ouvre le gestionnaire de **Plugins**, ajoute le marketplace `EmeGui/marketing-skills`, installe le plugin : les skills deviennent disponibles dans tes sessions de travail, et Claude les charge quand la tâche s'y prête.

### Avec n'importe quel LLM (sans rien installer)

Pas de Claude Code sous la main ? Colle le contenu d'un `SKILL.md` en contexte de ton modèle (Claude, ChatGPT, autre) et donne ta tâche : « Voici ma méthode de brand voice, analyse ces 6 textes et produis la fiche. » Chaque skill embarque aussi un **prompt d'injection** prêt à copier (Brand Voice étape 6, Écriture française étape 5). Et rien ne t'empêche de les lire comme des méthodes : les références (canvas, lexique, métriques) sont des outils autonomes.

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
