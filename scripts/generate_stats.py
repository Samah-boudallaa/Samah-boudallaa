#!/usr/bin/env python3
"""Génère le tableau de bord du profil (stats.svg en français, stats.en.svg en anglais)
à partir de l'API GitHub.

Toutes les valeurs proviennent de l'API. Si une donnée est indisponible,
un tiret est affiché : rien n'est inventé.

Variables d'environnement :
  GH_USER        nom d'utilisateur (défaut : Samah-boudallaa)
  GITHUB_TOKEN   jeton d'API. Avec le jeton par défaut des Actions, seules les
                 contributions publiques sont visibles. Avec un jeton personnel
                 (scope read:user, secret PROFILE_TOKEN), le calendrier inclut
                 aussi les contributions privées, comme sur la page du profil.
  EXCLUDE_LANGS  langages exclus du calcul, séparés par des virgules
                 (défaut : "Jupyter Notebook", dont le volume vient surtout des sorties).
                 Mettre une chaîne vide pour tout inclure.
  OUT_DIR        dossier de sortie (défaut : .)
"""
import os, json, datetime, urllib.request
from html import escape

USER = os.environ.get("GH_USER", "Samah-boudallaa")
TOKEN = os.environ.get("GITHUB_TOKEN")
OUT_DIR = os.environ.get("OUT_DIR", ".")
EXCLUDE = {s.strip() for s in os.environ.get("EXCLUDE_LANGS", "Jupyter Notebook").split(",") if s.strip()}

LANG_COLORS = {"Python": "#3572A5", "Jupyter Notebook": "#DA5B0B", "HTML": "#e34c26", "CSS": "#8b5cf6",
               "JavaScript": "#f1e05a", "C": "#8b949e", "SQL": "#e38c00", "Shell": "#89e051",
               "TypeScript": "#3178c6", "R": "#198CE7", "Dockerfile": "#384d54"}
PALETTE = ["#161b22", "#1e3a8a", "#2563eb", "#7c3aed", "#d8b4fe"]

# L'API GraphQL renvoie *_QUARTILE (et non *_QUARTER). Les deux orthographes sont acceptées.
LEVELS = {"NONE": 0,
          "FIRST_QUARTILE": 1, "SECOND_QUARTILE": 2, "THIRD_QUARTILE": 3, "FOURTH_QUARTILE": 4,
          "FIRST_QUARTER": 1, "SECOND_QUARTER": 2, "THIRD_QUARTER": 3, "FOURTH_QUARTER": 4}

