#!/usr/bin/env python3

import os
# from _ import site modules


"""
outside

_ : /usr/bin/python3
"""

"""
inside

VIRTUAL_ENV : /home/tribeirinho/42/Python_Modules/.venv  # extra!!

VIRTUAL_ENV_PROMPT : (.venv)  # extra!!

PATH : /home/tribeirinho/42/Python_Modules/.venv/bin  # extra!!

_ : /home/tribeirinho/42/Python_Modules/.venv/bin/python3  # Changed!!
"""


def construct():

    environment = os.environ

    # for key, value in os.environ.items():
    #     print(key, ":", value)
    #     print()

    environment_path = environment.get("VIRTUAL_ENV")
    current_puython = environment["_"]

    if not environment_path:

        matrix_status = "You're still plugged in"
        viritual_environment = "None detected"
        main_status_message = "WARNING: You're in the global environment!"
        main_message = "The machines can see everything you install."

    else:

        matrix_status = "Welcome to the construct"
        # print("1", environment["VIRTUAL_ENV_PROMPT"])
        viritual_environment = environment["VIRTUAL_ENV_PROMPT"][2:-2]
        # print("2", viritual_environment)
        main_status_message = "SUCCESS: You're in an isolated environment!"
        main_message = ("Safe to install packages without "
                        "affecting the global system.")

    print()

    print("MATRIX STATUS:", matrix_status)

    print()

    print("Current Python:", current_puython)
    print("Virtual Environment:", viritual_environment)
    if environment_path:
        print("Environment Path:", environment_path)

    print()

    print(main_status_message)
    print(main_message)
    print()

    if not environment_path:

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
        # print(viritual_environment)

        for path in environment["PATH"].strip().split(":"):
            # print(path)
            if viritual_environment in path:
                installation_path = path[:-3]
                break

        print("Package installation path:")
        print(installation_path, "lib/python3.11/site-packages", sep="")


if __name__ == "__main__":
    construct()
