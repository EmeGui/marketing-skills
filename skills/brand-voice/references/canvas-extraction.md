# Canvas d'extraction de voix de marque

> Prompt à coller dans un LLM pour analyser un corpus de textes et en extraire une voix de marque structurée. S'utilise à l'**Étape 2** du skill [Brand Voice](../SKILL.md).

## Mode d'emploi

1. Rassemble 5 à 10 textes de la marque (3 000 mots cumulés, voir Étape 1 du skill).
2. Colle le prompt ci-dessous dans un LLM.
3. Colle tes textes après la ligne `---`, en les séparant par `=== TEXTE N ===`.
4. Relis la sortie en gardant la **règle de triangulation** : ne retiens que ce qui apparaît dans au moins 2 textes.

## Le prompt

```
Tu es un analyste de voix de marque. Je vais te donner plusieurs textes d'une
même marque. Analyse-les ensemble et produis une fiche structurée. Règle
absolue : pour chaque point, cite un passage réel entre guillemets. Ne déduis
rien sans preuve dans le texte. Si une dimension n'est pas observable, écris
« non déterminable » plutôt que d'inventer.

D1 : PERSONNALITÉ
3 à 5 adjectifs qui ressortent. Puis l'archétype dominant, un seul parmi :
expert qui enseigne / guide qui accompagne / pair qui partage / challenger qui
provoque / pionnier qui trace la voie. Justifie par un passage.

D2 : REGISTRE
Niveau : familier / courant / soutenu. Adresse : tutoiement / vouvoiement /
impersonnel. Distance : autorité distante / expert accessible / pair-à-pair.

D3 : POSTURE
La marque enseigne / partage / inspire / accompagne / provoque ?
Structure dominante : réponse directe d'abord (BLUF) / construction
progressive / narratif / orienté preuve ?

D4 : SYNTAXE
Longueur de phrase dominante (courte < 15 / longue > 25 / mixte). Voix active
ou passive. Pronom narratif (nous / on / vous / impersonnel). Densité des
paragraphes. Donne une phrase courte et une phrase longue caractéristiques.

D5 : TONALITÉ
Chaleur (froide / neutre / chaleureuse). Humour (absent / subtil / assumé).
Rapport à la prudence (assertif direct / prudent / factuel neutre).

D6 : LEXIQUE SIGNATURE
Les 5 à 10 mots ou expressions récurrents et non génériques. Les 2-3 champs
lexicaux dominants. Cite chaque expression avec son contexte d'usage.

D7 : RAPPORT À LA PREUVE
Affirmation pure / chiffres et études / anecdotes clients / mix. À quelle
fréquence la marque prouve ce qu'elle avance.

D8 : CE QUE LA MARQUE NE FAIT JAMAIS
Le plus important. Mots et tournures hors-ton (buzzwords, anglicismes,
superlatifs qu'elle évite). Constructions absentes. Sujets jamais abordés.
Rapport aux concurrents (jamais nommés / comparaisons assumées). Rapport au
prix (caché / transparent). Déduis-le de ce que la marque évite
systématiquement, pas seulement de ce qu'elle dit.

SYNTHÈSE EN UNE PHRASE
« Cette marque parle comme un [archétype] qui [posture] à [cible]. »

---
[COLLE TES TEXTES ICI, séparés par === TEXTE N ===]
```

## Interpréter les résultats

1. **Valide les extractions.** Vérifie que chaque citation est représentative, pas un cas isolé. Si le LLM cite un passage que tu ne retrouves qu'une fois, écarte-le.
2. **Complète les manques.** Si une dimension ressort « non déterminable », relis les textes toi-même : le modèle rate parfois le lexique signature.
3. **Soigne D8.** C'est la section que le LLM remplit le moins bien, car elle demande d'inférer une absence. Enrichis-la à la main.
4. **Bascule vers la fiche.** Reporte les résultats dans le template d'une page (Étape 5 du skill), puis rédige le prompt d'injection (Étape 6).

## Pièges

- Ne donne jamais un seul texte : le modèle surinterprète des détails non signifiants.
- Ne mélange pas les auteurs : si la marque a plusieurs rédacteurs très différents, analyse-les séparément, puis unifie.
- Ne prends pas la sortie pour argent comptant : un LLM invente des patterns plausibles. Tout se vérifie dans les textes d'origine.
