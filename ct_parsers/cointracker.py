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


