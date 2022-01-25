"""File system helpers for ct_parsers."""
import csv
from pathlib import Path
from typing import Generator


def read_csv_file(file_path: Path) -> Generator:
    """Read a csv file and return a generator that yields each row."""
    with open(file_path) as f:
        yield from csv.DictReader(f)
