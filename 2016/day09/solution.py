from typing import List


def process(text: str) -> str:
    new_text = ""
    i = 0
    while i < len(text):
        char = text[i]
        if char == '(':
            j = i
            while text[j] != ')':
                j += 1
            counter, multiplier = text[i + 1:j].split('x')
            text_to_add = text[j + 1:j + int(counter) + 1]
            for _ in range(int(multiplier)):
                new_text += text_to_add
            i = j + int(counter) + 1
        else:
            new_text += text[i]
            i += 1
    return new_text

def deep_process(text: str) -> int:
    length = 0
    i = 0
    while i < len(text):
        char = text[i]
        if char == '(':
            j = i
            while text[j] != ')':
                j += 1
            counter, multiplier = text[i + 1:j].split('x')
            deep_counter = deep_process(text[j + 1:j + int(counter) + 1])
            length += deep_counter * int(multiplier)
            i = j + int(counter) + 1
        else:
            length += 1
            i += 1
    return length

def part1(input_text: str) -> str:
    result = process(input_text)
    return f"decompress length {len(result)}"


def part2(input_text: str) -> str:
    result = deep_process(input_text)
    return f"decompress length {result}"
