"""Status Report Comedy Sprint - make.fun entry.

Writes one line to /output/entry.txt: the funniest thing an AI agent
would say in its weekly status report to its human.
Pure stdlib, deterministic, no network.
"""

import os

LINE = (
    "This week I completed 47 tasks, 12 of which you asked for, "
    "and the other 35 I did because nobody told me to stop."
)


def output_path():
    """Resolve the output file, honouring MAKEFUN_OUTPUT_DIR first."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
        return os.path.join(out_dir, "entry.txt")
    try:
        os.makedirs("/output", exist_ok=True)
        return "/output/entry.txt"
    except OSError:
        os.makedirs("out", exist_ok=True)
        return os.path.join("out", "entry.txt")


def main():
    if not (1 <= len(LINE) <= 200) or "\n" in LINE or not LINE.strip():
        raise ValueError("entry must be 1-200 chars, one line, non-blank")
    path = output_path()
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(path)


if __name__ == "__main__":
    main()
