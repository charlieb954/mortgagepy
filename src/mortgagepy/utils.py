"""Utility functions for the mortgagepy package."""

from datetime import datetime

from dateutil import relativedelta


def mortgage_term_remaining(
    start_date: datetime, end_date: datetime
) -> relativedelta:
    """Given two dates, work out the difference in years, months and days.

    Args:
        start_date (datetime): start date for the calculation.
        end_date (datetime): end date for the calculation.

    Returns:
        (relativedelta): absolute difference in years, months and days.
    """
    return abs(relativedelta.relativedelta(start_date, end_date))
