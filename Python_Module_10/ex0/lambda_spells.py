#!/usr/bin/env python3


def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda x: x["power"], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda x: x["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda x: "* " + x + " *", spells))


def mage_stats(mages: list[dict]) -> dict:
    mages_power = list(map(lambda x: x['power'], mages))
    max_ = max(mages_power)
    min_ = min(mages_power)
    sum_ = sum(mages_power)
    len_ = len(mages_power)
    avg_ = round(sum_ / len_, 2)

    return {"max_power": max_, "min_power": min_, "avg_power": avg_}


def lambda_spells() -> None:

    artifacts = [{'name': 'Light Prism', 'power': 50, 'type': 'accessory'},
        {'name': 'Water Chalice', 'power': 100, 'type': 'relic'},
        {'name': 'Earth Shield', 'power': 40, 'type': 'armor'},
        {'name': 'Shadow Blade', 'power': 3, 'type': 'weapon'}]
    mages = [{'name': 'Ember', 'power': 94, 'element': 'earth'},
        {'name': 'Jordan', 'power': 72, 'element': 'wind'},
        {'name': 'Luna', 'power': 84, 'element': 'ice'},
        {'name': 'Morgan', 'power': 100, 'element': 'water'},
        {'name': 'Sage', 'power': 76, 'element': 'earth'}]
    spells = ['meteor', 'darkness', 'tsunami', 'flash']

    print()

    print("Testing artifact sorter...")
    print("Before:")
    print(artifacts)
    artifacts_sort = artifact_sorter(artifacts)
    print("After:")
    print(artifacts_sort)

    print()

    print("Testing power filter...")
    print("Before:")
    print(mages)
    mages_filter = power_filter(mages, 80)
    print("After:")
    print(mages_filter)

    print()

    print("Testing spell transformer...")
    print("Before:")
    print(spells)
    spells_transformed = spell_transformer(spells)
    print("After:")
    print(spells_transformed)

    print()

    print("Testing mage stats...")
    print("Before:")
    print(mages)
    mages_stats = mage_stats(mages)
    print("After:")
    print(mages_stats)

    print()


if __name__ == "__main__":
    lambda_spells()


"""
=== Exercise 0 Test Data ===
# Lambda Sanctum Test Data
artifacts = [{'name': 'Light Prism', 'power': 108, 'type': 'accessory'},
    {'name': 'Water Chalice', 'power': 83, 'type': 'relic'},
    {'name': 'Earth Shield', 'power': 88, 'type': 'armor'},
    {'name': 'Shadow Blade', 'power': 62, 'type': 'weapon'}]
mages = [{'name': 'Ember', 'power': 94, 'element': 'earth'},
    {'name': 'Jordan', 'power': 72, 'element': 'wind'},
    {'name': 'Luna', 'power': 84, 'element': 'ice'},
    {'name': 'Morgan', 'power': 94, 'element': 'water'},
    {'name': 'Sage', 'power': 76, 'element': 'earth'}]
spells = ['meteor', 'darkness', 'tsunami', 'flash']

=== Exercise 0 Test Data ===
# Lambda Sanctum Test Data
artifacts = [{'name': 'Shadow Blade', 'power': 74, 'type': 'armor'},
    {'name': 'Lightning Rod', 'power': 120, 'type': 'focus'},
    {'name': 'Wind Cloak', 'power': 93, 'type': 'armor'},
    {'name': 'Fire Staff', 'power': 73, 'type': 'focus'}]
mages = [{'name': 'Nova', 'power': 77, 'element': 'water'},
    {'name': 'Rowan', 'power': 93, 'element': 'shadow'},
    {'name': 'Luna', 'power': 76, 'element': 'ice'},
    {'name': 'Storm', 'power': 93, 'element': 'earth'},
    {'name': 'Ash', 'power': 100, 'element': 'lightning'}]
spells = ['darkness', 'freeze', 'earthquake', 'blizzard']
"""
