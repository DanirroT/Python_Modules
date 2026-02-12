
def ft_seed_inventory(
        seed_type: str,
        quantity: int,
        unit: str) -> None:
    quantity_str = str(quantity)
    if unit == "packets":
        unit_output = quantity_str + " packets available"
    elif unit == "grams":
        unit_output = quantity_str + " grams total"
    elif unit == "area":
        unit_output = "covers " + quantity_str + " square meters"
    else:
        print("Unknown unit type")
        return
    print(seed_type.capitalize(), "seeds:", unit_output)

# ft_seed_inventory("tomato", 15, "packets")
# print()
# print()
# ft_seed_inventory("carrot", 8, "grams")
# print()
# print()
# ft_seed_inventory("lettuce", 12, "area")
# print()
# print()
# ft_seed_inventory("onion", 4, "bulbs")
