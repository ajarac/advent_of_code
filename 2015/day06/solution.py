from typing import List


class Operation:
    def __init__(self, op: str, start: (int, int), end: (int, int)):
        self.op = op
        self.start = start
        self.end = end

    def __str__(self):
        return f"{self.op} from: {self.start} to: {self.end}"


def part1(input_text: str) -> str:
    grid = [[0 for _ in range(1000)] for _ in range(1000)]

    for instruction in input_text.split('\n'):
        operation = get_operation(instruction)
        execute1(grid, operation)
    lights = count_lights(grid)
    return f"lights on: {lights}"


def part2(input_text: str) -> str:
    grid = [[0 for _ in range(1000)] for _ in range(1000)]

    for instruction in input_text.split('\n'):
        operation = get_operation(instruction)
        execute2(grid, operation)
    lights = count_lights(grid)
    return f"counter brightness: {lights}"


def count_lights(grid: List[List[int]]) -> int:
    counter = 0
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            counter += grid[i][j]

    return counter


def execute1(grid: List[List[int]], operation: Operation):
    for i in range(operation.start[0], operation.end[0] + 1):
        for j in range(operation.start[1], operation.end[1] + 1):
            if operation.op == 'on':
                grid[i][j] = 1
            elif operation.op == 'off':
                grid[i][j] = 0
            else:
                grid[i][j] = 1 if grid[i][j] == 0 else 0


def execute2(grid: List[List[int]], operation: Operation):
    for i in range(operation.start[0], operation.end[0] + 1):
        for j in range(operation.start[1], operation.end[1] + 1):
            if operation.op == 'on':
                grid[i][j] += 1
            elif operation.op == 'off':
                grid[i][j] = max(grid[i][j] - 1, 0)
            else:
                grid[i][j] += 2


def get_operation(input: str) -> Operation:
    parts = input.split('through')
    first_part = parts[0].strip().split(' ')
    if len(first_part) == 3:
        op = first_part[1]
    else:
        op = first_part[0]
    start_part = first_part[-1].strip().split(',')
    start = (int(start_part[0]), int(start_part[1]))
    end_part = parts[1].strip().split(',')
    end = (int(end_part[0]), int(end_part[1]))
    return Operation(op, start, end)
