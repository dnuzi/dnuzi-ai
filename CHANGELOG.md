# Changelog

All notable changes to **NiyoX AI** are documented here.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [Unreleased]

### Planned
- Streaming response support
- Conversation export (JSON / Markdown)
- OpenAI-compatible interface shim

---

## [0.0.2] — 2025-05-29

### Added

#### Custom MongoDB support
- `NiyoXStorage` constructor now accepts `mongoUri` and `dbName` options — plug in any MongoDB instance instead of the shared NiyoX cloud database
- `connect(userId?, mongoUri?, dbName?)` accepts override arguments at connect-time for dynamic configuration
- Connections are cached per-URI so multiple `NiyoXStorage` instances pointing at the same database share one `MongoClient`
- `closeAllDb()` helper exported for graceful shutdown of all open connections
- `NiyoXAI` constructor forwards `mongoUri` / `dbName` options through to `NiyoXStorage`
- `enableStorage(userId?, mongoUri?, dbName?)` accepts the same overrides

#### Python SDK (`python/niyox.py`)
- `NiyoXClient` — synchronous HTTP client, mirrors the JS API exactly
- `NiyoXStorage` — optional MongoDB persistence layer (requires `pip install "niyox-ai[mongo]"`)
- `NiyoXAI` — high-level class combining client + storage, with context manager support (`with NiyoXAI() as ai:`)
- `AsyncNiyoXClient` / `AsyncNiyoXAI` — async variants using `aiohttp` (requires `pip install "niyox-ai[async]"`)
- `setup.py` with `[mongo]`, `[async]`, and `[all]` extras
- Zero hard dependencies — stdlib `urllib` only for sync usage

#### React / Vite / Next.js (`react/useNiyoX.js`)
- `useNiyoX(options?)` hook — returns `messages`, `input`, `setInput`, `sendMessage`, `isLoading`, `error`, `newConversation`, `conversationId`
- `<NiyoXChat>` — drop-in styled dark-theme chat component, zero extra dependencies
- `<NiyoXProvider>` + `useNiyoXContext()` — share a single AI session across a React component tree
- Compatible with React 17/18, Create React App, Vite, and Next.js App Router (`"use client"` directive included)
- Importable as `import { useNiyoX } from "niyox/react"` via the new exports map entry

#### CLI (`bin/cli.js`)
- `/mongo <url>` — connect to a custom MongoDB URI directly from the REPL
- `/mongourl <url>` — update the saved URI without reconnecting; persisted across sessions via `conf`
- Custom URI and `useMongo` flag are both saved to local config and restored on next launch
- Banner and help table updated to document the new commands

#### Examples
- `examples/react-cra/App.jsx` — full chat UI using `useNiyoX` for Create React App / Vite
- `examples/nextjs/chat-page.tsx` — Next.js 13+ App Router page with Tailwind styling
- `examples/vite/main.js` — Vite vanilla JS example with no framework

### Changed
- `package.json` version bumped to `0.0.2`
- `exports` map extended with `"./react"` entry
- `files` array extended to include `react/` and `examples/`
- `peerDependencies` added for `react` / `react-dom` (both optional)
- `keywords` extended with `react`, `nextjs`, `vite`, `python`, `mongodb`
- `SECURITY.md` — Known Considerations updated to reflect custom MongoDB URI feature

### Fixed
- Storage connection cache now keyed by both URI and database name, preventing cross-database collisions when two instances share the same URI but different `dbName` values

---

## [0.0.1] — 2024-01-01

### Added
- `NiyoXClient` — core HTTP wrapper around the `ai.dnuz.top` REST API
  - `chat(message)` / `ask(message)` for sending messages
  - In-memory conversation history with `getHistory()`
  - `newConversation()` to reset conversation thread
  - Automatic `conversationId` persistence for multi-turn sessions
- `NiyoXStorage` — optional MongoDB persistence layer
  - `connect()` / `disconnect()`
  - `saveMessage()` / `saveTurn()`
  - `getConversation()` / `listConversations()` / `deleteConversation()`
  - `getStats()` for per-user usage statistics
  - `setPref()` / `getPref()` for persistent user preferences
- `NiyoXAI` — high-level SDK combining client and storage
  - `enableStorage()` opt-in
  - Full delegation to `NiyoXClient` and `NiyoXStorage`
- **CLI** (`bin/cli.js`) with interactive REPL
  - Commands: `/help`, `/new`, `/history`, `/stats`, `/convs`, `/mongo`, `/user`, `/clear`, `/exit`
  - One-shot mode: `niyox "your question"`
  - `--version` / `-v` and `--help` / `-h` flags
  - Markdown rendering with syntax highlighting
  - Coloured boxed responses with response-time display
- **Browser SDK** (`html/index.html`) — zero-dependency chat UI
- **ESM + CJS dual build** (`lib/index.mjs`, `lib/index.cjs`)
- Jest test suite — 28 tests, ~94 % statement coverage
- GitHub Actions CI/CD workflow
- MIT licence

---

[Unreleased]: https://github.com/dnuzi/niyox/compare/v0.0.2...HEAD
[0.0.2]: https://github.com/dnuzi/niyox/compare/v0.0.1...v0.0.2
[0.0.1]: https://github.com/dnuzi/niyox/releases/tag/v0.0.1
