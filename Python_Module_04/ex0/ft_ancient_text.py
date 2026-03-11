#!/usr/bin/env python3

def ft_ancient_text() -> None:
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
    print()
    file_name = "ancient_fragment.txt"

    # file_dir = ""
    # from self, targeting self
    # file_dir = "../data-generator-tools/"
    # from self, targeting data-generator-tools

    # dir = "Python_Module_04/ex0/"
    # from Python_Modules, targeting self
    # dir = "Python_Module_04/data-generator-tools/"
    # from Python_Modules, targeting data-generator-tools

    # dir = "ex0/"
    # from eval, targeting self
    dir = "data-generator-tools/"
    # from eval, targeting data-generator-tools

    print("Accessing Storage Vault:", file_name)
    try:
        text_file = open(dir + file_name)
    except FileNotFoundError as e:
        print(f"File {file_name} was not found.\nError: {e}")
        return
    print("Connection established...")
    print()
    print("RECOVERED DATA:")
    print(text_file.read())
    print()
    print("Data recovery complete. Storage unit disconnected.")
    text_file.close()


if __name__ == "__main__":
    ft_ancient_text()
