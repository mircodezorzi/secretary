from dataclasses import dataclass
from typing import Iterable

import PyInquirer


@dataclass
class Option:
    option: any
    result: any
    depends_on: str


def option(t: str, name: str, items: Iterable[any], depends_on: str = '') -> Option:
    return Option(
        option={
            'type': t,
            'name': name,
            'message': name,
            'choices': items,
        },
        result={},
        depends_on=depends_on
    )


def checkbox(name: str, items: Iterable[str], depends_on: str = '') -> Option:
    return option('checkbox', name, list({'name': i} for i in items), depends_on)


def choice(name: str, items: Iterable[str], depends_on: str = '') -> Option:
    return option('list', name, items, depends_on)


def prompt(options: any) -> any:
    prev = None

    for opt in options:
        if prev and opt.depends_on:
            key, values = list(prev.items())[0]
            if opt.depends_on not in [f'{key}.{value}' for value in values]:
                continue
        result = PyInquirer.prompt(opt.option)
        prev = opt.result = result

    return opt
