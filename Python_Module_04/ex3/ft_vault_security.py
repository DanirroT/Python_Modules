#!/usr/bin/env python3

def ft_vault_security():
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===")
    print()
    clas_name = "classified_data.txt"
    sec_name = "security_protocols.txt"

    # dir = ""
    # from self, targeting self
    dir = "../data-generator-tools/"
    # from self, targeting data-generator-tools

    # dir = "Python_Module_04/ex0/"
    # from Python_Module_04, targeting self
    dir = "Python_Module_04/data-generator-tools/"
    # from Python_Module_04, targeting data-generator-tools

    print("Initiating secure vault access...")
    with open(dir + clas_name, "r") as clas, open(dir + sec_name, "r") as sec:
        print("Vault connection established with failsafe protocols")
        print()
        print("SECURE EXTRACTION:")
        print(clas.read())
        print()
        print("SECURE PRESERVATION:")
        print(sec.read())
    print("Vault automatically sealed upon completion")
    print()
    print("All vault operations completed with maximum security.")


if __name__ == "__main__":
    ft_vault_security()
