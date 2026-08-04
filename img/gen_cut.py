import math

OX, OY, ANG, L = 96, 384, -31, 540
C, S = math.cos(math.radians(ANG)), math.sin(math.radians(ANG))

# profondeurs, dans le repère du rampant (y croissant = vers l'intérieur)
ARD0, ARD1 = -13.5, 0      # ardoises
LIT1 = 9.5                 # liteaux
ECR1 = 14.5                # écran sous-toiture
ISO1 = 43                  # isolation entre chevrons
PLA1 = 52                  # plaque de plâtre
CHEV = (96, 440)           # abscisses des chevrons coupés

def page(x, y):
    """local (le long du rampant, en profondeur) → coordonnées de la page"""
    return (OX + C * x - S * y, OY + S * x + C * y)

def f(v):
    return f"{v:.1f}".rstrip('0').rstrip('.')

s = []
s.append('<svg class="art-cut" viewBox="0 0 640 480" role="img" aria-labelledby="cutT" xmlns="http://www.w3.org/2000/svg">')
s.append("<title id=\"cutT\">Coupe d'un rampant de toiture en ardoise : couverture, liteaux, écran "
         "sous-toiture, isolation, charpente et gouttière zinc</title>")
s.append(f'<defs><clipPath id="clipIso"><rect x="-6" y="{ECR1}" width="{L+22}" height="{ISO1-ECR1}"/></clipPath></defs>')

s.append(f'<g transform="translate({OX},{OY}) rotate({ANG})">')

# plafond
s.append('<g class="cch" style="--d:0">')
s.append(f'<rect x="-6" y="{ISO1}" width="{L+22}" height="{PLA1-ISO1}" fill="#DCD6CB" stroke="#8E8A80" stroke-width="1"/>')

s.append('</g>')

# isolation : fond teinté + hachures tracées une à une (un <pattern> vire au brun au rendu)
s.append(f'<rect x="-6" y="{ECR1}" width="{L+22}" height="{ISO1-ECR1}" fill="#E1712C" fill-opacity=".13"/>')
s.append('<g class="cch" style="--d:1">')
s.append('<g clip-path="url(#clipIso)" stroke="#F5B98C" stroke-opacity=".6" stroke-width="2">')
hx = -40
while hx < L + 60:
    s.append(f'<line x1="{hx}" y1="{ECR1}" x2="{hx - (ISO1-ECR1)}" y2="{ISO1}"/>')
    hx += 15
s.append('</g>')

s.append('</g>')

# chevrons coupés
s.append('<g class="cch" style="--d:2">')
for cx in CHEV:
    s.append(f'<rect x="{cx}" y="{ECR1}" width="19" height="{ISO1-ECR1}" fill="#C08A4A" stroke="#4E3415" stroke-width="2"/>')
    s.append(f'<path d="M{cx+5} {ECR1+5} q5 9 0 18 M{cx+13} {ECR1+4} q4.5 10 0 20" stroke="#8A6031" stroke-width="1.2" fill="none"/>')

s.append('</g>')

# écran sous-toiture
s.append('<g class="cch" style="--d:3">')
s.append(f'<rect x="-10" y="{LIT1}" width="{L+28}" height="{ECR1-LIT1}" fill="#C3D6E3"/>')

s.append('</g>')

# liteaux
s.append('<g class="cch" style="--d:4">')
lx = 6
while lx < L + 10:
    s.append(f'<rect x="{lx}" y="0" width="12" height="{LIT1}" fill="#C9924F" stroke="#7F5A2C" stroke-width="1"/>')
    lx += 40

s.append('</g>')

# ardoises chevauchantes
s.append('<g class="cch" style="--d:5">')
sx = -14
while sx < L + 4:
    s.append(f'<rect x="{sx}" y="{ARD0}" width="50" height="{ARD1-ARD0}" rx="1.5" '
             'fill="#3B6D9E" stroke="#A8CBE6" stroke-opacity=".95" stroke-width="1.6"/>')
    sx += 40

# faîtière
s.append(f'<path d="M{L+2} {ARD0} q16 -21 32 0 z" fill="#4E80AF" stroke="#A8CBE6" stroke-width="1.6"/>')

s.append('</g>')

# sens d'écoulement
s.append('<g class="cch" style="--d:7" stroke="#8FD0F0" stroke-opacity=".85" stroke-width="2.6" stroke-linecap="round" fill="none">')
s.append('<path d="M348 -26 L266 -26"/><path d="M276 -33 L266 -26 L276 -19"/>')
s.append('</g>')
s.append('</g>')

# ---- planche de rive + gouttière zinc ----
r0, r1 = page(-14, ARD0), page(-14, PLA1)
gx, gy = r1[0] - 34, r1[1] - 4
s.append('<g class="cch" style="--d:6">')
s.append(f'<path d="M{f(r0[0])} {f(r0[1])} L{f(r1[0])} {f(r1[1])} L{f(r1[0]-21)} {f(r1[1]-11)} '
         f'L{f(r0[0]-21)} {f(r0[1]-11)} Z" fill="#6A5340" stroke="#3D2E22" stroke-width="1.4"/>')
s.append(f'<path d="M{f(gx-23)} {f(gy)} a23 23 0 0 0 46 0 z" fill="#8C9AA6"/>')
s.append(f'<path d="M{f(gx-23)} {f(gy)} a23 23 0 0 0 46 0" fill="none" stroke="#CBD5DD" stroke-width="2.8" stroke-linecap="round"/>')
s.append('</g>')

# ---- lignes de rappel ----
# Les pastilles se posent hors de la coupe, sinon elles masquent la couche qu'elles désignent.
# Direction perpendiculaire au rampant, vers l'extérieur puis vers l'intérieur.
NX, NY = -math.sin(math.radians(-ANG)), -math.cos(math.radians(-ANG))   # normale sortante
DIST = 62
reperes = [('Ardoises', 120, (ARD0 + ARD1) / 2, +1),
           ('Liteaux', 220, (ARD1 + LIT1) / 2, -1),
           ('Ecran', 305, (LIT1 + ECR1) / 2, +1),
           ('Isolation', 380, (ECR1 + ISO1) / 2, -1),
           ('Charpente', CHEV[1] + 9.5, (ECR1 + ISO1) / 2, +1)]

marques = []
s.append('<g class="rappels cch" style="--d:8" stroke="#E1712C" stroke-opacity=".65" stroke-width="1.6" stroke-linecap="round">')
for nom, x, y, sens in reperes:
    ax, ay = page(x, y)
    mx, my = ax + sens * DIST * NX, ay + sens * DIST * NY
    s.append(f'<line x1="{f(ax)}" y1="{f(ay)}" x2="{f(mx)}" y2="{f(my)}"/>')
    s.append(f'<circle cx="{f(ax)}" cy="{f(ay)}" r="2.6" fill="#E1712C" stroke="none"/>')
    marques.append((nom, mx, my))
# gouttière : rappel vers le haut-gauche
s.append(f'<line x1="{f(gx)}" y1="{f(gy + 12)}" x2="62" y2="398"/>')
s.append(f'<circle cx="{f(gx)}" cy="{f(gy + 12)}" r="2.6" fill="#E1712C" stroke="none"/>')
marques.append(('Gouttiere', 62, 398))
s.append('</g>')

s.append('</svg>')
open('img/_cut.svg', 'w').write('\n'.join(s))

for nom, mx, my in marques:
    print(f'{nom:10s} left:{mx/640*100:.1f}%  top:{my/480*100:.1f}%')
