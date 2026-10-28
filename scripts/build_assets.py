#!/usr/bin/env python3
"""Generate the profile graphics (stdlib only, no third-party dependency).

    python scripts/build_assets.py                 # hero + constellation + dashboard
    python scripts/build_assets.py --sample --out /tmp/preview   # synthetic data, watermarked

Dashboard data comes from the GitHub API. With a token (GH_TOKEN / GITHUB_TOKEN)
the GraphQL API supplies the contribution calendar; without one only public REST
data is available and the calendar panel says so. Nothing is ever estimated: a
missing value is rendered as "n/a". If the API fails, an existing dashboard file
is left untouched.
"""
import argparse
import json
import math
import os
import sys
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from design import (BG, BORDER, DIM, MONO, MUTED, PANEL, PANEL_HI, TEXT, VIOLET,  # noqa: E402
                    VIOLET_DEEP, esc, svg_open)
from facts import PROJECTS, STAGES, USER  # noqa: E402

I18N = {
    "en": {
        "tagline": "Reliable data systems, from ingestion to monitoring.",
        "sub": "Data Science student · EST Kelâa des Sraghna, Cadi Ayyad University · Morocco",
        "hero_desc": "Abstract data flow: sources, transformation, model, API and monitoring.",
        "stages": ["INGEST", "TRANSFORM", "MODEL", "SERVE", "OBSERVE"],
        "dash_title": "ENGINEERING TELEMETRY",
        "kpis": ["PUBLIC REPOS", "STARS", "FORKS", "FOLLOWERS", "COMMITS · 12 MO", "PRS · ISSUES"],
        "activity": "WEEKLY CONTRIBUTIONS · LAST 52 WEEKS",
        "repos": "REPOSITORIES · BY LAST PUSH",
        "unavail": "Contribution calendar unavailable (token or API error)",
        "foot": "Public data via GitHub API. Private work is never inferred.",
        "updated": "UPDATED",
        "fork": "fork",
        "peak": "peak",
        "const_title": "ENGINEERING SYSTEMS MAP",
        "const_note": "Static 3D preview. An edge means the capability is documented in the repository.",
        "d_ago": "d ago",
        "today": "today",
    },
    "fr": {
        "tagline": "Des systèmes de données fiables, de l’ingestion à la supervision.",
        "sub": "Étudiante en Data Science · EST Kelâa des Sraghna, Université Cadi Ayyad · Maroc",
        "hero_desc": "Flux de données abstrait : sources, transformation, modèle, API et supervision.",
        "stages": ["INGESTION", "TRANSFORM.", "MODÈLE", "API", "SUPERVISION"],
        "dash_title": "TÉLÉMÉTRIE D’INGÉNIERIE",
        "kpis": ["DÉPÔTS PUBLICS", "ÉTOILES", "FORKS", "ABONNÉS", "COMMITS · 12 MOIS", "PR · ISSUES"],
        "activity": "CONTRIBUTIONS HEBDO · 52 DERNIÈRES SEMAINES",
        "repos": "DÉPÔTS · PAR DERNIER PUSH",
        "unavail": "Calendrier indisponible (jeton ou erreur d’API)",
        "foot": "Données publiques via l’API GitHub. Le travail privé n’est jamais déduit.",
        "updated": "MIS À JOUR",
        "fork": "fork",
        "peak": "pic",
        "const_title": "CARTE DES SYSTÈMES",
        "const_note": "Aperçu 3D statique. Un lien signifie que la capacité est documentée dans le dépôt.",
        "d_ago": "j",
        "today": "aujourd’hui",
    },
}


