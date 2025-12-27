from typing import List

list_match_traps = ['^^.', '.^^', '..^', '^..']


def is_trap(prev_row, index: int) -> bool:
    row = '.' + prev_row + '.'
    i = index + 1
    prev_traps = row[i - 1:i + 2]
    return prev_traps in list_match_traps


def get_next_row(row: str) -> str:
    new_row = ''
    for i in range(len(row)):
        if is_trap(row, i):
            new_row += '^'
        else:
            new_row += '.'
    return new_row


def generate_grid(first_row: str, num_rows: int) -> List[str]:
    grid = [first_row]
    while len(grid) < num_rows:
        grid.append(get_next_row(grid[-1]))

    return grid


def count_safe_tiles(grid: List[str]) -> int:
    count = 0
    for row in grid:
        count += row.count('.')
    return count


def part1(input_text: str) -> str:
    row, num_rows = input_text.split('\n')
    grid = generate_grid(row, int(num_rows))
    print("\n".join(grid))
    return f"safe tiles: {count_safe_tiles(grid)}"


def part2(input_text: str) -> str:
    row, num_rows = input_text.split('\n')
    grid = generate_grid(row, int(num_rows) * 10000)
    return f"safe tiles: {count_safe_tiles(grid)}"
