#!/usr/bin/env python3

from PyInquirer import prompt, style_from_dict, Token

from secretary import run_shell, copy, remove

import argparse
import os
import sys


style = style_from_dict({
    Token.QuestionMark: '#E91E63 bold',
    Token.Selected: '#673AB7 bold',
    Token.Instruction: '',
    Token.Answer: '#2196f3 bold',
    Token.Question: '',
})


def dynamic_import(module: str):
    return __import__(f"templates.{module}.task", fromlist=["setup"])


def templates():
    return [
        {
            'type': 'list',
            'name': 'templates',
            'message': 'choose a template',
            'choices': os.listdir('templates'),
        }
    ]


def create(options) -> int:
    """Create new project from scaffold."""

    if not options.template:
        answers = prompt(templates(), style=style)
        options.template = answers['templates']

    try:
        if os.path.exists(options.name):
            print("Project already exists. Aborting...")
            return 1

        print("Copying all files...")
        copy(f"templates/{options.template}/files", options.name)

        print("Taking a short coffee break...")
        cmd = dynamic_import(options.template)
        cmd.setup(options)

        print("Initializing git repository...")
        run_shell(["git", "init"], cwd=options.name)
        run_shell(["git", "add", "."], cwd=options.name)
        run_shell(["git", "commit", "-m", "initial commit"], cwd=options.name)

        print(f"Type `cd {options.name}` and run `make` to get started.")
    except Exception:
        remove(options.name)


def main() -> int:
    parser = argparse.ArgumentParser(prog="secretary")
    subparsers = parser.add_subparsers(dest="subparser")

    parser_create = subparsers.add_parser("create", help="create from scaffold")
    parser_create.add_argument("--name", type=str, help="project name")
    parser_create.add_argument("--template", type=str, help="template")

    options = parser.parse_args()

    if options.subparser is None:
        parser.print_help(sys.stderr)
        return 1

    ops = {
        "create": create,
    }

    return ops[options.subparser](options)


if __name__ == "__main__":
    raise SystemExit(main())
