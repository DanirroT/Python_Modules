#!/usr/bin/env python3

class Plant():
    """Class to Manage Plants. Has name, height(in cm) and age_days as inbuilt
variables."""
    name: str
    height: int
    age_days: int


def ft_garden_data() -> None:
    """Introduction to Garden Data Management. Uses the Plant Class to create
plant profiles. After, Prints the information."""
    print("=== Garden Plant Registry ===")
    plant_1 = Plant()
    plant_2 = Plant()
    plant_3 = Plant()

    plant_1.name, plant_1.height, plant_1.age_days = ("Rose", 25, 30)
    plant_2.name, plant_2.height, plant_2.age_days = ("Sunflower", 80, 45)
    plant_3.name, plant_3.height, plant_3.age_days = ("Cactus", 15, 120)

    print(f"{plant_1.name}: {plant_1.height}cm, {plant_1.age_days} days old")
    print(f"{plant_2.name}: {plant_2.height}cm, {plant_2.age_days} days old")
    print(f"{plant_3.name}: {plant_3.height}cm, {plant_3.age_days} days old")


if __name__ == "__main__":
    ft_garden_data()
