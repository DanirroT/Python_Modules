#!/usr/bin/env python3

from typing import Any


def test_error_types(error_list: list[tuple[str, str]],
                     error_type: str | None = None,
                     error_msg: str | None = None,
                     end: bool = False
                     ) -> list[tuple[str, str]]:
    if end:
        if len(error_list) == 0:
            return error_list
        if len(error_list) == 1:
            print(f"Caught {error_list[0][0]}: {error_list[0][1]}")
            return error_list
        else:
            print("Caught an error, but program continues!")
            return error_list

    error_list.append((error_type, error_msg))
    return error_list


def operation(input_t: tuple[str | int, str | int]) -> str | None:
    error_list: list[tuple[str, str]] = []
    result: int | None = None
    try:
        num1: int = int(input_t[0])
    except ValueError:
        error_list = test_error_types(error_list,
                                      "ValueError",
                                      "invalid literal for int()")
        num1 = 0

    try:
        num2: int = int(input_t[1])
    except ValueError:
        error_list = test_error_types(error_list,
                                      "ValueError",
                                      "invalid literal for int()")
        num2 = 0

    try:
        result = num1 // num2
    except ZeroDivisionError:
        error_list = test_error_types(error_list,
                                      "ZeroDivisionError",
                                      "division by zero")

    test_error_types(error_list, end=True)
    if len(error_list) > 0:
        return None
    return str(result)


def read_file(file_name: str) -> str | None:
    error_list: list[tuple[str, str]] = []
    result = None
    try:
        file = open(file_name)
    except FileNotFoundError:
        test_error_types(error_list,
                         "FileNotFoundError",
                         "No such file \'missing.txt\'")
        test_error_types(error_list, end=True)
        return None

    print("File has been opened")
    result = file.read(10)
    file.close()
    print("File has been closed")
    return str(result)


def read_dict_3(input_d: dict[str | int, str | int]) -> str | None:
    error_list: list[tuple[str, str]] = []
    result = []
    for i in ["missing\\_plant", "2", "3"]:
        try:
            result.append(input_d[i])
        except KeyError as e:
            test_error_types(error_list, "KeyError", str(e.args[0]))
            test_error_types(error_list, end=True)
            return None

    test_error_types(error_list, end=True)
    return str(result)


def garden_operations(mode: str, input_val: Any) -> None:
    output = None
    if mode == "op":
        output = operation(input_val)
    elif mode == "file":
        output = read_file(input_val)
    elif mode == "dict":
        output = read_dict_3(input_val)
    if output is not None:
        print("output:", output)


def ft_different_errors() -> None:
    print("=== Garden Error Types Demo ===")
    print()
    print("Testing ValueError...")
    # garden_operations("op", ("10", "2"))
    garden_operations("op", ("abc", "2"))
    print()
    print("Testing ZeroDivisionError...")
    # garden_operations("op", ("1", "2"))
    garden_operations("op", ("1", "0"))
    print()
    print("Testing FileNotFoundError...")
    # garden_operations("file", "preset.txt")
    garden_operations("file", "missing.txt")
    print()
    print("Testing KeyError...")

    # num1 = {"missing\\_plant": "one", "2": "two", "3": "three"}
    num2 = {"1": "one", "2": "two", "3": "three"}

    # garden_operations("dict", num1)
    garden_operations("dict", num2)
    print()
    print("Testing multiple errors together...")
    # garden_operations("op", ("1", "2"))
    garden_operations("op", ("1", "abc"))
    print()
    print("All error types tested successfully!")


if __name__ == "__main__":
    ft_different_errors()
