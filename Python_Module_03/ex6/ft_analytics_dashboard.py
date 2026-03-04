#!/usr/bin/env python3

class Player():

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

        if not name or name == "":
            raise ValueError("Player name cannot be empty.")
        self.name = name
        if not location or location == "":
            raise ValueError("Player location cannot be empty.")
        self.location = location
        self.score = int(score)
        self.kill_count = int(kill_count)
        self.level = int(level)
        self.active = active
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


def list_comprehension(player_list: list[Player]) -> None:

    print("=== List Comprehension Examples ===")

    scores = {player.name: player.score for player in player_list}

    high_scorers = [player for player, score in scores.items() if score > 2000]
    doubled_scores = [score * 2 for score in scores.values()]
    active_players = [player.name for player in player_list if player.active]

    print("High scorers (>2000):", high_scorers)
    print("Scores doubled:", doubled_scores)
    print("Active players:", active_players)


def dict_comprehension(player_list: list[Player]) -> None:

    print("=== Dict Comprehension Examples ===")

    scores_active = {player.name: player.score
                     for player in player_list
                     if player.active}

    score_brackets = {"high": 0, "medium": 0, "low": 0}

    for player in player_list:
        if player.score > 2500:
            score_brackets["high"] += 1

        elif player.score > 2000:
            score_brackets["medium"] += 1

        else:
            score_brackets["low"] += 1

    achievement_count_active = {player.name: len(player.achivements)
                                for player in player_list
                                if player.active}

    print("Player scores:", scores_active)
    print("Score categories:", score_brackets)
    print("Achievement counts:", achievement_count_active)


def set_comprehension(player_list: list[Player]) -> None:

    print("=== Set Comprehension Examples ===")

    scores = {player.name: player.score for player in player_list}

    # achievement_list = {player.name: player.achivements
    #                     for player in player_list}

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


def combined_analysis(player_list: list[Player]) -> None:

    print("=== Combined Analysis ===")

    scores = {player.name: player.score for player in player_list}

    achievement_count = {player.name: len(player.achivements)
                         for player in player_list}

    players_count: int = len(scores)
    print("Total players:", players_count)
    print("Total unique achievements:", 12)
    average_score: float = sum(scores.values()) / players_count
    print(f"Average score: {average_score:.1f}")
    top_performer = max(scores, key=scores.get)
    print("Top performer: ", top_performer,
          " (", scores[top_performer], " points, ",
          achievement_count[top_performer], " achievements)", sep="")


def ft_analytics_dashboard() -> None:
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

    list_comprehension(player_list)

    print()

    dict_comprehension(player_list)

    print()

    set_comprehension(player_list)

    print()

    combined_analysis(player_list)


if __name__ == "__main__":
    ft_analytics_dashboard()


