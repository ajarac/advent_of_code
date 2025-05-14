import json


def part1(input_text: str) -> str:
    data = json.loads(input_text)
    return f"total sum: {parse_and_sum(data, False)}"


def part2(input_text: str) -> str:
    data = json.loads(input_text)
    return f"total sum: {parse_and_sum(data, True)}"


def parse_and_sum(data, should_skip: bool) -> int:
    total = 0
    if type(data) is list:
        for d in data:
            total += parse_and_sum(d, should_skip)
    elif type(data) is dict:
        for key in data:
            if should_skip and data[key] == 'red':
                return 0
            total += parse_and_sum(data[key], should_skip)
    elif type(data) is int:
        total += data

    return total
