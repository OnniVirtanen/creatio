from creatio import name


def test_first_name_is_valid():
    """Test that first_name() returns a valid first name."""
    result = name.first_name()
    assert isinstance(result, str)
    assert result in name.FIRST_NAMES


def test_last_name_is_valid():
    """Test that last_name() returns a valid last name."""
    result = name.last_name()
    assert isinstance(result, str)
    assert result in name.LAST_NAMES


def test_full_name_format():
    """Test that full_name() returns a valid full name."""
    full = name.full_name()
    parts = full.split()
    
    assert isinstance(full, str)
    assert len(parts) == 2

    first, last = parts
    assert first in name.FIRST_NAMES
    assert last in name.LAST_NAMES
