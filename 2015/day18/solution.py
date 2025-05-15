from time import sleep
from typing import List


def build_grid(input_text: str) -> List[List[bool]]:
    grid = []
    for row in input_text.split('\n'):
        grid_row = []
        for light in row:
            grid_row.append(light == '#')
        grid.append(grid_row)
    return grid


directions = [
    (-1, 1),
    (-1, 0),
    (-1, -1),
    (0, 1),
    (0, -1),
    (1, 1),
    (1, 0),
    (1, -1)
]


def neighbors_on(grid: List[List[bool]], r: int, c: int) -> int:
    counter = 0
    for direction in directions:
        rr, cc = direction[0] + r, direction[1] + c
        if 0 <= rr < len(grid) and 0 <= cc < len(grid[r]) and grid[rr][cc]:
            counter += 1

    return counter


def step(grid: List[List[bool]]) -> List[List[bool]]:
    new_grid = []
    for r in range(len(grid)):
        new_grid_row = []
        for c in range(len(grid[r])):
            counter_neighbors_on = neighbors_on(grid, r, c)
            if grid[r][c]:
                new_grid_row.append(counter_neighbors_on in [2, 3])
            else:
                new_grid_row.append(counter_neighbors_on == 3)
        new_grid.append(new_grid_row)
    return new_grid


def counter_lights_on(grid: List[List[bool]]) -> int:
    counter = 0
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c]:
                counter += 1
    return counter


def part1(input_text: str) -> str:
    grid = build_grid(input_text)
    for _ in range(100):
        grid = step(grid)
    return f"lights on: {counter_lights_on(grid)}"

def keep_corners_on(grid: List[List[bool]]):
    ROWS, COLS = len(grid) -1 , len(grid[0])- 1
    grid[0][0] = True
    grid[0][COLS] = True
    grid[ROWS][0] = True
    grid[ROWS][COLS] = True


def part2(input_text: str) -> str:
    grid = build_grid(input_text)
    keep_corners_on(grid)
    for _ in range(100):
        grid = step(grid)
        keep_corners_on(grid)
    return f"lights on: {counter_lights_on(grid)}"
