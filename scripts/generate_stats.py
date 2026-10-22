#!/usr/bin/env python3
"""Génère stats.svg (tableau de bord du profil) à partir de l'API GitHub.

Toutes les valeurs proviennent de l'API. Si une donnée est indisponible,
un tiret est affiché : rien n'est inventé.

Variables d'environnement :
  GH_USER        nom d'utilisateur (défaut : Samah-boudallaa)
  GITHUB_TOKEN   jeton d'API (fourni par GitHub Actions)
  EXCLUDE_LANGS  langages exclus du calcul, séparés par des virgules
                 (défaut : "Jupyter Notebook", dont le volume vient surtout des sorties).
                 Mettre une chaîne vide pour tout inclure.
  OUT            fichier de sortie (défaut : stats.svg)
"""
import os, json, datetime, urllib.request
from html import escape

USER = os.environ.get("GH_USER", "Samah-boudallaa")
TOKEN = os.environ.get("GITHUB_TOKEN")
OUT = os.environ.get("OUT", "stats.svg")
EXCLUDE = {s.strip() for s in os.environ.get("EXCLUDE_LANGS", "Jupyter Notebook").split(",") if s.strip()}

LANG_COLORS = {"Python": "#3572A5", "Jupyter Notebook": "#DA5B0B", "HTML": "#e34c26", "CSS": "#8b5cf6",
               "JavaScript": "#f1e05a", "C": "#8b949e", "SQL": "#e38c00", "Shell": "#89e051",
               "TypeScript": "#3178c6", "R": "#198CE7", "Dockerfile": "#384d54"}
PALETTE = ["#161b22", "#1f3a6e", "#1f6feb", "#8957e5", "#d2a8ff"]
LEVELS = {"NONE": 0, "FIRST_QUARTER": 1, "SECOND_QUARTER": 2, "THIRD_QUARTER": 3, "FOURTH_QUARTER": 4}


def _req(url, data=None):
    headers = {"Accept": "application/vnd.github+json", "User-Agent": "profile-stats"}
    if TOKEN:
        headers["Authorization"] = f"Bearer {TOKEN}"
    if data is not None:
        headers["Content-Type"] = "application/json"
    with urllib.request.urlopen(urllib.request.Request(url, data=data, headers=headers), timeout=30) as r:
        return json.load(r)


def api(path):
    return _req("https://api.github.com" + path)


def graphql(query, variables):
    out = _req("https://api.github.com/graphql", json.dumps({"query": query, "variables": variables}).encode())
    if out.get("errors"):
        raise RuntimeError(out["errors"])
    return out["data"]


# ---------- Données ----------
repos = [r for r in api(f"/users/{USER}/repos?per_page=100&type=owner") if not r["fork"]]

langs = {}
for r in repos:
    try:
        for name, size in api(f"/repos/{USER}/{r['name']}/languages").items():
            if name not in EXCLUDE:
                langs[name] = langs.get(name, 0) + size
    except Exception as e:
        print("langages indisponibles pour", r["name"], e)
total = sum(langs.values()) or 1
top = sorted(langs.items(), key=lambda x: -x[1])[:5]
recent = sorted(repos, key=lambda r: r.get("pushed_at") or "", reverse=True)[:4]

QUERY = """query($login:String!){user(login:$login){contributionsCollection{contributionCalendar{
totalContributions weeks{contributionDays{date contributionCount contributionLevel}}}}}}"""
cal = None
try:
    cal = graphql(QUERY, {"login": USER})["user"]["contributionsCollection"]["contributionCalendar"]
except Exception as e:
    print("GraphQL indisponible :", e)

weeks, days = [], []
if cal:
    for w in cal["weeks"]:
        wk = [{"date": d["date"], "count": d["contributionCount"], "level": LEVELS.get(d["contributionLevel"], 0)}
              for d in w["contributionDays"]]
        weeks.append(wk)
        days.extend(wk)
    days.sort(key=lambda d: d["date"])


