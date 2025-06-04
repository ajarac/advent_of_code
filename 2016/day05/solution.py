import hashlib
from typing import List

num_zeros = 5
password_length = 8


def is_valid_hash(h: str) -> bool:
    should_init = "0" * num_zeros
    return h[0:num_zeros] == should_init


def part1(input_text: str) -> str:
    password = ""
    nonce = 0
    while len(password) < password_length:
        nonce += 1
        to_hash = input_text + str(nonce)
        hashed = hashlib.md5(to_hash.encode()).hexdigest()
        if is_valid_hash(hashed):
            password += hashed[num_zeros]
    return f"password: {password}"


def is_valid_hash_2(password: List[str], hashed: str) -> bool:
    return (is_valid_hash(hashed) and
            hashed[num_zeros].isdigit() and
            0 <= int(hashed[num_zeros]) < password_length and
            password[int(hashed[num_zeros])] == "")


def part2(input_text: str) -> str:
    password: List[str] = [""] * password_length
    counter = 0
    nonce = 0
    while counter < password_length:
        nonce += 1
        to_hash = input_text + str(nonce)
        hashed = hashlib.md5(to_hash.encode()).hexdigest()
        if is_valid_hash_2(password, hashed):
            password[int(hashed[num_zeros])] = hashed[num_zeros + 1]
            counter += 1
    return f"password: {"".join(password)}"
