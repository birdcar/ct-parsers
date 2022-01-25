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

