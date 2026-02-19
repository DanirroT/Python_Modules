#!/usr/bin/env python3

def check_temperature(temp_str: str) -> int:
    """Checks if the String given is numeric and reasonable (0 < T < 40)."""
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


print("outout:", check_temperature("12"))
print()
print("outout:", check_temperature("0"))
print()
print("outout:", check_temperature("40"))
print()
print("outout:", check_temperature("123"))
print()
print("outout:", check_temperature("-1"))
print()
print("outout:", check_temperature("twelve"))
print()

try:
    raise ValueError()
except ValueError as e:
    print(e)
