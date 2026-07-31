# AI Efficiency Machine — Master State Ledger

**THIS FILE IS THE SINGLE SOURCE OF TRUTH.** Every scan run reads this ledger first and writes its results back here. The Excel database and change memos are renderings of this file — never edit those and expect it to stick; edit here.

- **Universe:** 345 companies (boss-provided Bloomberg screen, "AI adoption .pdf")
- **Baseline:** Phase 1 deep verification completed 2026-07-21
- **Methodology:** see `claude/AI_Efficiency_Methodology.md` (admission criteria, strictness filter, scoring rubric, run procedure)
- **Last run:** 2026-07-31 (Tier 0 degraded a fourth consecutive run — finnhub blocked; calendar rebuilt from digrin, which added only CBOE, so the run was effectively the carried 47-name requeue. Calibration PASSED exactly 87/53/38. 48 queued, 26 scanned to full transcript, 6 Tier 1 PASSes, 5 independent adversarial passes, 0 additions)
- **Standing:** 21 realized · 25 plan · 23 cut · 276 outside · 9 near-misses · 0 additions since baseline
- **Pending requeue (next run):** BG, BGC, CBOE, CHRW, CI, CR, FLS, GATX, GH, ITW, L, LECO, LNC, MMSI, PRU, RCL, RYAN, SAIA, SPXC, TTEK, VIRT, WERN (22) — CHRW is still first: `pending_deep_review` is retained and the demotion review stays open because the Q2-2026 transcript has now been unobtainable for three consecutive runs. Only three of the 22 are genuine timing (L reports 3 Aug, PRU 5 Aug, CBOE 31 Jul); the rest are sourcing failures — MarketScreener paywalled, Seeking Alpha barred by rule, stale Fool URLs, and WebFetch's provenance gate blocking any URL not surfaced by a search result. Next run must try investor.chrobinson.com directly before spending budget on aggregators.

## Status codes

| Code | Meaning |
|---|---|
| `realized` | Criteria B: credible quantified plan AND AI benefit already quantified in the financials |
| `plan` | Criteria A: highly specific, quantified, credible plan; not yet visible in the numbers |
| `cut` | Was admitted or deep-reviewed, then removed (AI-washing / unverifiable / immaterial / AI-is-a-revenue-product). Re-admission requires NEW evidence that overcomes the cut reason |
| `outside` | In the watch universe; scanned but has never produced qualifying evidence |

## ADMITTED — the database (46 names)

Ticker key: `TICKER·CN` = Canadian listing; all others US.

| # | Ticker | Company | Sub-industry | Mkt Cap $B | Status | Score | Admitted | Last scanned | Last qtr verified | Notes / evidence pointer |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **CHRW** | CH ROBINSON | Air Freight & Logistics | 23.2 | realized | 87 | 2026-07-21 | 2026-07-21 | Q1-2026 era (Phase 1) | Phase 1 top score. Realized anchor: quantified AI productivity in shipments/person/day and opex. |
| 2 | **XPO** | XPO INC | Cargo Ground Transportation | 24.6 | realized | 71 | 2026-07-21 | 2026-07-21 | Q1-2026 era (Phase 1) | Phase 1 evidence: see TCM_AI_Efficiency_Database_FINAL (tear-sheets) |
| 3 | **FDS** | FACTSET RESEARCH | Financial Exchanges & Data | 9.4 | realized | 70 | 2026-07-21 | 2026-07-21 | Q1-2026 era (Phase 1) | Phase 1 evidence: see TCM_AI_Efficiency_Database_FINAL (tear-sheets) |
| 4 | **HNGE** | HINGE HEALTH-A | Health Care Services | 7.0 | realized | 70 | 2026-07-21 | 2026-07-21 | Q1-2026 era (Phase 1) | Phase 1 evidence: see TCM_AI_Efficiency_Database_FINAL (tear-sheets) |
| 5 | **HOOD** | ROBINHOOD MARK-A | Investment Banking & Brokerage | 99.0 | realized | 70 | 2026-07-21 | 2026-07-21 | Q1-2026 era (Phase 1) | Phase 1 evidence: see TCM_AI_Efficiency_Database_FINAL (tear-sheets) |
| 6 | **UPST** | UPSTART HOLDINGS | Consumer Finance | 3.0 | realized | 66 | 2026-07-21 | 2026-07-21 | Q1-2026 era (Phase 1) | Phase 1 evidence: see TCM_AI_Efficiency_Database_FINAL (tear-sheets) |
| 7 | **LMND** | LEMONADE INC | Property & Casualty Insurance | 5.4 | realized | 66 | 2026-07-21 | 2026-07-21 | Q1-2026 era (Phase 1) | Phase 1 evidence: see TCM_AI_Efficiency_Database_FINAL (tear-sheets) |
| 8 | **XMTR** | XOMETRY INC-A | Trading Companies & Distributors | 5.3 | realized | 66 | 2026-07-21 | 2026-07-21 | Q1-2026 era (Phase 1) | Phase 1 evidence: see TCM_AI_Efficiency_Database_FINAL (tear-sheets) |
| 9 | **RKT** | ROCKET COS INC-A | Commercial & Residential Mortgage Finance | 39.4 | realized | 64 | 2026-07-21 | 2026-07-21 | Q1-2026 era (Phase 1) | Phase 1 evidence: see TCM_AI_Efficiency_Database_FINAL (tear-sheets) |
| 10 | **TRV** | TRAVELERS COS IN | Property & Casualty Insurance | 72.6 | realized | 64 | 2026-07-21 | 2026-07-21 | Q1-2026 era (Phase 1) | Phase 1 evidence: see TCM_AI_Efficiency_Database_FINAL (tear-sheets) |
| 11 | **PFSI** | PENNYMAC FINANCI | Commercial & Residential Mortgage Finance | 4.2 | realized | 63 | 2026-07-21 | 2026-07-21 | Q1-2026 era (Phase 1) | Phase 1 evidence: see TCM_AI_Efficiency_Database_FINAL (tear-sheets) |
| 12 | **ARCB** | ARCBEST CORP | Cargo Ground Transportation | 3.3 | realized | 60 | 2026-07-21 | 2026-07-21 | Q1-2026 era (Phase 1) | Phase 1 evidence: see TCM_AI_Efficiency_Database_FINAL (tear-sheets) |
| 13 | **SPGI** | S&P GLOBAL INC | Financial Exchanges & Data | 129.1 | realized | 60 | 2026-07-21 | 2026-07-21 | Q1-2026 era (Phase 1) | Phase 1 evidence: see TCM_AI_Efficiency_Database_FINAL (tear-sheets) |
| 14 | **NAVN** | NAVAN INC-CL A | Hotels, Resorts & Cruise Lines | 6.6 | realized | 60 | 2026-07-21 | 2026-07-21 | Q1-2026 era (Phase 1) | Phase 1 evidence: see TCM_AI_Efficiency_Database_FINAL (tear-sheets) |
| 15 | **TOST** | TOAST INC-A | Transaction & Payment Processing Services | 17.4 | realized | 60 | 2026-07-21 | 2026-07-21 | Q1-2026 era (Phase 1) | Phase 1 evidence: see TCM_AI_Efficiency_Database_FINAL (tear-sheets) |
| 16 | **GLBE** | GLOBAL-E ONLINE | Broadline Retail | 6.5 | realized | 58 | 2026-07-21 | 2026-07-21 | Q1-2026 era (Phase 1) | Phase 1 evidence: see TCM_AI_Efficiency_Database_FINAL (tear-sheets) |
| 17 | **INGM** | INGRAM MICRO HOL | Technology Distributors | 6.7 | realized | 57 | 2026-07-21 | 2026-07-21 | Q1-2026 era (Phase 1) | Phase 1 evidence: see TCM_AI_Efficiency_Database_FINAL (tear-sheets) |
| 18 | **WMT** | WALMART INC | Consumer Staples Merchandise Retail | 913.4 | realized | 56 | 2026-07-21 | 2026-07-21 | Q1-2026 era (Phase 1) | Phase 1 evidence: see TCM_AI_Efficiency_Database_FINAL (tear-sheets) |
| 19 | **DAVE** | DAVE INC | Consumer Finance | 5.0 | realized | 53 | 2026-07-21 | 2026-07-21 | Q1-2026 era (Phase 1) | Phase 1 evidence: see TCM_AI_Efficiency_Database_FINAL (tear-sheets) |
| 20 | **HQY** | HEALTHEQUITY INC | Managed Health Care | 8.0 | realized | 53 | 2026-07-21 | 2026-07-21 | Q1-2026 era (Phase 1) | Phase 1 evidence: see TCM_AI_Efficiency_Database_FINAL (tear-sheets) |
| 21 | **OSCR** | OSCAR HEALTH -A | Life & Health Insurance | 9.5 | realized | 47 | 2026-07-21 | 2026-07-21 | Q1-2026 era (Phase 1) | Phase 1 evidence: see TCM_AI_Efficiency_Database_FINAL (tear-sheets) |
| 22 | **IFC·CN** | INTACT FINANCIAL | Property & Casualty Insurance | 52.3 | plan | 64 | 2026-07-21 | 2026-07-21 | Q1-2026 era (Phase 1) | Phase 1 evidence: see TCM_AI_Efficiency_Database_FINAL (tear-sheets) |
| 23 | **RYAN** | RYAN SPECIALTY H | Insurance Brokers | 11.0 | plan | 57 | 2026-07-21 | 2026-07-21 | Q1-2026 era (Phase 1) | Re-run after a data glitch in Phase 1; admitted as Plan. |
| 24 | **C** | CITIGROUP INC | Diversified Banks | 240.0 | plan | 56 | 2026-07-21 | 2026-07-21 | Q1-2026 era (Phase 1) | Phase 1 evidence: see TCM_AI_Efficiency_Database_FINAL (tear-sheets) |
| 25 | **WTW** | WILLIS TOWERS WA | Insurance Brokers | 27.9 | plan | 54 | 2026-07-21 | 2026-07-21 | Q1-2026 era (Phase 1) | Phase 1 evidence: see TCM_AI_Efficiency_Database_FINAL (tear-sheets) |
| 26 | **ADT** | ADT INC | Specialized Consumer Services | 5.4 | plan | 54 | 2026-07-21 | 2026-07-21 | Q1-2026 era (Phase 1) | Phase 1 evidence: see TCM_AI_Efficiency_Database_FINAL (tear-sheets) |
| 27 | **AIG** | AMERICAN INTERNA | Property & Casualty Insurance | 42.4 | plan | 53 | 2026-07-21 | 2026-07-21 | Q1-2026 era (Phase 1) | Phase 1 evidence: see TCM_AI_Efficiency_Database_FINAL (tear-sheets) |
| 28 | **BAC** | BANK OF AMERICA | Diversified Banks | 422.2 | plan | 52 | 2026-07-21 | 2026-07-21 | Q1-2026 era (Phase 1) | Phase 1 evidence: see TCM_AI_Efficiency_Database_FINAL (tear-sheets) |
| 29 | **MFC·CN** | MANULIFE FIN | Life & Health Insurance | 97.4 | plan | 52 | 2026-07-21 | 2026-07-21 | Q1-2026 era (Phase 1) | Phase 1 evidence: see TCM_AI_Efficiency_Database_FINAL (tear-sheets) |
| 30 | **CB** | CHUBB LTD | Property & Casualty Insurance | 137.6 | plan | 52 | 2026-07-21 | 2026-07-21 | Q1-2026 era (Phase 1) | Phase 1 evidence: see TCM_AI_Efficiency_Database_FINAL (tear-sheets) |
| 31 | **NU** | NU HOLDINGS LT-A | Diversified Banks | 66.0 | plan | 50 | 2026-07-21 | 2026-07-21 | Q1-2026 era (Phase 1) | Phase 1 evidence: see TCM_AI_Efficiency_Database_FINAL (tear-sheets) |
| 32 | **AON** | AON PLC-CLASS A | Insurance Brokers | 78.5 | plan | 50 | 2026-07-21 | 2026-07-21 | Q1-2026 era (Phase 1) | Phase 1 evidence: see TCM_AI_Efficiency_Database_FINAL (tear-sheets) |
| 33 | **CM·CN** | CAN IMPL BK COMM | Diversified Banks | 151.5 | plan | 48 | 2026-07-21 | 2026-07-21 | Q1-2026 era (Phase 1) | Phase 1 evidence: see TCM_AI_Efficiency_Database_FINAL (tear-sheets) |
| 34 | **RSG** | REPUBLIC SVCS | Environmental & Facilities Services | 68.7 | plan | 48 | 2026-07-21 | 2026-07-21 | Q1-2026 era (Phase 1) | Phase 1 evidence: see TCM_AI_Efficiency_Database_FINAL (tear-sheets) |
| 35 | **RDNT** | RADNET INC | Health Care Services | 5.0 | plan | 48 | 2026-07-21 | 2026-07-21 | Q1-2026 era (Phase 1) | Phase 1 evidence: see TCM_AI_Efficiency_Database_FINAL (tear-sheets) |
| 36 | **OPCH** | OPTION CARE HEAL | Health Care Services | 3.4 | plan | 47 | 2026-07-21 | 2026-07-21 | Q1-2026 era (Phase 1) | Phase 1 evidence: see TCM_AI_Efficiency_Database_FINAL (tear-sheets) |
| 37 | **UWMC** | UWM HOLDINGS COR | Commercial & Residential Mortgage Finance | 3.2 | plan | 46 | 2026-07-21 | 2026-07-21 | Q1-2026 era (Phase 1) | Phase 1 evidence: see TCM_AI_Efficiency_Database_FINAL (tear-sheets) |
| 38 | **TD·CN** | TORONTO-DOM BANK | Diversified Banks | 282.1 | plan | 46 | 2026-07-21 | 2026-07-21 | Q1-2026 era (Phase 1) | Phase 1 evidence: see TCM_AI_Efficiency_Database_FINAL (tear-sheets) |
| 39 | **RY·CN** | ROYAL BANK OF CA | Diversified Banks | 413.9 | plan | 45 | 2026-07-21 | 2026-07-21 | Q1-2026 era (Phase 1) | Phase 1 evidence: see TCM_AI_Efficiency_Database_FINAL (tear-sheets) |
| 40 | **NDAQ** | NASDAQ INC | Financial Exchanges & Data | 50.5 | plan | 44 | 2026-07-21 | 2026-07-21 | Q1-2026 era (Phase 1) | Phase 1 evidence: see TCM_AI_Efficiency_Database_FINAL (tear-sheets) |
| 41 | **ARX** | ACCELERANT HOL-A | Insurance Brokers | 2.9 | plan | 44 | 2026-07-21 | 2026-07-21 | Q1-2026 era (Phase 1) | Phase 1 evidence: see TCM_AI_Efficiency_Database_FINAL (tear-sheets) |
| 42 | **BRO** | BROWN & BROWN | Insurance Brokers | 23.5 | plan | 43 | 2026-07-21 | 2026-07-21 | Q1-2026 era (Phase 1) | Phase 1 evidence: see TCM_AI_Efficiency_Database_FINAL (tear-sheets) |
| 43 | **CACC** | CREDIT ACCEPTANC | Consumer Finance | 6.5 | plan | 42 | 2026-07-21 | 2026-07-21 | Q1-2026 era (Phase 1) | Phase 1 evidence: see TCM_AI_Efficiency_Database_FINAL (tear-sheets) |
| 44 | **USFD** | US FOODS HOLDING | Food Distributors | 22.3 | plan | 38 | 2026-07-21 | 2026-07-21 | Q1-2026 era (Phase 1) | Boss-designated anchor. Deep review: efficiency is Lean/routing/procurement-driven, not AI; "AI" items (MOXe) are revenue tools. Watch for genuinely AI-attributed cost numbers. |
| 45 | **HIG** | HARTFORD INSURAN | Property & Casualty Insurance | 38.6 | plan | 38 | 2026-07-21 | 2026-07-21 | Q1-2026 era (Phase 1) | Phase 1 evidence: see TCM_AI_Efficiency_Database_FINAL (tear-sheets) |
| 46 | **PNC** | PNC FINANCIAL SE | Diversified Banks | 101.5 | plan | 37 | 2026-07-21 | 2026-07-21 | Q1-2026 era (Phase 1) | Phase 1 evidence: see TCM_AI_Efficiency_Database_FINAL (tear-sheets) |

