def part1(input_text: str) -> str:
    floor = 0
    for char in input_text:
        if char == '(':
            floor += 1
        elif char == ')':
            floor -= 1
    return f"floor: {floor}"


def part2(input_text: str) -> str:
    floor = 0
    index = 0
    for i, char in enumerate(input_text):
        if char == '(':
            floor += 1
        elif char == ')':
            floor -= 1
        if floor == -1:
            index = i + 1
            break
    return f"index: {index}"
