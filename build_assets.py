#!/usr/bin/env python3
"""Generate the full monochrome profile-README asset set for Kirankanth35.
Mirrors the design language of the reference repo: mono type, hairline rules,
CSS-keyframe reveals, light/dark via prefers-color-scheme, reduced-motion safe.
Writes assets/*.svg and assets/dark/*.svg (identical files; the <picture>
srcset in the README selects between them, same as the reference)."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent
A = ROOT / "assets"
D = A / "dark"
A.mkdir(parents=True, exist_ok=True)
D.mkdir(parents=True, exist_ok=True)

VARS = (':root { --bone: #444444; --rule: #C0C0C0; --muted: #888888; '
        '--dim: #AAAAAA; --accent: #555555; --ghost: #CCCCCC; }\n'
        '    @media (prefers-color-scheme: dark) { :root { --bone: #DDDDDD; '
        '--rule: #444444; --muted: #777777; --dim: #666666; --accent: #AAAAAA; '
        '--ghost: #2A2A2A; } }')
MONO = ('.mono { font-family: ui-monospace, "SFMono-Regular", "SF Mono", Menlo, '
        'Consolas, "Liberation Mono", monospace; }')
RISE = ('.rise { opacity: 0; animation: rise .7s cubic-bezier(.2,.7,.2,1) forwards; }\n'
        '    @keyframes rise { from { opacity:0;transform:translateY(8px); } '
        'to { opacity:1;transform:translateY(0); } }')
FADE = ('.fade { opacity: 0; animation: fade .7s ease forwards; }\n'
        '    @keyframes fade { to { opacity: 1; } }')
DRAW = ('.draw { stroke-dasharray: 1000; stroke-dashoffset: 1000; '
        'animation: draw 1.4s cubic-bezier(.6,0,.2,1) forwards; }\n'
        '    @keyframes draw { to { stroke-dashoffset: 0; } }')
RM = ('@media (prefers-reduced-motion: reduce) { .rise,.fade,.draw { animation: none; } '
      '.rise,.fade { opacity: 1; } .draw { stroke-dashoffset: 0; } }')
DELAYS = ' '.join(f'.a{i}{{animation-delay:{d}s}}'
                  for i, d in enumerate(
                      [.1, .2, .35, .5, .65, .8, .95, 1.1, 1.25, 1.4], 1))


def write(name: str, svg: str):
    (A / name).write_text(svg)
    (D / name).write_text(svg)
    print(f"  {name}")


def shell(inner: str, w: int, h: int, label: str, extra_css: str = "") -> str:
    return f'''<svg viewBox="0 0 {w} {h}" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{label}">
  <style>
    {VARS}
    {MONO}
    {RISE}
    {FADE}
    {DELAYS}
    {extra_css}
    {RM}
  </style>
{inner}
</svg>'''


# ── section headers ────────────────────────────────────────────────────────
def section(num: str, title: str, slug: str) -> str:
    css = ('.d { stroke: var(--rule); stroke-width: 1; stroke-dasharray: 760; '
           'stroke-dashoffset: 760; animation: dd 1.3s cubic-bezier(.6,0,.2,1) .2s forwards; }\n'
           '    @keyframes dd { to { stroke-dashoffset: 0; } }\n'
           '    @media (prefers-reduced-motion: reduce){.d{animation:none;stroke-dashoffset:0}}')
    inner = f'''  <g class="fade a1">
    <text class="mono" x="48" y="68" font-size="52" fill="var(--ghost)">{num}</text>
    <text class="mono" x="128" y="58" font-size="14" fill="var(--accent)" letter-spacing="6">{title}</text>
    <text class="mono" x="952" y="58" font-size="11" fill="var(--muted)" letter-spacing="2" text-anchor="end">~/{slug}</text>
  </g>
  <line class="d" x1="{128 + len(title) * 13 + 40}" y1="53" x2="831" y2="53"/>'''
    return shell(inner, 1000, 92, f"Section {num} — {title}", css)


# ── header ─────────────────────────────────────────────────────────────────
def header() -> str:
    css = ('.draw2 { stroke-dasharray: 1000; stroke-dashoffset: 1000; '
           'animation: draw2 1.4s cubic-bezier(.6,0,.2,1) forwards; }\n'
           '    @keyframes draw2 { to { stroke-dashoffset: 0; } }\n'
           '    @media (prefers-reduced-motion: reduce){.draw2{animation:none;stroke-dashoffset:0}}')
    inner = '''  <line class="draw2 a1" x1="48" y1="58" x2="952" y2="58" stroke="var(--rule)" stroke-width="1"/>
  <g class="fade a1">
    <text class="mono" fill="var(--muted)" x="48" y="44" font-size="11" letter-spacing="3.5">PORTFOLIO — INDEX N&#186; 001</text>
    <text class="mono" fill="var(--muted)" x="952" y="44" font-size="11" letter-spacing="3.5" text-anchor="end">FREMONT, CA — 37.55&#176; N</text>
  </g>

  <g class="rise a2">
    <text fill="var(--bone)" class="mono" x="46" y="176" font-size="62" letter-spacing="-2">Kiran Kanth Madigani</text>
  </g>
  <g class="fade a3">
    <text fill="var(--muted)" class="mono" x="48" y="214" font-size="19">Business &#183; BI &#183; Data Analyst — Fremont, California.</text>
  </g>

  <g class="fade a4">
    <text fill="var(--dim)" class="mono" x="48" y="274" font-size="12.5" letter-spacing="1">focus  &#9656;</text>
    <text fill="var(--accent)" class="mono" x="128" y="274" font-size="12.5" letter-spacing="1">A/B testing &#183; causal inference &#183; BI dashboards &#183; stakeholder analytics</text>
  </g>
  <g class="fade a5">
    <text fill="var(--dim)" class="mono" x="48" y="300" font-size="12.5" letter-spacing="1">open to entry-level analyst roles &#183; internships &#183; collaboration</text>
  </g>

  <line class="draw2 a5" x1="48" y1="342" x2="952" y2="342" stroke="var(--rule)" stroke-width="1"/>
  <g class="fade a6">
    <text fill="var(--muted)" class="mono" x="48" y="374" font-size="11.5" letter-spacing="3">BUSINESS ANALYTICS</text>
    <text fill="var(--accent)" class="mono" x="292" y="374" font-size="11.5">&#183;</text>
    <text fill="var(--muted)" class="mono" x="322" y="374" font-size="11.5" letter-spacing="3">EXPERIMENTATION</text>
    <text fill="var(--accent)" class="mono" x="540" y="374" font-size="11.5">&#183;</text>
    <text fill="var(--muted)" class="mono" x="570" y="374" font-size="11.5" letter-spacing="3">DECISION SUPPORT</text>
    <text fill="var(--muted)" class="mono" x="952" y="374" font-size="11.5" letter-spacing="3" text-anchor="end">CSUN — 2024 / 2026</text>
  </g>'''
    return shell(inner, 1000, 400, "Kiran Kanth Madigani — Business, BI and Data Analyst", css)


# ── whoami ─────────────────────────────────────────────────────────────────
def whoami() -> str:
    inner = '''  <text class="mono rise a1" x="48" y="32" font-size="16" fill="var(--bone)">MS Business Analytics, California State University Northridge (2026).</text>
  <text class="mono rise a2" x="48" y="60" font-size="16" fill="var(--bone)">turning messy data into decisions &#8212; Python &#183; SQL &#183; R &#183; Tableau &#183; Power BI.</text>
  <text class="mono rise a3" x="48" y="88" font-size="15" fill="var(--muted)">drawn to questions where the answer changes what someone does next. rigour first, then the dashboard.</text>

  <line class="rise a4" x1="48" y1="116" x2="952" y2="116" stroke="var(--rule)" stroke-width="1" opacity=".5"/>

  <text class="mono rise a4" x="48"  y="148" font-size="11" fill="var(--muted)" letter-spacing="2.5">FOCUS</text>
  <text class="mono rise a4" x="154" y="148" font-size="15" fill="var(--bone)">A/B Testing &#183; Causal Inference &#183; BI &amp; Dashboards &#183; Requirements Analysis</text>

  <text class="mono rise a5" x="48"  y="180" font-size="11" fill="var(--muted)" letter-spacing="2.5">STATUS</text>
  <text class="mono rise a5" x="154" y="180" font-size="15" fill="var(--bone)">open to Business Analyst / BI Analyst / Data Analyst roles</text>

  <text class="mono rise a6" x="48"  y="212" font-size="11" fill="var(--muted)" letter-spacing="2.5">PRIOR</text>
  <text class="mono rise a6" x="154" y="212" font-size="15" fill="var(--bone)">B.E. Computer Science (Hons), KL University &#183; AWS &#215;3 certified</text>'''
    return shell(inner, 1000, 236, "whoami — bio, focus, status")


# ── ecosystem / system map ─────────────────────────────────────────────────
def ecosystem() -> str:
    css = ('.n { opacity:0; animation: rise .7s cubic-bezier(.2,.7,.2,1) forwards; }\n'
           '    .ln { stroke: var(--rule); stroke-width:1; stroke-dasharray:300; '
           'stroke-dashoffset:300; animation: dl 1.1s cubic-bezier(.6,0,.2,1) forwards; }\n'
           '    @keyframes dl { to { stroke-dashoffset:0; } }\n'
           '    @media (prefers-reduced-motion: reduce){.n{animation:none;opacity:1}'
           '.ln{animation:none;stroke-dashoffset:0}}')

    def node(x, y, w, h, title, sub, delay_cls):
        return f'''  <g class="n {delay_cls}">
    <rect x="{x}" y="{y}" width="{w}" height="{h}" rx="2" stroke="var(--rule)" stroke-width="1" fill="none"/>
    <text class="mono" x="{x+16}" y="{y+28}" font-size="12.5" fill="var(--bone)" letter-spacing="1">{title}</text>
    <text class="mono" x="{x+16}" y="{y+50}" font-size="11" fill="var(--muted)">{sub}</text>
  </g>'''

    inner = f'''  <text class="mono fade a1" x="48" y="30" font-size="11" fill="var(--muted)" letter-spacing="3.5">SYSTEM MAP</text>
  <text class="mono fade a1" x="952" y="30" font-size="11" fill="var(--muted)" letter-spacing="3.5" text-anchor="end">FIG. 01</text>
  <line class="ln a1" x1="48" y1="48" x2="952" y2="48"/>

  <g class="n a2">
    <rect x="380" y="96" width="240" height="76" rx="2" stroke="var(--accent)" stroke-width="1.5" fill="none"/>
    <text class="mono" x="500" y="128" font-size="14" fill="var(--bone)" letter-spacing="2" text-anchor="middle">RAW DATA</text>
    <text class="mono" x="500" y="150" font-size="11" fill="var(--muted)" text-anchor="middle">CSV &#183; SQL &#183; public datasets &#183; surveys</text>
  </g>

  <line class="ln a3" x1="500" y1="172" x2="500" y2="212"/>

  <g class="n a3">
    <rect x="330" y="212" width="340" height="76" rx="2" stroke="var(--rule)" stroke-width="1" fill="none"/>
    <text class="mono" x="500" y="244" font-size="13" fill="var(--bone)" letter-spacing="2" text-anchor="middle">CLEAN &#183; MODEL &#183; TEST</text>
    <text class="mono" x="500" y="266" font-size="11" fill="var(--muted)" text-anchor="middle">pandas &#183; regression &#183; hypothesis tests &#183; A/B</text>
  </g>

  <line class="ln a4" x1="500" y1="288" x2="500" y2="322"/>
  <line class="ln a4" x1="170" y1="322" x2="830" y2="322"/>
  <line class="ln a4" x1="170" y1="322" x2="170" y2="356"/>
  <line class="ln a4" x1="500" y1="322" x2="500" y2="356"/>
  <line class="ln a4" x1="830" y1="322" x2="830" y2="356"/>

{node(48, 356, 244, 84, "DASHBOARDS", "Tableau &#183; Power BI &#183; KPI views", "a5")}
{node(378, 356, 244, 84, "EXPERIMENTS", "A/B tests &#183; causal estimates", "a6")}
{node(708, 356, 244, 84, "RESEARCH", "regression studies &#183; papers", "a7")}

  <line class="ln a7" x1="170" y1="440" x2="170" y2="474"/>
  <line class="ln a7" x1="500" y1="440" x2="500" y2="474"/>
  <line class="ln a7" x1="830" y1="440" x2="830" y2="474"/>
  <line class="ln a7" x1="170" y1="474" x2="830" y2="474"/>
  <line class="ln a7" x1="500" y1="474" x2="500" y2="508"/>

  <g class="n a8">
    <rect x="300" y="508" width="400" height="86" rx="2" stroke="var(--accent)" stroke-width="1.5" fill="none"/>
    <text class="mono" x="500" y="542" font-size="14" fill="var(--bone)" letter-spacing="2" text-anchor="middle">STAKEHOLDER DECISION</text>
    <text class="mono" x="500" y="564" font-size="11" fill="var(--muted)" text-anchor="middle">memo &#183; recommendation &#183; measurable action</text>
    <text class="mono" x="500" y="582" font-size="10.5" fill="var(--dim)" text-anchor="middle">the only output that actually counts</text>
  </g>

  <line class="ln a8" x1="48" y1="628" x2="952" y2="628"/>
  <text class="mono fade a8" x="48" y="654" font-size="11" fill="var(--muted)" letter-spacing="2">ONE PIPELINE &#8212; QUESTION &#8594; EVIDENCE &#8594; DECISION</text>'''
    return shell(inner, 1000, 680, "System map: data in, decisions out", css)


# ── projects ───────────────────────────────────────────────────────────────
PROJECTS = [
    ("FAFSA NUDGE EXPERIMENT",
     "End-to-end A/B testing study measuring whether behavioural nudges lift FAFSA aid-renewal rates.",
     "Pre-registered design, power analysis, CI pipeline and a stakeholder memo written without a single p-value.",
     "PYTHON &#183; A/B TESTING &#183; CAUSAL INFERENCE &#183; CI"),
    ("SOCIAL PROOF TO ACTION",
     "Graduate research on algorithmic amplification and influencer authority across 10,000 posts from 800 accounts.",
     "Regression-based mediation and moderation models with clustered standard errors to separate real effects from noise.",
     "PYTHON &#183; R &#183; REGRESSION &#183; MEDIATION &#183; MODERATION"),
    ("END-TO-END RETAIL BI DASHBOARD",
     "Full retail analytics pipeline from raw transactions through to an executive-facing BI layer.",
     "Cleaning, modelling and KPI design, surfaced as dashboards built for non-technical decision makers.",
     "PYTHON &#183; SQL &#183; POWER BI &#183; TABLEAU &#183; KPI DESIGN"),
    ("EXECUTIVE SALES REVENUE DASHBOARD",
     "Revenue and performance reporting for a top-five product portfolio, framed for leadership review.",
     "Trend decomposition and variance analysis translated into a single-screen executive view.",
     "PYTHON &#183; DASHBOARDING &#183; REPORTING &#183; VARIANCE ANALYSIS"),
    ("GLOBAL AUTISM ANALYTICS",
     "Public-health analysis of global autism prevalence, diagnosis patterns and reporting gaps.",
     "Data cleaning across inconsistent international sources, then comparative statistical analysis.",
     "PYTHON &#183; EDA &#183; PUBLIC DATA &#183; STATISTICAL ANALYSIS"),
    ("GLOBAL HUNGER &amp; CHILD MALNUTRITION",
     "Cross-country study of hunger indices and child malnutrition indicators over time.",
     "Correlation and trend analysis surfacing where reported progress diverges from underlying measures.",
     "PYTHON &#183; EDA &#183; TIME SERIES &#183; DATA VISUALIZATION"),
    ("TOP-10 MARKET GAP ANALYTICS",
     "Market gap analysis identifying underserved segments across a ranked competitive set.",
     "Gap scoring model with an interactive HTML output for browsing findings by segment.",
     "HTML &#183; PYTHON &#183; GAP ANALYSIS &#183; MARKET RESEARCH"),
    ("SPACEX IPO MARKET IMPACT",
     "Event-style analysis of anticipated market impact around a high-profile IPO scenario.",
     "Comparable-company framing with sensitivity checks on the headline assumptions.",
     "PYTHON &#183; FINANCIAL ANALYSIS &#183; SCENARIO MODELLING"),
    ("IRAN OIL CONFLICT ANALYTICS",
     "Geopolitical-risk analysis linking conflict events to oil market movements.",
     "Time-aligned event study joining commodity price series with conflict timelines.",
     "PYTHON &#183; EVENT STUDY &#183; TIME SERIES &#183; RISK ANALYSIS"),
]


def projects() -> str:
    css = ('.title { font-family: ui-monospace,"SFMono-Regular","SF Mono",Menlo,Consolas,monospace; '
           'font-size:15px; fill:var(--bone); letter-spacing:1.5px; }\n'
           '    .copy { font-family: ui-monospace,"SFMono-Regular","SF Mono",Menlo,Consolas,monospace; '
           'font-size:13px; fill:var(--muted); }\n'
           '    .meta { font-family: ui-monospace,"SFMono-Regular","SF Mono",Menlo,Consolas,monospace; '
           'font-size:10.5px; fill:var(--dim); letter-spacing:1.5px; }\n'
           '    .rule { stroke:var(--rule); stroke-width:1; opacity:.5; }\n'
           '    .row { opacity:0; animation: rise .7s cubic-bezier(.2,.7,.2,1) forwards; }\n'
           + ' '.join(f'.r{i}{{animation-delay:{.1 + i * .09:.2f}s}}' for i in range(1, 11))
           + '\n    @media (prefers-reduced-motion: reduce){.row{animation:none;opacity:1}}')
    rows = []
    for i, (t, c1, c2, meta) in enumerate(PROJECTS, 1):
        y = (i - 1) * 110
        rows.append(f'''    <g class="row r{i}" transform="translate(0 {y})">
      <text class="title" x="48" y="24">{i:02d} / {t}</text>
      <text class="copy" x="48" y="49">{c1}</text>
      <text class="copy" x="48" y="68">{c2}</text>
      <text class="meta" x="48" y="87">{meta}</text>
      <line class="rule" x1="48" y1="104" x2="952" y2="104"/>
    </g>''')
    h = len(PROJECTS) * 110 + 40
    inner = f'  <g transform="translate(0 20)">\n' + "\n".join(rows) + "\n  </g>"
    return shell(inner, 1000, h, f"{len(PROJECTS)} analytics projects", css)


# ── telemetry ──────────────────────────────────────────────────────────────
def telemetry() -> str:
    css = ('.grow { transform:scaleX(0); transform-origin:left; '
           'animation:grow .9s cubic-bezier(.2,.7,.2,1) forwards; }\n'
           '    @keyframes grow { to { transform:scaleX(1); } }\n'
           + ' '.join(f'.g{i}{{animation-delay:{.1 * i:.1f}s}}' for i in range(1, 7))
           + '\n    .cnt { opacity:0; animation: rise .8s cubic-bezier(.2,.7,.2,1) forwards; }\n'
           '    @media (prefers-reduced-motion: reduce){.grow{animation:none;transform:scaleX(1)}'
           '.cnt{animation:none;opacity:1}}')
    langs = [("PYTHON", 11, 270), ("HTML", 1, 25), ("JAVA", 1, 25)]
    bars = []
    for i, (name, n, w) in enumerate(langs, 1):
        y = 96 + (i - 1) * 36
        bars.append(
            f'    <text class="mono" x="48" y="{y+11}" font-size="10.5" fill="var(--muted)" letter-spacing="1.5">{name}</text>'
            f'<rect x="160" y="{y}" width="270" height="12" stroke="var(--rule)" stroke-width="1" fill="none"/>'
            f'<rect class="grow g{i}" x="160" y="{y}" width="{w}" height="12" fill="var(--accent)"/>'
            f'<text class="mono" x="446" y="{y+11}" font-size="10.5" fill="var(--dim)">{n}</text>')

    counters = [("18", "PUBLIC REPOS"), ("9", "ANALYTICS PROJECTS"),
                ("3", "AWS CERTS"), ("2026", "MS COMPLETED")]
    cnt = []
    for i, (big, small) in enumerate(counters):
        x = 560 + i * 108
        cnt.append(
            f'  <g class="cnt a{i+3}"><text class="mono" x="{x}" y="130" font-size="30" '
            f'fill="var(--bone)">{big}</text>'
            f'<text class="mono" x="{x}" y="150" font-size="9.5" fill="var(--muted)" '
            f'letter-spacing="1.2">{small}</text></g>')

    inner = f'''  <text class="mono fade a1" x="48" y="30" font-size="11" fill="var(--muted)" letter-spacing="3.5">TELEMETRY</text>
  <text class="mono fade a1" x="952" y="30" font-size="11" fill="var(--muted)" letter-spacing="3.5" text-anchor="end">FIG. 02</text>
  <line x1="48" y1="48" x2="952" y2="48" stroke="var(--rule)" stroke-width="1"/>

  <text class="mono fade a2" x="48" y="76" font-size="11" fill="var(--muted)" letter-spacing="2">LANGUAGE DISTRIBUTION BY REPOSITORY</text>
{chr(10).join(bars)}

  <text class="mono fade a2" x="560" y="76" font-size="11" fill="var(--muted)" letter-spacing="2">COUNTERS</text>
{chr(10).join(cnt)}

  <line x1="48" y1="212" x2="952" y2="212" stroke="var(--rule)" stroke-width="1" opacity=".5"/>
  <text class="mono fade a4" x="48" y="240" font-size="11" fill="var(--muted)" letter-spacing="2">PRIMARY TOOLING</text>
  <text class="mono fade a4" x="240" y="240" font-size="13" fill="var(--bone)">Python &#183; SQL &#183; R &#183; Tableau &#183; Power BI &#183; Excel</text>
  <text class="mono fade a5" x="48" y="270" font-size="11" fill="var(--muted)" letter-spacing="2">METHODS</text>
  <text class="mono fade a5" x="240" y="270" font-size="13" fill="var(--bone)">A/B testing &#183; regression &#183; mediation &#183; hypothesis testing</text>
  <text class="mono fade a6" x="48" y="300" font-size="11" fill="var(--muted)" letter-spacing="2">ACCOUNT SINCE</text>
  <text class="mono fade a6" x="240" y="300" font-size="13" fill="var(--bone)">October 2021</text>'''
    return shell(inner, 1000, 330, "Telemetry: languages, counters, tooling", css)


# ── github stats ───────────────────────────────────────────────────────────
def github_stats() -> str:
    css = ('.grow { transform:scaleX(0); transform-origin:left; '
           'animation:grow .8s cubic-bezier(.2,.7,.2,1) forwards; }\n'
           '    @keyframes grow { to { transform:scaleX(1); } }\n'
           '    .g2{animation-delay:.1s}.g3{animation-delay:.2s}\n'
           '    @media (prefers-reduced-motion:reduce){.grow{animation:none;transform:scaleX(1)}}')
    inner = '''  <rect x="24" y="20" width="456" height="270" rx="2" stroke="var(--rule)" stroke-width="1" fill="none"/>
  <rect x="520" y="20" width="456" height="270" rx="2" stroke="var(--rule)" stroke-width="1" fill="none"/>

  <g class="mono">
    <text x="52" y="58" font-size="15" font-weight="700" letter-spacing="2" fill="var(--bone)">GITHUB STATS</text>
    <line x1="52" y1="72" x2="452" y2="72" stroke="var(--rule)" stroke-width="1"/>
    <text x="52" y="110" font-size="11" letter-spacing="1" fill="var(--muted)">PUBLIC REPOSITORIES</text><text x="436" y="110" font-size="13" text-anchor="end" fill="var(--bone)">18</text>
    <text x="52" y="146" font-size="11" letter-spacing="1" fill="var(--muted)">TOTAL STARS</text><text x="436" y="146" font-size="13" text-anchor="end" fill="var(--bone)">2</text>
    <text x="52" y="182" font-size="11" letter-spacing="1" fill="var(--muted)">ANALYTICS PROJECTS</text><text x="436" y="182" font-size="13" text-anchor="end" fill="var(--bone)">9</text>
    <text x="52" y="218" font-size="11" letter-spacing="1" fill="var(--muted)">AWS CERTIFICATIONS</text><text x="436" y="218" font-size="13" text-anchor="end" fill="var(--bone)">3</text>
    <text x="52" y="254" font-size="11" letter-spacing="1" fill="var(--muted)">MEMBER SINCE</text><text x="436" y="254" font-size="13" text-anchor="end" fill="var(--bone)">2021</text>

    <text x="548" y="58" font-size="15" font-weight="700" letter-spacing="2" fill="var(--bone)">LANGUAGES BY REPOSITORY</text>
    <line x1="548" y1="72" x2="948" y2="72" stroke="var(--rule)" stroke-width="1"/>
    <text x="548" y="105" font-size="10" fill="var(--muted)">PYTHON</text><rect x="660" y="94" width="270" height="12" stroke="var(--rule)" stroke-width="1" fill="none"/><rect class="grow" x="660" y="94" width="270" height="12" fill="var(--accent)"/>
    <text x="548" y="141" font-size="10" fill="var(--muted)">HTML</text><rect x="660" y="130" width="270" height="12" stroke="var(--rule)" stroke-width="1" fill="none"/><rect class="grow g2" x="660" y="130" width="25" height="12" fill="var(--accent)"/>
    <text x="548" y="177" font-size="10" fill="var(--muted)">JAVA</text><rect x="660" y="166" width="270" height="12" stroke="var(--rule)" stroke-width="1" fill="none"/><rect class="grow g3" x="660" y="166" width="25" height="12" fill="var(--accent)"/>
    <text x="548" y="222" font-size="10" fill="var(--dim)">SQL, R, TABLEAU AND POWER BI WORK LIVES INSIDE</text>
    <text x="548" y="240" font-size="10" fill="var(--dim)">NOTEBOOKS AND WORKBOOKS, NOT AS REPO LANGUAGES.</text>
  </g>'''
    return shell(inner, 1000, 310, "GitHub statistics and repository languages", css)


# ── timeline ───────────────────────────────────────────────────────────────
def timeline() -> str:
    css = ('.axis { stroke: var(--rule); stroke-width: 1; stroke-dasharray: 1110; '
           'stroke-dashoffset: 1110; animation: dax 2.4s cubic-bezier(.6,0,.2,1) forwards; }\n'
           '    @keyframes dax { to { stroke-dashoffset: 0; } }\n'
           '    .m { opacity: 0; animation: rise .7s cubic-bezier(.2,.7,.2,1) forwards; }\n'
           + ' '.join(f'.m{i}{{animation-delay:{.4 + i * .35:.2f}s}}' for i in range(1, 7))
           + '\n    .pulse { animation: pl 2.6s ease-in-out infinite; }\n'
           '    @keyframes pl { 0%,100%{opacity:1} 50%{opacity:.35} }\n'
           '    .ring { animation: rg 2.6s ease-out infinite; transform-origin: 1060px 125px; }\n'
           '    @keyframes rg { 0%{transform:scale(.4);opacity:.8} 80%,100%{transform:scale(3);opacity:0} }\n'
           '    @media (prefers-reduced-motion: reduce){.axis,.m,.pulse,.ring{animation:none}'
           '.axis{stroke-dashoffset:0}.m{opacity:1}.ring{opacity:0}}')

    def mk(cx, year, label, up, cls):
        if up:
            tick = f'<line x1="{cx}" y1="121" x2="{cx}" y2="96" stroke="var(--rule)"/>'
            ty, ly = 74, 90
        else:
            tick = f'<line x1="{cx}" y1="129" x2="{cx}" y2="154" stroke="var(--rule)"/>'
            ty, ly = 172, 188
        return f'''  <g class="m {cls}">
    <circle cx="{cx}" cy="125" r="4" fill="var(--bone)"/>
    {tick}
    <text fill="var(--accent)" class="mono" x="{cx}" y="{ty}" font-size="11" letter-spacing="2" text-anchor="middle">{year}</text>
    <text fill="var(--bone)" class="mono" x="{cx}" y="{ly}" font-size="10.5" letter-spacing="1" text-anchor="middle">{label}</text>
  </g>'''

    inner = f'''  <line x1="48" y1="40" x2="1152" y2="40" stroke="var(--rule)"/>
  <text fill="var(--muted)" class="mono" x="48" y="28" font-size="11" letter-spacing="3.5">THE ROUTE SO FAR</text>
  <text fill="var(--muted)" class="mono" x="1152" y="28" font-size="11" letter-spacing="3.5" text-anchor="end">FIG. 03</text>

  <line class="axis" x1="48" y1="125" x2="1158" y2="125"/>

{mk(120, "2020", "B.E. Computer Science &#183; KL University", True, "m1")}
{mk(340, "2022", "Data Analytics Intern &#183; AICTE", False, "m2")}
{mk(560, "2024", "MS Business Analytics &#183; CSUN", True, "m3")}
{mk(780, "2026", "capstone &#183; influencer engagement study", False, "m4")}
{mk(940, "2026", "FAFSA A/B testing experiment", True, "m5")}

  <g class="m m6">
    <circle class="ring" cx="1060" cy="125" r="5" stroke="var(--accent)" stroke-width="1" fill="none"/>
    <circle class="pulse" cx="1060" cy="125" r="4" fill="var(--accent)"/>
    <line x1="1060" y1="129" x2="1060" y2="154" stroke="var(--rule)"/>
    <text fill="var(--accent)" class="mono" x="1060" y="172" font-size="11" letter-spacing="2" text-anchor="middle">NOW</text>
    <text fill="var(--bone)" class="mono" x="1060" y="188" font-size="10.5" letter-spacing="1" text-anchor="middle">open to analyst roles</text>
  </g>'''
    return shell(inner, 1200, 250, "Timeline from 2020 to now", css)


# ── experience ─────────────────────────────────────────────────────────────
def experience() -> str:
    inner = '''  <line x1="120" y1="10" x2="120" y2="360" stroke="var(--rule)" stroke-width="1" opacity=".4"/>

  <g class="rise a1">
    <text class="mono" x="48" y="42"  font-size="12" fill="var(--accent)" letter-spacing="2">2026</text>
    <text class="mono" x="136" y="42"  font-size="15" fill="var(--bone)">CSUN &#183; Graduate Capstone &#183; Business Analytics</text>
    <text class="mono" x="136" y="68"  font-size="14" fill="var(--muted)">requirements gathering &#8594; gap analysis &#8594; cost-benefit framing &#8594; recommendation</text>
    <text class="mono" x="136" y="90"  font-size="14" fill="var(--muted)">Tableau and Power BI dashboards built for non-technical stakeholders</text>
  </g>

  <g class="rise a2">
    <text class="mono" x="48" y="138" font-size="12" fill="var(--accent)" letter-spacing="2">2026</text>
    <text class="mono" x="136" y="138" font-size="15" fill="var(--bone)">Independent Research &#183; FAFSA Nudge Experiment</text>
    <text class="mono" x="136" y="164" font-size="14" fill="var(--muted)">pre-registered A/B design with power analysis and reproducibility checks</text>
    <text class="mono" x="136" y="186" font-size="14" fill="var(--muted)">stakeholder memo written for decision makers, not for statisticians</text>
  </g>

  <g class="rise a3">
    <text class="mono" x="48" y="234" font-size="12" fill="var(--accent)" letter-spacing="2">2022</text>
    <text class="mono" x="136" y="234" font-size="15" fill="var(--bone)">AICTE &#183; Data Analytics Intern &#183; National Internship Program</text>
    <text class="mono" x="136" y="260" font-size="14" fill="var(--muted)">analysed structured datasets in Python, R and SQL for decision support</text>
    <text class="mono" x="136" y="282" font-size="14" fill="var(--muted)">presented findings to cross-functional stakeholders and peer teams</text>
  </g>

  <g class="rise a4">
    <text class="mono" x="48" y="330" font-size="12" fill="var(--accent)" letter-spacing="2">2020 &#8211;</text>
    <text class="mono" x="136" y="330" font-size="15" fill="var(--bone)">KL University &#183; B.E. Computer Science (Honors)</text>
    <text class="mono" x="136" y="356" font-size="14" fill="var(--muted)">published: edge computing in 5G for AR/VR data prediction (WCONF2023)</text>
  </g>'''
    return shell(inner, 1000, 370, "Experience — CSUN, AICTE, KL University")


# ── stack ──────────────────────────────────────────────────────────────────
def stack() -> str:
    css = ' '.join(f'.s{i}{{animation-delay:{.1 * i:.1f}s}}' for i in range(1, 8))
    rows = [
        ("LANGUAGES", "Python &#183; SQL &#183; R"),
        ("BI &amp; VIZ", "Tableau &#183; Power BI &#183; Excel &#183; dashboard design"),
        ("STATISTICS", "regression &#183; mediation &#183; moderation &#183; hypothesis testing"),
        ("EXPERIMENTS", "A/B testing &#183; causal inference &#183; power analysis"),
        ("DATA", "MySQL &#183; data cleaning &#183; EDA &#183; feature engineering"),
        ("CLOUD", "AWS (&#215;3 certified) &#183; Azure"),
        ("PROCESS", "requirements gathering &#183; gap analysis &#183; UAT &#183; Agile"),
    ]
    body = []
    for i, (k, v) in enumerate(rows, 1):
        y = 32 + (i - 1) * 32
        body.append(
            f'  <text class="mono rise s{i}" x="48" y="{y}" font-size="12" fill="var(--muted)" letter-spacing="2">{k}</text>\n'
            f'  <text class="mono rise s{i}" x="180" y="{y}" font-size="15" fill="var(--bone)">{v}</text>')
    inner = ('  <line x1="164" y1="8" x2="164" y2="230" stroke="var(--rule)" stroke-width="1" opacity=".4"/>\n\n'
             + "\n\n".join(body))
    return shell(inner, 1000, 238, "Stack — languages, BI, statistics, cloud", css)


# ── now (marquee) ──────────────────────────────────────────────────────────
def now() -> str:
    css = ('.belt { animation: belt 36s linear infinite; }\n'
           '    @keyframes belt { from{transform:translateX(0)} to{transform:translateX(-1560px)} }\n'
           '    .dot { animation: pulse 2.4s ease-in-out infinite; }\n'
           '    @keyframes pulse { 0%,100%{opacity:1} 50%{opacity:.25} }\n'
           '    @media (prefers-reduced-motion: reduce) { .belt,.dot { animation: none; } }')
    seg = ('<tspan fill="var(--accent)">NOW&#160;&#160;&#9656;&#160;&#160;</tspan>'
           '<tspan fill="var(--bone)">MS BUSINESS ANALYTICS &#183; CSUN 2026</tspan>'
           '<tspan fill="var(--accent)">&#160;&#160;&#160;&#10038;&#160;&#160;&#160;</tspan>'
           '<tspan fill="var(--bone)">BUSINESS &#183; BI &#183; DATA ANALYST</tspan>'
           '<tspan fill="var(--accent)">&#160;&#160;&#160;&#10038;&#160;&#160;&#160;</tspan>'
           '<tspan fill="var(--bone)">A/B TESTING &#183; CAUSAL INFERENCE</tspan>'
           '<tspan fill="var(--accent)">&#160;&#160;&#160;&#10038;&#160;&#160;&#160;</tspan>'
           '<tspan fill="var(--bone)">OPEN TO ENTRY-LEVEL ANALYST ROLES</tspan>'
           '<tspan fill="var(--accent)">&#160;&#160;&#160;&#10038;&#160;&#160;&#160;</tspan>')
    inner = f'''  <line x1="0" y1="0.5" x2="1000" y2="0.5" stroke="var(--rule)"/>
  <line x1="0" y1="63.5" x2="1000" y2="63.5" stroke="var(--rule)"/>
  <g class="belt">
    <text class="mono" x="60" y="38" font-size="13" letter-spacing="2">{seg}</text>
    <text class="mono" x="1620" y="38" font-size="13" letter-spacing="2">{seg}</text>
  </g>'''
    return shell(inner, 1000, 64, "Now — status marquee", css)


# ── footer ─────────────────────────────────────────────────────────────────
def footer() -> str:
    css = ('.dw { stroke: var(--rule); stroke-width: 1; stroke-dasharray: 1000; '
           'stroke-dashoffset: 1000; animation: dw 1.6s cubic-bezier(.6,0,.2,1) forwards; }\n'
           '    @keyframes dw { to { stroke-dashoffset: 0; } }\n'
           '    .dot { animation: p 2.4s ease-in-out infinite; }\n'
           '    .ring { animation: r 2.4s ease-out infinite; transform-origin: 60px 64px; }\n'
           '    @keyframes p { 0%,100%{opacity:1} 50%{opacity:.35} }\n'
           '    @keyframes r { 0%{transform:scale(.4);opacity:.8} 80%,100%{transform:scale(2.6);opacity:0} }\n'
           '    @media (prefers-reduced-motion: reduce){.dw,.dot,.ring{animation:none}'
           '.dw{stroke-dashoffset:0}.ring{opacity:0}}')
    inner = '''  <line class="dw" x1="48" y1="24" x2="952" y2="24"/>
  <circle class="ring" cx="60" cy="64" r="5" stroke="var(--accent)" stroke-width="1" fill="none"/>
  <circle class="dot" cx="60" cy="64" r="4" fill="var(--accent)"/>
  <text class="mono" x="82" y="62" font-size="12" letter-spacing="3" fill="var(--bone)">STATUS &#8212; OPEN TO WORK</text>
  <text class="mono" x="82" y="82" font-size="11" letter-spacing="2" fill="var(--muted)">business analyst &#183; bi analyst &#183; data analyst</text>
  <text class="mono" x="952" y="66" font-size="15" text-anchor="end" fill="var(--muted)">Fremont, CA&#160;&#160;&#183;&#160;&#160;&#169; 2026</text>'''
    return shell(inner, 1000, 110, "Status: open to work. Fremont, CA.", css)


print("writing assets:")
write("header-v1.svg", header())
write("s01.svg", section("01", "WHOAMI", "01-whoami"))
write("whoami.svg", whoami())
write("s02.svg", section("02", "SYSTEM MAP", "02-system-map"))
write("ecosystem.svg", ecosystem())
write("s03.svg", section("03", "PROJECTS", "03-projects"))
write("projects.svg", projects())
write("s04.svg", section("04", "TELEMETRY", "04-telemetry"))
write("telemetry.svg", telemetry())
write("github-stats.svg", github_stats())
write("s05.svg", section("05", "THE ROUTE", "05-route"))
write("timeline.svg", timeline())
write("experience.svg", experience())
write("s06.svg", section("06", "STACK", "06-stack"))
write("stack.svg", stack())
write("now.svg", now())
write("footer.svg", footer())
print("done")
