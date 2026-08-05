# DESIGN.md — Home Rénovation 14

Direction : **le toit normand face à la Manche**. Ardoise mouillée, terre cuite, embruns.
Palette prise dans le logo réel du flyer (marine + orange), inflechie vers la matière du
métier : le marine du logo *est* la couleur de l'ardoise, l'orange *est* celle de la tuile.
Objectif unique : appels et demandes de devis. Ton : couvreur du littoral, direct, pas startup.

Contrainte forte du brief : **couvreur d'abord**. La toiture occupe le hero, la section
signature et la moitié de la page. Peinture, ravalement, placo, isolation, maçonnerie et
carrelage existent, groupés dans une bande secondaire clairement subordonnée.

---

## 1. Palette (relevée sur le logo vectoriel du client)

| Token | Hex | Rôle | Contraste |
|-------|-----|------|-----------|
| `--ardoise` | `#10305C` | Marine du logo, Ardoise mouillée, Titres, sections profondes, | 11,75:1 sur `--nacre` ✓ AAA |
| `--ardoise-nuit` | `#081F41` | Ardoise à contre-jour, En-tête, hero, contact, footer, | 14,65:1 sur `--nacre` ✓ AAA |
| `--tuile` | `#F26205` | Orange du logo, **Graphique uniquement** : filets, carrés-repères, icônes, pastille d'urgence, | 5,09:1 sur `--ardoise-nuit` ✓ AA non-textuel |
| `--tuile-fonce` | `#C24A02` | Orange assombri, **Boutons pleins** avec texte blanc, | blanc dessus 4,91:1 ✓ AA |
| `--tuile-clair` | `#FBA36A` | Orange éclairci, Petits textes d'accent sur fond marine, | 8,22:1 sur `--ardoise-nuit` ✓ AA |
| `--nacre` | `#F5F2EC` | Blanc coquillage tiède, côte de Nacre. Fond de page. | — |
| `--galet` | `#5C6875` | Gris galet. Texte secondaire, légendes. | 5,1:1 sur `--nacre` ✓ AA |
| `--sable` | `#E4DED2` | Sable de Sword Beach. Filets, séparateurs, fonds de cartes. | — |

**Deux oranges, une raison.** L'orange de marque `#F26205` ne passe pas AA en texte blanc
(3,22:1). Plutôt que de le tordre, je le garde pur pour tout ce qui est graphique et
j'assombris à `#C24A02` pour les boutons pleins. Le client reconnaît son orange, le
malvoyant lit le bouton.

**D'où viennent ces valeurs.** La première version du site était calée sur une photo du
flyer papier, donc sur des couleurs ternies par l'impression et l'éclairage. Le logo
vectoriel fourni ensuite donne les vraies : marine `#002048`, orange `#F86008`. Le marine
pur est presque noir et alourdissait les grandes surfaces, l'orange pur ne passe pas en
petit texte : la palette du site les reprend en les ouvrant d'un cran, sans changer de
teinte. Côte à côte, le logo et les boutons sont maintenant du même orange.

**Pourquoi ça évite les interdits :** pas de crème + serif + terracotta, pas de dégradé
SaaS, pas de glassmorphism. Le duo marine/orange est celui du client.

---

## 2. Typographie

2 familles, woff2 auto-hébergées dans `fonts/`, `font-display: swap`, latin + latin-ext.

- **Display — Barlow Condensed** (600/700, souvent CAPITALES).
  Grotesque **condensée**, lecture « signalétique de port, panneau de chantier, marquage
  d'échafaudage ». Le choix de la largeur étroite est délibéré : Felicioni utilise une
  Expanded, on prend l'axe inverse pour que les deux sites ne se ressemblent pas.
- **Corps — Public Sans** (400/500/600/700, variable).
  Sans institutionnelle, très lisible, un peu administrative. Ni Inter, ni Plex.

**Échelle** — base 16 px mobile / 17 px desktop.

