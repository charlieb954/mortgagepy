import mortgagepy


def test_monthly_interest():
    november_debit_interest = -158.70
    october_debit_interest = -154.22
    october_balance = -98_868.70
    september_balance = -99_276.93

    assert (
        mortgagepy.monthly_interest(september_balance, 1.89, 9, 2023)
        == october_debit_interest
    )
    assert (
        mortgagepy.monthly_interest(october_balance, 1.89, 10, 2023)
        == november_debit_interest
    )


def test_ltv_calculator():
    assert mortgagepy.ltv_calculator(200_000, 50_000) == 75


def test_interest_only_calculator():
    assert mortgagepy.interest_only_calculator(130_500, 3.89) == 423.04


def test_repayment_calculator():
    assert mortgagepy.repayment_calculator(130_500, 3.89, 300) == 680.93
    assert mortgagepy.repayment_calculator(130_500, 6.89, 300) == 913.21

def test_total_cost_of_mortgage():
    assert mortgagepy.total_cost_of_mortgage(130_500, 6.89, 300) == 273_963.0