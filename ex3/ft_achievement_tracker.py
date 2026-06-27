import random


class Player:
    def __init__(self, name: str, ach_set: set) -> None:
        self.name = name
        self.ach_set = ach_set


def gen_player_achievements(achievements_list) -> set:
    count = random.randint(3, len(achievements_list) // 2)
    return set(random.sample(achievements_list, count))


def main():
    print("=== Achievement Tracker System ===")
    print()
    achievements_list = [
        'Crafting Genius', 'Strategist', 'World Savior', 'Speed Runner',
        'Survivor', 'Master Explorer', 'Treasure Hunter', 'Unstoppable',
        'First Steps', 'Collector Supreme', 'Untouchable', 'Sharp Mind',
        'Boss Slayer'
    ]
    all_achievements = set(achievements_list)

    player1 = Player("Alice", gen_player_achievements(achievements_list))
    player2 = Player("Bob", gen_player_achievements(achievements_list))
    player3 = Player("Charlie", gen_player_achievements(achievements_list))
    player4 = Player("Dylan", gen_player_achievements(achievements_list))

    for p in [player1, player2, player3, player4]:
        print(f"Player {p.name}: {p.ach_set}")

    print()
    print(f"All distinct achievements: {player1.ach_set.union(player2.ach_set, player3.ach_set, player4.ach_set)}")
    print(f"\nCommon achievements: {player1.ach_set.intersection(player2.ach_set, player3.ach_set, player4.ach_set)}")
    print(f"\nOnly {player1.name} has: {player1.ach_set.difference(player2.ach_set, player3.ach_set, player4.ach_set)}")
    print(f"Only {player2.name} has: {player2.ach_set.difference(player1.ach_set, player3.ach_set, player4.ach_set)}")
    print(f"Only {player3.name} has: {player3.ach_set.difference(player1.ach_set, player2.ach_set, player4.ach_set)}")
    print(f"Only {player4.name} has: {player4.ach_set.difference(player1.ach_set, player2.ach_set, player3.ach_set)}")
    print(f"\n{player1.name} is missing: {all_achievements.difference(player1.ach_set)}")
    print(f"{player2.name} is missing: {all_achievements.difference(player2.ach_set)}")
    print(f"{player3.name} is missing: {all_achievements.difference(player3.ach_set)}")
    print(f"{player4.name} is missing: {all_achievements.difference(player4.ach_set)}")


if __name__ == "__main__":
    main()