## CUT (23 names) — do not re-litigate without NEW evidence

| Ticker | Company | Sub-industry | Cut date | Reason |
|---|---|---|---|---|
| **ALL** | ALLSTATE CORP | Property & Casualty Insurance | 2026-07-21 | Phase 1 deep verification: claims failed AI-attribution / materiality bar |
| **BMO·CN** | BANK OF MONTREAL | Diversified Banks | 2026-07-21 | Phase 1 deep verification: claims failed AI-attribution / materiality bar |
| **CI** | THE CIGNA GROUP | Health Care Services | 2026-07-21 | Phase 1 deep verification: claims failed AI-attribution / materiality bar |
| **COIN** | COINBASE GLOBA-A | Financial Exchanges & Data | 2026-07-21 | Phase 1 deep verification: claims failed AI-attribution / materiality bar |
| **EQPT** | EQUIPMENTSHARE-A | Trading Companies & Distributors | 2026-07-21 | Phase 1 deep verification: claims failed AI-attribution / materiality bar |
| **EXPD** | EXPEDITORS INTL | Air Freight & Logistics | 2026-07-21 | Phase 1 deep verification: claims failed AI-attribution / materiality bar |
| **HRB** | H&R BLOCK INC | Specialized Consumer Services | 2026-07-21 | Phase 1 deep verification: claims failed AI-attribution / materiality bar |
| **JPM** | JPMORGAN CHASE | Diversified Banks | 2026-07-21 | Phase 1 deep verification: claims failed AI-attribution / materiality bar |
| **L·CN** | LOBLAW COS LTD | Food Retail | 2026-07-21 | Phase 1 deep verification: claims failed AI-attribution / materiality bar |
| **LH** | LABCORP HOLDINGS | Health Care Services | 2026-07-21 | Phase 1 deep verification: claims failed AI-attribution / materiality bar |
| **LPLA** | LPL FINANCIAL HO | Investment Banking & Brokerage | 2026-07-21 | Phase 1 deep verification: claims failed AI-attribution / materiality bar |
| **MRSH** | MARSH & MCLENNAN | Insurance Brokers | 2026-07-21 | Phase 1 deep verification: claims failed AI-attribution / materiality bar |
| **MS** | MORGAN STANLEY | Investment Banking & Brokerage | 2026-07-21 | Phase 1 deep verification: claims failed AI-attribution / materiality bar |
| **PGR** | PROGRESSIVE CORP | Property & Casualty Insurance | 2026-07-21 | Phase 1 deep verification: claims failed AI-attribution / materiality bar |
| **PRVA** | PRIVIA HEALTH GR | Health Care Services | 2026-07-21 | Phase 1 deep verification: claims failed AI-attribution / materiality bar |
| **SCHW** | SCHWAB (CHARLES) | Investment Banking & Brokerage | 2026-07-21 | Phase 1 deep verification: claims failed AI-attribution / materiality bar |
| **SKWD** | SKYWARD SPECIALT | Property & Casualty Insurance | 2026-07-21 | Phase 1 deep verification: claims failed AI-attribution / materiality bar |
| **SYY** | SYSCO CORP | Food Distributors | 2026-07-21 | Phase 1 deep verification: claims failed AI-attribution / materiality bar |
| **UNH** | UNITEDHEALTH GRP | Managed Health Care | 2026-07-21 | Phase 1 deep verification: claims failed AI-attribution / materiality bar |
| **WH** | WYNDHAM HOTELS & | Hotels, Resorts & Cruise Lines | 2026-07-21 | Phase 1 deep verification: claims failed AI-attribution / materiality bar |
| **WM** | WASTE MANAGEMENT | Environmental & Facilities Services | 2026-07-21 | Phase 1 deep verification: claims failed AI-attribution / materiality bar |
| **WSO** | WATSCO INC | Trading Companies & Distributors | 2026-07-21 | Phase 1 deep verification: claims failed AI-attribution / materiality bar |
| **YMM** | FULL TRUCK A-ADR | Cargo Ground Transportation | 2026-07-21 | Phase 1 deep verification: claims failed AI-attribution / materiality bar |

## WATCH UNIVERSE — outside (276 names)

Screened in Phase 1 with no qualifying evidence as of 2026-07-21. The daily scan re-checks each name every time it reports earnings. `Last scanned` updates on every scan, hit or not.

