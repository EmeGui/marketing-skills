# Écriture française — Rédiger en français sans IA slop

> Les LLMs écrivent le français avec un accent américain. Ce skill t'apprend à le détecter, le corriger et le prévenir.

## Principe

Les grands modèles de langage sont entraînés majoritairement sur du texte anglais. Quand ils écrivent en français, ils conservent des réflexes syntaxiques anglais : calques, passifs abusifs, connecteurs pauvres, rythme haché, vocabulaire interchangeable.

Résultat : un texte grammaticalement correct mais stylistiquement **étranger**. On sent que ce n'est pas un humain francophone qui l'a écrit. C'est ce qu'on appelle le **IA slop**.

Ce skill couvre les trois étapes du traitement :
1. **Détecter** les marqueurs du IA slop
2. **Corriger** un texte déjà généré
3. **Prévenir** en donnant les bonnes instructions au LLM en amont

## Quand l'utiliser

- Tu fais rédiger un article ou une page par un LLM et le résultat sonne faux
- Tu relis un texte généré et tu as l'impression que "quelque chose cloche" sans pouvoir dire quoi
- Tu veux créer un assistant de rédaction qui produit du français naturel
- Tu formes une équipe à la rédaction assistée par IA
- Tu publies du contenu en français et ta crédibilité dépend de la qualité de la langue

## Méthode

### Étape 1 : Détecter le IA slop

Apprends à repérer les **20 marqueurs** du français artificiel. Voici les plus fréquents :

#### Syntaxe et grammaire

1. **Passif abusif** — "Cette solution est adoptée par les entreprises" → "Les entreprises adoptent cette solution"
2. **Nominalisation excessive** — "La mise en œuvre de l'optimisation" → "Optimiser"
3. **Calques de l'anglais** — "adresser un problème" (to address) → "traiter un problème"
4. **Gérondifs mal placés** — "En utilisant cette méthode, les résultats sont améliorés" (dangling modifier)

#### Connecteurs et transitions

5. **"De plus" / "En outre" / "Par ailleurs"** en début de phrase — systématiques, mécaniques
6. **"Cependant" / "Néanmoins" / "Toutefois"** — utilisés comme des balises, pas comme des nuances
7. **"Il est important de noter que"** — périphrase vide, toujours supprimable
8. **"Dans le monde de" / "À l'ère du" / "Dans le paysage de"** — clichés d'introduction

#### Vocabulaire

9. **Anglicismes non nécessaires** — "implémenter", "digital", "scalable", "disruption", "solution"
10. **Verbes faibles** — "permettre de", "contribuer à", "participer à" (au lieu du verbe direct)
11. **Adverbes gonflants** — "véritablement", "réellement", "particulièrement", "significativement"
12. **Superlatifs vides** — "meilleur", "leader", "excellence", "innovant"

#### Rythme et structure

13. **Phrases à 3 étages** — sujet, relative, complétive, comme en anglais
14. **Paragraphes de 2 phrases** — le LLM segmente comme un bullet-point déguisé
15. **Ouverture en "Dans un monde où..."** — le cliché absolu du texte généré
16. **Conclusion en "En conclusion..."** — redondant, scolaire

#### Contenu

17. **Listes sans priorisation** — "X, Y et Z" sans dire lequel importe le plus
18. **Absence de point de vue** — le texte couvre toutes les opinions sans en choisir une
19. **Énumérations à 3 éléments** — "les entreprises, les organisations et les institutions"
20. **Définition d'évidences** — "Le marketing, qui consiste à promouvoir des produits..."

### Étape 2 : Corriger un texte existant

Quand tu obtiens un texte d'un LLM, passe-le au crible de cette checklist :

- [ ] Remplacer tous les passifs évitables par des actifs
- [ ] Supprimer "De plus", "En outre", "Par ailleurs" — réécrire la transition
- [ ] Traduire les anglicismes (voir [liste de référence](references/anti-anglicismes.md))
- [ ] Raccourcir les phrases de plus de 30 mots
- [ ] Supprimer chaque adverbe en "-ment" et vérifier s'il manque
- [ ] Remplacer "permettre de" + verbe par le verbe directement
- [ ] Supprimer les définitions d'évidences
- [ ] Vérifier que le texte prend position sur au moins un point

Le prompt de post-édition :

```
Réécris ce texte en français naturel. Règles :
- Supprime tous les passifs inutiles (voix active partout où c'est possible)
- Remplace "permettre de", "contribuer à", "participer à" par le verbe direct
- Supprime les adverbes en -ment sauf s'ils sont indispensables
- Remplace les anglicismes par leur équivalent français
- Fais des phrases de longueur variée (8 à 25 mots)
- Si une phrase dit la même chose que la précédente, supprime-la
- Si une phrase définit une évidence, supprime-la
- Le texte doit prendre position, pas énumérer des options

Texte à réécrire :
---
[COLLE TON TEXTE]
---
```

### Étape 3 : Prévenir le IA slop

Injecte ces instructions dans ton prompt de rédaction **avant** la génération :

```
Écris en français naturel. Règles non négociables :
1. Jamais de passif sauf intention délibérée
2. Jamais de "De plus", "En outre", "Par ailleurs", "Cependant" en tête de phrase
3. Pas d'anglicismes : "mettre en œuvre" pas "implémenter", "numérique" pas "digital"
4. Varier la longueur des phrases (8-25 mots)
5. Varier les constructions (ne pas commencer 3 phrases de suite par le sujet)
6. Chaque paragraphe avance une idée, pas un résumé de la précédente
7. Prendre position : ne pas dire "certains pensent X, d'autres Y" sans trancher
8. Supprimer les évidences : si un lecteur de 15 ans le sait, ne pas le dire
```

## Exemples

- [Avant/après : article de blog B2B](exemples/avant-apres-blog.md) — un article généré par LLM puis corrigé
- [Avant/après : page "À propos"](exemples/avant-apres-a-propos.md) — une page institutionnelle dé-sloppée

## Pièges

- ❌ **Corriger mécaniquement** — appliquer la checklist sans réfléchir produit un texte haché. Relire à voix haute.
- ❌ **Supprimer tous les passifs** — le passif a des usages légitimes (quand l'agent est inconnu ou moins important que le patient). La règle est "évitable", pas "interdit".
- ❌ **Remplacer tous les adverbes** — certains sont utiles. Le test : supprimer l'adverbe. Si la phrase ne perd rien, il était inutile.
- ❌ **Confondre IA slop et mauvais français** — un humain peut écrire du mauvais français. Le IA slop est spécifique : c'est un français grammaticalement correct mais stylistiquement artificiel.
- ❌ **Uniformiser le style** — varier la longueur des phrases et les constructions est précisément ce qui rend le texte naturel. Une correction trop agressive peut créer l'effet inverse.
- ❌ **Oublier le registre** — le français d'un rapport technique et celui d'un post LinkedIn n'ont pas les mêmes règles. Adapter la checklist.

## Pour aller plus loin

- [Anti-anglicismes — liste de référence](references/anti-anglicismes.md)
- [Brand Voice](skills/brand-voice/SKILL.md) — skill complémentaire pour capturer une voix distinctive
- *Le français est à nous* — Laélia Véron et Maria Candea (pour comprendre les rapports de force dans la langue)
- Dire, ne pas dire — Académie française (pour les néologismes et anglicismes)

---

*Dernière mise à jour : 17/06/2026*