I18N = {
    "fr": {
        "file": "stats.svg",
        "aria": "Tableau de bord GitHub",
        "live": "LIVE · généré par pipeline · @{user} · maj {when}",
        "k_repos": "DÉPÔTS PUBLICS", "k_contrib": "CONTRIBUTIONS", "k_days": "JOURS ACTIFS",
        "k_stars": "ÉTOILES", "k_langs": "LANGAGES",
        "s_contrib": "12 mois", "s_days": "{p} % des jours", "s_stars": "sur mes dépôts publics",
        "s_langs": "hors notebooks",
        "cal": "CALENDRIER DE CONTRIBUTIONS (12 DERNIERS MOIS)",
        "wd": ("lun", "mer", "ven"), "less": "Moins", "more": "Plus", "unit": "j",
        "tip": "{n} contribution(s) le {d}",
        "cal_off": "Calendrier indisponible pour cette exécution",
        "cur": "SÉRIE ACTUELLE", "best": "SÉRIE MAXIMALE",
        "c_commits": "COMMITS", "c_month": "MOIS LE PLUS ACTIF", "c_day": "MEILLEUR JOUR", "c_avg": "MOYENNE",
        "c_commits_s": "12 mois", "c_avg_s": "par jour actif",
        "langs": "LANGAGES (octets de code, dépôts publics)",
        "recent": "DERNIERS PROJETS TRAVAILLÉS",
        "note": "Données de l'API GitHub · régénéré chaque jour par GitHub Actions",
        "mode_full": "contributions publiques et privées", "mode_pub": "contributions publiques uniquement",
        "excl": "langages exclus",
        "months": ["janv.", "févr.", "mars", "avr.", "mai", "juin", "juil.", "août", "sept.", "oct.", "nov.", "déc."],
        "dfmt": "{d:02d}/{m:02d}",
    },
    "en": {
        "file": "stats.en.svg",
        "aria": "GitHub dashboard",
        "live": "LIVE · pipeline-generated · @{user} · updated {when}",
        "k_repos": "PUBLIC REPOS", "k_contrib": "CONTRIBUTIONS", "k_days": "ACTIVE DAYS",
        "k_stars": "STARS", "k_langs": "LANGUAGES",
        "s_contrib": "12 months", "s_days": "{p}% of days", "s_stars": "across my public repos",
        "s_langs": "excluding notebooks",
        "cal": "CONTRIBUTION CALENDAR (LAST 12 MONTHS)",
        "wd": ("Mon", "Wed", "Fri"), "less": "Less", "more": "More", "unit": "d",
        "tip": "{n} contribution(s) on {d}",
        "cal_off": "Calendar unavailable for this run",
        "cur": "CURRENT STREAK", "best": "LONGEST STREAK",
        "c_commits": "COMMITS", "c_month": "MOST ACTIVE MONTH", "c_day": "BEST DAY", "c_avg": "AVERAGE",
        "c_commits_s": "12 months", "c_avg_s": "per active day",
        "langs": "LANGUAGES (bytes of code, public repos)",
        "recent": "LATEST PROJECTS",
        "note": "Data from the GitHub API · rebuilt daily by GitHub Actions",
        "mode_full": "public and private contributions", "mode_pub": "public contributions only",
        "excl": "excluded languages",
        "months": ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
        "dfmt": "{m:02d}/{d:02d}",
    },
}


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
stars = sum(r.get("stargazers_count", 0) for r in repos)

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
# Le dépôt du profil est poussé chaque jour par le robot : il ne reflète pas mon travail.
recent = sorted((r for r in repos if r["name"].lower() != USER.lower()),
                key=lambda r: r.get("pushed_at") or "", reverse=True)[:4]

# Un jeton personnel du propriétaire voit aussi les contributions privées ; le jeton des Actions non.
full_access = False
try:
    full_access = api("/user").get("login", "").lower() == USER.lower()
except Exception:
    pass

QUERY = """query($login:String!){user(login:$login){contributionsCollection{
restrictedContributionsCount totalCommitContributions totalPullRequestContributions
totalIssueContributions totalPullRequestReviewContributions
contributionCalendar{totalContributions weeks{contributionDays{date contributionCount contributionLevel}}}}}}"""
coll = None
try:
    coll = graphql(QUERY, {"login": USER})["user"]["contributionsCollection"]
except Exception as e:
    print("GraphQL indisponible :", e)
cal = coll["contributionCalendar"] if coll else None


def level_from_count(c, mx):
    if c <= 0:
        return 0
    return min(4, 1 + int(3 * (c - 1) / max(mx, 1))) if mx > 1 else 2


weeks, days = [], []
if cal:
    raw = [d for w in cal["weeks"] for d in w["contributionDays"]]
    mx = max((d["contributionCount"] for d in raw), default=0)
    for w in cal["weeks"]:
        wk = []
        for d in w["contributionDays"]:
            lvl = LEVELS.get(d["contributionLevel"])
            if lvl is None:  # énumération inconnue : on retombe sur le calcul par volume
                lvl = level_from_count(d["contributionCount"], mx)
            if d["contributionCount"] > 0 and lvl == 0:  # un jour actif n'est jamais peint « vide »
                lvl = level_from_count(d["contributionCount"], mx)
            wk.append({"date": d["date"], "count": d["contributionCount"], "level": lvl})
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
total_contrib = cal["totalContributions"] if cal else None
hidden = coll["restrictedContributionsCount"] if coll else 0
best_day = max(days, key=lambda d: d["count"]) if days else None
by_month = {}
for d in days:
    by_month[d["date"][:7]] = by_month.get(d["date"][:7], 0) + d["count"]
