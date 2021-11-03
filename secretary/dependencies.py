import sys
import shutil

from typing import Iterable


def dynamic_import(path: str, module: str):
    sys.path.append(path)
    return __import__(f"templates.{module}.task", fromlist=[
        "setup",
        "registry",
        "dependencies"
    ])


def check_dependencies(deps: Iterable[str]) -> bool:
    ret = True
    for dep in deps:
        if shutil.which(dep) is None:
            ret = False
            print(f'missing dependency: {dep}')
    return ret
