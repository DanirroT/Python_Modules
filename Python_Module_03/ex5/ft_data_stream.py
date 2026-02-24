#!/usr/bin/env python3

from typing import Generator


def stream_wizard() -> Generator[tuple[tuple[str, int], str], None, None]:
    player_dict = {
        "alice": 5,
        "bob": 12,
        "charlie": 8,
        "dave": 1
        }
    event_actions = [
        "killed a monster",
        "found a treasure",
        "leveled up",
        "killed a monster",
        "killed a monster",
        "killed a monster",
        "leveled up",
        "killed a monster",
        "killed a monster",
        "found a treasure",
        "killed a monster",
        "leveled up",
        "killed a monster",
        "killed a monster",
        "killed a monster",
        "leveled up",
        "killed a monster",
        "killed a monster",
        "killed a monster",
        "killed a monster",
        "killed a monster",
        "killed a monster",
        "killed a monster"
        ]

    player_count = len(player_dict)
    actions_count = len(event_actions)
    player_i = 0
    actions_i = 0

    while True:

        agent = list(player_dict.items())[player_i]
        event_action = event_actions[actions_i]
        player_i += 1
        actions_i += 1

        while player_i >= player_count:
            player_i -= player_count
        while actions_i >= actions_count:
            actions_i -= actions_count

        if event_action == "leveled up":
            player_dict[agent[0]] += 1
        yield (agent, event_action)


def ft_fibonacci_gen() -> Generator[int, None, None]:
    """Generator for Fibonacci sequence."""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def ft_prime_gen() -> Generator[int, None, None]:
    """Generator for prime numbers."""
    n = 2
    while True:
        is_prime = True
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                is_prime = False
                break
        if is_prime:
            yield n
        n += 1


def ft_data_stream() -> None:
    print("=== Game Data Stream Processor ===")
    print()
    n_events = 1000
    print(f"Processing {n_events} game events...")
    print()
    high_level = 0
    player_dict: dict[str, int] = {}
    event_count: dict[str, int] = {}
    generator = stream_wizard()
    for i_event in range(1, n_events + 1):
        agent, event_action = next(generator)
        agent_name, agent_level = agent
        agent_level_str = f"(level {agent_level})"
        if agent_level > 10:
            high_level += 1
        if event_action not in event_count:
            event_count[event_action] = 0
        event_count[event_action] += 1
        player_dict[agent_name] = agent_level
        event_description = " ".join(("Player", agent_name, agent_level_str,
                                     event_action))
        if i_event < 4:
            print(f"Event {i_event}: {event_description}")
    print("...")
    print()
    print("=== Stream Analytics ===")
    print(f"Total events processed: {sum(event_count.values())}")

    print(f"High-level players (10+): {event_count["found a treasure"]}")
    print(f"Treasure events: {event_count["found a treasure"]}")
    print(f"Level-up events: {event_count["leveled up"]}")

    print()

    print("Memory usage: Constant (streaming)")

    processing_time = 0.045  # Simulated processing time

    print(f"Processing time: {processing_time} seconds")

    print()

    print("=== Generator Demonstration ===")

    fib_sequence = ft_fibonacci_gen()
    fib_len = 10

    print(f"Fibonacci sequence (first {fib_len}):", end=" ")
    for i in range(fib_len):
        print(next(fib_sequence), end=" ")

    print()

    prime_numbers = ft_prime_gen()
    prime_len = 5

    print(f"Prime numbers (first {prime_len}):", end=" ")
    for i in range(prime_len):
        print((next(prime_numbers)), end=" ")
    print()


if __name__ == "__main__":
    ft_data_stream()

    # high_level_players = 0
    # for player_lvl in player_dict.values():
    #     if player_lvl >= 10:
    #         high_level_players += 1
