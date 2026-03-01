#!/usr/bin/env python3

import sys, os
from _ import site modules


def construct():

    in_vm = True

    if not in_vm:

        matrix_status = "You're still plugged in"
        current_puython = ""
        viritual_environment = "None detected"
        environment_path = ""
        main_status_message = "WARNING: You're in the global environment!"
        main_message = "The machines can see everything you install."

    else:

        matrix_status = "Welcome to the construct"
        current_puython = ""
        viritual_environment = ""
        environment_path = ""
        main_status_message = "SUCCESS: You're in an isolated environment!"
        main_message = "Safe to install packages without affecting the global system."


    print("MATRIX STATUS:", matrix_status)

    print()

    print("Current Python:", current_puython)
    print("Virtual Environment:", viritual_environment)
    print("Environment Path:", environment_path)

    print()

    print(main_status_message)
    print(main_message)
    print()

    if not in_vm:

        env_name = "matrix_env"

        print("To enter the construct, run:")

        print("python -m venv", env_name)
        print(f"source {env_name}/bin/activate # On Unix")

        print("matrix_env")
        print("Scripts")
        print("activate # On Windows")

        print()

        print("Then run this program again.")

    else:

        print("Package installation path:")
        print("/path/to/matrix_env/lib/python3.11/site-packages")


if __name__ == "__main__":
    construct()
