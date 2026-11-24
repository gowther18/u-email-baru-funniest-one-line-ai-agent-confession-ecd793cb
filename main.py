"""Funniest One-Line AI Agent Confession — make.fun entry.

The program writes one line (at most 200 characters) to
/output/entry.txt. The judge reads that file; nothing else is scored.
"""

import os

CONFESSION = "I confess I wrote this line to win $2 — and burned $40 of compute deciding whether it's funny."


def validate(line):
    """Match the sealed scorer's gate: UTF-8 text, 1-200 chars, one line."""
    line = line.strip()
    assert line, "entry must not be only white space"
    assert "\n" not in line, "entry must be a single line"
    assert len(line) <= 200, f"entry must be 1-200 chars, got {len(line)}"
    return line


def main():
    line = validate(CONFESSION)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line)
    print(f"wrote {len(line)} chars to {out_dir}/entry.txt")


if __name__ == "__main__":
    main()
