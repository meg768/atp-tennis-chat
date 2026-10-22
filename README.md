# ATP Tennis Chat

Ask the tennis database in plain language.

This is a Codex project meant to become a public natural-language interface for ATP tennis data. The idea is that anyone should be able to clone the repo, open it in Codex, configure the shared skill, ask a question in normal language, and get an answer based on current database and odds data.

If you do not use Git, the intended flow is to download the project as a ZIP from GitHub, unzip it, and open the folder in Codex.

- [Download this project as a ZIP](https://github.com/meg768/atp-tennis-chat/archive/refs/heads/main.zip)

Examples:

- `Vilka spelare har plusstatistik mot Borg?`
- `Vilken Grand Slam-vinnare har minusstatistik mot lägst antal spelare?`
- `Visa Jannik Sinners längsta matchstreak`
- `Vilka matcher spelas i morgon, med odds och edge?`

## Why This Exists

Tennis databases are powerful, but they are usually only practical if you already know:

- the schema
- the table names
- SQL
- the quirks of the underlying data

This project exists to remove that friction and turn the tennis database into something you can query in ordinary language.

## How It Works

Database access and current Svenska Spel odds come only from the shared
[atp-tennis skill](https://github.com/meg768/atp-tennis-skill), installed at
`~/.agents/skills/atp-tennis`. Read its `SKILL.md` and relevant references for
connection setup, schema, TA calculations, and interpreting odds markets.

The skill connects directly to MariaDB in a read-only transaction and fetches
Svenska Spel's ATP offering through HTTP without opening a browser. If a source
is unavailable, report the failure. Do not create a local connection fallback
or use `tennis.egelberg.se`, including its query, schema, and odds endpoints.
Historical source labels remain provenance, not instructions to reuse them.

This supersedes older connection examples and endpoint preferences in saved
context and reports. The project has no local database connector or `.env`.
Database dependencies and credentials belong to the shared skill.

From this project, use the skill's Python and scripts:

```sh
echo 'SELECT 1 AS connection_ok;' | ~/.agents/skills/atp-tennis/.venv/bin/python ~/.agents/skills/atp-tennis/scripts/database.py
~/.agents/skills/atp-tennis/.venv/bin/python ~/.agents/skills/atp-tennis/scripts/database.py query.sql
~/.agents/skills/atp-tennis/.venv/bin/python ~/.agents/skills/atp-tennis/scripts/svenskaspel.py
```

Project-specific analysis scripts also use the shared connector. For example:

```sh
~/.agents/skills/atp-tennis/.venv/bin/python -m scripts.build_top10_comparison
~/.agents/skills/atp-tennis/.venv/bin/python -m unittest discover -s tests
```

The comparison builder checks historical ranking observations and writes its
analysis cache/results. It does not change database records. Saved analysis
scripts have historical dates and filters; inspect them before rerunning, and
preserve original data when producing a new analysis.

## Image Rendering

Pillow is a project-specific dependency. Keep a separate local environment for
image rendering; this environment does not need database credentials or drivers.

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python -m scripts.render_top10_comparison
```

## First-Time Setup With Codex

If you are completely new to Codex, use this simple flow.

### 1. Get access to Codex

- Make sure you have access to Codex through your OpenAI / ChatGPT setup
- Install the Codex app if needed
- Sign in when prompted

### 2. Download the project

If you do not use Git:

- Click [Download this project as a ZIP](https://github.com/meg768/atp-tennis-chat/archive/refs/heads/main.zip)
- Unzip the file on your computer

If you do use Git:

- clone the repository normally

### 3. Install and configure the shared skill

Install [atp-tennis-skill](https://github.com/meg768/atp-tennis-skill) and link
its repository directory as `~/.agents/skills/atp-tennis`. Follow its `SKILL.md`
to prepare its Python environment and local database settings. Credentials are
provided separately; they are not included in either GitHub repository.

### 4. Open the project in Codex

- Open Codex
- Choose to open a local folder or project
- Select the unzipped `atp-tennis-chat` folder
- Codex will read [AGENTS.md](/Users/magnus/Documents/GitHub/atp-tennis-chat/AGENTS.md)
- [AGENTS.md](/Users/magnus/Documents/GitHub/atp-tennis-chat/AGENTS.md) points Codex to [CONTEXT.md](/Users/magnus/Documents/GitHub/atp-tennis-chat/CONTEXT.md)

### 5. Start with a simple first prompt

Example prompts:

- `What can this project do?`
- `Use atp-tennis and show tomorrow's matches with current Svenska Spel odds`
- `Which players have a winning record against Borg?`
- `Use atp-tennis and show the current top 10 in the database`

Codex-specific files in this repo:

- [AGENTS.md](/Users/magnus/Documents/GitHub/atp-tennis-chat/AGENTS.md)
- [CONTEXT.md](/Users/magnus/Documents/GitHub/atp-tennis-chat/CONTEXT.md)

OpenAI documents Codex project instructions through `AGENTS.md`: [Introducing Codex](https://openai.com/index/introducing-codex/)

## Examples

Questions this project should eventually answer well:

- historical tennis questions
  - `Vilka svenskar har slagit Björn Borg?`
  - `Vilka spelare har plusstatistik mot Borg?`
- ranking and record questions
  - `Vem nådde 300 segrar på minst antal matcher?`
  - `Visa de yngsta spelarna som vunnit alla fyra Grand Slams`
- streak and form questions
  - `Visa spelare med flest set i rad vunna`
  - `Visa Jannik Sinners längsta Masters-streak`
- match and betting questions
  - `Vilka matcher spelas i morgon?`
  - `Visa odds, modellodds och edge`

## Project Memory

This repository uses lightweight instruction files so coding agents can understand the project quickly.

[CONTEXT.md](/Users/magnus/Documents/GitHub/atp-tennis-chat/CONTEXT.md) is the durable project context and source of truth for:

- working rules
- data access assumptions
- saved project context
- important modeling and integration decisions

Supporting files:

- [AGENTS.md](/Users/magnus/Documents/GitHub/atp-tennis-chat/AGENTS.md) for Codex

## Current State

Right now this repo is intentionally lightweight.

It does not yet contain a finished end-user app. Today it mainly serves as:

- the shell around the natural-language querying workflow
- the durable instruction layer for the project
- the place where the project direction is captured

There is also a small chart example in [examples/RankingGapChart.jsx](/Users/magnus/Documents/GitHub/atp-tennis-chat/examples/RankingGapChart.jsx) that shows how to render ATP ranking-gap data with `recharts` and an in-chart legend.

## Roadmap

Likely next steps:

- add a tiny CLI that accepts a plain-language question
- add a small web UI for asking database questions
- standardize answer formatting for tables, assumptions, and caveats
- make the repo easy for others to run without any local database setup

## Goal

The end state is simple:

`Ask the ATP tennis database a question in plain language, and get a useful answer back.`

GitHub repository:

- [meg768/atp-tennis-chat](https://github.com/meg768/atp-tennis-chat)
