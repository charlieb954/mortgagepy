import pytest

from mortgagepy import CapitalRepaymentMortgage, InterestOnlyMortgage
from mortgagepy.exceptions import IncorrectType


@pytest.fixture
def capital_mortgage() -> CapitalRepaymentMortgage:
    return CapitalRepaymentMortgage(
        property_value=280000, mortgage=210000, term_months=300, interest_rate=1.8
    )


@pytest.fixture
def interest_mortgage() -> InterestOnlyMortgage:
    return InterestOnlyMortgage(
        property_value=280000, mortgage=210000, term_months=300, interest_rate=1.8
    )


def test_ltv_capital(capital_mortgage: CapitalRepaymentMortgage) -> None:
    assert capital_mortgage.ltv() == 75


def test_monthly_repayment_capital(capital_mortgage: CapitalRepaymentMortgage) -> None:
    assert capital_mortgage.monthly_repayment() == 869.79


def test_monthly_repayment_interest(interest_mortgage: InterestOnlyMortgage) -> None:
    assert interest_mortgage.monthly_repayment() == 315.0


def test_ltv_interest(interest_mortgage: InterestOnlyMortgage) -> None:
    assert interest_mortgage.ltv() == 75


def test_mortgage_raise() -> None:
    with pytest.raises(IncorrectType):
        CapitalRepaymentMortgage(
            property_value="test",
            mortgage="test",
            term_months="test",
            interest_rate="test",
        )
