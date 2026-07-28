# TCM AI Efficiency Machine — Daily Run Procedure

This file is the operating procedure. A scheduled session executes it start to finish with no
human in the loop. **The ledger is the only state.** The website and any exported workbook are
renderings of it. Never treat a rendered artefact as state.

---

## 0. Setup (every run)

```bash
git clone https://x-access-token:$GH_TOKEN@github.com/danielrianhard/tcm-ai-efficiency.git site
cd site && python3 -c "import json;print(json.load(open('data/state.json'))['meta'])"
```

`data/state.json` holds all 345 names with `status`, `score`, `last_scanned`, `score_last_moved`.
`data/ledger.md` is the human-readable master. `build.py` renders `docs/`.

**Network constraint that shapes everything:** this environment cannot reach finnhub.io,
sec.gov or transcript sites from a shell — `curl` is blocked at the proxy. All data acquisition
must go through the WebFetch / WebSearch tools. GitHub *is* reachable from the shell, so
`git push` works normally. The machine is therefore an agent, not a scraper.

---

## 1. Tier 0 — who reported?

For each date since `meta.last_run`, one WebFetch per day:

```
https://finnhub.io/api/v1/calendar/earnings?from=YYYY-MM-DD&to=YYYY-MM-DD&token=$FINNHUB_KEY
```

Prompt it: *"List EVERY ticker symbol in this JSON, comma-separated, in order. No summary, no
omissions, no commentary. End with a final line giving the total count."* Fetch **one day per
call** — a multi-day range returns 1000+ entries and gets truncated.

Intersect the returned symbols with the US-listed names in `state.json` (Canadian listings do not
appear on this calendar and are handled on their own reporting dates). Add every name in
`meta.pending_requeue` — those are prior reporters whose transcript had not published yet.

If the intersection is empty: append one line to the run log, push, stop. No memo, no
notification. **Quiet days are recorded as quiet.**

## 2. Priority order when the queue is oversubscribed

1. Admitted names (`realized`, then `plan`) that reported — the database itself
2. Names carrying `pending_deep_review` — a flagged candidate is the most valuable unfinished work
3. Everything else that reported
4. `cut` names — a quick check only

A name is stamped `last_scanned` **only when it has actually been scanned**. Anything unfinished
is therefore retried automatically on the next run. Never stamp a name whose transcript you could
not read.

## 3. Tier 1 — thin screen (every reporter)

Batch roughly 10 companies per subagent. Per company:

1. `WebSearch: TICKER Q<n> <year> earnings call transcript`
2. WebFetch the transcript. **investing.com** carries full transcripts including analyst Q&A and
   is reliably fetchable; **marketbeat.com**, **benzinga.com**, **fool.com** are backups.
   **Never seekingalpha.com** — paywalled.
3. Ask: *"Quote verbatim every sentence where artificial intelligence, AI, machine learning,
   automation, or a named AI system is mentioned together with a specific number relating to cost,
   expense ratio, productivity, headcount, processing or cycle time, straight-through processing,
   or margin. If there are none, reply exactly NONE."*
4. Verdict: **PASS** (a named AI system or explicit attribution + a hard number + an
   operational-efficiency meaning) / **FAIL** / **NO_TRANSCRIPT**.

FAIL is the expected answer. Capture the best AI mention even on a FAIL so the rejection is
auditable. NO_TRANSCRIPT goes back in the requeue — do not advance `last_scanned`.

## 4. Tier 2 — deep scan (only on a PASS)

One subagent per candidate. Two halves, and the second half is the product.

**Build the case.** Re-fetch and verify every quote verbatim, with speaker and context — misquotes
are common in the thin screen. Establish what the number actually measures and what its
denominator is. Pull the reported financials:

```
https://finnhub.io/api/v1/stock/financials-reported?symbol=TICKER&freq=quarterly&token=$FINNHUB_KEY
```

Compute opex/revenue by quarter. Note that filings are often year-to-date — de-cumulate them.
Then read the **prior** call: was there a quantified target, is the metric defined the same way,
did they hit it? Goalpost-shifting is the most common tell.

**Kill it.** An independent adversarial pass whose only job is to destroy the finding. Work
through every competing explanation and state whether the finding survives each:

- volume / operating leverage from growth
- price or mix rather than cost
- Lean, Six Sigma or conventional process re-engineering
- offshoring or labour arbitrage (watch for "shared services with an external provider")
- headcount reduction unrelated to AI
- cycle recovery in the underlying industry
- **the peer set** — did sub-industry peers post the same delta with no AI story? This is the
  single most decisive test and it must be run every time
- one-time saving presented as run-rate
- AI-as-revenue: selling AI products is a different thesis. Log it, never score it
- immateriality: under ~0.5% of opex with no credible scaling path

Three checks that have proved especially load-bearing in practice: **does management's own margin
bridge mention the tool?** (if they explain their margin without it, we do not add it);
**did unit cost actually fall?** (revenue per unit rising while volumes are flat compresses expense
ratios with zero productivity gain); and **did the CEO qualify his own number?**

## 5. Score

Only if new evidence arrived. Quantification quality 0–40, financial-statement visibility 0–25,
credibility of mechanism 0–20, track record 0–15. Penalties: promotional tone with thin numbers
−10 to −20, AI-revenue conflation −10, shifting metric definitions −15.

Anchors, which every run must respect: **CHRW 87** (best-in-class realized), **median admitted 53**,
**USFD 38** (efficiency real but Lean/routing/procurement-driven — the floor of what admission can
mean). A candidate scoring below the USFD floor is not admissible.

**A score never moves without new evidence.** There is no periodic re-scoring pass. Record
`score_last_moved` and the reason. Evidence age is displayed rather than decayed.

Borderline is a **rejection**, recorded as a near-miss with its kill reasoning and a watch item.
The near-miss page is where the standard is visible, so write those entries properly.

## 6. Write state, render, deliver

1. Update `data/state.json`: statuses, scores, `last_scanned`, `last_verdict`, near-misses,
   `meta.last_run`, `meta.pending_requeue`.
2. Append to `evidence_log` (append-only — corrections are new dated entries, never rewrites) and
   one line to `run_log`.
3. Mirror material changes into `data/ledger.md`, and write the same summary back to the
   claude.ai project doc `claude/AI_Efficiency_Ledger.md` so it survives across sessions.
4. `python3 build.py` then commit and push. Pages redeploys automatically.
5. **Change memo** only when something changed: additions first and loudest — ticker, criteria met,
   the qualifying numbers quoted verbatim, score. Then promotions, demotions, material score moves,
   then near-misses. One page unless additions demand more.

## 7. Discipline

- Never fabricate a quote or a number. If it cannot be verified verbatim from a source actually
  fetched, it does not exist.
- Quotes ≤25 words, attributed, with the source URL and call date.
- A `cut` name is not re-litigated without NEW evidence that specifically overcomes the recorded
  cut reason.
- When in doubt, the answer is no admission. The database's credibility is the product.