# ───────────────────────── hero ─────────────────────────
def build_hero(lang):
    t = I18N[lang]
    W, H = 1200, 400
    cy = 205
    xs = [650, 790, 910, 1010, 1110]
    src_y = [105, 155, 205, 255, 305]
    css = (
        ".flow{stroke-dasharray:3 9;animation:fl 2.6s linear infinite}"
        "@keyframes fl{to{stroke-dashoffset:-48}}"
        ".pulse{animation:pu 3s ease-in-out infinite}"
        "@keyframes pu{0%,100%{opacity:.25}50%{opacity:.8}}"
        "@media (prefers-reduced-motion:reduce){.flow,.pulse{animation:none}}"
    )
    o = svg_open(W, H, "Samah Boudallaa — Data Engineering, Machine Learning and AI",
                 t["hero_desc"], css)
    o += (
        "<defs>"
        f'<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{BG}"/>'
        f'<stop offset="1" stop-color="#171230"/></linearGradient>'
        f'<radialGradient id="glow" cx="910" cy="{cy}" r="300" gradientUnits="userSpaceOnUse">'
        f'<stop offset="0" stop-color="{VIOLET_DEEP}" stop-opacity=".34"/>'
        f'<stop offset="1" stop-color="{VIOLET_DEEP}" stop-opacity="0"/></radialGradient>'
        '<pattern id="dots" width="24" height="24" patternUnits="userSpaceOnUse">'
        f'<circle cx="1" cy="1" r="1" fill="{VIOLET}" fill-opacity=".10"/></pattern>'
        "</defs>"
        f'<rect width="{W}" height="{H}" fill="url(#bg)"/>'
        f'<rect width="{W}" height="{H}" fill="url(#dots)"/>'
        f'<rect width="{W}" height="{H}" fill="url(#glow)"/>'
        f'<rect x=".5" y=".5" width="{W-1}" height="{H-1}" fill="none" stroke="{BORDER}"/>'
    )
    # text block
    o += (
        f'<text class="m" x="64" y="118" font-size="14" letter-spacing="3" fill="{VIOLET}">'
        "DATA ENGINEERING · MACHINE LEARNING · AI</text>"
        f'<text x="62" y="190" font-size="62" font-weight="700" fill="{TEXT}" letter-spacing="-1">'
        "Samah Boudallaa</text>"
        f'<text x="64" y="240" font-size="24" fill="{TEXT}" fill-opacity=".9">{esc(t["tagline"])}</text>'
        f'<text x="64" y="282" font-size="15" fill="{MUTED}">{esc(t["sub"])}</text>'
        f'<rect x="64" y="316" width="56" height="3" rx="1.5" fill="{VIOLET}"/>'
    )
    # flows: sources -> transform
    for y in src_y:
        d = f"M{xs[0]} {y} C{xs[0]+70} {y} {xs[1]-80} {cy} {xs[1]-34} {cy}"
        o += f'<path d="{d}" fill="none" stroke="{VIOLET}" stroke-opacity=".55" class="flow"/>'
        o += f'<circle cx="{xs[0]}" cy="{y}" r="4" fill="{VIOLET}"/>'
    # transform node
    x = xs[1]
    o += (f'<rect x="{x-34}" y="{cy-34}" width="68" height="68" rx="10" fill="{PANEL_HI}" '
          f'stroke="{VIOLET}" stroke-opacity=".8"/>')
    for i in range(3):
        o += (f'<line x1="{x-20}" y1="{cy-14+i*14}" x2="{x+20}" y2="{cy-14+i*14}" '
              f'stroke="{VIOLET}" stroke-opacity="{.9-i*.25:.2f}" stroke-width="2"/>')
    # links between nodes
    for a, b in ((xs[1]+34, xs[2]-34), (xs[2]+34, xs[3]-30), (xs[3]+30, xs[4]-34)):
        o += (f'<line x1="{a}" y1="{cy}" x2="{b}" y2="{cy}" stroke="{VIOLET}" '
              'stroke-opacity=".7" class="flow"/>')
    # model hexagon
    x = xs[2]
    pts = " ".join(f"{x+36*math.cos(math.pi/3*i+math.pi/6):.1f},{cy+36*math.sin(math.pi/3*i+math.pi/6):.1f}"
                   for i in range(6))
    o += f'<polygon points="{pts}" fill="{PANEL_HI}" stroke="{VIOLET}" stroke-width="1.5"/>'
    for (dx, dy) in ((-12, -8), (0, 10), (12, -8)):
        o += f'<circle cx="{x+dx}" cy="{cy+dy}" r="3.5" fill="{VIOLET}"/>'
    o += (f'<polyline points="{x-12},{cy-8} {x},{cy+10} {x+12},{cy-8}" fill="none" '
          f'stroke="{VIOLET}" stroke-opacity=".6"/>')
    # API node
    x = xs[3]
    o += (f'<rect x="{x-30}" y="{cy-30}" width="60" height="60" rx="8" fill="{PANEL_HI}" '
          f'stroke="{VIOLET}" stroke-opacity=".8"/>'
          f'<text class="m" x="{x}" y="{cy+6}" font-size="16" text-anchor="middle" fill="{TEXT}">{{ }}</text>')
    # observe node
    x = xs[4]
    o += (f'<circle cx="{x}" cy="{cy}" r="34" fill="{PANEL_HI}" stroke="{VIOLET}" stroke-opacity=".8"/>'
          f'<circle class="pulse" cx="{x}" cy="{cy}" r="42" fill="none" stroke="{VIOLET}"/>'
          f'<polyline points="{x-22},{cy+4} {x-12},{cy+4} {x-6},{cy-14} {x+2},{cy+14} {x+8},{cy} {x+22},{cy}" '
          f'fill="none" stroke="{VIOLET}" stroke-width="2" stroke-linejoin="round"/>')
    # stage labels
    labels_x = [xs[0], xs[1], xs[2], xs[3], xs[4]]
    for lx, lab in zip(labels_x, t["stages"]):
        o += (f'<text class="m" x="{lx}" y="372" font-size="11" letter-spacing="1.5" '
              f'text-anchor="middle" fill="{MUTED}">{esc(lab)}</text>')
    return o + "</svg>\n"