top_month = max(by_month.items(), key=lambda kv: kv[1]) if by_month else None
avg_active = (sum(d["count"] for d in days) / active_days) if active_days else None
utc = datetime.datetime.now(datetime.timezone.utc)
dash = "–"


def fmt(v):
    return dash if v is None else str(v)


def render(lang):
    t = I18N[lang]
    now = utc.strftime("%d/%m/%Y · %H:%M UTC") if lang == "fr" else utc.strftime("%Y-%m-%d · %H:%M UTC")
    pct = round(100 * active_days / len(days)) if days and active_days is not None else None

    kpis = [(t["k_repos"], len(repos), "#58a6ff", ""),
            (t["k_contrib"], total_contrib, "#a371f7",
             t["s_contrib"] + (f" · +{hidden}" if hidden else "")),
            (t["k_days"], active_days, "#3fb950", t["s_days"].format(p=pct) if pct is not None else ""),
            (t["k_stars"], stars, "#e3b341", t["s_stars"]),
            (t["k_langs"], len(langs), "#f0883e", t["s_langs"])]

    # hauteur calculée pour que rien ne se chevauche
    Y0 = 224
    LY = Y0 + 7 * 14 + 16
    BY = LY + 34
    LT = BY + (66 if coll else 6) + 22
    H = LT + 20 + 4 * 44 + 46

    s = [f'<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="{H}" viewBox="0 0 1000 {H}" role="img" aria-label="{escape(t["aria"])}">']
    s.append('''<defs><pattern id="g" width="40" height="40" patternUnits="userSpaceOnUse"><path d="M40 0H0V40" fill="none" stroke="#58a6ff" stroke-opacity=".07"/></pattern>
<linearGradient id="edge" x1="0" x2="1"><stop offset="0" stop-color="#7c3aed"/><stop offset="1" stop-color="#1f6feb"/></linearGradient>
<style>.m{font-family:Consolas,Menlo,"Liberation Mono",monospace}
.k{animation:in .9s both}.b{transform-box:fill-box;transform-origin:left center;animation:grow 1.4s cubic-bezier(.2,.8,.2,1) both}
.c{transform-box:fill-box;transform-origin:center;animation:pop .5s both}.live{animation:p 1.6s infinite}
@keyframes in{from{opacity:0;transform:translateY(12px)}to{opacity:1;transform:none}}
@keyframes grow{from{transform:scaleX(0)}to{transform:scaleX(1)}}
@keyframes pop{from{opacity:0;transform:scale(.3)}to{opacity:1;transform:none}}
@keyframes p{50%{opacity:.25}}
@media (prefers-reduced-motion:reduce){.k,.b,.c,.live{animation:none}}</style></defs>''')
    s.append(f'<rect width="1000" height="{H}" rx="16" fill="#0d1117"/><rect width="1000" height="{H}" rx="16" fill="url(#g)"/>')
    s.append('<rect x="0" y="0" width="1000" height="3" rx="1.5" fill="url(#edge)"/>')
    s.append(f'<circle class="live" cx="34" cy="34" r="5" fill="#3fb950"/>'
             f'<text x="50" y="39" class="m" font-size="13" fill="#8b949e">{escape(t["live"].format(user=USER, when=now))}</text>')

    for i, (label, val, col, sub) in enumerate(kpis):
        x = 30 + i * 188
        s.append(f'<g class="k" style="animation-delay:{i*.12:.2f}s"><rect x="{x}" y="60" width="178" height="92" rx="12" fill="#161b22" stroke="{col}" stroke-opacity=".6"/>'
                 f'<text x="{x+16}" y="86" class="m" font-size="11" fill="#8b949e" letter-spacing="1">{escape(label)}</text>'
                 f'<text x="{x+16}" y="124" class="m" font-size="34" font-weight="700" fill="{col}">{fmt(val)}</text>'
                 f'<text x="{x+16}" y="143" class="m" font-size="9.5" fill="#6e7681">{escape(sub)}</text></g>')

    # ----- Calendrier -----
    s.append(f'<text x="30" y="184" class="m" font-size="14" fill="#c9d1d9" font-weight="700">{escape(t["cal"])}</text>')
    X0, STEP, SIZE = 56, 14, 12
    for r_, lab in zip((1, 3, 5), t["wd"]):
        s.append(f'<text x="30" y="{Y0 + r_*STEP + 10}" class="m" font-size="10" fill="#6e7681">{lab}</text>')

    if weeks:
        last_month = None
        for wi, wk in enumerate(weeks):
            first = datetime.date.fromisoformat(wk[0]["date"])
            if first.month != last_month and (wi > 0 or first.day <= 14):
                if wi > 0 or first.day <= 14:
                    s.append(f'<text x="{X0+wi*STEP}" y="{Y0-8}" class="m" font-size="10" fill="#8b949e">{t["months"][first.month-1]}</text>')
                last_month = first.month
            for d in wk:
                dt = datetime.date.fromisoformat(d["date"])
                row = (dt.weekday() + 1) % 7  # dimanche = 0
                tip = t["tip"].format(n=d["count"], d=d["date"])
                stroke = ' stroke="#d8b4fe" stroke-opacity=".35"' if d["level"] >= 3 else ""
                s.append(f'<rect class="c" x="{X0+wi*STEP}" y="{Y0+row*STEP}" width="{SIZE}" height="{SIZE}" rx="3" '
                         f'fill="{PALETTE[d["level"]]}"{stroke} style="animation-delay:{wi*0.03:.2f}s"><title>{escape(tip)}</title></rect>')
    else:
        for wi in range(53):
            for row in range(7):
                s.append(f'<rect x="{X0+wi*STEP}" y="{Y0+row*STEP}" width="{SIZE}" height="{SIZE}" rx="3" fill="{PALETTE[0]}"/>')
        s.append(f'<text x="430" y="272" text-anchor="middle" class="m" font-size="13" fill="#8b949e">{escape(t["cal_off"])}</text>')

    s.append(f'<text x="640" y="{LY+9}" class="m" font-size="11" fill="#6e7681">{t["less"]}</text>')
    for i, c in enumerate(PALETTE):
        s.append(f'<rect x="{680+i*16}" y="{LY}" width="12" height="12" rx="3" fill="{c}"/>')
    s.append(f'<text x="768" y="{LY+9}" class="m" font-size="11" fill="#6e7681">{t["more"]}</text>')

    u = f' {t["unit"]}'
    s.append(f'<text x="830" y="{Y0+8}" class="m" font-size="11" fill="#8b949e" letter-spacing="1">{t["cur"]}</text>'
             f'<text x="830" y="{Y0+40}" class="m" font-size="26" font-weight="700" fill="#58a6ff">{fmt(cur_streak)}{u if cur_streak is not None else ""}</text>'
             f'<text x="830" y="{Y0+70}" class="m" font-size="11" fill="#8b949e" letter-spacing="1">{t["best"]}</text>'
             f'<text x="830" y="{Y0+102}" class="m" font-size="26" font-weight="700" fill="#a371f7">{fmt(best_streak)}{u if best_streak is not None else ""}</text>')

    # ----- Indicateurs d'activité (tous calculés à partir du calendrier) -----
    if coll and days:
        mname = (t["months"][int(top_month[0][5:]) - 1] + " " + top_month[0][:4]) if top_month else ""
        bd = ""
        if best_day and best_day["count"]:
            bd = t["dfmt"].format(d=int(best_day["date"][8:]), m=int(best_day["date"][5:7])) + f" · {best_day['date'][:4]}"
        chips = [(t["c_commits"], coll["totalCommitContributions"], "#58a6ff", t["c_commits_s"]),
                 (t["c_month"], top_month[1] if top_month else dash, "#a371f7", mname),
                 (t["c_day"], best_day["count"] if best_day else dash, "#3fb950", bd),
                 (t["c_avg"], f"{avg_active:.1f}" if avg_active is not None else dash, "#f0883e", t["c_avg_s"])]
        for i, (lab, v, col, sub) in enumerate(chips):
            x = 30 + i * 238
            s.append(f'<g class="k" style="animation-delay:{.3+i*.1:.2f}s"><rect x="{x}" y="{BY}" width="222" height="56" rx="10" fill="#161b22"/>'
                     f'<rect x="{x}" y="{BY+10}" width="3" height="36" rx="1.5" fill="{col}"/>'
                     f'<text x="{x+16}" y="{BY+22}" class="m" font-size="10.5" fill="#8b949e" letter-spacing="1">{escape(lab)}</text>'
                     f'<text x="{x+16}" y="{BY+43}" class="m" font-size="11" fill="#6e7681">{escape(str(sub))}</text>'
                     f'<text x="{x+206}" y="{BY+38}" text-anchor="end" class="m" font-size="24" font-weight="700" fill="{col}">{v}</text></g>')

    # ----- Langages -----
    s.append(f'<text x="30" y="{LT}" class="m" font-size="14" fill="#c9d1d9" font-weight="700">{escape(t["langs"])}</text>')
    for i, (name, v) in enumerate(top):
        y = LT + 20 + i * 32
        p = v * 100 / total
        w = max(4, 330 * v / top[0][1])
        col = LANG_COLORS.get(name, "#8b949e")
        s.append(f'<g class="k" style="animation-delay:{.4+i*.12:.2f}s"><text x="30" y="{y+14}" class="m" font-size="13" fill="#c9d1d9">{escape(name)}</text>'
                 f'<rect x="170" y="{y}" width="330" height="18" rx="9" fill="#21262d"/>'
                 f'<rect class="b" x="170" y="{y}" width="{w:.0f}" height="18" rx="9" fill="{col}" style="animation-delay:{.5+i*.12:.2f}s"/>'
                 f'<text x="515" y="{y+14}" class="m" font-size="13" fill="#8b949e">{p:.1f}%</text></g>')

    # ----- Dépôts récents -----
    s.append(f'<text x="620" y="{LT}" class="m" font-size="14" fill="#c9d1d9" font-weight="700">{escape(t["recent"])}</text>')
    for i, r in enumerate(recent):
        y = LT + 20 + i * 44
        col = LANG_COLORS.get(r.get("language") or "", "#8b949e")
        date = (r.get("pushed_at") or "")[:10]
        s.append(f'<g class="k" style="animation-delay:{.5+i*.12:.2f}s"><rect x="620" y="{y}" width="350" height="36" rx="8" fill="#161b22"/>'
                 f'<circle cx="640" cy="{y+18}" r="6" fill="{col}"/><text x="656" y="{y+23}" class="m" font-size="13" fill="#79c0ff">{escape(r["name"][:30])}</text>'
                 f'<text x="955" y="{y+23}" text-anchor="end" class="m" font-size="11" fill="#6e7681">{escape(date)}</text></g>')

    note = t["note"] + " · " + (t["mode_full"] if full_access else t["mode_pub"])
    if EXCLUDE:
        note += f" · {t['excl']} : {', '.join(sorted(EXCLUDE))}"
    s.append(f'<text x="500" y="{H-16}" text-anchor="middle" class="m" font-size="10.5" fill="#6e7681">{escape(note)}</text></svg>')
    return "\n".join(s)


os.makedirs(OUT_DIR, exist_ok=True)
for lang in I18N:
    path = os.path.join(OUT_DIR, I18N[lang]["file"])
    with open(path, "w", encoding="utf-8") as f:
        f.write(render(lang))
    print("OK", path)
print("dépôts:", len(repos), "| calendrier:", bool(cal), "| total:", total_contrib,
      "| accès complet (privé inclus):", full_access, "| langages:", top)
