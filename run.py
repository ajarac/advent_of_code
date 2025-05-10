import sys
from pathlib import Path
from importlib import import_module

def load_input(year: str, day: str, test=False):
    filename = "test_input.txt" if test else "input.txt"
    path = Path(f"{year}/day{day.zfill(2)}/{filename}")
    return path.read_text()

def main():
    if len(sys.argv) < 3:
        print("Usage: python run.py <year> <day> [--test]")
        return

    year, day = sys.argv[1], sys.argv[2]
    test = "--test" in sys.argv

    module_path = f"{year}.day{day.zfill(2)}.solution"
    solution = import_module(module_path)
    input_data = load_input(year, day, test)

    print(f"Year {year} Day {day}")
    print("Part 1:", solution.part1(input_data))
    print("Part 2:", solution.part2(input_data))

if __name__ == "__main__":
    main()