#!/usr/bin/env python3


class InventoryMaster():
    """
    Class to Manage Inventory. Conteins only inventory as inbuilt variable.
    """

    inventory: dict[str, int]

    def __init__(self, inventory: dict[str, int] = {}) -> None:
        """
        Plant Class Initialisation function. Takes and sets
        name, kill_count, level. sets achivements to empty set.
        if any acivements are detected based on level or killcount, adds them
        to the achivements set."""
        self.inventory = inventory.copy()

    def add_items(self, items: dict[str, int]) -> None:
        for name in items:
            if not name or name == "":
                raise ValueError("Item name cannot be empty.")
            if name not in self.inventory:
                self.inventory[name] = 0
            add_val = int(items[name])
            if add_val < 0:
                print(f"Warning: Negative quantity for '{name}': {add_val}.")
            self.inventory[name] += add_val

    def subtract_items(self, items: dict[str, int]) -> None:
        for name in items:
            if name not in self.inventory:
                continue
            add_val = int(items[name])
            if add_val < 0:
                print(f"Warning: Negative quantity for '{name}': {add_val}.")
            self.inventory[name] -= add_val
            if self.inventory[name] <= 0:
                if self.inventory[name] < 0:
                    print(f"Error: Quatity of '{name}' went negative:"
                          f" {self.inventory[name]}.")
                self.inventory.pop(name)

    def ft_analyze_inventory(self) -> None:
        print("=== Inventory System Analysis ===")
        item_count = 0
        for name in self.inventory:
            item_count += self.inventory[name]
        item_type_count = len(self.inventory)
        print(f"Total items in inventory: {item_count}")
        print(f"Unique item types: {item_type_count}")
        print()
        print("=== Current Inventory ===")
        for name, quant in sorted(self.inventory.items(),
                                  key=lambda item: item[1],
                                  reverse=True
                                  ):
            percentage = (quant / item_count) * 100
            print(f"{name}: {quant} units ({percentage:.1f}%)")
        print()

        print("=== Inventory Statistics ===")
        most_abundant = max(self.inventory, key=self.inventory.get)
        least_abundant = min(self.inventory, key=self.inventory.get)
        print(f"Most abundant: {most_abundant}",
              f"({self.inventory[most_abundant]} units)")
        print(f"Least abundant: {least_abundant}",
              f" ({self.inventory[least_abundant]} units)")
        print()
        print("=== Inventory Classification ===")
        abundent_quantity = {}
        moderate_quantity = {}
        scarse_quantity = {}
        for name in self.inventory:
            if self.inventory[name] > 10:
                abundent_quantity[name] = self.inventory[name]
            elif self.inventory[name] > 3:
                moderate_quantity[name] = self.inventory[name]
            else:
                scarse_quantity[name] = self.inventory[name]
        if abundent_quantity:
            print("Abundant:", abundent_quantity)
        if moderate_quantity:
            print("Moderate:", moderate_quantity)
        if scarse_quantity:
            print("Scarce:", scarse_quantity)

        print()
        print("=== Management Suggestions ===")
        print("Restock needed:", ", ".join([item for item in self.inventory
                                           if self.inventory[item] == 1]))

    def demo(self) -> None:
        print("=== Dictionary Properties Demo ===")
        print("Inventory keys:", ", ".join(self.inventory.keys()))
        print("Inventory values:", ", ".join(map(str,
                                                 self.inventory.values())))
        lookup = "sword"
        print(f"Sample lookup - '{lookup}' in inventory:",
              lookup in self.inventory)


def ft_inventory_system() -> None:
    inventory_manager = InventoryMaster({
            "sword": 1,
            "potion": 5,
            "shield": 2,
            "armor": 3,
            "helmet": 1})

    inventory_manager.ft_analyze_inventory()
    print()
    inventory_manager.demo()

    # inventory_manager.add_items({"potion": 3, "sword": 2, "bow": 4})
    # inventory_manager.ft_analyze_inventory()

    # inventory_manager.subtract_items({"potion": 10, "sword": 2, "bow": 4})
    # inventory_manager.ft_analyze_inventory()


if __name__ == "__main__":
    ft_inventory_system()

# 'alice':
    # {'items':

    # {'pixel_sword': 1',
    # 'code_bow': 1',
    # 'health_byte': 1',
    # 'quantum_ring': 3}',

    # 'total_value': 1875',
    # 'item_count': 6}',

    # 'bob': {'items': {'code_bow': 3',
    # 'pixel_sword': 2}',

    # 'total_value': 900',
    # 'item_count': 5}',

    # 'charlie':
    # {'items':

    # {'pixel_sword': 1',
    # 'code_bow': 1}',

    # 'total_value': 350',
    # 'item_count': 2}',

    # 'diana':
    # {'items':

    # {'code_bow': 3',
    # 'pixel_sword': 3',
    # 'health_byte': 3',
    # 'data_crystal': 3}',

    # 'total_value': 4125',
    # 'item_count': 12}}',

    # 'catalog':
    # {'pixel_sword':
    #   {'type': 'weapon'',
    #   'value': 150',
    #   'rarity': 'common'}',,
    # 'health_byte':
    #   {'type': 'consumable'',
    #   'value': 25',
    #   'rarity': 'common'}',
    # 'code_bow':
    #   {'type': 'weapon'',
    #   'value': 200',
    #   'rarity': 'uncommon'}
    # 'quantum_ring':
    #   {'type': 'accessory'',
    #   'value': 500',
    #   'rarity': 'rare'}'
    # 'data_crystal':
    #   {'type': 'material'',
    #   'value': 1000',
    #   'rarity': 'legendary'}',
    # }}
