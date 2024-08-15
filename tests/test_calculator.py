import pytest
from mortgagepy.calculator import (
    IncorrectType,
    compare_repayment_interest_rates,
    interest_only_calculator,
    ltv_calculator,
    monthly_interest,
    repayment_calculator,
    total_cost_of_mortgage,
)


@pytest.fixture
def mortgage() -> int:
    return 130_500


def test_monthly_interest() -> None:
    november_debit_interest = -158.70
    october_debit_interest = -154.22
    october_balance = -98_868.70
    september_balance = -99_276.93

    assert monthly_interest(september_balance, 1.89, 9, 2023) == october_debit_interest
    assert monthly_interest(october_balance, 1.89, 10, 2023) == november_debit_interest


def test_ltv_calculator(mortgage: int) -> None:
    assert ltv_calculator(mortgage, 50_000) == 61


def test_interest_only_calculator(mortgage: int) -> None:
    assert interest_only_calculator(mortgage, 3.89) == 423.04


def test_repayment_calculator(mortgage: int) -> None:
    assert repayment_calculator(mortgage, 3.89, 300) == 680.93
    assert repayment_calculator(mortgage, 6.89, 300) == 913.21


def test_total_cost_of_mortgage(mortgage: int) -> None:
    assert total_cost_of_mortgage(mortgage, 6.89, 300) == 273_963.0


def test_compare_repayment_interest_rates(mortgage: int):
    with pytest.raises(IncorrectType):
        compare_repayment_interest_rates(mortgage, 1, 300)

    assert compare_repayment_interest_rates(mortgage, [1, 2], 300) == {
        1: 491.82,
        2: 553.13,
    }
