#!/usr/bin/env python3

import argparse
import json
import os
import sys

from PyInquirer import prompt

from .shell import copy, remove, run_shell
from .formatter import fmt
from .dependencies import dynamic_import, check_dependencies


secretary_path = os.environ["HOME"] + "/.secretary"


def templates():
    return [{
        "type": "list",
        "name": "templates",
        "message": "choose a template",
        "choices": os.listdir(f"{secretary_path}/templates"),
    }]


def create(options) -> int:
    """Create new project from scaffold."""

    if not options.template:
        answers = prompt(templates())
        options.template = answers["templates"]

    if os.path.exists(options.name):
        print("Project already exists. Aborting...")
        return 1

    try:
        print("Copying all files...")
        copy(
            f"{secretary_path}/templates/{options.template}/files",
            options.name,
        )

        print("Taking a short coffee break...")
        cmd = dynamic_import(secretary_path, options.template)
        if not check_dependencies(cmd.dependencies):
            return 1
        cmd.setup(options)

        print("Initializing git repository...")
        run_shell(["git", "init"], cwd=options.name)
        run_shell(["git", "add", "."], cwd=options.name)
        run_shell(["git", "commit", "-m", "initial commit"], cwd=options.name)

        with open(f'{options.name}/.secretaryrc', 'w') as f:
            f.write(json.dumps({
                'template': options.template
            }, indent=2))


        print(f"Type `cd {options.name}` and run `make` to get started.")
    except Exception as e:
        print('An error has occured while creating the project!')
        remove(options.name)


def add(options) -> int:
    with open('.secretaryrc', 'r') as f:
        data = json.loads(f.read())
    cmd = dynamic_import(data['template'])

    component = cmd.registry().components[options.component]
    for shard in component.shards:
        path = shard.path.format(options.name)
        with open(path, 'w') as f:
            content = fmt.format(shard.content, options.name)
            f.write(content)

    return 0


def main() -> int:
    parser = argparse.ArgumentParser(prog="secretary")
    subparsers = parser.add_subparsers(dest="subparser")

    parser_create = subparsers.add_parser(
        "create", help="create from scaffold"
    )
    parser_create.add_argument("name", type=str, help="project name")
    parser_create.add_argument("--template", type=str, help="template")

    parser_add = subparsers.add_parser(
        "add", help="add component to project"
    )
    parser_add.add_argument("component", type=str, help="component")
    parser_add.add_argument("name", type=str, help="name")

    options = parser.parse_args()

    if options.subparser is None:
        parser.print_help(sys.stderr)
        return 1

    ops = {
        "create": create,
        "add": add,
    }

    return ops[options.subparser](options)


if __name__ == "__main__":
    raise SystemExit(main())
