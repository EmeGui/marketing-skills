# Canvas d'extraction de voix de marque

> Prompt à utiliser avec un LLM pour analyser un corpus de textes et en extraire la voix de marque.

## Contexte

Ce canvas s'utilise à l'**Étape 2** du skill [Brand Voice](../SKILL.md). Il prend en entrée un corpus de 5-10 textes et produit une fiche de voix actionnable.

## Le prompt

Copie ce qui suit dans un LLM, puis colle les textes à analyser après la ligne `---`.

```
Tu es un analyste de voix de marque. Je vais te donner 5 à 10 textes d'une
même marque. Analyse-les et produis une fiche de voix structurée comme suit :

1. LONGUEUR DE PHRASE
Donne la longueur moyenne estimée en mots et la tendance (courte/moyenne/longue).
Donne un exemple de phrase typique et un exemple de phrase atypique.

2. PRONOMS
Qui parle ? "nous", "je", "vous", "on", impersonnel ?
À qui ? Le lecteur est-il tutoyé, vouvoyé, absent ?

3. TEMPS VERBAUX
Quel temps domine ? Présent, futur, passé composé ?
Y a-t-il un temps absent ou évité ?

4. CONNECTEURS
Quels connecteurs logiques reviennent ?
Est-ce que les phrases s'enchaînent par juxtaposition (parataxe) ou par
subordination (hypotaxe) ?

5. PONCTUATION
Y a-t-il des signes caractéristiques ? Points d'exclamation, tirets, deux-points ?
La ponctuation est-elle sobre ou expressive ?

6. MOTS SIGNATURES (top 10)
Les mots ou expressions qui reviennent systématiquement et qui ne sont pas
génériques.

7. MOTS À BANNIR (5-10)
Les mots que cette marque n'utilise jamais, ou qui trahiraient sa voix
(buzzwords, anglicismes, tics de langage).

8. REGISTRE
Familier / courant / soutenu / technique ? Justifie avec un exemple.

9. POSTURE
Camarade / expert neutre / provocateur / pédagogue / autre ? Justifie.

10. RÉSUMÉ EN UNE PHRASE
"Cette marque parle comme un [rôle] qui [posture] à [cible]."

Pour chaque point, sois spécifique. Cite des passages. Ne fais pas de
suppositions sans exemple.

---
[COLLE TES TEXTES ICI]
```

## Interpréter les résultats

Une fois le prompt exécuté :

1. **Valide les extractions** : vérifie que les citations sont représentatives
2. **Complète les manques** : si le LLM n'a pas trouvé de mots signatures, relis les textes toi-même
3. **Positionne les curseurs** : utilise les résultats pour remplir l'étape 3 du skill
4. **Crée le prompt d'injection** : synthétise les points 8, 9 et 10 en un paragraphe d'instructions

## Pièges

- Ne pas donner un seul texte : le LLM va surinterpréter des détails
- Ne pas mélanger les auteurs : si la marque a plusieurs rédacteurs, analyse-les séparément puis unifie
- Ne pas prendre le résultat pour argent comptant : un LLM peut inventer des patterns. Vérifie toujours avec les textes d'origine
