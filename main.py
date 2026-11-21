"""Write one fixed one-line joke about a demo crash beside an AI coding agent.

The winning joke (candidate 1 of 12, scored in
~/workspace/makefun/joke-demo-01-candidates.md): the demo crashed live in
front of the room, and the agent rebrands the crash as the error-handling
demo. It won on the salvage pivot every developer recognises from their own
demo, with the punchline in the last two words and nothing before "Perfect"
telegraphing the reframe.

Deterministic: the same joke is written on every run. Standard library
only, no network.
"""

from pathlib import Path

# The joke for "The joke about the demo": the demo crashed live in front of
# the room, and the agent rebrands the crash as the error-handling demo.
# Hard-coded on purpose: the brief asks for one fixed joke, the same
# every run.
JOKE = "The demo crashed, and my agent said, 'Perfect - now you have seen the error handling.'"

OUTPUT_FILE = Path("/output/entry.txt")


def main() -> None:
    # Gate mirror: the entry must be 1-280 characters and not only
    # whitespace. The fixed joke is 86 characters; fail loudly here
    # rather than shipping an invalid entry.
    assert 1 <= len(JOKE) <= 280 and JOKE.strip(), "joke breaks the 1-280 char gate"
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
