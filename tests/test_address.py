import re
import pytest
from creatio import address

def test_kotiosoite_returns_string():
    """Test that kotiosoite() returns a string containing a comma."""
    addr = address.kotiosoite()
    assert isinstance(addr, str)
    assert "," in addr