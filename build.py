#!/usr/bin/env python3
"""
TCM AI Operational Efficiency Database — static site generator.

Reads data/state.json (the machine-readable rendering of the ledger) and
writes docs/*.html. The ledger remains the source of truth; this only renders.

Usage:  python3 build.py
"""

import json, os, re, shutil, html
from datetime import date, datetime
from pathlib import Path

ROOT = Path(__file__).parent
DATA = ROOT / "data" / "state.json"
OUT = ROOT / "docs"

# ---------------------------------------------------------------- brand
PURPLE      = "#4A1A6B"
PURPLE_MID  = "#69398D"
BAND_A      = "#2D0F4D"
BAND_B      = "#6D2EA3"
GOLD        = "#C5A421"
GREEN       = "#1E8050"
RED         = "#B3261E"
TEAL        = "#1F6F6B"
ZEBRA       = "#F6F4F9"
INK         = "#1F1F1F"
GRAY        = "#6B6B6B"

CSS = f"""
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:'Times New Roman','Liberation Serif',Georgia,serif;color:{INK};
      background:#fff;line-height:1.5;-webkit-font-smoothing:antialiased}}
.wrap{{max-width:1180px;margin:0 auto;padding:0 28px}}
a{{color:{PURPLE};text-decoration:none}}
a:hover{{text-decoration:underline}}
.sans{{font-family:Arial,'Liberation Sans',Helvetica,sans-serif}}

/* masthead */
.band{{background:linear-gradient(135deg,{BAND_A} 0%,{BAND_B} 100%);
       border-bottom:4px solid {GOLD};padding:30px 0 26px}}
.eyebrow{{font-family:Arial,'Liberation Sans',sans-serif;font-size:11px;letter-spacing:.18em;
          color:{GOLD};font-weight:700;text-transform:uppercase}}
.eyebrow span{{color:#C7B3DE;font-weight:400}}
h1.title{{color:#fff;font-size:31px;font-weight:700;margin:9px 0 5px;letter-spacing:-.01em}}
.sub{{color:#D6C7E8;font-size:14px;font-style:italic}}
.meta{{color:#B49CCF;font-size:11.5px;margin-top:11px;font-family:Arial,sans-serif;letter-spacing:.03em}}

/* nav */
nav{{border-bottom:1px solid #E3DEE9;background:#FCFBFD}}
nav .wrap{{display:flex;gap:26px;flex-wrap:wrap}}
nav a{{font-family:Arial,sans-serif;font-size:12px;letter-spacing:.06em;text-transform:uppercase;
       color:{GRAY};padding:13px 0;font-weight:600;border-bottom:3px solid transparent;
       margin-bottom:-1px;text-decoration:none}}
nav a:hover{{color:{PURPLE};text-decoration:none}}
nav a.on{{color:{PURPLE};border-bottom-color:{GOLD}}}

/* metric strip */
.strip{{display:flex;border-top:1px solid #DDD8E4;border-bottom:1px solid #DDD8E4;margin:26px 0 30px}}
.card{{flex:1;padding:15px 14px;border-right:1px solid #E8E4EE;text-align:center}}
.card:last-child{{border-right:none}}
.card .lab{{font-family:Arial,sans-serif;font-size:9.5px;letter-spacing:.12em;color:{GRAY};
            text-transform:uppercase;font-weight:700}}
.card .val{{font-size:29px;color:{GOLD};font-weight:700;line-height:1.15;margin-top:3px}}
.card .note{{font-size:10.5px;color:{GRAY};font-family:Arial,sans-serif;margin-top:2px}}

/* sections */
h2{{font-family:Arial,sans-serif;font-size:16px;color:{PURPLE};margin:34px 0 4px;
    text-transform:uppercase;letter-spacing:.05em;display:flex;align-items:center;gap:9px}}
h2:before{{content:'';width:11px;height:11px;background:{PURPLE};display:inline-block;flex:none}}
h3{{font-family:Arial,sans-serif;font-size:13.5px;color:{PURPLE_MID};margin:22px 0 6px;font-weight:700}}
p{{margin:9px 0;font-size:14.5px}}
p.lede{{font-size:15px;color:#333}}
.rule{{height:1px;background:#E3DEE9;margin:8px 0 16px}}

/* tables */
table{{width:100%;border-collapse:collapse;margin:14px 0;font-size:13px}}
thead th{{background:{PURPLE};color:#fff;font-family:Arial,sans-serif;font-size:10px;
          letter-spacing:.07em;text-transform:uppercase;padding:9px 10px;text-align:left;
          font-weight:700;white-space:nowrap}}
thead th.num{{text-align:right}}
thead th.sortable{{cursor:pointer;user-select:none}}
thead th.sortable:hover{{background:{PURPLE_MID}}}
tbody td{{padding:8px 10px;border-bottom:1px solid #EDEAF1;vertical-align:top}}
tbody tr:nth-child(even){{background:{ZEBRA}}}
tbody tr:hover{{background:#F0EBF6}}
td.num{{text-align:right;font-variant-numeric:tabular-nums}}
td.tick{{font-weight:700;font-family:Arial,sans-serif;font-size:12.5px;white-space:nowrap}}
td.sm{{font-size:11.5px;color:{GRAY};font-family:Arial,sans-serif}}

/* badges */
.b{{display:inline-block;font-family:Arial,sans-serif;font-size:9.5px;font-weight:700;
    letter-spacing:.08em;text-transform:uppercase;padding:2.5px 7px;border-radius:2px;white-space:nowrap}}
.b-realized{{background:#EFF5F1;color:{GREEN};border:1px solid #278050}}
.b-plan{{background:#FBF7EC;color:#9A7B12;border:1px solid #C9B27A}}
.b-cut{{background:#FBEEEE;color:{RED};border:1px solid #D9A6A2}}
.b-outside{{background:#F2F2F4;color:{GRAY};border:1px solid #D5D2DA}}
.b-pending{{background:#EAF4F3;color:{TEAL};border:1px solid #1F6F6B}}

.score{{font-weight:700;font-family:Arial,sans-serif;font-size:14px}}
.s-hi{{color:{GREEN}}} .s-mid{{color:#9A7B12}} .s-lo{{color:{RED}}}

/* boxes */
.box{{border-left:4px solid;padding:11px 14px;margin:14px 0;font-size:13.5px}}
.box .h{{font-family:Arial,sans-serif;font-size:10px;font-weight:700;letter-spacing:.1em;
         text-transform:uppercase;margin-bottom:4px}}
.box-signal{{border-color:#278050;background:#EFF5F1}} .box-signal .h{{color:{GREEN}}}
.box-persp{{border-color:#C9B27A;background:#FBF7EC}}  .box-persp .h{{color:#9A7B12}}
.box-push{{border-color:{TEAL};background:#EAF4F3}}    .box-push .h{{color:{TEAL}}}

blockquote{{border-left:4px solid {PURPLE};background:#FAF8FC;padding:11px 15px;margin:12px 0;
            font-style:italic;font-size:14px}}
blockquote .attr{{font-style:normal;font-family:Arial,sans-serif;font-size:10px;color:{GRAY};
                  text-transform:uppercase;letter-spacing:.07em;margin-top:6px;display:block}}

/* controls */
.controls{{display:flex;gap:10px;flex-wrap:wrap;align-items:center;margin:16px 0 4px}}
input[type=search],select{{font-family:Arial,sans-serif;font-size:12.5px;padding:7px 10px;
   border:1px solid #D5D2DA;border-radius:3px;background:#fff;color:{INK}}}
input[type=search]{{min-width:270px}}
.count{{font-family:Arial,sans-serif;font-size:11.5px;color:{GRAY};margin-left:auto}}

footer{{margin:50px 0 34px;padding-top:16px;border-top:1px solid #E3DEE9;
        font-size:11px;color:{GRAY};font-style:italic}}
.kv{{display:grid;grid-template-columns:190px 1fr;gap:5px 16px;font-size:13.5px;margin:12px 0}}
.kv dt{{font-family:Arial,sans-serif;font-size:10.5px;letter-spacing:.07em;text-transform:uppercase;
        color:{GRAY};font-weight:700;padding-top:2px}}
.empty{{color:{GRAY};font-style:italic;font-size:13.5px;padding:14px 0}}
@media(max-width:820px){{
  .strip{{flex-wrap:wrap}} .card{{flex:0 0 33.33%;border-bottom:1px solid #E8E4EE}}
  .kv{{grid-template-columns:1fr}} h1.title{{font-size:24px}}
}}
"""