| Élément | Mobile | Desktop | Police / graisse / interlignage |
|---------|--------|---------|--------------------------------|
| Surtitre | 13 px | 13 px | Barlow Cond. 700, CAPS, tracking .12em, `--tuile` |
| h1 | 38 px | 66 px | Barlow Cond. 700, CAPS, LH 0.98, tracking .005em |
| h2 | 30 px | 46 px | Barlow Cond. 700, CAPS, LH 1.02 |
| h3 | 20 px | 21 px | Public Sans 700, LH 1.3 |
| Corps | 16 px | 17 px | Public Sans 400, LH 1.65, mesure max 66ch |
| Légende | 14 px | 14,5 px | Public Sans 500, `--galet`, LH 1.5 |
| Bouton | 16 px | 17 px | Public Sans 700, tracking .01em |
| Chiffres (téléphone) | 26 px | 34 px | Barlow Cond. 700, `font-variant-numeric: tabular-nums` |

Préchargement du seul `barlow-condensed-700-latin.woff2` (le h1 du hero).

---

## 3. Signature — la coupe de toit interactive

**« Ce qu'on regarde sur votre toit »** : une coupe SVG dessinée à la main d'un rampant
normand (ardoise, liteaux, écran sous-toiture, isolation, charpente, gouttière zinc).
Six repères numérotés ; on clique, le panneau à droite explique la couche, ce qui lâche
en premier sur la côte, et ce que ça coûte de laisser courir.

Pourquoi celle-là plutôt qu'un comparateur avant/après :
1. Aucun autre métier ne peut réutiliser ce composant. Un plombier n'a pas de rampant.
2. Elle prouve la compétence au lieu de l'affirmer, sans une seule photo — et on n'a
   justement aucune photo réelle du client à ce stade.
3. Elle **branche les métiers secondaires depuis l'intérieur du toit** : la couche
   « isolation » renvoie à l'isolation/placo, la couche « rives et planches de rive »
   renvoie à la peinture. Le brief « couvreur d'abord, le reste ensuite » est résolu par
   le composant lui-même, pas par un menu.

**Montage au scroll.** Quand la coupe entre dans le champ, les couches se posent dans
l'ordre d'un vrai chantier : plafond, isolant, chevrons, écran, liteaux, ardoises, puis
la gouttière et les lignes de rappel. Chaque groupe glisse de 30 px perpendiculairement
au rampant, avec 130 ms d'écart. Les six repères apparaissent après, une fois le toit
monté. L'état masqué n'est posé que par le JavaScript : sans lui, la coupe reste
entièrement visible. `prefers-reduced-motion` court-circuite l'ensemble.

**Le logo.** Seul le pictogramme est utilisé, jamais la version avec le lettrage : le nom
est déjà composé à côté, en Barlow Condensed. Ses aplats blancs et son marine profond
disparaîtraient sur l'en-tête sombre, il est donc posé sur une pastille `--nacre` — le même
rapport clair/sombre que sur le flyer. Le favicon reprend le motif central, la maison au
toit orange et le couvreur sur son échelle, seule partie qui reste lisible à 32 px.

Tissu conjonctif : chaque surtitre de section est précédé d'un **petit carré orange plein**
suivi d'un filet `--sable` de 1 px. Rappel du bloc de toit orange du logo. Répété, discret.

---

## 3 bis. Illustrations de section

Six visuels vectoriels dans la palette de marque, posés sur fond `--ardoise-nuit` pour
peser comme des photos : entretien, démoussage, fuite, zinguerie, littoral, second œuvre.
Ils sont générés par `img/gen_cards.py`, pas dessinés à la main, et affichés **comme des
illustrations** — jamais comme des chantiers du client. Le bandeau littoral porte sa
légende en clair. Ils comblent le vide en attendant les vraies photos, qui restent le
levier de conversion le plus fort.

---

## 4. Layout

Page unique, mobile-first, contenu max 1140 px. Alternance `--nacre` / `--ardoise-nuit`
sur trois respirations seulement.

**En-tête** — wordmark, nav ancre, bouton « Appeler » orange. Mobile : wordmark + barre
d'appel sticky en bas.

