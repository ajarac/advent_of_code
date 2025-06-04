from collections import defaultdict
from typing import List


def build_map(input_text: str) -> List[dict[str, int]]:
    words = input_text.split('\n')
    list_counters = []
    for _ in range(len(words[0])):
        list_counters.append(defaultdict(lambda: 0))

    for word in words:
        for i, c in enumerate(word):
            list_counters[i][c] += 1

    return list_counters


def get_most_common(counter: dict[str, int]) -> str:
    current_char = ''

    for char in counter:
        if current_char in counter:
            if counter[current_char] < counter[char]:
                current_char = char
        else:
            current_char = char

    return current_char

def get_least_common(counter: dict[str, int]) -> str:
    current_char = ''


    for char in counter:
        if current_char in counter:
            if counter[current_char] > counter[char]:
                current_char = char
        else:
            current_char = char

    return current_char

def part1(input_text: str) -> str:
    counter_map = build_map(input_text)
    message = ""
    for counter in counter_map:
        message += get_most_common(counter)
    return message


def part2(input_text: str) -> str:
    counter_map = build_map(input_text)
    message = ""
    for counter in counter_map:
        message += get_least_common(counter)
    return message
