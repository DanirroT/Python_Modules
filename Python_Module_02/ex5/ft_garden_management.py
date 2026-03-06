#!/usr/bin/env python3

class GardenError(Exception):
    """Base class for garden-related errors."""
    pass


class PlantError(GardenError):
    """Error for plant problems."""
    pass


class WaterError(GardenError):
    """Error for watering problems."""
    pass


class Plant():
    """Class to Manage Plants. Has name, height(in cm) and age_days as inbuilt
variables."""
    plant_name: str
    water_level: int
    sunlight_hour: int

    def __init__(self, name: str, water: int, sunlight: int) -> None:
        """Plant Class Initialisation function. Takes and sets
name, height(in cm) and age_days."""
        if not name:
            raise ValueError("Plant name cannot be empty!")
        self.plant_name = name
        self.water_level = water
        self.sunlight_hour = sunlight


class GardenManager():
    name: str
    plant_list: list[Plant]
    plant_count: int
    plants_added: int
    water_tank: int

    def __init__(self, name: str, tank: int, plants: list[Plant] = []
                 ) -> None:
        """Plant Class Initialisation function. Takes and sets
name, height(in cm) and age_d."""
        self.name = name
        self.water_tank = tank
        self.plant_list = []
        self.plant_count = 0
        self.plant_growth = 0
        self.plants_added = 0

        if plants:
            for plant in plants:
                self.plant_count += 1
                (self.plant_list).append(plant)

    def add_plant(self, name: str, water: int, sunlight: int) -> None:
        try:
            self.plant_list.append(Plant(name, water, sunlight))
            self.plant_count += 1
            self.plants_added += 1
            print(f"Added {name} successfully")
        except ValueError as e:
            print("Error adding plant:", e)

    def water_plants(self) -> None:
        print("Opening watering system")
        try:
            for plant in self.plant_list:
                print("Watering", plant.plant_name, "- success")
                self.water_tank -= 1
        except ValueError:
            print(f"Error: Cannot water {plant} - invalid plant!")
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self) -> None:
        for plant in self.plant_list:
            try:
                if not plant.plant_name:
                    raise ValueError("Plant name cannot be empty!")
                if 0 > plant.water_level:
                    raise WaterError(f"Water level {plant.water_level}"
                                     " is too low (min 0)")
                elif plant.water_level > 10:
                    raise WaterError(f"Water level {plant.water_level}"
                                     " is too high (max 10)")
                if 2 > plant.sunlight_hour:
                    raise PlantError(f"Sunlight hours {plant.sunlight_hour}"
                                     "is too low (min 2)")
                elif plant.sunlight_hour > 12:
                    raise PlantError(f"Sunlight hours {plant.sunlight_hour}"
                                     "is too high (max 12)")
                print(f"{plant.plant_name}, (water: {plant.water_level},"
                      f" sun: {plant.sunlight_hour})")
            except GardenError as e:
                print("Error:", e)

    def check_water_tank(self) -> None:
        try:
            if 0 > self.water_tank:
                raise WaterError("Tank is Empty!")
            if 5 > self.water_tank:
                raise WaterError("Not enough water in tank")
            elif self.water_tank > 40:
                raise WaterError("Too much water in tank")
        except GardenError as e:
            print("Caught GardenError:", e)
        finally:
            print("System recovered and continuing...")


def test_garden_management() -> None:
    print("=== Garden Management System ===")

    print()

    print("Adding plants to garden...")

    garden_manager = GardenManager("big garden", 6)

    garden_manager.add_plant("tomato", 5, 8)

    garden_manager.add_plant("lettuce", 15, 5)

    garden_manager.add_plant("", 5, 5)

    print()

    print("Watering plants...")

    garden_manager.water_plants()

    print()

    print("Checking plant health...")

    garden_manager.check_plant_health()

    print()

    print("Testing error recovery...")

    garden_manager.check_water_tank()

    print()

    print("Garden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
