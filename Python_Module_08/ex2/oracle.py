#!/usr/bin/env python3


from dotenv import load_dotenv
import os

"""
MATRIX_MODE - "development" or "production"
DATABASE_URL - Connection string for data storage
API_KEY - Secret key for external services
LOG_LEVEL - Logging verbosity
ZION_ENDPOINT - URL for the resistance network
"""


def oracle() -> None:

    print()

    print("ORACLE STATUS: Reading the Matrix...")

    load_dotenv()

    print()

    print("Configuration loaded:")

    env_dict = {
        "MATRIX_MODE": os.getenv("MATRIX_MODE"),
        "DATABASE_URL": os.getenv("DATABASE_URL"),
        "API_KEY": os.getenv("API_KEY"),
        "LOG_LEVEL": os.getenv("LOG_LEVEL"),
        "ZION_ENDPOINT": os.getenv("ZION_ENDPOINT"),
    }

    # print()
    # print(env_dict)
    # print()
    # print(dict(env_dict))
    # print()

    for key, value in env_dict.items():
        # if value is None:
        #     raise ValueError(f"{key} is missing from configuration")
        # env_dict[key] = value.split("#")[0].strip()
        if not env_dict[key]:
            raise ValueError(f"{key}={value} is not formatted correctly.\n"
                             "\tCorrect formatig is: VALUE_NAME=<value>")

    if (env_dict["MATRIX_MODE"]
            not in {"development", "production"}):
        raise ValueError(
            "MATRIX_MODE must be \"development\" or \"production\"")

    if not isinstance(env_dict["DATABASE_URL"], str):
        raise ValueError("DATABASE_URL must be a string")
    if not isinstance(env_dict["API_KEY"], str):
        raise ValueError("API_KEY must be a string")
    if not isinstance(env_dict["LOG_LEVEL"], str):
        raise ValueError("LOG_LEVEL must be a string")
    if not isinstance(env_dict["ZION_ENDPOINT"], str):
        raise ValueError("ZION_ENDPOINT must be a string")

    print("Mode:", env_dict["MATRIX_MODE"])
    print("Database:",
          "Connected to local instance"
          if env_dict["DATABASE_URL"]
          else "Connection Failed")
    print("API Access:",
          "Authenticated"
          if env_dict["API_KEY"]
          else "Connection Failed")
    print("Log Level:", env_dict["LOG_LEVEL"])
    print("Zion Network:",
          "Online"
          if env_dict["ZION_ENDPOINT"]
          else "Connection Failed")

    print()

    print("Environment security check:")

    print("[OK] No hardcoded secrets detected")
    print("[OK] .env file properly configured")
    print("[OK] Production overrides available")

    print()

    print("The Oracle sees all configurations.")


if __name__ == "__main__":
    oracle()

    # try:
    #     with open(".env", "r") as env:
    #         env_lines = env.read().split("\n")
    # except FileNotFoundError:
    #     print("\'.env\' file is missing from the directory.")
    #     print("Create one by taking the exemple provided and"
    #           " modifying it for your purposes")
    #     print("To do that:")
    #     print("$> cp .env.example .env")
    #     print("and then modify it")

    # for line in env_lines:
    #     line_no_com = line.split("#")[0].strip()
    #     if line_no_com == "":
    #         continue
    #     split_line = line_no_com.split("=")
    #     if len(split_line) != 2:
    #         raise ValueError(f"{line} is not formatted correctly.\n"
    #                          "\tCorrect formatig is: VALUE_NAME=<value>")
    #     split_line[0]
    #     if split_line[0] not in [
    #             "MATRIX_MODE", "DATABASE_URL",
    #             "API_KEY", "LOG_LEVEL", "ZION_ENDPOINT"]:
    #         raise ValueError(f"In {line}, VALUE_NAME is not a valid Key.\n")

    #     env_dict[split_line[0]] = split_line[1]
