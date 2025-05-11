def execute(input: str) -> str:
    result = ""
    prev_number = ""
    counter = 1
    for num in input:
        if prev_number == num:
            counter += 1
            continue
        if prev_number != "":
            result += f"{counter}{prev_number}"
        counter = 1
        prev_number = num

    return result + f"{counter}{prev_number}"


def part1(input_text: str) -> str:
    for _ in range(40):
        input_text = execute(input_text)

    return f"length: {len(input_text)}"


def part2(input_text: str) -> str:
    for _ in range(50):
        input_text = execute(input_text)
    return f"length: {len(input_text)}"
