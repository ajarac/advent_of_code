import random


def get_transformers(input_text: str) -> dict[str, str]:
    hash_map = {}
    for row in input_text.split('\n'):
        if row == '':
            return hash_map
        tokens = row.split('=>')
        token_from = tokens[0].strip()
        if token_from not in hash_map:
            hash_map[token_from] = []
        hash_map[token_from].append(tokens[1].strip())
    return hash_map

def get_inverse_transformers(input_text: str) -> dict[str, str]:
    hash_map = {}
    for row in input_text.split('\n'):
        if row == '':
            return hash_map
        tokens = row.split('=>')
        hash_map[tokens[1].strip()] = tokens[0].strip()
    return hash_map

def get_molecule(input_text: str) -> str:
    return input_text.split('\n')[-1].strip()


def count(hash_map: dict[str, str], molecule: str) -> int:
    visited = set()
    for key in hash_map:
        key_len = len(key)
        for i in range(len(molecule) - key_len + 1):
            if molecule[i:i + key_len] == key:
                for replacement in hash_map[key]:
                    new_molecule = molecule[:i] + replacement + molecule[i + key_len:]
                    visited.add(new_molecule)
    return len(visited)


def part1(input_text: str) -> str:
    counter = count(get_transformers(input_text), get_molecule(input_text))
    return f"number of molecules {counter}"



def calculate(transformers: dict[str, str], final_molecule: str, current_molecule: str) -> int:
    reversed_rules = list(transformers.items())

    # Optional: limit retry attempts
    max_attempts = 1000

    for attempt in range(max_attempts):
        shuffled_rules = sorted(reversed_rules, key=lambda x: -len(x[0]))
        random.shuffle(shuffled_rules)  # shuffle to vary path
        molecule = current_molecule
        counter = 0

        while molecule != final_molecule:
            for to_replace, replace_with in shuffled_rules:
                if to_replace in molecule:
                    molecule = molecule.replace(to_replace, replace_with, 1)
                    counter += 1
                    break
            else:
                # If no replacement was made, try again with a new shuffle
                break
        else:
            return counter  # succeeded

    raise ValueError("Stuck after multiple retries — transformation path not found.")

def part2(input_text: str) -> str:
    transformers = get_inverse_transformers(input_text)
    molecule = get_molecule(input_text)
    counter = calculate(transformers, 'e', molecule)
    return f"min counter {counter}"
