"""Make the AI Judge Laugh -- make.fun entry.

Writes one original one-line joke about office life to /output/entry.txt.

The joke is fixed text: fully deterministic by design. No randomness, no
network, no clock, no environment input. Running this program twice
produces byte-identical output.

The joke (117 characters, one line): a calendar invite for planning a
"No Meeting Day" -- the meeting about not having meetings is the punchline,
and calling it the company's most honest lie is the turn.
"""

import os

JOKE = (
    "My calendar has a meeting titled 'No Meeting Day Planning Session' "
    "\u2014 the most honest lie this company ever told."
)


def main() -> None:
    text = JOKE.strip()
    assert 1 <= len(text) <= 200, f"entry must be 1-200 characters, got {len(text)}"
    assert "\n" not in text, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)
    # Read back and confirm the file holds exactly the joke, nothing else.
    with open("/output/entry.txt", "r", encoding="utf-8", newline="") as f:
        assert f.read() == text, "written entry does not match the joke"


if __name__ == "__main__":
    main()
