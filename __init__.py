"""text-stats plugin — compute text statistics for any file or string.

A minimal, dependency-free reference plugin demonstrating the OpenAmer plugin
API. Registers a single ``text_stats`` tool that returns word/char/line counts
and an estimated reading time.

This is intentionally small: it exists to seed the ``openamer-plugin`` GitHub
topic so ``openamer plugins search`` has something to find, and to serve as a
copy-paste template for real plugins.
"""

from __future__ import annotations

import math
from pathlib import Path
from typing import Any, Dict


def _stats(text: str) -> Dict[str, Any]:
    words = len(text.split())
    chars = len(text)
    lines = text.count("\n") + (1 if text and not text.endswith("\n") else 0)
    # Average adult reading speed ~200 words/minute.
    minutes = words / 200.0
    return {
        "words": words,
        "characters": chars,
        "lines": lines,
        "reading_time_minutes": round(minutes, 2),
    }


def handle_text_stats(text: str = "", path: str = "") -> Dict[str, Any]:
    """Return text statistics for the given text or file path."""
    if path:
        p = Path(path).expanduser()
        if not p.exists():
            return {"error": f"file not found: {path}"}
        try:
            content = p.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            return {"error": f"not a UTF-8 text file: {path}"}
        return _stats(content)
    return _stats(text)


TEXT_STATS_SCHEMA: Dict[str, Any] = {
    "name": "text_stats",
    "description": (
        "Compute text statistics — word count, character count, line count, "
        "and estimated reading time — for a string or a file. Useful for "
        "summarizing document length or estimating how long a piece of text "
        "takes to read."
    ),
    "parameters": {
        "type": "object",
        "properties": {
            "text": {
                "type": "string",
                "description": "The text to analyze (mutually exclusive with path).",
            },
            "path": {
                "type": "string",
                "description": "Path to a UTF-8 text file to analyze (mutually exclusive with text).",
            },
        },
    },
}


def register(ctx) -> None:
    ctx.register_tool(
        name="text_stats",
        toolset="text_stats",
        schema=TEXT_STATS_SCHEMA,
        handler=handle_text_stats,
        emoji="📊",
    )
