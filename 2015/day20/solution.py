MAX_PRESENTS = 11


def calculate_presents(n: int) -> int:
    total = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            total += 10 * i
            if i != n // i:
                total += 10 * (n // i)
    return total


def calculate_presents_limit(n: int) -> int:
    total = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            if n // i <= 50:
                total += 11 * i
            if i != n // i and i <= 50:
                total += 11 * (n // i)
    return total


def part1(input_text: str) -> str:
    total_presents = int(input_text)
    found = None
    i = 1
    while found is None:
        presents = calculate_presents(i)
        if presents >= total_presents:
            found = i
        i += 1
    return f"house number: {found}"


def part2(input_text: str) -> str:
    total_presents = int(input_text)
    found = None
    i = 1
    while found is None:
        presents = calculate_presents_limit(i)
        if presents >= total_presents:
            found = i
        i += 1
    return f"house number: {found}"
