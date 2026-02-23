def water_plants(plant_list: list) -> None:
    """Water plants and always clean up."""
    valid_plants: list[str] = ["tomato", "lettuce", "carrots"]
    try:
        print("Opening watering system")
        for plant in plant_list:
            if plant not in valid_plants:
                raise ValueError
            print(f"Watering {plant}")
        print("Watering completed successfully!")

    except ValueError:
        print(f"Error: Cannot water {plant} - invalid plant!")

    finally:
        print("\nClosing watering system (cleanup)")


def test_watering_system() -> None:
    """Demonstrate finally block behavior."""
    print("\nTesting normal watering...")
    good_plants: list[str] = ["tomato", "lettuce", "carrots"]
    water_plants(good_plants)

    print("\nTesting with error...")
    bad_plants: list[str] = ["tomato", None, "lettuce"]
    water_plants(bad_plants)

    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    print("=== Garden Watering System ===")

    test_watering_system()
