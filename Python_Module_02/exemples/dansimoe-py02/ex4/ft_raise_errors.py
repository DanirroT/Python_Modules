def check_plant_health(plant_name: str, water_level: int,
                       sunlight_hours: int) -> str:
    if not plant_name:
        raise ValueError("Plant name cannot be empty!")
    if water_level < 1:
        raise ValueError(f"Water level {water_level} is too low (min 1)")
    if water_level > 10:
        raise ValueError(f"Water level {water_level} is too high (max 10)")
    if sunlight_hours < 2:
        raise ValueError(f"Sunlight hours {sunlight_hours} is too low (min 2)")
    if sunlight_hours > 12:
        raise ValueError(
            f"Sunlight hours {sunlight_hours} is too high (max 12)")

    return f"Plant {plant_name} is healthy"


def test_plant_checks(plant_name: str, water_level: int,
                      sunlight_hours: int) -> None:
    try:
        status: str = check_plant_health(plant_name,
                                         water_level,
                                         sunlight_hours)
    except ValueError as e:
        print(f"Error: {e}")
    else:
        print(status)


def main() -> None:
    print("=== Garden Plant Health Checker ===\n")

    print("Testing good values...")
    test_plant_checks("tomato", 5, 5)

    print("\nTesting empty plant name...")
    test_plant_checks(None, 5, 5)

    print("\nTesting bad water level...")
    test_plant_checks("tomato", 15, 5)

    print("\nTesting bad sunlight hours...")
    test_plant_checks("tomato", 5, 0)
    print("\nAll error raising tests completed!")


if __name__ == "__main__":
    main()
