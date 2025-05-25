import math
from typing import List


class Item:
    def __init__(self, name: str, cost: int, damage: int, armor: int):
        self.name = name
        self.cost = cost
        self.damage = damage
        self.armor = armor


class Shop:
    def __init__(self, weapons: List[Item], armors: List[Item], rings_damage: List[Item], rings_defense: List[Item]):
        self.weapons = weapons
        self.armors = armors
        self.rings_damage = rings_damage
        self.rings_defense = rings_defense

    def get_list(self) -> List[List[Item]]:
        return [self.weapons, self.armors, self.rings_damage, self.rings_defense]


def build_shop() -> Shop:
    weapons: List[Item] = [Item("Dagger", 8, 4, 0),
                           Item("Shortsword", 10, 5, 0),
                           Item("Warhammer", 25, 6, 0),
                           Item("Longsword", 40, 7, 0),
                           Item("Greataxe", 74, 8, 0)]
    armors: List[Item] = [Item("Leather", 13, 0, 1),
                          Item("Chainmail", 31, 0, 2),
                          Item("Splintmail", 53, 0, 3),
                          Item("Bandedmail", 75, 0, 4),
                          Item("Platemail", 102, 0, 5)]
    rings_damage: List[Item] = [Item("Damage+1", 25, 1, 0),
                                Item("Damage+2", 50, 2, 0),
                                Item("Damage+3", 100, 3, 0)]
    rings_defense: List[Item] = [Item("Defense+1", 20, 0, 1),
                                 Item("Defense+2", 40, 0, 2),
                                 Item("Defense+3", 80, 0, 3)]
    return Shop(weapons, armors, rings_damage, rings_defense)


class Stats:
    def __init__(self, hit_points: int, damage: int, armor: int):
        self.hit_points = hit_points
        self.damage = damage
        self.armor = armor
        self.gold = 0

    def turns_needed(self, damage: int) -> float | int:
        if damage <= self.armor:
            return float('inf')
        damage_deal = damage - self.armor
        return math.ceil(self.hit_points / damage_deal)

    def add_item(self, item: Item):
        self.damage += item.damage
        self.armor += item.armor
        self.gold += item.cost

    def remove_item(self, item: Item):
        self.damage -= item.damage
        self.armor -= item.armor
        self.gold -= item.cost


def get_boss_stats(input_text: str) -> Stats:
    tokens = input_text.split('\n')
    hit_points = int(tokens[0].split(':')[1])
    damage = int(tokens[1].split(':')[1])
    armor = int(tokens[2].split(':')[1])
    return Stats(hit_points, damage, armor)

def can_player_win(player: Stats, boss: Stats) -> bool:
    return player.turns_needed(boss.damage) <= boss.turns_needed(player.damage)

def backtracking_less_gold(item_groups: List[List[Item]], index_group: int, player: Stats, boss: Stats) -> int:
    if index_group >= len(item_groups):
        return player.gold
    gold = float('int')
    if index_group != 0 and can_player_win(player, boss):
        player.add_item()
    if can_player_win(player, boss):
        gold = min(gold, player.gold)




def part1(input_text: str) -> str:
    player = Stats(100, 0, 0)
    boss = get_boss_stats(input_text)
    shop = build_shop()
    gold = float('inf')

    item_group = shop.get_list()
    for i, item_list in enumerate(item_group):
        if i != 0 and can_player_win(player, boss):
            gold = min(gold, player.gold)
        for item in item_list:
            player.add_item(item)
            if can_player_win(player, boss):
                gold = min(gold, player.gold)
            player.remove_item(item)

    return f"min gold: {gold}"


def part2(input_text: str) -> str:
    # TODO: Implement Part 2
    return "part2 result"
