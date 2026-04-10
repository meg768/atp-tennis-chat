# Project Context

## Purpose
- Use this file as persistent project context for the `atp-tennis-chat` workspace.
- Prefer short, durable facts over long conversation logs.

## Current Workspace State
- Workspace path: `/Users/magnus/Documents/GitHub/atp-tennis-chat`
- As of 2026-04-03, the repo is effectively empty except for `.gitignore` and this file.
- Start from scratch unless new files are added later.

## Working Agreement
- Treat `CONTEXT.md` as the place to save important project context between turns.
- If the user says "save everything", summarize the durable context here rather than storing raw chat transcripts.

## Data Access
- As of 2026-04-07, the MCP/database bridge to the tennis database has been removed.
- Do not assume MCP access to tennis data anymore.
- When tennis data is needed, fetch it through `tennis.egelberg.se` endpoints instead.
- The sibling repo `../atp-tennis` may still be useful for local code and endpoint context, but database reads should be treated as HTTP/API-driven unless the user says otherwise.
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
