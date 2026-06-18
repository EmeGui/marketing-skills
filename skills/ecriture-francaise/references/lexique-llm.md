# Lexique signature LLM — à purger

> Ressource du skill [Écriture française](../SKILL.md). Cette liste recense les mots, tournures et transitions **sur-utilisés par les modèles de langage en français**. Elle sert à l'**Étape 3 : Purger le lexique**.

**Règle générale.** Aucun de ces termes n'est interdit en valeur absolue. C'est leur **densité** qui trahit une rédaction LLM. Vise moins de 0,20 % du total de mots. Remplace par un équivalent contextuel, ou mieux : supprime quand la phrase fonctionne sans.

**Règle de doublon.** Ne remplace jamais un terme de la purge par un autre terme de la purge. « Par ailleurs » ne devient pas « de plus » : même famille, même problème.

---

## 1. Verbes signature

| À purger | Remplacements possibles (selon contexte) |
|---|---|
| souligner, mettre en lumière, mettre en exergue | montrer, pointer, rappeler, noter, dire |
| éclairer | expliquer, décrire, préciser |
| décrypter, décoder, démystifier | comprendre, expliquer, résumer |
| aborder (un sujet) | traiter, examiner, ouvrir |
| s'inscrire dans, s'inscrire au cœur de | relève de, entre dans, participe à |
| témoigner de, attester de | prouve, montre, confirme, indique |
| constituer (un enjeu, un défi) | être, former, *ou supprimer* |
| permettre de | laisse, autorise, ouvre à, *ou reformuler en action directe* |
| offrir la possibilité de | donne, laisse, *ou supprimer* |
| se positionner comme | est, devient, revendique |
| marquer un tournant | change, bascule, rebat les cartes |
| redéfinir (les codes, la norme) | bouscule, réécrit, casse |
| révolutionner | change, transforme, bouleverse (avec modération) |
| repenser, réinventer | revoir, refaire, reprendre |
| capitaliser sur | exploiter, utiliser, tirer parti de |
| décliner (une stratégie) | appliquer, adapter, mettre en œuvre |

## 2. Adjectifs signature

| À purger | Remplacements / traitements |
|---|---|
| véritable (devant un nom) | *supprimer le plus souvent* : « un véritable enjeu » → « un enjeu » |
| crucial, pivotal | clé, central, décisif (avec parcimonie) |
| transformatif, transformationnel | qui change, décisif |
| robuste | solide, fiable, éprouvé |
| incontournable | central, reconnu, qu'on ne peut ignorer |
| majeur (en ouverture) | fort, important, de poids, *ou supprimer* |
| essentiel, central (en intensif) | *souvent supprimable* |
| pertinent | utile, adapté, juste, *souvent supprimable* |
| holistique | global, d'ensemble, systémique |
| dynamique (qualificatif vague) | *souvent supprimable* |
| stratégique (en ouverture vague) | *souvent supprimable* |
| innovant (sans objet) | *supprimer, ou dire précisément ce qui est nouveau* |

## 3. Transitions & connecteurs creux

| À purger | Remplacements / traitements |
|---|---|
| il est important de noter que | *supprimer* : dire la chose directement |
| par ailleurs (en tête de paragraphe) | *supprimer*, ou « mais », « aussi » |
| en outre, de surcroît | « et », « aussi », *ou supprimer* |
| dans un monde où, à l'heure où | *réécrire sans* |
| au cœur de (en ouverture) | « dans », « au centre de », *ou supprimer* |
| en effet (mécanique) | *supprimer dans 80 % des cas* |
| certes… mais… | nuance directe, sans la structure binaire |
| plongeons dans, explorons | *supprimer, entrer dans le sujet directement* |
| en conclusion, pour résumer | *supprimer ou rouvrir (question, perspective)* |
| force est de constater | on voit bien, manifestement |
| il convient de | il faut, mieux vaut, *ou supprimer* |

## 4. Hedging (incertitude molle)

