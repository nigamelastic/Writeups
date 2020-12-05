filename = "input.txt"

import os.path
from typing import Iterable

def load_input_file() -> Iterable[str]:
    input_file = os.path.join(os.path.dirname(__file__), 'input.txt')
    with open(input_file) as fd:
        return map(str.strip, fd.readlines())


def find_empty_seat(boarding_passes: Iterable[str]) -> int:
    ids = map(decode_boarding_pass_id, boarding_passes)
    ids = iter(sorted(ids))
    prev_seat = next(ids)
    while True:
        expected = prev_seat + 1
        next_seat = next(ids)
        if next_seat != expected:
            return expected
        prev_seat = next_seat


CODE_TRANS = str.maketrans('FBLR', '0101')


def decode_boarding_pass_id(code: str) -> int:
    """
    Extract the ID from a boarding pass code.
    """
    bincode = code.translate(CODE_TRANS)
    return int(bincode, 2)

boarding_passes = load_input_file()
print(find_empty_seat(boarding_passes))

