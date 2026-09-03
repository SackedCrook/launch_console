"""A small starter console for experimenting with launch commands."""

from __future__ import annotations


PROMPT = "launch> "


def show_help() -> None:
    """Print the commands supported by the starter console."""
    print("Commands: help, hello, quit")


def run() -> None:
    """Run the interactive console until the user exits."""
    print("Launch Console")
    print("Type 'help' for available commands.")

    while True:
        try:
            command = input(PROMPT).strip().lower()
        except EOFError:
            print()
            break

        if command in {"quit", "exit"}:
            print("Goodbye!")
            break
        if command == "help":
            show_help()
        elif command == "hello":
            print("Hello from Launch Console!")
        elif command:
            print(f"Unknown command: {command}")


if __name__ == "__main__":
    run()