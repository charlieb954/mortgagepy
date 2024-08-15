from functools import cache

from .calculator import (
    interest_only_calculator,
    ltv_calculator,
    repayment_calculator,
    total_cost_of_mortgage,
)
from .exceptions import IncorrectType


class MortgageBase:
    def __init__(
        self,
        property_value: float | int,
        mortgage: float | int,
        term_months: float | int,
        interest_rate: float | int,
    ):
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
        return self._property_value

    @property_value.setter
    def property_value(self, new_value: float | int) -> None:
        if new_value > 0 and isinstance(new_value, (float, int)):
            self._property_value = float(new_value)
        else:
            raise IncorrectType()

    @property
    def mortgage(self) -> float:
        return self._mortgage

    @mortgage.setter
    def mortgage(self, new_mortgage: float | int) -> None:
        if new_mortgage > 0 and isinstance(new_mortgage, (float, int)):
            self._new_mortgage = float(new_mortgage)
        else:
            raise IncorrectType()

    @property
    def term_months(self) -> float:
        return self._term_months

    @term_months.setter
    def term_months(self, new_term: float | int) -> None:
        if new_term > 0 and isinstance(new_term, (float, int)):
            self._term_months = float(new_term)
        else:
            raise IncorrectType()

    @property
    def interest_rate(self) -> float:
        return self._interest_rate

    @interest_rate.setter
    def interest_rate(self, new_rate: float | int) -> None:
        if new_rate > 0 and isinstance(new_rate, (float, int)):
            self._interest_rate = float(new_rate)
        else:
            raise IncorrectType()

    @cache
    def ltv(self) -> int:
        deposit = self.property_value - self.mortgage
        return ltv_calculator(property_value=self.property_value, deposit=deposit)


class CapitalRepaymentMortgage(MortgageBase):
    @cache
    def monthly_repayment(self) -> float:
        return repayment_calculator(
            mortgage=self.mortgage,
            interest_rate=self.interest_rate,
            mortgage_length_months=self.term_months,
        )

    @cache
    def mortgage_total_cost(self) -> float:
        return total_cost_of_mortgage(
            mortgage=self.mortgage,
            interest_rate=self.interest_rate,
            mortgage_length_months=self.term_months,
        )


class InterestOnlyMortgage(MortgageBase):
    @cache
    def monthly_repayment(self) -> float:
        return interest_only_calculator(
            mortgage=self.mortgage, interest_rate=self.interest_rate
        )
    
    @cache
    def mortgage_total_cost(self) -> float:
        monthly_repayment = interest_only_calculator(
            mortgage=self.mortgage, interest_rate=self.interest_rate
        )
        return monthly_repayment * self.term_months
