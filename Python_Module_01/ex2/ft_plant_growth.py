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

    def grow(self) -> None:
        """Function that allows for a called upon Plant to grow.
All Plants grow at a rate of 1 cm per call."""
        self.height += 1

    def age(self) -> None:
        """Function that allows for a called upon Plant to age.
All Plants age at a rate of 1 day per call. Every day they also grow 1 cm."""
        self.age_days += 1
        self.grow()

    def get_info(self) -> str:
        """Function that returns a String with formatted informations
about the Called upon Plant"""
        return f"{self.name}: {self.height}cm, {self.age_days} days old"


def ft_plant_growth():
    """Introduction to Garden Data Manipulation. Uses the Plant Class to create
a plant profile. After, simulates the plant aging and rowing for a week.
Also prints some imformation before and after"""
    print("=== Garden Plant Registry ===")
    plant = Plant("Rose", 25, 30)

    days_loop = 7

    for day in range(0, days_loop):
        if day == 0:
            print(f"=== Day {day} ===")
            print(plant.get_info())
            height_1st = plant.height
        if day == days_loop - 1:
            print(f"=== Day {day} ===")
            print(plant.get_info())
            height_lst = plant.height
        plant.age()

    delta_height = height_lst - height_1st

    if delta_height == 0:
        delta_height = "None"
    elif delta_height > 0:
        delta_height = "+" + str(delta_height) + "cm"
    elif delta_height < 0:
        delta_height = str(delta_height) + "cm"

    print("Growth this week:", delta_height)


if __name__ == "__main__":
    ft_plant_growth()
