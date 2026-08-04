#!/bin/sh
# Régénère les illustrations puis injecte les SVG dans index.html.
# À lancer depuis la racine du projet après toute modif de index.tpl.html
# ou des scripts img/gen_*.py.
set -e
python3 img/gen_hero.py
python3 img/gen_cut.py          # imprime les positions des repères de la coupe
python3 - <<'PY'
tpl = open('index.tpl.html').read()
hero = open('img/_hero.svg').read()
cut  = open('img/_cut.svg').read()
out = tpl.replace('<!--HERO_SVG-->', hero).replace('<!--CUT_SVG-->', cut)
assert '<!--HERO_SVG-->' not in out and '<!--CUT_SVG-->' not in out
open('index.html', 'w').write(out)
print('index.html reconstruit')
PY
