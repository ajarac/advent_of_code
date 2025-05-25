from collections import defaultdict
from typing import List


def parse(input_text: str) -> List[List[int]]:
    nums_list = []
    for row in input_text.split('\n'):
        nums = []
        for num in row.strip().split(' '):
            if num != '':
                nums.append(int(num))
        nums_list.append(nums)
    return nums_list


def is_valid_triangle(nums: List[int]) -> bool:
    max_num = max(nums)
    return sum(nums) - max_num > max_num


def part1(input_text: str) -> str:
    nums_list = parse(input_text)
    counter = 0
    for nums in nums_list:
        if is_valid_triangle(nums):
            counter += 1
    return f"valid triangles {counter}"


def parse_group(input_text: str, grouped_by: int) -> List[List[int]]:
    nums_list = parse(input_text)
    new_list = []
    for index in range(0, len(nums_list), grouped_by):
        nums = []
        for i in range(index, index + grouped_by):
            i_mod = i % grouped_by
            nums.append([])
            for j in range(index, index + grouped_by):
                j_mod = j % grouped_by
                nums[i_mod].append(nums_list[index + j_mod][i_mod])
        for num_list in nums:
            new_list.append(num_list)
    return new_list


def part2(input_text: str) -> str:
    nums_list = parse_group(input_text, 3)
    counter = 0
    for nums in nums_list:
        if is_valid_triangle(nums):
            counter += 1
    return f"valid triangles {counter}"
