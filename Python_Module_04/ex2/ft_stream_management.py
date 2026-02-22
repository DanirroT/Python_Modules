#!/usr/bin/env python3

import sys


def ft_print_stdout(message: str) -> None:
    print("[STANDARD]", message, file=sys.stdout)


def ft_print_stderr(message: str) -> None:
    print("[ALERT]", message, file=sys.stderr)


def ft_read_stdin(prompt: str) -> str:
    print("Input Stream active.", prompt, end="", file=sys.stdout, flush=True)
    return sys.stdin.readline().strip()


def ft_stream_management() -> None:
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===")
    print()
    archivist_id = ft_read_stdin("Enter archivist ID: ")
    status_report = ft_read_stdin("Enter status report: ")
    print()
    ft_print_stdout(f"Archive status from {archivist_id}: {status_report}")
    ft_print_stderr("System diagnostic: Communication channels verified")
    ft_print_stdout("Data transmission complete")
    print()
    print("Three-channel communication test successful.")


if __name__ == "__main__":
    ft_stream_management()