| Ticker | Company | Sub-industry | Mkt Cap $B | Last scanned | Last verdict |
|---|---|---|---|---|---|
| AGCO | AGCO CORP | Agricultural & Farm Machinery | 8.3 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| CNH | CNH INDUSTRIAL N | Agricultural & Farm Machinery | 12.9 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| DE | DEERE & CO | Agricultural & Farm Machinery | 158.1 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| TTC | TORO CO | Agricultural & Farm Machinery | 8.9 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| ADM | ARCHER-DANIELS | Agricultural Products & Services | 39.5 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| BG | BUNGE GLOBAL SA | Agricultural Products & Services | 22.8 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| DAR | DARLING INGREDIE | Agricultural Products & Services | 9.9 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| INGR | INGREDION INC | Agricultural Products & Services | 6.3 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| FDX | FEDEX CORP | Air Freight & Logistics | 74.9 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| GXO | GXO LOGISTIC | Air Freight & Logistics | 5.6 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| UPS | UNITED PARCEL-B | Air Freight & Logistics | 96.0 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| CTC/A·CN | CANADIAN TIRE-A | Broadline Retail | 10.1 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| DOL·CN | DOLLARAMA INC | Broadline Retail | 50.5 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| OLLI | OLLIE'S BARGAIN | Broadline Retail | 3.9 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| FDXF | FEDEX FREIGHT HO | Cargo Ground Transportation | 22.1 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| JBHT | HUNT (JB) TRANS | Cargo Ground Transportation | 26.7 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| KNX | KNIGHT-SWIFT TRA | Cargo Ground Transportation | 12.1 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| LSTR | LANDSTAR SYSTEM | Cargo Ground Transportation | 7.2 | 2026-07-29 | Q2-2026 FAIL — CEO Lonegro: agent-office AI rollout starts mid-Q3; nothing quantified |
| ODFL | OLD DOMINION FRT | Cargo Ground Transportation | 48.4 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| R | RYDER SYSTEM INC | Cargo Ground Transportation | 10.3 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| SAIA | SAIA INC | Cargo Ground Transportation | 11.5 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| TFII·CN | TFI INTERNATIONA | Cargo Ground Transportation | 17.2 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| WERN | WERNER ENT | Cargo Ground Transportation | 2.6 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| ESNT | ESSENT GROUP LTD | Commercial & Residential Mortgage Finance | 6.0 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| MTG | MGIC INVT CORP | Commercial & Residential Mortgage Finance | 6.0 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| RDN | RADIAN GROUP INC | Commercial & Residential Mortgage Finance | 5.1 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| GRMN | GARMIN LTD | Consumer Electronics | 47.0 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| ALLY | ALLY FINANCIAL I | Consumer Finance | 13.8 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| AXP | AMERICAN EXPRESS | Consumer Finance | 241.8 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| BFH | BREAD FINANCIAL | Consumer Finance | 3.9 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| COF | CAPITAL ONE FINA | Consumer Finance | 126.3 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| ENVA | ENOVA INTERNATIO | Consumer Finance | 5.8 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| EZPW | EZCORP INC-A | Consumer Finance | 2.0 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| FIGR | FIGURE TECHNOL-A | Consumer Finance | 6.6 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| OMF | ONEMAIN HOLDINGS | Consumer Finance | 7.1 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| SLM | SLM CORP | Consumer Finance | 4.7 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| SOFI | SOFI TECHNOLOGIE | Consumer Finance | 23.3 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| SYF | SYNCHRONY FINANC | Consumer Finance | 24.7 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| BJ | BJ'S WHOLESALE C | Consumer Staples Merchandise Retail | 11.5 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| COST | COSTCO WHOLESALE | Consumer Staples Merchandise Retail | 410.9 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| DG | DOLLAR GENERAL C | Consumer Staples Merchandise Retail | 27.2 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| DLTR | DOLLAR TREE INC | Consumer Staples Merchandise Retail | 24.3 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| PSMT | PRICESMART INC | Consumer Staples Merchandise Retail | 5.9 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| TGT | TARGET CORP | Consumer Staples Merchandise Retail | 61.2 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| BAP | CREDICORP LTD | Diversified Banks | 30.9 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| BNS·CN | BANK OF NOVA SCO | Diversified Banks | 152.3 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| FCNCA | FIRST CITIZENS-A | Diversified Banks | 24.1 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| FITB | FIFTH THIRD BANC | Diversified Banks | 51.8 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| KEY | KEYCORP | Diversified Banks | 25.1 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| NA·CN | NATL BK CANADA | Diversified Banks | 89.3 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| USB | US BANCORP | Diversified Banks | 97.1 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| WFC | WELLS FARGO & CO | Diversified Banks | 268.3 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| APO | APOLLO GLOBAL MA | Diversified Financial Services | 68.5 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| CRBG | COREBRIDGE FINAN | Diversified Financial Services | 13.7 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| EQH | EQUITABLE HOLDIN | Diversified Financial Services | 13.0 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| JXN | JACKSON FI-A | Diversified Financial Services | 8.4 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| VOYA | VOYA FINANCIAL I | Diversified Financial Services | 9.0 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| CTAS | CINTAS CORP | Diversified Support Services | 73.5 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| RBA·CN | RB GLOBAL INC | Diversified Support Services | 28.6 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| UNF | UNIFIRST CORP/MA | Diversified Support Services | 4.9 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| CLH | CLEAN HARBORS | Environmental & Facilities Services | 16.0 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| CWST | CASELLA WASTE | Environmental & Facilities Services | 6.2 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| GFL·CN | GFL ENVIRONM-SUB | Environmental & Facilities Services | 20.0 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| ROL | ROLLINS INC | Environmental & Facilities Services | 21.6 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| TTEK | TETRA TECH INC | Environmental & Facilities Services | 8.1 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| VLTO | VERALTO CORP | Environmental & Facilities Services | 22.8 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| WCN·CN | WASTE CONNECTION | Environmental & Facilities Services | 61.5 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| CBOE | CBOE GLOBAL MARK | Financial Exchanges & Data | 29.0 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| CME | CME GROUP INC | Financial Exchanges & Data | 88.8 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| ICE | INTERCONT EXCH I | Financial Exchanges & Data | 77.9 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| MCO | MOODY'S CORP | Financial Exchanges & Data | 86.6 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| MIAX | MIAMI INTERNATIO | Financial Exchanges & Data | 4.0 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| MKTX | MARKETAXESS | Financial Exchanges & Data | 4.1 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| MORN | MORNINGSTAR INC | Financial Exchanges & Data | 6.6 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| MSCI | MSCI INC | Financial Exchanges & Data | 45.4 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| TW | TRADEWEB MARKE-A | Financial Exchanges & Data | 21.7 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| X·CN | TMX GROUP LTD | Financial Exchanges & Data | 13.4 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| CHEF | CHEFS WAREHOUSE | Food Distributors | 4.0 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| PFGC | PERFORMANCE FOOD | Food Distributors | 17.8 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| ACI | ALBERTSONS COS-A | Food Retail | 7.2 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| ATD·CN | ALIMEN COUCHE | Food Retail | 84.3 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| CASY | CASEY'S GENERAL | Food Retail | 31.8 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| EMP/A·CN | EMPIRE CO LTD A | Food Retail | 11.3 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| KR | KROGER CO | Food Retail | 36.3 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| MRU·CN | METRO INC/CN | Food Retail | 19.8 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| SFM | SPROUTS FARMERS | Food Retail | 7.5 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| CAH | CARDINAL HEALTH | Health Care Distributors | 54.7 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| COR | CENCORA INC | Health Care Distributors | 59.6 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| HSIC | HENRY SCHEIN INC | Health Care Distributors | 9.8 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| MCK | MCKESSON CORP | Health Care Distributors | 95.1 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| ACHC | ACADIA HEALTHCAR | Health Care Facilities | 2.8 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| BKD | BROOKDALE SR | Health Care Facilities | 3.4 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| EHC | ENCOMPASS HEALTH | Health Care Facilities | 10.9 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| ENSG | ENSIGN GROUP INC | Health Care Facilities | 9.8 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| HCA | HCA HEALTHCARE I | Health Care Facilities | 86.7 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| PACS | PACS GROUP INC | Health Care Facilities | 6.8 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| THC | TENET HEALTHCARE | Health Care Facilities | 16.8 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| UHS | UNIVERSAL HLTH-B | Health Care Facilities | 9.2 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| AMN | AMN HEALTHCARE | Health Care Services | 1.3 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| BLLN | BILLIONTOONE INC | Health Care Services | 5.7 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| BTSG | BRIGHTSPRING HEA | Health Care Services | 13.5 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| CHE | CHEMED CORP | Health Care Services | 6.6 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| CVS | CVS HEALTH CORP | Health Care Services | 135.1 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| DGX | QUEST DIAGNOSTIC | Health Care Services | 23.0 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| DVA | DAVITA INC | Health Care Services | 15.1 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| GH | GUARDANT HEALTH | Health Care Services | 21.0 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| HIMS | HIMS & HERS HEAL | Health Care Services | 8.0 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| LFST | LIFESTANCE HEALT | Health Care Services | 4.2 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| OMDA | OMADA HEALTH INC | Health Care Services | 1.4 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| WGS | GENEDX HOLDINGS | Health Care Services | 1.9 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| ALGN | ALIGN TECHNOLOGY | Health Care Supplies | 12.9 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| COO | COOPER COS INC | Health Care Supplies | 13.9 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| ESTA | ESTABLISHMENT LA | Health Care Supplies | 2.6 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| HAE | HAEMONETICS CORP | Health Care Supplies | 3.5 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| ICUI | ICU MEDICAL | Health Care Supplies | 3.9 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| LNTH | LANTHEUS HOLDING | Health Care Supplies | 6.9 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| MDLN | MEDLINE INC-A | Health Care Supplies | 53.3 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| MMSI | MERIT MEDICAL | Health Care Supplies | 4.4 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| SOLV | SOLVENTUM | Health Care Supplies | 13.4 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| UFPT | UFP TECHNOLOGIES | Health Care Supplies | 1.8 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| XRAY | DENTSPLY SIRONA | Health Care Supplies | 2.6 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| CCL | CARNIVAL CORP LT | Hotels, Resorts & Cruise Lines | 36.4 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| CHH | CHOICE HOTELS | Hotels, Resorts & Cruise Lines | 4.9 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| H | HYATT HOTELS-A | Hotels, Resorts & Cruise Lines | 17.4 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| HGV | HILTON GRAND VAC | Hotels, Resorts & Cruise Lines | 4.0 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| HLT | HILTON WORLDWIDE | Hotels, Resorts & Cruise Lines | 73.4 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| HTHT | H WORLD GROU-ADR | Hotels, Resorts & Cruise Lines | 12.6 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| MAR | MARRIOTT INTL-A | Hotels, Resorts & Cruise Lines | 95.7 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| NCLH | NORWEGIAN CRUISE | Hotels, Resorts & Cruise Lines | 9.0 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| RCL | ROYAL CARIBBEAN | Hotels, Resorts & Cruise Lines | 77.4 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| TNL | TRAVEL + LEISURE | Hotels, Resorts & Cruise Lines | 4.6 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| VAC | MARRIOTT VACATIO | Hotels, Resorts & Cruise Lines | 3.4 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| VIK | VIKING HOLDINGS | Hotels, Resorts & Cruise Lines | 43.8 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| HON | HONEYWELL INTL | Industrial Conglomerates | 70.4 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| MMM | 3M CO | Industrial Conglomerates | 82.3 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| CECO | CECO ENVIRONMNTL | Industrial Machinery & Supplies & Components | 4.8 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| CR | CRANE CO | Industrial Machinery & Supplies & Components | 12.5 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| DCI | DONALDSON CO INC | Industrial Machinery & Supplies & Components | 10.3 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| DOV | DOVER CORP | Industrial Machinery & Supplies & Components | 28.9 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| EPAC | ENERPAC TOOL GRO | Industrial Machinery & Supplies & Components | 1.8 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| ESAB | ESAB CORP | Industrial Machinery & Supplies & Components | 5.3 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| ESE | ESCO TECH INC | Industrial Machinery & Supplies & Components | 8.3 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| FLS | FLOWSERVE CORP | Industrial Machinery & Supplies & Components | 8.7 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| FTV | FORTIVE CORP | Industrial Machinery & Supplies & Components | 19.0 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| GGG | GRACO INC | Industrial Machinery & Supplies & Components | 12.3 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| GTES | GATES INDUSTRIAL | Industrial Machinery & Supplies & Components | 6.7 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| GTLS | CHART INDUSTRIES | Industrial Machinery & Supplies & Components | 10.0 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| IEX | IDEX CORP | Industrial Machinery & Supplies & Components | 16.4 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| IR | INGERSOLL-RAND I | Industrial Machinery & Supplies & Components | 30.7 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| ITT | ITT INC | Industrial Machinery & Supplies & Components | 17.4 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| ITW | ILLINOIS TOOL WO | Industrial Machinery & Supplies & Components | 78.1 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| JBTM | JBT MAREL CORP | Industrial Machinery & Supplies & Components | 7.2 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| KAI | KADANT INC | Industrial Machinery & Supplies & Components | 3.4 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| LECO | LINCOLN ELECTRIC | Industrial Machinery & Supplies & Components | 13.8 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| MFP | MIDERA FOOD PROC | Industrial Machinery & Supplies & Components | 1.9 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| MIDD | MIDDLEBY CORP | Industrial Machinery & Supplies & Components | 6.1 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| MLI | MUELLER INDS | Industrial Machinery & Supplies & Components | 12.5 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| NDSN | NORDSON CORP | Industrial Machinery & Supplies & Components | 16.0 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| NPO | ENPRO INC | Industrial Machinery & Supplies & Components | 6.9 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| OTIS | OTIS WORLDWI | Industrial Machinery & Supplies & Components | 28.2 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| PH | PARKER HANNIFIN | Industrial Machinery & Supplies & Components | 119.9 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| PNR | PENTAIR PLC | Industrial Machinery & Supplies & Components | 12.4 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| RBC | RBC BEARINGS INC | Industrial Machinery & Supplies & Components | 18.5 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| SNA | SNAP-ON INC | Industrial Machinery & Supplies & Components | 20.8 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| SPXC | SPX TECHNOLOGIES | Industrial Machinery & Supplies & Components | 10.8 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| SWK | STANLEY BLACK & | Industrial Machinery & Supplies & Components | 13.5 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| SXI | STANDEX INTL CO | Industrial Machinery & Supplies & Components | 3.7 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| SYM | SYMBOTIC INC | Industrial Machinery & Supplies & Components | 25.6 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| TKR | TIMKEN CO | Industrial Machinery & Supplies & Components | 9.6 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| WTS | WATTS WATER TE-A | Industrial Machinery & Supplies & Components | 11.6 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| XYL | XYLEM INC | Industrial Machinery & Supplies & Components | 28.8 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| AJG | ARTHUR J GALLAGH | Insurance Brokers | 67.1 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| GSHD | GOOSEHEAD INSU-A | Insurance Brokers | 2.0 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| BGC | BGC GROUP INC-A | Investment Banking & Brokerage | 5.3 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| BULL | WEBULL CORP | Investment Banking & Brokerage | 3.9 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| EVR | EVERCORE INC | Investment Banking & Brokerage | 12.9 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| FRHC | FREEDOM HOLDING | Investment Banking & Brokerage | 9.9 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| FUTU | FUTU HOLDING-ADR | Investment Banking & Brokerage | 13.5 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| GS | GOLDMAN SACHS GP | Investment Banking & Brokerage | 320.6 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| HLI | HOULIHAN LOKEY I | Investment Banking & Brokerage | 9.2 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| IBKR | INTERACTIVE BROK | Investment Banking & Brokerage | 159.1 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| JEF | JEFFERIES FINANC | Investment Banking & Brokerage | 10.2 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| LAZ | LAZARD INC | Investment Banking & Brokerage | 4.6 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| MC | MOELIS & CO-CL A | Investment Banking & Brokerage | 5.0 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| MRX | MAREX GROUP LTD | Investment Banking & Brokerage | 4.7 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| PIPR | PIPER SANDLER CO | Investment Banking & Brokerage | 5.1 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| PJT | PJT PARTNERS - A | Investment Banking & Brokerage | 7.0 | 2026-07-29 | Q2-2026 FAIL — CEO Taubman: AI an unquantified expense headwind; rest is AI-as-deal-flow |
| RJF | RAYMOND JAMES | Investment Banking & Brokerage | 32.5 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| SF | STIFEL FINANCIAL | Investment Banking & Brokerage | 11.5 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| SNEX | STONEX GROUP INC | Investment Banking & Brokerage | 8.9 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| VIRT | VIRTU FINANCIA-A | Investment Banking & Brokerage | 10.0 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| XP | XP INC - CLASS A | Investment Banking & Brokerage | 8.5 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| AFL | AFLAC INC | Life & Health Insurance | 62.8 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| BHF | BRIGHTHOUSE FINA | Life & Health Insurance | 3.8 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| CNO | CNO FINANCIAL GR | Life & Health Insurance | 4.9 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| GL | GLOBE LIFE INC | Life & Health Insurance | 13.9 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| GWO·CN | GREAT-WEST LIFEC | Life & Health Insurance | 82.1 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| IAG·CN | IA FINANCIAL COR | Life & Health Insurance | 18.0 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| LNC | LINCOLN NATL CRP | Life & Health Insurance | 7.8 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| MET | METLIFE INC | Life & Health Insurance | 59.9 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| PFG | PRINCIPAL FINL | Life & Health Insurance | 24.5 | 2026-07-29 | Q2-2026 FAIL — CEO Strable frames AI as spend, not a measured outcome |
| POW·CN | POWER CORP CDA | Life & Health Insurance | 56.1 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| PRI | PRIMERICA INC | Life & Health Insurance | 9.7 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| PRU | PRUDENTL FINL | Life & Health Insurance | 40.3 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| SLF·CN | SUN LIFE FINANCI | Life & Health Insurance | 61.5 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| UNM | UNUM GROUP | Life & Health Insurance | 14.3 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| A | AGILENT TECH INC | Life Sciences Tools & Services | 37.9 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| ADPT | ADAPTIVE BIOTECH | Life Sciences Tools & Services | 3.4 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| AVTR | AVANTOR INC | Life Sciences Tools & Services | 7.2 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| BIO | BIO-RAD LABS-A | Life Sciences Tools & Services | 8.0 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| BRKR | BRUKER CORP | Life Sciences Tools & Services | 9.0 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| CRL | CHARLES RIVER LA | Life Sciences Tools & Services | 11.1 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| DHR | DANAHER CORP | Life Sciences Tools & Services | 141.7 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| ICLR | ICON PLC | Life Sciences Tools & Services | 12.7 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| ILMN | ILLUMINA INC | Life Sciences Tools & Services | 28.8 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| IQV | IQVIA HOLDINGS I | Life Sciences Tools & Services | 34.6 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| MEDP | MEDPACE HOLDINGS | Life Sciences Tools & Services | 15.1 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| MTD | METTLER-TOLEDO | Life Sciences Tools & Services | 26.3 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| PSNL | PERSONALIS INC | Life Sciences Tools & Services | 1.6 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| QGEN | QIAGEN NV | Life Sciences Tools & Services | 8.6 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| RGEN | REPLIGEN CORP | Life Sciences Tools & Services | 8.2 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| RVTY | REVVITY INC | Life Sciences Tools & Services | 12.4 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| SHC | SOTERA HEALTH CO | Life Sciences Tools & Services | 5.2 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| TECH | BIO-TECHNE CORP | Life Sciences Tools & Services | 11.2 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| TEM | TEMPUS AI INC-A | Life Sciences Tools & Services | 10.0 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| TMO | THERMO FISHER | Life Sciences Tools & Services | 196.4 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| TXG | 10X GENOMICS I-A | Life Sciences Tools & Services | 5.3 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| WAT | WATERS CORP | Life Sciences Tools & Services | 36.6 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| WST | WEST PHARMACEUT | Life Sciences Tools & Services | 25.4 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| ALHC | ALIGNMENT HEALTH | Managed Health Care | 4.2 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| CNC | CENTENE CORP | Managed Health Care | 33.7 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| ELV | ELEVANCE HEALTH | Managed Health Care | 92.3 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| HUM | HUMANA INC | Managed Health Care | 48.7 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| MOH | MOLINA HEALTHCAR | Managed Health Care | 12.7 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| PGNY | PROGYNY INC | Managed Health Care | 2.5 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| ACGL | ARCH CAPITAL GRP | Property & Casualty Insurance | 36.0 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| AFG | AMER FINL GROUP | Property & Casualty Insurance | 11.9 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| AIZ | ASSURANT INC | Property & Casualty Insurance | 13.9 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| AXS | AXIS CAPITAL | Property & Casualty Insurance | 8.4 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| CINF | CINCINNATI FIN | Property & Casualty Insurance | 28.4 | 2026-07-29 | Q2-2026 FAIL — CFO Sewell: "AI, this and that"; no named system, no number |
| ERIE | ERIE INDEMNITY-A | Property & Casualty Insurance | 12.9 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| FAF | FIRST AMERICAN F | Property & Casualty Insurance | 7.1 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| FFH·CN | FAIRFAX FINL HLD | Property & Casualty Insurance | 54.1 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| FNF | FIDELITY NATIONA | Property & Casualty Insurance | 13.5 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| KNSL | KINSALE CAPITAL | Property & Casualty Insurance | 8.0 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| L | LOEWS CORP | Property & Casualty Insurance | 24.0 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| MCY | MERCURY GEN CORP | Property & Casualty Insurance | 6.1 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| MKL | MARKEL GROUP INC | Property & Casualty Insurance | 24.6 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| ORI | OLD REPUB INTL | Property & Casualty Insurance | 10.2 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| PLMR | PALOMAR HOLDINGS | Property & Casualty Insurance | 3.7 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| RLI | RLI CORP | Property & Casualty Insurance | 5.7 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| SIGI | SELECT INS GRP | Property & Casualty Insurance | 5.8 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| THG | HANOVER INSURANC | Property & Casualty Insurance | 7.6 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| WRB | WR BERKLEY CORP | Property & Casualty Insurance | 27.5 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| WTM | WHITE MOUNTAINS | Property & Casualty Insurance | 5.4 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| FTDR | FRONTDOOR INC | Specialized Consumer Services | 5.3 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| SCI | SERVICE CORP INT | Specialized Consumer Services | 11.0 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| ARW | ARROW ELECTRONIC | Technology Distributors | 10.3 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| AVT | AVNET INC | Technology Distributors | 7.0 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| CDW | CDW CORP/DE | Technology Distributors | 18.4 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| NSIT | INSIGHT ENTERPRI | Technology Distributors | 3.7 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| SNX | TD SYNNEX CORP | Technology Distributors | 20.1 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| AER | AERCAP HOLDINGS | Trading Companies & Distributors | 24.1 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| AIT | APPLIED INDU TEC | Trading Companies & Distributors | 12.2 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| CNM | CORE & MAIN IN-A | Trading Companies & Distributors | 8.7 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| FAST | FASTENAL CO | Trading Companies & Distributors | 54.0 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| FTT·CN | FINNING INTL INC | Trading Companies & Distributors | 13.6 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| GATX | GATX CORP | Trading Companies & Distributors | 6.4 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| GWW | WW GRAINGER INC | Trading Companies & Distributors | 65.7 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| HRI | HERC HOLDINGS IN | Trading Companies & Distributors | 4.9 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| MSM | MSC INDL DIRECT | Trading Companies & Distributors | 6.9 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| SITE | SITEONE LANDSCAP | Trading Companies & Distributors | 4.7 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| SUNB | SUNBELT RENTALS | Trading Companies & Distributors | 30.2 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| TIH·CN | TOROMONT INDS | Trading Companies & Distributors | 18.5 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| URI | UNITED RENTALS | Trading Companies & Distributors | 68.0 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
| WCC | WESCO INTL | Trading Companies & Distributors | 16.1 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |

