# ATP Tennis Chat

Ask the tennis database in plain language.

This project is meant to become a public natural-language interface for ATP tennis data. The idea is that anyone should be able to clone the repo, ask a question in normal language, and get an answer based on live tennis data.

If you do not use Git, the intended flow is to download the project as a ZIP from GitHub, unzip it, and open the folder in your AI coding tool.

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

This repo does not assume direct database access.

Instead, it talks to the tennis service over HTTP:

- `https://tennis.egelberg.se/api/meta/endpoints`
- `https://tennis.egelberg.se/api/meta/schema.sql`
- `https://tennis.egelberg.se/api/query`

Core rules:

- `GET /api/meta/endpoints` is the live source of truth for available endpoints.
- `GET /api/meta/schema.sql` is the live source of truth for SQL/schema context.
- `POST /api/query` is read-only and is used for database reads.

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

### 3. Open the project in Codex

- Open Codex
- Choose to open a local folder or project
- Select the unzipped `atp-tennis-chat` folder
- Codex will read [AGENTS.md](/Users/magnus/Documents/GitHub/atp-tennis-chat/AGENTS.md)
- [AGENTS.md](/Users/magnus/Documents/GitHub/atp-tennis-chat/AGENTS.md) points Codex to [CONTEXT.md](/Users/magnus/Documents/GitHub/atp-tennis-chat/CONTEXT.md)

### 4. Start with a simple first prompt

Example prompts:

- `What can this project do?`
- `Use the tennis service and show tomorrow's matches`
- `Which players have a winning record against Borg?`
- `Answer using live data from tennis.egelberg.se`

Codex-specific files in this repo:

- [AGENTS.md](/Users/magnus/Documents/GitHub/atp-tennis-chat/AGENTS.md)
- [CONTEXT.md](/Users/magnus/Documents/GitHub/atp-tennis-chat/CONTEXT.md)

OpenAI documents Codex project instructions through `AGENTS.md`: [Introducing Codex](https://openai.com/index/introducing-codex/)

## First-Time Setup With Claude Code

If you are completely new to Claude Code, use this flow.

### 1. Get access to Claude Code

- Make sure you have access to Claude Code through Anthropic
- Install Claude Code if needed
- Sign in when prompted

### 2. Download the project

If you do not use Git:

- Click [Download this project as a ZIP](https://github.com/meg768/atp-tennis-chat/archive/refs/heads/main.zip)
- Unzip the file on your computer

If you do use Git:

- clone the repository normally

### 3. Open the project in Claude Code

- Open Claude Code
- Choose to open a local folder or project
- Select the unzipped `atp-tennis-chat` folder
- Claude Code will load [CLAUDE.md](/Users/magnus/Documents/GitHub/atp-tennis-chat/CLAUDE.md)
- [CLAUDE.md](/Users/magnus/Documents/GitHub/atp-tennis-chat/CLAUDE.md) points to [CONTEXT.md](/Users/magnus/Documents/GitHub/atp-tennis-chat/CONTEXT.md)

### 4. Start with a simple first prompt

Example prompts:

- `What data source should you use in this project?`
- `Show me which players have beaten Bjorn Borg`
- `Use the schema and answer in table form`
- `What endpoints are available right now?`

Claude-specific files in this repo:

- [CLAUDE.md](/Users/magnus/Documents/GitHub/atp-tennis-chat/CLAUDE.md)
- [CONTEXT.md](/Users/magnus/Documents/GitHub/atp-tennis-chat/CONTEXT.md)

Anthropic documents Claude Code project memory through `CLAUDE.md`: [Manage Claude's memory](https://docs.anthropic.com/en/docs/claude-code/memory)

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
- [CLAUDE.md](/Users/magnus/Documents/GitHub/atp-tennis-chat/CLAUDE.md) for Claude Code

## Current State

Right now this repo is intentionally lightweight.

It does not yet contain a finished end-user app. Today it mainly serves as:

- the shell around the natural-language querying workflow
- the durable instruction layer for the project
- the place where the project direction is captured

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
