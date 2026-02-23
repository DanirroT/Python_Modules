class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def check_plant_health(age: int) -> None:
    int(age)
    if age > 30:
        raise PlantError("The tomato plant is wilting!")


def check_water_level(tank: int) -> None:
    int(tank)
    if tank <= 0:
        raise WaterError("Not enough water in the tank!")


def catching_errors(age: int, tank: int) -> None:
    try:
        check_plant_health(age)
        check_water_level(tank)
    except PlantError as e:
        print(f"Caught PlantError: {e}")
    except WaterError as e:
        print(f"Caught WaterError: {e}")
    except ValueError as e:
        print(f"Error: {e}")


def catching_garden_errors(age: int, tank: int) -> None:
    try:
        check_plant_health(age)
        check_water_level(tank)
    except GardenError as e:
        print(f"Caught a garden error: {e}")
    except ValueError as e:
        print(f"Error: {e}")


def main() -> None:
    print("=== Custom Garden Errors Demo ===\n")

    print("Testing PlantError...")
    catching_errors(40, 20)
    print("\nTesting WaterError...")
    catching_errors(10, -5)

    print("\nTesting catching all garden errors...")
    catching_garden_errors(40, 20)
    catching_garden_errors(10, -5)
    print("\nAll custom error types work correctly")


if __name__ == "__main__":
    main()
