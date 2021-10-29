import subprocess
import shutil


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
        ["find", path, "-type", "f", "-exec", "sed", "-i", f"s/{pattern}/{repl}/g", "{}", "+"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )


def copy(src: str, dst: str):
    shutil.copytree(src, dst)


def remove(path: str):
    shutil.rmtree(path)
