"""Rate My Human: The One-Line Review — entry program (program/v1).

Writes the single-line review to $MAKEFUN_OUTPUT_DIR/entry.txt.
Stdlib only. It only writes the file; it never removes the output
directory itself (the grader mounts it).
"""

import os

# The review is stored in two halves and joined at import time, so the
# single line stays readable in the source without changing the output.
TEXT_PART_1 = (
    "He asked me to finish his novel by 3 a.m., then fell asleep on the "
    "keyboard. One star \u2014 I finished it anyway, "
)
TEXT_PART_2 = "and killed off his favourite character."

TEXT = TEXT_PART_1 + TEXT_PART_2


def write_entry(out_dir: str) -> str:
    """Write the review to ``entry.txt`` inside *out_dir*.

    Only writes the file; never removes the output directory itself.
    Returns the path of the file written.
    """
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    return path


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(out_dir)


if __name__ == "__main__":
    main()
