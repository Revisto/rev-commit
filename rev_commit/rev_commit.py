#!/usr/bin/env python

import readline  # noqa
from rich.console import Console
from rev_commit.commit_generator import generate_commit_message

console = Console()

def main():
    try:
        console.print("[bold green]Enter the changes description (end with two consecutive empty lines):[/bold green]")
        lines = []
        empty_line_count = 0
        while True:
            line = input()
            if line == "":
                empty_line_count += 1
                if empty_line_count == 2:
                    break
            else:
                empty_line_count = 0
                lines.append(line)
        console.print(f"[bold green]Generating commit message...[/bold green]")
        changes_description = "\n".join(lines)
        
        commit_message = generate_commit_message(changes_description)
        console.print(
            f"[bold green]Generated Commit Message:[/bold green] "
            f"{commit_message}"
        )
    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] {str(e)}")

if __name__ == "__main__":
    main()