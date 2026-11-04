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
- Google Business : 1 post/semaine le jeudi à 9 h, via Metricool (`providers` gmb, `gmbData.type=publication`, texte court ≤ 1500 caractères, image de la carte du jour). Connecté depuis le 04/11/2026.
- Format : PNG 1080×1350 (4:5).

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
