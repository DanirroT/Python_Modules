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


class FloweringPlant(Plant):
    """Class to Manage Flowing Plants Derived from the Plant Class.
Has name, height(in cm), age_d, collor and blooming as inbuilt variables."""
    color: str
    blooming: bool

    def __init__(self,
                 name: str,
                 height: int,
                 age_d: int,
                 color: str,
                 blooming: bool
                 ) -> None:
        """Flower Class Initialisation function. Takes and sets
name, height(in cm), age_d, collor and blooming. Prints when finnished."""
        super().__init__(name, height, age_d)
        self.color = color
        self.blooming = blooming
        print(f"\n{self.name} (Flower): {self.height}cm, {self.age_d}",
              f"days, {color} color")

    def bloom(self):
        """shows a nice message"""
        print(f"{self.name} is blooming beautifully!")


class PrizeFlower(FloweringPlant):
    """Class to Manage Prized Flowers Derived from the FloweringPlant Class.
Has name, height(in cm), age_d, collor, blooming and prize_points as inbuilt
variables."""
    prize_points: int

    def __init__(self,
                 name: str,
                 height: int,
                 age_d: int,
                 color: str,
                 blooming: bool,
                 prize_points: int,
                 ) -> None:
        """Flower Class Initialisation function. Takes and sets name, height
(in cm), age_d, collor, blooming and prize_points. Prints when finnished."""
        super().__init__(name, height, age_d, color, blooming)
        self.prize_points = prize_points
        print(f"\n{self.name} (Flower): {self.height}cm, {self.age_d}",
              f"days, {color} color")


class Garden():
    name: str
    owner: str
    plants: list[Plant]


class GardenManager():
    name: str
    gardens: list[Garden]


def ft_plant_types():
    """Introduction to Garden Data Analytics. Adds difrent Plants to a garden,
printing information as this happens. then it lets all plants grow using the
garden manager after it prints a status screen with relevant information."""

    print("=== Garden Management System Demo ===")
    plant_1 = Plant("Rose", 25, 30, "red")
    plant_1.bloom()

    plant_2 = FloweringPlant("Oak", 500, 1825, 50)
    plant_2.produce_shade()

    plant_3 = PrizeFlower("Tomato", 80, 90, "summer", "vitamin c")
    print(f"{plant_3.name}  is rich in {plant_3.nutritional_value}")


if __name__ == "__main__":
    ft_plant_types()
