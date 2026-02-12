
def day_loop(day: int, max: int) -> None:
    if day > max:
        return
    print(f"Day {day}")
    day_loop(day + 1, max)


def ft_count_harvest_recursive() -> None:
    print("Days until harvest:", end=" ")
    max = int(input())
    day_loop(1, max)
    print("Harvest Time!")

# ft_count_harvest_recursive()
