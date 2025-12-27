import hashlib
from collections import deque
from typing import List


def get_md5(data: str) -> str:
    return hashlib.md5(data.encode()).hexdigest()


# U for up, D for down, L for left, and R for right
paths = ['U', 'D', 'L', 'R']
path_step = [[0, 1], [0, - 1], [-1, 0], [1, 0]]


def get_open_doors(data: str) -> int:
    md5 = get_md5(data)
    result = 0
    for i in range(4):
        if md5[i] in 'bcdef':
            result += 2 ** (3 - i)
    return result


def get_next_steps(key: str, path: str) -> List[List[int | str]]:
    open_doors = format(get_open_doors(key + path), '04b')
    next_steps = []
    for i in range(len(open_doors)):
        if open_doors[i] == '1':
            next_steps.append([path_step[i][0], path_step[i][1], paths[i]])
    return next_steps


def find_shortest_path(key: str, curr_pos: List[int], goal: List[int]) -> str:
    queue = deque([(curr_pos[0], curr_pos[1], '')])

    while queue:
        x, y, path = queue.popleft()
        if x == goal[0] and y == goal[1]:
            return path
        next_steps = get_next_steps(key, path)
        for dx, dy, next_path in next_steps:
            nx, ny = x + dx, y + dy
            if 0 <= nx <= 3 and 0 <= ny <= 3:
                queue.append((nx, ny, path + next_path))
    return ''

def part1(input_text: str) -> str:
    path = find_shortest_path(input_text, [0, 3], [3, 0])
    return f"shorten path: {path}"


def find_longest_path_steps(key:str, curr_pos: List[int], goal: List[int]) -> int:
    queue = deque([(curr_pos[0], curr_pos[1], '')])
    longest_path = 0

    while queue:
        x, y, path = queue.popleft()
        if x == goal[0] and y == goal[1]:
            longest_path = max(longest_path, len(path))
            continue
        next_steps = get_next_steps(key, path)
        for dx, dy, next_path in next_steps:
            nx, ny = x + dx, y + dy
            if 0 <= nx <= 3 and 0 <= ny <= 3:
                queue.append((nx, ny, path + next_path))

    return longest_path

def part2(input_text: str) -> str:
    steps = find_longest_path_steps(input_text, [0, 3], [3, 0])
    return f"longest steps: {steps}"
