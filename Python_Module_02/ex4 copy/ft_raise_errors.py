#!/usr/bin/env python3

def check_plant_health(plant_name: str,
                       water_level: int,
                       sunlight_hour: int
                       ) -> None:
    try:
        if plant_name == "":
            raise ValueError("Plant name cannot be empty!")
        if 0 > water_level:
            raise ValueError(f"Water level {water_level} is too low (min 0)")
        elif water_level > 10:
            raise ValueError(f"Water level {water_level} is too high (max 10)")
        if 2 > sunlight_hour:
            raise ValueError(f"Water level {sunlight_hour} is too low (min 2)")
        elif sunlight_hour > 12:
            raise ValueError("Water level",
                             sunlight_hour,
                             "is too high (max 12)")
        print(f"Plant '{plant_name}' is healthy!")
    except ValueError as e:
        print("Error:", e)


def test_plant_checks() -> None:
    print("=== Garden Plant Health Checker ===")

    print()

    print("Testing good values...")

    check_plant_health("tomato", 5, 5)

    print()

    print("Testing empty plant name...")

    check_plant_health("", 5, 5)

    print()

    print("Testing bad water level...")

    # check_plant_health("tomato", -5, 5)
    check_plant_health("tomato", 15, 5)

    print()

    print("Testing bad sunlight hours...")

    check_plant_health("tomato", 5, 0)
    # check_plant_health("tomato", 5, 24)

    print()

    print("All error raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()
