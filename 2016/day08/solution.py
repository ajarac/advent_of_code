from typing import List

WIDE = 50
TALL = 6


def print_screen(screen: List[List[str]]):
    for row in screen:
        print("".join(row))


def parse_instruction(input_row: str) -> (str, int, int):
    if "rect" in input_row:
        v1, v2 = input_row.split(' ')[1].split('x')
        return 'rect', int(v1), int(v2)

    tokens = input_row.split(' ')
    v1 = int(tokens[2].split('=')[1])
    v2 = int(tokens[4])
    return tokens[1], v1, v2


def build_screen() -> List[List[str]]:
    screen = []
    for _ in range(TALL):
        row = []
        for _ in range(WIDE):
            row.append('.')
        screen.append(row)
    return screen


def turn_on(screen: List[List[str]], x: int, y: int):
    for r in range(y):
        for c in range(x):
            screen[r][c] = '#'


def rotate_column(screen: List[List[str]], column: int, by: int):
    old_column = [screen[r][column] for r in range(TALL)]
    for row in range(TALL):
        new_index = (row + by) % TALL
        screen[new_index][column] = old_column[row]


def rotate_row(screen: List[List[str]], row: int, by: int):
    old_row = [screen[row][c] for c in range(WIDE)]
    for column in range(WIDE):
        new_index = (column + by) % WIDE
        screen[row][new_index] = old_row[column]


def apply_instruction(screen: List[List[str]], instruction: (str, int, int)):
    operation, v1, v2 = instruction

    match operation:
        case 'rect':
            turn_on(screen, v1, v2)
        case 'column':
            rotate_column(screen, v1, v2)
        case 'row':
            rotate_row(screen, v1, v2)

def count_lit_pixels(screen: List[List[str]]) -> int:
    counter = 0
    for row in range(len(screen)):
        for column in range(len(screen[row])):
            if screen[row][column] == '#':
                counter += 1
    return counter


def get_display(input_text: str) -> List[List[str]]:
    screen = build_screen()
    for input_row in input_text.split('\n'):
        instruction = parse_instruction(input_row)
        apply_instruction(screen, instruction)
    return screen


def part1(input_text: str) -> str:
    screen = get_display(input_text)
    pixels_lit = count_lit_pixels(screen)
    return f"pixels lit: {pixels_lit}"


def part2(input_text: str) -> str:
    screen = get_display(input_text)
    print_screen(screen)
    return ""