def streaks(ds):
    best = cur = 0
    for d in ds:
        cur = cur + 1 if d["count"] > 0 else 0
        best = max(best, cur)
    seq = ds[:-1] if ds and ds[-1]["count"] == 0 else ds  # la journée en cours peut encore être vide
    now = 0
    for d in reversed(seq):
        if d["count"] > 0:
            now += 1
        else:
            break
    return now, best


cur_streak, best_streak = streaks(days) if cal else (None, None)
active_days = sum(1 for d in days if d["count"] > 0) if cal else None
dash = "–"
fmt = lambda v: dash if v is None else str(v)

kpis = [("DÉPÔTS PUBLICS", len(repos), "#58a6ff"),
        ("CONTRIBUTIONS (12 MOIS)", cal["totalContributions"] if cal else None, "#a371f7"),
        ("JOURS ACTIFS", active_days, "#3fb950"),
        ("LANGAGES", len(langs), "#f0883e")]

now = datetime.datetime.now(datetime.timezone.utc).strftime("%d/%m/%Y")
H = 590

# ---------- SVG ----------
s = [f'<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="{H}" viewBox="0 0 1000 {H}" role="img" aria-label="Tableau de bord GitHub">']
s.append('''<defs><pattern id="g" width="40" height="40" patternUnits="userSpaceOnUse"><path d="M40 0H0V40" fill="none" stroke="#58a6ff" stroke-opacity=".07"/></pattern>
<style>.m{font-family:Consolas,Menlo,"Liberation Mono",monospace}
.k{animation:in .9s both}.b{transform-box:fill-box;transform-origin:left center;animation:grow 1.4s cubic-bezier(.2,.8,.2,1) both}
.c{transform-box:fill-box;transform-origin:center;animation:pop .5s both}.live{animation:p 1.6s infinite}
@keyframes in{from{opacity:0;transform:translateY(12px)}to{opacity:1;transform:none}}
@keyframes grow{from{transform:scaleX(0)}to{transform:scaleX(1)}}
@keyframes pop{from{opacity:0;transform:scale(.3)}to{opacity:1;transform:none}}
@keyframes p{50%{opacity:.25}}
@media (prefers-reduced-motion:reduce){.k,.b,.c,.live{animation:none}}</style></defs>''')
s.append(f'<rect width="1000" height="{H}" rx="16" fill="#0d1117"/><rect width="1000" height="{H}" rx="16" fill="url(#g)"/>')
s.append(f'<circle class="live" cx="34" cy="34" r="5" fill="#3fb950"/>'
         f'<text x="50" y="39" class="m" font-size="13" fill="#8b949e">LIVE · tableau de bord généré par pipeline · @{escape(USER)} · maj {now}</text>')

for i, (label, val, col) in enumerate(kpis):
    x = 30 + i * 238
    s.append(f'<g class="k" style="animation-delay:{i*.15:.2f}s"><rect x="{x}" y="60" width="222" height="86" rx="12" fill="#161b22" stroke="{col}" stroke-opacity=".6"/>'
             f'<text x="{x+20}" y="92" class="m" font-size="12" fill="#8b949e" letter-spacing="1">{label}</text>'
             f'<text x="{x+20}" y="130" class="m" font-size="36" font-weight="700" fill="{col}">{fmt(val)}</text></g>')

# Calendrier de contributions
s.append('<text x="30" y="176" class="m" font-size="14" fill="#c9d1d9" font-weight="700">CALENDRIER DE CONTRIBUTIONS (12 DERNIERS MOIS)</text>')
X0, Y0, STEP, SIZE = 30, 192, 14, 12
if weeks:
    for wi, wk in enumerate(weeks):
        for d in wk:
            dt = datetime.date.fromisoformat(d["date"])
            row = (dt.weekday() + 1) % 7  # dimanche = 0
            tip = f'{d["count"]} contribution(s) le {d["date"]}'
            s.append(f'<rect class="c" x="{X0+wi*STEP}" y="{Y0+row*STEP}" width="{SIZE}" height="{SIZE}" rx="3" '
                     f'fill="{PALETTE[d["level"]]}" style="animation-delay:{wi*0.03:.2f}s"><title>{escape(tip)}</title></rect>')
