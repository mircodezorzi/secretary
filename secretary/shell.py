import subprocess
import shutil


def run_shell(cmd: list[str], cwd: str = "", silent: bool = False) -> None:
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
        ["find", path, "-type", "f", "-exec", "sed", "-i", f"s/{pattern}/{repl}/g", "{}", "+"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )


def copy(src: str, dst: str, symlinks: bool = False, ignore: bool = None):
    shutil.copytree(src, dst, symlinks, ignore)


def remove(path: str):
    shutil.rmtree(path)
