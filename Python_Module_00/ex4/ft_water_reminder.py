
def ft_water_reminder() -> None:
    print("Days since last watering:", end=" ")
    water = int(input())
    if (water <= 2):
        print("Plants are fine")
    else:
        print("Water the plants!")

# ft_water_reminder()
