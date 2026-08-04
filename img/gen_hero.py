def lerp(a, b, t):
    return (a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t)

def f(v):
    return f"{v:.1f}".rstrip('0').rstrip('.')

def P(v):
    return f"{f(v[0])} {f(v[1])}"

# --- plan de toiture en perspective 3/4 ---
RL = (150, 168)   # faîtage gauche
RR = (474, 208)   # faîtage droit
EL = (18, 330)    # égout gauche
ER = (418, 382)   # égout droit

def pt(u, t):
    """u = le long du faîtage (0 gauche → 1 droite) ; t = du faîtage vers l'égout."""
    return lerp(lerp(RL, RR, u), lerp(EL, ER, u), t)

s = []
s.append('<svg class="art-hero" viewBox="0 0 560 440" role="img" aria-labelledby="heroArtT" xmlns="http://www.w3.org/2000/svg">')
s.append('<title id="heroArtT">Toiture en ardoise avec fenêtre de toit, souche de cheminée et gouttière zinc, le phare de Ouistreham au fond</title>')
s.append('<defs>')
s.append('<linearGradient id="gSlope" x1=".15" y1="0" x2=".55" y2="1">'
         '<stop offset="0" stop-color="#31608F"/><stop offset="1" stop-color="#1C3B5F"/></linearGradient>')
s.append('<linearGradient id="gWall" x1="0" y1="0" x2="0" y2="1">'
         '<stop offset="0" stop-color="#15304E"/><stop offset="1" stop-color="#102640"/></linearGradient>')
s.append('<linearGradient id="gBeam" x1="1" y1="0" x2="0" y2="0">'
         '<stop offset="0" stop-color="#F0A470" stop-opacity=".30"/>'
         '<stop offset="1" stop-color="#F0A470" stop-opacity="0"/></linearGradient>')
s.append('</defs>')

# ---------- fond ----------
s.append('<line x1="0" y1="286" x2="560" y2="286" stroke="#ffffff" stroke-opacity=".13"/>')
s.append('<g stroke="#ffffff" stroke-opacity=".06" stroke-linecap="round" stroke-width="2">')
for i, y in enumerate((297, 308, 319)):
    x0 = 10 + i * 34
    s.append(f'<line x1="{x0}" y1="{y}" x2="{x0+58}" y2="{y}"/>')
    s.append(f'<line x1="{x0+92}" y1="{y}" x2="{x0+140}" y2="{y}"/>')
s.append('</g>')

# rafales de vent
s.append('<g stroke="#8FB3D2" stroke-opacity=".2" stroke-width="2" stroke-linecap="round">')
for x, y, w in ((22, 52, 92), (52, 74, 128), (14, 96, 66)):
    s.append(f'<path d="M{x} {y} h{w}"/>')
s.append('</g>')

# mouettes
s.append('<g fill="none" stroke="#C8DAE9" stroke-opacity=".45" stroke-width="2.2" stroke-linecap="round">')
s.append('<path d="M238 74 q9 -9 18 0 q9 -9 18 0"/>')
s.append('<path d="M300 46 q6.5 -6.5 13 0 q6.5 -6.5 13 0"/>')
s.append('</g>')

# toits lointains (gauche)
s.append('<g fill="#1D3F65">')
s.append('<path d="M0 286 L0 258 L28 234 L56 258 L56 286 Z"/>')
s.append('<path d="M62 286 L62 250 L92 224 L122 250 L122 286 Z"/>')
s.append('</g>')

# phare de Ouistreham (droite)
s.append('<g>')
s.append('<path d="M504 286 L516 166 L530 166 L540 286 Z" fill="#22456B"/>')
s.append('<rect x="512" y="157" width="22" height="10" fill="#22456B"/>')
s.append('<rect x="517" y="136" width="12" height="21" fill="#2C5480"/>')
s.append('<rect x="517" y="141" width="12" height="7" fill="#E1712C" fill-opacity=".9"/>')
s.append('</g>')

# ---------- façade sous l'égout ----------
s.append(f'<path d="M{P(EL)} L{P(ER)} L418 440 L18 440 Z" fill="url(#gWall)"/>')
for wx, wt in ((0.14, 0), (0.42, 0), (0.70, 0)):
    a = lerp(EL, ER, wx)
    s.append(f'<rect x="{f(a[0])}" y="{f(a[1]+26)}" width="46" height="52" rx="2" fill="#0B1B2E"/>')
    s.append(f'<path d="M{f(a[0]+23)} {f(a[1]+26)} v52 M{f(a[0])} {f(a[1]+52)} h46" '
             'stroke="#3E6E9C" stroke-opacity=".45" stroke-width="1.6"/>')

# ---------- pan de toiture ----------
s.append(f'<path d="M{P(EL)} L{P(RL)} L{P(RR)} L{P(ER)} Z" fill="url(#gSlope)"/>')

