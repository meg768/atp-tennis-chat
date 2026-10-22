# AGENTS

This repository uses [CONTEXT.md](/Users/magnus/Documents/GitHub/atp-tennis-chat/CONTEXT.md) as the project context and source of truth.

Before doing meaningful work in this repo:

1. Read [CONTEXT.md](/Users/magnus/Documents/GitHub/atp-tennis-chat/CONTEXT.md).
2. Treat it as the canonical summary of durable project context and decisions.
3. Update `CONTEXT.md` only when Magnus explicitly asks to save context or update it.

Project-specific notes:

- Use only the shared `atp-tennis` skill at `~/.agents/skills/atp-tennis` for
  database access and current Svenska Spel odds. Read its `SKILL.md` and relevant
  references. Run its database and odds scripts with the skill's Python.
- The shared skill's MariaDB tool is read-only. Schema documentation and TA
  pricing rules live in the skill; do not duplicate connection code here.
- Fetch Svenska Spel through the skill's direct HTTP script, without a browser.
  Report connection failures rather than opening a browser as fallback.
- Do not use `tennis.egelberg.se`, including HTTP query/schema/odds endpoints,
  as a proxy, or as a fallback. Historical source labels remain provenance only.
- These access instructions supersede older access and endpoint instructions
  in `CONTEXT.md` and historical reports. Keep saved results and analyses intact.
- Use the project's own Python environment only for project-specific tools
  such as Pillow rendering; it does not contain a database connection.
