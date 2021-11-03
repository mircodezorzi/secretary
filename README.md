# `secretary`

Scaffolding framework written in Python.

# Installation

```bash
$ git clone https://github.com/mircodezorzi/secretary
$ cd secretary
$ pip install .
```

# Usage
Create new project
```bash
$ secretary create foobar
```

Add component to existining project
```bash
$ cd foobar
$ secretary add header foobar
```
This will generate a `include/foobar.h` and `src/foobar.c`.
For more look into `templates/*/field.py`.

# Templates
- make (C)
	- Toolchain: Make, ccache, gcc/clang
- cmake (C++ 20)
	- Toolchain: g++, ninja, cmake, clang-format, ccache, g++/clang++
- conan (C++ 20)
	- Toolchain: g++, ninja, cmake, conan clang-format, ccache, g++/clang++
