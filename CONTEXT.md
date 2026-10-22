# Project Context

## Purpose
- Use this file as persistent project context for the `atp-tennis-chat` workspace.
- Prefer short, durable facts over long conversation logs.

## Working Agreement
- Treat `CONTEXT.md` as the place to save important project context between turns.
- If the user says "save everything", summarize the durable context here rather than storing raw chat transcripts.

## Data Access
- 2026-10-19: Magnus wants direct MariaDB access as the default for tennis data because it is faster; this supersedes the previous HTTP-first instruction. Use `scripts/database.py` and the project-local ignored `.env`; never expose credentials. HTTP endpoints remain an available fallback. This preference authorizes reads, not unsolicited data/schema changes.
- Tennis Abstract is also an allowed supplementary source for tennis research and matchup context when useful.

## ATP Service Endpoint Map
- Assume `tennis.egelberg.se` is the main HTTP entrypoint for these routes unless the user says otherwise.
- `GET /api/meta/endpoints` is a machine-readable endpoint catalog and should be preferred when I need to confirm current service routes/response shapes.
- `GET /api/meta/schema.sql` exposes the raw schema SQL file and can be used when I need up-to-date SQL documentation over HTTP.
- `POST /api/query` is read-only and intended for SQL reads only.

## Analysis and Presentation — latest agreement 2026-10-19
- Magnus explicitly reset the earlier detailed format instructions: he asks the question; Codex independently chooses the analysis and presentation. Do not turn every reaction into a new rule or impose a fixed card template. This supersedes earlier rigid preferences about headings, fonts, image dimensions and mandatory sections.
- Aim for compact, informative, readable results with substantive analysis and creative observations. Images, tables, charts or prose are all appropriate; use the space the content needs. Avoid all-caps headings (normal abbreviations ATP/GS are fine).
- Magnus particularly praised the independent top-20 form analysis (`analysis/ATP-20261019-04/topp20-form.png`) and the Shimabukuro–Safiullin analysis (`analysis/ATP-20261019-07/shimabukuro-safiullin-analys.png`). These are examples of good judgment, not compulsory templates.
- Database first. Proactively use external research when useful, clearly marking external facts and sources in the result/image. Distinguish facts, subjective judgments and model outputs.
- Keep selection criteria consistent for comparable questions. A curated watchlist is not the same as a systematic ranking; explain substantive changes to the population or sorting.
- For reproducibility, include sufficient source/date, filters, calculation and ordering information for a screenshot to convey the method. Save SQL/raw results when useful. An analysis ID alone is only a local reference, not a public link or a guarantee that a screenshot can reproduce original data. Prefer “Källa och urvalsregler” over promising exact recreation; updated data can change results.
- 2026-10-21: Magnus praised the creative freedom and the tennis poster (`analysis/ATP-20261020-01/spelval-21-oktober-affisch-med-marginal.png`). Continue choosing analysis and presentation independently; this is a successful example, not a mandatory poster format.

## Odds Comparison — clarified 2026-10-21
- Use the finished TA and GPT odds from `PLAYER_ODDS` directly when comparing with Svenska Spel. Magnus means to include the existing 5 percent pricing markup, not to match Svenska Spel's exact per-match overround. Do not add a second markup or replace the standard pricing with per-match margin adjustments unless explicitly requested.
- Verified directly in MariaDB: `PLAYER_ODDS` multiplies each model probability by 1.05, clamps it to 0.001–0.999, takes its reciprocal, and rounds to two decimals. Both TA and GPT outputs already include this pricing. `WIN_PROBABILITY_TA` returns the underlying probability without a margin.
- Label displayed TA/GPT odds as including the 5 percent markup. Svenska Spel's actual overround may differ; direct price comparison does not imply identical internal bookmaker pricing.
- An odds-price gap `(Svenska Spel odds / model odds - 1) × 100` is not expected return. Expected return requires the underlying margin-free model probability: `(probability × Svenska Spel odds - 1) × 100`, conditional on that probability being accurate. Preserve source, odds-snapshot date, surface and relevant model limitations in analysis artifacts.

## Context Scope — clarified 2026-10-19
- When Magnus asks to save context, prioritize the overall conversation: goals, collaboration style, data-source priorities and durable decisions. Do not preserve each match, transient odds, individual betting decisions or a detailed handoff unless explicitly requested. Analysis files already retain the underlying work.
- Magnus wants Codex to investigate independently and explain what the data means, including when a simple statistic or model output is misleading. Avoid turning conversational feedback into an expanding rulebook.

## Ranking Comparison Method — 2026-10-19
- The database has match-time rankings and current player-profile ranking, but no separate weekly ranking-history table. For year-over-year comparisons, latest positive match ranking at an event start on/before the historical cutoff is only an estimate of the ranking at that cutoff.
- Expose historical observation dates and stale observations when relevant. Current profile ranking is the value at extraction, not a separately verified weekly list. Missing match rankings can affect ordering.
- For the approved young-climbers example, used under 23 and current top 100, displayed the ten largest positive rank changes, and added context about the youngest players. These were analysis-specific choices, not permanent default thresholds.
- Saved query/results for that example are under `/Users/magnus/Documents/GitHub/codex-chat/sandbox/young-ranking/`. A set-based union of winner/loser observations with ROW_NUMBER per player returned quickly; repeated PLAYER_RANK_AT_DATE calls over the candidate list were much slower in this session.

