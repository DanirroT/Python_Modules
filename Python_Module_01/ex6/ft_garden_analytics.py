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


class Garden():
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

    def report(self) -> None:
        regular = 0
        flower = 0
        prized = 0
        print(f"=== {self.owner}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
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
        print(f"Plants added: {self.plants_added},",
              f"Total growth: {self.plant_growth}cm")
        print(f"Plant types: {regular} regular, {flower}",
              f"flowering, {prized} prize flowers")


class GardenManager():
    gardens: list[Garden]
    garden_count: int

    def __init__(self, gardens: list[Garden] = []) -> None:
        self.gardens = []
        self.garden_count = 0

        if gardens:
            for garden in gardens:
                self.garden_count += 1
                (self.gardens).append(garden)

    def validate_height(self) -> bool:
        problems: list[tuple[str, str]] = []
        for garden in self.gardens:
            for plant in garden.plants:
                if plant.height < 0:
                    problems.append((garden.name, plant.name))
        if problems == []:
            return True
        print("found problems at:", ", ".join(f"{g} {p}" for g, p in problems))
        return False

    def judge(self) -> None:
        height_val = self.validate_height()
        print(f"Height validation test: {height_val}")
        if not height_val:
            return
        start = True
        print("Garden scores - ", end="")
        for garden in self.gardens:
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
        print(f"Total gardens managed: {self.garden_count}")


def ft_plant_types() -> None:
    """Introduction to Garden Data Analytics. Adds difrent Plants to a garden,
printing information as this happens. then it lets all plants grow using the
garden manager after it prints a status screen with relevant information."""

    print("=== Garden Management System Demo ===")

    garden = Garden("Big Garden", "Alice")

    print()
    garden.add_plant(Plant("Oak tree", 100, 1825))
    # garden.add_plant(Plant("Rotting tree", -100, 1825))
    garden.add_plant(FloweringPlant("Rose", 25, 30, "red"))
    garden.add_plant(PrizeFlower("Sunflower", 50, 90, "yellow", 10))
    print()
    garden.grow()
    print()
    garden.report()
    print()
    garden_manager = GardenManager([garden,
                                    Garden("Small Garden", "Ben",
                                           [Plant("Jacaranda", 82, 150)])])

    garden_manager.judge()


if __name__ == "__main__":
    ft_plant_types()
