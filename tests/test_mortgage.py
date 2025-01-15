"""pytest tests for mortgagepy.mortgage module."""

import pytest

from mortgagepy import CapitalRepaymentMortgage, InterestOnlyMortgage
from mortgagepy.exceptions import IncorrectType


@pytest.fixture
def capital_mortgage() -> CapitalRepaymentMortgage:
    """CapitalRepaymentMortgage fixture."""
    return CapitalRepaymentMortgage(
        property_value=280000,
        mortgage=210000,
        term_months=300,
        interest_rate=1.8,
    )


@pytest.fixture
def interest_mortgage() -> InterestOnlyMortgage:
    """InterestOnlyMortgage fixture."""
    return InterestOnlyMortgage(
        property_value=280000,
        mortgage=210000,
        term_months=300,
        interest_rate=1.8,
    )


def test_ltv_capital(capital_mortgage: CapitalRepaymentMortgage) -> None:
    """check loan to value of capital repayment mortgage."""
    assert capital_mortgage.ltv() == 75


def test_monthly_repayment_capital(
    capital_mortgage: CapitalRepaymentMortgage,
) -> None:
    """check monthly repayment of capital repayment mortgage."""
    assert capital_mortgage.monthly_repayment() == 869.79


def test_monthly_repayment_interest(
    interest_mortgage: InterestOnlyMortgage,
) -> None:
    """check monthly repayment of interest only mortgage."""
    assert interest_mortgage.monthly_repayment() == 315.0


def test_ltv_interest(interest_mortgage: InterestOnlyMortgage) -> None:
    """check loan to value of interest only mortgage."""
    assert interest_mortgage.ltv() == 75


def test_mortgage_raise() -> None:
    """check if the mortgage raises an exception when passed an incorrect
    value."""
    with pytest.raises(IncorrectType):
        CapitalRepaymentMortgage(
            property_value="test",
            mortgage="test",
            term_months="test",
            interest_rate="test",
        )
