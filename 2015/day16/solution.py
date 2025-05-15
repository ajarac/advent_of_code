from typing import List

#
# children: 3
# cats: 7
# samoyeds: 2
# pomeranians: 3
# akitas: 0
# vizslas: 0
# goldfish: 5
# trees: 3
# cars: 2
# perfumes: 1
ticker_tape = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1
}

greater_than = ['cats', 'trees']
less_than = ['pomeranians', 'goldfish']


class Sue:
    def __init__(self, num: int, attributes: dict[str, int]):
        self.num = num
        self.attributes = attributes

    def can_be_a_candidate(self, attributes_needed: dict[str, int]) -> bool:
        for attribute in self.attributes:
            if self.attributes[attribute] != attributes_needed[attribute]:
                return False
        return True

    def can_be_a_candidate_2(self, attributes_needed: dict[str, int]) -> bool:
        for attribute in self.attributes:
            value = self.attributes[attribute]
            needed = attributes_needed.get(attribute)

            if attribute in greater_than:
                if value <= needed:
                    return False
            elif attribute in less_than:
                if value >= needed:
                    return False
            elif value != needed:
                return False

        return True


def parse(row: str) -> Sue:
    parts = row.split(' ')
    num = int(parts[1].split(':')[0])
    tokens = "".join(parts[2:]).split(',')
    attributes = {}
    for token in tokens:
        attribute = token.split(':')
        attributes[attribute[0].strip()] = int(attribute[1].strip())
    return Sue(num, attributes)


def parse_all(input: str) -> List[Sue]:
    return [parse(row) for row in input.split('\n')]


def part1(input_text: str) -> str:
    sue_list = parse_all(input_text)
    for sue in sue_list:
        if sue.can_be_a_candidate(ticker_tape):
            return f"Sue found: {sue.num}"
    return "NOT FOUND"


def part2(input_text: str) -> str:
    sue_list = parse_all(input_text)
    for sue in sue_list:
        if sue.can_be_a_candidate_2(ticker_tape):
            return f"Sue found: {sue.num}"
    return "NOT FOUND"
