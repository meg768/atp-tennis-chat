# Project Memory

## Purpose
- Use this file as persistent project memory for the `atp-tennis-chat` workspace.
- Prefer short, durable facts over long conversation logs.

## Current Workspace State
- Workspace path: `/Users/magnus/Documents/GitHub/atp-tennis-chat`
- As of 2026-04-03, the repo is effectively empty except for `.gitignore` and this file.
- Start from scratch unless new files are added later.

## Working Agreement
- Treat `CODEX.md` as the place to save important project context between turns.
- If the user says "save everything", summarize the durable context here rather than storing raw chat transcripts.

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

## PLAYER_WIN_FACTOR
- A new standalone MariaDB function `PLAYER_WIN_FACTOR(playerID, opponentID, surface)` now exists in the tennis database.
- This function is intentionally separate from the older `PLAYER_*_FACTOR` helpers.
- Surface behavior:
  - `Hard` -> `elo_rank_hard`
  - `Clay` -> `elo_rank_clay`
  - `Grass` -> `elo_rank_grass`
  - fallback -> `elo_rank`
- v1 model:
  - `gap = elo_player - elo_opponent`
  - `win_probability = 1 / (1 + POW(10, -gap / 400))`
- v2 model:
- Current section model:
- Current factor model:
  - Elo = 55%
  - Ranking = 20%
  - Head To Head = 10%
  - Form = 15%
  - active factors are renormalized to 100% when a factor is excluded
- Ranking factor:
  - uses current ATP ranks from the `players` table
  - lower ranking number is better
  - raw gap is based on:
    - `rank_score = LN(rank_opponent) - LN(rank_player)`
    - `rank_factor = 1 / (1 + EXP(-rank_score))`
    - `rank_edge = (rank_factor - 0.5) * 2`
    - `rank_raw_gap = rank_edge * 100`
  - excluded if either player has missing or non-positive rank
- Head To Head section:
  - sample = completed matches in the last 2 years
  - if a surface is provided, only that surface is used
  - smoothing = `(wins_player + 1) / (matches + 2)`
  - raw gap = `((h2h_factor - 0.5) * 2) * 100`
  - excluded entirely if there are no qualifying H2H matches
- Form section:
  - sample = completed matches in the last 8 weeks
  - all surfaces are used
  - recency weight = `POW(0.5, days_ago / (8 * 7))`
  - smoothing = `(weighted_wins + 4) / (weighted_matches + 8)`
  - raw gap = `(form_factor_player - form_factor_opponent) * 100`
  - excluded entirely if neither player has any qualifying recent matches
- Verified example from the Elo-only version:
  - `PLAYER_WIN_FACTOR('AE14', 'M0CI', 'Clay') = 0.3760`
  - `PLAYER_WIN_FACTOR('M0CI', 'AE14', 'Clay') = 0.6240`
- Verified example from the current section model:
  - `PLAYER_WIN_FACTOR('S0AG', 'A0E2', 'Hard') = 0.5854`
  - `PLAYER_WIN_FACTOR('S0AG', 'A0E2', 'Clay') = 0.4626`
  - `PLAYER_WIN_FACTOR('S0AG', 'A0E2', NULL) = 0.5509`
  - `PLAYER_WIN_FACTOR('AE14', 'M0CI', 'Clay') = 0.4212`
- Plan forward: evolve this function gradually by adding small Elo-style nudges rather than reusing the old blended factor helpers.

## Sibling Project Integration
- `../atp-tennis/database/functions/PLAYER_WIN_FACTOR.sql` now exists and mirrors the live win-factor model.
- `../atp-tennis/database/procedures/PLAYER_ODDS.sql` now delegates fair probability to `PLAYER_WIN_FACTOR(...)` and then applies the fixed margin.
- `../atp-tennis/README.md` and `../atp-tennis/database/README.md` now describe `PLAYER_WIN_FACTOR(...)` as the main model source of truth.
- The legacy MariaDB functions `PLAYER_ELO_FACTOR`, `PLAYER_FORM_FACTOR`, `PLAYER_HEAD_TO_HEAD_FACTOR`, and `PLAYER_RANK_FACTOR` have been removed from both the sibling repo SQL files and the live database.
- The legacy MariaDB procedure `PLAYER_ODDS_DEBUG` has also been removed from both the sibling repo SQL files and the live database.
- `../atp-tennis/database/schema.sql` was already locally modified before this work, so it was intentionally left untouched.

## Notes
- Earlier UI discussion referred to a "Kommande matcher" table with a player row showing flags, names, `[0-0]`, and a play icon.
- No source code for that UI exists in this workspace right now, so future UI fixes require the actual app files to be added first.
