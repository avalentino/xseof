#!/usr/bin/env python3

import pathlib
import argparse


def fix_names(root):
    root = pathlib.Path(root)
    substitutions = {}
    for filename in root.glob("*_xsd.py"):
        new_name = filename.stem.removesuffix("_xsd")
        substitutions[filename.stem] = new_name
        new_name = filename.parent / (new_name + ".py")
        print(f"Rename: {str(filename)!r} --> {str(new_name)!r}")
        filename.rename(new_name)

    for filename in root.glob("*.py"):
        data = filename.read_text()
        for old, new in substitutions.items():
            data = data.replace(old, new)
        filename.write_text(data)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('root')

    args = parser.parse_args()
    return fix_names(args.root)


if __name__ == "__main__":
    import sys
    sys.exit(main())
