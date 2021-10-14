#!/usr/bin/env python3

import argparse
import datetime
import os
import shutil
import subprocess
import sys


def run_shell(cmd: list[str], cwd: str = "", silent: bool = True) -> None:
    """Run command silently."""
    if silent:
        subprocess.call(
            cmd,
            cwd=cwd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
    else:
        subprocess.call(cmd, cwd=cwd)


def replace(pattern: str, repl: str, path: str) -> None:
    """Replace `pattern` with `repl` in file `path`"""
    subprocess.Popen(
        ["find", path, "-type", "f", "-exec",
             "sed", "-i", f"s/{pattern}/{repl}/g", "{}", "+"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )


def new(options) -> int:
    """Create new project from template."""

    if os.path.exists(options.name):
        print("Project already exists. Aborting...")
        return 1

    print("Copying all files...")
    shutil.copytree(f"templates/{options.template}", options.name)

    print("Taking a short coffee break...")

    print("Updating configuration...")
    replace("<NAME>", options.name, options.name)

    print("Initializing git repository...")
    run_shell(["git", "init"], cwd=options.name)
    run_shell(["git", "add", "."], cwd=options.name)
    run_shell(["git", "commit", "-m", "initial commit"], cwd=options.name)

    print(f"Type `cd {options.name}` and run `make` to get started.")


def main() -> int:
    parser = argparse.ArgumentParser(prog="secretary")
    subparsers = parser.add_subparsers(dest="subparser")

    parser_new = subparsers.add_parser("new", help="create new project")
    parser_new.add_argument("--name", type=str, help="project name")
    parser_new.add_argument("--template", type=str, help="template (make/cmake/python)")

    options = parser.parse_args()

    if options.subparser is None:
        parser.print_help(sys.stderr)
        return 1

    ops = {
        "new": new,
    }

    return ops[options.subparser](options)


if __name__ == "__main__":
    raise SystemExit(main())
