import re
from collections import defaultdict


def part1(input_text: str) -> str:
    bots, rules = get_bots_and_rules(input_text)

    # Step 2: Simulate
    return simulation(bots, rules, [17, 61])


def simulation(bots, rules, target):
    outputs = defaultdict(list)
    while True:
        # Find any bot with 2 chips
        ready_bots = [bot_id for bot_id, chips in bots.items() if len(chips) == 2]
        if not ready_bots:
            break

        for bot_id in ready_bots:
            low, high = sorted(bots[bot_id])

            # Check for the target comparison
            if [low, high] == target:
                return str(bot_id)

            # Distribute chips
            rule = rules[bot_id]
            for kind, value, chip in zip(["low", "high"], [low, high], [low, high]):
                target_type, target_id = rule[kind]
                if target_type == "bot":
                    bots[target_id].append(chip)
                else:
                    outputs[target_id].append(chip)

            bots[bot_id] = []  # Bot has given away its chips
    return "Not found"


def get_bots_and_rules(input_text: str):
    bots = defaultdict(list)
    rules = {}
    for line in input_text.strip().splitlines():
        if line.startswith("value"):
            # Example: "value 5 goes to bot 2"
            value, bot = map(int, re.findall(r'\d+', line))
            bots[bot].append(value)
        else:
            # Example: "bot 2 gives low to bot 1 and high to bot 0"
            nums = re.findall(r'\d+', line)
            bot_id = int(nums[0])
            low_type = "output" if "low to output" in line else "bot"
            high_type = "output" if "high to output" in line else "bot"
            rules[bot_id] = {
                "low": (low_type, int(nums[1])),
                "high": (high_type, int(nums[2]))
            }
    return bots, rules


def part2(input_text: str) -> str:
    bots, rules = get_bots_and_rules(input_text)

    return simulation_2(bots, rules)


def simulation_2(bots, rules):
    outputs = defaultdict(list)
    while True:
        ready_bots = [bot_id for bot_id, chips in bots.items() if len(chips) == 2]
        if not ready_bots:
            break

        for bot_id in ready_bots:
            low, high = sorted(bots[bot_id])
            rule = rules[bot_id]

            for kind, chip in zip(["low", "high"], [low, high]):
                target_type, target_id = rule[kind]
                if target_type == "bot":
                    bots[target_id].append(chip)
                else:
                    outputs[target_id].append(chip)

            bots[bot_id] = []

        # Check outputs 0, 1, and 2
        if all(len(outputs[o]) > 0 for o in [0, 1, 2]):
            product = outputs[0][0] * outputs[1][0] * outputs[2][0]
            return str(product)
    return "Not found"