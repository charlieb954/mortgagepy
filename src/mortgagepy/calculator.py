"""Mortgage calculations module for mortgagepy package."""

from calendar import isleap, monthrange
from datetime import datetime
from typing import Optional


def monthly_capital_repayment(
    mortgage: float,
    interest_rate: float,
    mortgage_length_months: int,
) -> float:
    """A calculator to work out monthly mortgage repayments for a capital
    repayment mortgage. At least one of mortgage_length_months or
    mortgage_length_years must be passed.

    repayment = P*((r(1+r)^n)/((1+r)^n-1))

    r = Annual interest rate (APRC)/12 (months)
    P = Principal (starting balance) of the loan
    n = Number of payments in total: if you make
        one mortgage payment every month for 25
        years, that’s 25*12 = 300

    Args:
        mortgage (float): outstanding mortgage value.
        interest_rate (float): current interest rate as a decimal.
        mortgage_length_months (int): number of months remaining of
            the mortgage.

    Returns:
        monthly_mortgage_repayment (float): monthly mortgage repayment.
    """

    r = (interest_rate / 100) / 12
    rate = (1 + r) ** mortgage_length_months
    monthly_mortgage_repayment = round(mortgage * (r * rate / (rate - 1)), 2)

    return monthly_mortgage_repayment


def total_cost_of_mortgage(
    mortgage: float,
    interest_rate: float,
    mortgage_length_months: int,
) -> float:
    """Works out the total cost of the mortgage assuming that the interest rate
    stays the same. At least one of mortgage_length_months or
    mortgage_length_years must be passed.

    Args:
        mortgage (float): outstanding mortgage value.
        interest_rate (float): current interest rate as a decimal.
        mortgage_length_months (int): number of months remaining of
            the mortgage.

    Returns:
        total_cost (float): total cost of the mortgage.
    """

    monthly_repayment = monthly_capital_repayment(
        mortgage, interest_rate, mortgage_length_months
    )

    total_cost = monthly_repayment * mortgage_length_months

    return total_cost


def monthly_interest_only_repayment(
    mortgage: float, interest_rate: float
) -> float:
    """A calculator to work out monthly mortgage repayments of an interest only
    mortgage.

    Args:
        mortgage (float): outstanding mortgage value.
        interest_rate (float): current interest rate as a decimal.

    Returns:
        monthly_interest_only_repayment (float): monthly cost of the mortgage.
    """
    interest_rate_dec = interest_rate / 100
    monthly_interest_only_repayment = round(
        (mortgage * interest_rate_dec) / 12, 2
    )

    return monthly_interest_only_repayment


def ltv(property_value: float, deposit: float) -> int:
    """Loan to value percentage calculator.

    Args:
        property_value (float): current property price.
        deposit (float): current equity or deposit.

    Returns:
        (int): loan to value as a percentage.
    """
    deposit_dec = deposit / property_value
    loan_dec = 1 - deposit_dec

    return int(loan_dec * 100)


def monthly_interest(
    balance_at_previous_month: float,
    interest_rate: float,
    month: Optional[int] = 1,
    year: Optional[int] = 2023,
) -> float:
    """Monthly mortgage interest calculator to work out the exact interest in a
    single month, given the balance at the previous month and interest rate.

    Args:
        balance_at_previous_month (float): outstanding mortgage at previous
            month.
        interest_rate (float): interest rate as a percentage.
        month (int, optional): month of the year to calculate interest,
            required for daily interest calculation. Default is 1 which assumes
            31 days in the month.
        year (int, optional): year to calculate interest, required to account
            for leap years. Default is 2023 which assumes a non-leap year.

    Returns:
        monthly_interest (float): absolute value of monthly interest.
    """
    interest_rate_dec = interest_rate / 100

    _, days_in_month = monthrange(2023, month)

    if isleap(year):
        days = 366
    else:
        days = 365

    monthly_interest = round(
        ((balance_at_previous_month * interest_rate_dec) / days)
        * days_in_month,
        2,
    )

    return monthly_interest


def capital_overpayment(
    mortgage: float,
    interest_rate: float,
    mortgage_length_months: int,
    monthly_overpayment: float = 0,
    lump_sum_payment: float = 0,
    lump_sum_payment_month: int = 1,
) -> dict:
    """Calculate the impact of regular monthly overpayments and a lump sum
    payment on a mortgage.

    Args:
        mortgage (float): outstanding mortgage value.
        interest_rate (float): current interest rate as a decimal.
        mortgage_length_months (int): original number of months of the
            mortgage.
        monthly_overpayment (float): additional monthly overpayment amount.
        lump_sum_payment (float): one-time lump sum payment amount.
        lump_sum_payment_month (int): the month in which the lump sum payment
            is made (default is 1).

    Returns:
        dict: A dictionary containing the impact details.
    """
    standard_payment = monthly_capital_repayment(
        mortgage, interest_rate, mortgage_length_months
    )

    remaining_balance = mortgage
    months_to_repay = 0
    total_interest_paid = 0

    year = datetime.now().year
    month = datetime.now().month

    while remaining_balance > 0:
        months_to_repay += 1

        # Apply lump sum payment if it's the correct month
        if months_to_repay == lump_sum_payment_month:
            remaining_balance -= lump_sum_payment
            if remaining_balance < 0:
                remaining_balance = 0
                break

        interest = monthly_interest(
            balance_at_previous_month=remaining_balance,
            interest_rate=interest_rate,
            month=1,  # for ease assumes every month is 31 days
        )
        total_interest_paid += interest

        total_payment = standard_payment + monthly_overpayment

        if remaining_balance < total_payment:
            total_payment = remaining_balance + interest

        remaining_balance = remaining_balance + interest - total_payment

        if months_to_repay >= mortgage_length_months:
            break

        month += 1

        if month == 12:
            month = 1
            year += 1

    time_saved = mortgage_length_months - months_to_repay

    return {
        "months_to_repay": months_to_repay,
        "time_saved_months": time_saved,
        "total_interest_paid": round(total_interest_paid, 2),
        "final_balance": round(remaining_balance, 2),
    }
