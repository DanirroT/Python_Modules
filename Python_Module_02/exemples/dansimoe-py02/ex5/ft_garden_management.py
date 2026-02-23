class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.set_name(name)
        self.set_height(height)
        self.set_age(age)

    def __str__(self) -> str:
        return f"{self._name} ({self.__class__.__name__}): " \
                f"{self._height}cm, {self._age} days"

    def set_name(self, name: str) -> None:
        if not name:
            raise PlantError("Plant name cannot be empty!")
        self._name = name

    def set_height(self, height: int) -> None:
        try:
            height = int(height)
        except ValueError:
            raise PlantError(f"Height {height} must be a number!")
        if height < 0:
            raise PlantError(f"Height {height}cm must be positive!")

        self._height = height

    def set_age(self, age: int) -> None:
        try:
            age = int(age)
        except ValueError:
            raise PlantError(f"Age {age} must be a number!")
        if age < 0:
            raise PlantError(f"Age {age} days must be positive!")

        self._age = age

    def get_name(self) -> str:
        return self._name


class GardenManager:
    def __init__(self, garden: str) -> None:
        self._plants: list[Plant] = []
        self._garden: str = garden
        self._tank: int = 10

    def add_plant(self, name: str, height: int, age: int) -> None:
        plant = Plant(name, height, age)
        self._plants.append(plant)
        print(f"Added {plant.get_name()} successfully")

    def water_plants(self) -> None:
        print("Opening watering system")
        try:
            for plant in self._plants:
                if self._tank <= 0:
                    raise WaterError("Not enough water in tank")

                print(f"Watering {plant.get_name()} - success")
                self._tank -= 5
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self, plant_name: str, water_level: int,
                           sunlight_hours: int) -> str:
        if not plant_name:
            raise PlantError("Plant name cannot be empty!")
        if water_level < 1:
            raise PlantError(f"Water level {water_level} is too low (min 1)")
        if water_level > 10:
            raise PlantError(f"Water level {water_level} is too high "
                             "(max 10)")
        if sunlight_hours < 2:
            raise PlantError(f"Sunlight hours {sunlight_hours} "
                             f"is too low (min 2)")
        if sunlight_hours > 12:
            raise PlantError(
                f"Sunlight hours {sunlight_hours} is too high (max 12)")

        return (f"{plant_name}: healthy (water: {water_level}, "
                f"sun: {sunlight_hours})")

    def check_water(self) -> None:
        if self._tank <= 0:
            raise GardenError("Not enough water in tank")

        print("Tank has still some water available")


def test_garden_management(garden: GardenManager) -> None:
    plant_list: list[list[str | int]] = [
        ["tomato", 20, 5],
        ["lettuce", 15, 10],
        [None, 10, 10],
    ]

    print("Adding plants to garden...")
    for plant in plant_list:
        try:
            garden.add_plant(plant[0],
                             plant[1],
                             plant[2])
        except PlantError as e:
            print(f"Error adding plant: {e}")
    print()

    try:
        print("Watering plants...")
        garden.water_plants()
    except WaterError as e:
        print(f"Error watering plant: {e}")
    print()

    plant_status: list[list[str | int]] = [
        ["tomato", 5, 8],
        ["lettuce", 15, 5],
    ]
    print("Checking plant health...")
    for plant in plant_status:
        try:
            print(garden.check_plant_health(plant[0],
                                            plant[1],
                                            plant[2]))
        except GardenError as e:
            print(f"Error checking  {plant[0]}: {e}")
    print()

    print("Testing error recovery...")
    try:
        garden.check_water()
    except GardenError as e:
        print(f"Caught {e.__class__.__name__}: {e}")
    print("System recovered and continuing...\n")


def main() -> None:
    garden = GardenManager("Alice")

    print("=== Garden Management System ===\n")
    test_garden_management(garden)
    print("Garden management system test complete!")


if __name__ == "__main__":
    main()
