# Contribuer à marketing-skills

Merci de votre intérêt pour contribuer. Ce repo est ouvert à toute personne qui souhaite partager des compétences marketing actionnables.

## Règles de contribution

### Ce qu'on accepte

- Des skills marketing complets, structurés selon le [format standard](../docs/skill-format.md)
- Des améliorations de skills existants (précisions, nouveaux exemples, pièges supplémentaires)
- Des corrections (typos, erreurs factuelles, liens cassés)
- Des traductions de ressources anglaises en français (avec attribution)

### Ce qu'on n'accepte pas

- Des prompts bruts sans méthode ni contexte
- Du contenu promotionnel pour un outil ou service
- Des skills qui ne concernent pas le marketing
- Du contenu en anglais (ce repo est en français)

## Processus

1. **Fork** le repo
2. **Créez une branche** : `git checkout -b mon-skill`
3. **Ajoutez votre skill** dans `skills/<nom-du-skill>/` en suivant le [format standard](../docs/skill-format.md)
4. **Commitez** avec un message clair : `git commit -m "Ajout du skill [nom]"`
5. **Poussez** : `git push origin mon-skill`
6. **Ouvrez une Pull Request** avec une description de votre skill

## Style

- Français uniquement (pas de mélange fr/en)
- Tutoiement
- Exemples concrets, pas de cas théoriques
- Pas de jargon inutile

## Curation

Ce repo est une bibliothèque curée par Nodiris. Les contributions sont les bienvenues, mais Nodiris garde le contrôle du merge : une PR peut être refusée, renvoyée pour modification, ou éditée pour rester cohérente avec la méthode et la voix du repo. Le délai de réponse n'est pas garanti.

## Vérification automatique

Chaque PR passe un lint (`scripts/lint.py`, lancé par GitHub Actions) qui contrôle : frontmatter des skills, liens internes, typographie (pas de tiret cadratin en prose) et manifestes JSON. Lancez-le en local avant de soumettre :

```bash
python3 scripts/lint.py
```

## Licence

En contribuant, vous acceptez que votre contribution soit publiée sous la licence MIT de ce repo (voir [LICENSE](../LICENSE)).
