#!/usr/bin/env python3

def check_temperature(temp_str: str) -> int:
    """Checks if the String given (Temprature) is numeric and reasonable (0 < T < 40)."""
    print("input:", temp_str)
    try:
        out_int: int = int(temp_str)
    except ValueError as e:
        print(f"Error: '{temp_str}' is not a valid number", e)
        return None
    if 0 > out_int:
        print(f"Error: {temp_str}°C is too cold for plants (min 0°C)")
        return None
    if out_int > 40:
        print(f"Error: {temp_str}°C is too hot for plants (max 40°C)")
        return None
    print(f"Temperature {out_int}°C is perfect for plants!")
    return out_int


def test_temperature_input() -> None:
    """Run temperature validation tests."""

    print("=== Garden Temperature Checker ===\n")

    inputs: list[str] = ["25", "0", "abc", "100", "-50"]

    for input in inputs:
        print(f"Testing temperature: {input}")
        try:
            check_temperature(input)
            print(f"Temperature {input}°C is perfect for plants!\n")
        except ValueError as e:
            print(e)

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":

    test_temperature_input()
