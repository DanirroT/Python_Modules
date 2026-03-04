#!/usr/bin/env python3

class Player():
    """
    Class to Manage Players. Has name, kill_count, level and
    achivements as inbuilt variables.
    """
    name: str
    kill_count: int
    level: int
    achivements: set[str]

    def __init__(self, name: str, kill_count: int, level: int) -> None:

        if not name or name == "":
            raise ValueError("Player name cannot be empty.")
        self.name = name
        self.kill_count = int(kill_count)
        self.level = int(level)
        self.achivements: set[str] = set()
        self.check_kill_achievements()
        self.check_level_achievements()

    def add_achievement(self, achievements: list[str]) -> None:
        """Adds a list of achievements to the player's achievement set."""
        for acm in achievements:
            self.achivements.add(acm)

    def level_up(self, levels: int) -> None:
        """Increases the player's level by a specified number of levels."""
        self.level += int(levels)
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

        acms_present: set[str] = set()
        acms_in_common = self.achievement_list.copy()
        rare_acms = set()
        for player in self.players:
            acms_present = acms_present.union(player.achivements)
            acms_in_common = acms_in_common.intersection(player.achivements)

        rare_acms = {acm
                     for acm in acms_present
                     if sum(acm in player.achivements
                            for player in self.players)
                     == 1}

        print(f"All unique achievements: {acms_present}")
        print(f"Total unique achievements: {len(acms_present)}")
        print()
        print(f"Common to all players: {acms_in_common}")

        print(f"Rare achievements (1 player): {rare_acms}")

    def compare(self, i1: int, i2: int) -> None:
        if self.players[i1] is None or self.players[i2] is None:
            print("Invalid player indices for comparison.")
            return
        player1 = self.players[i1]
        player2 = self.players[i2]
        common = player1.achivements.intersection(player2.achivements)
        print(f"{player1.name} vs {player2.name} common: {common}")
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