| À purger | Traitement |
|---|---|
| il semble que | *prendre position ou citer la source* |
| on peut considérer que | *idem* |
| il est possible de / qu'il | *reformuler en affirmation* |
| dans une certaine mesure | *supprimer* |
| globalement, d'une manière générale | *supprimer* |
| relativement, assez (en intensif) | *supprimer ou chiffrer* |
| potentiellement | *supprimer ou chiffrer* |

Cible : **4-8 occurrences de hedging pour 1000 mots**. Les LLM en produisent plus de 15.

## 5. Anglicismes calqués

| À purger | Terme FR correct |
|---|---|
| supporter (= soutenir) | soutenir, appuyer, prendre en charge |
| adresser (= traiter) | traiter, répondre à, régler |
| implémenter | mettre en œuvre, déployer, appliquer |
| délivrer (= fournir) | fournir, livrer, apporter |
| challenger (verbe) | remettre en cause, contester, éprouver |
| opportunité (= occasion) | occasion |
| finaliser (= conclure) | conclure, terminer, boucler |
| investiguer (= enquêter) | enquêter, examiner |
| impacter | peser sur, affecter, toucher |
| basiquement | au fond, pour l'essentiel, *ou supprimer* |
| initier (= lancer) | lancer, engager, ouvrir |
| digital (adjectif général) | numérique |

## 6. Tics structurels

- **Triplets rhétoriques mécaniques** : « X, Y et Z » répété trois paragraphes d'affilée. Varie la forme.
- **Listes à puces pour tout** : préfère la prose quand la structure ne l'exige pas.
- **Question rhétorique en ouverture de section** : éviter les « Mais au fait, qu'est-ce que X ? ».
- **Reformulation de la question dans la réponse** (en FAQ) : répondre directement, sans répéter la question.
- **Paragraphes mono-phrase systématiques** : alterner les densités.
- **Emojis décoratifs** : à proscrire sauf si la voix de marque les assume explicitement.

## 6b. Le tiret cadratin `—` et le tiret simple `-`

**Em-dash `—` (U+2014) : à supprimer systématiquement.** Quel que soit le contexte (transition ou incise marquée), remplace par `,` `.` `:` `;` ou réécris la phrase. **Jamais** de remplacement par `-` simple. Beaucoup de lecteurs francophones perçoivent le `—` comme une signature IA, indépendamment de la justesse typographique de l'usage. Idem pour `--`.

**Tiret simple `-` : réduire en texte courant.** Le lecteur hostile au cadratin confond visuellement `-` et `—`.

- **À préserver** : mots composés (*c'est-à-dire, peut-être, vis-à-vis, au-delà, lui-même, ci-dessous, week-end…*), pronoms enclitiques (*dit-il, peut-on, faut-il*), nombres composés (*trente-deux, dix-sept*), listes à puces, URLs et slugs.
- **À réécrire** : le `-` entouré d'espaces (`X - Y`, faux cadratin) → `,` `.` `:` `;` ; et les anglicismes composés ci-dessous.

| Anglicisme composé | Remplacement FR |
|---|---|
| trade-off | arbitrage, compromis |
| win-win | gagnant-gagnant |
| in-house | en interne |
| one-shot | unique, ponctuel |
| hands-on | concret, pratique |
| end-to-end | de bout en bout |
| step-by-step | étape par étape, pas à pas |
| state-of-the-art | de pointe, à la pointe |
| out-of-the-box | clé en main, prêt à l'emploi |
| must-have | indispensable |
| nice-to-have | optionnel, secondaire |

## 7. Faux positifs (à ne PAS purger)

Ces termes paraissent « IA-ish » mais sont légitimes dans certains contextes métier. Ne les purge pas mécaniquement :

- **accompagner** : légitime en RH, coaching, services.
- **stratégique** : légitime en analyse business.
- **performant** : légitime en tech, sport, commercial.
- **expertise** : légitime pour un cabinet, une ESN.
- **digital** : légitime si la voix de marque l'emploie déjà.
- **opportunité** : légitime en commercial, quand le sens n'est pas « occasion ».

> Règle d'or : si la voix de ta marque revendique un de ces termes comme mot signature, garde-le. La cohérence de marque prime sur la règle générique.
