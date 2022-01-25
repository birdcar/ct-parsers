"""Cointracker validation module."""

import datetime as dt
from collections import namedtuple
from pathlib import Path
from typing import List, Tuple

from .utilities.fs import read_csv_file

VALID_HEADER = (
    "Date",
    "Received Quantity",
    "Received Currency",
    "Sent Quantity",
    "Sent Currency",
    "Fee Amount",
    "Fee Currency",
    "Tag",
)

VALID_DATE = "%m/%d/%Y %H:%M:%S"
VALID_SYMBOLS = {
    "USD",
    "EUR" "GBP",
    "BTC",
    "ETH2",
    "ETH",
    "USDT",
    "BNB",
    "USDC",
    "ADA",
    "HEX",
    "SOL",
    "XRP",
}

ValidationResult = namedtuple('ValidationResult', ('success', 'errors'))


def validate_header(row: dict) -> bool:
    """Verify header exactly matches our valid header."""
    return tuple(row.keys()) != VALID_HEADER


def validate_dates(row: dict):
    """Raise ValueError if the date is invalid."""
    try:
        dt.datetime.strptime(row['Date'], VALID_DATE)
    except ValueError:
        raise ValueError("Required date format is MM/DD/YYYY HH:MM:SS")


def validate_symbols(row: dict):
    """Raise ValueError if any of the symbol columns are invalid."""
    if row["Received Currency"] and row["Received Currency"] not in VALID_SYMBOLS:
        raise ValueError(f"'Recieved Currency' must be a one of {VALID_SYMBOLS}")
    if row["Sent Currency"] and row["Sent Currency"] not in VALID_SYMBOLS:
        raise ValueError(f"'Sent Currency' must be a one of {VALID_SYMBOLS}")
    if row["Fee Currency"] and row["Fee Currency"] not in VALID_SYMBOLS:
        raise ValueError(f"'Fee Currency' must be a one of {VALID_SYMBOLS}")


def validate_decimal_places(row: dict):
    """Raise ValueError if any number has more than 8 decimal places."""
    if any(
        [
            len(row["Received Quantity"].split(".")[-1]) > 8,
            len(row["Sent Quantity"].split('.')[-1]) > 8,
            len(row["Fee Amount"].split('.')[-1]) > 8,
        ]
    ):
        raise ValueError("Decimal numbers must be 8 decimal places or less")


def validate(file_path: Path, fail_fast: bool = False) -> ValidationResult:
    """Validate a csv file is in the CoinTracker CSV format."""
    errors: List[Tuple[int, str]] = list()

    for row_idx, row in enumerate(read_csv_file(file_path)):
        row_idx += 2  # increment the index to match the actual row in the file

        try:
            if row_idx == 2 and validate_header(row):
                fail_fast = True
                raise ValueError(f"{file_path.name} header must exactly match {VALID_HEADER}.")

            validate_dates(row)
            validate_symbols(row)
            validate_decimal_places(row)

        except Exception as err:
            if fail_fast:
                raise
            else:
                errors.append((row_idx, str(err)))
    if errors:
        return ValidationResult(False, errors)
    else:
        return ValidationResult(True, errors)