**1 · Hero (fond ardoise-nuit, split)** — le sujet, la zone, les deux promesses réelles du
flyer, puis le téléphone en gros. À droite, la coupe de toit en version décorative.
```
┌────────────────────────────────┬──────────────┐
│ ▪ COUVREUR — OUISTREHAM & CÔTE  │              │
│ Votre toit encaisse             │  [ coupe de  │
│ la Manche toute l'année         │   toit SVG   │
│                                 │   dessinée ] │
│ Entretien, démoussage, réparat. │              │
│ ✓ Devis gratuit  ✓ Déplacement  │              │
│ [ ☎ 06 58 94 19 08 ] [ Devis ]  │              │
└────────────────────────────────┴──────────────┘
```

**2 · Toiture (le cœur)** — 4 blocs : entretien & démoussage, réparation & fuite,
traitement hydrofuge, zinguerie & gouttières. Un paragraphe concret chacun.

**3 · Coupe interactive (signature, fond ardoise-nuit)** — 6 repères + panneau.

**4 · Le climat de la côte** — 3 blocs : vent de la Manche, air salé, mousse. Le seul
contenu de la page qu'aucun couvreur de l'intérieur des terres ne pourrait recopier.

**5 · Le reste de la rénovation (secondaire, compact)** — 6 puces sur une bande basse :
peinture, ravalement, placo, isolation, petite maçonnerie, carrelage & joints de pierre.
Typo plus petite, pas de photo, pas de CTA propre. Volontairement en retrait.

**6 · Méthode** — 01 Appel · 02 Visite et montée sur toit · 03 Devis gratuit · 04 Chantier.

**7 · Zone d'intervention** — liste texte des communes, pas de carte image.

**8 · FAQ** — 5 questions, celles qui tombent au téléphone.

**9 · Contact** — téléphone en gros + formulaire 5 champs.

**10 · Footer** — coordonnées, SIREN réel, liens légaux.

**Barre sticky mobile** — `tel:` orange pleine largeur, toujours visible sous 768 px.

---

## 5. Auto-relecture « et si c'était pour n'importe quel couvreur ? »

1. **Palette** : marine + orange sortis du flyer, pas d'une charte inventée. Le double
   orange (marque / bouton) est une décision propre à ce logo.
2. **Type** : condensée de signalétique portuaire, à l'opposé de l'Expanded de Felicioni
   et du Bricolage Grotesque de RJ Raval.
3. **Signature** : la coupe de toit ne sert qu'à un couvreur, et son contenu parle
   d'ardoise, de zinc et d'embruns — pas de tuile canal du Sud.
4. **Copy** : la section climat nomme la Manche, le sel, les vents d'ouest et la mousse
   normande. Transposée à Brétigny ou Toulouse, elle devient fausse.
5. **Preuve sociale** : aucune note Google inventée (il n'y en a pas). À la place, le seul
   fait vérifiable dont on dispose : entreprise immatriculée depuis avril 2009, SIREN
   affiché en clair et cliquable vers l'annuaire officiel.
6. **Zéro compteur animé**, zéro « 200 chantiers ».

---

## ⚠️ Réserves ouvertes — à régler avant mise en ligne

- **Aucune fiche Google Business trouvée**, donc aucune note, aucun avis sur la page. Créer
  la fiche est le premier levier, devant le site. Bloc avis prêt dans le README à coller
  dès qu'il y a 5 avis réels.
- **Aucune photo réelle.** Le design tient sans, par choix. Il faut 8 à 10 photos de
  chantiers pour la galerie (bloc prêt dans le README).
- **Adresse légale divergente.** Le flyer indique 80 av. du Maréchal Foch, 14150 Ouistreham ;
  l'annuaire des entreprises donne 22 rue Surcouf, 53500 Ernée. Le site affiche Ouistreham
  comme adresse d'intervention, les mentions légales sont laissées à compléter.
- **NAF déclaré = 43.34Z peinture et vitrerie**, pas couverture. Aucune mention de garantie
  décennale ou d'assurance sur la page tant que l'attestation n'est pas fournie.
- **Formulaire** : `formsubmit.co` en place, il faut l'adresse e-mail du client et une
  première validation du domaine.
