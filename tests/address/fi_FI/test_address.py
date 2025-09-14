import pytest
from creatio.address.fi_FI import address


def test_home_address_is_valid_string():
    """Test that home_address returns a non-empty, valid string."""
    addr = address.home_address()

    # Check it's a string
    assert isinstance(addr, str), "home_address() should return a string"

    # Check it's not empty or just whitespace
    assert (
        addr.strip()
    ), "home_address() should not return an empty or whitespace-only string"

    # Optional: Check it contains a street name and number (very basic heuristic)
    assert any(
        char.isdigit() for char in addr
    ), "Address should contain a number (e.g. street number)"
    assert any(
        char.isalpha() for char in addr
    ), "Address should contain letters (e.g. street name)"
