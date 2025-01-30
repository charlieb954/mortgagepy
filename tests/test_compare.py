"""pytest tests for the mortgagepy.compare module."""

import pytest

from mortgagepy.compare import (
    compare_capital_repayment_rates,
    compare_interest_only_rates,
)
from mortgagepy.exceptions import IncorrectType


@pytest.fixture
def mortgage() -> int:
    """fixture for mortgage amount."""
    return 130_500


def test_compare_capital_repayments_repayment_interest_rates(
    mortgage: int,
) -> None:
    """check if the capital repayment rates are compared correctly"""
    with pytest.raises(IncorrectType):
        compare_capital_repayment_rates(
            mortgage=mortgage, interest_rates=1, mortgage_length_months=300
        )

    assert compare_capital_repayment_rates(
        mortgage=mortgage, interest_rates=[1, 2], mortgage_length_months=300
    ) == [
        {"interest_rate": 1, "repayment": 491.82},
        {"interest_rate": 2, "repayment": 553.13},
    ]


def test_compare_interest_only_rates(mortgage: int) -> None:
    """check if the interest only rates are compared correctly"""
    with pytest.raises(IncorrectType):
        compare_interest_only_rates(mortgage=mortgage, interest_rates=1)

    assert compare_interest_only_rates(
        mortgage=mortgage, interest_rates=[1, 2]
    ) == [
        {"interest_rate": 1, "repayment": 108.75},
        {"interest_rate": 2, "repayment": 217.50},
    ]