# ───────────────────────── constellation ─────────────────────────
def _project3d(p, rot_y, rot_x, cx, cy, D=950):
    x, y, z = p
    x, z = x*math.cos(rot_y)+z*math.sin(rot_y), -x*math.sin(rot_y)+z*math.cos(rot_y)
    y, z = y*math.cos(rot_x)-z*math.sin(rot_x), y*math.sin(rot_x)+z*math.cos(rot_x)
    s = D/(D+z)
    return cx+x*s, cy+y*s, z, s


def build_constellation(lang):
    t = I18N[lang]
    W, H = 1200, 600
    cx, cy = 600, 292
    ry, rx = 0.55, -0.32
    stage_pos = {}
    n = len(STAGES)
    for i, (key, _) in enumerate(STAGES):
        a = 2*math.pi*i/n + 0.4
        stage_pos[key] = (400*math.cos(a), 70*math.sin(2*a+1) , 250*math.sin(a))
    proj_pos = {"SYSTEM_01": (-150, -70, 40), "SYSTEM_02": (140, -10, -50), "SYSTEM_03": (0, 120, 70)}

    P = {}
    for k, v in stage_pos.items():
        P[("s", k)] = _project3d(v, ry, rx, cx, cy)
    for k, v in proj_pos.items():
        P[("p", k)] = _project3d(v, ry, rx, cx, cy)
    zs = [v[2] for v in P.values()]
    zmin, zmax = min(zs), max(zs)

    def depth(z):  # 0 (far) .. 1 (near)
        return 1-(z-zmin)/((zmax-zmin) or 1)

    o = svg_open(W, H, "Engineering systems map: three projects linked to the engineering stages they implement",
                 "Static 3D constellation. " + t["const_note"])
    o += (
        "<defs>"
        f'<radialGradient id="g" cx="50%" cy="48%" r="60%"><stop offset="0" stop-color="#1c1633"/>'
        f'<stop offset="1" stop-color="{BG}"/></radialGradient>'
        f'<radialGradient id="halo"><stop offset="0" stop-color="{VIOLET}" stop-opacity=".55"/>'
        f'<stop offset="1" stop-color="{VIOLET}" stop-opacity="0"/></radialGradient>'
        "</defs>"
        f'<rect width="{W}" height="{H}" fill="url(#g)"/>'
        f'<rect x=".5" y=".5" width="{W-1}" height="{H-1}" fill="none" stroke="{BORDER}"/>'
        f'<text class="m" x="40" y="48" font-size="13" letter-spacing="3" fill="{VIOLET}">{esc(t["const_title"])}</text>'
    )
    # orbit rings (projected ellipse of the stage ring for depth feeling)
    ring = []
    for i in range(0, 73):
        a = 2*math.pi*i/72
        sx, sy, _, _ = _project3d((400*math.cos(a), 0, 250*math.sin(a)), ry, rx, cx, cy)
        ring.append(f"{sx:.1f},{sy:.1f}")
    o += f'<polyline points="{" ".join(ring)}" fill="none" stroke="{VIOLET}" stroke-opacity=".12" stroke-dasharray="2 6"/>'

    # edges (back to front is not required for lines; opacity encodes depth)
    for pk, pv in PROJECTS.items():
        for sk in pv["stages"]:
            x1, y1, z1, _ = P[("p", pk)]
            x2, y2, z2, _ = P[("s", sk)]
            op = 0.22+0.5*depth((z1+z2)/2)
            o += (f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
                  f'stroke="{VIOLET}" stroke-opacity="{op:.2f}" stroke-width="1"/>')

    # nodes sorted far -> near
    items = [(("s", k), lab) for k, lab in STAGES] + [(("p", k), v["name"]) for k, v in PROJECTS.items()]
    items.sort(key=lambda it: -P[it[0]][2])
    for (kind, key), label in items:
        x, y, z, s = P[(kind, key)]
        d = depth(z)
        if kind == "s":
            r = 6*s+1
            o += (f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r:.1f}" fill="{PANEL_HI}" stroke="{VIOLET}" '
                  f'stroke-opacity="{0.45+0.5*d:.2f}"/>')
            side = 1 if x >= cx else -1
            anchor = "start" if side > 0 else "end"
            o += (f'<text class="m" x="{x+side*(r+8):.1f}" y="{y+4:.1f}" font-size="12" text-anchor="{anchor}" '
                  f'fill="{TEXT}" fill-opacity="{0.55+0.45*d:.2f}">{esc(label)}</text>')
        else:
            r = 15*s
            o += f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r*3:.1f}" fill="url(#halo)"/>'
            o += (f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r:.1f}" fill="{VIOLET_DEEP}" stroke="{TEXT}" '
                  f'stroke-opacity=".8"/>')
            o += (f'<text class="m" x="{x:.1f}" y="{y-r-22:.1f}" font-size="11" letter-spacing="1.5" '
                  f'text-anchor="middle" fill="{VIOLET}">{esc(key)}</text>'
                  f'<text x="{x:.1f}" y="{y-r-7:.1f}" font-size="15" font-weight="600" '
                  f'text-anchor="middle" fill="{TEXT}">{esc(label)}</text>')
    o += (f'<text x="40" y="{H-26}" font-size="13" fill="{MUTED}">{esc(t["const_note"])}</text>')
    return o + "</svg>\n"


