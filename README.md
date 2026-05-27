<div align="center">

```
██████╗ ███╗   ██╗██╗   ██╗███████╗██╗
██╔══██╗████╗  ██║██║   ██║╚══███╔╝██║
██║  ██║██╔██╗ ██║██║   ██║  ███╔╝ ██║
██║  ██║██║╚██╗██║██║   ██║ ███╔╝  ██║
██████╔╝██║ ╚████║╚██████╔╝███████╗██║
╚═════╝ ╚═╝  ╚═══╝ ╚═════╝ ╚══════╝╚═╝
```

**Dnuzi AI** — SDK & CLI powered by [DanuZz](https://ai.dnuz.top)

[![npm version](https://img.shields.io/npm/v/dnuzi?style=flat-square&color=a044ff&labelColor=0d0d1a)](https://npmjs.com/package/dnuzi)
[![npm downloads](https://img.shields.io/npm/dm/dnuzi?style=flat-square&color=00d2ff&labelColor=0d0d1a)](https://npmjs.com/package/dnuzi)
[![license](https://img.shields.io/npm/l/dnuzi?style=flat-square&color=00ffa3&labelColor=0d0d1a)](LICENSE)
[![node](https://img.shields.io/node/v/dnuzi?style=flat-square&color=ffd93d&labelColor=0d0d1a)](package.json)
[![tests](https://img.shields.io/github/actions/workflow/status/YOUR_USERNAME/dnuzi/publish.yml?style=flat-square&color=00ffa3&labelColor=0d0d1a&label=tests)](https://github.com/YOUR_USERNAME/dnuzi/actions)
[![provenance](https://img.shields.io/badge/provenance-GitHub%20Actions-a044ff?style=flat-square&labelColor=0d0d1a)](https://github.com/YOUR_USERNAME/dnuzi/actions)

</div>

---

## ◈  Contents

- [Install](#-install)
- [CLI](#-cli)
- [Node.js](#-nodejs)
- [Python](#-python)
- [Browser](#-browser)
- [MongoDB Storage](#-mongodb-storage)
- [API Reference](#-api-reference)
- [Publishing](#-publishing-to-npm)

---

## ◈  Install

```bash
# global — gives you the dnuzi command everywhere
npm install -g dnuzi

# local — use in your project
npm install dnuzi
```

---

## ◈  CLI

Launch the interactive REPL:

```
dnuzi
```

One-shot question (no REPL):

```
dnuzi "what is the speed of light?"
```

Flags:

```
dnuzi --help        show the reference screen
dnuzi --version     print version number
dnuzi -v            same as --version
```

### Inside the REPL

```
  ╭──────────────────────────────────────────────────────────╮
  │                                                          │
  │   ✦ DNUZI  AI       v0.0.1                              │
  │   Powered by DanuZz  ·  @dnuzi                          │
  │                                                          │
  │   ◇ Commands                                             │
  │                                                          │
  │   › /help            →  show all commands                │
  │   › /new             →  fresh conversation thread        │
  │   › /history         →  in-memory chat log               │
  │   › /stats           →  usage stats  (MongoDB)           │
  │   › /convs           →  stored conversation list         │
  │   › /mongo           →  enable persistent storage        │
  │   › /user <id>       →  set your user ID                 │
  │   › /clear           →  clear the screen                 │
  │   › /exit            →  quit                             │
  │                                                          │
  ╰──────────────────────────────────────────────────────────╯

  █ ❯ _
```

AI responses render in a colour-framed box with inline syntax highlighting,
bold/italic markdown, numbered lists, and live response-time display.

---

## ◈  Node.js

**CommonJS:**

```js
const { DnuziAI } = require("dnuzi");

const ai = new DnuziAI();
const { result, responseTime } = await ai.chat("Tell me something interesting.");
console.log(result);
// → "Did you know that honey never spoils…"
console.log(responseTime + "ms");
```

**ESM:**

```js
import { DnuziAI } from "dnuzi";

const ai  = new DnuziAI({ userId: "alice" });
const res = await ai.ask("Explain quantum entanglement.");
console.log(res.result);
```

**Multi-turn conversation:**

```js
const ai = new DnuziAI();

await ai.chat("My name is Bob.");
const r = await ai.chat("What is my name?");
console.log(r.result);     // remembers "Bob"

ai.newConversation();      // start fresh
```

---

## ◈  Python

```python
# pip install requests
from dnuzi import DnuziAI

ai   = DnuziAI()
resp = ai.chat("What is the capital of France?")
print(resp.result)
print(f"  response in {resp.response_time}ms")
```

**Python CLI:**

```bash
# one-shot
python dnuzi.py "summarise the Turing test"

# interactive REPL
python dnuzi.py
```

---

## ◈  Browser

Drop-in via script tag (no bundler needed):

```html
<script>
  const ai  = new DnuziAI.Client();
  const res = await ai.chat("Hello!");
  console.log(res.result);
</script>
```

Or open `html/index.html` for a fully styled chat UI with zero dependencies.

---

## ◈  MongoDB Storage

Storage is **completely optional** — opt in with one call.

```js
const ai = new DnuziAI({ userId: "alice" });
await ai.enableStorage();          // connects to Dnuzi cloud DB

// every subsequent chat() call is automatically persisted
const res = await ai.chat("Hello!");

// list all conversation IDs
const ids = await ai.listConversations();

// retrieve a conversation
const msgs = await ai.getPersistentHistory(ids[0]);

// usage statistics
const stats = await ai.getStats();
// { totalMessages: 42, totalConversations: 7, avgResponseTimeMs: "834" }

// per-user preferences
await ai.setPref("language", "en");
const lang = await ai.getPref("language");

// graceful shutdown
await ai.close();
```

**In the CLI**, just type `/mongo` — preference is remembered between sessions.

---

## ◈  API Reference

### `new DnuziAI(options?)`

| Option      | Type   | Default         | Description             |
|-------------|--------|-----------------|-------------------------|
| `userId`    | string | `"anonymous"`   | MongoDB user identifier |
| `sessionId` | string | `"default"`     | API session ID          |

### Instance methods

| Method                           | Returns         | Description                              |
|----------------------------------|-----------------|------------------------------------------|
| `chat(message)`                  | `Promise<Resp>` | Send a message                           |
| `ask(message)`                   | `Promise<Resp>` | Alias for `chat()`                       |
| `enableStorage(userId?)`         | `Promise<this>` | Connect to MongoDB                       |
| `newConversation()`              | `void`          | Reset the conversation thread            |
| `getHistory()`                   | `Turn[]`        | In-memory history for this session       |
| `getPersistentHistory(convId?)`  | `Promise<[]>`   | Load stored turns from MongoDB           |
| `listConversations()`            | `Promise<id[]>` | All stored conversation IDs              |
| `deleteConversation(id)`         | `Promise<n>`    | Delete a stored conversation             |
| `getStats()`                     | `Promise<obj>`  | Usage statistics                         |
| `setPref(key, value)`            | `Promise`       | Persist a user preference                |
| `getPref(key, default?)`         | `Promise<any>`  | Retrieve a user preference               |
| `close()`                        | `Promise`       | Close the MongoDB connection             |

### Response shape

```ts
{
  result:         string   // AI reply text
  conversationId: string   // thread ID (persist for multi-turn)
  sessionId:      string
  responseTime:   number   // milliseconds
  attempts:       number
}
```

---

## ◈  Publishing to npm

This package auto-publishes via **GitHub Actions** with **provenance signing**
(the green "Built and signed on GitHub Actions" badge shown on npm).

### Setup (one time)

1. Create an npm account and generate an **Automation** token at npmjs.com
2. Add it as a GitHub secret named `NPM_TOKEN`
   `Settings → Secrets and variables → Actions → New repository secret`

### Release

```bash
# bump version in package.json, commit, then tag
git add package.json
git commit -m "chore: release v0.0.2"
git tag v0.0.2
git push origin main --tags
```

GitHub Actions will:

```
  ◈  run tests on Node 18, 20, 22
  ◈  build the package
  ◈  sync version from git tag
  ◈  npm publish --provenance --access public
  ◈  create a GitHub Release with auto-generated notes
```

The provenance entry on npm will look exactly like:

```
  Built and signed on GitHub Actions
  Source Commit   github.com/you/dnuzi@<sha>
  Build File      .github/workflows/publish.yml
  Public Ledger   Transparency log entry
```

---

## ◈  Development

```bash
git clone https://github.com/YOUR_USERNAME/dnuzi
cd dnuzi
npm install

# run tests
npm test

# run tests with coverage report
npx jest --coverage --forceExit
```

### Test output (expected)

```
  PASS  test/client.test.js
  PASS  test/sdk.test.js
  PASS  test/cli.test.js

  Tests:   28 passed, 28 total
  Coverage: statements 94%  |  branches 88%  |  functions 100%
```

---

<div align="center">

Built with care by **DanuZz** · `@dnuzi`

API endpoint · `https://ai.dnuz.top`

</div>