else:
    for wi in range(53):
        for row in range(7):
            s.append(f'<rect x="{X0+wi*STEP}" y="{Y0+row*STEP}" width="{SIZE}" height="{SIZE}" rx="3" fill="{PALETTE[0]}"/>')
    s.append('<text x="401" y="248" text-anchor="middle" class="m" font-size="13" fill="#8b949e">En attente de la première exécution du workflow</text>')

s.append('<text x="640" y="310" class="m" font-size="11" fill="#6e7681">Moins</text>')
for i, c in enumerate(PALETTE):
    s.append(f'<rect x="{680+i*16}" y="301" width="12" height="12" rx="3" fill="{c}"/>')
s.append('<text x="768" y="310" class="m" font-size="11" fill="#6e7681">Plus</text>')

s.append(f'<text x="805" y="212" class="m" font-size="11" fill="#8b949e" letter-spacing="1">SÉRIE ACTUELLE</text>'
         f'<text x="805" y="244" class="m" font-size="26" font-weight="700" fill="#58a6ff">{fmt(cur_streak)}{" j" if cur_streak is not None else ""}</text>'
         f'<text x="805" y="274" class="m" font-size="11" fill="#8b949e" letter-spacing="1">SÉRIE MAXIMALE</text>'
         f'<text x="805" y="306" class="m" font-size="26" font-weight="700" fill="#a371f7">{fmt(best_streak)}{" j" if best_streak is not None else ""}</text>')

# Langages
s.append('<text x="30" y="352" class="m" font-size="14" fill="#c9d1d9" font-weight="700">LANGAGES (octets de code, dépôts publics)</text>')
for i, (name, v) in enumerate(top):
    y = 372 + i * 32
    pct = v * 100 / total
    w = max(4, 330 * v / top[0][1])
    col = LANG_COLORS.get(name, "#8b949e")
    s.append(f'<g class="k" style="animation-delay:{.4+i*.12:.2f}s"><text x="30" y="{y+14}" class="m" font-size="13" fill="#c9d1d9">{escape(name)}</text>'
             f'<rect x="170" y="{y}" width="330" height="18" rx="9" fill="#21262d"/>'
             f'<rect class="b" x="170" y="{y}" width="{w:.0f}" height="18" rx="9" fill="{col}" style="animation-delay:{.5+i*.12:.2f}s"/>'
             f'<text x="515" y="{y+14}" class="m" font-size="13" fill="#8b949e">{pct:.1f}%</text></g>')

# Dépôts récents
s.append('<text x="620" y="352" class="m" font-size="14" fill="#c9d1d9" font-weight="700">DERNIÈRES ACTIVITÉS</text>')
for i, r in enumerate(recent):
    y = 372 + i * 44
    col = LANG_COLORS.get(r.get("language") or "", "#8b949e")
    date = (r.get("pushed_at") or "")[:10]
    s.append(f'<g class="k" style="animation-delay:{.5+i*.12:.2f}s"><rect x="620" y="{y}" width="350" height="36" rx="8" fill="#161b22"/>'
             f'<circle cx="640" cy="{y+18}" r="6" fill="{col}"/><text x="656" y="{y+23}" class="m" font-size="13" fill="#79c0ff">{escape(r["name"][:30])}</text>'
             f'<text x="955" y="{y+23}" text-anchor="end" class="m" font-size="11" fill="#6e7681">{escape(date)}</text></g>')

note = "Données publiques de l'API GitHub · régénéré chaque jour par GitHub Actions"
if EXCLUDE:
    note += f" · langages exclus du calcul : {', '.join(sorted(EXCLUDE))}"
s.append(f'<text x="500" y="572" text-anchor="middle" class="m" font-size="11" fill="#6e7681">{escape(note)}</text></svg>')

with open(OUT, "w", encoding="utf-8") as f:
    f.write("\n".join(s))
print("OK", OUT, "| dépôts:", len(repos), "| calendrier:", bool(cal), "| langages:", top)
