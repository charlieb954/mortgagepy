import pytest

from mortgagepy.compare import (
    compare_capital_repayment_rates,
    compare_interest_only_rates,
)
from mortgagepy.exceptions import IncorrectType


@pytest.fixture
def mortgage() -> int:
    return 130_500


def test_compare_capital_repayments_repayment_interest_rates(mortgage: int):
    with pytest.raises(IncorrectType):
        compare_capital_repayment_rates(
            mortgage=mortgage, interest_rates=1, mortgage_length_months=300
        )

    assert compare_capital_repayment_rates(
        mortgage=mortgage, interest_rates=[1, 2], mortgage_length_months=300
    ) == {
        1: 491.82,
        2: 553.13,
    }


def test_compare_interest_only_rates(mortgage: int):
    with pytest.raises(IncorrectType):
        compare_interest_only_rates(mortgage=mortgage, interest_rates=1)

    assert compare_interest_only_rates(mortgage=mortgage, interest_rates=[1, 2]) == {
        1: 108.75,
        2: 217.50,
    }
