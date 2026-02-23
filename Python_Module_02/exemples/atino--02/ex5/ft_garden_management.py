class GardenError(Exception):
    """Base class for garden-related errors."""
    pass


class PlantError(GardenError):
    """Error for plant problems."""
    pass


class WaterError(GardenError):
    """Error for watering problems."""
    pass


class GardenManager:
    """Simple garden management system."""

    plants: list[str]
    water_levels: dict[str, int]
    sun_levels: dict[str, int]

    def __init__(self) -> None:
        self.plants = []
        self.water_levels: dict[str, int] = {}
        self.sun_levels: dict[str, int] = {}

    def add_plant(self, name: str, water: int, sun: int) -> None:
        """Add a plant to the garden with water and sunlight levels."""
        try:
            is_empty: bool = True
            for char in name:
                if char != " ":
                    is_empty = False
                    break

            if name == "" or is_empty:
                raise PlantError("Plant name cannot be empty!")

            valid_plants: list[str] = ("tomato", "lettuce", "carrot")
            if name not in valid_plants:
                raise PlantError(f"'{name}' is not a valid plant!")

            self.plants += [name]
            self.water_levels[name] = water
            self.sun_levels[name] = sun
            print(f"Added {name} successfully")

        except PlantError as e:
            print(f"Error adding plant: {e}")

    def water_plants(self) -> None:
        """Simulate watering all plants, handle low water errors, clean up."""
        print("\nWatering plants...")
        try:
            print("Opening watering system")
            for plant in self.plants:
                if self.water_levels[plant] < 1:
                    raise WaterError(f"Not enough water in tank for {plant}")
                self.water_levels[plant] -= 1
                print(f"Watering {plant} - success")
        except WaterError as e:
            print(f"Caught GardenError: {e}")
            print("System recovered and continuing...")
        finally:
            print("Closing watering system (cleanup)")

    def check_health(self) -> None:
        """Check plant health based on water and sunlight ranges."""
        print("\nChecking plant health...")
        for plant in self.plants:
            try:
                water: int = self.water_levels[plant]
                sun: int = self.sun_levels[plant]

                water_bad: bool = water < 1 or water > 10
                sunlight_bad: bool = sun < 2 or sun > 12
                if water_bad and sunlight_bad:
                    raise PlantError(
                        f"Both values are out of range!\n"
                        f"Water level should be 1-10 (got {water}),\n"
                        f"Sunlight hours should be 2-12 (got {sun})"
                    )

                if water < 1:
                    raise PlantError(f"Water level {water} is too low (min 1)")
                if water > 10:
                    raise PlantError(
                        f"Water level {water} is too high (max 10)"
                    )
                if sun < 2:
                    raise PlantError(
                        f"Sunlight hours {sun} is too low (min 2)"
                    )
                if sun > 12:
                    raise PlantError(
                        f"Sunlight hours {sun} is too high (max 12)"
                    )

                print(f"{plant}: healthy (water: {water}, sun: {sun})")

            except PlantError as e:
                print(f"Error checking {plant}: {e}")


def test_garden_management() -> None:
    """Demonstrate garden management with error handling."""
    garden: GardenManager = GardenManager()

    print("Adding plants to garden...")
    garden.add_plant("tomato", 5, 8)
    garden.add_plant("lettuce", 15, 8)
    garden.add_plant("", 3, 5)
    garden.add_plant("chocolate cake", 55, 42)

    garden.water_plants()

    garden.check_health()

    print("\nTesting error recovery...")
    garden.add_plant("carrot", 0, 9)
    garden.water_plants()

    print("\nGarden management system test complete!")


if __name__ == "__main__":
    print("=== Garden Management System ===\n")

    test_garden_management()
