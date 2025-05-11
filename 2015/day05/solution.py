def part1(input_text: str) -> str:
    counter = 0
    for string in input_text.split('\n'):
        if is_nice_string(string):
            counter += 1
    return f"number of nice strings: {counter}"


def is_nice_string(string: str) -> bool:
    not_allowed = ['ab', 'cd', 'pq', 'xy']
    vocals = ['a', 'e', 'i', 'o', 'u']
    vocals_found = 0
    double_letter = False
    for i, c in enumerate(string):
        if i > 0:
            if string[i - 1:i + 1] in not_allowed:
                return False
            if string[i - 1] == string[i]:
                double_letter = True
        if c in vocals:
            vocals_found += 1

    return vocals_found >= 3 and double_letter


def part2(input_text: str) -> str:
    counter = 0
    for string in input_text.split('\n'):
        if is_nice_string2(string):
            counter += 1
    return f"number of nice strings: {counter}"


def is_nice_string2(string: str) -> bool:
    double_letter = False
    hash_map = {}
    double_pair = False
    for i, c in enumerate(string):
        if i > 0:
            pair = string[i - 1: i + 1]
            if pair not in hash_map:
                hash_map[pair] = i
            elif abs(hash_map[pair] - i) > 1:
                double_pair = True
        if i > 1:
            if string[i - 2] == string[i]:
                double_letter = True
    return double_letter and double_pair
