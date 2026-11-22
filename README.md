# openamer-plugin-text-stats

A minimal, dependency-free reference plugin for [OpenAmer](https://github.com/openamer/openamer).

Registers a single `text_stats` tool that returns word/char/line counts and an
estimated reading time for any string or UTF-8 text file.

## Install

```bash
openamer plugins install openamer/openamer-plugin-text-stats
openamer plugins enable text-stats
openamer gateway restart
```

## Usage

The agent can then call `text_stats` with either `text` or `path`:

```json
{ "text": "The quick brown fox jumps over the lazy dog." }
```

```json
{ "path": "/path/to/document.md" }
```

## Why this exists

This plugin seeds the `openamer-plugin` GitHub topic so that
`openamer plugins search` has something to find, and serves as a copy-paste
template for real plugins. See the
[plugin guide](https://github.com/openamer/openamer/blob/main/website/docs/guides/build-a-openamer-plugin)
for the full API.

## Structure

- `plugin.yaml` — manifest (name, version, description, author)
- `__init__.py` — the `register(ctx)` entry point + tool schema + handler

---

## Kontakt

Fragen, Fehlerberichte, Sponsoring: **openamer-max@proton.me**

Unterstützen: [PayPal](https://www.paypal.com/qrcodes/p2pqrc/BVZD4HRJ9G6YG) · [Website](https://openamer-max.github.io/)
