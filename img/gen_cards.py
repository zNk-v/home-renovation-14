"""Illustrations de section, style plat, palette de marque.

Chaque visuel est posé sur un fond ardoise-nuit pour peser visuellement comme
une photo. Ils tiennent la place tant qu'il n'y a pas de vraies photos de
chantier — voir README, section « Photos ».
"""

NUIT = '#12253C'
ARD = '#3B6D9E'
ARD_F = '#2A5075'
ARD_C = '#5D93C2'
LISERE = '#A8CBE6'
TUILE = '#E1712C'
TUILE_C = '#F0A470'
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
# 1 · Entretien — une ardoise déposée, le liteau apparaît
# ============================================================
c = ['<g clip-path="url(#cEnt)">', '<defs><clipPath id="cEnt"><rect width="400" height="260"/></clipPath></defs>']
c.append(f'<rect x="-10" y="60" width="420" height="14" fill="{BOIS}" stroke="#7F5A2C" stroke-width="1"/>')
c.append(f'<rect x="-10" y="128" width="420" height="14" fill="{BOIS}" stroke="#7F5A2C" stroke-width="1"/>')
# le trou laissé par l'ardoise déposée : liteau nu et ombre
c.append(f'<rect x="176" y="60" width="38" height="30" fill="#0B1728"/>')
c.append(f'<rect x="176" y="60" width="38" height="14" fill="{BOIS}"/>')
c += rampant(-20, 8, 14, 2, saut=lambda i, j: None)
c += rampant(-20, 76, 14, 2, saut=lambda i, j: 'none' if (i, j) == (6, 0) else None)
c += rampant(-20, 144, 14, 4)
c.append(f'<rect x="-10" y="196" width="420" height="14" fill="{BOIS}" stroke="#7F5A2C" stroke-width="1"/>')
c += rampant(-20, 212, 14, 2)
# l'ardoise déposée, tenue en l'air, en accent
c.append('<g transform="translate(238 28) rotate(-16) scale(1.5)">')
c.append(ardoise(0, 0, 36, 30, fill=TUILE))
c.append('</g>')
c.append(f'<path d="M232 74 q10 -16 14 -26" stroke="{TUILE_C}" stroke-width="2.4" fill="none" '
         'stroke-dasharray="5 5" stroke-linecap="round"/>')
c.append('</g>')
svg('entretien', 400, 260, c,
    "Pan de toiture en ardoise, une ardoise déposée laissant voir le liteau")

# ============================================================
# 2 · Démoussage — moitié envahie, moitié nettoyée
# ============================================================
c = ['<defs><clipPath id="cDem"><rect width="400" height="260"/></clipPath>'
     f'<linearGradient id="gSale" x1="0" y1="0" x2="1" y2="0">'
     f'<stop offset="0" stop-color="{MOUSSE_F}"/><stop offset="1" stop-color="{MOUSSE}"/></linearGradient></defs>',
     '<g clip-path="url(#cDem)">']
c += rampant(-20, 6, 14, 15)
# voile de mousse sur la moitié gauche
c.append('<g clip-path="url(#cDem)" opacity=".92">')
c.append(f'<path d="M0 0 L186 0 L150 260 L0 260 Z" fill="url(#gSale)" fill-opacity=".55"/>')
c.append('</g>')
import random
random.seed(4)
c.append('<g>')
for k in range(78):
    x = random.uniform(-6, 178)
    y = random.uniform(0, 258)
    if x > 186 - (36 / 260) * y:
        continue
    r = random.uniform(3.5, 11)
    c.append(f'<ellipse cx="{x:.0f}" cy="{y:.0f}" rx="{r:.1f}" ry="{r*0.62:.1f}" '
             f'fill="{MOUSSE}" fill-opacity="{random.uniform(.35,.8):.2f}"/>')
c.append('</g>')
# la limite de nettoyage
c.append(f'<path d="M186 -4 L150 264" stroke="{TUILE}" stroke-width="3.5" stroke-linecap="round"/>')
c.append('</g>')
svg('demoussage', 400, 260, c,
    "Toiture en ardoise, moitié gauche envahie de mousse, moitié droite nettoyée")

# ============================================================
# 3 · Fuite — le trajet de l'eau, du toit au plafond
# ============================================================
c = ['<defs><clipPath id="cFui"><rect width="400" height="260"/></clipPath></defs>',
     '<g clip-path="url(#cFui)">']
c += rampant(-20, 4, 14, 2)
# l'ardoise fendue
c.append('<g>')
c.append(ardoise(160, 21, 36, 30, fill=ARD_F))
c.append(f'<path d="M176 24 l-5 12 l7 5 l-4 9" stroke="{TUILE}" stroke-width="2.4" fill="none" stroke-linecap="round"/>')
c.append('</g>')
# charpente + isolant
c.append(f'<rect x="-10" y="72" width="420" height="9" fill="#B9CEDD"/>')
c.append(f'<rect x="-10" y="81" width="420" height="46" fill="{TUILE}" fill-opacity=".13"/>')
c.append('<g stroke="#F5B98C" stroke-opacity=".45" stroke-width="2">')
for x in range(-40, 440, 16):
    c.append(f'<line x1="{x}" y1="81" x2="{x-46}" y2="127"/>')
