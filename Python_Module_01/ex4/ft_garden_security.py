#!/usr/bin/env python3

class SecurePlant():
    """Class to Manage Plants with some inbuilt Saety features.
Has and checks name, height(in cm) and age_d as inbuilt variables."""
    name: str
    _height: int
    _age_days: int

    def __init__(self, name: str, height: int, age_d: int):
        """Plant Class Initialisation function. Takes and sets
name, height(in cm) and age_d."""
        print(f"Plant created: {name}")
        self.name = name
        self.set_height(height)
        self.set_age(age_d)

    def set_height(self, height: int):
        """Sets the Heigth Value of the called upon SecurePlant.
Conteins protection from Negative numbers"""
        if height < 0:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            print(f"Height updated: {height}cm [OK]")
            self._height = height

    def set_age(self, age_d: int):
        """Sets the Age Value of the called upon SecurePlant.
Conteins protection from Negative numbers"""
        if age_d < 0:
            print(f"Invalid operation attempted: age {age_d} days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            print(f"Age updated: {age_d} days [OK]")
            self.age_d = age_d

    def get_height(self):
        """Safely returns the Heigth Value of the called upon SecurePlant."""
        return self._height

    def get_age(self):
        """Safely returns the Age Value of the called upon SecurePlant."""
        return self.age_d


def ft_garden_security():
    """Introduction to Garden Data Security. Uses the SecurePlant Class
to create plant profiles while checking for any miss inputs.
The Security Functions print status messages allong this process."""
    print("=== Garden Security System ===")
    plant = SecurePlant("Rose", 25, 30)
    print()
    plant.set_age(-5)
    print()
    print(f"Current plant: {plant.name}, ({plant.get_height()}cm,",
          f"{plant.get_age()} days)")


if __name__ == "__main__":
    ft_garden_security()
