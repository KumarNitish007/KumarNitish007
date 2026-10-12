"""
Generates the profile's SVG artwork (light + dark variants) into ../assets.
Pure SVG + CSS animations: no external services, fonts or scripts, so the images
render reliably on GitHub (which proxies README images through its camo cache).

    python scripts/generate_assets.py
"""
from pathlib import Path
from xml.sax.saxutils import escape

OUT = Path(__file__).resolve().parent.parent / "assets"
OUT.mkdir(exist_ok=True)

SANS = "-apple-system,BlinkMacSystemFont,'Segoe UI',Ubuntu,Helvetica,Arial,sans-serif"
MONO = "ui-monospace,SFMono-Regular,'Cascadia Code',Consolas,'Liberation Mono',monospace"

THEMES = {
    "dark": dict(bg1="#0d1117", bg2="#161b2e", card="#161b22", border="#30363d", text="#e6edf3",
                 muted="#8b949e", grid="#ffffff", grid_op=0.035, glow1="#6366f1", glow2="#06b6d4", pill="#21262d"),
    "light": dict(bg1="#ffffff", bg2="#f3f6ff", card="#ffffff", border="#d0d7de", text="#1f2328",
                  muted="#57606a", grid="#0b1f44", grid_op=0.045, glow1="#818cf8", glow2="#22d3ee", pill="#eef1f6"),
}
ACCENTS = ["#6366f1", "#06b6d4", "#a855f7", "#f59e0b", "#10b981", "#ec4899"]


def save(name: str, svg: str) -> None:
    (OUT / name).write_text(svg, encoding="utf-8")
    print("wrote", name)


# --------------------------------------------------------------------------------------------- header

TAGLINES = [
    "Building ERP platforms with .NET 8, Angular 19 and SQL Server",
    "Designing event-driven microservices with sagas and outboxes",
    "Shipping AI document search with Claude and hybrid retrieval",
    "Making SQL Server backups you can actually restore",
    "Publishing IndiaKit: GST, PAN and Aadhaar tooling for .NET",
]


