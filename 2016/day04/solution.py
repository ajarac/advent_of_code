import heapq
from typing import List, Counter


class Encryption:
    def __init__(self, encrypted: List[str], sector_id: int, checksum: str):
        self.encrypted = encrypted
        self.min_heap = self.heap_list("".join(encrypted))
        self.sector_id = sector_id
        self.checksum = checksum

    def heap_list(self, encrypted: str) -> List:
        counter = Counter(encrypted)
        min_heap = []
        for c in counter:
            min_heap.append((counter[c] * -1, c))
        heapq.heapify(min_heap)
        return min_heap

    def is_valid(self) -> bool:
        i = 0
        min_heap = self.min_heap.copy()
        while i < len(self.checksum):
            counter, c = heapq.heappop(min_heap)
            if c != self.checksum[i]:
                return False
            i += 1

        return True

    def decrypt(self) -> str:
        decrypt = ""
        for word in self.encrypted:
            decrypt += " "
            for letter in word:
                decrypt += self.decrypt_letter(letter)
        return decrypt

    def decrypt_letter(self, letter: str) -> str:
        index = ord(letter) - ord('a')
        new_index = (index + self.sector_id) % 26
        return chr(new_index + ord('a'))


def parse_item(row: str) -> Encryption:
    tokens = row.split('-')
    last_tokens = tokens[-1].split('[')
    signal_id = int(last_tokens[0])
    checksum = last_tokens[1][:-1]
    return Encryption(tokens[:-1], signal_id, checksum)


def parse(input_text: str) -> List[Encryption]:
    return [parse_item(row) for row in input_text.split('\n')]


def part1(input_text: str) -> str:
    counter = 0
    encryptions = parse(input_text)
    for encryption in encryptions:
        if encryption.is_valid():
            counter += encryption.sector_id

    return f"counter of valid rooms: {counter}"


def part2(input_text: str) -> str:
    encryptions = parse(input_text)
    for encryption in encryptions:
        if 'northpole' in encryption.decrypt():
            return f"northpole object storage => sector id {encryption.sector_id}"
    return "NOT FOUND"
