from typing import Generator

from .annotations import Dictionary
from .dictionary import parse_dictionary


def get_string_list(source: str) -> Generator[str, None, None]:
    for s in source.split('\n'):
        if s:
            yield s


def merge(source: str, dictionary: Dictionary) -> str:
    buffer_ = []

    _, dictionary_origin = parse_dictionary(source)
    string_list = get_string_list(source)

    for i in string_list:
        buffer_.append(i)
        buffer_.append('\n')

        if i in dictionary_origin:
            buffer_.append(dictionary_origin[i])
        elif i in dictionary:
            buffer_.append(dictionary[i])

        buffer_.append('\n\n\n')

    return ''.join(buffer_)
