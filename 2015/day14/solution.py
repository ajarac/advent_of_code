from typing import List


class Reindeer:
    def __init__(self, name: str, speed: int, speed_time: int, rest_time: int):
        self.name = name
        self.speed = speed
        self.speed_time = speed_time
        self.rest_time = rest_time
        self.is_resting = False
        self.current_distance = 0
        self.current_time = 0
        self.points = 0

    def calculate_distance(self, seconds: int) -> int:
        self.current_distance = 0
        while self.speed_time < seconds:
            if self.is_resting:
                seconds -= self.rest_time
            else:
                self.current_distance += self.speed * self.speed_time
                seconds -= self.speed_time
            self.is_resting = not self.is_resting
        if seconds > 0:
            self.current_distance += self.speed * seconds
        return self.current_distance

    def iterate_second(self) -> int:
        self.current_time += 1
        if self.is_resting:
            if self.current_time == self.rest_time:
                self.is_resting = False
                self.current_time = 0
        else:
            self.current_distance += self.speed
            if self.current_time == self.speed_time:
                self.is_resting = True
                self.current_time = 0
        return self.current_distance


def parse(input_row: str) -> Reindeer:
    tokens = input_row.split(' ')
    name = tokens[0]
    speed = int(tokens[3])
    speed_time = int(tokens[6])
    rest_time = int(tokens[13])
    return Reindeer(name, speed, speed_time, rest_time)


def parse_all(input_text: str) -> List[Reindeer]:
    return [parse(row) for row in input_text.split('\n')]


def part1(input_text: str) -> str:
    reindeers = parse_all(input_text)
    max_distance = 0
    for reindeer in reindeers:
        max_distance = max(max_distance, reindeer.calculate_distance(2503))
    return f"max distance {max_distance}"


def part2(input_text: str) -> str:
    reindeers = parse_all(input_text)
    for _ in range(2503):
        for reindeer in reindeers:
            reindeer.iterate_second()
        leader = reindeers[0]
        for reindeer in reindeers:
            if leader.current_distance < reindeer.current_distance:
                leader = reindeer
        leader.points += 1
    max_points = 0
    for reindeer in reindeers:
        max_points = max(max_points, reindeer.points)
    return f"max points {max_points}"
