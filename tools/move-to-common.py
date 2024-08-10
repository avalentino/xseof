#!/usr/bin/env python3

import pathlib
import argparse


BLACKLIST = (
    "*/__init__.py",
    "*/eo_*.py",
)


OVERWRITE_PATTERNS = (
    "xseof/int_attref/time_types_0101.py",
    "xseof/int_attref/time_types_0102.py",
    "xseof/int_attref/time_types_0200.py",
    "xseof/int_attref/time_types_0201.py",
    "xseof/int_attref/time_types_0300.py",
)

RELAXCHECKS = (
    "*/time_types_*.py",
)


def move_to_common(
    root, blacklist=BLACKLIST, overwrite_patterns=OVERWRITE_PATTERNS,
    relaxcheck=RELAXCHECKS,
):
    root = pathlib.Path(root)
    substitutions = {}
    for filename in root.glob("*.py"):
        if any(filename.match(pattern) for pattern in blacklist):
            continue
        substitutions[f" .{filename.stem}"] = f" ..common.{filename.stem}"
        new_path = filename.parent.parent.joinpath("common", filename.name)
        overwrite = any(
            filename.match(pattern) for pattern in overwrite_patterns
        )
        if new_path.exists() and not overwrite:
            common_data = new_path.read_text()
            data = filename.read_text()
            skipcheck = any(filename.match(pattern) for pattern in relaxcheck)
            if data != common_data and not skipcheck:
                raise RuntimeError(
                    f"modules with the same name have different content: "
                    f"'{filename}', '{new_path}'"
                )
            filename.unlink()
        else:
            print(f"move: {str(filename)!r} --> {str(new_path)!r}")
            if new_path.exists():
                new_path.unlink()  # compatibility with windows
            filename.rename(new_path)

    for filename in root.glob("*.py"):
        data = filename.read_text()
        for old, new in substitutions.items():
            data = data.replace(old, new)
        filename.write_text(data)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('root')

    args = parser.parse_args()
    return move_to_common(args.root)


if __name__ == "__main__":
    import sys
    sys.exit(main())
