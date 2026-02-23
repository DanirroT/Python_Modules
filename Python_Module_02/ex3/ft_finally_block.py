#!/usr/bin/env python3

def water_plants(plant_list: list[str]) -> None:
    print("Opening watering system")
    try:
        for plant in plant_list:
            if plant.__class__.__name__ != "str":
                raise ValueError
            print("Watering", plant)
        print("Watering completed successfully!")
    except ValueError:
        print(f"Error: Cannot water {plant} - invalid plant!")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system() -> None:
    print("=== Garden Watering System ===")

    print()

    print("Testing normal watering...")

    water_plants(["tomato", "lettuce", "carrots"])

    print()

    print("Testing with error...")

    water_plants(["tomato", None, "carrots"])

    print()

    print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
