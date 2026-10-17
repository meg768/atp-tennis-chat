# Project Context

## Purpose
- Use this file as persistent project context for the `atp-tennis-chat` workspace.
- Prefer short, durable facts over long conversation logs.

## Working Agreement
- Treat `CONTEXT.md` as the place to save important project context between turns.
- If the user says "save everything", summarize the durable context here rather than storing raw chat transcripts.

## Data Access
- When tennis data is needed, fetch it through `tennis.egelberg.se` endpoints instead.
- Tennis Abstract is also an allowed supplementary source for tennis research and matchup context when useful.

## ATP Service Endpoint Map
- Assume `tennis.egelberg.se` is the main HTTP entrypoint for these routes unless the user says otherwise.
- `GET /api/meta/endpoints` is a machine-readable endpoint catalog and should be preferred when I need to confirm current service routes/response shapes.
- `GET /api/meta/schema.sql` exposes the raw schema SQL file and can be used when I need up-to-date SQL documentation over HTTP.
- `POST /api/query` is read-only and intended for SQL reads only.

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
