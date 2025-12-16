from typing import List


def execute(memory: dict[str, int], instructions: List[str]) -> int:
    index = 0
    while 0 <= index < len(instructions):
        instruction = instructions[index].split(' ')
        match instruction[0]:
            case 'cpy':
                if instruction[1].isdigit():
                    memory[instruction[2]] = int(instruction[1])
                else:
                    memory[instruction[2]] = memory[instruction[1]]
                index += 1
            case 'inc':
                memory[instruction[1]] = memory[instruction[1]] + 1
                index += 1
            case 'dec':
                memory[instruction[1]] = memory[instruction[1]] - 1
                index += 1
            case 'jnz':
                if instruction[1].isdigit():
                    value = int(instruction[1])
                else:
                    value = memory.get(instruction[1], 0)

                if value != 0:
                    index += int(instruction[2])
                else:
                    index += 1
    return memory['a']


def part1(input_text: str) -> str:
    a_value = execute(dict(), input_text.split('\n'))
    return f"Value in 'a' = {a_value}"


def part2(input_text: str) -> str:
    a_value = execute({'c': 1}, input_text.split('\n'))
    return f"Value in 'a' = {a_value}"
