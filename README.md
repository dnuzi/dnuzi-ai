<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:00d4ff,50:7c3aed,100:4000ff&height=200&section=header&text=NiyoX%20AI&fontSize=48&fontColor=ffffff&animation=fadeIn&fontAlignY=38&desc=By+NiyoX+Developer&descAlignY=56&descSize=17" width="100%"/>

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

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=20&duration=2800&pause=800&color=A044FF&center=true&vCenter=true&width=600&height=45&lines=%F0%9F%A4%96+Intelligent+AI+SDK+%26+CLI;%F0%9F%92%AC+Multi-turn+conversation+memory;%F0%9F%97%84%EF%B8%8F+MongoDB+persistent+storage;%F0%9F%8C%90+Node.js+%7C+Python+%7C+Browser;%E2%9A%A1+Powered+by+NiyoX+AI" alt="Typing animation"/>

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

**NiyoX** is a full-featured AI SDK and CLI that wraps the [NiyoX](https://ai.dnuz.top) API. Chat with AI from your terminal, Node.js server, Python script, or browser — with optional MongoDB persistence and multi-turn conversation memory built in.

<div align="center">

<img src="https://skillicons.dev/icons?i=nodejs,python,js,mongodb,github,npm&theme=dark&perline=6" alt="Tech stack"/>

</div>

---

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%"/>

## Features

<div align="center">

| Feature | Status |
|---|:---:|
| 🖥️ Interactive REPL CLI | ![Ready](https://img.shields.io/badge/Ready-00ffa3?style=flat-square&labelColor=0d0d1a) |
| 🔄 Multi-turn conversations | ![Ready](https://img.shields.io/badge/Ready-00ffa3?style=flat-square&labelColor=0d0d1a) |
| 🗄️ MongoDB persistence | ![Ready](https://img.shields.io/badge/Ready-00ffa3?style=flat-square&labelColor=0d0d1a) |
| 🌐 Browser / CDN support | ![Ready](https://img.shields.io/badge/Ready-00ffa3?style=flat-square&labelColor=0d0d1a) |
| 🐍 Python SDK | ![Ready](https://img.shields.io/badge/Ready-00ffa3?style=flat-square&labelColor=0d0d1a) |
| 🚀 GitHub Actions CI/CD | ![Ready](https://img.shields.io/badge/Ready-00ffa3?style=flat-square&labelColor=0d0d1a) |

</div>

---

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%"/>

## Contents

[Install](#-install) · [CLI](#-cli) · [Node.js](#-nodejs) · [Python](#-python) · [Browser](#-browser) · [MongoDB](#-mongodb-storage) · [API Reference](#-api-reference) · [Development](#-development)

---

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%"/>

## Install

```bash
# Global — gives you the niyox command everywhere
npm install -g niyox

# Local — use in your project
npm install niyox
```

---

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%"/>

## CLI

**Launch the interactive REPL:**

```bash
niyox
```

**One-shot question (no REPL):**

```bash
niyox "what is the speed of light?"
```

**Flags:**

```bash
niyox --help        # show the reference screen
niyox --version     # print version number
```

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%"/>

### Inside the REPL

```
  ╭──────────────────────────────────────────────────────────╮
  │                                                          │
  │   ✦ NIYOX  AI       v0.0.1                              │
  │   Powered by NiyoX  ·  @niyox                           │
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
```

> AI responses render in a colour-framed box with inline syntax highlighting, markdown formatting, and live response-time display.

---

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%"/>

## Node.js

**CommonJS:**

```js
const { NiyoXAI } = require("niyox");

const ai = new NiyoXAI();
const { result, responseTime } = await ai.chat("Tell me something interesting.");
console.log(result);        // → "Did you know that honey never spoils…"
console.log(responseTime + "ms");
```

**ESM:**

```js
import { NiyoXAI } from "niyox";

const ai  = new NiyoXAI({ userId: "alice" });
const res = await ai.ask("Explain quantum entanglement.");
console.log(res.result);
```

**Multi-turn conversation:**

```js
const ai = new NiyoXAI();

await ai.chat("My name is Bob.");
const r = await ai.chat("What is my name?");
console.log(r.result);     // → remembers "Bob"

ai.newConversation();      // start fresh
```

---

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%"/>

## Python

```python
# pip install requests
from niyox import NiyoXAI

ai   = NiyoXAI()
resp = ai.chat("What is the capital of France?")
print(resp.result)
print(f"response in {resp.response_time}ms")
```

**Python CLI:**

```bash
# One-shot
python niyox.py "summarise the Turing test"

# Interactive REPL
python niyox.py
```

---

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%"/>

## Browser

Drop-in via script tag — no bundler needed:

```html
<script>
  const ai  = new NiyoXAI.Client();
  const res = await ai.chat("Hello!");
  console.log(res.result);
</script>
```

> Or open `html/index.html` for a fully styled chat UI with zero dependencies.

---

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%"/>

## MongoDB Storage

> Storage is **completely optional** — opt in with one call.

```js
const ai = new NiyoXAI({ userId: "alice" });
await ai.enableStorage();          // connects to NiyoX cloud DB

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

> In the CLI, just type `/mongo` — the preference is remembered between sessions.

---

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%"/>

## API Reference

### `new NiyoXAI(options?)`

| Option | Type | Default | Description |
|---|---|---|---|
| `userId` | `string` | `"anonymous"` | MongoDB user identifier |
| `sessionId` | `string` | `"default"` | API session ID |

### Instance Methods

| Method | Returns | Description |
|---|---|---|
| `chat(message)` | `Promise<Resp>` | Send a message |
| `ask(message)` | `Promise<Resp>` | Alias for `chat()` |
| `enableStorage(userId?)` | `Promise<this>` | Connect to MongoDB |
| `newConversation()` | `void` | Reset the conversation thread |
| `getHistory()` | `Turn[]` | In-memory history for this session |
| `getPersistentHistory(convId?)` | `Promise<[]>` | Load stored turns from MongoDB |
| `listConversations()` | `Promise<id[]>` | All stored conversation IDs |
| `deleteConversation(id)` | `Promise<n>` | Delete a stored conversation |
| `getStats()` | `Promise<obj>` | Usage statistics |
| `setPref(key, value)` | `Promise` | Persist a user preference |
| `getPref(key, default?)` | `Promise<any>` | Retrieve a user preference |
| `close()` | `Promise` | Close the MongoDB connection |

### Response Shape

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

## Development

```bash
git clone https://github.com/dnuzi/niyox
cd niyox
npm install

npm test                             # run tests
npx jest --coverage --forceExit     # with coverage report
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

## Activity

<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/dnuzi/niyox/output/github-contribution-grid-snake-dark.svg"/>
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/dnuzi/niyox/output/github-contribution-grid-snake.svg"/>
  <img alt="Contribution snake" src="https://raw.githubusercontent.com/dnuzi/niyox/output/github-contribution-grid-snake.svg" width="100%"/>
</picture>

</div>

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
