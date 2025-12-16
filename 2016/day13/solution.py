from collections import deque
from typing import List

next_positions = [[1, 0], [0, 1], [-1, 0], [0, -1]]


def is_open(x: int, y: int, favourite: int) -> bool:
    value = x * x + 3 * x + 2 * x * y + y + y * y + favourite
    return bin(value).count('1') % 2 == 0


def calculate_steps(favourite: int, goal: List[int]) -> int:
    queue = deque([(1, 1, 0)])  # (x, y, steps)
    visited = set()
    visited.add((1, 1))

    while queue:
        x, y, steps = queue.popleft()

        if x == goal[0] and y == goal[1]:
            return steps

        for dx, dy in next_positions:
            nx, ny = x + dx, y + dy
            if nx >= 0 and ny >= 0 and (nx, ny) not in visited and is_open(nx, ny, favourite):
                visited.add((nx, ny))
                queue.append((nx, ny, steps + 1))

    return -1


def part1(input_text: str) -> str:
    input_data = input_text.split('\n')
    favourite = int(input_data[0])
    goal = [int(x) for x in input_data[1].split(',')]
    steps = calculate_steps(favourite, goal)
    return f"min steps: {steps}"


def calculate_distinct_locations(favourite: int, max_steps: int) -> int:
    queue = deque([(1, 1, 0)])  # (x, y, steps)
    visited = {(1, 1)}

    while queue:
        x, y, steps = queue.popleft()

        if steps >= max_steps:
            continue

        for dx, dy in next_positions:
            nx, ny = x + dx, y + dy
            if nx >= 0 and ny >= 0 and (nx, ny) not in visited and is_open(nx, ny, favourite):
                visited.add((nx, ny))
                queue.append((nx, ny, steps + 1))

    return len(visited)


def part2(input_text: str) -> str:
    favourite = int(input_text.split('\n')[0])
    steps = calculate_distinct_locations(favourite, 50)
    return f"distinct locations: {steps}"
