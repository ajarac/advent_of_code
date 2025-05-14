from typing import List


class Ingredients:
    def __init__(self, ingredients: List[List[int]]):
        self.ingredients = ingredients

    def calculate(self, teaspoons: List[int]) -> int:
        if len(teaspoons) != len(self.ingredients):
            return 0
        points = 1
        for i in range(0, 4):
            points *= self.calculate_property(i, teaspoons)
        return points

    def calculate_property(self, i, teaspoons):
        property_points = 0
        for j in range(0, len(self.ingredients)):
            property_points += teaspoons[j] * self.ingredients[j][i]
        if property_points < 0:
            property_points = 0
        return property_points

    def calculate_with_calories(self, teaspoons: List[int]) -> int:
        calories = self.calculate_property(4, teaspoons)
        if calories != 500:
            return 0
        return self.calculate(teaspoons)


def spread_teaspoons(max_value: int, num_ingredients: int):
    def backtrack(so_far: List[int], remaining: int):
        if len(so_far) == num_ingredients - 1:
            yield so_far + [remaining]
            return
        for i in range(remaining + 1):
            yield from backtrack(so_far + [i], remaining - i)

    yield from backtrack([], max_value)


def parse(row: str) -> List[int]:
    tokens = row.split(':')[1].split(',')
    capacity = int(tokens[0].split(' ')[2])
    durability = int(tokens[1].split(' ')[2])
    flavor = int(tokens[2].split(' ')[2])
    texture = int(tokens[3].split(' ')[2])
    calories = int(tokens[4].split(' ')[2])
    return [capacity, durability, flavor, texture, calories]


def parse_all(input_text: str) -> Ingredients:
    return Ingredients([parse(row) for row in input_text.split('\n')])


def part1(input_text: str) -> str:
    ingredients = parse_all(input_text)
    max_points = 0
    for combination in spread_teaspoons(100, len(ingredients.ingredients)):
        max_points = max(max_points, ingredients.calculate(combination))
    return f"max points {max_points}"


def part2(input_text: str) -> str:
    ingredients = parse_all(input_text)
    max_points = 0
    for combination in spread_teaspoons(100, len(ingredients.ingredients)):
        max_points = max(max_points, ingredients.calculate_with_calories(combination))
    return f"max points {max_points}"
