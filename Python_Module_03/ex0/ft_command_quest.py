#!/usr/bin/env python3

import sys

def ft_command_quest(args: list[str]) -> None:
    print("=== Command Quest ===")
    argc: int = len(args)
    if argc == 1:
        print("No arguments provided!")
    print("Program name:", args[0])
    if argc != 1:
        print("Arguments received:", argc -1)
    i: int = 1
    for arg in args[1:]:
        print(f"Argument {i}:", arg)
        i += 1
    print("Total arguments:", argc)
    


if __name__ == "__main__":
    ft_command_quest(sys.argv)
