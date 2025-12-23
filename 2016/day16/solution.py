def dragon_curve(value: str) -> str:
    return value + '0' + ''.join('1' if c == '0' else '0' for c in value[::-1])


def calculate_checksum(data) -> str:
    checksum = ''.join(['1' if data[i] == data[i + 1] else '0' for i in range(0, len(data), 2)])
    if len(checksum) % 2 == 0:
        return calculate_checksum(checksum)
    return checksum


def calculate(input_text: str, length: int) -> str:
    data = input_text
    while len(data) < length:
        data = dragon_curve(data)
    return f"checksum: {calculate_checksum(data[:length])}"


def part1(input_text: str) -> str:
    return calculate(input_text, 272)


def part2(input_text: str) -> str:
    return calculate(input_text, 35651584)
