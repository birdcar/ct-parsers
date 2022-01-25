#!/usr/bin/env python
"""Tests for `ct_parsers` package."""

import pytest

from ct_parsers.cointracker import VALID_SYMBOLS, validate


def test_valid_file_parses_successfully(cointracker_kg_csv):
    """When a file is successfully parsed, return a successful ValidationResult"""
    assert validate(cointracker_kg_csv) == (True, [])


def test_invalid_header_fails_fast(cointracker_kb_header_csv):
    """When a header is bad, fail immediately with a value error."""
    with pytest.raises(ValueError):
        validate(cointracker_kb_header_csv)


def test_invalid_symbols(cointracker_kb_symbols_csv):
    """When symbols are wrong, compile each error and return it as a ValidationResult"""
    expected_errors = [
        (2, f"'Recieved Currency' must be a one of {VALID_SYMBOLS}"),
        (3, f"'Sent Currency' must be a one of {VALID_SYMBOLS}"),
        (5, f"'Fee Currency' must be a one of {VALID_SYMBOLS}"),
    ]
    successful, errors = validate(cointracker_kb_symbols_csv)
    assert not successful
    assert errors == expected_errors


def test_invalid_date_format(cointracker_kb_dates_csv):
    """When dates are improperly formatted, compile each error and return it as a ValidationResult."""
    expected_errors = [
        (2, "Required date format is MM/DD/YYYY HH:MM:SS"),
        (5, "Required date format is MM/DD/YYYY HH:MM:SS"),
    ]
    successful, errors = validate(cointracker_kb_dates_csv)
    assert not successful
    assert errors == expected_errors


def test_invalid_decimal_count(cointracker_kb_decimals_csv):
    """When decimals have more than 8 places, compile each error and return it as a ValidationResult"""
    expected_errors = [
        (2, "Decimal numbers must be 8 decimal places or less"),
    ]
    successful, errors = validate(cointracker_kb_decimals_csv)
    assert not successful
    assert errors == expected_errors


def test_invalid_deposit_transaction():
    pass


def test_invalid_withdrawl_transaction():
    pass


def test_invalid_trade_transaction():
    pass


def test_invalid_tag():
    pass
