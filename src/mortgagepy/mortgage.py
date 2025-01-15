"""Mortgage classes for mortgagepy package."""

from functools import cache

from .calculator import (
    ltv,
    monthly_capital_repayment,
    monthly_interest_only_repayment,
    total_cost_of_mortgage,
)
from .exceptions import IncorrectType


class MortgageBase:
    """Base class for mortgages."""

    def __init__(
        self,
        property_value: float | int,
        mortgage: float | int,
        term_months: float | int,
        interest_rate: float | int,
    ):
        """Initialises the MortgageBase class.

        Args:
            property_value (float | int): property value
            mortgage (float | int): mortgage amount
            term_months (float | int): term in months
            interest_rate (float | int): interest rate

        Raises:
            IncorrectType: If any of the inputs are not of type float or int.
        """
        if not all(
            isinstance(item, (float, int))
            for item in [property_value, mortgage, term_months, interest_rate]
        ):
            raise IncorrectType()

        self._property_value = float(property_value)
        self._mortgage = float(mortgage)
        self._term_months = float(term_months)
        self._interest_rate = float(interest_rate)

    @property
    def property_value(self) -> float:
        """Property value.

        Returns:
            float: Property value.
        """
        return self._property_value

    @property_value.setter
    def property_value(self, new_value: float | int) -> None:
        if new_value > 0 and isinstance(new_value, (float, int)):
            self._property_value = float(new_value)
        else:
            raise IncorrectType()

    @property
    def mortgage(self) -> float:
        """Mortgage amount.

        Returns:
            float: Mortgage amount.
        """
        return self._mortgage

    @mortgage.setter
    def mortgage(self, new_mortgage: float | int) -> None:
        if new_mortgage > 0 and isinstance(new_mortgage, (float, int)):
            self._new_mortgage = float(new_mortgage)
        else:
            raise IncorrectType()

    @property
    def term_months(self) -> float:
        """Term in months.

        Returns:
            float: Term in months.
        """
        return self._term_months

    @term_months.setter
    def term_months(self, new_term: float | int) -> None:
        if new_term > 0 and isinstance(new_term, (float, int)):
            self._term_months = float(new_term)
        else:
            raise IncorrectType()

    @property
    def interest_rate(self) -> float:
        """Interest rate.

        Returns:
            float: Interest rate.
        """
        return self._interest_rate

    @interest_rate.setter
    def interest_rate(self, new_rate: float | int) -> None:
        if new_rate > 0 and isinstance(new_rate, (float, int)):
            self._interest_rate = float(new_rate)
        else:
            raise IncorrectType()

    @cache
    def ltv(self) -> int:
        """Calculates the loan to value ratio.

        Returns:
            int: The loan to value ratio.
        """
        deposit = self.property_value - self.mortgage
        return ltv(property_value=self.property_value, deposit=deposit)


class CapitalRepaymentMortgage(MortgageBase):
    """Capital repayment mortgage class.

    Args:
        MortgageBase (MortgageBase): Base class for mortgage types.
    """

    @cache
    def monthly_repayment(self) -> float:
        """Calculates the monthly repayment for a capital repayment mortgage.

        Returns:
            float: The monthly repayment for a capital repayment mortgage.
        """
        return monthly_capital_repayment(
            mortgage=self.mortgage,
            interest_rate=self.interest_rate,
            mortgage_length_months=self.term_months,
        )

    @cache
    def mortgage_total_cost(self) -> float:
        """Calculates the total cost of the mortgage.

        Returns:
            float: The total cost of the mortgage.
        """
        return total_cost_of_mortgage(
            mortgage=self.mortgage,
            interest_rate=self.interest_rate,
            mortgage_length_months=self.term_months,
        )


class InterestOnlyMortgage(MortgageBase):
    """Interest only mortgage class.

    Args:
        MortgageBase (MortgageBase): Base class for mortgage types.
    """

    @cache
    def monthly_repayment(self) -> float:
        """Calculates the monthly repayment for an interest only mortgage.

        Returns:
            float: The monthly repayment for an interest only mortgage.
        """
        return monthly_interest_only_repayment(
            mortgage=self.mortgage, interest_rate=self.interest_rate
        )

    @cache
    def mortgage_total_cost(self) -> float:
        """Calculates the total cost of the mortgage.

        Returns:
            float: The total cost of the mortgage.
        """
        monthly_repayment = monthly_interest_only_repayment(
            mortgage=self.mortgage, interest_rate=self.interest_rate
        )
        return monthly_repayment * self.term_months
