import hashlib


def part1(input_text: str) -> str:
    nonce = calculate_nonce(input_text, 5)
    return f"nonce: {nonce}"


def part2(input_text: str) -> str:
    nonce = calculate_nonce(input_text, 6)
    return f"nonce: {nonce}"


def calculate_nonce(input_text: str, difficult: int) -> int:
    current_hash = hashlib.md5(input_text.encode())
    nonce = 0
    compare = '0' * difficult
    while current_hash.hexdigest()[0:difficult] != compare:
        current_hash = hashlib.md5(f"{input_text}{nonce}".encode())
        nonce += 1
    return nonce - 1


def is_valid(hash_value: str, difficult: int) -> bool:
    return hash_value[0:5] == '0' * difficult
