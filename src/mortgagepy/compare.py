from .calculator import monthly_capital_repayment, monthly_interest_only_repayment
from .exceptions import IncorrectType


def compare_interest_only_rates(
    mortgage: float,
    interest_rates: list,
) -> dict:
    """Compare multiple interest rates with the same mortgage to see how
    the interest rate changes the repayments for an interest only mortgage.

    Args:
        mortgage (float): outstanding mortgage value.
        interest_rates (list): interest rates to compare.

    Returns:
        (dict): all the interest rate and monthly repayment values.
    """
    if not isinstance(interest_rates, list):
        raise IncorrectType("Please ensure you pass a list of interest rates.")

    repayments = dict()

    for interest_rate in interest_rates:
        repayments[interest_rate] = monthly_interest_only_repayment(
            mortgage=mortgage, interest_rate=interest_rate
        )

    return repayments


def compare_capital_repayment_rates(
    mortgage: float,
    interest_rates: list,
    mortgage_length_months: int,
) -> dict:
    """Compare multiple interest rates with the same mortgage to see how
    the interest rate changes the repayments for a capital repayment mortgagae.

    Args:
        mortgage (float): outstanding mortgage value.
        interest_rates (list): interest rates to compare.
        mortgage_length_months (int): number of months remaining of
            the mortgage.

    Returns:
        (dict): all the interest rate and monthly repayment values.
    """
    if not isinstance(interest_rates, list):
        raise IncorrectType("Please ensure you pass a list of interest rates.")

    repayments = dict()

    for interest_rate in interest_rates:
        repayments[interest_rate] = monthly_capital_repayment(
            mortgage=mortgage,
            interest_rate=interest_rate,
            mortgage_length_months=mortgage_length_months,
        )

    return repayments
