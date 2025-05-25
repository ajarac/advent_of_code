directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
map_instruction = {'R': 1, 'L': -1}

def part1(input_text: str) -> str:
    position = (0, 0)
    instructions = input_text.split(',')
    index = 0
    for instruction in instructions:
        trim = instruction.strip()
        direction, steps = trim[0], int(trim[1:])
        index = (index + map_instruction[direction]) % len(directions)
        step_direction = directions[index]
        position = (position[0] + step_direction[0] * steps, position[1] + step_direction[1] * steps)
    distance = abs(position[0]) + abs(position[1])
    return f"distance: {distance}"


def part2(input_text: str) -> str:
    position = (0, 0)
    visited = set()
    instructions = input_text.split(',')
    index = 0
    for instruction in instructions:
        trim = instruction.strip()
        direction, steps = trim[0], int(trim[1:])
        index = (index + map_instruction[direction]) % len(directions)
        step_direction = directions[index]
        for _ in range(steps):
            position = (position[0] + step_direction[0], position[1] + step_direction[1])
            if position in visited:
                distance = abs(position[0]) + abs(position[1])
                return f"distance: {distance}"
            visited.add(position)
    return f"distance NOT FOUND"
