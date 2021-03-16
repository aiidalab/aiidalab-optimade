import json
from pathlib import Path
import re
import sys
from typing import Tuple

from invoke import task


TOP_DIR = Path(__file__).parent.resolve()


def update_file(filename: str, sub_line: Tuple[str, str], strip: str = None):
    """Utility function for tasks to read, update, and write files"""
    with open(filename, "r") as handle:
        lines = [
            re.sub(sub_line[0], sub_line[1], line.rstrip(strip)) for line in handle
        ]

    with open(filename, "w") as handle:
        handle.write("\n".join(lines))
        handle.write("\n")


@task
def update_version(_, version=""):
    """Update package version to given version"""
    if version:
        if version.startswith("v"):
            version = version[1:]
        if re.match(r"[0-9]+(\.[0-9]+){2}.*", version) is None:
            sys.exit(
                f"Error: Passed version ({version}) does adhere to SemVer standards."
            )
    else:
        sys.exit("Error: version not supplied. It should adhere to SemVer standards.")

    update_file(
        TOP_DIR.joinpath("metadata.json"), (r'"version": ".+"', f'"version": "{version}"')
    )

    with open(TOP_DIR / "metadata.json") as handle:
        metadata: dict = json.load(handle)
    with open(TOP_DIR / "requirements.txt") as handle:
        for line in handle.readlines():
            optimade_req = re.match(r"^optimade-client~=(.*)$", line)
            if optimade_req is not None:
                optimade_req = optimade_req.group(0)
                break
        else:
            sys.exit("Error: Could not find 'optimade-client' dependency in 'requirements.txt' !")

    if f">={version}" in metadata.get("requires", {}).keys():
        # This version is - for some reason - already in the "requires" dict
        print(
            f"Bumped version to {version} !\nNote: >={version} was already found in "
            "metadata.requires."
        )
        sys.exit()

    latest_requires = sorted(metadata.get("requires", {}).keys())[-1]
    if latest_requires > f">={version}":
        # The found latest "requires" key is a later version that the currently supplied
        print(
            f"Bumped version to {version} !\nNote: The current version is lower than the latest "
            "in metadata.requires, so nothing has been done extra."
        )
        sys.exit()

    extra_print = f"\nNo new addition to metadata.requires as optimade-client has not been updated."
    if optimade_req not in metadata.get("requires", {}).get(latest_requires, []):
        # New "requires" entry will be added
        metadata["requires"].update(
            {f">={version}": [optimade_req]}
        )
        with open(TOP_DIR / "metadata.json", "w") as handle:
            json.dump(metadata, handle, indent=4)
            handle.write("\n")
        extra_print = f"\nAdded new >={version} key to metadata.requires."

    print(f"Bumped version to {version} !{extra_print}")
