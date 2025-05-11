from typing import List


def part1(input_text: str) -> str:
    boxes = input_text.split("\n")
    total_square_feet = 0
    for box in boxes:
        total_square_feet += calculate_square_feet(box.split("x"))
    return f"total square feet: {total_square_feet}"


def calculate_square_feet(dimensions: List[str]) -> int:
    d1 = int(dimensions[0])
    d2 = int(dimensions[1])
    d3 = int(dimensions[2])

    side1 = d1 * d2
    side2 = d2 * d3
    side3 = d1 * d3
    return 2 * side1 + 2 * side2 + 2 * side3 + min(side1, side2, side3)


def part2(input_text: str) -> str:
    boxes = input_text.split("\n")
    ribbon_feet = 0
    for box in boxes:
        ribbon_feet += calculate_ribbon_feet(box.split("x"))
    return f"total of ribbon feet: {ribbon_feet}"


def calculate_ribbon_feet(dimensions: List[str]) -> int:
    d1 = int(dimensions[0])
    d2 = int(dimensions[1])
    d3 = int(dimensions[2])

    extra_ribbon = 2 * d1 + 2 * d2 + 2 * d3 - 2 * max(d1, d2, d3)
    return d1 * d2 * d3 + extra_ribbon
