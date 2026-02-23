def garden_operations(operation: str) -> None:
    """Demonstrate operations that can cause different errors."""
    if operation == "ValueError":
        int("abc")

    elif operation == "ZeroDivisionError":
        5 / 0

    elif operation == "FileNotFoundError":
        open("missing.txt")

    elif operation == "KeyError":
        data: dict = {}
        data["missing_plant"]

    else:
        int("abc")
        5 / 0
        open("missing.txt")
        data: dict = {}
        data["missing_plant"]

def test_error_types() -> None:
    """Test and catch different error types."""
    print("Testing ValueError...")
    try:
        garden_operations("ValueError")
    except ValueError as e:
        print(f"Caught ValueError: {e}\n")

    print("Testing ZeroDivisionError...")
    try:
        garden_operations("ZeroDivisionError")
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}\n")

    print("Testing FileNotFoundError...")
    try:
        garden_operations("FileNotFoundError")
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: {e}\n")

    print("Testing KeyError...")
    try:
        garden_operations("KeyError")
    except KeyError as e:
        print(f"Caught KeyError: {e}\n")

    print("Testing multiple errors together...")
    try:
        garden_operations("")
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError) as e:
        print("Caught an error, but program continues!\n")

    print("All error types tested successfully!")


if __name__ == "__main__":
    print("=== Garden Error Types Demo ===\n")

    test_error_types()