## EVIDENCE LOG (append-only)

Every ADD / PROMOTE / DEMOTE / CUT / score change gets one dated entry here with the quantified evidence quoted verbatim and its source. Baseline evidence lives in the Phase 1 deliverables.

- 2026-07-21 — BASELINE — Phase 1 deep verification complete: 21 realized, 25 plan, 23 cut, 276 outside. Top score CHRW 87. Full evidence in TCM_AI_Efficiency_Database_FINAL.pdf/.xlsx.
- 2026-07-28 — SCAN — 82 of the 345 reported 21–28 Jul. 62 screened; 3 passed the thin screen (AXP, FAF, GSHD) and all 3 were rejected on deep scan. AXP 22: CEO Squeri disclaimed his own 30–40% coding cycle-time figure one sentence later ("that's really not a savings"); opex ratio 150bp worse YoY and 62% of the pretax gain was a $321mm provision release. FAF 24: richest AI disclosure of the quarter, but order counts were flat-to-down while revenue per order rose 17.3%, so opex per closed order ROSE ~10.6%; peer Stewart posted a BETTER 210bp labour-ratio improvement with no AI story. GSHD 20: management's own bridge of 30% EBITDA growth omitted the AI tool entirely, and the CFO guided comp and G&A to grow ahead of core revenue. Zero admissions, zero score moves. Cut names MRSH/SCHW/WH rechecked — no new evidence (SCHW closest: 15–20% developer productivity, explicit attribution but no flow-through to any expense line).
- 2026-07-28 — SCAN (second pass, same day) — finnhub earnings calendar unreachable this run (WebFetch returned PROVENANCE_REQUIRED on every attempt, including via subagent), so Tier 0 could add no new reporters; the queue was the 33 names in pending_requeue. 33 screened for transcript availability, 5 actually scanned. 26 remain requeued: 13 held calls on 28 Jul with no transcript published yet (SPGI, CINF, UHS, ITW, PNR, XYL, HLT, RCL, HRI, LSTR, WERN, PFG, PJT) and 13 hold calls on 29–30 Jul (AON, WM, ACGL, AXS, THG, ACHC, CHE, ENSG, ICLR, BG, CR, VLTO, UNM). Two thin-screen PASSes, both destroyed on deep scan. CNC 32: CEO London's AI legal-invoice agent saving "a point and a half" a month is real and honestly disclosed but bounds to 0.01–0.12% of SG&A; membership fell 7.6% while SG&A dollars rose $67mm, so SG&A per member per month ROSE 10.6% to $39.96 — the 20bp ratio gain is revenue leverage and Marketplace mix runoff, which management's own bridge says twice without mentioning AI. UPS 18: the 28% automated-building cost advantage is conveyor/sortation capex, not AI — the CEO's answer never says AI, the figure has been repeated unchanged for three quarters, and cost per piece ROSE ~8.5% adjusted (~17% GAAP) in the quarter automation penetration rose to 68.5%; FedEx delivered a larger, explicitly quantified $1bn cost-out on the identical mechanism with no AI story at all. BRO FAIL: named Anthropic, McKinsey and Accenture partnerships with explicit "faster cycle times, higher productivity" language but not one hard number — score held at 43, no move without evidence. IQV FAIL (90bp margin expansion attributed to broad productivity programmes; CFO Fedock: AI is "just another lever in that toolkit"; rest is AI-as-revenue). RGEN FAIL (no AI mention of any kind). GTLS removed from the queue — acquired by Baker Hughes, merger closed 16 Jul 2026, listing terminated. MLI removed — reported by press release only, no conference call exists to screen. Zero admissions, zero promotions, zero demotions, zero score moves.
- 2026-07-28 — REVIEW (third pass, test fire) — SPGI and BRO taken as priority admitted names, plus a transcript re-check of the twelve 28 Jul callers. SPGI: still no published transcript after a second search across seven sources; MarketBeat/Markets Daily 'earnings call highlights' pages are AI-generated summaries and were rejected as transcript substitutes; score held at 60, last_scanned not advanced, requeued. Flag carried forward: SPGI has issued recast segment financials, which can move a metric definition innocently. BRO: full admitted-name review of the Q2-2026 call against the suspicion that -0.7% organic growth would tempt management to relabel ordinary cost control as AI. It did not — the AI-attributed quantified list is EMPTY, and all eleven quantified expense/margin items are bridged by management to lower interest income, contingents, Accession synergies, one-time accruals and staff departures. A demotion 43 -> 28 with a cut was drafted on the non-restatement of Q1's '25% of the end-to-end submission process' and 'saving more than 50,000 hours annually', then destroyed on the adversarial pass: the written rubric penalises staleness only after four quarters at -5/quarter, nothing was contradicted or disowned, the margin decline has no AI content, one pillar rested on an unverifiable quote, the promotional-tone penalty had already been waived for UPS in this same run, and the cohort test showed AON (50) and WTW (54) carry identical evidence vintage but report 29-30 Jul — so a cut would have scored disclosure timing rather than substance. BRO HELD at plan/43 with a hard Q3-2026 trigger recorded. Twelve 28 Jul callers (CINF, UHS, ITW, PNR, XYL, HLT, RCL, HRI, LSTR, WERN, PFG, PJT) re-checked: zero transcripts posted since the earlier pass, all remain requeued with last_scanned unchanged. Zero additions, zero promotions, zero demotions, zero score moves.

