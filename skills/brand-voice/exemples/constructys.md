# Exemple : Constructys — Voix d'une marque B2B industrielle

> Application complète du skill Brand Voice sur une marque fictive du BTP.

## Contexte

**Constructys** est une ETI française de 200 personnes, spécialisée dans la construction modulaire bas carbone. Elle vend à des maîtres d'ouvrage publics et privés. Son site est technique, ses articles de blog rares mais travaillés. L'équipe marketing veut lancer une newsletter et automatiser la rédaction avec un LLM.

## Étape 1 : Corpus analysé

- Page d'accueil du site (480 mots)
- Page "Nos réalisations" (620 mots)
- Article de blog "Pourquoi le modulaire bas carbone est l'avenir du BTP" (1100 mots)
- Post LinkedIn du DG (180 mots)
- Email de prospection type (250 mots)
- Fiche technique produit (340 mots)

**Total** : ~2970 mots sur 6 textes.

## Étape 2 : Patterns extraits

1. **Longueur moyenne** : 16-22 mots par phrase. Les phrases techniques sont plus longues, les posts LinkedIn plus courts.
2. **Pronoms** : "nous" dominant (marque collective), "vous" présent (adresse directe). Pas de "je".
3. **Temps** : présent indicatif dominant (80%). Futur simple pour les engagements. Pas de passé composé.
4. **Connecteurs** : juxtaposition dominante. "Mais" absent. "Car" plutôt que "parce que". Peu de subordination.
5. **Ponctuation** : sobre. Points d'exclamation absents. Deux-points fréquents pour introduire des listes. Points-virgules occasionnels (registre soutenu).
6. **Mots signatures** : "filière", "module", "cycle de vie", "maîtrise d'ouvrage", "performance", "engagement", "réalisé en France", "béton bas carbone", "industrialisation".
7. **Mots absents** : aucun anglicisme. Pas de superlatifs ("meilleur", "leader"). Pas de jargon startup.

## Étape 3 : Curseurs

| Curseur | Score | Commentaire |
|---|---|---|
| Registre | 4 | Soutenu sans être froid. Technique mais accessible. |
| Densité | 3 | 16-22 mots, tendance à la concision. |
| Posture | 3 | Expert neutre. Affirme sans fanfaronner. |
| Énergie | 2 | Calme, posé. L'urgence est dans l'enjeu écologique, pas dans le ton. |
| Abstraction | 3 | Mélange de concret (chantiers, délais) et de concepts (filière, impact). |

## Étape 4 : Lexique

**Mots interdits** :
- ❌ "disruption", "révolutionner", "next-gen", "scalable"
- ❌ "leader" (ne jamais s'auto-proclamer)
- ❌ "solution" (trop vague — dire ce qu'on fait)
- ❌ "green", "durable" (remplacé par "bas carbone", chiffré)

**Mots signatures** :
- ✅ "filière", "engagement", "performance mesurable"
- ✅ "maîtrise d'ouvrage", "cycle de vie"
- ✅ "réalisé en France", "industrialisation"

## Étape 5 : Prompt d'injection

```
Écris avec la voix suivante :
Tu es un expert technique qui parle à des professionnels de la construction.
Ton ton est sobre, précis, jamais autopromotionnel. Tu dis "nous" pour la
marque, "vous" pour le lecteur. Tu n'utilises jamais d'anglicismes ni de
superlatifs creux ("leader", "meilleur"). Tu préfères "béton bas carbone" à
"écologique" et "performance mesurable" à "durable". Chaque affirmation
technique est étayée par un chiffre ou une référence. Les phrases sont
juxtaposées plutôt que subordonnées. La ponctuation est sobre : pas de
points d'exclamation, des deux-points pour les énumérations.
```

## Étape 6 : Test

**Texte original** (écrit par le DG sur LinkedIn) :

> Notre dernier module livré à la Ville de Nantes. 42 logements, 6 mois de chantier, -40% de béton vs une construction classique grâce à notre système poteaux-poutres optimisé.

**Texte généré avec le prompt d'injection** (pour un post similaire) :

> Nous livrons cette semaine 28 logements à Rennes Métropole. Quatre mois de pose, une réduction de 35% du béton nécessaire par rapport à une solution traditionnelle. Les modules sont assemblés sur site en trois semaines, limitant les nuisances de chantier pour les riverains.

Le résultat reproduit fidèlement le rythme et le lexique de la marque. La voix est reconnaissable.
