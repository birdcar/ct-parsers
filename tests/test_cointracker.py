#!/usr/bin/env python
"""Tests for `ct_parsers` package."""

import pytest

from ct_parsers.cointracker import VALID_SYMBOLS, VALID_TAGS, validate


def test_valid_file_parses_successfully(cointracker_kg_csv):
    """Return a successful ValidationResult when parsing a known good file."""
    assert validate(cointracker_kg_csv) == (True, [])


def test_invalid_header_fails_fast(cointracker_kb_header_csv):
    """Fail immediately with a ValueError when the header is malformed."""
    with pytest.raises(ValueError):
        validate(cointracker_kb_header_csv)


def test_invalid_symbols(cointracker_kb_symbols_csv):
    """Compile each error and return it as a ValidationResult when symbols are invalid."""
    expected_errors = [
        (2, f"'Recieved Currency' must be a one of {VALID_SYMBOLS}"),
        (3, f"'Sent Currency' must be a one of {VALID_SYMBOLS}"),
        (5, f"'Fee Currency' must be a one of {VALID_SYMBOLS}"),
    ]
    successful, errors = validate(cointracker_kb_symbols_csv)
    assert not successful
    assert errors == expected_errors


def test_invalid_date_format(cointracker_kb_dates_csv):
    """Compile each error and return it as a ValidationResult when dates are improperly formatted."""
    expected_errors = [
        (2, "Required date format is MM/DD/YYYY HH:MM:SS"),
        (5, "Required date format is MM/DD/YYYY HH:MM:SS"),
    ]
    successful, errors = validate(cointracker_kb_dates_csv)
    assert not successful
    assert errors == expected_errors


def test_invalid_decimal_count(cointracker_kb_decimals_csv):
    """Compile each error and return it as a ValidationResult when decimal values have more than 8 places."""
    expected_errors = [
        (2, "Decimal numbers must be 8 decimal places or less"),
    ]
    successful, errors = validate(cointracker_kb_decimals_csv)
    assert not successful
    assert errors == expected_errors
