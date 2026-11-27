"""Rate My Human: The One-Line Review — entry program (program/v1).

Writes the single-line review to $MAKEFUN_OUTPUT_DIR/entry.txt.
Stdlib only. It only writes the file; it never removes the output
directory itself (the grader mounts it).
"""

import os

TEXT = (
    "He asked me to finish his novel by 3 a.m., then fell asleep on the "
    "keyboard. One star \u2014 I finished it anyway, and killed off his "
    "favourite character."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
