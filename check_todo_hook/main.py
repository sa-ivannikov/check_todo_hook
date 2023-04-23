from __future__ import annotations
import argparse
from typing import Sequence

PATTERS = [
    b'TODO:',
    b'FIXME:',
]
LATER_PATTERN = b'--later'

def main(argv: Sequence[str] | None = None):
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*')
    args = parser.parse_args(argv)

    retcode = 0

    for filename in args.filenames:
        with open(filename, 'rb') as inputfile:
            for i, line in enumerate(inputfile, start=1):
                for pattern in PATTERS:
                    if pattern in line:
                        comment = line.split(pattern)[1]
                        if LATER_PATTERN not in comment:
                            print(f'{filename}: {i}: detected {pattern.strip(b":")} ')
                            retcode = 1

    return retcode

if __name__ == '__main__':
    raise SystemExit(main())
