from pathlib import Path

import pytest


@pytest.fixture()
def cointracker_kg_csv() -> Path:
    return Path(__file__).resolve(strict=True).parent / "fixtures" / "cointracker" / "kg.csv"


@pytest.fixture()
def cointracker_kb_header_csv() -> Path:
    return Path(__file__).resolve(strict=True).parent / "fixtures" / "cointracker" / "kb_header.csv"


@pytest.fixture()
def cointracker_kb_dates_csv() -> Path:
    return Path(__file__).resolve(strict=True).parent / "fixtures" / "cointracker" / "kb_dates.csv"


@pytest.fixture()
def cointracker_kb_symbols_csv() -> Path:
    return Path(__file__).resolve(strict=True).parent / "fixtures" / "cointracker" / "kb_symbols.csv"


@pytest.fixture()
def cointracker_kb_decimals_csv() -> Path:
    return Path(__file__).resolve(strict=True).parent / "fixtures" / "cointracker" / "kb_decimals.csv"
