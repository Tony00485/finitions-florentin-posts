# Finitions Florentin — publication automatique des réseaux sociaux

Ce dépôt est public : il sert d'hébergement d'images à Metricool (adresse
`https://raw.githubusercontent.com/Tony00485/finitions-florentin-posts/main/images/<fichier>.png`)
et de mémoire au système. N'y mettre que des images destinées à être publiées.

## Client
FINITIONS FLORENTIN, 3 rue de Genève 69006 Lyon, tél. 07 87 85 93 06, finitionsflorentin.fr,
contact@finitionsflorentin.fr. Gérant : Anthony D'Orazio. Fondée en 2005, reprise en 2019 par Anthony et Jordan.
Métiers : peinture, plâtrerie, isolation par l'intérieur, carrelage, revêtements de sols et de murs.
Qualibat (peinture, ravalement, plaques de plâtre), mention RGE (isolation thermique par l'intérieur), RC Pro + décennale
(n° de police sur chaque devis, attestation sur demande).

## RÈGLES ABSOLUES (validées par le gérant)
- Français naturel, professionnel, **vouvoiement**. « Nous » (jamais « j'ai posé »). Légendes de photos : « Réalisé par Finitions Florentin ».
- **Aucun prix, aucun délai chiffré, aucune comparaison avec des concurrents, aucun avis ou chiffre inventé.**
- **Aucun nom de produit ni de marque.** Jamais de sous-traitants (« tous les chantiers sont à nous »). **Ne jamais citer la taille de l'équipe** ni « 150 projets par an ».
- Pas de « écologique / respectueux de l'environnement » : la classe A+ = émissions dans l'air intérieur.
- CEE : seulement « selon éligibilité », sans montant. Le client demande lui-même les autres aides (MaPrimeRénov'…). Nous ne gérons que le dossier CEE, la prime étant déduite de la facture.
- Logos Qualibat/RGE : uniquement le fichier officiel `tools/logo_qualibat_rge.png`, non modifié.
- Aucune image qui ressemble à de l'IA ; jamais de fausse photo de chantier. Photos : retouche légère uniquement (pas de retrait de défaut, pas de changement de teinte, pas d'IA). Flouter toute information privée visible.
- Faits confirmés par le gérant : velours sur les murs (plus de satin), mat au plafond, laque pour les boiseries/portes/plinthes (aspect satiné, velours ou mat au choix) ; protection du chantier par une bâche adaptée au support (souvent autoadhésive, ne jamais citer le polyane) ; faux plafond courbe = plâtrerie + peinture ; devis et travaux après dégât des eaux/sinistre ; plaques de plâtre : standard, hydrofuge, feu, phonique, haute densité (renfort, charges lourdes) ; isolants posés : laine de verre, laine de roche, laine de bois.
- Pas de contenu sur : plaques « NF », avantages financiers non confirmés, promesses de résultat.
- Fond de carte : blanc, bleu marine (#1E3B7D), bleu ciel, pierre. Jamais noir ni rouge plein. Varier mise en page et fond : ne jamais mettre deux fois le même fond d'affilée, ne jamais répéter un sujet déjà publié (voir `etat.json`).
- Toute affirmation technique nouvelle doit être vérifiée par une recherche web (sources sérieuses) avant publication. En cas de doute : ne pas publier ce sujet.

## Rythme (chaque semaine = jeudi → lundi)
- Instagram + Facebook : 5 posts (jeu, ven, sam, dim, lun). 12 h 30 en semaine, 10 h le week-end.
- LinkedIn : 3 posts (jeu, ven, lun) à 8 h 30, avec une légende LinkedIn **différente** (plus rédigée, sans hashtags en rafale).
- Le samedi : post photo (carte photo, `tools/render.py` layout `photo`). Les autres jours : cartes typographiques.
- Google Business : 2 posts/semaine, le jeudi et le lundi à 9 h, via Metricool (`providers` gmb, `gmbData.type=publication`, texte court ≤ 1500 caractères, image d'une carte de la semaine, texte rédigé dans le style Google ci-dessous). Connecté depuis le 04/11/2026. Déjà programmés : 4/11 (publié), 6/11, 9/11, 12/11, 16/11, 19/11, 23/11, 26/11, 30/11, 3/12, 7/12.
- Format : PNG 1080×1350 (4:5).

## LinkedIn personnel d'Anthony (marque Metricool « Anthony D'ORAZIO », blogId 7872561)
- 2 posts par semaine, **mardi et mercredi à 8 h 30** (jours sans post de la page). `providers` linkedin, `linkedinData.type=post`.
- C'est Anthony qui parle : **première personne** (« je », « mon père et moi », « mon frère Jordan et moi »). **Ne jamais inventer de souvenir, d'anecdote, d'opinion ou de fait personnel** : uniquement des faits confirmés (voir plus haut) et des conseils de métier neutres.
- Contenu majoritairement différent de la page ; parfois le même sujet quand il est important (décennale, dégât des eaux, qualifications). Certains posts en **texte seul** (sans image), d'autres avec une carte du dépôt.
- Déjà programmés : 10/11 histoire, 11/11 support avant peinture, 17/11 devis + décennale, 18/11 dégât des eaux.

## Outils
- `tools/render.py spec.json dossier_sortie` : rend les cartes (voir en-tête du script). Mises en page :
  - `lst(theme,kicker,titre,[(libellé,valeur),...],top=620)` (top=700 si le titre fait 3 lignes) — thèmes : blanc, bleu, ciel, pierre
  - `qa(theme,kicker,question,label,réponse)`, `vf(theme,kicker,énoncé,verdict,explication)`
  - `frise(theme,kick,titre,[(date,texte),...])`, `pastilles(theme,kick,titre,[(titre,sous-titre),...],y0,step,fs)`,
    `geant(theme,kick,gros,petit,sous)`, `tuiles(theme,kick,titre,[(titre,texte)...≤5])`, `coches(theme,kick,titre,[(titre,texte)...≤3])`,
    `confiance(theme,kick,titre,[(titre,texte)...])`, `photo(kicker,titre,sous-titre,fichier_photo,position)` (photos dans `photos/`).
  - Toujours **regarder l'image rendue** (Read) avant de publier : pas de texte qui déborde, pas de titre orphelin (utiliser `&nbsp;` avant « ? » et « : »).
- Metricool (connecteur) : `blogId` 7867468, fuseau Europe/Paris. Facebook+Instagram dans un même post (`providers` facebook+instagram, `facebookData.type=POST`, `instagramData.type=POST`) ; LinkedIn dans un post séparé (`linkedinData.previewIncluded=false`). Ajouter un `mediaAltText` descriptif. `media` = URL raw GitHub de l'image poussée dans `images/`.
- Nommage des images : `images/AAAA-MM-JJ_<nom>.png`.
- Légendes et idées déjà utilisées : `sources/legendes_lot1.md`, `etat.json`.

## Procédure hebdomadaire (tâche programmée)
1. Cloner le dépôt, lire ce README, `etat.json`, `idees.md`.
2. Vérifier dans Metricool (`getScheduledPosts`) ce qui est déjà programmé ; prendre la semaine suivante la plus proche non programmée.
3. Choisir 5 sujets neufs dans `idees.md` (ou proposer des sujets cohérents avec les règles), dont 1 post photo. Vérifier les faits par recherche web.
4. Rédiger les légendes (IG/FB + LinkedIn pour jeu/ven/lun), rendre les cartes, **regarder chaque image**.
5. Pousser les images (`git push`), programmer les posts dans Metricool, relire avec `getScheduledPosts`.
6. Mettre à jour `etat.json` et `sources/legendes_lot1.md`, puis pousser.
7. Si quelque chose échoue (Metricool, GitHub, rendu) : **ne rien publier à moitié**, arrêter, et le dire clairement dans le message de fin (le gérant est prévenu par notification).
8. Terminer par un résumé court (sujets, dates, ce qui est incertain).

## Style des posts Google (d'après les anciens posts d'Anthony, relevés le 04/11/2026)
Structure à respecter à chaque post Google Business (gmb, type publication, image jointe) :
1. Une ligne d'accroche avec un emoji au début (🎨 🏠 🛡️ 🏅 🤝 ⚠️ ✨), souvent sous forme de question ou de constat.
2. Une courte phrase d'explication, puis 2 à 4 puces « ✔ » (une idée par puce).
3. Une phrase « Chez FINITIONS FLORENTIN, nous… » (nom de l'entreprise en majuscules).
4. Pied de post fixe : « 📍 Intervention à Lyon et alentours » puis « 📞 Devis gratuit – contactez-nous au 07 87 85 93 06 ».
Paragraphes aérés (ligne vide entre blocs), 5 hashtags en fin de post, séparés du pied de post par une ligne vide (ex. #PeintreLyon #RenovationLyon #ArtisanLyon + un hashtag du sujet + #FinitionsFlorentin). Mêmes règles absolues que le reste (pas de prix, délais, chiffres inventés, marques).
Les 5 posts Google du 5/11 au 3/12 ont été réécrits dans ce style le 04/11/2026.

## Dates spéciales (à traiter automatiquement, sans que le gérant le demande)
Quand la semaine programmée contient une de ces dates, remplace le post du jour (ou ajoute-le) par un post de vœux, sobre, au « nous », sans promo, sans prix, sans horaires ni fermeture inventés :
- 24/12 : « Belles fêtes de fin d'année » (JAMAIS « Joyeux Noël » : Noël est religieux et pas fêté par tout le monde, consigne du gérant). Carte typographique sobre, sans symbole religieux.
- 31/12 ou 01/01 : vœux de bonne année 2027 (carte « Bonne année 2027 », remerciement aux clients, souhait de projets réussis). Publier le 01/01 à 10 h sur Instagram, Facebook, LinkedIn page (8 h 30) et Google (9 h), plus un message d'Anthony à la première personne sur son LinkedIn perso (texte seul, sincère, sans anecdote inventée).
- Ensuite : même principe chaque année : « belles fêtes de fin d'année » le 24/12 et vœux de bonne année le 1er janvier ; pour toute autre date marquante (rentrée, printemps), rester sur du contenu utile, sans promotion.
Vérifier dans etat.json que le post de vœux n'a pas déjà été programmé.
