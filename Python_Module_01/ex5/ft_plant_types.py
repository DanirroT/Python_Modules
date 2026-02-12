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


class Flower(Plant):
    """Class to Manage Flowing Plants Derived from the Plant Class.
Has name, height(in cm), age_d and collor as inbuilt variables."""
    color: str

    def __init__(self,
                 name: str,
                 height: int,
                 age_d: int,
                 color: str
                 ) -> None:
        """Flower Class Initialisation function. Takes and sets
name, height(in cm), age_d and collor. Prints when finnished."""

        super().__init__(name, height, age_d)
        self.color = color
        print(f"\n{self.name} (Flower): {self.height}cm, {self.age_d}",
              f"days, {color} color")

    def bloom(self):
        """shows a nice message"""
        print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    """Class to Manage Trees Derived from the Plant Class.
Has name, height(in cm), age_d and trunk_diameter as inbuilt variables."""
    trunk_diameter: int

    def __init__(self,
                 name: str,
                 height: int,
                 age_d: int, trunk_diameter: int
                 ) -> None:
        """Tree Class Initialisation function. Takes and sets
name, height(in cm), age_d and trunk_diameter. Prints when finnished."""
        super().__init__(name, height, age_d)
        self.trunk_diameter = trunk_diameter
        print(f"\n{self.name} (Tree): {self.height}cm, {self.age_d}",
              f"days, {trunk_diameter}cm diameter")

    def produce_shade(self):
        """Calculates and displays the shade given by the called upon Tree"""
        # trunk_area = (((self.trunk_diameter / 2)**2 * 3.14) / 10000)
        shade = int((self.trunk_diameter**2 * 3.14) / 100)
        print(f"{self.name} provides {shade} square meters of shade")


class Vegetable(Plant):
    """Class to Manage Vegetables Derived from the Plant Class.
Has name, height(in cm), age_d, harvest_season and nutritional_value
as inbuilt variables."""
    harvest_season: str
    nutritional_value: str

    def __init__(self,
                 name: str,
                 height: int,
                 age_d: int,
                 harvest_season: str,
                 nutritional_value: str
                 ) -> None:
        """Vegetable Class Initialisation function. Takes and sets
name, height(in cm), age_d, harvest_season and nutritional_value.
Prints when finnished."""
        super().__init__(name, height, age_d)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value
        print(f"\n{self.name} (Vegetable): {self.height}cm, {self.age_d}",
              f"days,{harvest_season} harvest")


def ft_plant_types():
    """Introduction to Garden Data Management. Uses difrent Plant Derived
Classes to create plant profiles. After, Prints the information."""
    print("=== Garden Plant Types ===")
    plant_1 = Flower("Rose", 25, 30, "red")
    plant_1.bloom()

    plant_2 = Tree("Oak", 500, 1825, 50)
    plant_2.produce_shade()

    plant_3 = Vegetable("Tomato", 80, 90, "summer", "vitamin c")
    print(f"{plant_3.name}  is rich in {plant_3.nutritional_value}")


if __name__ == "__main__":
    ft_plant_types()
