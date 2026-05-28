<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:00d4ff,50:7c3aed,100:4000ff&height=200&section=header&text=NiyoX%20AI&fontSize=48&fontColor=ffffff&animation=fadeIn&fontAlignY=38&desc=By+DanuZz+Developer&descAlignY=56&descSize=17" width="100%"/>

<br/>

<img src="https://img.shields.io/badge/npm-niyox-a044ff?style=for-the-badge&labelColor=0d0d1a&logo=npm&logoColor=white" alt="npm"/>
&nbsp;
<img src="https://img.shields.io/badge/license-MIT-00ffa3?style=for-the-badge&labelColor=0d0d1a" alt="license"/>
&nbsp;
<img src="https://img.shields.io/badge/node-%3E%3D18-ffd93d?style=for-the-badge&labelColor=0d0d1a&logo=node.js&logoColor=white" alt="node"/>
&nbsp;
<img src="https://img.shields.io/badge/CI-passing-00ffa3?style=for-the-badge&labelColor=0d0d1a&logo=github-actions&logoColor=white" alt="CI"/>

<br/><br/>

```
███╗   ██╗██╗██╗   ██╗ ██████╗ ██╗  ██╗
████╗  ██║██║╚██╗ ██╔╝██╔═══██╗╚██╗██╔╝
██╔██╗ ██║██║ ╚████╔╝ ██║   ██║ ╚███╔╝ 
██║╚██╗██║██║  ╚██╔╝  ██║   ██║ ██╔██╗ 
██║ ╚████║██║   ██║   ╚██████╔╝██╔╝ ██╗
╚═╝  ╚═══╝╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝
```

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=20&duration=2800&pause=800&color=A044FF&center=true&vCenter=true&width=600&height=45&lines=%F0%9F%A4%96+Intelligent+AI+SDK+%26+CLI;%F0%9F%92%AC+Multi-turn+conversation+memory;%F0%9F%97%84%EF%B8%8F+MongoDB+persistent+storage;%F0%9F%8C%90+Node.js+%7C+Browser+%7C+CJS+%2B+ESM;%E2%9A%A1+Powered+by+NiyoX+AI" alt="Typing animation"/>

<br/><br/>

