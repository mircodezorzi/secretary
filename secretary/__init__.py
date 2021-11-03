from .shell import run_shell, replace, copy, remove
from .prompt import checkbox, choice, prompt
from .component import shard, component, registry

__author__ = "Mirco De Zorzi (mircodezorzi@gmail.com)"
__version__ = "0.0.1"
__copyright__ = "Copyright (c) 2021-2021 Mirco De Zorzi"
__licence__ = "MIT"

__all__ = (
    # Shell utilities
    "run_shell", "replace", "copy", "remove",

    # Prompt utilities
    "checkbox", "choice", "prompt",

    # Component Registry
    "shard", "component", "registry",
)
