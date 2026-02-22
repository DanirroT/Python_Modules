#!/usr/bin/env python3

def validate_ingredients(ingredients: str) -> str:
    ingredients_split = ingredients.lower().split(" ")
    valid = False
    for ingredient in ingredients_split:
        if ingredient.strip() in ["fire", "water", "earth", "air"]:
            valid = True
    if valid:
        return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