NAV = [
    ("index.html",       "The Database"),
    ("nearmisses.html",  "Near Misses"),
    ("evidence.html",    "Evidence Log"),
    ("rejections.html",  "Rejections"),
    ("universe.html",    "Universe (345)"),
    ("methodology.html", "Methodology"),
    ("runlog.html",      "Run Log"),
]


def esc(s):
    return html.escape(str(s if s is not None else ""))


def shell(title, subtitle, active, body, depth=0, meta_line=None):
    up = "../" * depth
    nav = "".join(
        f'<a href="{up}{h}" class="{"on" if h == active else ""}">{esc(l)}</a>'
        for h, l in NAV
    )
    meta_line = meta_line or (
        f"345-name watch universe &nbsp;·&nbsp; Baseline 21 Jul 2026 "
        f"&nbsp;·&nbsp; Last scan {date.today():%d %b %Y}"
    )
    return f"""<!DOCTYPE html><html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex,nofollow">
<title>{esc(title)} · TCM AI Efficiency Database</title>
<style>{CSS}</style></head><body>
<div class="band"><div class="wrap">
  <div class="eyebrow">Thames Capital Management <span>· Equity Research</span></div>
  <h1 class="title">{esc(title)}</h1>
  <div class="sub">{subtitle}</div>
  <div class="meta">{meta_line}</div>
</div></div>
<nav><div class="wrap">{nav}</div></nav>
<div class="wrap">{body}
<footer>Thames Capital Management — internal research tool. Companies are excluded by default;
admission requires quantified, AI-attributable operational-efficiency evidence that survives an
explicit attempt to refute it. Figures are sourced from company filings, earnings calls and
investor materials, and are attributed on each company page. Not investment advice.</footer>
</div></body></html>"""


def score_cls(s):
    if s is None:
        return ""
    return "s-hi" if s >= 65 else ("s-mid" if s >= 45 else "s-lo")


