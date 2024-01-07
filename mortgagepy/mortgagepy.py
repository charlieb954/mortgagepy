from calendar import monthrange, isleap
import json
import click


def repayment_calculator(
    mortgage: float, interest_rate: float, mortgage_length_months: int
) -> dict:
    """repayment mortgage calculator.

    repayment = P*((r(1+r)^n)/((1+r)^n-1))

    r = Annual interest rate (APRC)/12 (months)
    P = Principal (starting balance) of the loan
    n = Number of payments in total: if you make
        one mortgage payment every month for 25
        years, that’s 25*12 = 300
    """
    r = (interest_rate / 100) / 12
    rate = (1 + r) ** mortgage_length_months
    repayment = round(mortgage * (r * rate / (rate - 1)), 2)

    return {"monthly_repayment": repayment}


def interest_only_calculator(mortgage: float, interest_rate: float) -> dict:
    """interest only mortgage calculator."""
    interest_rate_dec = interest_rate / 100
    repayment = round((mortgage * interest_rate_dec) / 12, 2)

    return {"monthly_repayment": repayment}


def ltv_calculator(property_price: float, deposit: float) -> dict:
    """loan to value calculator."""
    deposit_dec = 25_000 / 100_000
    loan_dec = 1 - deposit_dec

    return {"ltv_pct": int(loan_dec * 100)}


def monthly_interest(
    balance_at_previous_month: float, interest_rate: float, month: int, year: int
) -> float:
    """monthly mortgage interest calculator.

    Args:
        balance_at_previous_month (float): outstanding mortgage at previous month
        interest_rate (float): interest rate as a percentage
        month (int): month of the year to calculate interest, required for daily interest calculation
        year (int): year to calculate interest, required to account for leap years

    Returns:
        (float): monthly interest
    """
    interest_rate_dec = interest_rate / 100

    _, days_in_month = monthrange(2023, month)

    if isleap(year):
        days = 366
    else:
        days = 365

    return round(
        ((balance_at_previous_month * interest_rate_dec) / days) * days_in_month, 2
    )
