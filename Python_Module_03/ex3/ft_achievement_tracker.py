#!/usr/bin/env python3

class Player():
    """
    Class to Manage Players. Has name, kill_count, level and
    achivements as inbuilt variables."""
    name: str
    kill_count: int
    level: int
    achivements: set[str]

    def __init__(self, name: str, kill_count: int, level: int) -> None:
        """
        Plant Class Initialisation function. Takes and sets
        name, kill_count, level. sets achivements to empty set.
        if any acivements are detected based on level or killcount, adds them
        to the achivements set."""

        self.name = name
        self.kill_count = kill_count
        self.level = level
        self.achivements = set()
        self.check_kill_achievements()
        self.check_level_achievements()

    def add_achievement(self, achievements: list[str]) -> None:
        """Adds a list of achievements to the player's achievement set."""
        for achievement in achievements:
            self.achivements.add(achievement)

    def level_up(self, levels: int) -> None:
        """Increases the player's level by a specified number of levels."""
        self.level += levels
        self.check_level_achievements()

    def check_level_achievements(self) -> None:
        """Checks the player's level and adds corresponding achievements."""
        if self.level >= 10:
            self.achivements.add("level_10")
        if self.level >= 50:
            self.achivements.add("level_50")
        if self.level >= 100:
            self.achivements.add("level_100")

    def check_kill_achievements(self) -> None:
        """Checks the player's level and adds corresponding achievements."""
        # if self.kill_count == 0:
        # self.achivements.add("pacifist")
        if self.kill_count >= 1:
            self.achivements.add("first_kill")
            # if "pacifist" in self.achivements:
            # self.achivements.remove("pacifist")
        if self.kill_count >= 100:
            self.achivements.add("berserker")


class PlayerAnalytics():
    """Class to perform analytics on a list of players."""
    players: list[Player]
    achievement_list: set[str] = {"level_10", "level_50", "level_100",
                                  "pacifist", "first_kill", "berserker",
                                  "boss_slayer", "strategist",
                                  "explorer", "treasure_hunter",
                                  "social_butterfly", "lone_wolf"
                                  "speedrun", "collector",
                                  "perfectionist", "completionist"
                                  }

    def __init__(self, players: list[Player]) -> None:
        """Initializes the player analytics with a list of players."""
        self.players = players

    def analyze_achievements(self) -> None:
        """
        Analyzes the achievements of the players and prints various
        statistics."""

        achievements_present = set()
        achievements_in_common = self.achievement_list.copy()
        rare_achievements = set()
        for player in self.players:
            achievements_present.update(player.achivements)
            achievements_in_common.intersection_update(player.achivements)

        rare_achievements = {achievement
                             for achievement in achievements_present
                             if sum(achievement in player.achivements
                                    for player in self.players)
                             == 1}

        print(f"All unique achievements: {achievements_present}")
        print(f"Total unique achievements: {len(achievements_present)}")
        print()
        print(f"Common to all players: {achievements_in_common}")

        print(f"Rare achievements (1 player): {rare_achievements}")

    def compare(self, i1: int, i2: int) -> None:
        if self.players[i1] is None or self.players[i2] is None:
            print("Invalid player indices for comparison.")
            return
        player1 = self.players[i1]
        player2 = self.players[i2]
        common = player1.achivements.intersection(player2.achivements)
        print(f"player1 vs player2 common: {common}")
        player1_unique = player1.achivements.difference(player2.achivements)
        player2_unique = player2.achivements.difference(player1.achivements)
        print(f"{player1.name} unique: {player1_unique}")
        print(f"{player2.name} unique: {player2_unique}")


def ft_achievement_tracker() -> None:
    print("=== Achievement Tracker System ===")

    print()
    alice = Player("Alice", 50, 12)
    alice.add_achievement(["treasure_hunter", "speed_demon"])
    print(f"Player {alice.name} achievements: {alice.achivements}")

    bob = Player("Bob", 50, 20)
    bob.add_achievement(["boss_slayer", "collector"])
    print(f"Player {bob.name} achievements: {bob.achivements}")

    charlie = Player("Charlie", 0, 10)
    charlie.add_achievement(["treasure_hunter", "boss_slayer", "speed_demon",
                             "perfectionist"])
    print(f"Player {charlie.name} achievements: {charlie.achivements}")
    print()
    print("=== Achievement Analytics ===")

    player_analytics = PlayerAnalytics([alice, bob, charlie])
    player_analytics.analyze_achievements()
    print()
    player_analytics.compare(0, 1)


if __name__ == "__main__":
    ft_achievement_tracker()
# {
# 'alice':
    # ['first_blood',
    # 'pixel_perfect',
    # 'speed_runner',
    # 'first_blood',
    # 'first_blood'],
# 'bob':
    # ['level_master',
    # 'boss_hunter',
    # 'treasure_seeker',
    # 'level_master',
    # 'level_master'],
# 'charlie':
    # ['treasure_seeker',
    # 'boss_hunter',
    # 'combo_king',
    # 'first_blood',
    # 'boss_hunter',
    # 'first_blood',
    # 'boss_hunter',
    # 'first_blood'],
# 'diana':
    # ['first_blood',
    # 'combo_king',
    # 'level_master',
    # 'treasure_seeker',
    # 'speed_runner',
    # 'combo_king',
    # 'combo_king',
    # 'level_master'],
# 'eve':
    # ['level_master',
    # 'treasure_seeker',
    # 'first_blood',
    # 'treasure_seeker',
    # 'first_blood',
    # 'treasure_seeker'],
# 'frank':
    # ['explorer',
    # 'boss_hunter',
    # 'first_blood',
    # 'explorer',
    # 'first_blood',
    # 'boss_hunter']
# }
