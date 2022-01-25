"""CLI module."""
import sys
from pathlib import Path

import typer

from .cointracker import validate as ct_validate
from .utilities.display import build_error_table, console

app = typer.Typer()


@app.command()
def validate(file_path: Path, fail_fast: bool = False):
    """Validate a CSV file to verify that it complies with CoinTrackers Generic CSV format."""
    try:
        validation = ct_validate(file_path, fail_fast)

        if not validation.success:
            tbl = build_error_table(title=f"[bold red]Validation failed for {file_path.name}", errors=validation.errors)
            console.print(tbl)
            sys.exit(1)
        else:
            console.print(f"[bold green]{file_path.name} is a valid CoinTracker CSV!")

    except ValueError as e:
        console.print(f"[bold red] {e}")
