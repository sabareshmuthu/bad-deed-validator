import pytest
import sys
import os

# Add project root to Python path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from validators import validate_dates, validate_amounts


def test_invalid_dates():
    with pytest.raises(ValueError):
        validate_dates("2024-01-15", "2024-01-10")


def test_amount_mismatch():
    with pytest.raises(ValueError):
        validate_amounts("$1,250,000.00", "One Million Two Hundred Thousand Dollars")