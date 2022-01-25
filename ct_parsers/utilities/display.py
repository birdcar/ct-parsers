"""Display utilities using Rich."""
from typing import List, Tuple

from rich.console import Console
from rich.table import Table

console = Console()


def build_error_table(title: str, errors: List[Tuple[int, str]]) -> Table:
    """Return a rich.table.Table of errors to display to the user."""
    table = Table(title=title)
    table.add_column('Row #')
    table.add_column('Error')

    for row, error in errors:
        table.add_row(str(row), error)

    return table
