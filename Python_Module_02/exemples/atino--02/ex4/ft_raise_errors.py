def check_plant_health(
    plant_name: str,
    water_level: int,
    sunlight_hours: int
) -> None:
    """Check plant health and raise errors when invalid."""
    is_empty: bool = True
    for char in plant_name:
        if char != " ":
            is_empty = False
            break

    if plant_name == "" or is_empty:
        raise ValueError("Error: Plant name cannot be empty!")

    water_bad: bool = water_level < 1 or water_level > 10
    sunlight_bad: bool = sunlight_hours < 2 or sunlight_hours > 12
    if water_bad and sunlight_bad:
        raise ValueError(
            f"Error: Both values are out of range!\n"
            f"Water level should be 1-10 (got {water_level}),\n"
            f"Sunlight hours should be 2-12 (got {sunlight_hours})"
        )

    if water_level < 1:
        raise ValueError(
            f"Error: Water level {water_level} is too low (min 1)"
        )
    if water_level > 10:
        raise ValueError(
            f"Error: Water level {water_level} is too high (max 10)"
        )

    if sunlight_hours < 2:
        raise ValueError(
            f"Error: Sunlight hours {sunlight_hours} is too low (min 2)"
        )
    if sunlight_hours > 12:
        raise ValueError(
            f"Error: Sunlight hours {sunlight_hours} is too high (max 12)"
        )

    valid_plants: list[str] = ["tomato", "lettuce", "carrot"]
    if plant_name not in valid_plants:
        raise ValueError(f"'{plant_name}' is not a valid plant")
    print(f"Plant '{plant_name}' is healthy!")


def test_plant_checks() -> None:
    """Demonstrate raising and catching errors."""
    print("Testing good values...")
    try:
        check_plant_health("tomato", 8, 5)
    except ValueError as e:
        print(e)

    print("\nTesting empty plant name...")
    try:
        check_plant_health("", 8, 5)
    except ValueError as e:
        print(e)

    print("\nTesting bad water level...")
    try:
        check_plant_health("lettuce", 15, 5)
    except ValueError as e:
        print(e)

    print("\nTesting bad sunlight hours...")
    try:
        check_plant_health("carrot", 8, 0)
    except ValueError as e:
        print(e)

    print("\nAll error raising tests completed!")


if __name__ == "__main__":
    print("=== Garden Plant Health Checker ===\n")

    test_plant_checks()
