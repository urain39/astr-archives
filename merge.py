import sys

from pathlib import Path
from typing import List
from tools.dictionary import parse_dictionary
from tools.merger import merge


def main(argv: List[str]) -> None:
    argc = len(argv)

    if argc < 3:
        print('Usage: python merge.py <dictionary1> <dictionary2, dictionary3, ...>')

        sys.exit(1)

    _, main_dict = parse_dictionary(Path(argv[1]).read_text())

    def apply_(filename: str) -> None:
        file_ = Path(filename)
        source = file_.read_text()

        file_.write_text(
            merge(source, main_dict)
        )

    list(map(apply_, argv[2:]))


if __name__ == '__main__':
    main(sys.argv)