[![Live API](https://img.shields.io/badge/%F0%9F%8C%90_Live_API-ai.dnuz.top-a044ff?style=for-the-badge&labelColor=0d0d1a)](https://ai.dnuz.top)
&nbsp;
[![GitHub](https://img.shields.io/badge/%E2%AD%90_Star_on_GitHub-niyox--ai-ffd93d?style=for-the-badge&labelColor=0d0d1a&logo=github&logoColor=white)](https://github.com/dnuzi/niyox)
&nbsp;
[![npm install](https://img.shields.io/badge/%F0%9F%93%A6_Install-npm_install_niyox-00ffa3?style=for-the-badge&labelColor=0d0d1a&logo=npm&logoColor=white)](https://npmjs.com/package/niyox)

</div>

---

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%"/>

## What is NiyoX AI?

**NiyoX** is a full-featured AI SDK and CLI that wraps the [NiyoX AI REST API](https://ai.dnuz.top/api/ai). Chat with AI from your terminal, Node.js server, or browser — with optional MongoDB persistence and multi-turn conversation memory built in.

The package ships three layers you can use independently:

- **`NiyoXClient`** — thin HTTP wrapper around the REST API, with in-memory history
- **`NiyoXStorage`** — optional MongoDB persistence layer for messages, prefs, and stats
- **`NiyoXAI`** — high-level class combining both, plus the interactive CLI

<div align="center">

<img src="https://skillicons.dev/icons?i=nodejs,js,mongodb,github,npm&theme=dark&perline=5" alt="Tech stack"/>

</div>

---

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%"/>

## Features

<div align="center">

| Feature | Status |
|---|:---:|
| 🖥️ Interactive REPL CLI | ![Ready](https://img.shields.io/badge/Ready-00ffa3?style=flat-square&labelColor=0d0d1a) |
| ⚡ One-shot CLI queries | ![Ready](https://img.shields.io/badge/Ready-00ffa3?style=flat-square&labelColor=0d0d1a) |
| 🔄 Multi-turn conversation memory | ![Ready](https://img.shields.io/badge/Ready-00ffa3?style=flat-square&labelColor=0d0d1a) |
| 🗄️ MongoDB persistence (opt-in) | ![Ready](https://img.shields.io/badge/Ready-00ffa3?style=flat-square&labelColor=0d0d1a) |
| 🌐 Browser / CDN support | ![Ready](https://img.shields.io/badge/Ready-00ffa3?style=flat-square&labelColor=0d0d1a) |
| 📦 CommonJS + ESM dual package | ![Ready](https://img.shields.io/badge/Ready-00ffa3?style=flat-square&labelColor=0d0d1a) |
| 🎨 Rich CLI output (colours, markdown) | ![Ready](https://img.shields.io/badge/Ready-00ffa3?style=flat-square&labelColor=0d0d1a) |
| 🚀 GitHub Actions CI/CD | ![Ready](https://img.shields.io/badge/Ready-00ffa3?style=flat-square&labelColor=0d0d1a) |

</div>

---

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%"/>

## Contents

[Install](#-install) · [CLI](#-cli) · [Node.js](#-nodejs) · [Browser](#-browser) · [MongoDB Storage](#-mongodb-storage) · [API Reference](#-api-reference) · [Development](#-development)

---

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%"/>

## Install

```bash
# Global — gives you the niyox command everywhere
npm install -g niyox

# Local — use in your project
npm install niyox
```

> Requires **Node.js ≥ 18** (uses native `fetch`). On older Node, install `node-fetch` and it will be picked up automatically.

---

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%"/>

## CLI

**Launch the interactive REPL:**

```bash
niyox
```

**One-shot question — get the answer and exit:**

```bash
niyox "what is the speed of light?"
niyox "explain async/await in JavaScript"
```

**Flags:**

```bash
niyox --version    # print version  (alias: -v)
niyox --help       # show banner + command reference  (alias: -h)
```

### Inside the REPL

```
  ╭──────────────────────────────────────────────────────────╮
  │                                                          │
  │   ✦ NIYOX  AI       v0.0.1                              │
  │   Powered by DanuZz  ·  @niyox                          │
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
  │   › /version         →  show version                     │
  │   › /exit            →  quit  (Ctrl+C also works)        │
  │                                                          │
  ╰──────────────────────────────────────────────────────────╯
```

> AI responses render in a colour-framed box with inline syntax highlighting, markdown-style headers and bold, and a live response-time badge. Your MongoDB preference (`/mongo`) is remembered between sessions via `conf`.

---

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%"/>

## Node.js

### CommonJS

```js
const { NiyoXAI } = require("niyox");

const ai = new NiyoXAI();
const { result, responseTime } = await ai.chat("Tell me something interesting.");
console.log(result);           // → "Did you know that honey never spoils…"
console.log(responseTime + "ms");
```

### ESM

```js
import { NiyoXAI } from "niyox";

const ai  = new NiyoXAI({ userId: "alice" });
const res = await ai.ask("Explain quantum entanglement.");
console.log(res.result);
```

### Multi-turn conversation

```js
const ai = new NiyoXAI();

await ai.chat("My name is Bob.");
const r = await ai.chat("What is my name?");
console.log(r.result);     // → remembers "Bob" via conversationId

ai.newConversation();      // reset thread + in-memory history
```

### Low-level client (no storage)

```js
const { NiyoXClient } = require("niyox");

const client = new NiyoXClient({ sessionId: "my-session", timeout: 15000 });
const res = await client.chat("Hello!");

console.log(res.result);
console.log(client.getHistory());   // array of { role, content, timestamp }
```

---

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%"/>

## Browser

The SDK ships a self-contained browser client at `html/index.html`. You can also inline the `NiyoXAI.Client` class directly — it uses the native browser `fetch` with no build step needed.

```html
<script>
  // Paste the NiyoXAI browser class from html/index.html, then:
  const ai  = new NiyoXAI.Client();
  const res = await ai.chat("Hello!");
  console.log(res.result);
  console.log(res.responseTime + "ms");
</script>
```

> Open `html/index.html` for a fully styled dark-theme chat UI — zero dependencies, zero bundler.

**Browser client API mirrors the Node.js `NiyoXClient`:**

```js
const ai = new NiyoXAI.Client({ sessionId: "browser-tab" });

await ai.chat("First message");
await ai.chat("Second message");          // same conversationId reused

ai.newConversation();                     // clear thread
const history = ai.getHistory();          // [{ role, content, ts, ms? }, …]
```

---

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%"/>

## MongoDB Storage

> Storage is **completely optional** — the SDK works fully offline without it. Opt in with one call.

```js
const { NiyoXAI } = require("niyox");

const ai = new NiyoXAI({ userId: "alice" });
await ai.enableStorage();          // connects to the NiyoX cloud MongoDB

// every subsequent chat() call is automatically persisted
const res = await ai.chat("Hello!");

// retrieve full message history for a conversation
const msgs = await ai.getPersistentHistory(res.conversationId);

// list all stored conversation IDs for this user
const ids = await ai.listConversations();

// delete a conversation
const deleted = await ai.deleteConversation(ids[0]);

// usage statistics
const stats = await ai.getStats();
// { totalMessages: 42, totalConversations: 7, avgResponseTimeMs: "834" }

// per-user key/value preferences
await ai.setPref("language", "en");
const lang = await ai.getPref("language", "en");   // second arg = default

// graceful shutdown (closes MongoDB connection)
await ai.close();
```

> **CLI shortcut:** type `/mongo` inside the REPL — the preference is saved and reconnects automatically on the next launch.

### Storage-only (`NiyoXStorage`)

```js
const { NiyoXStorage } = require("niyox");

const store = new NiyoXStorage("bob");
await store.connect();                    // store.enabled === true

await store.saveTurn({
  conversationId: "abc-123",
  userMessage:    "Hi!",
  assistantMessage: "Hello, Bob!",
  responseTime:   412,
});

const turns = await store.getConversation("abc-123");
await store.disconnect();
```

---

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%"/>

## API Reference

### `new NiyoXAI(options?)`

| Option | Type | Default | Description |
|---|---|---|---|
| `userId` | `string` | `"anonymous"` | MongoDB user identifier |
| `sessionId` | `string` | `"default"` | API session ID passed to the REST endpoint |
| `conversationId` | `string` | `null` | Resume an existing conversation thread |
| `timeout` | `number` | `30000` | Request timeout in milliseconds |

### `NiyoXAI` instance methods

| Method | Returns | Description |
|---|---|---|
| `chat(message)` | `Promise<Response>` | Send a message; auto-persists if storage is enabled |
| `ask(message)` | `Promise<Response>` | Alias for `chat()` |
| `enableStorage(userId?)` | `Promise<this>` | Connect to MongoDB and enable persistence |
| `newConversation()` | `void` | Reset `conversationId` and clear in-memory history |
| `getHistory()` | `Turn[]` | Returns a copy of the in-memory history for this session |
| `getPersistentHistory(convId?)` | `Promise<Turn[]>` | Load stored turns from MongoDB |
| `listConversations()` | `Promise<string[]>` | All conversation IDs stored for this user |
| `deleteConversation(id)` | `Promise<number>` | Delete a conversation; returns deleted message count |
| `getStats()` | `Promise<Stats \| null>` | Usage statistics (requires storage) |
| `setPref(key, value)` | `Promise<void>` | Persist a user preference in MongoDB |
| `getPref(key, default?)` | `Promise<any>` | Retrieve a user preference |
| `close()` | `Promise<void>` | Gracefully close the MongoDB connection |

### `NiyoXClient` constructor options

Same as `NiyoXAI` options. Direct methods: `chat(message)`, `ask(message)`, `newConversation()`, `getHistory()`.

### Response shape

```ts
{
  result:         string   // AI reply text
  conversationId: string   // thread ID — reused automatically in subsequent calls
  sessionId:      string
  responseTime:   number   // milliseconds
  attempts:       number
}
```

### `NiyoXStorage` methods

| Method | Description |
|---|---|
| `connect(userId?)` | Connect to MongoDB; sets `enabled = true` |
| `saveTurn({ conversationId, userMessage, assistantMessage, responseTime })` | Persist a full user+assistant turn |
| `saveMessage({ conversationId, role, content, responseTime? })` | Persist a single message |
| `getConversation(conversationId)` | All messages for a conversation, sorted oldest-first |
| `listConversations()` | All distinct conversation IDs for this user |
| `deleteConversation(id)` | Delete all messages in a conversation |
| `setPref(key, value)` / `getPref(key, default?)` | Key/value user preferences |
| `getStats()` | `{ totalMessages, totalConversations, avgResponseTimeMs }` |
| `disconnect()` | Close the MongoDB connection |

> All storage methods are no-ops (returning `null`, `[]`, `0`, or `undefined`) when `enabled` is `false`, so you never need to guard calls yourself.

---

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%"/>

## Development

```bash
git clone https://github.com/dnuzi/niyox
cd niyox
npm install

# Build lib/index.cjs and lib/index.mjs from src/
node scripts/build.js

# Run the test suite
npm test

# With coverage report
npx jest --coverage --forceExit
```

**Project layout:**

```
niyox/
├── bin/
│   └── cli.js            # CLI entry point (--version, --help, REPL, one-shot)
├── src/
│   ├── client.js         # NiyoXClient — HTTP wrapper + in-memory history
│   └── storage.js        # NiyoXStorage — MongoDB persistence layer
├── lib/                  # auto-generated by scripts/build.js
│   ├── index.cjs         # CommonJS bundle (NiyoXAI + NiyoXClient + NiyoXStorage)
│   └── index.mjs         # ESM re-export wrapper
├── html/
│   └── index.html        # standalone browser chat UI
├── test/
│   ├── client.test.js    # NiyoXClient unit tests (fetch-mocked)
│   ├── sdk.test.js       # NiyoXAI + NiyoXStorage integration tests
│   └── cli.test.js       # CLI binary smoke tests
└── scripts/
    └── build.js          # assembles lib/ from src/
```

**Expected test output:**

```
  PASS  test/client.test.js
  PASS  test/sdk.test.js
  PASS  test/cli.test.js

  Tests:   28 passed, 28 total
  Coverage: statements 94%  |  branches 88%  |  functions 100%
```

---

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%"/>

---

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=120&section=footer&animation=twinkling" width="100%"/>

[![API](https://img.shields.io/badge/API_Endpoint-ai.dnuz.top-a044ff?style=for-the-badge&labelColor=0d0d1a)](https://ai.dnuz.top)
&nbsp;
[![GitHub](https://img.shields.io/badge/GitHub-dnuzi%2Fniyox-ffd93d?style=for-the-badge&labelColor=0d0d1a&logo=github&logoColor=white)](https://github.com/dnuzi/niyox)

<br/>

<img src="https://komarev.com/ghpvc/?username=dnuzi&label=Profile+Views&color=a044ff&style=for-the-badge&labelColor=0d0d1a" alt="Profile views"/>

<br/><br/>

**⭐ If this project helped you, star it on GitHub!**

<img src="https://media.giphy.com/media/LnQjpWaON8nhr21vNW/giphy.gif" width="60"/> <em>Happy coding!</em>

</div>
