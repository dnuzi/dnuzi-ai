# Security Policy

## Supported Versions

| Version | Supported |
|---|:---:|
| 0.0.x (latest) | ✅ |
| < 0.0.1 | ❌ |

As Dnuzi AI is pre-1.0, security fixes are applied to the latest release only.

---

## Reporting a Vulnerability

**Please do not open a public GitHub Issue for security vulnerabilities.**

If you discover a security issue, please report it privately:

1. Go to the [Security tab](https://github.com/dnuzi/dnuzi-ai/security/advisories/new) on GitHub and open a **private advisory**, or
2. Email the maintainer directly (see the author field in `package.json`).

Include as much detail as possible:

- Description of the vulnerability
- Steps to reproduce
- Potential impact
- Suggested fix (optional but appreciated)

You can expect an acknowledgement within **48 hours** and a status update within **7 days**.

---

## Disclosure Policy

We follow a **coordinated disclosure** model:

1. Reporter submits the vulnerability privately.
2. Maintainer confirms, assesses severity, and begins a fix.
3. A patched release is published.
4. A public advisory is opened **after** the patch is available.

We ask that you give us a reasonable timeframe (typically **14 days**) to address the issue before any public disclosure.

---

## Known Considerations

- **MongoDB URI** — The default connection string in `src/storage.js` and `python/dnuzi.py` uses a shared cloud database intended for demo/development use. Do not store sensitive or production data through the default URI. For production use, supply your own MongoDB instance.
- **API endpoint** — All AI requests are sent to `https://ai.dnuz.top/api/ai` over HTTPS. No API keys are required or transmitted by the client at this time.
- **No authentication layer** — The CLI and SDK do not authenticate the end user. Access controls are the responsibility of the deploying application.

---

## Out of Scope

The following are **not** considered security vulnerabilities for this project:

- Rate limiting or abuse of the public `ai.dnuz.top` API endpoint
- Issues in third-party dependencies (please report those upstream)
- Theoretical attacks with no practical exploit path

---

Thank you for helping keep Dnuzi AI safe! 🔒
