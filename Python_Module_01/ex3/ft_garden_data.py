#!/usr/bin/env python3

class Plant():
    """Class to Manage Plants. Has name, height(in cm) and age_days as inbuilt
variables."""
    name: str
    height: int
    age_days: int

    def __init__(self, name: str, height: int, age_days: int) -> None:
        """Plant Class Initialisation function. Takes and sets
name, height(in cm) and age_days."""
        self.name = name
        self.height = height
        self.age_days = age_days
        print(f"Created: {self.name} ({self.height}cm, {self.age_days} days)")


def ft_garden_data():
    """Introduction to Garden Data Management Streamlining. Uses
the Plant Class to create plant profiles. After, Prints the information."""
    print("=== Plant Factory Output ===")
    plant_1 = Plant("Rose", 25, 30)
    _ = plant_1
    plant_2 = Plant("Oak", 200, 260)
    _ = plant_2
    plant_3 = Plant("Cactus", 5, 90)
    _ = plant_3
    plant_4 = Plant("Sunflower", 80, 45)
    _ = plant_4
    plant_5 = Plant("Fern", 15, 120)
    _ = plant_5

    print("\nTotal plants created: 5")


if __name__ == "__main__":
    ft_garden_data()
