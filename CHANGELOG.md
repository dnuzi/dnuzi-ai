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
- `DnuziAI` — high-level SDK combining client and storage
  - `enableStorage()` opt-in
  - Full delegation to `NiyoXClient` and `NiyoXStorage`
- **CLI** (`bin/cli.js`) with interactive REPL
  - Commands: `/help`, `/new`, `/history`, `/stats`, `/convs`, `/mongo`, `/user`, `/clear`, `/exit`
  - One-shot mode: `niyox "your question"`
  - `--version` / `-v` and `--help` / `-h` flags
  - Markdown rendering with syntax highlighting
  - Coloured boxed responses with response-time display
- **Browser SDK** (`html/index.html`)
  - Zero-dependency chat UI
  - Inline `NiyoXAI.Client` — drop-in via script tag
- **ESM + CJS dual build** (`lib/index.mjs`, `lib/index.cjs`)
- Jest test suite — 28 tests, ~94 % statement coverage
- GitHub Actions CI/CD workflow
- MIT licence

---

[Unreleased]: https://github.com/dnuzi/niyox/compare/v0.0.1...HEAD
[0.0.1]: https://github.com/dnuzi/niyox/releases/tag/v0.0.1
