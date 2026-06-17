# Brand Voice — Extraire, formaliser et utiliser une voix de marque distinctive

> Une marque qui sonne comme tout le monde est une marque qu'on oublie. Ce skill t'aide à capturer la voix unique d'une marque et à l'injecter dans tous tes contenus.

## Principe

La plupart des "chartes éditoriales" sont des PDF de 20 pages que personne ne lit. Une voix de marque efficace tient sur une fiche A4 avec 4 à 5 curseurs actionnables. L'objectif n'est pas de tout documenter, mais de rendre la voix **reproductible** : n'importe qui (ou n'importe quel LLM) doit pouvoir écrire dans cette voix après avoir lu la fiche.

Ce qui fait une voix, ce n'est pas une liste d'adjectifs ("moderne", "dynamique", "humain"). C'est une combinaison mesurable de :

- **Registre** (familier → soutenu)
- **Densité** (phrases courtes → longues)
- **Posture** (expert neutre → provocateur)
- **Vocabulaire** (mots interdits, mots signatures)
- **Rythme** (construction de phrase typique)

## Quand l'utiliser

- Tu crées une nouvelle marque et tu veux définir sa voix avant d'écrire
- Ta marque existe mais chaque rédacteur écrit différemment
- Tu utilises un LLM pour rédiger et le résultat est fade ou générique
- Tu refondes ton site et tu veux une cohérence éditoriale
- Un client te demande "peux-tu écrire comme nous ?"

## Méthode

### Étape 1 : Collecter les échantillons

Rassemble 5 à 10 contenus représentatifs de la marque :

- Pages clés du site (accueil, about, offres)
- 3 à 5 articles de blog ou posts LinkedIn
- 2 à 3 emails ou newsletters
- Si possible, des transcripts vidéo ou audio (la voix parlée est plus authentique)

**Critère de succès** : tu as au moins 5 textes, totalisant 3000+ mots.

### Étape 2 : Extraire les patterns

Pour chaque texte, relève :

1. **Longueur moyenne des phrases** — courte (<15 mots), moyenne (15-25), longue (>25)
2. **Pronoms dominants** — "nous" (collectif), "je" (personnel), "vous" (conversationnel), absent (impersonnel)
3. **Temps verbaux** — présent (direct), futur (projection), passé (récit)
4. **Connecteurs** — "mais" (contraste), "donc" (logique), "et" (accumulation), rares (juxtaposition)
5. **Mots signatures** — les 5-10 mots ou expressions qui reviennent systématiquement
6. **Ponctuation** — points d'exclamation (énergie), tirets (digression), deux-points (explication)

**Outil** : colle chaque texte dans le prompt d'analyse (voir [references/canvas-extraction.md](references/canvas-extraction.md)).

### Étape 3 : Positionner les curseurs

Place 5 curseurs sur une échelle de 1 à 5 :

| Curseur | 1 | 3 | 5 |
|---|---|---|---|
| **Registre** | Très familier | Professionnel | Soutenu/technique |
| **Densité** | Phrases < 12 mots | 15-20 mots | > 25 mots |
| **Posture** | Camarade | Expert neutre | Provocateur |
| **Énergie** | Calme/posé | Engagé | Urgent/passionné |
| **Abstraction** | Très concret | Mixte | Conceptuel |

Exemple pour une marque B2B tech :
> Registre 3 • Densité 3 • Posture 3 • Énergie 2 • Abstraction 3

### Étape 4 : Formaliser le lexique

Crée deux listes :

- **Mots interdits** (5-10) — jargon, anglicismes, tics de langage que la marque rejette
- **Mots signatures** (5-10) — expressions que la marque utilise systématiquement

Exemple :
> ✅ "pilotage", "dirigeant", "décision", "résultat mesurable", "terrain"
> ❌ "disruption", "révolutionner", "booster", "next-gen", "scalable"

### Étape 5 : Créer le prompt d'injection

Rédige un paragraphe de 4-5 phrases qui capture l'essence de la voix, à coller dans tes prompts LLM :

```
Écris avec la voix suivante :
Tu es un expert pragmatique qui parle à des dirigeants. Ton ton est direct,
jamais condescendant. Tu expliques des choses complexes simplement, sans les
simplifier. Tu n'utilises jamais de jargon anglais ni de superlatifs creux.
Chaque phrase apporte une information ou une question. Tu tutoies ton lecteur.
```

### Étape 6 : Tester sur un contenu réel

Prends un paragraphe écrit par la marque, et demande à un LLM de réécrire le même message avec le prompt d'injection. Compare. Si la voix est reconnaissable, le skill est maîtrisé.

## Exemples

- [Marque fictive B2B : Constructys](exemples/constructys.md) — extraction complète d'une voix B2B industrielle

## Pièges

- ❌ **Trop de curseurs** — au-delà de 6 paramètres, personne ne les utilise. Reste sur 4-5.
- ❌ **Confondre ton et voix** — le ton change selon le contexte (email vs billet de blog), la voix reste.
- ❌ **Décrire au lieu de prescrire** — "notre marque est authentique" n'aide personne à écrire. "Nos phrases font moins de 20 mots" oui.
- ❌ **Oublier le lexique négatif** — les mots qu'on n'utilise pas définissent la voix autant que ceux qu'on utilise.
- ❌ **Tester uniquement avec des humains** — si la voix n'est pas reproductible par un LLM avec un bon prompt, elle n'est pas assez formalisée.
- ❌ **Figer la voix** — une voix de marque évolue. Précise une date de dernière mise à jour et révise tous les 6 mois.

## Pour aller plus loin

- [Canvas d'extraction de voix](references/canvas-extraction.md) — le prompt complet pour analyser un corpus
- [Écriture française](skills/ecriture-francaise/SKILL.md) — skill complémentaire pour éviter le IA slop en français
- *The Brand Gap* — Marty Neumeier (référence fondatrice sur l'identité de marque)
- *Letting Go of the Words* — Janice Redish (écrire pour le web sans perdre sa voix)

---

*Dernière mise à jour : 17/06/2026*
