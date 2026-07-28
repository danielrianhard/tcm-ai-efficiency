# AI Efficiency Machine — Master State Ledger

**THIS FILE IS THE SINGLE SOURCE OF TRUTH.** Every scan run reads this ledger first and writes its results back here. The Excel database and change memos are renderings of this file — never edit those and expect it to stick; edit here.

- **Universe:** 345 companies (boss-provided Bloomberg screen, "AI adoption .pdf")
- **Baseline:** Phase 1 deep verification completed 2026-07-21
- **Methodology:** see `claude/AI_Efficiency_Methodology.md` (admission criteria, strictness filter, scoring rubric, run procedure)
- **Last run:** (baseline — no automated runs yet)

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
| LSTR | LANDSTAR SYSTEM | Cargo Ground Transportation | 7.2 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
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
| PJT | PJT PARTNERS - A | Investment Banking & Brokerage | 7.0 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
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
| PFG | PRINCIPAL FINL | Life & Health Insurance | 24.5 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
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
| CINF | CINCINNATI FIN | Property & Casualty Insurance | 28.4 | 2026-07-21 | no qualifying evidence (Phase 1 screen) |
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

## RUN LOG (append-only)

One line per scan run: date · names checked (earnings since last scan) · adds/promotions/demotions · memo produced y/n.

- 2026-07-21 — baseline established (Phase 1). No automated runs yet.
