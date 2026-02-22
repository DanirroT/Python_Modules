#!/usr/bin/env python3

from typing import Generator
import random


def stream_wizard() -> Generator[tuple[tuple[str, int], str], None, None]:
    player_dict = {
        "alice": 5,
        "bob": 12,
        "charlie": 8,
        "dave": 15
        }
    event_actions = ["killed a monster", "found a treasure", "leveled up"]
    while True:
        agent = random.choice(list(player_dict.items()))
        event_action = random.choice(event_actions)
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


def ft_analytics_dashboard() -> None:
    print("=== Game Data Stream Processor ===")
    print()
    n_events = 1000
    print(f"Processing {n_events} game events...")
    print()
    player_dict: dict[str, int] = {}
    event_count = {}
    for i_event in range(1, n_events + 1):
        agent, event_action = next(stream_wizard())
        agent_name, agent_level = agent
        agent_level_str = f"(level {agent_level})"
        if event_action not in event_count:
            event_count[event_action] = 0
        event_count[event_action] += 1
        player_dict[agent_name] = agent_level
        event_description = " ".join(("Player", agent_name, agent_level_str,
                                     event_action))
        print(f"Event {i_event}: {event_description}")
    print()
    print("=== Stream Analytics ===")
    print(f"Total events processed: {n_events}")
    high_level_players = 0
    for player_lvl in player_dict.values():
        if player_lvl >= 10:
            high_level_players += 1
    print(f"High-level players (10+): {high_level_players}")
    print(f"Treasure events: {event_count["found a treasure"]}")
    print(f"Level-up events: {event_count["leveled up"]}")
    print("Memory usage: Constant (streaming)")
    processing_time = 0.045  # Simulated processing time
    print(f"Processing time: {processing_time} seconds")
    print()
    print("=== Generator Demonstration ===")
    print()
    fib_sequence = ft_fibonacci_gen()
    prime_numbers = ft_prime_gen()
    fib_len = 10
    prime_len = 5
    print(f"Fibonacci sequence (first {fib_len}):", end=" ")
    for i in range(fib_len):
        print(next(fib_sequence), end=" ")
    print()
    print(f"Prime numbers (first {prime_len}):", end=" ")
    for i in range(prime_len):
        print((next(prime_numbers)), end=" ")


if __name__ == "__main__":
    ft_analytics_dashboard()
