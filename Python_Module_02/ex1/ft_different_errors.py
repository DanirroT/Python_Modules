#!/usr/bin/env python3

def test_error_types(error_list: list[tuple[str, str]], error_type: str | None = None, error_msg: str | None = None, end: bool = False) -> list[tuple[str, str]]:
    if end:
        if len(error_list) == 0:
            return error_list
        if len(error_list) == 1:
            print(f"Caught {error_list[0]}: {error_list[1]}")
        else:
            print("Testing multiple errors together...")

    error_list.append((error_type, error_msg))
    return error_list


def operation(input: tuple[str | int, str | int]) -> str | None:
    error_list: list[tuple[str, str]] = []
    result: int | None = None
    try:
        num1: int = int(input[0])
    except ValueError as e:
        error_list = test_error_types(error_list, "ValueError", e)

    try:
        num2: int = int(input[1])
    except ValueError as e:
        error_list = test_error_types(error_list, "ValueError", e)

    try:
        if num1 is NaN or  num2
        result = num1 // num2
    except ZeroDivisionError as e:
        error_list = test_error_types(error_list, "ZeroDivisionError", e)

    test_error_types(error_list, end=True)
    return str(result)


def read_file(file_name: str) -> str | None:
    error_list: list[tuple[str, str]] = []
    result = None
    try:
        file = open(file_name)
    except FileNotFoundError as e:
        test_error_types(error_list, "FileNotFoundError", e)

    print("File has been opened")
    result = file.read(10)
    file.close()
    print("File has been closed")
    return str(result)


def read_dict_3(input: tuple[str | int, str | int]) -> str | None:
    error_list: list[tuple[str, str]] = []
    result = None
    try:
        num1: int = int(input[0])
    except ValueError as e:
        test_error_types(error_list, "ValueError", e)

    try:
        num2: int = int(input[1])
    except ValueError:
        test_error_types(error_list, "ValueError", e)
    
    try:
        result = num1 / num2
    except ZeroDivisionError:
        test_error_types(error_list, "ZeroDivisionError", e)

    test_error_types(error_list, end=True)
    return str(result)


def garden_operations(mode: str,
                      input: tuple[str | int, str | int]
                      | str | dict[int, str]
                      ) -> str | None:
    print(input)
    output = None
    if mode == "op":
        output = operation(input)
    elif mode == "file":
        output = read_file(input)
    elif mode == "dict":
        output = read_dict_3(input)
    return output


print("=== Garden Error Types Demo ===")
print()
print("Testing ValueError...")
garden_operations("op", ("1", "2"))
garden_operations("op", ("1", "abc"))
print()
print("Testing ZeroDivisionError...")
garden_operations("op", ("1", "2"))
garden_operations("op", ("1", "0"))
print()
print("Testing FileNotFoundError...")
garden_operations("file", 1)
garden_operations("file", "abc")
print()
print("Testing KeyError...")

num1 = {1: "one", 2: "two", 3: "three"}
num2 = {4: "one", 5: "two", 6: "three"}

garden_operations("dict", num1)
garden_operations("dict", num2)
print()
print("Testing multiple errors together...")
garden_operations("op", ("1", "2"))
garden_operations("op", ("abc", "0"))
print("Caught an error, but program continues!")
print()
print("All error types tested successfully!")