# joints d'ardoises décalés d'un rang à l'autre
NC, NJ = 9, 11
s.append('<g stroke="#8FB6D6" stroke-opacity=".09" stroke-width="1">')
for k in range(NC):
    t0, t1 = k / NC, (k + 1) / NC
    off = 0.5 / NJ if k % 2 else 0.0
    for j in range(NJ + 1):
        u = j / NJ + off
        if u <= 0.004 or u >= 0.996:
            continue
        s.append(f'<line x1="{f(pt(u,t0)[0])}" y1="{f(pt(u,t0)[1])}" '
                 f'x2="{f(pt(u,t1)[0])}" y2="{f(pt(u,t1)[1])}"/>')
s.append('</g>')

# rangs
s.append('<g stroke="#9CC2E0" stroke-opacity=".36" stroke-width="1.3">')
for k in range(1, NC):
    t = k / NC
    s.append(f'<line x1="{f(pt(0,t)[0])}" y1="{f(pt(0,t)[1])}" '
             f'x2="{f(pt(1,t)[0])}" y2="{f(pt(1,t)[1])}"/>')
s.append('</g>')

# ---------- fenêtre de toit ----------
vu0, vu1, vt0, vt1 = 0.20, 0.345, 0.30, 0.62
s.append(f'<path d="M{P(pt(vu0,vt0))} L{P(pt(vu1,vt0))} L{P(pt(vu1,vt1))} L{P(pt(vu0,vt1))} Z" '
         'fill="#0C1D31" stroke="#93A3B1" stroke-width="3.5" stroke-linejoin="round"/>')
s.append(f'<path d="M{P(pt((vu0+vu1)/2,vt0))} L{P(pt((vu0+vu1)/2,vt1))}" '
         'stroke="#4C7BA6" stroke-opacity=".5" stroke-width="2"/>')

# ---------- souche de cheminée ----------
# Prisme vertical posé sur le rampant : les 4 points de base suivent la pente,
# les 4 points du sommet sont la même empreinte remontée d'une hauteur constante.
cu0, cu1, ct0, ct1 = 0.605, 0.715, 0.135, 0.245
H = 58
b_hl, b_hr = pt(cu0, ct0), pt(cu1, ct0)     # arête amont (côté faîtage)
b_ll, b_lr = pt(cu0, ct1), pt(cu1, ct1)     # arête aval (côté égout)
def up(p, h=H): return (p[0], p[1] - h)
t_hl, t_hr, t_ll, t_lr = up(b_hl), up(b_hr), up(b_ll), up(b_lr)

s.append('<g>')
# face aval (celle qu'on voit de face)
s.append(f'<path d="M{P(b_ll)} L{P(b_lr)} L{P(t_lr)} L{P(t_ll)} Z" fill="#173350"/>')
# face latérale droite
s.append(f'<path d="M{P(b_lr)} L{P(b_hr)} L{P(t_hr)} L{P(t_lr)} Z" fill="#0F2740"/>')
# couronnement : l'empreinte au sommet, légèrement débordante
cx = sum(p[0] for p in (t_hl, t_hr, t_ll, t_lr)) / 4
cy = sum(p[1] for p in (t_hl, t_hr, t_ll, t_lr)) / 4
def flare(p, k=1.16): return (cx + (p[0] - cx) * k, cy + (p[1] - cy) * k)
s.append(f'<path d="M{P(flare(t_ll))} L{P(flare(t_lr))} L{P(flare(t_hr))} L{P(flare(t_hl))} Z" fill="#2A4E75"/>')
# mitrons, posés sur le couronnement
s.append(f'<rect x="{f(cx-16)}" y="{f(cy-19)}" width="13" height="17" rx="1" fill="#93A3B1"/>')
s.append(f'<rect x="{f(cx+3)}" y="{f(cy-22)}" width="13" height="17" rx="1" fill="#93A3B1"/>')
s.append('</g>')

# ---------- faîtage, rive, gouttière ----------
s.append(f'<path d="M{P(RL)} L{P(RR)}" stroke="#E1712C" stroke-width="7" stroke-linecap="round"/>')
s.append(f'<path d="M{P(EL)} L{P(RL)}" stroke="#0E2138" stroke-width="5" stroke-linecap="round"/>')
s.append(f'<path d="M{P(RR)} L{P(ER)}" stroke="#0E2138" stroke-width="5" stroke-linecap="round"/>')
s.append(f'<path d="M{P(EL)} L{P(ER)}" stroke="#93A3B1" stroke-width="9" stroke-linecap="round"/>')
s.append(f'<path d="M{f(EL[0])} {f(EL[1]+7.5)} L{f(ER[0])} {f(ER[1]+7.5)}" '
         'stroke="#5E7284" stroke-width="4" stroke-linecap="round"/>')
# descente
s.append(f'<path d="M{f(ER[0]-3)} {f(ER[1]+4)} L{f(ER[0]-3)} 440" stroke="#6E8091" stroke-width="7" stroke-linecap="round"/>')

s.append('</svg>')

open('img/_hero.svg', 'w').write('\n'.join(s))
print("hero ok", len('\n'.join(s)))