def header(theme: str) -> str:
    t = THEMES[theme]
    n = len(TAGLINES)
    cycle = 4 * n  # seconds; each line shows for 4s
    lines = []
    for i, line in enumerate(TAGLINES):
        lines.append(
            f'<text class="tag" x="64" y="214" style="animation-delay:{i * 4}s">'
            f'<tspan class="prompt">&gt; </tspan>{escape(line)}</text>'
        )
    # keyframe: visible for 1/n of the cycle, with quick fades
    show = 100 / n
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="300" viewBox="0 0 1200 300" role="img" aria-label="Nitish Kumar - Senior .NET and Angular Full Stack Developer">
  <title>Nitish Kumar - Senior .NET and Angular Full Stack Developer</title>
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="{t['bg1']}"/><stop offset="1" stop-color="{t['bg2']}"/>
    </linearGradient>
    <linearGradient id="name" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="#6366f1"/><stop offset="0.5" stop-color="#a855f7"/><stop offset="1" stop-color="#06b6d4"/>
    </linearGradient>
    <radialGradient id="g1"><stop offset="0" stop-color="{t['glow1']}" stop-opacity="0.45"/><stop offset="1" stop-color="{t['glow1']}" stop-opacity="0"/></radialGradient>
    <radialGradient id="g2"><stop offset="0" stop-color="{t['glow2']}" stop-opacity="0.35"/><stop offset="1" stop-color="{t['glow2']}" stop-opacity="0"/></radialGradient>
    <pattern id="grid" width="32" height="32" patternUnits="userSpaceOnUse">
      <path d="M32 0H0V32" fill="none" stroke="{t['grid']}" stroke-opacity="{t['grid_op']}" stroke-width="1"/>
    </pattern>
    <clipPath id="clip"><rect width="1200" height="300" rx="18"/></clipPath>
  </defs>
  <style>
    .name {{ font: 800 64px {SANS}; letter-spacing: -1.5px; }}
    .role {{ font: 600 24px {SANS}; fill: {t['text']}; }}
    .meta {{ font: 500 16px {SANS}; fill: {t['muted']}; }}
    .tag {{ font: 500 18px {MONO}; fill: {t['text']}; opacity: 0; animation: cycle {cycle}s infinite; }}
    .prompt {{ fill: #10b981; }}
    .caret {{ fill: #10b981; animation: blink 1s steps(2) infinite; }}
    .orb1 {{ animation: drift 14s ease-in-out infinite alternate; }}
    .orb2 {{ animation: drift 18s ease-in-out infinite alternate-reverse; }}
    .ring {{ fill: none; stroke: url(#name); stroke-width: 2; stroke-dasharray: 6 10; animation: spin 40s linear infinite; transform-origin: 1010px 150px; }}
    .code {{ font: 500 14px {MONO}; fill: {t['muted']}; }}
    .k {{ fill: #a855f7; }} .s {{ fill: #10b981; }} .n {{ fill: #f59e0b; }} .p {{ fill: {t['text']}; }}
    @keyframes cycle {{
      0% {{ opacity: 0; transform: translateY(6px); }}
      3% {{ opacity: 1; transform: translateY(0); }}
      {show - 3:.2f}% {{ opacity: 1; transform: translateY(0); }}
      {show:.2f}% {{ opacity: 0; transform: translateY(-6px); }}
      100% {{ opacity: 0; }}
    }}
    @keyframes blink {{ 50% {{ opacity: 0; }} }}
    @keyframes drift {{ from {{ transform: translate(0,0); }} to {{ transform: translate(40px,18px); }} }}
    @keyframes spin {{ to {{ transform: rotate(360deg); }} }}
    @media (prefers-reduced-motion: reduce) {{ .tag {{ animation: none; }} .tag:first-of-type {{ opacity: 1; }} .orb1,.orb2,.ring,.caret {{ animation: none; }} }}
  </style>
  <g clip-path="url(#clip)">
    <rect width="1200" height="300" fill="url(#bg)"/>
    <rect width="1200" height="300" fill="url(#grid)"/>
    <circle class="orb1" cx="180" cy="40" r="220" fill="url(#g1)"/>
    <circle class="orb2" cx="1060" cy="270" r="240" fill="url(#g2)"/>
    <rect x="0.5" y="0.5" width="1199" height="299" rx="18" fill="none" stroke="{t['border']}"/>
  </g>

  <text class="meta" x="64" y="70">Hi there, I'm</text>
  <text class="name" x="60" y="132" fill="url(#name)">Nitish Kumar</text>
  <text class="role" x="64" y="172">Senior .NET &amp; Angular Full Stack Developer</text>
  {''.join(lines)}
  <text class="meta" x="64" y="262">6+ years · ERP · Healthcare · Pune, India · Open to work</text>

  <!-- right: a little class in the style of the portfolio -->
  <circle class="ring" cx="1010" cy="150" r="118"/>
  <g transform="translate(860,72)">
    <rect width="300" height="156" rx="12" fill="{t['card']}" stroke="{t['border']}"/>
    <circle cx="20" cy="18" r="5" fill="#ff5f57"/><circle cx="38" cy="18" r="5" fill="#febc2e"/><circle cx="56" cy="18" r="5" fill="#28c840"/>
    <text class="code" x="18" y="54"><tspan class="k">var</tspan><tspan class="p"> me = new</tspan><tspan class="k"> Developer</tspan><tspan class="p">{{</tspan></text>
    <text class="code" x="34" y="78"><tspan class="p">Stack = </tspan><tspan class="s">".NET 8 + Angular 19"</tspan><tspan class="p">,</tspan></text>
    <text class="code" x="34" y="100"><tspan class="p">Years = </tspan><tspan class="n">6</tspan><tspan class="p">,</tspan></text>
    <text class="code" x="34" y="122"><tspan class="p">OpenToWork = </tspan><tspan class="k">true</tspan></text>
    <text class="code" x="18" y="144"><tspan class="p">}};</tspan><tspan class="caret"> ▌</tspan></text>
  </g>
</svg>
"""


# ------------------------------------------------------------------------------------------- projects

PROJECTS = [
    dict(file="project-minierp", title="MiniERP", accent=ACCENTS[0], kicker="Multi-tenant SaaS",
         lines=["Inventory & GST invoicing: CGST/SGST/IGST, gap-free", "numbering, PDF invoices, live dashboard."],
         tags=[".NET 8", "Angular 19", "SQL Server", "Dapper"]),
    dict(file="project-orderflow", title="OrderFlow", accent=ACCENTS[1], kicker="Event-driven microservices",
         lines=["Saga-orchestrated orders with compensation,", "transactional outbox and distributed tracing."],
         tags=[".NET Aspire", "RabbitMQ", "MassTransit", "YARP"]),
    dict(file="project-askdocs", title="AskDocs", accent=ACCENTS[2], kicker="AI document Q&A (RAG)",
         lines=["Hybrid BM25 + vector search, streaming answers", "with page-level citations. Claude / Ollama."],
         tags=["Claude", "RAG", ".NET 8", "Angular 19"]),
    dict(file="project-sqlbackup", title="SqlBackupAgent", accent=ACCENTS[3], kicker="SQL Server reliability",
         lines=["Scheduled backups, chain-safe retention, LSN-based", "point-in-time restores and restore drills."],
         tags=["SQL Server", "Azure Blob", "Windows Service", "CLI"]),
    dict(file="project-indiakit", title="IndiaKit", accent=ACCENTS[4], kicker="NuGet package",
         lines=["GSTIN/PAN/Aadhaar validation with real checksums,", "lakh/crore formatting, GST maths, financial years."],
         tags=["NuGet", "netstandard2.0", ".NET 8", "105 tests"]),
]

def project_card(p: dict, theme: str) -> str:
    t = THEMES[theme]
    pills, x = [], 24
    for tag in p["tags"]:
        w = 14 + len(tag) * 7.4
        pills.append(f'<rect x="{x}" y="150" width="{w:.0f}" height="26" rx="13" fill="{t["pill"]}" stroke="{t["border"]}"/>'
                     f'<text class="pill" x="{x + w / 2:.0f}" y="167" text-anchor="middle">{escape(tag)}</text>')
        x += w + 8
    body = "".join(f'<text class="desc" x="24" y="{104 + i * 22}">{escape(l)}</text>' for i, l in enumerate(p["lines"]))
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="440" height="200" viewBox="0 0 440 200" role="img" aria-label="{escape(p['title'])} - {escape(p['kicker'])}">
  <title>{escape(p['title'])} - {escape(p['kicker'])}</title>
  <style>
    .title {{ font: 700 22px {SANS}; fill: {t['text']}; }}
    .kicker {{ font: 600 12px {SANS}; fill: {p['accent']}; letter-spacing: 1.2px; text-transform: uppercase; }}
    .desc {{ font: 400 14px {SANS}; fill: {t['muted']}; }}
    .pill {{ font: 500 12px {SANS}; fill: {t['text']}; }}
    .arrow {{ font: 600 18px {SANS}; fill: {p['accent']}; }}
    .card {{ transition: stroke .2s; }}
  </style>
  <defs><linearGradient id="a" x1="0" x2="1"><stop offset="0" stop-color="{p['accent']}"/><stop offset="1" stop-color="{p['accent']}" stop-opacity="0.2"/></linearGradient></defs>
  <rect class="card" x="0.5" y="0.5" width="439" height="199" rx="14" fill="{t['card']}" stroke="{t['border']}"/>
  <rect x="0.5" y="0.5" width="439" height="5" rx="2.5" fill="url(#a)"/>
  <text class="kicker" x="24" y="38">{escape(p['kicker'])}</text>
  <text class="title" x="24" y="70">{escape(p['title'])}</text>
  <text class="arrow" x="410" y="70" text-anchor="end">↗</text>
  {body}
  {''.join(pills)}
</svg>
"""


# ------------------------------------------------------------------------------------------- timeline

JOBS = [
    ("2019", "Feb 2021", "Glyphisoft Technology", ".NET Developer", "ERP modules · ASP.NET Core MVC"),
    ("2021", "May 2022", "Reliance Jio", "Executive Engineer", "Telecom network rollout"),
    ("2022", "Aug 2024", "Medimaze Solution", "Software Developer", "Healthcare ERP · Krsnaa, ABHA"),
    ("2024", "Present", "Orient Technology", ".NET Developer", "EPC ERP · .NET 8 + Angular 19"),
]


def timeline(theme: str) -> str:
    t = THEMES[theme]
    step, x0 = 280, 120
    nodes = []
    for i, (start, end, company, role, detail) in enumerate(JOBS):
        x = x0 + i * step
        current = end == "Present"
        color = ACCENTS[i % len(ACCENTS)]
        pulse = f'<circle cx="{x}" cy="92" r="9" fill="none" stroke="{color}" stroke-width="2" class="pulse"/>' if current else ""
        nodes.append(f"""
    <g>
      {pulse}
      <circle cx="{x}" cy="92" r="9" fill="{t['card']}" stroke="{color}" stroke-width="3"/>
      <circle cx="{x}" cy="92" r="3.5" fill="{color}"/>
      <text class="year" x="{x}" y="58" text-anchor="middle" fill="{color}">{start}</text>
      <text class="company" x="{x}" y="134" text-anchor="middle">{escape(company)}</text>
      <text class="role" x="{x}" y="158" text-anchor="middle">{escape(role)}</text>
      <text class="detail" x="{x}" y="180" text-anchor="middle">{escape(detail)}</text>
      <text class="period" x="{x}" y="202" text-anchor="middle">{start} – {end}</text>
    </g>""")
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="230" viewBox="0 0 1200 230" role="img" aria-label="Career timeline">
  <title>Career timeline: 2019 to present</title>
  <style>
    .year {{ font: 800 22px {SANS}; }}
    .company {{ font: 700 16px {SANS}; fill: {t['text']}; }}
    .role {{ font: 600 14px {SANS}; fill: {t['text']}; opacity: .85; }}
    .detail {{ font: 400 13px {SANS}; fill: {t['muted']}; }}
    .period {{ font: 500 12px {MONO}; fill: {t['muted']}; }}
    .line {{ stroke-dasharray: 1000; stroke-dashoffset: 1000; animation: draw 2.4s ease-out forwards; }}
    .pulse {{ transform-box: fill-box; transform-origin: center; animation: pulse 2s ease-out infinite; }}
    @keyframes draw {{ to {{ stroke-dashoffset: 0; }} }}
    @keyframes pulse {{ 0% {{ transform: scale(1); opacity: .9; }} 100% {{ transform: scale(2.6); opacity: 0; }} }}
    @media (prefers-reduced-motion: reduce) {{ .line {{ animation: none; stroke-dashoffset: 0; }} .pulse {{ animation: none; }} }}
  </style>
  <defs><linearGradient id="tl" x1="0" x2="1"><stop offset="0" stop-color="{ACCENTS[0]}"/><stop offset="0.5" stop-color="{ACCENTS[2]}"/><stop offset="1" stop-color="{ACCENTS[3]}"/></linearGradient></defs>
  <rect x="0.5" y="0.5" width="1199" height="229" rx="16" fill="{t['card']}" stroke="{t['border']}"/>
  <line class="line" x1="{x0}" y1="92" x2="{x0 + step * (len(JOBS) - 1)}" y2="92" stroke="url(#tl)" stroke-width="3" stroke-linecap="round"/>
  {''.join(nodes)}
</svg>
"""


# ------------------------------------------------------------------------------------------- divider

def divider(theme: str) -> str:
    return """<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="6" viewBox="0 0 1200 6" role="presentation">
  <defs><linearGradient id="d" x1="0" x2="1"><stop offset="0" stop-color="#6366f1" stop-opacity="0"/><stop offset=".5" stop-color="#a855f7"/><stop offset="1" stop-color="#06b6d4" stop-opacity="0"/></linearGradient></defs>
  <rect width="1200" height="2" y="2" rx="1" fill="url(#d)"/>
</svg>
"""


if __name__ == "__main__":
    for theme in THEMES:
        save(f"header-{theme}.svg", header(theme))
        save(f"timeline-{theme}.svg", timeline(theme))
        for p in PROJECTS:
            save(f"{p['file']}-{theme}.svg", project_card(p, theme))
    save("divider.svg", divider("dark"))
