#!/usr/bin/env python3

class GardenError(Exception):
    prefix: str = "Caught a garden error: "

    def __init__(self, message) -> None:
        super().__init__(self.prefix + message)


class PlantError(GardenError):
    prefix: str = "Caught PlantError: "


class WaterError(GardenError):
    prefix: str = "Caught WaterError: "


def check_age(age: int) -> None:
    if age > 60:
        raise PlantError("The tomato plant is wilting!")
    elif age < 0:
        raise PlantError("Impossible age (min 0)")
    elif age > 40:
        print("The tomato plant is ready to harvest")
    print("The tomato plant is growing")


def check_water(water_level: int) -> None:
    if water_level > 50:
        raise WaterError("The tank is overflowing!")
    elif water_level < 5:
        raise WaterError("Not enough water in the tank!")
    elif water_level < 0:
        raise WaterError("Impossible age (min 0)")
    print("water is fine")


print("=== Custom Garden Errors Demo ===")
print()
print("Testing PlantError...")
try:
    check_water(4)
except WaterError as e:
    print(e)
print()
print("Testing WaterError...")
try:
    check_age(100)
except PlantError as e:
    print(e)
print()
print("Testing catching all garden errors...")
try:
    check_age(100)
except GardenError as e:
    print(e)
try:
    check_water(100)
except GardenError as e:
    print(e)
print()
print("All custom error types work correctly!")

print()
