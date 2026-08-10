"""Illustrations de section, style plat, palette de marque.

Il n'en reste que deux : le bandeau du littoral et le chantier intérieur. Les quatre
illustrations des cartes de prestation ont été remplacées par des photos réelles de
Christopher (img/presta-*.jpg) — une photo de son chantier vaut mieux qu'un schéma
dès qu'elle existe. Leur code est dans l'historique git si besoin.
"""

NUIT = '#081F41'
ARD = '#3B6D9E'
ARD_F = '#2A5075'
ARD_C = '#5D93C2'
LISERE = '#A8CBE6'
TUILE = '#F26205'
TUILE_C = '#FBA36A'
BOIS = '#C9924F'
ZINC = '#8C9AA6'
ZINC_C = '#CBD5DD'
MOUSSE = '#6E8A4C'
MOUSSE_F = '#4E6636'
PLATRE = '#DCD6CB'


def ardoise(x, y, w=36, h=30, fill=ARD, op=1):
    """Une ardoise : rectangle à bord bas arrondi."""
    r = w / 2
    return (f'<path d="M{x} {y} h{w} v{h - r} a{r} {r} 0 0 1 -{w} 0 z" '
            f'fill="{fill}" fill-opacity="{op}" stroke="{LISERE}" stroke-opacity=".45" stroke-width="1.2"/>')


def rampant(x0, y0, cols, rows, pas_x=34, pas_y=17, fill=ARD, saut=None):
    """Un pan d'ardoises en rangs décalés. saut(i,j) -> couleur ou None."""
    out = []
    for j in range(rows):
        dec = (pas_x / 2) if j % 2 else 0
        for i in range(cols):
            x = x0 + i * pas_x - dec
            y = y0 + j * pas_y
            c = saut(i, j) if saut else None
            out.append(ardoise(x, y, fill=c or fill))
    return out


def svg(nom, w, h, corps, titre):
    s = [f'<svg class="ill" viewBox="0 0 {w} {h}" role="img" aria-labelledby="t{nom}" '
         f'xmlns="http://www.w3.org/2000/svg">',
         f'<title id="t{nom}">{titre}</title>',
         f'<rect width="{w}" height="{h}" fill="{NUIT}"/>']
    s += corps
    s.append('</svg>')
    open(f'img/ill-{nom}.svg', 'w').write('\n'.join(s))
    return nom


# ============================================================
# 5 · Climat — la côte, le vent, le phare (bandeau large)
# ============================================================
W, H = 1000, 300
c = [f'<defs><clipPath id="cCli"><rect width="{W}" height="{H}"/></clipPath>'
     f'<linearGradient id="gCiel" x1="0" y1="0" x2="0" y2="1">'
     f'<stop offset="0" stop-color="#0B2853"/><stop offset="1" stop-color="{NUIT}"/></linearGradient></defs>',
     '<g clip-path="url(#cCli)">',
     f'<rect width="{W}" height="{H}" fill="url(#gCiel)"/>']
# rafales
c.append(f'<g stroke="{ARD_C}" stroke-opacity=".28" stroke-width="2.5" stroke-linecap="round" fill="none">')
for x, y, w2 in ((40, 44, 150), (110, 70, 210), (24, 96, 108), (300, 38, 170), (420, 84, 130), (700, 56, 190)):
    c.append(f'<path d="M{x} {y} q{w2/2} -9 {w2} 0"/>')
c.append('</g>')
# horizon + mer
c.append(f'<line x1="0" y1="176" x2="{W}" y2="176" stroke="#ffffff" stroke-opacity=".13" stroke-width="1.5"/>')
c.append(f'<g stroke="#ffffff" stroke-opacity=".07" stroke-width="2" stroke-linecap="round">')
for i, y in enumerate((188, 200, 212)):
    for x in range(20 + i * 40, W, 190):
        c.append(f'<line x1="{x}" y1="{y}" x2="{x+70}" y2="{y}"/>')
c.append('</g>')
# phare
c.append(f'<path d="M846 176 L858 58 L874 58 L886 176 Z" fill="#22456B"/>')
c.append(f'<rect x="853" y="48" width="26" height="11" fill="#22456B"/>')
c.append(f'<rect x="859" y="25" width="14" height="23" fill="{ARD_F}"/>')
c.append(f'<rect x="859" y="30" width="14" height="8" fill="{TUILE}" fill-opacity=".9"/>')
# mouettes
c.append(f'<g fill="none" stroke="#C8DAE9" stroke-opacity=".45" stroke-width="2.4" stroke-linecap="round">')
c.append('<path d="M560 62 q10 -10 20 0 q10 -10 20 0"/><path d="M632 38 q7 -7 14 0 q7 -7 14 0"/>')
c.append('</g>')
# rangée de maisons : pignon + rampant d'ardoises
import math
maisons = [(-30, 196, 210, 92), (170, 176, 250, 112), (400, 190, 190, 98),
           (570, 168, 260, 120), (790, 194, 200, 94), (950, 182, 190, 106)]
