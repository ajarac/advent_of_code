import re
from typing import List

def has_abba(token: str) -> bool:
    left, right = 0, 3

    while right < len(token):
        if (token[left] == token[right] and
                token[left + 1] == token[right - 1] and
                token[left] != token[left + 1]):
            return True
        left += 1
        right += 1

    return False


def supports_tls(inside: List[str], outside: List[str]) -> bool:
    return any(has_abba(x) for x in outside) and all(not has_abba(x) for x in inside)


def get_list_aba(outside: List[str]) -> List[str]:
    list_aba = []
    for token in outside:
        left, right = 0, 2
        while right < len(token):
            if token[left] == token[right] and token[left] != token[left + 1]:
                list_aba.append(token[left: right + 1])
            left += 1
            right += 1
    return list_aba


def contains_bab(inside: List[str], list_aba: List[str]) -> bool:
    for aba in list_aba:
        bab = f"{aba[1]}{aba[0]}{aba[1]}"
        for token in inside:
            if bab in token:
                return True

    return False


def support_ssl(inside: List[str], outside: List[str]) -> bool:
    list_aba = get_list_aba(outside)
    return contains_bab(inside, list_aba)


def part1(input_text: str) -> str:
    counter = 0
    for ip in input_text.split('\n'):
        inside = re.findall(r'\[([^\]]+)\]', ip)
        outside = re.split(r'\[[^\]]+\]', ip)
        if supports_tls(inside, outside):
            counter += 1
    return f"valid ips: {counter}"


def part2(input_text: str) -> str:
    counter = 0
    for ip in input_text.split('\n'):
        inside = re.findall(r'\[([^\]]+)\]', ip)
        outside = re.split(r'\[[^\]]+\]', ip)
        if support_ssl(inside, outside):
            counter += 1
    return f"valid ips: {counter}"
