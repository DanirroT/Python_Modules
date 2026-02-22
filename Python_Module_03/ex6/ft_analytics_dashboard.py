#!/usr/bin/env python3

class Player():
    """
    Class to Manage Players. Has name, kill_count, level and
    achivements as inbuilt variables."""
    name: str
    location: str
    kill_count: int
    score: int
    level: int
    active: bool
    achivements: set[str]

    def __init__(self, name: str, location: str,
                 kill_count: int, score: int, level: int,
                 active: bool) -> None:
        """
        Plant Class Initialisation function. Takes and sets
        name, kill_count, level. sets achivements to empty set.
        if any acivements are detected based on level or killcount, adds them
        to the achivements set.
        """

        self.name = name
        self.location = location
        self.kill_count = kill_count
        self.score = score
        self.level = level
        self.active = active
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


def ft_analytics_dashboard():
    print("=== Game Analytics Dashboard ===")
    print()
    alice = Player("alice", "north", 0, 2300, 6, True)
    alice.add_achievement(["treasure_hunter", "speed_demon",
                           "strategist", "explorer", "collector"])

    bob = Player("bob", "east", 0, 1800, 4, True)
    bob.add_achievement(["collector", "explorer", "perfectionist"])

    charlie = Player("charlie", "central", 1, 2150, 10, True)
    charlie.add_achievement(["treasure_hunter", "boss_slayer",
                             "speed_demon", "perfectionist", "strategist"])

    diana = Player("diana", "west", 0, 2000 + 50, 2, False)
    diana.add_achievement(["strategist", "collector"])

    player_list = [alice, bob, charlie, diana]

    print("=== List Comprehension Examples ===")

    scores = {player.name: player.score for player in player_list}
    # achievement_list = {player.name: player.achivements
    #                     for player in player_list}
    achievement_count = {player.name: len(player.achivements)
                         for player in player_list}
    achievement_count_active = {player.name: len(player.achivements)
                                for player in player_list
                                if player.active}
    high_scorers = [player for player, score in scores.items() if score > 2000]
    doubled_scores = [score * 2 for score in scores.values()]
    active_players = [player.name for player in player_list if player.active]

    print("High scorers (>2000):", high_scorers)
    print("Scores doubled:", doubled_scores)
    print("Active players:", active_players)
    print()
    print("=== Dict Comprehension Examples ===")
    scores_active = {player.name: player.score for player in player_list if player.active}
    print("Player scores:", scores_active)
    print("Score categories:", {'high': 3, 'medium': 2, 'low': 1})
    print("Achievement counts:", achievement_count_active)
    print()
    print("=== Set Comprehension Examples ===")

    achievements_present = set()
    for player in player_list:
        achievements_present.update(player.achivements)

    rare_achievements = {achievement
                         for achievement in achievements_present
                         if sum(achievement in player.achivements
                                for player in player_list)
                         == 1}
    active_locations = {player.location
                        for player in player_list
                        if player.active}

    print("Unique players:", set(scores.keys()))
    print("Unique achievements:", rare_achievements)
    print("Active regions:", active_locations)
    print()
    print("=== Combined Analysis ===")
    players_count: int = len(scores)
    print("Total players:", players_count)
    print("Total unique achievements:", 12)
    average_score: float = sum(scores.values()) / players_count
    print(f"Average score: {average_score:.2f}")
    top_performer = max(scores, key=scores.get)
    print("Top performer: ", top_performer,
          " (", scores[top_performer], " points, ",
          achievement_count[top_performer], " achievements)", sep="")


if __name__ == "__main__":
    ft_analytics_dashboard()
