def check_temperature(temp_str: str) -> int:
    """Validate and report plant-safe temperature."""
    try:
        value: int = int(temp_str)
    except ValueError:
        raise ValueError(f"Error: '{temp_str}' is not a valid number\n")

    if value < 0:
        raise ValueError(
            f"Error: {value}°C is too cold for plants (min 0°C)\n"
        )

    if value > 40:
        raise ValueError(
            f"Error: {value}°C is too hot for plants (max 40°C)\n"
        )

    return value


def test_temperature_input() -> None:
    """Run temperature validation tests."""
    inputs: list[str] = ["25", "abc", "100", "-50"]

    for input in inputs:
        print(f"Testing temperature: {input}")
        try:
            check_temperature(input)
            print(f"Temperature {input}°C is perfect for plants!\n")
        except ValueError as e:
            print(e)

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    print("=== Garden Temperature Checker ===\n")

    test_temperature_input()
