def water_plants(plant_list: list[str]) -> None:
    print("Opening watering system")
    try:
        for plant in plant_list:
            if plant not in {"tomato", "lettuce", "carrots"}:
                raise ValueError(f"{plant}")
            print(f"Watering {plant}")

    except ValueError as e:
        print(f"Error: Cannot water {e} - invalid plant!")

    finally:
        print("Closing watering system (cleanup)")


def test_watering_system() -> None:
    print("Testing normal watering...")
    water_plants(["tomato", "lettuce", "carrots"])
    print("Watering completed successfully!\n")

    print("Testing with error...")
    water_plants(["tomato", None, "lettuce"])

    print("\nCleanup always happens, even with errors!")


def main() -> None:
    print("=== Garden Watering System ===\n")
    test_watering_system()


if __name__ == "__main__":
    main()
