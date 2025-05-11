import os
from pathlib import Path
import sys

TEMPLATE = '''def part1(input_text: str) -> str:
    # TODO: Implement Part 1
    return "part1 result"

def part2(input_text: str) -> str:
    # TODO: Implement Part 2
    return "part2 result"
'''

def create_day(year: str, day: str):
    day_folder = Path(f"{year}/day{day.zfill(2)}")
    if day_folder.exists():
        print(f"Day {day} already exists.")
        return

    os.makedirs(day_folder)
    (day_folder / "solution.py").write_text(TEMPLATE)
    (day_folder / "input.txt").touch()
    (day_folder / "test_input.txt").touch()

    print(f"Created {day_folder} with solution.py, input.txt, and test_input.txt")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python new_day.py <year> <day>")
        sys.exit(1)

    create_day(sys.argv[1], sys.argv[2])