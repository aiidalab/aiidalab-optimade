import json
from pathlib import Path

from setuptools import find_packages, setup

TOP_DIR = Path(__file__).parent.resolve()

with open(TOP_DIR.joinpath("metadata.json")) as handle:
    METADATA = json.load(handle)

setup(
    name="aiidalab-optimade",
    version=METADATA["version"],
    license="MIT License",
    author="AiiDAlab Team",
    description=METADATA["description"],
    url="https://github.com/aiidalab/aiidalab-optimade",
    packages=find_packages(),
    install_requires=["optimade-client~=2020.9"],
)
