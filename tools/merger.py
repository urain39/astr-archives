import re

from typing import Generator
from .annotations import Dictionary
from .dictionary import parse_dictionary


_RE_STRING = re.compile(r'([^\n]+)(?:\n[^\n]+)?', re.MULTILINE)


def get_string_list(source: str) -> Generator[str, None, None]:
    for s in _RE_STRING.findall(source):
        yield s


def merge(source: str, dictionary: Dictionary) -> str:
    buffer_ = []

    string_list = get_string_list(source)
    _, dictionary_origin = parse_dictionary(source)

    for i in string_list:
        buffer_.append(i)
        buffer_.append('\n')

        if i in dictionary_origin:
            buffer_.append(dictionary_origin[i])
        elif i in dictionary:
            buffer_.append(dictionary[i])

        buffer_.append('\n\n\n')

    return ''.join(buffer_)
