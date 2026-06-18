---
name: brand-voice
description: Extraire, formaliser et rendre reproductible la voix d'une marque sur une fiche d'une page, à partir de l'URL de son site ou d'un corpus de textes. Utiliser ce skill quand l'utilisateur veut définir, documenter ou analyser un ton de voix, bâtir une charte éditoriale actionnable, comprendre « comment écrit telle marque », unifier le style de plusieurs rédacteurs, ou rendre une voix reproductible par un LLM. Couvre la découverte du corpus (sitemap, pages clés), l'analyse sur 8 dimensions, les curseurs, le lexique signature et le test de reproductibilité. NE PAS utiliser pour corriger le style d'un texte déjà rédigé (voir le skill ecriture-francaise).
argument-hint: "[url ou nom de marque]"
license: MIT
---

# Brand Voice — Extraire, formaliser et rendre reproductible une voix de marque

> Une marque qui sonne comme tout le monde est une marque qu'on oublie. Ce skill capture la voix d'une marque sur une fiche d'une page, assez précise pour qu'un humain ou un modèle écrive dans cette voix sans la trahir.

## Principe

La plupart des chartes éditoriales sont des PDF de vingt pages que personne ne lit. Une voix de marque utile tient sur une page et reste **prescriptive** : elle ne décrit pas la marque, elle dit comment écrire.

Le vrai test a changé. Aujourd'hui, une grande partie de tes contenus passe par un modèle de langage à un moment ou un autre. Une voix qu'un LLM ne sait pas reproduire est une voix qui se dissout dès que tu passes à l'échelle. Donc le critère final n'est pas « est-ce que ça nous ressemble ? », c'est : **est-ce qu'on peut confier cette fiche à n'importe qui, humain ou machine, et obtenir un texte reconnaissable ?**

Ce qui rend une voix reproductible, ce n'est pas une liste d'adjectifs (« moderne », « humain », « dynamique »). C'est une combinaison **mesurable** et **délimitée** :

- ce que la marque fait (registre, rythme, posture, lexique) ;
- ce que la marque ne fait **jamais** : la frontière définit la voix autant que le centre.

## Quand l'utiliser

- Tu lances une marque et tu veux fixer sa voix avant d'écrire la première ligne.
- Ta marque existe, mais chaque rédacteur écrit dans son coin et l'ensemble part dans tous les sens.
- Tu fais rédiger par un LLM et le résultat est fade, générique, interchangeable.
- Tu refonds ton site et tu cherches une cohérence éditoriale d'une page à l'autre.
- Un client te demande « peux-tu écrire comme nous ? » et tu n'as rien de formalisé à lui montrer.

## Méthode

### Étape 0 — Point de départ : une URL ou un nom de marque

Le skill s'active avec une entrée (`$ARGUMENTS`) : `/brand-voice https://exemple.com` ou `/brand-voice "Nom de marque"`.

- Une **URL** : c'est ton point d'entrée direct.
- Un **nom de marque** : trouve d'abord le site officiel (recherche web), et confirme-le avant d'aller plus loin.
- Ni l'un ni l'autre : demande l'URL. Sans corpus, pas d'analyse.

### Étape 1 — Découvrir le corpus (sans le réclamer)

Ne demande pas au client de t'envoyer ses textes : va les chercher. La cible reste 5 à 10 contenus **variés**, 3 000 mots cumulés. La voix se révèle dans le contraste entre une page institutionnelle et un post écrit à chaud.

1. **Cartographie le site.** Récupère le `sitemap.xml` (à la racine, ou listé dans `/robots.txt` sous `Sitemap:`) : il liste les pages publiées. Pas de sitemap exploitable ? Replie-toi sur les liens de la navigation et du pied de page de l'accueil.
2. **Priorise les pages qui portent la voix**, dans cet ordre :
   - l'accueil ;
   - la page « à propos » / « qui sommes-nous » / « notre vision » ;
   - l'offre, les services ou le produit principal ;
   - les 3 à 5 articles de blog les plus récents (le ton y est le plus libre) ;
   - à défaut de blog, 2 pages cas client ou réalisations.