#
#  {'players':
#   {'alice': {'level': 41, 'total_score': 2824, 'sessions_played': 13,
#  'favorite_mode': 'ranked', 'achievements_count': 5},
# 'bob':
#   {'level': 16, 'total_score': 4657, 'sessions_played': 27,
#  'favorite_mode': 'ranked', 'achievements_count': 2},
# 'charlie':
#   {'level': 44, 'total_score': 9935, 'sessions_played': 21,
#  'favorite_mode': 'ranked', 'achievements_count': 7},
# 'diana':
#   {'level': 3, 'total_score': 1488, 'sessions_played': 21,
#  'favorite_mode': 'casual', 'achievements_count': 4},
# 'eve':
#   {'level': 33, 'total_score': 1434, 'sessions_played': 81,
#  'favorite_mode': 'casual', 'achievements_count': 7},
# 'frank':
#   {'level': 15, 'total_score': 8359, 'sessions_played': 85,
#  'favorite_mode': 'competitive', 'achievements_count': 1}},
#
# 'sessions': [
#   {'player': 'bob', 'duration_minutes': 94, 'score': 1831,
#  'mode': 'competitive', 'completed': False},
#   {'player': 'bob', 'duration_minutes': 32, 'score': 1478,
#  'mode': 'casual', 'completed': True},
#   {'player': 'diana', 'duration_minutes': 17, 'score': 1570,
#  'mode': 'competitive', 'completed': False},
#   {'player': 'alice', 'duration_minutes': 98, 'score': 1981,
#  'mode': 'ranked', 'completed': True},
#   {'player': 'diana', 'duration_minutes': 15, 'score': 2361,
#  'mode': 'competitive', 'completed': False},
#   {'player': 'eve', 'duration_minutes': 29, 'score': 2985,
#  'mode': 'casual', 'completed': True},
#   {'player': 'frank', 'duration_minutes': 34, 'score': 1285,
#  'mode': 'casual', 'completed': True},
#   {'player': 'alice', 'duration_minutes': 53, 'score': 1238,
#  'mode': 'competitive', 'completed': False},
#   {'player': 'bob', 'duration_minutes': 52, 'score': 1555,
#  'mode': 'casual', 'completed': False},
#   {'player': 'frank', 'duration_minutes': 92, 'score': 2754,
#  'mode': 'casual', 'completed': True},
#   {'player': 'eve', 'duration_minutes': 98, 'score': 1102,
#  'mode': 'casual', 'completed': False},
#   {'player': 'diana', 'duration_minutes': 39, 'score': 2721,
#  'mode': 'ranked', 'completed': True},
#   {'player': 'frank', 'duration_minutes': 46, 'score': 329,
#  'mode': 'casual', 'completed': True},
#   {'player': 'charlie', 'duration_minutes': 56, 'score': 1196,
#  'mode': 'casual', 'completed': True},
#   {'player': 'eve', 'duration_minutes': 117, 'score': 1388,
#  'mode': 'casual', 'completed': False},
#   {'player': 'diana', 'duration_minutes': 118, 'score': 2733,
#  'mode': 'competitive', 'completed': True},
#   {'player': 'charlie', 'duration_minutes': 22, 'score': 1110,
#  'mode': 'ranked', 'completed': False},
#   {'player': 'frank', 'duration_minutes': 79, 'score': 1854,
#  'mode': 'ranked', 'completed': False},
#   {'player': 'charlie', 'duration_minutes': 33, 'score': 666,
#  'mode': 'ranked', 'completed': False},
#   {'player': 'alice', 'duration_minutes': 101, 'score': 292,
#  'mode': 'casual', 'completed': True},
#   {'player': 'frank', 'duration_minutes': 25, 'score': 2887,
#  'mode': 'competitive', 'completed': True},
#   {'player': 'diana', 'duration_minutes': 53, 'score': 2540,
#  'mode': 'competitive', 'completed': False},
#   {'player': 'eve', 'duration_minutes': 115, 'score': 147,
#  'mode': 'ranked', 'completed': True},
#   {'player': 'frank', 'duration_minutes': 118, 'score': 2299,
#  'mode': 'competitive', 'completed': False},
#   {'player': 'alice', 'duration_minutes': 42, 'score': 1880,
#  'mode': 'casual', 'completed': False},
#   {'player': 'alice', 'duration_minutes': 97, 'score': 1178,
#  'mode': 'ranked', 'completed': True},
#   {'player': 'eve', 'duration_minutes': 18, 'score': 2661,
#  'mode': 'competitive', 'completed': True},
#   {'player': 'bob', 'duration_minutes': 52, 'score': 761,
#  'mode': 'ranked', 'completed': True},
#   {'player': 'eve', 'duration_minutes': 46, 'score': 2101,
#  'mode': 'casual', 'completed': True},
#   {'player': 'charlie', 'duration_minutes': 117, 'score': 1359,
#  'mode': 'casual', 'completed': True}],
#
# 'game_modes': ['casual', 'competitive', 'ranked'],
# 'achievements': ['first_blood', 'level_master', 'speed_runner',
#                  'treasure_seeker', 'boss_hunter', 'pixel_perfect',
#                  'combo_king', 'explorer']}
