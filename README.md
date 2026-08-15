# Home Rénovation 14 — couvreur à Ouistreham

Site one-page pour Christopher Jardin, construit à partir du seul flyer papier.
Angle imposé : **couvreur d'abord**, les autres corps de métier en second plan.

- Direction artistique : [DESIGN.md](DESIGN.md)
- Preview locale : `python3 -m http.server 8143` puis http://localhost:8143

## Ce qui est dans la page

| Section | Contenu |
|---------|---------|
| En-tête | Pictogramme du logo sur pastille claire + nom composé, bouton d'appel portant la mention 24h/24 |
| Hero | Photo de toiture plein cadre, urgence 24h/24, téléphone, trois arguments |
| Atouts | Bande blanche à quatre colonnes juste sous le hero : urgence, fuite, devis, décennale |
| Toiture | 4 prestations, chacune avec une photo de ses chantiers |
| Coupe interactive | 6 repères cliquables sur une coupe de rampant (l'élément signature), **montée couche par couche au scroll** |
| Climat de la côte | Vent d'ouest, air salé, humidité + bandeau littoral — le contenu non transposable |
| Réalisations | 11 photos de chantiers du client, recadrées et légendées |
| Le reste | 6 métiers secondaires + illustration, bande compacte, volontairement en retrait |
| Méthode | 4 étapes |
| Zone | 24 communes en liste texte (SEO local) |
| FAQ | 5 questions, balisées `FAQPage` mot pour mot |
| Contact | Téléphone en gros + formulaire 5 champs |

## À faire avant mise en ligne

Par ordre d'impact commercial.

### 1. Créer la fiche Google Business — avant tout le reste

Aucune fiche n'existe aujourd'hui, aucun avis nulle part. Pour un artisan local
c'est le premier levier, devant le site. Tant qu'il n'y a pas d'avis réels, la page
n'affiche **aucune note** : rien n'a été inventé.

Dès qu'il y a 5 avis, coller ce bloc dans `index.html` juste après `</ul>` des promesses
du hero, et ajouter `aggregateRating` au JSON-LD :

```html
<p class="hero-note" style="font-size:15px;color:#F0A470;font-weight:600">
  ★ X,X sur Google · N avis
</p>
```

```json
"aggregateRating":{"@type":"AggregateRating","ratingValue":"X.X","reviewCount":"N"}
```

### 2. Adresse e-mail du formulaire

Dans [js/app.js](js/app.js), renseigner :

```js
var CONTACT_EMAIL = 'adresse@exemple.fr';
```

Tant que la chaîne est vide, le formulaire bascule sur un SMS pré-rempli vers le
06 09 71 03 89. Ça marche, mais l'e-mail est plus confortable. Premier envoi :
formsubmit.co renvoie un mail de confirmation à valider une fois.

### 3. Vérifier l'adresse légale

Le flyer indique **80 avenue du Maréchal Foch, 14150 Ouistreham**.
L'annuaire des entreprises donne **22 rue Surcouf, 53500 Ernée** (Mayenne).
Il faut demander à Christopher laquelle est la bonne et, si besoin, mettre à jour
l'adresse à l'INSEE. Le site affiche Ouistreham.

### 4. Coordonnées de l'assurance décennale

La garantie décennale est annoncée sur le site : bande des atouts, FAQ, pied de page et
mentions légales. Il manque les trois informations que l'article L.241-1 du Code des
assurances rend obligatoires sur les devis et factures, et qu'il faut donc aussi porter
ici : **nom de l'assureur, numéro de contrat, couverture géographique**. Le bloc est
signalé en orange dans [mentions-legales.html](mentions-legales.html).

À noter : le code NAF déclaré à l'INSEE reste **43.34Z, travaux de peinture et vitrerie**.
Ça n'empêche pas d'exercer la couverture ni d'être assuré pour, mais un client qui vérifie
le SIREN verra « peinture ». Ça vaut le coup de faire ajouter l'activité de couverture.

### 5. Délai de réponse

Le flyer promet le devis et le déplacement gratuits, pas de délai. Si Christopher
confirme qu'il rappelle sous 24 h, l'ajouter dans le `<title>`, le hero et le
formulaire : c'est un argument qui convertit.

### 6. Photos de chantiers — deux points à confirmer

La section **Réalisations** est en ligne avec 11 photos fournies par Christopher.
Elles venaient de captures d'écran Snapchat : l'interface a été détourée, la photo
couchée redressée, chaque fichier renommé d'après son contenu. Les versions pleine
résolution renommées sont dans `Desktop/Site internet client/Calvados/renommees/`.

**À confirmer avant une mise en ligne sur son domaine :**

1. **Que ces onze chantiers sont bien les siens.** Elles arrivent par Snapchat, rien
   ne le prouve côté site. Une photo qui ne serait pas de lui n'a rien à faire dans
   une section « Réalisations ».
2. **Le décalage entre les photos et le positionnement.** Sept des onze montrent de la
   construction neuve, de la charpente ou du gros œuvre. Le site, lui, est bâti sur
   l'entretien, le démoussage et l'urgence fuite, d'après son flyer. Soit son activité
   réelle est plus large que le flyer ne le dit et il faut élargir le discours du site,
   soit il faut des photos d'entretien et de démoussage pour que les deux concordent.

Les quatre cartes de prestation sont passées en photo, chacune recadrée au gabarit
depuis une photo de la galerie :

| Carte | Source | Ce que montre la photo |
|-------|--------|------------------------|
| Entretien de toiture | `02-pose-tuiles` | Remplacement de tuiles, liteaux et écran apparents |
| Démoussage | `03-travaux-toiture` | Lance en action, brume visible sur les tuiles |
| Réparation & fuite | `04-intervention-toiture` | Deux couvreurs au bord du toit, échelles en place |
| Zinguerie & gouttières | `01-couvreur-echelle` | Gouttière zinc en bas de pente, sous-face et chevrons |

Les alt décrivent ce qui est réellement sur l'image, jamais la prestation nommée par la
carte. La seule qui reste approximative est **Réparation & recherche de fuite** : aucune
photo ne montre une fuite ni une recherche de fuite, celle retenue montre une intervention
sur toiture. C'est la première à remplacer dès qu'il en aura une vraie.

Les fichiers sont `img/presta-*.jpg`, cadrés au ratio 400/260. Pour en changer un, poser
le nouveau fichier au même ratio et changer le `src`.

Pour ajouter une photo à la galerie, la déposer dans `img/chantiers/` (JPEG, 1000 px de
large, qualité 80) et ajouter une `<figure class="chantier">` dans `index.tpl.html`.
Les deux premières tuiles occupent deux colonnes : y mettre les meilleures photos de
couverture. `object-position` se règle par photo si le sujet n'est pas centré.

### 7. Nom de domaine

Le site est en ligne sur **https://znk-v.github.io/home-renovation-14/** — c'est cette
adresse que portent le `canonical`, les balises `og:` et le `sitemap.xml`, pour que
l'aperçu du lien fonctionne quand on l'envoie par WhatsApp ou SMS.

Si Christopher prend un vrai domaine (`home-renovation-14.fr` par exemple), il faut :
1. remplacer l'URL dans `index.tpl.html`, `sitemap.xml` et `robots.txt`, puis `./build.sh` ;
2. ajouter un fichier `CNAME` à la racine du dépôt contenant le domaine ;
3. pointer le DNS chez le registrar vers GitHub Pages.

## Structure

```
index.tpl.html                 source de la page (les SVG y sont des marqueurs)
index.html                     page servie — GÉNÉRÉE, ne pas éditer à la main
build.sh                       régénère les SVG puis reconstruit index.html
css/style.css                  tokens, layout, responsive
js/app.js                      coupe interactive, FAQ, formulaire
fonts/                         Barlow Condensed + Public Sans, auto-hébergées
img/gen_hero.py img/gen_cut.py sources du hero et de la coupe
img/gen_cards.py               sources des 6 illustrations de section
img/_hero.svg   img/_cut.svg   hero et coupe, générés
img/ill-climat.svg ill-autres.svg  les deux illustrations restantes, générées
img/presta-*.jpg               les 4 photos des cartes de prestation
img/logo-mark.png              pictogramme du client, détouré, 720 px
img/logo-mark-360.png          même pictogramme, taille servie
favicon.ico  img/favicon-512.png  img/apple-touch-icon.png
img/hero-toiture.jpg           photo du hero, 1800 px
img/hero-toiture-900.jpg       même photo, servie sous 600 px de large
img/chantiers/                 11 photos de chantiers, 1000 px, JPEG q80 (1,7 Mo au total)
og-image.jpg                   1200×630, aperçu WhatsApp / Messenger
robots.txt  sitemap.xml
mentions-legales.html  politique-confidentialite.html
```

**`index.html` est un fichier généré.** Modifier `index.tpl.html`, puis :

```bash
./build.sh
```

`build.sh` calcule aussi une empreinte du CSS et du JS et l'ajoute à leur URL
(`css/style.css?v=3974c232`). Sans ça, GitHub Pages sert les assets en `max-age=600` :
un visiteur déjà venu reçoit le nouveau HTML avec l'ancienne feuille pendant dix minutes,
et la page s'affiche cassée. L'empreinte change dès que le fichier change, donc le
navigateur ne peut plus jamais associer un HTML neuf à un CSS périmé. **Toujours relancer
`./build.sh` après avoir touché `css/style.css` ou `js/app.js`**, même si le HTML n'a pas
bougé — c'est ce qui met l'empreinte à jour.

Les deux illustrations sont produites par des scripts Python : la géométrie est
calculée, pas dessinée à la main. `gen_cut.py` imprime à l'exécution les positions
des six repères ; si la coupe change, il faut recopier ces pourcentages dans les
`style="left:…;top:…"` des boutons `.hot` de `index.tpl.html`.

## Vérifications passées

- Contrastes : tout le texte ≥ 5,0:1 sur son fond réel (AA à partir de 4,5).
- 375 px : aucun débordement horizontal, repères en pastilles de 44 px, barre d'appel
  sticky, `padding-bottom` du body compensé.
- Coupe interactive : clic et flèches du clavier, `role="tablist"`, `aria-selected`.
- FAQ : hauteur animée mesurée, `aria-expanded`, questions du `FAQPage` identiques
  au texte affiché.
- Formulaire : validation nom + téléphone, repli SMS, écran de confirmation qui
  redonne le numéro.
- Aucune requête réseau vers un tiers au chargement (polices locales, zéro tracker).
- Montage au scroll : les 9 groupes de la coupe apparaissent en cascade sur ~1,2 s,
  déclenchés par un `IntersectionObserver` à 30 % de visibilité. Sans JavaScript,
  ou en `prefers-reduced-motion`, tout s'affiche d'emblée.
- Un seul numéro de téléphone sur toute la page : `tel:+33609710389`.
- Ancres : `scroll-margin-top:96px` sur les sections, sinon l'en-tête collant recouvre
  le haut de la section visée. Les sept liens du menu et ceux du pied de page vérifiés.
- Barre d'appel mobile : une seule ligne de 54 px. Sur deux lignes elle mangeait l'écran
  en s'ajoutant à la barre d'URL du navigateur.
- En-tête : marque non compressible, mention 24h/24 dans le bouton plutôt qu'à côté,
  menu retiré sous 1100 px. Marge mesurée à 42 px au point le plus serré (1105 px), et
  aucun élément comprimé de 1920 à 320 px.
- Palette relevée sur le logo vectoriel, pas sur la photo du flyer : 34 paires
  texte/fond re-testées après le changement, aucune sous AA, minimum 4,91:1.
- Hero photo : contraste calculé dans le pire cas, c'est-à-dire un pixel de photo blanc pur
  sous le voile dégradé. 15,4:1 à gauche où se pose le titre, 5,7:1 au bord droit du bloc
  de texte. AA tenu sur toute la largeur, quelle que soit la zone de l'image dessous.
