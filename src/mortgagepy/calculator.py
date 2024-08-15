from calendar import isleap, monthrange
from datetime import datetime
from typing import Optional

from dateutil import relativedelta

from .exceptions import IncorrectType


def repayment_calculator(
    mortgage: float,
    interest_rate: float,
    mortgage_length_months: Optional[int] = None,
    mortgage_length_years: Optional[int] = None,
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
        mortgage_length_months (int, optional): number of months remaining of
            the mortgage. Defaults to None.
        mortgage_length_years (int, optional): number of years remaining of
            the mortgage. Defaults to None.

    Returns:
        monthly_mortgage_repayment (float): monthly mortgage repayment.
    """
    if mortgage_length_months is None and mortgage_length_years is not None:
        mortgage_length_months = mortgage_length_years * 12

    r = (interest_rate / 100) / 12
    rate = (1 + r) ** mortgage_length_months
    monthly_mortgage_repayment = round(mortgage * (r * rate / (rate - 1)), 2)

    return monthly_mortgage_repayment


def total_cost_of_mortgage(
    mortgage: float,
    interest_rate: float,
    mortgage_length_months: Optional[int] = None,
    mortgage_length_years: Optional[int] = None,
) -> float:
    """Works out the total cost of the mortgage assuming that the interest rate
    stays the same. At least one of mortgage_length_months or
    mortgage_length_years must be passed.

    Args:
        mortgage (float): outstanding mortgage value.
        interest_rate (float): current interest rate as a decimal.
        mortgage_length_months (int, optional): number of months remaining of
            the mortgage. Defaults to None.
        mortgage_length_years (int, optional): number of years remaining of
            the mortgage. Defaults to None.

    Returns:
        total_cost (float): total cost of the mortgage.
    """
    if mortgage_length_months is None:
        mortgage_length_months = mortgage_length_years * 12

    monthly_repayment = repayment_calculator(
        mortgage, interest_rate, mortgage_length_months
    )

    total_cost = monthly_repayment * mortgage_length_months

    return total_cost


def interest_only_calculator(mortgage: float, interest_rate: float) -> float:
    """A calculator to work out monthly mortgage repayments of an interest only
    mortgage.

    Args:
        mortgage (float): outstanding mortgage value.
        interest_rate (float): current interest rate as a decimal.

    Returns:
        monthly_interest_only_repayment (float): monthly cost of the mortgage.
    """
    interest_rate_dec = interest_rate / 100
    monthly_interest_only_repayment = round((mortgage * interest_rate_dec) / 12, 2)

    return monthly_interest_only_repayment


def mortgage_term_remaining(start_date: datetime, end_date: datetime) -> relativedelta:
    """Given two dates, work out the difference in years, months and days.

    Args:
        start_date (datetime): start date for the calculation.
        end_date (datetime): end date for the calculation.

    Returns:
        (relativedelta): absolute difference in years, months and days.
    """
    return abs(relativedelta.relativedelta(start_date, end_date))


def ltv_calculator(property_value: float, deposit: float) -> int:
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
    balance_at_previous_month: float, interest_rate: float, month: int, year: int
) -> float:
    """Monthly mortgage interest calculator to work out the exact interest in a
    single month, given the balance at the previous month and interest rate.

    Args:
        balance_at_previous_month (float): outstanding mortgage at previous month.
        interest_rate (float): interest rate as a percentage.
        month (int): month of the year to calculate interest, required for daily
            interest calculation.
        year (int): year to calculate interest, required to account for leap years.

    Returns:
        monthly_interest (float): monthly interest.
    """
    interest_rate_dec = interest_rate / 100

    _, days_in_month = monthrange(2023, month)

    if isleap(year):
        days = 366
    else:
        days = 365

    monthly_interest = round(
        ((balance_at_previous_month * interest_rate_dec) / days) * days_in_month, 2
    )

    return monthly_interest


def compare_interest_only_interest_rates():
    pass


def compare_repayment_interest_rates(
    mortgage: float,
    interest_rates: list,
    mortgage_length_months: Optional[int] = None,
    mortgage_length_years: Optional[int] = None,
) -> dict:
    """Compare multiple interest rates with the same mortgage to see how
    the interest rate changes the repayments.

    Args:
        mortgage (float): outstanding mortgage value.
        interest_rates (list): interest rates to compare.
        mortgage_length_months (int, optional): number of months remaining of
            the mortgage. Defaults to None.
        mortgage_length_years (int, optional): number of years remaining of
            the mortgage. Defaults to None.

    Returns:
        (dict): all the interest rate and monthly repayment values.
    """
    if not isinstance(interest_rates, list):
        raise IncorrectType("Please ensure you pass a list of interest rates.")

    repayments = dict()

    for interest_rate in interest_rates:
        repayments[interest_rate] = repayment_calculator(
            mortgage=mortgage,
            interest_rate=interest_rate,
            mortgage_length_months=mortgage_length_months,
            mortgage_length_years=mortgage_length_years,
        )

    return repayments
