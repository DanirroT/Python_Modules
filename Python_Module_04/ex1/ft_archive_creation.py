#!/usr/bin/env python3

def ft_archive_creation():
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===")
    print()
    file_name = "new_discovery.txt"

    print("Initializing new storage unit:", file_name)
    # try:
    text_file = open(file_name, "w")
    # except FileNotFoundError:
    #     text_file = open(file_name, "x")
    print("Storage unit created successfully...")
    print()
    print("Inscribing preservation data...")
    data = """[ENTRY 001] New quantum algorithm discovered
[ENTRY 002] Efficiency increased by 347%
[ENTRY 003] Archived by Data Archivist trainee"""
    print(data)
    text_file.write(data)
    print()
    print("Data recovery complete. Storage unit disconnected.")
    text_file.close()


if __name__ == "__main__":
    ft_archive_creation()
