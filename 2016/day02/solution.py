from typing import List

directions = {
    'U': (-1, 0),
    'L': (0, -1),
    'R': (0, 1),
    'D': (1, 0)
}


def get_code(key_pad: List[List[str]], position: tuple[int, int], instructions_group: List[str]) -> str:
    code = ""
    for instructions in instructions_group:
        for instruction in instructions:
            direction = directions[instruction]
            row = position[0] + direction[0]
            colum = position[1] + direction[1]
            if 0 <= row < len(key_pad) and 0 <= colum < len(key_pad[0]) and key_pad[row][colum] != '':
                position = (row, colum)
        code += key_pad[position[0]][position[1]]
    return code


def part1(input_text: str) -> str:
    key_pad = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
    code = get_code(key_pad, (1, 1), input_text.split('\n'))
    return f"code {code}"

def part2(input_text: str) -> str:
    key_pad = [
        ['', '', '1', '', ''],
        ['', '2', '3', '4', ''],
        ['5', '6', '7', '8', '9'],
        ['', 'A', 'B', 'C', ''],
        ['', '', 'D', '', ''],
    ]
    code = get_code(key_pad, (2, 0), input_text.split('\n'))
    return f"code {code}"