3. **Récupère et nettoie.** Charge chaque page, garde le texte éditorial, jette le boilerplate (menu, cookies, mentions légales). Compte les mots récoltés.
4. **Contrôle le volume.** Moins de 3 000 mots exploitables, ou site qui ne rend presque rien (one-pager, rendu JS vide) : continue, mais baisse la confiance de la fiche finale et dis pourquoi.

> **Sans accès web** (tu appliques la méthode à la main, ou ton outil ne navigue pas) : demande au client 5 à 10 contenus représentatifs et variés, puis enchaîne. Un seul texte ne suffit jamais : le modèle surinterprète alors des détails non signifiants. Il faut du volume pour distinguer le pattern du hasard.

### Étape 2 — Analyser sur 8 dimensions (avec triangulation)

Passe le corpus au crible des 8 dimensions ci-dessous. **Règle de triangulation** : ne valide une observation que si elle apparaît dans **au moins 2 textes différents**. Une tournure vue une seule fois est un accident, pas une signature.

| # | Dimension | Ce que tu cherches |
|---|---|---|
| D1 | **Personnalité** | 3 à 5 adjectifs qui ressortent + l'archétype dominant (voir plus bas) |
| D2 | **Registre** | Familier / courant / soutenu. Tutoiement, vouvoiement ou impersonnel. Distance : autorité distante, expert accessible, pair-à-pair |
| D3 | **Posture rhétorique** | Enseigne / partage / inspire / accompagne / provoque. Et la structure : réponse directe d'abord (BLUF), construction progressive, ou narratif |
| D4 | **Syntaxe** | Longueur de phrase dominante, voix active ou passive, pronom narratif (nous / on / vous / impersonnel), densité des paragraphes |
| D5 | **Tonalité émotionnelle** | Chaleur (froide, neutre, chaleureuse), humour (absent, subtil, assumé), rapport à la prudence (assertif ou prudent) |
| D6 | **Lexique signature** | Les 5 à 10 mots ou expressions qui reviennent et qui ne sont pas génériques. Les 2-3 champs lexicaux dominants |
| D7 | **Rapport à la preuve** | Affirmation pure, chiffres et études, anecdotes clients, ou mix. À quelle fréquence la marque prouve ce qu'elle avance |
| D8 | **Ce que la marque ne fait JAMAIS** | Mots hors-ton, constructions bannies, sujets évités, rapport aux concurrents et au prix |

**Les archétypes (D1)** : choisis-en un, pas trois :

- **L'expert qui enseigne** : pédagogie descendante, autorité tranquille.
- **Le guide qui accompagne** : se met à côté du lecteur, pas au-dessus.
- **Le pair qui partage** : « voilà ce qu'on a appris », horizontal.
- **Le challenger qui provoque** : remet en cause le consensus.
- **Le pionnier qui trace la voie** : projette une vision, ouvre un chemin.

**D8 est la dimension la plus importante.** Ce qu'une marque refuse de dire la définit mieux que ce qu'elle dit. Si le blog existe, repère ce qu'elle évite **systématiquement** : c'est là qu'est la signature.

### Étape 3 — Positionner les curseurs

Traduis les dimensions qualitatives en 5 curseurs mesurables, de 1 à 5. C'est ce qui rend la voix opposable et vérifiable.

| Curseur | 1 | 3 | 5 |
|---|---|---|---|
| **Registre** | Très familier | Professionnel | Soutenu / technique |
| **Densité** | Phrases < 12 mots | 15-20 mots | > 25 mots |
| **Posture** | Camarade | Expert neutre | Provocateur |
| **Énergie** | Calme, posé | Engagé | Urgent, passionné |
| **Abstraction** | Très concret | Mixte | Conceptuel |

Exemple, marque B2B industrielle :
> Registre 4 • Densité 3 • Posture 3 • Énergie 2 • Abstraction 3

### Étape 4 — Formaliser le lexique

Trois listes, courtes et tranchées :

- **Mots signatures** (5-10) : les expressions que la marque utilise et que tu dois replacer quand le sujet s'y prête.
- **Mots interdits** (5-10) : jargon, anglicismes, superlatifs creux que la marque rejette.
- **Postures interdites** (2-3) : pas des mots mais des attitudes, comme « ne jamais s'auto-proclamer leader » ou « ne jamais nommer un concurrent ».

