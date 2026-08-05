# Home Rénovation 14 — couvreur à Ouistreham

Site one-page pour Christopher Jardin, construit à partir du seul flyer papier.
Angle imposé : **couvreur d'abord**, les autres corps de métier en second plan.

- Direction artistique : [DESIGN.md](DESIGN.md)
- Preview locale : `python3 -m http.server 8143` puis http://localhost:8143

## Ce qui est dans la page

| Section | Contenu |
|---------|---------|
| En-tête | Pictogramme du logo sur pastille claire + nom composé, mention 24h/24, bouton d'appel |
| Hero | Photo de toiture plein cadre, urgence 24h/24, téléphone, trois arguments |
| Atouts | Bande blanche à quatre colonnes juste sous le hero : urgence, fuite, devis, décennale |
| Toiture | 4 prestations, chacune avec son illustration |
| Coupe interactive | 6 repères cliquables sur une coupe de rampant (l'élément signature), **montée couche par couche au scroll** |
| Climat de la côte | Vent d'ouest, air salé, humidité + bandeau littoral — le contenu non transposable |
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
06 58 94 19 08. Ça marche, mais l'e-mail est plus confortable. Premier envoi :
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

### 6. Photos de chantiers

**Le site utilise pour l'instant des illustrations vectorielles, pas des photos.**
Elles sont dessinées dans la palette de la marque et affichées comme illustrations,
jamais présentées comme des chantiers de Christopher. Le bandeau du littoral porte
d'ailleurs la mention « Illustration » en légende.

Elles tiennent la place. Elles ne remplacent pas des photos réelles : sur un site
d'artisan, la photo du vrai chantier est ce qui fait basculer un visiteur.
Il en faut 8 à 10, prises au téléphone, en lumière du jour. Ensuite, coller cette
section entre `#climat` et `#autres` :

```html
<section class="sect" id="realisations">
  <div class="wrap">
    <p class="sur">Réalisations</p>
    <h2>Des chantiers de la côte</h2>
    <div class="grid4" style="margin-top:36px">
      <img src="img/chantier-1.jpg" alt="Démoussage de toiture à Ouistreham" width="600" height="450">
      <!-- … -->
    </div>
  </div>
</section>
```

Photos réelles uniquement. Pas de banque d'images.

Pour remplacer une illustration de carte par une photo, il suffit de changer le `src` :

```html
<img class="presta-ill" src="img/chantier-demoussage.jpg" alt="…" width="400" height="260" loading="lazy">
```

Le gabarit est déjà en 400×260 avec `object-fit: cover`, une photo s'y insère sans
retoucher le CSS.

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
img/ill-*.svg                  illustrations de section, générées
img/logo-mark.png              pictogramme du client, détouré, 720 px
img/logo-mark-360.png          même pictogramme, taille servie
favicon.ico  img/favicon-512.png  img/apple-touch-icon.png
img/hero-toiture.jpg           photo du hero, 1800 px
img/hero-toiture-900.jpg       même photo, servie sous 600 px de large
og-image.jpg                   1200×630, aperçu WhatsApp / Messenger
robots.txt  sitemap.xml
mentions-legales.html  politique-confidentialite.html
```

**`index.html` est un fichier généré.** Modifier `index.tpl.html`, puis :

```bash
./build.sh
```

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
- Un seul numéro de téléphone sur toute la page : `tel:+33658941908`.
- Palette relevée sur le logo vectoriel, pas sur la photo du flyer : 34 paires
  texte/fond re-testées après le changement, aucune sous AA, minimum 4,91:1.
- Hero photo : contraste calculé dans le pire cas, c'est-à-dire un pixel de photo blanc pur
  sous le voile dégradé. 15,4:1 à gauche où se pose le titre, 5,7:1 au bord droit du bloc
  de texte. AA tenu sur toute la largeur, quelle que soit la zone de l'image dessous.
