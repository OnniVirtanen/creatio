import pytest
from creatio.name.fi_FI import name


def test_firstname_returns_valid_string():
    """Test that firstname() returns a non-empty string from either gender list."""
    first = name.firstname()
    assert isinstance(first, str)
    assert first.strip()
    assert first in name.FIRSTNAMES_MALE + name.FIRSTNAMES_WOMEN


@pytest.mark.parametrize("is_male", [True, False])
def test_firstname_gender_returns_gendered_name(is_male):
    """Test firstname_gender() returns correct gendered name."""
    first = name.firstname_gender(is_male)
    assert isinstance(first, str)
    assert first.strip()
    if is_male:
        assert first in name.FIRSTNAMES_MALE
    else:
        assert first in name.FIRSTNAMES_WOMEN


def test_lastname_returns_valid_string():
    """Test lastname() returns a valid Finnish surname."""
    last = name.lastname()
    assert isinstance(last, str)
    assert last.strip()
    assert last in name.LASTNAMES


def test_full_name_format():
    """Test that full_name() returns a first and last name separated by a space."""
    full = name.full_name()
    assert isinstance(full, str)
    assert full.strip()
    parts = full.split()
    assert len(parts) == 2, f"Expected two parts in full name, got: {full}"
    first, last = parts
    assert first in name.FIRSTNAMES_MALE + name.FIRSTNAMES_WOMEN
    assert last in name.LASTNAMES
