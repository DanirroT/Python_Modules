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


def ft_plant_factory() -> None:
    """Introduction to Garden Data Management Streamlining. Uses
the Plant Class to create plant profiles. After, Prints the information."""
    print("=== Plant Factory Output ===")

    plants: list[Plant] = []

    plants.append(Plant("Rose", 25, 30))
    plants.append(Plant("Oak", 200, 260))
    plants.append(Plant("Cactus", 5, 90))
    plants.append(Plant("Sunflower", 80, 45))
    plants.append(Plant("Fern", 15, 120))

    print(f"\nTotal plants created: {len(plants)}")


if __name__ == "__main__":
    ft_plant_factory()
