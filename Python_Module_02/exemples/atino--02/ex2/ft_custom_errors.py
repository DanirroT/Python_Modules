class GardenError(Exception):
    """Base class for garden-related errors."""
    pass


class PlantError(GardenError):
    """Error for plant problems."""
    def __init__(self) -> None:
        self.message: str = "The plant is wilting!"
        super().__init__(self.message)


class WaterError(GardenError):
    """Error for watering problems."""
    def __init__(self) -> None:
        self.message: str = "Not enough water in the tank!"
        super().__init__(self.message)


def test_plant_error(temp_level: int) -> None:
    """Test PlantError."""
    try:
        if temp_level > 30:
            raise PlantError()
        print("Temperature: OK\n")
    except PlantError as e:
        print(f"Caught PlantError: {e}\n")


def test_water_error(water_amount: int) -> None:
    """Test WaterError."""
    try:
        if water_amount < 10:
            raise WaterError()
        print("Water: OK\n")
    except WaterError as e:
        print(f"Caught WaterError: {e}\n")


def test_catch_all_garden_errors(temp_level: int, water_amount: int) -> None:
    """Test catching all garden errors with GardenError."""
    try:
        if temp_level > 30:
            raise PlantError()
        print("Temperature: OK")
    except GardenError as e:
        print(f"Caught a garden error: {e}")

    try:
        if water_amount < 10:
            raise WaterError()
        print("Water: OK")
    except GardenError as e:
        print(f"Caught a garden error: {e}")


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===\n")

    print("Testing PlantError...")
    test_plant_error(55)

    print("Testing WaterError...")
    test_water_error(5)

    print("Testing catching all garden errors...")
    test_catch_all_garden_errors(55, 5)

    print("\nAll custom error types work correctly!")
