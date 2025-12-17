# Create an md5 hash object
import hashlib
from typing import Optional

hash_map = dict()

def get_md5(data: str) -> str:
    return hashlib.md5(data.encode()).hexdigest()

def get_md5_times(data: str, md5_times: int) -> str:
    original_data = data
    if original_data in hash_map:
        return hash_map[data]
    for i in range(md5_times):
        data = get_md5(data)
    hash_map[original_data] = data
    return data


def find_triple(input_data: str, index: int, md5_times: int) -> Optional[str]:
    data = get_md5_times(input_data + str(index), md5_times)
    for i in range(2, len(data)):
        if data[i - 2] == data[i - 1] == data[i]:
            return data[i]
    return None


def is_valid_next_1000(input_data: str, index: int, triple: str, md5_times: int) -> bool:
    should_contain = triple[0] * 5
    for i in range(index + 1, index + 1000):
        data = get_md5_times(input_data + str(i), md5_times)
        if data.__contains__(should_contain):
            return True

    return False


def is_valid_key(input_data: str, index: int, md5_times: int = 1) -> bool:
    triple = find_triple(input_data, index, md5_times)
    if triple is None:
        return False
    return is_valid_next_1000(input_data, index, triple, md5_times)


def part1(input_text: str) -> str:
    hash_map.clear()
    i = 0
    counter = 0
    while counter < 64:
        if is_valid_key(input_text, i, 1):
            counter += 1
        i += 1
    return f"64th key in index {i - 1}"


def part2(input_text: str) -> str:
    hash_map.clear()
    i = 0
    counter = 0
    while counter < 64:
        if is_valid_key(input_text, i, 2017):
            counter += 1
        i += 1
    return f"64th key in index {i - 1}"
