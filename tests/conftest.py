"""CT Parsers test fixtures."""
from pathlib import Path

import pytest


@pytest.fixture()
def cointracker_kg_csv() -> Path:
    """Return the path to a Known Good Generic CSV."""
    return Path(__file__).resolve(strict=True).parent / "fixtures" / "cointracker" / "kg.csv"


@pytest.fixture()
def cointracker_kb_header_csv() -> Path:
    """Return the path to a CSV with a badly formated header."""
    return Path(__file__).resolve(strict=True).parent / "fixtures" / "cointracker" / "kb_header.csv"


@pytest.fixture()
def cointracker_kb_dates_csv() -> Path:
    """Return the path to a CSV with some badly formatted dates."""
    return Path(__file__).resolve(strict=True).parent / "fixtures" / "cointracker" / "kb_dates.csv"


@pytest.fixture()
def cointracker_kb_symbols_csv() -> Path:
    """Return the path to a CSV with some invalid symbols."""
    return Path(__file__).resolve(strict=True).parent / "fixtures" / "cointracker" / "kb_symbols.csv"


@pytest.fixture()
def cointracker_kb_decimals_csv() -> Path:
    """Return the path to a CSV with some improperly truncated decimal values."""
    return Path(__file__).resolve(strict=True).parent / "fixtures" / "cointracker" / "kb_decimals.csv"
