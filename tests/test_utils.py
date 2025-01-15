"""pytest test cases for mortgagepy.utils module."""

from datetime import datetime

from mortgagepy.utils import mortgage_term_remaining


def test_mortgage_term_remaining():
    """check if mortgage_term_remaining returns the correct number of years."""
    assert (
        mortgage_term_remaining(
            datetime(2023, 1, 1), datetime(2024, 1, 1)
        ).years
        == 1
    )
