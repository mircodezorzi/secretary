from secretary import replace, run_shell
from secretary import checkbox, choice, prompt
from secretary import shard, component, registry


r = registry()
r.register(component('header', [
    shard('src/{0}.c', '#include "{0}.h"'),
    shard('include/{0}.h', '#ifndef __{0:u}_H__\n#define __{0:u}_H__\n\n\n#endif /* __{0:u}_H__ */'),
]))


dependencies = [
    'ccache',
    'clang',
    'make',
]

choices = [
    choice('compiler', [
        'gcc',
        'clang',
    ]),
    checkbox('toolchain', [
        'ccache',
        'pre-commit'
    ]),
    checkbox('pre-commit hooks', [
        'clang-format',
        'clang-tidy',
        'oclint',
        'uncrustify',
        'cppcheck',
        'cpplint',
        'include-what-you-use',
    ], depends_on='toolchain.pre-commit'),
]


def registry():
    return r


def setup(options):
    # prompt(choices)

    replace('<NAME>', options.name, options.name)
    replace('<COMPILER>', 'gcc', options.name)

    run_shell(["pre-commit", "install"], cwd=options.name)
    run_shell(["pre-commit", "autoupdate"], cwd=options.name)

    run_shell(["make", "compile_commands"], cwd=options.name)
