from typing import List


def get_index(char: str) -> int:
    return ord(char) - ord('a')


letters_not_allowed = [get_index('i'), get_index('o'), get_index('l')]


def part1(input_text: str) -> str:
    password = get_next_password(string_to_index(input_text), 1)
    return f"next valid password: {index_to_string(password)}"


def part2(input_text: str) -> str:
    password = get_next_password(string_to_index(input_text), 2)
    return f"next valid password: {index_to_string(password)}"


def get_next_password(password_index: List[int], iterations: int) -> List[int]:
    for _ in range(iterations):
        password_index = get_next(password_index)
        while not is_valid_password(password_index):
            password_index = get_next(password_index)
    return password_index


def get_next(password_index: List[int]) -> List[int]:
    i = len(password_index) - 1
    while i >= 0:
        password_index[i] += 1
        if password_index[i] >= 26:
            password_index[i] = 0
            i -= 1
        else:
            break

    # Fix disallowed characters like 'i', 'o', 'l'
    for i, val in enumerate(password_index):
        if val in letters_not_allowed:
            password_index[i] += 1
            for j in range(i + 1, len(password_index)):
                password_index[j] = 0
            break

    return password_index


def string_to_index(password: str) -> List[int]:
    return [get_index(char) for char in password]


def index_to_string(password_index: List[int]) -> str:
    return "".join([chr(i + ord('a')) for i in password_index])


def is_valid_password(password_index: List[int]) -> bool:
    # Rule 2: Check for forbidden letters
    for letter in password_index:
        if letter in letters_not_allowed:
            return False

    # Rule 1: Check for increasing straight of three letters
    has_straight = False
    for i in range(len(password_index) - 2):
        if (password_index[i] + 1 == password_index[i + 1] and
            password_index[i + 1] + 1 == password_index[i + 2]):
            has_straight = True
            break

    if not has_straight:
        return False

    # Rule 3: Check for at least two different non-overlapping pairs
    pair_count = 0
    i = 1
    while i < len(password_index):
        if password_index[i] == password_index[i - 1]:
            pair_count += 1
            i += 2  # skip next char to avoid overlapping pairs
        else:
            i += 1

    return pair_count >= 2
