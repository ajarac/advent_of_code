from typing import List


def parse(input_text):
    return [int(value) for value in input_text.split('\n')]


def dfs(containers: List[int], index: int, remaining_liters: int) -> int:
    if remaining_liters < 0:
        return 0
    if remaining_liters == 0:
        return 1
    if len(containers) == index:
        return 0

    return (dfs(containers, index + 1, remaining_liters - containers[index]) +
            dfs(containers, index + 1, remaining_liters))


def dfs_counter(containers: List[int], index: int, remaining_liters: int, counter: int,
                counter_map: dict[int, int]):
    if remaining_liters < 0:
        return None
    if remaining_liters == 0:
        if counter not in counter_map:
            counter_map[counter] = 0
        counter_map[counter] += 1
        return None
    if len(containers) == index:
        return None

    dfs_counter(containers, index + 1, remaining_liters - containers[index], counter + 1, counter_map)
    dfs_counter(containers, index + 1, remaining_liters, counter, counter_map)
    return None


def part1(input_text: str) -> str:
    containers = parse(input_text)
    combinations = dfs(containers, 0, 150)
    return f"combinations: {combinations}"


def part2(input_text: str) -> str:
    containers = parse(input_text)
    counter_map = {}
    dfs_counter(containers, 0, 150, 0, counter_map)
    min_containers = len(containers)
    for num in counter_map:
        min_containers = min(min_containers, num)
    return f"minimum containers counter combinations: {counter_map[min_containers]}"