c.append('</g>')
for cx in (48, 236, 330):
    c.append(f'<rect x="{cx}" y="81" width="18" height="46" fill="{BOIS}" stroke="#4E3415" stroke-width="1.6"/>')
c.append(f'<rect x="-10" y="127" width="420" height="12" fill="{PLATRE}"/>')
# la tache au plafond, décalée par rapport à l'ardoise fendue
c.append(f'<ellipse cx="252" cy="139" rx="52" ry="13" fill="#8A6A46" fill-opacity=".8"/>')
c.append(f'<ellipse cx="252" cy="139" rx="30" ry="7.5" fill="#6B4E30" fill-opacity=".9"/>')
# le trajet de l'eau
c.append(f'<path d="M178 52 L178 76 Q178 96 210 104 Q244 112 250 136" stroke="{TUILE_C}" '
         'stroke-width="2.6" fill="none" stroke-dasharray="6 5" stroke-linecap="round"/>')
c.append(f'<path d="M252 152 q7 12 0 17 q-7 -5 0 -17 z" fill="{ZINC_C}"/>')
c.append(f'<path d="M252 196 q6 10 0 14 q-6 -4 0 -14 z" fill="{ZINC_C}" fill-opacity=".55"/>')
c.append('</g>')
svg('fuite', 400, 260, c,
    "Coupe montrant le trajet d'une infiltration, d'une ardoise fendue jusqu'à la tache au plafond")

# ============================================================
# 4 · Zinguerie — gouttière, crochet, descente
# ============================================================
c = ['<defs><clipPath id="cZin"><rect width="400" height="260"/></clipPath></defs>',
     '<g clip-path="url(#cZin)">']
c += rampant(-20, -14, 14, 3, pas_y=17)
c.append(f'<rect x="-10" y="44" width="420" height="13" fill="#6A5340" stroke="#3D2E22" stroke-width="1.4"/>')
# gouttière demi-ronde
c.append(f'<path d="M-10 60 h420 v14 a24 24 0 0 1 -24 24 h-372 a24 24 0 0 1 -24 -24 z" fill="{ZINC}"/>')
c.append(f'<path d="M-10 62 h420" stroke="{ZINC_C}" stroke-width="4"/>')
c.append(f'<path d="M-10 74 a24 24 0 0 0 24 24 h372 a24 24 0 0 0 24 -24" fill="none" '
         f'stroke="#61707C" stroke-width="2"/>')
# crochets
for hx in (60, 200, 340):
    c.append(f'<path d="M{hx} 52 v10 a26 26 0 0 0 26 26" fill="none" stroke="{TUILE}" stroke-width="5" '
             'stroke-linecap="round"/>')
# descente
c.append(f'<path d="M262 96 q0 22 -22 26 h-8" fill="none" stroke="{ZINC}" stroke-width="17" stroke-linecap="round"/>')
c.append(f'<rect x="-10" y="98" width="420" height="172" fill="#1B3350"/>')
c.append('<g stroke="#12253C" stroke-width="2.5">')
for _yy in (128, 160, 192, 224, 256):
    c.append(f'<line x1="-10" y1="{_yy}" x2="410" y2="{_yy}"/>')
for _r, _y in enumerate((113, 145, 177, 209, 241)):
    for _x in range(-10 + (34 if _r % 2 else 0), 410, 68):
        c.append(f'<line x1="{_x}" y1="{_y - 15}" x2="{_x}" y2="{_y + 17}"/>')
c.append('</g>')
c.append(f'<rect x="216" y="112" width="19" height="150" rx="3" fill="{ZINC}"/>')
c.append(f'<rect x="219" y="112" width="5" height="150" fill="{ZINC_C}" fill-opacity=".55"/>')
c.append(f'<rect x="210" y="176" width="31" height="11" rx="2" fill="#61707C"/>')
c.append('</g>')
svg('zinguerie', 400, 260, c,
    "Détail de zinguerie : gouttière zinc demi-ronde, crochets et descente d'eau pluviale")

# ============================================================
# 5 · Climat — la côte, le vent, le phare (bandeau large)
# ============================================================
W, H = 1000, 300
c = [f'<defs><clipPath id="cCli"><rect width="{W}" height="{H}"/></clipPath>'
     f'<linearGradient id="gCiel" x1="0" y1="0" x2="0" y2="1">'
     f'<stop offset="0" stop-color="#16304E"/><stop offset="1" stop-color="{NUIT}"/></linearGradient></defs>',
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
c.append(f'<rect x="146" y="104" width="104" height="34" rx="17" fill="none" stroke="#8C3C0C" stroke-width="2.5"/>')
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
c.append(f'<rect x="-10" y="214" width="420" height="60" fill="#0E1F35"/>')
c.append(f'<path d="M-10 224 q70 -16 140 -2 q70 14 140 -2 q70 -16 140 4 v50 h-420 z" fill="{ZINC}" fill-opacity=".45"/>')
c.append(f'<path d="M34 232 h96 l-10 26 h-76 z" fill="{ARD_F}"/>')
c.append(f'<path d="M44 236 h76 l-6 15 h-64 z" fill="{TUILE}" fill-opacity=".85"/>')
c.append('</g>')
svg('autres', 400, 260, c,
    "Chantier intérieur : cloison en plaques de plâtre, bande de peinture fraîche, rouleau et bac")

print("illustrations écrites : entretien, demoussage, fuite, zinguerie, climat, autres")
