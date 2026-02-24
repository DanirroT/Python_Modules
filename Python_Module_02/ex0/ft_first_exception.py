#!/usr/bin/env python3

def check_temperature(temp_str: str) -> None:
    """
    Checks if the String given (Temprature)
    is numeric and reasonable (0 < T < 40).
    """
    try:
        out_int: int = int(temp_str)
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")
        return
    if 0 > out_int:
        print(f"Error: {temp_str}°C is too cold for plants (min 0°C)")
        return
    if out_int > 40:
        print(f"Error: {temp_str}°C is too hot for plants (max 40°C)")
        return
    print(f"Temperature {out_int}°C is perfect for plants!")


def test_temperature_input() -> None:
    """Run temperature validation tests."""

    print("=== Garden Temperature Checker ===")

    print()

    inputs: list[str] = ["25", "0", "abc", "100", "-50"]

    for input in inputs:

        print(f"Testing temperature: {input}")

        check_temperature(input)

        print()

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":

    test_temperature_input()
