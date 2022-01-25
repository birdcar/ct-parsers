#!/usr/bin/env python
"""Tests for `ct_parsers` package."""

from ct_parsers.cointracker import validate


def test_valid_file_parses_successfully(cointracker_kg_csv):
    """When a file is successfully parsed, return a successful ValidationResult"""
    assert validate(cointracker_kg_csv) == (True, [])