def badge(status, pending=False):
    if pending:
        return '<span class="b b-pending">Pending Deep Review</span>'
    return f'<span class="b b-{status}">{status}</span>'


def slug(c):
    return re.sub(r"[^A-Za-z0-9]+", "-", f"{c['ticker']}-{c['listing']}").strip("-").upper()


def qtrs_since(d):
    """Rough quarter age of an ISO date."""
    if not d:
        return None
    try:
        then = datetime.strptime(d, "%Y-%m-%d").date()
    except ValueError:
        return None
    return max(0, ((date.today() - then).days) // 91)


# ---------------------------------------------------------------- pages
def page_index(st, adm):
    realized = [c for c in adm if c["status"] == "realized"]
    plan = [c for c in adm if c["status"] == "plan"]
    cut = [c for c in st["companies"] if c["status"] == "cut"]
    scores = sorted(c["score"] for c in adm if c["score"] is not None)
    med = scores[len(scores) // 2] if scores else 0
    top = max(adm, key=lambda c: c["score"] or 0)

    strip = "".join(
        f'<div class="card"><div class="lab">{l}</div><div class="val">{v}</div>'
        f'<div class="note">{n}</div></div>'
        for l, v, n in [
            ("Universe",   len(st["companies"]), "names screened"),
            ("Admitted",   len(adm), f"{len(adm)*100//len(st['companies'])}% of universe"),
            ("Realized",   len(realized), "criteria B"),
            ("Plan",       len(plan), "criteria A"),
            ("Rejected",   len(cut), "failed verification"),
            ("Near Misses", len(st.get("near_misses", [])), "deep-reviewed, rejected"),
                    ]
    )

    rows = []
    for c in adm:
        age = qtrs_since(c.get("score_last_moved"))
        stale = ' <span class="b b-cut">Stale</span>' if (age or 0) >= 3 else ""
        rows.append(
            f'<tr data-status="{c["status"]}" data-t="{esc(c["ticker"]+" "+c["company"]+" "+c["sub_industry"]).lower()}">'
            f'<td class="num">{c["rank"]}</td>'
            f'<td class="tick"><a href="company/{slug(c)}.html">{esc(c["ticker"])}</a></td>'
            f'<td>{esc(c["company"])}</td>'
            f'<td class="sm">{esc(c["sub_industry"])}</td>'
            f'<td class="num">{c["mkt_cap_b"] if c["mkt_cap_b"] is not None else "—"}</td>'
            f'<td>{badge(c["status"], c.get("pending_deep_review"))}</td>'
            f'<td class="num"><span class="score {score_cls(c["score"])}">{c["score"]}</span></td>'
            f'<td class="sm">{esc(c.get("score_last_moved") or "—")}{stale}</td></tr>'
        )

    body = f"""
<div class="strip">{strip}</div>

<h2>The Database</h2><div class="rule"></div>
<p class="lede">Companies from the {len(st['companies'])}-name watch universe that have produced
<strong>specific, quantified and credible</strong> evidence of AI-driven operational efficiency.
Two tiers: <strong>Plan</strong> (criteria A) is a highly specific quantified plan that makes
operational sense; <strong>Realized</strong> (criteria B) additionally shows the benefit already
landing in the financial statements, quantified by the company.</p>

<div class="box box-persp"><div class="h">How to read the score</div>
Conviction, 0–100, built from quantification quality (0–40), visibility in the reported
financials (0–25), credibility of the causal mechanism (0–20) and management track record (0–15),
less penalties for promotional tone, AI-revenue conflation and shifting metric definitions.
<strong>A score only moves when new evidence arrives</strong> — the date it last moved is shown,
so age is visible rather than silently decaying the number.</div>

<div class="controls">
  <input type="search" id="q" placeholder="Search ticker, company or sub-industry…">
  <select id="f">
    <option value="">All admitted ({len(adm)})</option>
    <option value="realized">Realized only ({len(realized)})</option>
    <option value="plan">Plan only ({len(plan)})</option>
  </select>
  <span class="count" id="n"></span>
</div>

<table id="tbl"><thead><tr>
  <th class="num sortable" data-c="0" data-n="1">#</th>
  <th class="sortable" data-c="1">Ticker</th>
  <th class="sortable" data-c="2">Company</th>
  <th class="sortable" data-c="3">Sub-industry</th>
  <th class="num sortable" data-c="4" data-n="1">Mkt Cap $B</th>
  <th class="sortable" data-c="5">Status</th>
  <th class="num sortable" data-c="6" data-n="1">Score</th>
  <th class="sortable" data-c="7">Score last moved</th>
</tr></thead><tbody>{''.join(rows)}</tbody></table>
{TABLE_JS}
"""
    return shell("AI Operational Efficiency Database",
                 "Quantified, AI-attributable operational efficiency — verified holdings list",
                 "index.html", body)


TABLE_JS = """
<script>
(function(){
  var q=document.getElementById('q'),f=document.getElementById('f'),
      tb=document.querySelector('#tbl tbody'),n=document.getElementById('n');
  function filt(){
    var s=(q?q.value:'').toLowerCase(), st=(f?f.value:''), c=0;
    Array.prototype.forEach.call(tb.rows,function(r){
      var ok=(!s||r.dataset.t.indexOf(s)>-1)&&(!st||r.dataset.status===st);
      r.style.display=ok?'':'none'; if(ok)c++;
    });
    if(n)n.textContent=c+' shown';
  }
  if(q)q.addEventListener('input',filt); if(f)f.addEventListener('change',filt); filt();
  var dir={};
  Array.prototype.forEach.call(document.querySelectorAll('th.sortable'),function(th){
    th.addEventListener('click',function(){
      var c=+th.dataset.c, num=th.dataset.n==='1', d=dir[c]=-(dir[c]||1);
      var rows=Array.prototype.slice.call(tb.rows);
      rows.sort(function(a,b){
        var x=a.cells[c].innerText.trim(), y=b.cells[c].innerText.trim();
        if(num){x=parseFloat(x.replace(/[^0-9.\\-]/g,''))||0;y=parseFloat(y.replace(/[^0-9.\\-]/g,''))||0;
                return (x-y)*d;}
        return x.localeCompare(y)*d;
      });
      rows.forEach(function(r){tb.appendChild(r);});
    });
  });
})();
</script>
"""



def split_quarters(text):
    """Split a 'Q1 2025: ... Q2 2025: ...' blob into (label, body) pairs."""
    if not text:
        return []
    parts = re.split(r'(?=(?:Q[1-4]|FY|H[12])\s*(?:20)?\d{2}\s*:)', text)
    out = []
    for chunk in [x.strip() for x in parts if x and x.strip()]:
        m = re.match(r'^((?:Q[1-4]|FY|H[12])\s*(?:20)?\d{2})\s*:\s*(.*)$', chunk, re.S)
        if m:
            out.append((m.group(1).strip(), m.group(2).strip()))
        else:
            out.append(("", chunk))
    return out


def split_bullets(text):
    """Split a risks blob into sentences/clauses that read as separate risks."""
    if not text:
        return []
    parts = re.split(r'(?<=[.;])\s+(?=[A-Z(])', text)
    return [x.strip() for x in parts if x and len(x.strip()) > 3]


def page_company(c, st, adm):
    peers = [p for p in adm if p["sub_industry"] == c["sub_industry"] and p["ticker"] != c["ticker"]]
    peer_html = ", ".join(
        f'<a href="{slug(p)}.html">{esc(p["ticker"])}</a>' for p in peers
    ) or '<span class="sm">No other admitted name in this sub-industry.</span>'

    ev = [e for e in st.get("evidence_log", [])
          if c["ticker"] in (e.get("entry") or "")]
    ev_html = "".join(
        f'<tr><td class="sm" style="white-space:nowrap">{esc(e["date"])}</td>'
        f'<td>{esc(e["entry"])}</td></tr>' for e in ev
    ) or ('<tr><td colspan="2" class="empty">No company-specific evidence entries yet. '
          'Baseline evidence was established in the Phase 1 deep verification; entries '
          'accumulate here as the machine verifies each subsequent quarter.</td></tr>')

    age = qtrs_since(c.get("score_last_moved"))
    age_txt = "this quarter" if not age else f"~{age} quarter{'s' if age != 1 else ''} ago"

    rows = c.get('evidence_rows') or []
    if rows:
        trs = []
        for r in rows:
            live = str(r.get('added_by','')).startswith('scan')
            mark = ('<span class="b b-realized" style="margin-left:6px">Qualifies</span>'
                    if r.get('qualifies') else
                    '<span class="b b-outside" style="margin-left:6px">None disclosed</span>')
            src = ''
            if r.get('source_url'):
                src = (f'<br><span class="sm" style="font-size:10.5px">'
                       f'<a href="{esc(r["source_url"])}">{esc(r.get("source") or "source")}</a></span>')
            elif r.get('source'):
                src = f'<br><span class="sm" style="font-size:10.5px">{esc(r["source"])}</span>'
            scan_tag = ('<span class="b b-pending" style="margin-left:6px">Added by scan</span>'
                        if live else '')
            trs.append(
                f'<tr><td class="tick" style="white-space:nowrap">{esc(r["period"])}{scan_tag}</td>'
                f'<td>{esc(r["finding"])}{src}</td>'
                f'<td style="white-space:nowrap">{mark}</td></tr>')
        q = sum(1 for r in rows if r.get('qualifies'))
        quarters_html = (
            '<table><thead><tr><th style="width:130px">Period</th>'
            '<th>Quantified evidence, as disclosed</th>'
            '<th style="width:110px">Verdict</th></tr></thead><tbody>'
            + "".join(trs) + '</tbody></table>'
            + f'<p class="sm" style="font-family:Arial,sans-serif;font-size:11.5px;color:{GRAY}">'
              f'<strong>{q} of {len(rows)}</strong> recorded quarters carry a qualifying, '
              f'AI-attributed efficiency number. Rows marked <em>Added by scan</em> were written '
              f'by the automated machine; the rest are the Phase 1 baseline. This table is '
              f'append-only — every scanned quarter is recorded, including quarters where '
              f'nothing was disclosed.</p>')
    else:
        quarters_html = ('<div class="box box-push"><div class="h">&#9679; Pending</div>'
                         'No quantified evidence on file for this name. It populates on the first '
                         'automated scan following its next report.</div>')

    rs = split_bullets(c.get('risks'))
    risks_html = ('<div class="box box-persp"><div class="h">What would break this thesis</div><ul style="margin:6px 0 0 18px">'
                  + "".join(f'<li style="margin:4px 0">{esc(x)}</li>' for x in rs)
                  + '</ul></div>') if rs else '<p class="empty">No risks recorded.</p>'

    src = c.get('sources_detail')
    sources_html = (f'<p class="sm" style="font-size:12px;line-height:1.6">{esc(src)}</p>'
                    if src else '<p class="empty">Sources are recorded per evidence entry.</p>')

    body = f"""
<div class="strip">
  <div class="card"><div class="lab">Status</div><div class="val" style="font-size:20px">{c['status'].title()}</div><div class="note">{'criteria B' if c['status']=='realized' else 'criteria A'}</div></div>
  <div class="card"><div class="lab">Score</div><div class="val">{c['score']}</div><div class="note">rank {c['rank']} of {len(adm)}</div></div>
  <div class="card"><div class="lab">Mkt Cap</div><div class="val" style="font-size:22px">${c['mkt_cap_b']}B</div><div class="note">{esc(c['listing'])} listing</div></div>
  <div class="card"><div class="lab">Admitted</div><div class="val" style="font-size:18px">{esc(c['admitted'])}</div><div class="note">Phase 1 baseline</div></div>
  <div class="card"><div class="lab">Last Scanned</div><div class="val" style="font-size:18px">{esc(c['last_scanned'])}</div><div class="note">{esc(c.get('last_qtr_verified') or '—')}</div></div>
  <div class="card"><div class="lab">Score Age</div><div class="val" style="font-size:20px">{age or 0}Q</div><div class="note">moved {age_txt}</div></div>
</div>

<h2>Position</h2><div class="rule"></div>
<dl class="kv">
  <dt>Company</dt><dd>{esc(c['company'])} ({esc(c['ticker'])})</dd>
  <dt>Sub-industry</dt><dd>{esc(c['sub_industry'])}</dd>
  <dt>Status</dt><dd>{badge(c['status'], c.get('pending_deep_review'))}</dd>
  <dt>Score last moved</dt><dd>{esc(c.get('score_last_moved') or '—')} — {esc(c.get('score_last_moved_reason') or '—')}</dd>
  <dt>Peers in database</dt><dd>{peer_html}</dd>
</dl>

<h2>Investment Thesis</h2><div class="rule"></div>
{('<p class="lede">' + esc(c['thesis']) + '</p>') if c.get('thesis') else
 '<p>' + esc(c.get('notes') or 'Admitted in the Phase 1 deep verification.') + '</p>'}

<h2>Quantified Evidence</h2><div class="rule"></div>
{quarters_html}

<h2>Key Risks &amp; Red Flags</h2><div class="rule"></div>
{risks_html}

<h2>Sources</h2><div class="rule"></div>
{sources_html}

<h2>Evidence Log</h2><div class="rule"></div>
<table><thead><tr><th>Date</th><th>Entry</th></tr></thead><tbody>{ev_html}</tbody></table>

<h2>Quantitative Panel</h2><div class="rule"></div>
<div class="box box-push"><div class="h">● Pending</div>
Operating-expense ratio, operating margin and revenue-per-head series are pulled from as-reported
quarterly financials so a management claim can be tested against the statements rather than taken
on trust. This panel populates on the first automated scan following this company's next report.</div>

<h2>Kill-Step Checklist</h2><div class="rule"></div>
<p>Before any score moves, the deep scan must rule out each competing explanation for an
efficiency gain. Recorded per quarter:</p>
<table><thead><tr><th>Competing explanation</th><th>Status</th></tr></thead><tbody>
{''.join(f'<tr><td>{e}</td><td class="sm">Assessed at Phase 1 baseline</td></tr>' for e in
  ['Volume leverage / operating leverage from growth',
   'Price or mix, not cost',
   'Lean, Six Sigma or conventional process re-engineering',
   'Offshoring or labour arbitrage',
   'Headcount reduction unrelated to AI',
   'Cycle recovery in the underlying industry',
   'Peer set showing the same delta without an AI story',
   'One-time saving presented as run-rate'])}
</tbody></table>
"""
    return shell(f"{c['company']} ({c['ticker']})",
                 f"{esc(c['sub_industry'])} — {c['status']} · score {c['score']}",
                 "index.html", body, depth=1)


def page_rejections(st):
    cut = [c for c in st["companies"] if c["status"] == "cut"]
    rows = "".join(
        f'<tr data-t="{esc(c["ticker"]+" "+c["company"]+" "+c["sub_industry"]).lower()}">'
        f'<td class="tick">{esc(c["ticker"])}</td><td>{esc(c["company"])}</td>'
        f'<td class="sm">{esc(c["sub_industry"])}</td>'
        f'<td class="sm">{esc(c.get("cut_date") or c.get("last_scanned") or "—")}</td>'
        f'<td>{esc(c.get("cut_reason") or "—")}</td></tr>' for c in cut
    )
    body = f"""
<h2>Rejections</h2><div class="rule"></div>
<p class="lede">Names that were reviewed in depth and <strong>removed</strong>. These are as much
the product as the admissions: nearly every company in the universe now discusses AI, and the
value of this database is what it refuses to include.</p>

<div class="box box-signal"><div class="h">▲ Why this page exists</div>
A database that only shows what it admitted cannot be audited. Every rejection carries its reason,
and a rejected name is not re-litigated without <em>new</em> evidence that specifically overcomes
that reason.</div>

<div class="controls"><input type="search" id="q" placeholder="Search rejections…">
<span class="count" id="n"></span></div>
<table id="tbl"><thead><tr><th class="sortable" data-c="0">Ticker</th>
<th class="sortable" data-c="1">Company</th><th class="sortable" data-c="2">Sub-industry</th>
<th class="sortable" data-c="3">Cut date</th><th>Reason</th></tr></thead>
<tbody>{rows}</tbody></table>{TABLE_JS}"""
    return shell("Rejections", f"{len(cut)} names reviewed and removed", "rejections.html", body)


def page_universe(st):
    order = {"realized": 0, "plan": 1, "cut": 2, "outside": 3}
    comps = sorted(st["companies"], key=lambda c: (order[c["status"]], -(c["score"] or 0), c["ticker"]))
    rows = "".join(
        f'<tr data-status="{c["status"]}" data-t="{esc(c["ticker"]+" "+c["company"]+" "+c["sub_industry"]).lower()}">'
        f'<td class="tick">'
        + (f'<a href="company/{slug(c)}.html">{esc(c["ticker"])}</a>' if c["rank"] else esc(c["ticker"]))
        + f'</td><td>{esc(c["company"])}</td><td class="sm">{esc(c["sub_industry"])}</td>'
        f'<td class="num">{c["mkt_cap_b"] if c["mkt_cap_b"] is not None else "—"}</td>'
        f'<td>{badge(c["status"], c.get("pending_deep_review"))}</td>'
        f'<td class="num">{c["score"] if c["score"] is not None else "—"}</td>'
        f'<td class="sm">{esc(c.get("last_scanned") or "—")}</td></tr>' for c in comps
    )
    counts = {k: sum(1 for c in st["companies"] if c["status"] == k)
              for k in ["realized", "plan", "cut", "outside"]}
    body = f"""
<h2>Watch Universe</h2><div class="rule"></div>
<p class="lede">All {len(comps)} names under surveillance. Every name is re-examined when it
reports earnings; a name outside the database is <em>checked off until its next report</em>
rather than dropped.</p>
<div class="controls">
  <input type="search" id="q" placeholder="Search all {len(comps)} names…">
  <select id="f"><option value="">All statuses</option>
    <option value="realized">Realized ({counts['realized']})</option>
    <option value="plan">Plan ({counts['plan']})</option>
    <option value="cut">Cut ({counts['cut']})</option>
    <option value="outside">Outside ({counts['outside']})</option></select>
  <span class="count" id="n"></span></div>
<table id="tbl"><thead><tr><th class="sortable" data-c="0">Ticker</th>
<th class="sortable" data-c="1">Company</th><th class="sortable" data-c="2">Sub-industry</th>
<th class="num sortable" data-c="3" data-n="1">Mkt Cap $B</th>
<th class="sortable" data-c="4">Status</th>
<th class="num sortable" data-c="5" data-n="1">Score</th>
<th class="sortable" data-c="6">Last scanned</th></tr></thead>
<tbody>{rows}</tbody></table>{TABLE_JS}"""
    return shell("Watch Universe", f"{len(comps)} names under continuous surveillance",
                 "universe.html", body)


def page_evidence(st):
    rows = "".join(
        f'<tr><td class="sm" style="white-space:nowrap">{esc(e["date"])}</td>'
        f'<td>{esc(e["entry"])}</td></tr>' for e in st.get("evidence_log", [])
    )
    body = f"""
<h2>Evidence Log</h2><div class="rule"></div>
<p class="lede">Append-only. Every admission, promotion, demotion, cut and score move is recorded
here with the quantified evidence and its source. History is never rewritten — corrections are
added as new dated entries.</p>
<table><thead><tr><th>Date</th><th>Entry</th></tr></thead><tbody>{rows}</tbody></table>"""
    return shell("Evidence Log", "Append-only record of every state change", "evidence.html", body)


def page_runlog(st):
    rows = "".join(
        f'<tr><td class="sm" style="white-space:nowrap">{esc(e["date"])}</td>'
        f'<td>{esc(e["entry"])}</td></tr>' for e in st.get("run_log", [])
    )
    body = f"""
<h2>Run Log</h2><div class="rule"></div>
<p class="lede">One line per scan. Quiet days are recorded as quiet — the machine does not
manufacture activity to look busy.</p>
<div class="box box-persp"><div class="h">Scan procedure</div>
<strong>Tier 0</strong> — the earnings calendar identifies which of the 345 have reported since
their last scan. <strong>Tier 1</strong> — a thin screen reads each reporter's call for the
co-occurrence of a named AI system, a hard number and an efficiency concept; failures are checked
off until the next quarter. <strong>Tier 2</strong> — only for names that pass, a deep scan reads
the full transcript, the release, the reported financials, prior-quarter calls and the peer set,
then attempts to <em>refute</em> its own finding. <strong>Tier 3</strong> — surviving findings are
written to the ledger and this site is rebuilt.</div>
<table><thead><tr><th>Date</th><th>Entry</th></tr></thead><tbody>{rows}</tbody></table>"""
    return shell("Run Log", "Scan history", "runlog.html", body)


def page_nearmiss(st):
    nms = st.get("near_misses", [])
    if not nms:
        blocks = '<p class="empty">No near-misses recorded yet.</p>'
    else:
        parts = []
        for nm in nms:
            quotes = "".join(
                f'<blockquote>“{esc(q["q"])}”<span class="attr">{esc(q["who"])}</span></blockquote>'
                for q in nm.get("quotes", [])
            )
            peer = (f'<div class="box box-push"><div class="h">● Peer check</div>{esc(nm["peer"])}</div>'
                    if nm.get("peer") else "")
            parts.append(f"""
<h3 style="font-size:16px;margin-top:30px">{esc(nm['ticker'])} — {esc(nm['company'])}
  <span class="b b-pending" style="margin-left:8px">Near Miss · scored {nm['score']}</span></h3>
<p class="sm" style="font-family:Arial,sans-serif;font-size:11.5px;color:{GRAY}">
  {esc(nm['sub_industry'])} &nbsp;·&nbsp; call {esc(nm['call_date'])} &nbsp;·&nbsp;
  <a href="{esc(nm['url'])}">source transcript</a></p>
<p><strong>{esc(nm['headline'])}</strong></p>
{quotes}
<div class="box box-signal"><div class="h">▲ What survived</div>{esc(nm['survives'])}</div>
<div class="box box-persp"><div class="h">The kill</div>{esc(nm['kill'])}</div>
{peer}
<p><strong>Materiality.</strong> {esc(nm['materiality'])}</p>
<p><strong>Watch item.</strong> {esc(nm['watch'])}</p>
<div class="rule" style="margin-top:26px"></div>""")
        blocks = "".join(parts)

    body = f"""
<h2>Near Misses</h2><div class="rule"></div>
<p class="lede">Companies that passed the thin screen, earned a full deep review, and were
<strong>rejected</strong>. Each was scored against the same rubric as an admitted name and fell
short. They are the closest thing the universe currently has to a future admission, and they are
re-tested when they next report.</p>

<div class="box box-persp"><div class="h">Why these are worth reading</div>
Every name here had a real, quoted, AI-attributed number — which is already rarer than it sounds.
They failed on what happened next: the number measured activity rather than cost, the reported
financials moved the other way, a peer achieved the same result with no AI story, or management's
own explanation of its margin never mentioned the tool. This page is where the standard is
actually visible.</div>
{blocks}"""
    return shell("Near Misses", f"{len(nms)} candidates deep-reviewed and rejected",
                 "nearmisses.html", body)


def page_method(st):
    body = """
<h2>Admission Criteria</h2><div class="rule"></div>
<p class="lede">Companies are <strong>out by default</strong>. Admission is an event, and it is
rare. Strictness is the product: a small database of verified names is worth more than a large
database of claims.</p>

<h3>A — Plan</h3>
<p>A highly specific, quantified and credible plan for driving AI efficiency into the business.
<em>Credible</em> means it makes operational sense — not a promotional management team telling
investors what they want to hear. <em>Specific and quantified</em> means named systems, named
workflows, numeric targets and timelines. "We are leaning into AI" is nothing.</p>

<h3>B — Realized</h3>
<p>Satisfies A, <strong>and</strong> the benefit is already visible in the financial statements
with the company quantifying it — the CHRW standard: shipments per person per day, quantified
opex reduction attributed to named AI tooling.</p>

<h2>What Counts as Evidence</h2><div class="rule"></div>
<p>A data point qualifies only if all four hold:</p>
<table><thead><tr><th>Test</th><th>Requirement</th></tr></thead><tbody>
<tr><td><strong>It is a number</strong></td><td>A percentage, dollar amount, ratio, headcount, throughput or unit-cost figure. Adjectives are not evidence.</td></tr>
<tr><td><strong>It measures efficiency</strong></td><td>Cost, productivity per head, cycle time, unit economics, cost-driven margin — not revenue growth, and not revenue from selling AI products.</td></tr>
<tr><td><strong>It is attributable to AI</strong></td><td>Either explicit company attribution, or a clean before/after around a named deployment with no better competing explanation.</td></tr>
<tr><td><strong>It survives the noise checks</strong></td><td>See the kill list below.</td></tr>
</tbody></table>

<h2>The Kill List</h2><div class="rule"></div>
<div class="box box-push"><div class="h">● The central problem</div>
Nearly every company now talks about AI. Most efficiency gains attributed to AI are not caused by
AI. The deep scan therefore runs two independent passes: one builds the case, a second tries to
destroy it. A finding is admitted only if it survives the attempt to refute it.</div>
<table><thead><tr><th>Failure mode</th><th>What it looks like</th></tr></thead><tbody>
<tr><td><strong>AI-washing</strong></td><td>Gains actually driven by Lean, procurement, routing software, offshoring, layoffs or cycle recovery, relabelled as AI.</td></tr>
<tr><td><strong>Promotional non-numbers</strong></td><td>"AI is transforming how we work." "Significant productivity gains." No figure, no evidence.</td></tr>
<tr><td><strong>Immateriality</strong></td><td>A real number too small to matter — under roughly 0.5% of opex or operating income with no credible path to scale.</td></tr>
<tr><td><strong>Unverifiable</strong></td><td>A number that appears once, is never reconciled to segment or financial data, and that management dodges on follow-up.</td></tr>
<tr><td><strong>One-time vs run-rate</strong></td><td>A one-off saving presented as a recurring benefit. Always labelled.</td></tr>
<tr><td><strong>Competing explanation</strong></td><td>Volume, price, mix, fuel or unrelated headcount cuts explain the delta. The peer set is checked: if the whole sub-industry posted the same move without an AI story, AI gets no credit.</td></tr>
<tr><td><strong>AI as revenue</strong></td><td>Selling AI products is a different thesis. Logged, never scored.</td></tr>
</tbody></table>

<h2>Scoring</h2><div class="rule"></div>
<p>Conviction 0–100, starting at zero and awarded stingily.</p>
<table><thead><tr><th>Component</th><th class="num">Max</th><th>Basis</th></tr></thead><tbody>
<tr><td>Quantification quality</td><td class="num">40</td><td>How hard, specific and repeated the numbers are. Verbatim AI-attributed financial figures reconciled to the statements score high; one soft number scores low.</td></tr>
<tr><td>Financial-statement visibility</td><td class="num">25</td><td>Whether the effect is visible in reported margin, opex and headcount trends independent of management's narrative.</td></tr>
<tr><td>Credibility of mechanism</td><td class="num">20</td><td>Whether the causal story makes operational sense for this business model. Named systems, plausible arithmetic.</td></tr>
<tr><td>Track record</td><td class="num">15</td><td>Whether management has hit prior quantified targets, and whether the same metric has held its definition across quarters.</td></tr>
<tr><td>Penalties</td><td class="num">—</td><td>Promotional tone with thin numbers (−10 to −20); AI-revenue conflation (−10); metric definitions that shift quarter to quarter (−15).</td></tr>
</tbody></table>
<div class="box box-persp"><div class="h">Score stability</div>
A score <strong>does not move without new evidence</strong>. There is no periodic re-scoring pass,
because a number that drifts run to run cannot be used to track progress. Instead, the date a
score last moved is displayed alongside it, and names whose evidence has gone three or more
quarters without refresh are flagged stale rather than silently marked down.</div>

<h2>Calibration Anchors</h2><div class="rule"></div>
<table><thead><tr><th>Name</th><th class="num">Score</th><th>Role</th></tr></thead><tbody>
<tr><td><strong>CHRW</strong></td><td class="num">87</td><td>Best-in-class realized. Quantified AI productivity in shipments per person per day and in opex.</td></tr>
<tr><td>Median admitted</td><td class="num">53</td><td>The centre of the admitted distribution.</td></tr>
<tr><td><strong>USFD</strong></td><td class="num">38</td><td>Anchor retained by instruction despite failed attribution: the efficiency is real but Lean-, routing- and procurement-driven, and its AI-labelled products are revenue tools. The floor of what admission can mean.</td></tr>
</tbody></table>
<div class="box box-signal"><div class="h">▲ Why anchors matter</div>
Every scan re-scores these three. If the anchors move, the run is treated as miscalibrated and is
not written to the ledger. This is what keeps a score assigned in July comparable to one assigned
in December.</div>

<h2>Discipline Rules</h2><div class="rule"></div>
<table><tbody>
<tr><td>The ledger is the only state. The site and any exported workbook are renderings of it.</td></tr>
<tr><td>The evidence log is append-only. History is never rewritten; corrections are new dated entries.</td></tr>
<tr><td>Every quantified claim carries its source — call date and document.</td></tr>
<tr><td>When evidence is borderline, the answer is no admission. Borderline names are recorded as near-misses and revisited next quarter.</td></tr>
<tr><td>A cut name is not re-litigated without new evidence that specifically overcomes the recorded cut reason.</td></tr>
<tr><td>If a transcript is not yet available for a company that has reported, its scan date is left unchanged so the next run retries it automatically.</td></tr>
</tbody></table>"""
    return shell("Methodology", "Admission criteria, kill list, scoring and discipline rules",
                 "methodology.html", body)


# ---------------------------------------------------------------- main
def main():
    st = json.loads(DATA.read_text())
    adm = sorted([c for c in st["companies"] if c["rank"]], key=lambda c: c["rank"])

    if OUT.exists():
        shutil.rmtree(OUT)
    (OUT / "company").mkdir(parents=True)
    (OUT / ".nojekyll").write_text("")

    (OUT / "index.html").write_text(page_index(st, adm))
    (OUT / "rejections.html").write_text(page_rejections(st))
    (OUT / "nearmisses.html").write_text(page_nearmiss(st))
    (OUT / "universe.html").write_text(page_universe(st))
    (OUT / "evidence.html").write_text(page_evidence(st))
    (OUT / "runlog.html").write_text(page_runlog(st))
    (OUT / "methodology.html").write_text(page_method(st))
    for c in adm:
        (OUT / "company" / f"{slug(c)}.html").write_text(page_company(c, st, adm))

    shutil.copy(DATA, OUT / "state.json")
    n = len(list(OUT.rglob("*.html")))
    print(f"built {n} pages -> {OUT}")


if __name__ == "__main__":
    main()
