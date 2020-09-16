import json
from pathlib import Path

from setuptools import find_packages, setup

TOP_DIR = Path(__file__).parent.resolve()

with open(TOP_DIR.joinpath("metadata.json")) as handle:
    METADATA = json.load(handle)

with open(TOP_DIR.joinpath("requirements.txt")) as handle:
    REQUIREMENTS = handle.read()

setup(
    name="aiidalab-optimade",
    version=METADATA["version"],
    license="MIT License",
    author="AiiDAlab Team",
    author_email="aiidalab@materialscloud.org",
    description=METADATA["description"],
    url="https://github.com/aiidalab/aiidalab-optimade",
    packages=find_packages(),
    install_requires=REQUIREMENTS,
)
