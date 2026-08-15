#!/bin/sh
# Régénère les illustrations puis injecte les SVG dans index.html.
# À lancer depuis la racine du projet après toute modif de index.tpl.html,
# de css/style.css, de js/app.js ou des scripts img/gen_*.py.
set -e
python3 img/gen_hero.py
python3 img/gen_cut.py          # imprime les positions des repères de la coupe
python3 img/gen_cards.py
python3 - <<'PY'
import hashlib, re, pathlib

def empreinte(chemin):
    return hashlib.md5(pathlib.Path(chemin).read_bytes()).hexdigest()[:8]

vcss, vjs = empreinte('css/style.css'), empreinte('js/app.js')

tpl = pathlib.Path('index.tpl.html').read_text()
hero = pathlib.Path('img/_hero.svg').read_text()
cut  = pathlib.Path('img/_cut.svg').read_text()
out = tpl.replace('<!--HERO_SVG-->', hero).replace('<!--CUT_SVG-->', cut)
assert '<!--HERO_SVG-->' not in out and '<!--CUT_SVG-->' not in out

# GitHub Pages sert les assets en max-age=600. Sans empreinte dans l'URL, un
# visiteur déjà venu reçoit le nouveau HTML avec l'ancienne feuille pendant dix
# minutes — l'en-tête s'effondre. L'empreinte change dès que le fichier change.
out = re.sub(r'(href="css/style\.css)(\?v=[0-9a-f]+)?"', rf'\1?v={vcss}"', out)
out = re.sub(r'(src="js/app\.js)(\?v=[0-9a-f]+)?"',      rf'\1?v={vjs}"',  out)
pathlib.Path('index.html').write_text(out)

# les pages légales chargent la même feuille
for p in ('mentions-legales.html', 'politique-confidentialite.html'):
    f = pathlib.Path(p)
    f.write_text(re.sub(r'(href="css/style\.css)(\?v=[0-9a-f]+)?"', rf'\1?v={vcss}"', f.read_text()))

print(f'index.html reconstruit — css v={vcss}, js v={vjs}')
PY