- 2026-07-29 — SCAN (29 Jul) — Tier 0 DEGRADED: finnhub.io is unreachable from this container through WebFetch (PROVENANCE_REQUIRED on every attempt, main session and subagent, both 28 and 29 Jul date URLs); this is the second consecutive run with no finnhub calendar. Fell back to a secondary published calendar (Kiplinger week of 27-31 Jul), which intersected to 33 in-universe names; combined with the 26-name requeue the queue was 56 unique names. The fallback calendar proved UNRELIABLE ON DATES: every name it listed under 28 Jul (AER, AVTR, BG, CHEF, CLH, EVR, FTV, GRMN, HUM, IEX, ODFL, OMF, SITE, SOFI, SWK, WSO, AON, ARCB, LMND, OPCH) was confirmed from the companies' own scheduling releases to be a 29 Jul call, and four of its 29 Jul names (ICLR, MTG, TTEK, FLS) are 30 Jul calls. Tier 1 subagents caught this by verifying each call date at screen time rather than trusting the calendar; no name was screened against the wrong quarter and no verdict was recorded on an unheld call. OUTCOME: 4 of 56 actually screened — CINF, LSTR, PFG, PJT, all four 28 Jul calls with full investing.com transcripts, all four FAIL on the same pattern: AI named without a number, or a number named without AI. 0 PASS, therefore no Tier 2 and no adversarial pass. 52 names carry NO_TRANSCRIPT and were NOT stamped last_scanned; they return to the requeue. The binding constraint is now source lag, not screening capacity: free-tier publishers (investing.com, fool.com, benzinga, alphastreet, stockanalysis) are running roughly 4-7 days behind this cohort, and WERN's Q2 transcript verifiably exists but only behind the Seeking Alpha paywall, which protocol excludes. Traps logged and avoided: an investing.com 'Humana posts higher profit in Q2 2026' page that is Humana AB of Sweden, not HUM; an 'MTG Q2 2026' page that is Modern Times Group AB of Stockholm, not MGIC; HLI and TTEK fiscal-quarter transcripts (HLI FY ends 31 Mar, so today's call is fiscal Q1 FY27) offered as calendar Q2; a marketbeat HLT page that is Hilton Q1 2022; and a marketbeat HRI page that is an earnings preview. AI-generated 'earnings call highlights' pages from gurufocus, marketbeat, dailypolitical, StockStory and BigGo were rejected as transcript substitutes throughout, consistent with the 28 Jul SPGI precedent. No additions, no promotions, no demotions, no score moves, no new near-misses. Nothing in the database changed.

- 2026-07-30 — SCAN (30 Jul) — Tier 0 DEGRADED for a third consecutive run: finnhub.io returned PROVENANCE_REQUIRED to WebFetch and is proxy-blocked from the shell, so the calendar was rebuilt from earningscall.biz for 29 and 30 Jul and intersected with the universe. 88-name queue, 13 already scanned 29 Jul, 75 screened or attempted. 27 names scanned to a full transcript; 3 Tier 1 PASSes, all already-admitted names; 3 Tier 2 deep reviews with independent adversarial passes; 0 additions, 0 promotions, 0 demotions, 0 score moves. WM — the only cut-name reopen request of the run, DENIED. Fish's "$300 million of run rate EBITDAs" for Smart Truck is a first-time dollar label on a platform Morris dated to "closer to a decade" on the pre-cut Q1-2026 call, blends revenue capture with cost, is refused the AI framing by Fish himself, and sits against collection unit cost that ROSE 2.1%. Peer set decisive: Clean Harbors +190bp with no AI story; Waste Connections, with far better AI disclosure, books $20m realized against WM's unitemized $300m. Cut stands; recorded as a near-miss. PFSI — held at 63. The Q2 call introduced a genuinely new quantified framework (150 mapped origination tasks, 25% automated today, 80% targeted by YE2027, 40-80% cycle-time reduction, cost to originate down >50%), but the adversarial pass killed the score move: Spector attributes the $60m to "rates being higher" and a smaller market, AI is credited only with making the cut safe ("while preserving operational capacity"), CFO Perotti's entire expense bridge names volume and capacity and never AI, the 25% is an unweighted count of self-defined task types Spector concedes is "low-hanging fruit", and production expenses rose 35% YoY across five consecutive quarters. Realized AI-attributed saving this quarter: $0. No mortgage peer had reported Q2 yet, so the peer test has no control group — a further reason not to move. SPGI — held at 60. Goalpost check passes cleanly (end-2027 deadline unchanged since Q4-2025) but attribution is blended ("AI-driven efficiencies and other productivity initiatives"), the $100m target is ~1.3% of company expenses, and Cheung's margin bridge credits "disciplined expense management" with no AI. Third consecutive run with no speaker-attributed primary source. CHRW — DEMOTION REVIEW OPENED, SCORE HELD AT 87. The adversarial pass built a serious case for 87 to ~35: the productivity metric definition was withdrawn this quarter (prior calls named shipments per person per day; the Q2 8-K says only "productivity" and merges the previously separate NAST and Global Forwarding series into a single ">60%" floor), opex ROSE $4.9m YoY so 112% of the operating-income gain came from gross profit, personnel cost per employee rose 13.2% on headcount down 10.8%, $26.8m of H1 severance is co-mingled with the AI headcount story, and the company's own disclosure of truckload rate per mile +25.5% points to rate inflation. It is held because the peer-set check — the runbook's single most decisive test, mandatory every run — could not be run once the session WebSearch budget was exhausted, and no full Q2 transcript was obtainable from any permitted source. A 52-point cut to the calibration anchor of the whole scale will not be taken on an incomplete Tier 2. CHRW carries pending_deep_review and is first in the queue next run. CORRECTION (append-only, supersedes nothing): the widely-quoted CHRW claim that the Lean AI Engineer "can assess a supply chain in 25 to 30 minutes, compared with assessments that can take up to four weeks" originates in a BusinessWire product-launch release dated 2026-05-20, not an earnings call, and is struck from the earnings-call evidence set. The "more than 450 in-house engineers and data scientists" figure has been unchanged for four quarters and is a static input metric. DISCLOSURE-ATTRITION FLAGS raised on three admitted names that reported and quantified nothing: HOOD (realized/70, zero AI operational disclosure this quarter), AON (plan/50) and OPCH (plan/47). None is a demotion yet; a second consecutive absent quarter makes each one. Closest outside names, all rejected: GWO — Empower CEO Ed Murphy ties AI and straight-through processing to "driving our unit cost lower" with no figure attached; FTV — Gordian Flash AI cuts construction cost estimating "from days to minutes", unquantified and customer-facing; THG — named proprietary tool Triage Pro, zero quantification; MC — Moelis discussed AI at length and the CFO expressly declined to quantify it. MORN flagged STRUCTURAL: Morningstar holds no earnings conference call and can never yield a transcript-based verdict; removed from the transcript requeue.

## RUN LOG (append-only)

One line per scan run: date · names checked (earnings since last scan) · adds/promotions/demotions · memo produced y/n.

- 2026-07-21 — baseline established (Phase 1). No automated runs yet.
- 2026-07-28 — First automated scan. 82 reporters identified · 62 screened · 3 deep reviews · 0 additions · 0 promotions · 0 demotions · 0 score moves · 3 near-misses recorded · 32 names requeued pending transcript publication. Memo: yes.
- 2026-07-28 — Second scan of 28 Jul (requeue pass). Tier 0 blocked — finnhub calendar unreachable, no new reporters added · 33 queued · 5 scanned · 2 deep reviews · 0 additions · 0 promotions · 0 demotions · 0 score moves · 2 near-misses recorded (CNC 32, UPS 18) · 2 names retired from the queue (GTLS delisted, MLI no call) · 26 requeued. Memo: yes.
- 2026-07-28 — Third pass (manual test fire). SPGI + BRO priority review · 14 names re-checked · 0 new transcripts · 0 additions · 0 promotions · 0 demotions · 0 score moves · 1 demotion drafted and rejected on adversarial review (BRO held at plan/43, Q3 trigger recorded) · 26 requeued. Memo: yes.
- 2026-07-29 — Scan of 29 Jul. Tier 0 degraded — finnhub unreachable for a second consecutive run, secondary calendar used and found unreliable on dates · 56 queued · 4 scanned · 4 FAIL · 0 PASS · 0 deep reviews · 0 additions · 0 promotions · 0 demotions · 0 score moves · 0 near-misses · 52 requeued (transcript lag). Memo: no change to report.

- 2026-07-30 — Scan of 30 Jul. Tier 0 degraded a third consecutive run (finnhub blocked; earningscall.biz substituted for 29-30 Jul) · 88 queued · 75 attempted · 27 scanned to full transcript · 3 PASS (all already admitted) · 3 Tier 2 deep reviews with independent adversarial passes · 1 cut-name reopen request DENIED (WM) · 0 additions · 0 promotions · 0 demotions · 0 score moves · 1 new near-miss (WM) · 1 demotion review opened and held pending the mandatory peer test (CHRW 87) · 3 disclosure-attrition flags (HOOD, AON, OPCH) · 1 evidence correction (CHRW 25-minute claim struck as marketing) · 48 requeued. Session WebSearch budget exhausted at 200/200, which blocked the CHRW peer set. Memo: yes.

## NEAR-MISSES (rejections worth recording)

Borderline evidence is a rejection. Each entry records the kill reasoning and a watch item.

### AXP — AMERICAN EXPRESS · Consumer Finance · score 22 · call 2026-07-24
**CEO disclaimed his own AI number in the next sentence**

> "anywhere from a 30 to 40% decrease in cycle time from a coding perspective." — Stephen Squeri, Chairman & CEO

> "Now that's really not a savings because what that does is allows us to do more." — Stephen Squeri, Chairman & CEO

> "a lack of acceleration in hiring of more travel representatives, more customer service reps, even as the business continues to grow" — Stephen Squeri, Chairman & CEO

*Source:* https://www.investing.com/news/transcripts/earnings-call-transcript-american-express-beats-q2-2026-eps-shares-fall-93CH-4812024

**Kill.** The CEO removes his own headline from contention one sentence later: the coding gain is recycled into backlog throughput, not harvested as cost. The financials agree — total expenses +12.3% on revenue +10.0%, opex ratio 150bp WORSE year over year, and 62% of the pretax increase comes from a $321mm provision release. The metric definition also drifted in a single quarter, from Q1's '30% benefit... coding and testing' to Q2's '30–40% decrease in cycle time... coding'.

**What survives.** Management does attribute flat servicing hiring to AI tools — explicit, correctly ordered attribution. But it arrives with no rep count, no baseline and no cost figure. Attribution without quantification is a lead, not evidence.

**Materiality.** Most generous construction: ~$23mm quarterly, 0.16% of the $14,482mm expense base — below the 0.5% floor.

**Watch.** Q3 2026: if servicing headcount actually declines as Squeri predicts AND the opex ratio inflects below 72%, re-open with a quantified basis. Otherwise hard reject.

### FAF — FIRST AMERICAN FINANCIAL · Property & Casualty Insurance · score 24 · call 2026-07-23
**Richest AI disclosure of the quarter; unit costs went the wrong way**

> "Using our new AI tools, we reduced the time required by 97%." — Mark Seaton, CEO

> "It has now processed more than 50,000 orders, delivering 92% with no additional human review." — Mark Seaton, CEO

> "We have also improved automation rates from 30% in Q1 to 34% in Q2, and so far in July, we are at 39%." — Mark Seaton, CEO

*Source:* https://www.investing.com/news/transcripts/earnings-call-transcript-first-american-financial-tops-q2-2026-estimates-93CH-4809563

**Kill.** Revenue rose 15% on a 17.3% lift in revenue per order while order counts were FLAT to DOWN (closes 2,145/day vs 2,161). Title firms staff to order count but bill on order value, so price and commercial mix compress the expense ratio with zero productivity gain. Opex per closed order actually ROSE ~10.6% and personnel per order ~8.4%. The 97% covers a one-time 1,300-form template update. Management's own success ratio MISSED at 66% against a 60% target.

**What survives.** Endpoint's 30%→34%→39% series is genuinely consistently defined across two quarters — the single best piece of evidence in the file. The title-plant data moat is a credible mechanism.

**Materiality.** Every AI figure is an activity metric with no dollar or headcount attached. Exam Assist's 50,000 cumulative orders is ~36% of ONE quarter's direct closes; Endpoint's 39% applies to one converted branch, with network rollout not due until end-2027.

**Watch.** FNF, the decisive comparable, reports 2026-08-05. Re-scan after it prints and after two more Endpoint datapoints on a stable definition.

### GSHD — GOOSEHEAD INSURANCE · Insurance Brokers · score 20 · call 2026-07-22
**Management's own margin bridge omits the AI tool**

> "Lily, our AI voice assistant, now handles approximately 20% of our inbound service calls from start to finish, with performance exceeding 30% during certain periods." — Mark Jones Jr., President & COO

> "intelligent case routing, which has allowed us to reinvest roughly 40 full-time service team members towards more complex and value-added interactions" — Mark Miller, CEO (Q1 2026)

> "comp and G&A to grow in the high teens to low 20% for the year, which will likely be in excess of core revenue growth" — John Martin, CFO

*Source:* https://m.investing.com/news/transcripts/earnings-call-transcript-goosehead-beats-q2-2026-estimates-shares-rebound-after-hours-93CH-4807139

**Kill.** Management bridged 30% adjusted EBITDA growth to retention of 86%, new business, carrier commission dynamics and bind rates — and did not mention AI. When management lists its own margin bridge and omits the tool, the analyst does not get to add it. The CFO then guided comp and G&A to grow AHEAD of core revenue, which is the opposite of harvesting service automation. The metric definition also narrowed: Q1's 'all inbound calls' became Q2's 'inbound service calls', mechanically inflating the ratio, so 19%→20% may be flat or down like-for-like.

**What survives.** The peer check FAILS to kill it — Brown & Brown's margin went the other way (EBITDAC 35.7% vs 36.7%), so there is no sector tailwind explaining GSHD away. Its expansion is company-specific. The mechanism is also genuinely credible: 2.1m policies in force and labour-intensive personal-lines service calls are exactly where voice AI works.

**Materiality.** The 40 redeployed FTEs are ~$4.9mm, ~1.7% of FY2025 opex — but they were REINVESTED, not removed. Realized disclosed saving: $0. Headcount leverage also predates Lily's deployment.

**Watch.** Q3 2026: one disclosure — service headcount against policies in force, or cost per service interaction, on a stable definition — would put this into scoring range quickly.

### CNC — CENTENE CORP · Managed Health Care · score 32 · call 2026-07-28
**Real AI saving, honestly disclosed, roughly two orders of magnitude too small to reach the financials**

> "Even our legal department has several high ROI adjunctive use cases in production." — Sarah London, Chief Executive Officer

> "including one agent that reviews invoices from outside counsel firms and now saves us a point and a half in our legal bills every month" — Sarah London, Chief Executive Officer

> "reflecting continued discipline and scale, as well as product mix." — Drew Asher, Chief Financial Officer

*Source:* https://www.investing.com/news/transcripts/earnings-call-transcript-centene-beats-q2-2026-forecasts-but-shares-fall-93CH-4817133

**Kill.** The saving is 1.5% of an undisclosed sub-line-item — outside counsel spend, which appears nowhere in Centene's income statement — so it is structurally unverifiable and bounds to roughly $1.5–$15mm a year, 0.01–0.12% of annualised SG&A. Management's own bridge explains the 20bp adjusted SG&A improvement (7.1% → 6.9%) twice without AI: the CFO cites "continued discipline and scale, as well as product mix", and the release cites "leveraging of expenses over higher revenues and reduced Marketplace membership, which operates at a meaningfully higher SG&A expense ratio". The unit-cost test is fatal — membership fell 7.6% (28.00mm → 25.89mm) while SG&A dollars ROSE $67mm to $3,103mm, so SG&A per member per month rose from $36.14 to $39.96, +10.6% (+20.6% ex-PDP). The ratio fell only because revenue per member rose 13.0%. The real SG&A lever is a $480mm workforce and enterprise optimisation programme that management never attributes to AI.

**What survives.** The mechanism is genuine and the disclosure is unusually restrained — outside-counsel e-billing review is a mature, auditable AI application, and London volunteered a hard percentage while calling the use cases "adjunctive" and describing AI deployed "selectively, with a strong focus on return on investment rather than broad experimentation". No revenue conflation. CNC was also the only managed-care name in the peer set to improve its ratio at all (UNH +40bp, ELV +100bp, MOH +50bp) — but that gap is revenue growth (+4.5% vs Molina −4.8%), not productivity, so the peer test did not rescue it.

**Materiality.** $1.5–$15mm a year on the disclosed 1.5%; 0.012–0.121% of ~$12.4bn annualised SG&A; explains 0.4–4.2% of the 20bp improvement. Below the 0.5% floor by an order of magnitude.

**Watch.** Q3/Q4 2026: re-open only on (a) an absolute dollar AI-attributed SG&A saving, or disclosure of the legal spend base that makes "a point and a half" computable, AND (b) SG&A per member per month falling year over year — the test is a print below the $36.14 Q2-2025 baseline. Also watch whether any quantified share of the $480mm optimisation programme is attributed to AI-enabled workflows rather than headcount, and whether AI moves out of the legal department into claims, FWA or member services. A repeat of the legal-only anecdote with no dollar base is confirmation of immateriality, not corroboration.

### UPS — UNITED PARCEL-B · Air Freight & Logistics · score 18 · call 2026-07-28
**Conveyor automation wearing an AI label — and unit cost went the wrong way**

> "We know that the cost per piece in an automated building is about 28% lower than a non-automated building." — Carol Tomé, Chairman & CEO

> "By the end of the second quarter, 68.5% of the volume in our U.S. business was flowing through an automated building compared to 64% one year ago." — Carol Tomé, Chairman & CEO

> "Strong base rate growth and increased productivity in our reconfigured network contributed to revenue per piece growing 130 basis points faster than the cost per piece growth rate." — Brian Dykes, Chief Financial Officer

*Source:* https://www.investing.com/news/transcripts/earnings-call-transcript-ups-beats-q2-2026-estimates-but-shares-fall-93CH-4817084

**Kill.** The 28%/68.5%/337mm-package evidence is not about artificial intelligence. It describes a UPS facility classification — conveyors, sortation and robotics, 127 automated buildings at end-2025 with 24 more planned — and Tomé's answer to Jordan Aliger (Goldman Sachs) never uses the word AI. The call's four AI references ("AI as the brain", an "AI-powered digital twin", "Our AI is constantly tracking network performance") carry no number, no named system and no baseline; joining them to the 28% is an inference the company never made. The 28% has been stated identically on three consecutive calls (Q4-2025, Q1-2026, Q2-2026), never dated and never reconciled to the segment P&L — a costing constant used to justify capex, not a measured saving. Decisively, unit cost moved the wrong way: revenue per piece +9.3% less the CFO's own 130bp spread implies cost per piece ROSE ~8.0% (adjusted arithmetic +8.5%, GAAP +17.2%) in the very quarter automation penetration rose 4.5pp. The full 100bp US Domestic adjusted margin gain reconciles arithmetically to price over cost, and Dykes' bridge names base rates, customer mix, fuel and "our reconfigured network" — automation and AI appear nowhere in it.

**What survives.** UPS has the right SHAPE of disclosure — a repeated cost-per-piece ratio, a tracked penetration series (64% → 66.5% → 68.5%), and a package-equivalent conversion — and it beat its own quantified automation target (68% of US volume by year-end 2026) two quarters early, alongside $3.5bn of 2025 savings delivered and $3bn reaffirmed for 2026. RFID is fully deployed across all US delivery facilities and package cars and the network digital twin is a real system, not vapour. If a number is ever attached to either and it enters the CFO's bridge, UPS becomes a live candidate quickly.

**Materiality.** Taken at face value the penetration shift is ~126bp of blended cost per piece, ~$170mm a quarter / ~$690mm annualised against a $13.7bn adjusted US Domestic cost base — material in size, but zero of it currently attributable to AI, and swamped by an 850bp actual increase in cost per piece.

**Watch.** Q3 2026 (late Oct): (1) does adjusted cost per piece turn negative year over year — with the Amazon glide-down complete and ~2mm pieces/day gone, Q3 is the first clean read without the volume-deleverage alibi; (2) does the 28% move, get dated or get reconciled — a fourth identical print confirms it as a costing constant and it should be permanently discounted; (3) does automation or AI enter the CFO's margin bridge, which is the admission gate; (4) any number attached to RFID or the digital twin — misload rate, hours per building, planning cycle time. That, not the 28%, would be UPS's first genuine criteria-A datapoint.

**Scoring note.** Adversarial reviewer recommended 3 after a −10 promotional-tone and −5 AI-revenue-conflation penalty against a gross of 18. The run analyst recorded the gross 18 and waived both: UPS never claimed the 28% for AI and its AI language is descriptive rather than promotional — the over-reading was the thin screen's, not management's. Either figure is far below the 38 floor; the rejection is unchanged.


### WM — WASTE MANAGEMENT · Environmental & Facilities Services · reopen DENIED · call 2026-07-29
**Reopen denied — a dollar sign newly attached to a decade-old camera platform, and unit cost rose**

> our Smart Truck platform, which is a combination of artificial intelligence and other forms of technology, certainly, $300 million of run rate EBITDAs is significant. — Jim Fish, Chief Executive Officer (Q&A)

> more than $300 million of annual run rate operating EBITDA through service upgrades, optimized routing, and lower operating costs — prepared remarks, Q2-2026 call

> That technology on the truck I'm speaking of has been around for probably closer to a decade. — John Morris, President — Q1-2026 call, 2026-04-29

> we limited the increase in collection operating costs to less than 1.7% compared to the second quarter of 2025 — John Morris, President

> margin expanded 40 basis points, driven by a strong price to cost spread and continued cost reductions from technology and automation — David Reed, Chief Financial Officer

*Source:* https://www.investing.com/news/transcripts/earnings-call-transcript-waste-management-tops-q2-eps-lifts-margin-outlook-93CH-4821055

**Kill.** WM was cut on 2026-07-21 for failing the AI-attribution and materiality bar; a cut is not re-litigated without NEW evidence that overcomes the recorded cut reason. The $300m figure is new, but Smart Truck is not: Morris disclosed the platform on the pre-cut Q1-2026 call and dated the hardware to "closer to a decade". The figure is therefore an accumulated program total newly given a run-rate label, not a saving delivered since the cut, and it is arithmetically impossible as an incremental item — $300m is 114bp of margin on FY26 revenue guidance against 40bp of actual margin expansion, inside a 140bp gross line the CFO attributes first to price-to-cost spread while core price runs 6.3% and yield 3.9%. Annualised over the platform's life it is roughly $30m, 0.17% of the $18.2bn opex base, three times below the materiality floor. Attribution fails independently: Fish twice refuses the AI framing ("I don't look at it as just AI"), nobody ever sizes the AI share, and one of the three named benefit sources — "service upgrades" — is revenue capture, not opex. The recycling "30% improvement in labor cost per ton" says automation and never says AI; it is a capex benchmark against legacy facilities. Unit cost moved the wrong way: collection opex +1.7% on volumes -0.4% is +2.1% per unit, and the sub-60% opex ratio is compressed by price in the denominator. Technology appears in the CFO's bridge only as a -40bp HEADWIND, exactly cancelling the +40bp net expansion.

**What survives.** WM has a real, decade-matured telematics and imaging estate — every commercial and residential truck outfitted, over 300 million images a year, roughly 95% processed without a human touch — and that is a genuine AI workload at scale. If the company ever decomposes the $300m into an AI-attributable, cost-only figure with a baseline and vintage, WM becomes a live candidate quickly.

**Materiality.** $300m against implied FY26 opex of ~$18.2bn is 1.65% as stated, clearing the 0.5% floor on paper. But it is a stock, not a flow: gross EBITDA blending revenue and cost, no accumulation period disclosed, on a platform roughly ten years old. Annualised incrementally it is ~$30m, 0.17% of opex — below the floor by three times.

**Watch.** Q3 2026 (late Oct): (1) is the $300m decomposed into AI-versus-cameras/telematics/routing and into service-upgrade revenue versus opex reduction; (2) is a baseline and vintage given so an incremental annual delta can be reconciled to the Collection & Disposal segment P&L; (3) does collection operating cost growth print BELOW volume growth, against this quarter's +1.7% cost on -0.4% volume; (4) does technology move from the headwind side of the CFO's bridge to a named, quantified benefit line. A repeat of "$300 million" unchanged with no reconciliation is confirmation of the UPS costing-constant pattern, not corroboration.

**Peer note.** Peer set is decisive and was run: Clean Harbors posted +190bp of adjusted EBITDA margin — a company-record quarter and a $110m guidance raise — with zero AI attribution, and Waste Connections, whose AI disclosure is genuinely rigorous (seven initiatives, named tools, deployment dates, $100m invested), books just $20m of realized run-rate EBITDA today. WM's unitemized $300m is fifteen times WCN's itemized $20m. Republic Services, Casella and GFL had not published Q2-2026 transcripts in the window.

---

## Run 2026-07-30 — material changes

**No additions. No promotions. No demotions. No score moves.** Standing unchanged at 21 realized · 25 plan · 23 cut · 276 outside.

**WM — reopen request DENIED, cut of 2026-07-21 stands (new near-miss).** The Q2-2026 call produced the run's only cut-name reopen candidate: Jim Fish, CEO — *"our Smart Truck platform, which is a combination of artificial intelligence and other forms of technology, certainly, $300 million of run rate EBITDAs is significant."* The figure is new; the platform is not. John Morris dated the truck hardware to *"closer to a decade"* on the pre-cut Q1-2026 call, so the $300m is an accumulated program total newly given a run-rate label — roughly $30m a year, 0.17% of the $18.2bn opex base, three times below the materiality floor. It is arithmetically impossible as an incremental item: $300m is 114bp of margin against 40bp of actual expansion, and the CFO's bridge names price-to-cost spread first and puts technology on the *headwind* side at −40bp. Fish twice refuses the AI framing. Collection unit cost rose 2.1%. Peer set decisive: Clean Harbors +190bp and a record margin with no AI story at all; Waste Connections, with genuinely rigorous AI disclosure, books $20m realized against WM's unitemized $300m.

**CHRW — demotion review OPENED, score HELD at 87, `pending_deep_review` set.** The adversarial pass made a serious case for cutting the anchor to ~35 and demoting realized → plan: the productivity metric definition was withdrawn this quarter (prior calls named *shipments per person per day*; the Q2 8-K says only "productivity" and merges the previously separate NAST and Global Forwarding series into one ">60%" floor), operating expenses **rose** $4.9m YoY so 112% of the operating-income gain came from adjusted gross profit, personnel cost per employee rose 13.2% on headcount down 10.8%, $26.8m of H1 severance is co-mingled with the AI headcount story, and CHRW's own disclosure of truckload rate per mile +25.5% points to rate inflation. **Held** because the peer-set check — the runbook's single most decisive test, mandatory every run — could not be run once the session WebSearch budget was exhausted, and no full Q2 transcript was obtainable. A 52-point cut to the calibration anchor of the entire scale will not be taken on an incomplete Tier 2. First in the queue next run.

**CHRW evidence correction.** The claim that the Lean AI Engineer *"can assess a supply chain in 25 to 30 minutes, compared with assessments that can take up to four weeks"* originates in a BusinessWire product-launch release dated 2026-05-20, **not** an earnings call, and is struck from the earnings-call evidence set. The "more than 450 in-house engineers and data scientists" figure has been unchanged for four quarters and is a static input metric, not evidence.

**PFSI — held at 63.** Genuinely new quantified framework (150 mapped origination tasks, 25% automated, 80% by YE2027, 40–80% cycle-time reduction), but the score move was killed: Spector attributes the $60m to *"rates being higher"* and a smaller market, with AI credited only for making the cut safe (*"while preserving operational capacity"*); CFO Perotti's entire expense bridge names volume and capacity and never AI; the 25% is an unweighted count of self-defined task types Spector concedes is *"low-hanging fruit"*; production expenses rose 35% YoY across five consecutive quarters. Realized AI-attributed saving this quarter: **$0**. No mortgage peer had reported Q2, so there is no control group.

**SPGI — held at 60.** Goalpost check passes cleanly (end-2027 deadline unchanged since Q4-2025), but attribution is blended ("AI-driven efficiencies **and other** productivity initiatives"), $100m is ~1.3% of company expenses, and Cheung's margin bridge credits "disciplined expense management" with no AI. Third consecutive run with no speaker-attributed primary source. Q3 trigger recorded: if "nearly 60%" has not advanced, that becomes the demotion trigger this quarter was not.

**Disclosure-attrition flags: HOOD (realized/70), AON (plan/50), OPCH (plan/47)** — all three reported and quantified nothing. None is a demotion yet; a second consecutive absent quarter makes each one.

**Closest outside names, all rejected:** GWO (Empower CEO ties AI and straight-through processing to *"driving our unit cost lower"* — no figure), FTV (Gordian Flash AI, *"days to minutes"*, unquantified and customer-facing), THG (named tool Triage Pro, zero quantification), MC (Moelis discussed AI at length; the CFO expressly declined to quantify it).

**MORN flagged structural** — Morningstar holds no earnings conference call and can never yield a transcript-based verdict. Removed from the transcript requeue.

---

## Run 2026-07-31 — material changes

**No additions. No promotions. No demotions. No score moves.** Standing unchanged at 21 realized · 25 plan · 23 cut · 276 outside. Three new near-misses take the near-miss page to nine.

**Calibration passed exactly.** The three frozen 2026-07-21 snapshots, re-scored blind, returned **87 / 53 / 38** against expected 87 / 53 / 38 — zero deviation on all three anchors. Score decisions were therefore permitted this run, and the fact that none were taken is a judgement about the evidence, not a rubric block.

### The three Tier 1 PASSes from outside the database — all rejected

**AJG — Arthur J. Gallagher, rejected at 25.** Doug Howell, CFO, answering Evercore's David Motemaden: *"That math would produce 600 basis points of margin expansion"* — on a framework of 5% production-layer / 10-15% support / 20-30% back-office savings, which he then haircut himself to *"maybe there's 400 basis points there"* over *"three to five years."* The word "maybe" appears four times inside the framework's construction. Zero AI dollars are quantified for the quarter. Management's own margin bridge excludes AI entirely — Howell credits *"productivity and quality efforts"* for 50bps of underlying expansion, and FY26 guidance was reaffirmed unchanged at 40-60bps. Peer set decisive: AON expanded adjusted operating margin 70bps in the same quarter and attributed roughly 60bps of it to a named, dollarised, **non-AI** restructuring programme ($25m in the quarter, $100m in 2026 toward $450m by 2027), while MMC runs a $400m "Thrive" programme whose stated levers include right-shoring. Gallagher's 50bps is at or below what its two largest peers delivered with no AI attribution at all — below what one peer achieved through severance alone.

**ICLR — ICON plc, rejected at 22, and a lesson in ellipsis.** The thin screen recorded *"SmartDraft will now have a Claude back end... taking 30% out of the time of negotiating clinical trial contracts."* The deleted words were **"that helps us build on the progress we've already made"** — and they invert the sentence. The 30% belongs to the pre-Claude, rules-based SmartDraft; the Claude back end arrives prospectively. The ICON–Anthropic collaboration was announced 2026-07-28, one day before the call, entirely in future tense, and does not mention SmartDraft at all. The number has no baseline, no scope and no dollar value, and appears in no company IR document — spoken remarks only. The beneficiary is unresolved: site-contract negotiation is billable study start-up work performed for sponsors, and management never said whether the saving is retained or passed through. CFO Nigel Clerkin's bridge credits pass-through mix, cost actions and resourcing, with AI absent from every driver, and $20.9m of Q2 restructuring for *"elimination of redundant positions"* independently explains the cost actions. Peer set: IQVIA booked $63m of restructuring in the same quarter with no AI label, and Medpace turned 17.2% revenue growth into a 90bp SG&A-ratio improvement with no AI and no restructuring at all. The cost actions are the CRO downturn's sector-wide reflex.

**MKL — Markel Group, rejected outright at 18 — the best AI deployment story of the run, and unscoreable.** Simon Wilson, CEO of Markel Insurance: *"the reduction in time to have an initial risk assessment in front of an underwriter has fallen by between 50%-90%."* Named vendors (Harvey AI, Bain, Cytura), a named new unit (Cortex), a dated capital vehicle (February AI accelerator fund, nine ideas into production in a single month), six classes rewired over *"$500 million of existing GWP."* The technology is not in doubt. Two independent kills are. First, Wilson monetizes the metric as **revenue** in the same breath — *"The result is higher levels of better quality business, with the WI portfolio in London growing by 50%"* — underwriters are redeployed, not removed, and AI-as-revenue is logged, never scored. Second, Markel **discloses no expense ratio at all**, in the release or on either call; the CFO offers only the adjective *"a slightly lower expense ratio."* There is no financial series in which an AI-driven expense benefit could ever be observed. The combined ratio of 93% vs 97% is reserve development and cats, and $500m of GWP is a premium denominator, not an expense one. W.R. Berkley improved its combined ratio 160bps in the same quarter with its expense ratio dead flat at 28.5%.

*Speaker-attribution note for the record:* the investing.com transcript renders Wilson first-name-only under the label "Head of Insurance Operations." That is the vendor's label, not his corporate title, confirmed against markel.com. It must not be published as his title.

### XPO — the highest-value finding of the run

**XPO (realized/71) is the first admitted realized name in this database to quietly drop the AI credit from its flagship metric on the call.** Q1-2026 paired the quantified productivity gain with *"proprietary tools that use AI to improve planning, optimize trade flows and enhance day-to-day execution."* Q2-2026 credits the identical metric to *"workforce planning technology"* — Mario Harik, Chairman & CEO: *"In the second quarter, we used our workforce planning technology to improve productivity by nearly 2.5 points versus last year."* AI appears nowhere in that sentence.

The mitigant matters: the Q2 earnings **release** does retain the credit (*"implementing new AI capabilities across the network"*), so this is script relocation rather than corporate withdrawal — but a press release is not an earnings call and is not primary evidence. There *is* a new AI number this quarter, and it is properly attributed — Harik on the trailer-loading application: *"at the pilot sites, load quality improved by more than 40%, while damages were reduced by 50%"* — but it is pilot-scoped and denominated in quality units, not cost. The banked series also decelerated (4% in Q1 to 2.5 points in Q2) and its unit has drifted again across points, hours-per-shipment and percent, with the denominator never defined on any call.

**Score held at 71. Attribution-drift watch opened.** Trigger: if the Q3-2026 call again carries the productivity number without an on-call AI attribution, that is two consecutive quarters of dropped credit and XPO goes to demotion review with a target range of 55-60. No future raise until management defines the productivity denominator once.

### CHRW — the peer test finally ran, and it exonerates the name

The mandatory peer-set check that the 2026-07-30 run could not complete was run today against Landstar, RXO, Expeditors and Forward Air. **Result: SURVIVES.** The premise of the proposed demotion — that CHRW's gain is a cycle-and-cost-discipline gain wearing an AI label — is refuted by the control group. The 2026 freight market is a rate **upcycle**, not a recession, and it moved peer broker margins the *wrong* way: Landstar revenue +18.2% on loads +1.9% with revenue per load +17.0%, operating margin **flat** at 4.6% vs 4.6% and SG&A +22.4%, with CFO Jim Todd citing *"a 129 basis point compression in our brokerage net revenue margin"*; RXO's brokerage gross margin fell 50bp sequentially on truckload volume −12%; Expeditors **added** FTEs +6.0% with salaries +9.1% while expanding margin 63bp; Forward Air's adjusted EBITDA rose 1.4% with zero AI mentions in the transcript. A cycle that compressed or reversed the delta at four peers cannot explain CHRW expanding NAST operating margin from 34.3% to ~39%. The test does corroborate one lesser charge: rate inflation is market-wide (Landstar revenue per load +17.0%), so the portion of operating-income gain riding on adjusted gross profit is partly cyclical.

**A fallback markdown of 87 → 72 was then proposed and denied.** The −15 maps correctly onto the rubric's *"metric definitions that shift quarter to quarter"* — it is a principled number, not a split-the-difference. But its **predicate is unproven**: the charge that *shipments per person per day* was withdrawn rests on the metric's absence from an 8-K, and absence from a press release is not evidence of withdrawal when the venue in which it has always been disclosed — the call — has never been read. The Q2-2026 transcript has now been unobtainable from any permitted source for a **third consecutive run**. Moving the calibration anchor of the entire scale on an unread primary source, in an append-only log, buys one run's impatience at the price of a documented error. Precedent from the last two runs is unanimous the other way: SPGI held, BRO's drafted cut destroyed on adversarial review, WM's reopen denied.

**Conditional trigger recorded.** When the transcript is obtained: (a) if management does not restate a per-person-per-day productivity metric on the call, apply the −15 immediately, **87 → 72**; (b) if it additionally fails to attribute any quantified opex reduction to named AI tooling, **realized → plan** follows with a further markdown; (c) if the metric is restated intact, close the review at 87 and log the 8-K's financial deterioration (personnel cost per employee +13.2%, opex +$4.9m YoY, $26.8m H1 severance) as a standing Q3 watch item. Score held at 87, status held at realized, `pending_deep_review` retained, `last_scanned` not advanced, first in the queue.

### The two admitted names that asked for a move and did not get one

**ADT (plan/54) — promotion to realized denied.** Jim DeVries, Chairman/President/CEO, with correct attribution ordering: *"we handled nearly 20% fewer customer contacts through human agents and reduced service tickets by a similar amount."* ADT's first quantified AI operational metric. But it has no denominator and no baseline — not stated per subscriber, per period, or against a stated contact base — so it cannot be re-tested next quarter; gross subscriber additions fell 22% in the quarter, which mechanically reduces contact volume independent of any AI deflection (the same confound that killed FAF); and every relevant financial line moved the wrong way — SG&A $386m vs $356m (+8%) on revenue +2%, i.e. 29.4% of revenue vs 27.7%, operating income −8%, adjusted EBITDA margin −100bp. The company's own release names *"higher selling, general, and administrative expenses"* as a driver of the income decline, with AI nowhere in the bridge. Promotion trigger for Q3: deflection restated per-subscriber with a baseline, **and** SG&A/revenue inflecting below 27.7%, **and** AI in the margin bridge. A second quarter of a rising SG&A ratio alongside AI claims opens a demotion review.

**WTW (plan/54) — score move 54 → 62 proposed and denied.** This was the closest call of the run. Propel is genuinely new and substantial: ~$400m run-rate savings on ~$625m investment (1.6x cost-to-achieve), ~30% adjusted operating margin in 2028, named platforms (Neuron, Willis Navigator, Violet), a baselined productivity metric corroborated by two named executives — Carl Hess, CEO: *"Schedules of insurance that once took four hours are now generated in about five minutes,"* and Lucy Clarke, President Risk & Broking, independently. And CFO Andrew Krasner attached AI to a **realized** number: *"A growing share of this expansion is structural, driven by AI and automation embedded across our operating model,"* against 100bp of adjusted operating margin expansion.

It was denied on four grounds. **Consistency:** that is the same blended attribution that failed SPGI on this same run, and weaker — SPGI at least dates and dollarises its blend, whereas *"a growing share"* of 100bp is anywhere between 1bp and 99bp, and Krasner's own predicate is *"strong operating discipline and expense management,"* with AI entering in the following sentence. **The refusal:** Elyse Greenspan (Wells Fargo) asked directly to break it down in dollars and Krasner answered with categories instead — and two of his three named $400m levers, lower third-party spend and retiring duplicative and legacy technology, are not AI. **The disclaimer:** *"the capacity these tools free up is being reinvested into higher value client-facing work and growth"* — the GSHD and AXP kill, realized AI-attributed saving $0. **The peer set:** AON cut compensation and benefits to $2,271m from $2,360m, −3.8% in absolute dollars on revenue +2.2%, producing 331bp of labour-ratio leverage — 2.8x WTW's ~120bp — with no AI attribution at all, and AON's GAAP operating margin rose 80bp in the quarter WTW's *fell* 150bp to 14.8% on transaction and integration expense of $61m vs $2m. Broker comp ratios in Q2-2026 dispersed from +331bp (AON) to −230bp (AJG) with no relationship to AI disclosure.

*One charge against WTW was itself rejected on the adversarial pass, and the record should show it:* the Newfront-confound objection does not hold. Acquisitions were ~3% of the 9% reported growth (~$68m), which moves a $2.47bn revenue base by 15-20bp, not 120bp. WTW's labour leverage is probably real. It simply does not belong to AI.

Held at 54. Triggers: if Q3 still puts no dollar or percentage on the AI share of the $400m, apply the promotional-tone penalty and consider 54 → high-40s; the ~30% 2028 margin and the $400m/$625m figures are now on the record and get a goalpost check every quarter; and if the *"AI and automation"* pairing persists without ever being decomposed, cap WTW below 70 permanently — a blend that never separates is an AI-washing tell.

### Cut names, and the rest

**COIN, LH and LPLA quick-checked; all fail, all stay cut.** Nothing overcomes the recorded cut reasons. LPLA is the only one worth a Q3 re-check: LPL now has a named agent ("Cyan") in production and Matthew Audette, President & CFO, describes straight-through behaviour — *"can just be completely processed through by that agent"* — with zero quantification. A quantified STP rate or cost-per-transaction disclosure would be a genuine trigger. Richard Steinmeier's *"nearly $2 billion over the last few years"* is input spend bundled across four categories, not an efficiency outcome. **CI** could not be sourced and is requeued rather than treated as settled.

**Closest outside names among the FAILs, all rejected:** ICE (Benjamin Jackson, President, on *"a voice assistant resolving common inbound calls before they reach a person taking cost out of the call center"* — an unusually specific mechanism with no number anywhere; the highest-probability future PASS in the batch), H — Hyatt (a large-scale AI platform for scoring group business, but the one hard number, PMS cost to owners −40%, belongs to a platform migration, not to AI), WCC (CFO Indraneel Dev ties AI to compressing the working-capital cycle — right category, zero quantification), PIPR (AI discussed adjacent to non-comp expense with no causal link), SCI (AI-driven sales training at scale, unquantified). **TEM — Tempus AI** is a clean confirmation of the AI-vendor exclusion rule: it produced the batch's only quantified AI figures and every one of them was product revenue.

**Sourcing is now a structural problem, not a one-off.** 22 of 48 names could not be advanced, and only three are genuine timing. The rest failed on sourcing: MarketScreener paywalled, Seeking Alpha barred by rule, several Motley Fool URLs stale or 404, and WebFetch's provenance gate blocking any URL not surfaced by a search result. None of the 22 was stamped `last_scanned`; all retry tomorrow. Tier 0 has now been degraded four consecutive runs — finnhub.io is not reachable by any permitted route from this environment, and the calendar substitute of the day determines coverage. That is worth fixing before it silently narrows the universe.
