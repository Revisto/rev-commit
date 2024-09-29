#!/usr/bin/env python

from rich.prompt import Prompt
from rich.console import Console
from rev_commit.commit_generator import generate_commit_message

console = Console()


def main():
    try:
        changes_description = Prompt.ask("Enter the description of changes")
        commit_message = generate_commit_message(changes_description)
        console.print(
            f"[bold green]Generated Commit Message:[/bold green] "
            f"{commit_message}"
        )
    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] {str(e)}")


if __name__ == "__main__":
    main()
