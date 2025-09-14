import pytest
from creatio.occupation.fi_FI import occupation


def test_occupation_returns_valid_string():
    """Test that occupation() returns a valid occupation string."""
    job = occupation.occupation()
    assert isinstance(job, str), "Occupation should be a string"
    assert job.strip(), "Occupation should not be empty or whitespace"
    assert job in occupation.OCCUPATIONS, f"'{job}' is not in the OCCUPATIONS list"
