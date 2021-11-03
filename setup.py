import os
import shutil
from pathlib import Path

import setuptools

secretary_path = os.environ["HOME"] + "/.secretary"


setuptools.setup(
    name="secretary",
    version="0.1.0",
    description="Python scaffolding framework.",
    author="Mirco De Zorzi",
    author_email="mircodezorzi@protonmail.com",
    url="https://github.com/mircodezorzi/secretary",
    license="MIT",
    packages=["secretary"],
    entry_points={
        "console_scripts": ["secretary=secretary.__main__:main"],
    },
    include_package_data=True,
    package_data={},
    install_requires=[
        "argparse",
        "PyInquirer",
    ],
)

shutil.copytree(
    f"{Path('./').resolve()}/templates",
    f"{secretary_path}/templates",
    dirs_exist_ok=True,
)
