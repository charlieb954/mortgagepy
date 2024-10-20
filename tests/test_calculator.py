import pytest

from mortgagepy.calculator import (
    compare_capital_repayment_rates,
    compare_interest_only_rates,
    ltv,
    monthly_capital_repayment,
    monthly_interest,
    monthly_interest_only_repayment,
    total_cost_of_mortgage,
)
from mortgagepy.exceptions import IncorrectType


@pytest.fixture
def mortgage() -> int:
    return 130_500


def test_monthly_interest() -> None:
    november_debit_interest = -158.70
    october_debit_interest = -154.22
    october_balance = -98_868.70
    september_balance = -99_276.93

    assert (
        monthly_interest(
            balance_at_previous_month=september_balance,
            interest_rate=1.89,
            month=9,
            year=2023,
        )
        == october_debit_interest
    )
    assert (
        monthly_interest(
            balance_at_previous_month=october_balance,
            interest_rate=1.89,
            month=10,
            year=2023,
        )
        == november_debit_interest
    )


def test_ltv_calculator() -> None:
    assert ltv(property_value=100_000, deposit=50_000) == 50


def test_interest_only_calculator(mortgage: int) -> None:
    assert (
        monthly_interest_only_repayment(mortgage=mortgage, interest_rate=3.89) == 423.04
    )


def test_repayment_calculator(mortgage: int) -> None:
    assert (
        monthly_capital_repayment(
            mortgage=mortgage, interest_rate=3.89, mortgage_length_months=300
        )
        == 680.93
    )
    assert (
        monthly_capital_repayment(
            mortgage=mortgage, interest_rate=6.89, mortgage_length_months=300
        )
        == 913.21
    )


def test_total_cost_of_mortgage(mortgage: int) -> None:
    assert (
        total_cost_of_mortgage(
            mortgage=mortgage, interest_rate=6.89, mortgage_length_months=300
        )
        == 273_963.0
    )


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
