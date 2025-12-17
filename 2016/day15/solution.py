from typing import List


class Disc:

    def __init__(self, positions: int, current_position: int):
        self.positions = positions
        self.time = 0
        self.current_position = current_position

    def next(self):
        self.current_position += 1
        if self.current_position > self.positions:
            self.current_position = 0

    def is_zero(self):
        return self.current_position == 0


def parse_line(line: str) -> Disc:
    parts = line.split()
    positions = int(parts[3])
    current_pos = int(parts[-1].rstrip('.'))
    return Disc(positions, current_pos)


def parse(input_text: str) -> List[Disc]:
    return [parse_line(line) for line in input_text.split('\n')]


def check_alignment(discs: List[Disc], start_time: int) -> bool:
    for i, disc in enumerate(discs):
        arrival_time = start_time + i + 1
        position_at_arrival = (disc.current_position + arrival_time) % disc.positions
        if position_at_arrival != 0:
            return False
    return True

def part1(input_text: str) -> str:
    discs = parse(input_text)
    time = 0
    while not check_alignment(discs, time):
        time += 1
    return f"time: {time}"


def part2(input_text: str) -> str:
    discs = parse(input_text)
    discs.append(Disc(11, 0))
    time = 0
    while not check_alignment(discs, time):
        time += 1
    return f"time: {time}"
