def garden_operations(error: str) -> None:
    print(f"Testing {error}...")
    error_list = []
    if error == "ValueError":
        int("abc")
        error_list.append(e)

    elif error == "ZeroDivisionError":
        10 / 0

    elif error == "FileNotFoundError":
        open("missing.txt")
        erro

    elif error == "KeyError":
        plants = {"rose": 1, "violet": 2}
        print(plants['missing_plant'])

    elif error == "multiple errors together":
        try:
            int("abc")
            10 / 0
        except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError) as e:
            print("Caught an error, but program continues!", e)


def test_error_types(error: str) -> None:
    try:
        garden_operations(error)

    except ValueError as e:
        print(f"Caught ValueError: {e}")

    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}")

    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: {e}")

    except KeyError as e:
        print(f"Caught KeyError: {e}")
    print()


def main() -> None:
    print("=== Garden Error Types Demo ===\n")
    for err in ["abc", 1/0, 1,
                "KeyError", "multiple errors together"]:
        test_error_types(str_int, div_zero, file_name)
    print("All error types tested successfully!")


if __name__ == "__main__":
    main()