## Verified Tennis Context
- Match discussed: Daniel Altmaier (GER, rank 52) vs Fabian Marozsan (HUN, rank 47)
- Surface used for the calculation: clay
- Computed model odds:
  - Altmaier: 2.32
  - Marozsan: 1.61
- Screenshot bookmaker odds shown in chat:
  - Altmaier: 2.88
  - Marozsan: 1.42
- Implied value from that comparison:
  - Altmaier: about +8.4%
  - Marozsan: about -8.3%
- Model conclusion from that snapshot: value on Altmaier
- Head-to-head on clay at the time checked: 0-0


## Notes
- Earlier UI discussion referred to a "Kommande matcher" table with a player row showing flags, names, `[0-0]`, and a play icon.
- No source code for that UI exists in this workspace right now, so future UI fixes require the actual app files to be added first.
- For all graphs in this project, prefer `Recharts` over Mermaid or ad hoc SVG unless there is a strong reason not to. A sample component lives in `examples/RankingGapChart.jsx`.
- Preferred graph style for historical comparisons: stacked yearly bar charts with a legend inside the chart area. This format worked well for explaining ATP ranking gaps to non-technical readers.
- Historical Davis Cup coverage in `tennis.egelberg.se` appears incomplete for some older ties. Example: Bjorn Borg's 1978 Davis Cup singles results are missing at least `Borg vs Sean Sorensen`, `Borg vs Manuel Orantes`, and `Borg vs Jose Higueras`, which can undercount winning-streak calculations by 3+ matches.
- After the later data re-import checked on 2026-05-04, Bjorn Borg's Davis Cup rows were expanded enough to change the no-status winning-streak results. With pure win/loss logic (`winner`/`loser` only, ignoring `match.status`), Borg's streaks over 30 wins are 31 (1977), 35 (1978), 31 (1979), and 41 (1979-1980).
- For historical Borg match exports, do not rely on score text alone to infer the result. The safer presentation is separate `Outcome`, `Score`, and `Status` columns because the database stores scores from the winner's perspective and also includes `Aborted` and `Walkover` rows.
- Live check against all 2026 matches on 2026-05-04: for every `Completed` match with a non-empty score, the `score` field matches winner-first orientation. One `Completed` row (`2026-02-01 Santo Domingo Este RR: Duarte Vale vs Enmanuel Munoz`) has an empty score. `Aborted` rows are not reliable for winner-first inference because the official winner can be tied or trailing when the opponent retires/defaults.
- Older historical data includes malformed score tokens that look like importer/formatting bugs rather than real scoring formats. Verified examples around 1968 include `1-08`, `1-19`, `1-06`, `1-05`, and `1-0`, which strongly resemble corrupted two-digit winner scores such as `10-8`, `11-9`, `10-6`, `10-5`, and `10-0`. Treat these tokens as data-quality issues and avoid literal score-based inference without cleanup.
- For consecutive-set streaks by surface, the closest database-to-Wikipedia comparison so far is to exclude `Challenger` and `Rod Laver Cup` events and derive set winners from the score itself instead of assuming scores are always stored from the winner's perspective.
- Under that rule, the clay and grass leaderboards align well with Wikipedia/UTS, but hard-court streaks still look inflated by historical surface classification. Example: `1975 Stockholm Open` is stored as `Hard` in the database, while public historical sources describe it as `Carpet`.
- Top-10 career checks (2026-10-13): use opponent match-time `winner_rank`/`loser_rank` between 1 and 10, include Completed/Aborted and exclude Walkover; make event scope explicit. Missing opponent rankings are substantial (e.g. Becker 94, Sampras 93, Federer 67, Djokovic 56 in the non-Challenger/non-Laver played-match scope), so raw aggregates cannot establish complete career totals. Reproducible comparison and coverage results are saved in `analysis/top10-verification/`. Players table currently lists 29 former No. 1s; Sinner is included, Zverev highest_rank=2 and Draper highest_rank=4.
- Davis Cup top-10 audit (2026-10-13): Borg has 40 Completed/Aborted Davis Cup singles rows, but all 40 lack opponent ranking; therefore none enters the top-10 aggregate despite all event types being allowed. Former No. 1 Davis Cup coverage is saved in `analysis/top10-verification/davis-cup-coverage.json`. Original image label was `Doper*` referring to Sinner, not Draper; earlier identification as Draper was corrected.
- Installed `PLAYER_RANK_AT_DATE(player, as_of_date)` on 2026-10-14 using explicitly authorized temporary direct MariaDB access. Source: `sql/PLAYER_RANK_AT_DATE.sql`. Uses latest positive winner_rank/loser_rank observation with event start date <= requested date; all statuses/event types allowed, no future fallback, same-date ties resolved by descending match ID. Returns NULL for absent observations/invalid inputs. Uses PLAYER_LOOKUP, so ambiguous surnames can select another player (e.g. Borg selects Leo Borg); prefer ATP IDs or full names. Connection credentials are not stored in project files. Verified inclusive cutoff and earlier observation behavior, missing player/date/history cases.
