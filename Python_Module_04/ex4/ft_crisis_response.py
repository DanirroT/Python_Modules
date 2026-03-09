#!/usr/bin/env python3

def ft_crisis_response() -> None:
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")
    print()
    files_to_access = [
        "lost_archive.txt",
        "classified_vault.txt",
        "standard_archive.txt"]

    # dir = ""
    # from self, targeting self
    # dir = "../data-generator-tools/"
    # from self, targeting data-generator-tools

    # dir = "Python_Module_04/ex4/"
    # from Python_Module_04, targeting self
    dir = "Python_Module_04/data-generator-tools/"
    # from Python_Module_04, targeting data-generator-tools

    for file_name in files_to_access:
        try:
            with open(dir + file_name, "r") as text_file:
                print(f"ROUTINE ACCESS: Attempting access to '{file_name}'...")
                print(f"SUCCESS: Archive recovered - ``{text_file.read()}``")
                print("STATUS: Normal operations resumed")
        except FileNotFoundError:
            print(f"CRISIS ALERT: Attempting access to '{file_name}'...")
            print("RESPONSE: Archive not found in storage matrix")
            print("STATUS: Crisis handled, system stable")
        except PermissionError:
            print(f"CRISIS ALERT: Attempting access to '{file_name}'...")
            print("RESPONSE: Security protocols deny access")
            print("STATUS: Crisis handled,  security maintained")
        finally:
            print()
    print("All crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    ft_crisis_response()
