# Finitions Florentin — publication automatique des réseaux sociaux

Ce dépôt est public : il sert d'hébergement d'images à Metricool (adresse
`https://raw.githubusercontent.com/Tony00485/finitions-florentin-posts/main/images/<fichier>.png`)
et de mémoire au système. N'y mettre que des images destinées à être publiées.

## Client
FINITIONS FLORENTIN, 3 rue de Genève 69006 Lyon, finitionsflorentin.fr,
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
- Google Business : 2 posts/semaine, le jeudi et le lundi à 9 h, via Metricool (`providers` gmb, `gmbData.type=publication`, texte court ≤ 1500 caractères, image d'une carte de la semaine, texte rédigé dans le style Google ci-dessous). Connecté depuis le 04/11/2026. Déjà programmés : 4/11 (publié), 6/11, 9/11, 12/11, 16/11, 19/11, 23/11, 26/11, 30/11, 3/12, 7/12, 10/12, 14/12.
- Format : PNG 1080×1350 (4:5).

## LinkedIn personnel d'Anthony (marque Metricool « Anthony D'ORAZIO », blogId 7872561)
- 2 posts par semaine, **mardi et mercredi à 8 h 30** (jours sans post de la page). `providers` linkedin, `linkedinData.type=post`.
- C'est Anthony qui parle : **première personne** (« je », « mon père et moi », « mon frère Jordan et moi »). **Ne jamais inventer de souvenir, d'anecdote, d'opinion ou de fait personnel** : uniquement des faits confirmés (voir plus haut) et des conseils de métier neutres.
- Contenu majoritairement différent de la page ; parfois le même sujet quand il est important (décennale, dégât des eaux, qualifications). Certains posts en **texte seul** (sans image), d'autres avec une carte du dépôt.
- Déjà programmés : 10/11 histoire, 11/11 support avant peinture, 17/11 devis + décennale, 18/11 dégât des eaux, 15/12 peinture en dernier (texte seul), 16/12 bandes à joints. Pas encore de posts perso les 24/11, 25/11, 1/12, 2/12, 8/12, 9/12.

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
4. Pied de post fixe : « 📍 Intervention à Lyon et alentours » puis « 💬 Devis gratuit – contactez-nous via notre fiche Google ». JAMAIS de numéro de téléphone, e-mail ni identifiant de réseau dans le texte : Google a désactivé les publications de la fiche le 04/11/2026 (mail « votre post ne respecte pas le règlement Google », cause probable : coordonnées non vérifiées dans le texte).
Paragraphes aérés (ligne vide entre blocs), 5 hashtags en fin de post, séparés du pied de post par une ligne vide (ex. #PeintreLyon #RenovationLyon #ArtisanLyon + un hashtag du sujet + #FinitionsFlorentin). Mêmes règles absolues que le reste (pas de prix, délais, chiffres inventés, marques).
Les 5 posts Google du 5/11 au 3/12 ont été réécrits dans ce style le 04/11/2026.

## Dates spéciales (à traiter automatiquement, sans que le gérant le demande)
Quand la semaine programmée contient une de ces dates, remplace le post du jour (ou ajoute-le) par un post de vœux, sobre, au « nous », sans promo, sans prix, sans horaires ni fermeture inventés :
- 24/12 : « Belles fêtes de fin d'année » (JAMAIS « Joyeux Noël » : Noël est religieux et pas fêté par tout le monde, consigne du gérant). Carte typographique sobre, sans symbole religieux.
- 31/12 ou 01/01 : vœux de bonne année 2027 (carte « Bonne année 2027 », remerciement aux clients, souhait de projets réussis). Publier le 01/01 à 10 h sur Instagram, Facebook, LinkedIn page (8 h 30) et Google (9 h), plus un message d'Anthony à la première personne sur son LinkedIn perso (texte seul, sincère, sans anecdote inventée).
- Ensuite : même principe chaque année : « belles fêtes de fin d'année » le 24/12 et vœux de bonne année le 1er janvier ; pour toute autre date marquante (rentrée, printemps), rester sur du contenu utile, sans promotion.
Vérifier dans etat.json que le post de vœux n'a pas déjà été programmé.

## Photos de chantier disponibles (envoyées par le gérant le 03/11/2026)
27 photos retouchées légèrement dans photos/ (NN_nom_beau.jpg). Utilisées déjà : 20 cuisine, 40 plafond courbe, 23 terracotta, 35 feuillage. Reste à exploiter : décoratives (61, 68, 52, 30, 78, 80, 69, 71, 50, 51), et techniques (44 placo sur ossature, 42 plaques+ponçage, 22/55/19/74 bandes à joints, 47 pare-vapeur, 45/46/43/49/58 isolation dont laine de bois). Regarder la photo avant d'écrire : ne décrire que ce qui est visible, jamais de retouche des défauts. Photo 64 (véhicules) : LinkedIn/Facebook seulement. Objectif : au moins 2 posts photo par semaine (IG/FB), et utiliser une photo en image des posts Google quand le sujet s'y prête (isolation, plâtrerie).

## IMAGES des posts Google : jamais de téléphone ni de site dedans
Les cartes IG/FB portent en pied « finitionsflorentin.fr · [numéro] » : INTERDIT sur Google (coordonnées non vérifiées → Google retire le post et peut bloquer les publications ; incident du 04/11/2026, l'erreur venait aussi de l'image, pas seulement du texte). Pour Google, utiliser les versions du dossier google/ (pied « FINITIONS FLORENTIN · Lyon »), ou créer une version sans coordonnées. Toujours REGARDER l'image avant de programmer un post Google : ni numéro, ni e-mail, ni adresse de site.


## RÈGLE ABSOLUE (consigne du gérant, 05/11/2026) : JAMAIS de numéro de téléphone
Le numéro de téléphone (le numéro du gérant) ne doit apparaître NULLE PART : ni dans les images, ni dans les légendes, ni dans les posts Instagram, Facebook, LinkedIn, Google. Remplacer par :
- Instagram / Facebook : « Devis gratuit : écrivez-nous en message privé. »
- LinkedIn (page et perso) : « Devis gratuit sur finitionsflorentin.fr »
- Google : « 💬 Devis gratuit – contactez-nous via notre fiche Google »
Les cartes sont rendues avec le pied « finitionsflorentin.fr · Lyon » (tools/*.py corrigés). Le site finitionsflorentin.fr peut apparaître. Le dossier ig/ contient les images IG/FB/LinkedIn à jour sans numéro ; google/ celles pour Google.

## VARIÉTÉ VISUELLE (consigne du gérant, 05/11/2026)
Les cartes ne doivent pas toutes se ressembler (les 3 traits rouge/bleu/noir en haut + même mise en page = lassant). Chaque semaine : au moins 2 posts IG/FB avec une vraie photo du dossier photos/ (mise en page « photo » ou photo seule), pas deux fois de suite la même mise en page ni le même fond, et les traits du haut sur une carte sur deux seulement. Relire chaque légende et chaque ligne de carte : tout doit être clair et vrai, sans formule vague.

## Finitions de peinture (précision du gérant, 05/11/2026) : ne jamais figer de règle
Murs : mat, velours OU satiné selon le rendu voulu. Boiseries : satiné, voire brillant. Plafonds : mat en général. Pièces humides : peinture adaptée à l'humidité. Toujours formuler en choix possibles (« au choix selon le rendu »), jamais « mat = plafonds uniquement ».

## CONTRÔLE QUALITÉ AVANT PROGRAMMATION (le gérant n'est pas toujours là pour corriger)
Pour chaque post, avant de programmer : (1) chaque affirmation technique est confirmée par une recherche web sur une source sérieuse (DTU, fabricants, ADEME, service-public) ; sinon, la reformuler en « selon les cas » ou abandonner le sujet ; (2) pas de règle absolue du type « X = Y uniquement » : un métier a presque toujours plusieurs options ; (3) chaque ligne de carte doit se comprendre seule par un particulier, sans jargon vague ; (4) relire la carte à l'image et la légende côte à côte : mêmes faits ; (5) en cas de doute, ne pas programmer ce post.

Option de rendu : `"nobars": true` dans l'objet de spec de tools/render.py supprime les 3 traits du haut. Utiliser sur au moins une carte typographique sur deux.

## NOUVEAU STYLE VALIDÉ PAR LE GÉRANT (05/11/2026) : tools/render2.py — À UTILISER POUR TOUTES LES CARTES
`python3 tools/render2.py spec.json dossier_sortie` (voir l'en-tête du script). Logo posé sans bulle, angles droits partout, petit titre rouge, grand titre, trait rouge, contenu, bandeau de pied coloré avec phrase + bouton « Devis gratuit ».
- Thèmes à faire tourner (jamais deux fois le même d'affilée) : marine, pierre, ciel, blanc, degrade. Le ton pierre doit revenir chaque semaine.
- Mises en page (kind) à varier : checks, numbers, tiles (4 cases), stat (grand chiffre ou « NON »), duo, photo (photo de chantier en haut + titre + bandeau).
- Au moins 2 posts photo par semaine (kind photo).
- Textes courts et lisibles sur téléphone ; ne pas surcharger.
- Version Google : même carte avec `"nosite": true` (pied « Lyon et alentours », sans site), copiée dans google/.
- L'ancien tools/render.py (cartes à 3 traits) n'est plus utilisé.
- Histoire de l'entreprise : créée en 2005 par Anthony et son père ; Jordan a rejoint l'équipe bien avant 2019 (année exacte inconnue : ne jamais l'inventer) ; depuis 2019 Anthony et Jordan dirigent l'entreprise.

## NOUVEAU DÉPART (05/11/2026, consigne du gérant) — CE RYTHME REMPLACE TOUS LES PRÉCÉDENTS
Le gérant a supprimé tous les anciens posts publiés. Lancement le 06/11/2026 à 12 h 30 (carrousel de présentation partout).
Les anciens posts programmés sont passés en BROUILLON avec le texte « [ANCIEN POST - BROUILLON À SUPPRIMER] » : les ignorer complètement (ne pas les compter comme programmés, ne jamais les republier).
- **Tous les jours, 1 publication** : Instagram + Facebook (12 h 30 en semaine, 10 h le week-end), page LinkedIn (8 h 30, légende plus rédigée), LinkedIn perso d'Anthony (12 h 30, première personne).
- **LinkedIn perso** : la même publication que la page, réécrite à la première personne (« je », « nous »). De temps en temps (1 à 2 fois par semaine), un texte plus personnel, sans image, à la place : regard d'artisan sur le métier, valeurs, coulisses. JAMAIS d'anecdote, de chiffre ou de fait inventé (client, chantier précis, date, souvenir) : rester sur des convictions et des généralités vraies du métier. Faits connus : entreprise créée en 2005 par Anthony et son père ; Jordan a rejoint l'équipe bien avant 2019 (année inconnue) ; depuis 2019 Anthony et Jordan dirigent l'entreprise.
- **Google Business : 3 posts par semaine, lundi, mercredi et vendredi à 9 h.** Pensés pour le RÉFÉRENCEMENT LOCAL : un service par post (peinture, plâtrerie, isolation intérieure RGE, carrelage, sols, papier peint, dégât des eaux…), titre avec mot-clé + ville (« Peintre à Lyon 6e », « Isolation intérieure à Lyon »), texte avec mots-clés locaux (Lyon, Lyon 6e, Lyon et alentours), puces ✔, « Chez FINITIONS FLORENTIN, nous… », « 📍 Intervention à Lyon et alentours », « 💬 Devis gratuit – contactez-nous via notre fiche Google », 5 hashtags locaux (#PeintreLyon #PlatrierLyon #IsolationLyon #RenovationLyon #Lyon6 #ArtisanLyon…). Image spécifique Google (render2 avec "nosite": true, dossier google/), de préférence une vraie photo de chantier liée au service. INTERDIT sur Google, texte ET image : téléphone, e-mail, adresse de site.
- **Téléphone : jamais nulle part.**
- Les sujets et textes des anciens posts (sources/legendes_lot1.md) sont vérifiés et peuvent être réutilisés, redessinés avec render2 (non encore publiés depuis le nouveau départ : décennale, 5 métiers, plafond courbe, isolants, déphasage, engagements, peinture A+/COV, terracotta, CEE, sinistre, feuillage, plomb, laque, humidité, couleur, arches, bandes à joints, avant devis).
- Déjà programmé depuis le nouveau départ : du 06/11 au 16/11 (voir etat.json).

- PAS DE CARROUSEL sans accord explicite du gérant (05/11/2026) : une seule image par post.

## PHOTOS (consigne du gérant, 07/11/2026)
- Le gérant envoie un dossier de BELLES PHOTOS : elles sont rangées dans `photos_selection/`. Dès qu'il contient des photos, n'utiliser QUE ce dossier pour les posts photo et les images Google ; oublier les autres photos de chantier (`photos/`). Tant qu'il est vide, `photos/` reste utilisable.
- Ne jamais oublier les posts photo : au moins 3 par semaine sur IG/FB/LinkedIn, et de préférence une photo pour chaque post Google.
- 07/11/2026 (14h48) : dossier WebP reçu et il REMPLACE le premier envoi. 112 photos dans `photos_selection/` (peinture, papier-peint, placo, isolation, carrelage-faience, sols, sols/parquet, sols/poncage-vitrification, sols/pvc-moquette). Les noms de fichiers sont descriptifs et contiennent des mots-clés utiles pour Google. Voir `photos_selection/catalogue.md` et marquer chaque photo utilisée (colonne « Déjà utilisée », avec la date). Le dossier `photos/` est ABANDONNÉ : ne plus jamais l'utiliser.
- Les métiers de la sélection donnent les thèmes Google : peinture, plâtrerie/placo, isolation, carrelage, papier peint, parquet (pose, ponçage et vitrification), sols PVC et moquette (aussi bureaux et locaux professionnels).
- Clients professionnels (consigne 07/11/2026) : on PEUT et on DOIT dire le type de lieu (boutique de vêtements, cabinet dentaire, bureaux, locaux professionnels, commerce) pour montrer que l'entreprise travaille aussi pour les pros ; JAMAIS le nom du client ni de l'enseigne. Les photos retouchées de la sélection sont validées par le gérant.
- Nouveaux thèmes visibles dans la sélection : peinture extérieure (façade, portail), ratissage et préparation des murs, ragréage autolissant, terrasse en dalles sur plots, faux plafonds à spots, dalles de bureaux.

## PHOTOS — MISE À JOUR 07/11/2026 15h25 (prime sur tout ce qui précède)
Le gérant demande d'OUBLIER toutes les photos envoyées jusqu'ici. Elles sont rangées dans `photos_archive_ne_plus_utiliser/` : NE JAMAIS les utiliser. Seul le prochain dossier envoyé par le gérant, rangé dans `photos_selection/`, sert aux posts. Si `photos_selection/` est vide, ne programme aucun post photo : fais des cartes et signale dans le message final qu'il manque les photos.

## PHOTOS — VERSION DÉFINITIVE (08/11/2026, prime sur tout ce qui précède)
Le gérant a envoyé le dossier « PHOTOS DE CHANTIER », classé par activité : c'est la SEULE source de photos pour toutes les publications. Il est dans `photos_selection/` (peinture, papier-peint, placo, isolation, carrelage-faience, sols, sols/parquet, sols/poncage-vitrification, sols/pvc-moquette) avec `catalogue.md`. Aucune autre photo, jamais. Le dossier `photos/` et toute archive antérieure sont abandonnés.

## STORIES (08/11/2026)
- Outil : `tools/story.py` (1080x1920, style render2 ; kinds card, photo, split avant/après). Images dans `ig/stories/`.
- 1 story par jour vers 18 h (IG + FB) qui complète le post du jour. Créées en BROUILLON : le gérant valide chacune. Metricool ne gère ni texte ni stickers sur les stories : le sticker (sondage, question, quiz, curseur) s'ajoute à la main dans Instagram au moment de publier ; une zone vide est prévue dans l'image.
- 9-16/11 : voir sources/stories_2026-11-09_16.json.

## PLAN 17/11/2026 → 01/01/2027 et nouvelles règles (08/11/2026, consigne du gérant — prime sur tout ce qui précède)
- **Tous les POSTS (IG/FB, LinkedIn page, LinkedIn perso, Google) sont créés en BROUILLON (`draft: true`)** : le gérant valide avant publication. Ne jamais créer un post en publication directe.
- **EXCEPTION : les STORIES sont en publication AUTOMATIQUE (`draft: false`)**, 1 par jour à 18h sur IG + FB, programmées au fur et à mesure chaque semaine par la tâche (sans texte, image 1080x1920 via tools/story.py).
- Rythme : IG/FB 1 post/jour (12h30 en semaine, 10h le week-end et jours fériés) ; LinkedIn page 8h30 ; LinkedIn perso 12h30 ; Google **2 par semaine (lundi et jeudi 9h)** + dates spéciales (24/12, 01/01).
- **Reels** : 1 à 2 par semaine, UNIQUEMENT de vrais avant/après ou étapes d'un même chantier (photos_selection). Montage ffmpeg (fondu xfade), mp4 dans `reels/`, type REEL sur IG et FB. Paires déjà utilisées : faux plafond (ossature → spots), isolation salle de bains (isolant → fenêtre placo → bandes). Faute de vraie paire, ne pas inventer : poster une photo et demander de nouvelles paires au gérant.
- **Les deux LinkedIn ne publient JAMAIS le même sujet le même jour** : le perso reprend un sujet de la page à une autre date (décalé) ou un texte personnel (2 fois/semaine, sans image).
- Les brouillons existants (hors « [ANCIEN POST ») = déjà programmés : ne pas les dupliquer.
- Metricool n'a pas d'outil de suppression : pour remplacer un post, le mettre à jour (updateScheduledPost) plutôt que d'en créer un nouveau.

## PUBLICATION AUTOMATIQUE EN PERMANENCE (08/11/2026 19h35, consigne du gérant — prime sur tout ce qui précède)
- « Tout doit partir automatiquement en permanence » : TOUS les posts (IG/FB, Reels, LinkedIn page, LinkedIn perso, Google) ET les stories sont créés avec `draft: false` et `autoPublish: true`. Plus aucun brouillon.
- Le plan 17/11 → 01/01/2027 a été entièrement basculé en publication automatique le 08/11/2026.
- Conséquence : le contrôle qualité avant programmation (texte, faits vérifiés, pas de téléphone, pas de site/mail sur Google, photos de photos_selection uniquement) est d'autant plus impératif, car personne ne relit avant publication.

## REELS (08/11/2026 19h47, consigne du gérant)
- Le gérant n'a PAS de photos « avant » pour l'instant : ne JAMAIS présenter un Reel comme un « avant/après ».
- Seuls Reels possibles : les étapes réelles d'un même chantier (en cours → fini) déjà identifiées (faux plafond, isolation/doublage). Pas de nouvelle paire = pas de Reel, posts photo à la place. Ne pas relancer le gérant à ce sujet ; il enverra des photos avant quand il en aura.
- 08/11 20h15 : le gérant accepte les « PENDANT / APRÈS » (photo en cours de chantier → pièce finie). Outil : `tools/reel.py` (spec JSON, étiquettes PENDANT/APRÈS, carte de fin render2). Paire salon haussmannien (préparation-ratissage → cheminée marbre rose) utilisée en Reel le 29/11.
