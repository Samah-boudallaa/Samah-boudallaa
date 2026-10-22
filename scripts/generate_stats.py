#!/usr/bin/env python3
"""Génère stats.svg à partir de l'API GitHub (données réelles, aucune valeur inventée)."""
import os, json, datetime, urllib.request
from html import escape

USER = os.environ.get("GH_USER", "Samah-boudallaa")
TOKEN = os.environ.get("GITHUB_TOKEN")
OUT = os.environ.get("OUT", "stats.svg")
COLORS = {"Python": "#3572A5", "Jupyter Notebook": "#DA5B0B", "HTML": "#e34c26", "CSS": "#8b5cf6",
          "JavaScript": "#f1e05a", "C": "#8b949e", "SQL": "#e38c00", "Shell": "#89e051",
          "TypeScript": "#3178c6", "R": "#198CE7", "Dockerfile": "#384d54"}

def api(path):
    h = {"Accept": "application/vnd.github+json", "User-Agent": "profile-stats"}
    if TOKEN:
        h["Authorization"] = f"Bearer {TOKEN}"
    with urllib.request.urlopen(urllib.request.Request("https://api.github.com" + path, headers=h), timeout=30) as r:
        return json.load(r)

user = api(f"/users/{USER}")
repos = [r for r in api(f"/users/{USER}/repos?per_page=100&type=owner") if not r["fork"]]
stars = sum(r["stargazers_count"] for r in repos)
langs = {}
for r in repos:
    try:
        for k, v in api(f"/repos/{USER}/{r['name']}/languages").items():
            langs[k] = langs.get(k, 0) + v
    except Exception:
        pass
total = sum(langs.values()) or 1
top = sorted(langs.items(), key=lambda x: -x[1])[:5]
try:
    ev = api(f"/users/{USER}/events/public?per_page=100")
except Exception:
    ev = []
commits = sum(len(e["payload"].get("commits", [])) for e in ev if e["type"] == "PushEvent")
recent = sorted(repos, key=lambda r: r["pushed_at"], reverse=True)[:4]
now = datetime.datetime.now(datetime.timezone.utc).strftime("%d/%m/%Y")

kpis = [("DÉPÔTS PUBLICS", len(repos), "#58a6ff"), ("ÉTOILES", stars, "#f0883e"),
        ("ABONNÉS", user["followers"], "#a371f7"), ("COMMITS RÉCENTS", commits, "#3fb950")]
s = []
s.append('<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="400" viewBox="0 0 1000 400" role="img" aria-label="Tableau de bord GitHub">')
s.append('''<defs><pattern id="g" width="40" height="40" patternUnits="userSpaceOnUse"><path d="M40 0H0V40" fill="none" stroke="#58a6ff" stroke-opacity=".07"/></pattern>
<style>.m{font-family:Consolas,Menlo,"Liberation Mono",monospace}.k{animation:in .9s both}.b{transform-box:fill-box;transform-origin:left center;animation:grow 1.4s cubic-bezier(.2,.8,.2,1) both}.live{animation:p 1.6s infinite}
@keyframes in{from{opacity:0;transform:translateY(12px)}to{opacity:1;transform:none}}@keyframes grow{from{transform:scaleX(0)}to{transform:scaleX(1)}}@keyframes p{50%{opacity:.25}}</style></defs>''')
s.append('<rect width="1000" height="400" rx="16" fill="#0d1117"/><rect width="1000" height="400" rx="16" fill="url(#g)"/>')
s.append(f'<circle class="live" cx="34" cy="34" r="5" fill="#3fb950"/><text x="50" y="39" class="m" font-size="13" fill="#8b949e">LIVE · dashboard généré par pipeline · @{escape(USER)} · maj {now}</text>')
for i, (lab, val, col) in enumerate(kpis):
    x = 30 + i * 238
    s.append(f'<g class="k" style="animation-delay:{i*.15}s"><rect x="{x}" y="64" width="222" height="86" rx="12" fill="#161b22" stroke="{col}" stroke-opacity=".6"/>'
             f'<text x="{x+20}" y="96" class="m" font-size="12" fill="#8b949e" letter-spacing="1">{lab}</text>'
             f'<text x="{x+20}" y="134" class="m" font-size="36" font-weight="700" fill="{col}">{val}</text></g>')
s.append('<text x="30" y="188" class="m" font-size="14" fill="#c9d1d9" font-weight="700">LANGAGES (octets de code, dépôts publics)</text>')
for i, (name, v) in enumerate(top):
    y = 208 + i * 34
    pct = v * 100 / total
    w = max(4, 330 * pct / 100 * (100 / max(top[0][1] * 100 / total, 1)))
    col = COLORS.get(name, "#8b949e")
    s.append(f'<g class="k" style="animation-delay:{.4+i*.12}s"><text x="30" y="{y+14}" class="m" font-size="13" fill="#c9d1d9">{escape(name)}</text>'
             f'<rect x="170" y="{y}" width="330" height="18" rx="9" fill="#21262d"/>'
             f'<rect class="b" x="170" y="{y}" width="{w:.0f}" height="18" rx="9" fill="{col}" style="animation-delay:{.5+i*.12}s"/>'
             f'<text x="515" y="{y+14}" class="m" font-size="13" fill="#8b949e">{pct:.1f}%</text></g>')
s.append('<text x="620" y="188" class="m" font-size="14" fill="#c9d1d9" font-weight="700">DERNIÈRES ACTIVITÉS</text>')
for i, r in enumerate(recent):
    y = 208 + i * 44
    col = COLORS.get(r.get("language") or "", "#8b949e")
    s.append(f'<g class="k" style="animation-delay:{.5+i*.12}s"><rect x="620" y="{y}" width="350" height="36" rx="8" fill="#161b22"/>'
             f'<circle cx="640" cy="{y+18}" r="6" fill="{col}"/><text x="656" y="{y+23}" class="m" font-size="13" fill="#79c0ff">{escape(r["name"][:30])}</text>'
             f'<text x="955" y="{y+23}" text-anchor="end" class="m" font-size="11" fill="#6e7681">{escape(r["pushed_at"][:10])}</text></g>')
s.append('<text x="500" y="385" text-anchor="middle" class="m" font-size="11" fill="#6e7681">Données publiques de l\'API GitHub · régénéré chaque jour par GitHub Actions</text></svg>')
open(OUT, "w", encoding="utf-8").write("\n".join(s))
print("OK", OUT, len(repos), stars, user["followers"], commits, top)