# ───────────────────────── dashboard data ─────────────────────────
GQL = """
query($login:String!){ user(login:$login){
  followers{totalCount}
  repositories(privacy:PUBLIC, ownerAffiliations:OWNER, first:100, orderBy:{field:PUSHED_AT,direction:DESC}){
    totalCount nodes{ name isFork stargazerCount forkCount pushedAt primaryLanguage{name} } }
  contributionsCollection{ totalCommitContributions totalPullRequestContributions totalIssueContributions
    contributionCalendar{ weeks{ contributionDays{ date contributionCount } } } }
}}"""


def _http(url, token=None, body=None):
    headers = {"User-Agent": "profile-assets", "Accept": "application/vnd.github+json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    req = urllib.request.Request(url, data=body, headers=headers)
    with urllib.request.urlopen(req, timeout=30) as r:  # noqa: S310 (fixed https GitHub URLs)
        return json.load(r)


def fetch_data(user, token):
    """Return a normalised dict, or None on failure. Never logs the token."""
    try:
        if token:
            res = _http("https://api.github.com/graphql", token,
                        json.dumps({"query": GQL, "variables": {"login": user}}).encode())
            if res.get("errors") or not res.get("data", {}).get("user"):
                raise RuntimeError("GraphQL error")
            u = res["data"]["user"]
            cc = u["contributionsCollection"]
            weeks = [sum(d["contributionCount"] for d in w["contributionDays"])
                     for w in cc["contributionCalendar"]["weeks"]]
            return {
                "followers": u["followers"]["totalCount"],
                "repos": [{"name": r["name"], "fork": r["isFork"], "stars": r["stargazerCount"],
                           "forks": r["forkCount"], "pushed": r["pushedAt"],
                           "lang": (r["primaryLanguage"] or {}).get("name")} for r in u["repositories"]["nodes"]],
                "commits": cc["totalCommitContributions"], "prs": cc["totalPullRequestContributions"],
                "issues": cc["totalIssueContributions"], "weeks": weeks,
            }
        prof = _http(f"https://api.github.com/users/{user}")
        repos = _http(f"https://api.github.com/users/{user}/repos?per_page=100&sort=pushed")
        return {
            "followers": prof["followers"],
            "repos": [{"name": r["name"], "fork": r["fork"], "stars": r["stargazers_count"],
                       "forks": r["forks_count"], "pushed": r["pushed_at"], "lang": r["language"]}
                      for r in repos],
            "commits": None, "prs": None, "issues": None, "weeks": None,
        }
    except Exception as exc:  # network, HTTP 403 rate limit, schema change...
        print(f"::warning::GitHub API unavailable: {type(exc).__name__}", file=sys.stderr)
        return None


def sample_data():
    weeks = [max(0, int(6+5*math.sin(i/4.0)+(i % 7)-2+(14 if i in (30, 31) else 0))) for i in range(52)]
    return {
        "followers": 0, "commits": sum(weeks), "prs": 0, "issues": 0, "weeks": weeks,
        "repos": [
            {"name": "SAMPLE-repo-a", "fork": False, "stars": 2, "forks": 1, "pushed": "2026-10-20T10:00:00Z", "lang": "Python"},
            {"name": "SAMPLE-repo-b", "fork": False, "stars": 2, "forks": 0, "pushed": "2026-09-30T10:00:00Z", "lang": "Python"},
            {"name": "SAMPLE-repo-c", "fork": True, "stars": 2, "forks": 0, "pushed": "2026-08-12T10:00:00Z", "lang": "Python"},
        ],
    }


def _days_ago(iso, now, t):
    d = (now-datetime.fromisoformat(iso.replace("Z", "+00:00"))).days
    return t["today"] if d <= 0 else f"{d}{'' if lang_is_fr(t) else ' '}{t['d_ago']}"


def lang_is_fr(t):
    return t is I18N["fr"]


def build_dashboard(lang, data, now, sample=False, repo_filter=USER):
    t = I18N[lang]
    W, H = 1200, 470
    na = "n/a"
    repos = [r for r in (data["repos"] if data else []) if r["name"] != repo_filter]
    pub = len(repos)+(1 if data and any(r["name"] == repo_filter for r in data["repos"]) else 0) if data else None
    stars = sum(r["stars"] for r in data["repos"]) if data else None
    forks = sum(r["forks"] for r in data["repos"]) if data else None

    def fmt(v):
        return na if v is None else f"{v:,}".replace(",", " ")

    pr_issue = na if not data or data["prs"] is None else f"{data['prs']} · {data['issues']}"
    kpis = [fmt(pub), fmt(stars), fmt(forks), fmt(data["followers"]) if data else na,
            fmt(data["commits"]) if data else na, pr_issue]

    o = svg_open(W, H, "GitHub engineering telemetry", "Contribution activity, repository indicators and recent pushes.")
    o += (f'<rect width="{W}" height="{H}" fill="{BG}"/>'
          f'<rect x=".5" y=".5" width="{W-1}" height="{H-1}" fill="none" stroke="{BORDER}"/>'
          f'<text class="m" x="40" y="46" font-size="13" letter-spacing="3" fill="{VIOLET}">{esc(t["dash_title"])}</text>'
          f'<circle cx="{W-268}" cy="42" r="4" fill="{VIOLET}"/>'
          f'<text class="m" x="{W-40}" y="46" font-size="12" text-anchor="end" fill="{MUTED}">'
          f'@{esc(USER)} · {esc(t["updated"])} {now:%Y-%m-%d} UTC</text>')
    # KPI tiles
    tw, gap = 170, 16
    for i, (lab, val) in enumerate(zip(t["kpis"], kpis)):
        x = 40+i*(tw+gap)
        o += (f'<rect x="{x}" y="70" width="{tw}" height="84" rx="8" fill="{PANEL}" stroke="{BORDER}"/>'
              f'<text class="m" x="{x+16}" y="96" font-size="10.5" letter-spacing="1.5" fill="{MUTED}">{esc(lab)}</text>'
              f'<text x="{x+16}" y="136" font-size="34" font-weight="700" fill="{TEXT if val != na else DIM}">{esc(val)}</text>')
    # activity panel
    px, py, pw, ph = 40, 176, 700, 252
    o += (f'<rect x="{px}" y="{py}" width="{pw}" height="{ph}" rx="8" fill="{PANEL}" stroke="{BORDER}"/>'
          f'<text class="m" x="{px+18}" y="{py+28}" font-size="10.5" letter-spacing="1.5" fill="{MUTED}">{esc(t["activity"])}</text>')
    weeks = data["weeks"] if data else None
    if weeks:
        cx0, cx1, cy0, cy1 = px+24, px+pw-24, py+60, py+ph-34
        m = max(weeks) or 1
        step = (cx1-cx0)/(len(weeks)-1)
        pts = [(cx0+i*step, cy1-(v/m)*(cy1-cy0)) for i, v in enumerate(weeks)]
        for g in range(4):
            gy = cy0+g*(cy1-cy0)/3
            o += f'<line x1="{cx0}" y1="{gy:.1f}" x2="{cx1}" y2="{gy:.1f}" stroke="{BORDER}" stroke-opacity=".7"/>'
        area = f"M{cx0},{cy1} " + " ".join(f"L{x:.1f},{y:.1f}" for x, y in pts) + f" L{cx1},{cy1} Z"
        o += (f'<defs><linearGradient id="ar" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{VIOLET}" stop-opacity=".45"/>'
              f'<stop offset="1" stop-color="{VIOLET}" stop-opacity="0"/></linearGradient></defs>'
              f'<path d="{area}" fill="url(#ar)"/>'
              f'<polyline points="{" ".join(f"{x:.1f},{y:.1f}" for x, y in pts)}" fill="none" stroke="{VIOLET}" stroke-width="2" stroke-linejoin="round"/>')
        pi = weeks.index(max(weeks))
        o += (f'<circle cx="{pts[pi][0]:.1f}" cy="{pts[pi][1]:.1f}" r="4" fill="{TEXT}"/>'
              f'<text class="m" x="{pts[pi][0]:.1f}" y="{pts[pi][1]-10:.1f}" font-size="11" text-anchor="middle" fill="{TEXT}">'
              f'{esc(t["peak"])} {max(weeks)}</text>')
    else:
        o += f'<text x="{px+pw/2}" y="{py+ph/2+6}" font-size="15" text-anchor="middle" fill="{DIM}">{esc(t["unavail"])}</text>'
    # repo panel
    rx0, rw = 760, 400
    o += (f'<rect x="{rx0}" y="{py}" width="{rw}" height="{ph}" rx="8" fill="{PANEL}" stroke="{BORDER}"/>'
          f'<text class="m" x="{rx0+18}" y="{py+28}" font-size="10.5" letter-spacing="1.5" fill="{MUTED}">{esc(t["repos"])}</text>')
    for i, r in enumerate(repos[:5]):
        y = py+66+i*34
        name = r["name"] if len(r["name"]) <= 24 else r["name"][:23]+"…"
        tag = f' · {t["fork"]}' if r["fork"] else ""
        o += (f'<text x="{rx0+18}" y="{y}" font-size="14" font-weight="600" fill="{TEXT}">{esc(name)}</text>'
              f'<text class="m" x="{rx0+18}" y="{y+15}" font-size="10.5" fill="{MUTED}">'
              f'{esc(r["lang"] or na)}{esc(tag)} · {esc(_days_ago(r["pushed"], now, t))}</text>'
              f'<text class="m" x="{rx0+rw-18}" y="{y+6}" font-size="12" text-anchor="end" fill="{VIOLET}">'
              f'★ {r["stars"]}   ⑂ {r["forks"]}</text>')
    if not repos:
        o += f'<text x="{rx0+rw/2}" y="{py+ph/2+6}" font-size="15" text-anchor="middle" fill="{DIM}">n/a</text>'
    o += f'<text x="40" y="{H-22}" font-size="12" fill="{MUTED}">{esc(t["foot"])}</text>'
    if sample:
        o += (f'<text x="{W/2}" y="{H/2+30}" font-size="64" font-weight="800" text-anchor="middle" '
              f'fill="#ff5d5d" fill-opacity=".35" transform="rotate(-8 {W/2} {H/2})">SAMPLE DATA · NOT REAL</text>')
    return o + "</svg>\n"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="assets")
    ap.add_argument("--sample", action="store_true", help="synthetic data, watermarked (rendering test only)")
    ap.add_argument("--skip-dashboard", action="store_true")
    a = ap.parse_args()
    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    now = datetime.now(timezone.utc)

    for lang in ("en", "fr"):
        (out/f"hero-{lang}.svg").write_text(build_hero(lang), encoding="utf-8")
        (out/f"constellation-{lang}.svg").write_text(build_constellation(lang), encoding="utf-8")

    if a.skip_dashboard:
        return 0
    token = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN")
    data = sample_data() if a.sample else fetch_data(USER, token)
    for lang in ("en", "fr"):
        path = out/f"dashboard-{lang}.svg"
        if data is None and path.exists():
            print(f"API failed: keeping existing {path}", file=sys.stderr)
            continue
        path.write_text(build_dashboard(lang, data, now, sample=a.sample), encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
