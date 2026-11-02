#!/usr/bin/env python3

"""Return error code if duplicate slugs are found.

Author: Jochen Kupperschmidt
License: MIT
"""

from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
import sys
import tomllib


@dataclass(frozen=True, slots=True)
class Data:
    path: Path
    slug: str


def main(filenames: list[str]) -> None:
    if not filenames:
        return

    paths = map(Path, filenames)
    datas = map(load_data, paths)

    slugs_to_paths: dict[str, list[Path]] = defaultdict(list)
    for data in datas:
        slugs_to_paths[data.slug].append(data.path)

    duplicate_slugs_to_paths = {
        slug: paths for slug, paths in slugs_to_paths.items() if len(paths) > 1
    }

    if duplicate_slugs_to_paths:
        print_duplicate_slugs(duplicate_slugs_to_paths)
        sys.exit(1)
    else:
        print('No duplicate slugs found.')


def load_data(path: Path) -> Data:
    toml = path.read_text()
    data = tomllib.loads(toml)

    return Data(
        path=path,
        slug=data['slug'],
    )


def print_duplicate_slugs(
    duplicate_slugs_to_paths: dict[str, list[Path]],
) -> None:
    write_error_line('Found duplicate slugs:')
    for slug, paths in duplicate_slugs_to_paths.items():
        write_error_line(f'+ Slug "{slug}" appears in multiple files:')
        for path in sorted(paths):
            write_error_line(f'  - file: {path}')


def write_error_line(text: str) -> None:
    sys.stderr.write(f'{text}\n')


if __name__ == '__main__':
    filenames = sys.argv[1:]
    main(filenames)
