import sys
from itertools import permutations


def parse(input_text: str) -> dict[str, dict[str, int]]:
    hash_map = {}
    for row in input_text.split('\n'):
        tokens = row.split('=')
        cities = tokens[0].split(' ')
        city1 = cities[0]
        city2 = cities[2]
        distance = int(tokens[1].strip())
        if city1 not in hash_map:
            hash_map[city1] = {}
        hash_map[city1][city2] = distance
        if city2 not in hash_map:
            hash_map[city2] = {}
        hash_map[city2][city1] = distance
    return hash_map


def calculate_path_distance(path, distances):
    total = 0
    for i in range(len(path) - 1):
        total += distances[path[i]][path[i + 1]]
    return total


def part1(input_text: str) -> str:
    distances = parse(input_text)
    cities = list(distances.keys())
    min_distance = float('inf')
    for path in permutations(cities):
        min_distance = min(min_distance, calculate_path_distance(path, distances))
    return f"Minimal distance: {min_distance}"


def part2(input_text: str) -> str:
    distances = parse(input_text)
    cities = list(distances.keys())
    min_distance = 0
    for path in permutations(cities):
        min_distance = max(min_distance, calculate_path_distance(path, distances))
    return f"Maximum distance: {min_distance}"
