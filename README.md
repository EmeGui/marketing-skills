# marketing-skills — des compétences marketing actionnables, pas des prompts

> Par [Nodiris](https://nodiris.ai) — Agence de marketing stratégique pour dirigeants de PME et ETI.

**marketing-skills** est une bibliothèque ouverte de compétences marketing structurées. Chaque skill est un bloc autonome : principe, méthode, contexte d'utilisation, exemples et pièges. Pas des prompts copiés-collés. Des patterns réutilisables.

## Pourquoi ce repo ?

Les marketeurs passent trop de temps à chercher des prompts sur Twitter ou Reddit. Le problème : un prompt sans méthode ni contexte ne donne pas de résultats fiables.

Un **skill**, c'est différent :
- Un **principe** clair (pourquoi ça marche)
- Une **méthode** étape par étape (comment l'appliquer)
- Des **exemples** concrets (à quoi ça ressemble)
- Les **pièges** à éviter (ce qui fait échouer)

Ce repo est construit par Nodiris à partir de cas réels sur le terrain PME/ETI, et ouvert à contribution.

## Contenu

| Skill | Description | Statut |
|---|---|---|
| [Brand Voice](skills/brand-voice/SKILL.md) | Extraire, formaliser et utiliser une voix de marque distinctive | ✅ |
| [Écriture française](skills/ecriture-francaise/SKILL.md) | Écrire en français sans IA slop : syntaxe, registres, anti-anglicismes | ✅ |
| Stratégie de contenu GEO | Construire une présence éditoriale visible dans les LLMs | 🔜 |
| Audit de messagerie | Diagnostiquer et repositionner un message commercial | 🔜 |
| Ancrage persona | Créer des personas acheteurs actionnables pour le contenu | 🔜 |
| Contenu d'aide à la vente | Équiper les équipes commerciales avec du contenu qui convertit | 🔜 |

## Format d'un skill

Chaque skill suit une structure standard :

1. **Principe** — la logique sous-jacente
2. **Quand l'utiliser** — les déclencheurs
3. **Méthode** — étapes concrètes
4. **Exemples** — avant/après, cas d'usage
5. **Pièges** — les erreurs classiques
6. **Pour aller plus loin** — ressources et skills connexes

Voir [docs/skill-format.md](docs/skill-format.md) pour la spécification complète.

## Contribuer

Les pull requests sont bienvenues. Avant de soumettre :

1. Vérifiez que le skill n'existe pas déjà
2. Suivez le [format standard](docs/skill-format.md)
3. Fournissez au moins un exemple concret
4. La langue du repo est le **français** — les contributions en français uniquement

## Licence

MIT © Nodiris — voir [LICENSE](LICENSE)

## À propos de Nodiris

[Nodiris](https://nodiris.ai) aide les dirigeants de PME et ETI à construire une présence éditoriale stratégique, visible dans les moteurs de recherche comme dans les LLMs. Stratégie de contenu, GEO, positionnement et pilotage par la data.