Exemple :
> ✅ « pilotage », « dirigeant », « résultat mesurable », « terrain », « filière »
> ❌ « disruption », « révolutionner », « booster », « scalable », « solution » (trop vague)
> 🚫 Ne jamais utiliser de superlatif auto-référentiel. Ne jamais ouvrir sur « Dans un monde où… ».

### Étape 5 — Écrire la fiche de voix

Réunis tout sur **une page**. Pas deux. Si ça déborde, c'est que tu décris au lieu de prescrire.

```markdown
# Voix de marque — [Nom]
*Mise à jour : [date] • Confiance : [faible / moyenne / élevée]*

## En une phrase
[Marque] parle comme un [archétype] qui [posture] à [cible].

## Curseurs
Registre [n] • Densité [n] • Posture [n] • Énergie [n] • Abstraction [n]

## Règles d'écriture
- Pronom : [nous / on / vous / impersonnel], cohérent partout
- Phrases : [courtes / mixtes / longues] : [consigne précise]
- Ouverture : [comment on commence un texte : jamais un cliché]
- Preuve : [chiffrer / citer / illustrer / affirmer]

## Lexique
Signatures : [liste]
Interdits : [liste]
Postures interdites : [liste]

## Ce qu'on ne fait jamais
[3 à 5 lignes : la frontière de la voix]
```

Le champ **Confiance** est honnête : si ton corpus est mince ou si le site est pauvre en texte éditorial, écris « faible » et note ce qui manque. Une fiche qui surinterprète est pire qu'une fiche qui assume ses trous.

### Étape 6 — Le test de reproductibilité

C'est l'étape que tout le monde saute, et c'est la seule qui prouve que la fiche marche.

1. Rédige un **prompt d'injection** : 4 à 5 phrases qui condensent la fiche, à coller en tête de n'importe quel prompt de rédaction.

```
Écris avec la voix suivante. Tu es un expert pragmatique qui parle à des
dirigeants. Ton direct, jamais condescendant. Tu expliques le complexe sans
le simplifier. Aucun jargon anglais, aucun superlatif creux. Phrases de
longueur variée. Tu emploies « nous » et tu vouvoies le lecteur. Tu n'ouvres
jamais sur « Dans un monde où ».
```

2. Prends un paragraphe réellement écrit par la marque. Cache-le. Demande à un modèle de rédiger le même message avec ton prompt d'injection.
3. Compare. **Si la voix est reconnaissable, la fiche est opérationnelle.** Sinon, la fiche est trop vague : reviens à D8 et aux curseurs, c'est presque toujours là que ça coince.

## Exemples

- [Marque fictive B2B : Constructys](exemples/constructys.md) : extraction complète d'une voix B2B industrielle, du corpus à la fiche.

## Pièges

- ❌ **Décrire au lieu de prescrire** : « notre marque est authentique » n'aide personne à écrire. « Nos phrases font moins de 20 mots et on n'emploie jamais le passif » oui.
- ❌ **Trop de curseurs** : au-delà de 6 paramètres, plus personne ne les utilise. Reste sur 5.
- ❌ **Oublier le lexique négatif** : les mots qu'on refuse définissent la voix autant que les mots signatures. Ne livre jamais une fiche sans la section « ce qu'on ne fait jamais ».
- ❌ **Confondre ton et voix** : le ton change selon le contexte (un email n'est pas un manifeste), la voix reste. Tu formalises la voix, pas le ton.
- ❌ **Sauter le test LLM** : si un modèle ne reproduit pas la voix avec un bon prompt, elle n'est pas assez formalisée. Le test n'est pas optionnel, c'est la preuve.
- ❌ **Figer la voix** : une voix évolue. Date la fiche et révise-la tous les six mois.

## Pour aller plus loin

- [Canvas d'extraction de voix](references/canvas-extraction.md) : le prompt complet pour analyser un corpus en une passe.
- [Écriture française](../ecriture-francaise/SKILL.md) : le skill complémentaire. Une fois la voix fixée, il élimine le slop IA qui la pollue.
- *The Brand Gap*, Marty Neumeier : la référence courte sur l'écart entre identité voulue et identité perçue.
- *Letting Go of the Words*, Janice Redish : écrire pour le web sans diluer sa voix.

---

*Dernière mise à jour : 18/06/2026*
