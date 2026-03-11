#!/usr/bin/env python3

def ft_vault_security() -> None:
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===")
    print()
    clas_name = "classified_data.txt"
    sec_name = "security_protocols.txt"

    # dir = ""
    # from self, targeting self
    # dir = "../data-generator-tools/"
    # from self, targeting data-generator-tools

    # dir = "Python_Module_04/ex3/"
    # from Python_Modules, targeting self
    # dir = "Python_Module_04/data-generator-tools/"
    # from Python_Modules, targeting data-generator-tools

    # dir = "ex3/"
    # from eval, targeting self
    dir = "data-generator-tools/"
    # from eval, targeting data-generator-tools

    # dir = "ex0/"
    # from eval, targeting self
    # dir = "data-generator-tools/"
    # from eval, targeting data-generator-tools

    print("Initiating secure vault access...")
    with open(dir + clas_name, "r") as clas, open(dir + sec_name, "w") as sec:
        print("Vault connection established with failsafe protocols")
        print()
        print("SECURE EXTRACTION:")
        print(clas.read())
        print()
        print("SECURE PRESERVATION:")
        data = "[CLASSIFIED] New security protocols archived"
        print(data)
        sec.write(data)
    print("Vault automatically sealed upon completion")
    print()
    print("All vault operations completed with maximum security.")


if __name__ == "__main__":
    ft_vault_security()
