import pytest
from mortgagepy import (
    CapitalRepaymentMortgage,
    InterestOnlyMortgage
)


@pytest.fixture
def capital_mortgage():
    return CapitalRepaymentMortgage(280000, 210000, 300, 1.8)

@pytest.fixture
def interest_mortgage():
    return InterestOnlyMortgage(280000, 210000, 300, 1.8)

def test_ltv_capital(capital_mortgage) -> None:
    assert capital_mortgage.ltv() == 75

def test_monthly_repayment_capital(capital_mortgage):
    assert capital_mortgage.monthly_repayment() == 869.79

def test_monthly_repayment_interest(interest_mortgage):
    assert interest_mortgage.monthly_repayment() == 315.0

def test_ltv_interest(interest_mortgage) -> None:
    assert interest_mortgage.ltv() == 75