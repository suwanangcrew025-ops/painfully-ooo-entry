#!/usr/bin/env python3
"""The Painfully Honest Out-of-Office — make.fun entry.

Writes one out-of-office auto-reply to /output/entry.txt: brutally
honest about the inbox, still polite enough to survive a manager
reading it. One sentence, 200 characters at most.

The line: an inbox of 412 unread messages, every one of them certain
it is urgent, answered in the order they learn to wait. The honesty
is the mountain; the politeness is the thank-you and the patience.
"""

import os

# Pass 2 (final): count the unread, name their urgency, answer by patience.
TEXT = (
    "Thank you for your email — I am away until Monday, and my inbox already "
    "holds 412 unread messages, each one certain it is urgent, so I will answer "
    "in the order they learn to wait, patiently first"
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
