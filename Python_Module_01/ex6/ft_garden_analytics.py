#!/usr/bin/env python3

class Plant():
    """Class to Manage Plants. Has name, height(in cm) and age_d as inbuilt
variables."""
    name: str
    height: int
    age_d: int

    def __init__(self, name: str, height: int, age_d: int) -> None:
        """Plant Class Initialisation function. Takes and sets
name, height(in cm) and age_d."""
        self.name = name
        self.height = height
        self.age_d = age_d

    @classmethod
    def get_plant_type(cls) -> str:
        return cls.__name__


class FloweringPlant(Plant):
    """Class to Manage Flowing Plants Derived from the Plant Class.
Has name, height(in cm), age_d, color and blooming as inbuilt variables."""
    color: str
    blooming: bool

    def __init__(self,
                 name: str,
                 height: int,
                 age_d: int,
                 color: str,
                 blooming: bool = True
                 ) -> None:
        """Flower Class Initialisation function. Takes and sets
name, height(in cm), age_d, color and blooming. Prints when finnished."""
        super().__init__(name, height, age_d)
        self.color = color
        self.blooming = blooming

    def bloom(self):
        """shows a nice message"""
        self.blooming = True
        print(f"{self.name} is blooming beautifully!")

    @classmethod
    def get_plant_type(cls) -> str:
        return cls.__name__


class PrizeFlower(FloweringPlant):
    """Class to Manage Prized Flowers Derived from the FloweringPlant Class.
Has name, height(in cm), age_d, color, blooming and prize_points as inbuilt
variables."""
    prize_points: int

    def __init__(self,
                 name: str,
                 height: int,
                 age_d: int,
                 color: str,
                 prize_points: int,
                 blooming: bool = True,
                 ) -> None:
        """Flower Class Initialisation function. Takes and sets name, height
(in cm), age_d, color, blooming and prize_points. Prints when finnished."""
        super().__init__(name, height, age_d, color, blooming)
        self.prize_points = prize_points

    @classmethod
    def get_plant_type(cls) -> str:
        return cls.__name__


class GardenManager():
    name: str
    owner: str
    plants: list[Plant]
    plant_count: int
    plants_added: int

    def __init__(self, name: str, owner: str, plants: list[Plant] = []
                 ) -> None:
        """Plant Class Initialisation function. Takes and sets
name, height(in cm) and age_d."""
        self.name = name
        self.owner = owner
        self.plants = []
        self.plant_count = 0
        self.plant_growth = 0
        self.plants_added = 0

        if plants:
            for plant in plants:
                self.plant_count += 1
                (self.plants).append(plant)

    def add_plant(self, new_plant: Plant) -> None:
        self.plants.append(new_plant)
        self.plant_count += 1
        self.plants_added += 1
        print(f"Added {new_plant.name} to {self.owner}'s garden")

    def grow(self) -> None:
        print("Alice is helping all plants grow...")
        for plant in self.plants:
            print(f"{plant.name} grew 1cm")
            self.plant_growth += 1
            plant.height += 1


class GardenStats():

    @staticmethod
    def create_garden_network(gardens_in: list[GardenManager] = []
                              ) -> list[GardenManager]:
        gardens_out = []

        if gardens_in:
            for garden in gardens_in:
                gardens_out.append(garden)
        return gardens_out

    @staticmethod
    def report(garden: GardenManager) -> None:
        regular = 0
        flower = 0
        prized = 0
        print(f"=== {garden.owner}'s Garden Report ===")
        print("Plants in garden:")
        for plant in garden.plants:
            plant_type = plant.get_plant_type()
            if plant_type == "PrizeFlower":
                prized += 1
                print(f"- {plant.name}: {plant.height}cm, {plant.color} "
                      "flower" " (blooming)" if plant.blooming else "",
                      f", Prize points: {plant.prize_points}", sep="")
            elif plant_type == "FloweringPlant":
                flower += 1
                print(f"- {plant.name}: {plant.height}cm, {plant.color} flower"
                      " (blooming)" if plant.blooming else "")
            elif plant_type == "Plant":
                regular += 1
                print(f"- {plant.name}: {plant.height}cm")
        print()
        print(f"Plants added: {garden.plants_added},",
              f"Total growth: {garden.plant_growth}cm")
        print(f"Plant types: {regular} regular, {flower}",
              f"flowering, {prized} prize flowers")

    @staticmethod
    def validate_height(plant: Plant) -> bool:
        if plant.height < 0:
            return False
        return True

    def judge(self, gardens_in: list[GardenManager]) -> None:

        problems: list[tuple[str, str]] = []

        gardens = self.create_garden_network(gardens_in)

        for garden in gardens:
            for plant in garden.plants:
                height_val = self.validate_height(plant)
                if not height_val:
                    problems.append((garden.name, plant.name))

        height_val = True
        if problems:
            print("Found problems at:", ", ".join(f"{p} in {g}"
                                                  for g, p in problems))
            height_val = False

        print(f"Height validation test: {height_val}")
        if not height_val:
            return

        print("Garden scores - ", end="")
        garden_count = 0
        start = True
        for garden in gardens:
            garden_count += 1
            if start:
                start = False
            else:
                print(", ", end="")
            score = 0
            print(garden.owner, end=" ")
            for plant in garden.plants:
                plant_type = plant.get_plant_type()
                score += 10
                if plant_type == "PrizeFlower":
                    score += plant.prize_points
                score += plant.height
            print(score, end="")
        print()
        print(f"Total gardens managed: {garden_count}")


def ft_garden_analytics() -> None:
    """Introduction to Garden Data Analytics. Adds difrent Plants to a garden,
printing information as this happens. then it lets all plants grow using the
garden manager after it prints a status screen with relevant information."""

    print("=== Garden Management System Demo ===")

    garden = GardenManager("Big Garden", "Alice")

    print()
    garden.add_plant(Plant("Oak tree", 100, 1825))
    # garden.add_plant(Plant("Rotting tree", -100, 1825))
    garden.add_plant(FloweringPlant("Rose", 25, 30, "red"))
    garden.add_plant(PrizeFlower("Sunflower", 50, 90, "yellow", 10))
    print()
    garden.grow()
    print()
    garden_stats = GardenStats()

    garden_stats.report(garden)
    print()
    garden_2 = GardenManager("Small Garden", "Ben",
                             [Plant("Jacaranda", 82, 150)])

    garden_stats.judge([garden, garden_2])


if __name__ == "__main__":
    ft_garden_analytics()
