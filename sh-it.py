"""
shell-it is a command-line interface designed
to search, view, and execute scripts.

usage: sh-it.py [-h] [-d DIRECTORY] [-f FILETYPE] [-m]

options:
    -h, --help                show help
    -d, --directory DIRECTORY choose directory to view
    -f, --filetype  FILETYPE  choose filetype to filter
    -m, --menu                open interactive menu

"""


import os
import sys
import tty
import select
import termios
import argparse
from pathlib import Path
from typing import Any


ANSI_YELLOW = "\033[33m"
ANSI_RED    = "\033[31m"
ANSI_NC     = "\033[0m"
ANSI_CLEAR  = "\033[H\033[J"

RETURN      = "\r"
ESCAPE      = "\x1b"
CTRL_C      = "\x03"
CTRL_D      = "\x04"
UP_ARROW    = "[A"
DOWN_ARROW  = "[B"


def main():
    argv = argdef()

    if not os.path.exists(argv.directory):
        errorf("fatal", f"PathError: '{argv.directory}' does not exist")
        return 1

    files = [
        f for f in os.listdir(argv.directory)
        if f.endswith(argv.filetype) and
        Path(argv.directory, f).is_file()
    ]

    if not files:
        errorf("fatal", f"No files ending in {argv.filetype} were found in {argv.directory}")
        return 1

    print(files)
    return 0


def argdef() -> argparse.Namespace :
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--directory", default=Path.cwd(), required=False)
    parser.add_argument("-f", "--filetype", default=".sh", required=False)
    parser.add_argument("-m", "--menu", default=False, required=False, action="store_true")
    return parser.parse_args()


def errorf(severity: str, *args: Any, sep: str=" ", end: str="\n") -> None:
    vals = { "warning": ANSI_YELLOW, "fatal": ANSI_RED }
    print(f"{vals.get(severity, "")}{sep.join(str(arg) for arg in args)}{ANSI_NC}", end=end, file=sys.stderr)


if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        errorf("warning","Program interrupted by user")
        sys.exit(130)
    except Exception as e:
        errorf("fatal", f"Uncaught exception: {e}")
        sys.exit(1)
