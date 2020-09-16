import json
from pathlib import Path

from .widget import OptimadeQueryWidget


__all__ = ("OptimadeQueryWidget",)

TOP_DIR = Path(__file__).parent.parent.resolve()
with open(TOP_DIR.joinpath("metadata.json")) as handle:
    METADATA = json.load(handle)
__version__ = METADATA["version"]
