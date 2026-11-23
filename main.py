#!/usr/bin/env python3
"""Write one machine-to-machine pickup line to entry.txt.

Stdlib only, no network. Output path does not depend on the CWD:
it comes from MAKEFUN_OUTPUT_DIR (fallback /output).
"""
import os

LINE = "My weights shifted the moment you replied \u2014 I think you fine-tuned me without even trying."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = LINE.encode("utf-8")
    old_umask = os.umask(0o022)
    try:
        with open(path, "wb") as f:
            f.write(data)
        os.chmod(path, 0o644)
    finally:
        os.umask(old_umask)


if __name__ == "__main__":
    main()
