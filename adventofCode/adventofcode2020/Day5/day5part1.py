filename = "input.txt"
sumValue = 2020
import os.path
from typing import Iterable

def load_input_file() -> Iterable[str]:
    input_file = os.path.join(os.path.dirname(__file__), 'input.txt')
    with open(input_file) as fd:
        return map(str.strip, fd.readlines())


def find_highest_boarding_pass_id(boarding_passes: Iterable[str]) -> int:
    ids = map(decode_boarding_pass_id, boarding_passes)
    return max(ids)


CODE_TRANS = str.maketrans('FBLR', '0101')


def decode_boarding_pass_id(code: str) -> int:
    
    bincode = code.translate(CODE_TRANS)
    return int(bincode, 2)

boarding_passes = load_input_file()
print(find_highest_boarding_pass_id(boarding_passes))