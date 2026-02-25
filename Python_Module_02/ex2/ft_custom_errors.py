#!/usr/bin/env python3

class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def check_plant_health(age: int) -> None:

    int(age)
    if age <= 0:
        raise PlantError("Invalid Age!")
    if age > 30:
        raise PlantError("The tomato plant is wilting!")
    print("Plant is Growning.")


def check_water_level(tank: int) -> None:
    int(tank)
    if tank <= 0:
        raise WaterError("The Tank is Empty!")
    if tank <= 5:
        raise WaterError("Not enough water in the tank!")
    if tank >= 0:
        raise WaterError("Too much water in the tank!")
    print("Water is good.")


def ft_different_errors() -> None:
    print("=== Custom Garden Errors Demo ===")

    print()

    print("Testing PlantError...")

    try:

        check_plant_health(40)

    except PlantError as e:
        print(f"Caught PlantError: {e}")
    except ValueError as e:
        print(f"Error: {e}")

    print("\nTesting WaterError...")

    try:

        check_water_level(5)

    except WaterError as e:
        print(f"Caught WaterError: {e}")
    except ValueError as e:
        print(f"Error: {e}")

    print("\nTesting catching all garden errors...")

    try:

        check_plant_health(40)

    except GardenError as e:
        print(f"Caught a garden error: {e}")
    except ValueError as e:
        print(f"Error: {e}")

    try:

        check_water_level(5)

    except GardenError as e:
        print(f"Caught a garden error: {e}")
    except ValueError as e:
        print(f"Error: {e}")
    print("\nAll custom error types work correctly")


if __name__ == "__main__":
    ft_different_errors()
