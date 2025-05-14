from itertools import permutations
from typing import List


def part1(input_text: str) -> str:
    hash_map = build_tree(input_text)
    max_happiness = calculate_total_happiness(hash_map)
    return f"max happiness: {max_happiness}"


def part2(input_text: str) -> str:
    hash_map = build_tree(input_text)
    hash_map = add_me(hash_map)
    max_happiness = calculate_total_happiness(hash_map)
    return f"max happiness: {max_happiness}"

def calculate_total_happiness(hash_map: dict[str, dict[str, int]]) -> int:
    max_happiness = float('-inf')
    for group in permutations(hash_map.keys()):
        max_happiness = max(max_happiness, calculate_happiness(hash_map, list(group)))
    return max_happiness

def calculate_happiness(hash_map: dict[str, dict[str, int]], group: List[str]) -> int:
    total = 0
    for i in range(len(group)):
        left = group[i]
        right = group[(i + 1) % len(group)]  # circular
        total += hash_map[left][right] + hash_map[right][left]
    return total

def build_tree(input_text: str) -> dict[str, dict[str, int]]:
    hash_map = {}
    for row in input_text.split('\n'):
        parts = row.split(' ')
        person1 = parts[0]
        operator = parts[2]
        num = parts[3]
        person2 = parts[10]
        if person1 not in hash_map:
            hash_map[person1] = {}
        person2_sanitized = person2.split('.')[0]
        signal = 1
        if operator == 'lose':
            signal = -1
        hash_map[person1][person2_sanitized] = int(num) * signal

    return hash_map

def add_me(hash_map: dict[str, dict[str, int]]) -> dict[str, dict[str, int]]:
    me = 'ME'
    persons = hash_map.keys()
    hash_map[me] = {}
    for person in persons:
        hash_map[person][me] = 0
        hash_map[me][person] = 0
    return hash_map

