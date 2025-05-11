def part1(input_text: str) -> str:
    visited = set()
    visited.add((0, 0))
    position = (0, 0)
    for move in input_text:
        position = new_position(position, move)
        visited.add(position)

    return f"number of houses visited: {len(visited)}"


def part2(input_text: str) -> str:
    positions = [(0, 0), (0, 0)]
    visited = set()
    visited.add((0, 0))
    for i, move in enumerate(input_text):
        positions[i % 2] = new_position(positions[i % 2], move)
        visited.add(positions[i % 2])

    return f"number of houses visited: {len(visited)}"


def new_position(position: (int, int), move: str) -> (int, int):
    if move == "^":
        return position[0] + 1, position[1]
    elif move == '>':
        return position[0], position[1] + 1
    elif move == '<':
        return position[0], position[1] - 1
    else:
        return position[0] - 1, position[1]
