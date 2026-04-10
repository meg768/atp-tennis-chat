# AGENTS

This repository uses [CONTEXT.md](/Users/magnus/Documents/GitHub/atp-tennis-chat/CONTEXT.md) as the project context and source of truth.

Before doing meaningful work in this repo:

1. Read [CONTEXT.md](/Users/magnus/Documents/GitHub/atp-tennis-chat/CONTEXT.md).
2. Treat it as the canonical summary of durable project context and decisions.
3. If new durable context appears, update [CONTEXT.md](/Users/magnus/Documents/GitHub/atp-tennis-chat/CONTEXT.md).

Project-specific notes:

- Primary tennis data source is `https://tennis.egelberg.se`.
- Prefer `GET /api/meta/endpoints` for current endpoint discovery.
- `GET /api/meta/schema.sql` is the live SQL/schema reference.
- `POST /api/query` is read-only.