for i, (mx, my, mw, mh) in enumerate(maisons):
    faite = my - mh * 0.30
    # souche de cheminée, posée avant le rampant pour rester derrière le faîtage
    _cx = mx + mw * 0.72
    c.append(f'<rect x="{_cx:.0f}" y="{faite - 34:.0f}" width="22" height="{my - faite + 34:.0f}" fill="#1B3350"/>')
    c.append(f'<rect x="{_cx - 4:.0f}" y="{faite - 40:.0f}" width="30" height="9" fill="{ZINC}" fill-opacity=".8"/>')
    c.append(f'<path d="M{mx} {my} L{mx + mw/2} {faite} L{mx + mw} {my} Z" fill="{ARD_F if i % 2 else ARD}"/>')
    # rangs
    n = 6
    for k in range(1, n):
        t = k / n
        x1 = mx + (mw / 2) * t
        x2 = mx + mw - (mw / 2) * t
        y = faite + (my - faite) * t
        c.append(f'<line x1="{x1:.0f}" y1="{y:.0f}" x2="{x2:.0f}" y2="{y:.0f}" '
                 f'stroke="{LISERE}" stroke-opacity=".22" stroke-width="1.4"/>')
    c.append(f'<path d="M{mx} {my} L{mx + mw/2} {faite} L{mx + mw} {my}" fill="none" '
             f'stroke="{TUILE if i % 2 == 0 else ZINC}" stroke-opacity=".85" stroke-width="4" stroke-linejoin="round"/>')
    c.append(f'<rect x="{mx}" y="{my}" width="{mw}" height="{H - my}" fill="{"#243B52" if i % 2 else "#2B4358"}"/>')
    c.append(f'<rect x="{mx}" y="{my}" width="{mw}" height="5" fill="{ZINC}" fill-opacity=".7"/>')
    for wx in range(int(mx + 34), int(mx + mw - 40), 74):
        c.append(f'<rect x="{wx - 4}" y="{my + 26}" width="42" height="50" rx="2" fill="#16293D"/>')
        c.append(f'<rect x="{wx}" y="{my + 30}" width="34" height="42" rx="2" fill="#0B1A2A"/>')
        c.append(f'<path d="M{wx + 17} {my + 30} v42 M{wx} {my + 51} h34" stroke="{ARD_C}" '
                 'stroke-opacity=".3" stroke-width="1.4"/>')
c.append('</g>')
svg('climat', W, H, c,
    "Rangée de maisons normandes à toiture d'ardoise face à la Manche, vent et embruns, le phare au fond")

# ============================================================
# 6 · Autres travaux — mur, rouleau, bac
# ============================================================
c = ['<defs><clipPath id="cAut"><rect width="400" height="260"/></clipPath></defs>',
     '<g clip-path="url(#cAut)">']
c.append(f'<rect x="-10" y="-10" width="420" height="232" fill="{PLATRE}"/>')
# joints de plaques de plâtre
c.append('<g stroke="#BFB8AA" stroke-width="2.5">')
c.append('<line x1="128" y1="-10" x2="128" y2="222"/><line x1="286" y1="-10" x2="286" y2="222"/>')
c.append('<line x1="-10" y1="88" x2="410" y2="88"/>')
c.append('</g>')
c.append('<g fill="#C9C2B4">')
for _x, _y in ((128, 40), (128, 152), (286, 24), (286, 130), (60, 88), (210, 88), (350, 88)):
    c.append(f'<circle cx="{_x}" cy="{_y}" r="3"/>')
c.append('</g>')
# la bande fraîchement peinte : plus claire que le support, bord irrégulier de rouleau
c.append('<path d="M150 -10 h96 v232 h-96 z" fill="#F2F6F9"/>')
c.append('<path d="M150 -10 q6 40 -2 78 q-7 38 3 74 q9 36 -1 80 v-232 z" fill="#E6EDF3"/>')
c.append('<path d="M246 -10 q-7 44 2 84 q8 38 -3 76 q-9 34 1 72 v-232 z" fill="#E6EDF3"/>')
# rouleau : manchon, étrier, manche
c.append(f'<rect x="146" y="104" width="104" height="34" rx="17" fill="{TUILE}"/>')
c.append(f'<rect x="146" y="104" width="104" height="34" rx="17" fill="none" stroke="#9B3B02" stroke-width="2.5"/>')
c.append('<g stroke="#7B8894" stroke-width="2" opacity=".55">')
for _x in range(158, 246, 11):
    c.append(f'<path d="M{_x} 106 v30"/>')
c.append('</g>')
c.append(f'<path d="M250 121 h26 v34" fill="none" stroke="{ZINC}" stroke-width="8" '
         'stroke-linecap="round" stroke-linejoin="round"/>')
c.append(f'<path d="M276 155 L372 244" stroke="{BOIS}" stroke-width="14" stroke-linecap="round"/>')
c.append(f'<path d="M276 155 L372 244" stroke="#8A6031" stroke-width="14" stroke-linecap="round" '
         'stroke-opacity=".25" stroke-dasharray="3 26"/>')
# sol : bâche et bac à peinture
c.append(f'<rect x="-10" y="214" width="420" height="60" fill="#05162F"/>')
c.append(f'<path d="M-10 224 q70 -16 140 -2 q70 14 140 -2 q70 -16 140 4 v50 h-420 z" fill="{ZINC}" fill-opacity=".45"/>')
c.append(f'<path d="M34 232 h96 l-10 26 h-76 z" fill="{ARD_F}"/>')
c.append(f'<path d="M44 236 h76 l-6 15 h-64 z" fill="{TUILE}" fill-opacity=".85"/>')
c.append('</g>')
svg('autres', 400, 260, c,
    "Chantier intérieur : cloison en plaques de plâtre, bande de peinture fraîche, rouleau et bac")

print("illustrations écrites : climat, autres")
