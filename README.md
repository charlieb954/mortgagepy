# mortgagepy

[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

**mortgagepy** is a python library used to work out common mortgage calculations including captial repayments, total cost of ownership and single month interest.

## Installation

To use this library, currently you will need to git clone it and install using the following command:

```bash
pip install .
pip install .[dev] # to include the developer dependencies
pip install .'[dev]' # for mac
```

Alternatively, it can be installed without cloning directly from this GitHub page using the following command:

```bash
pip install git+https://github.com/charlieb954/mortgagepy.git
```

## Examples - calculator

```python
>>> from mortgagepy.calculator import (
    repayment_calculator,
    total_cost_of_mortgage,
    interest_only_calculator,
    ltv_calculator,
    monthly_interest,
    compare_repayment_interest_rates
)
>>> repayment_calculator(
        mortgage=130_500, interest_rate=6.89, mortgage_length_months=300
    )
913.21
>>> total_cost_of_mortgage(
        mortgage=130_500, interest_rate=6.89, mortgage_length_months=300
    )
273_963.0
>>> interest_only_calculator(
        mortgage=130_500, interest_rate=3.89
    )
423.04
>>> ltv_calculator(
        property_value=200_000, deposit=50_000
    )
75
>>> monthly_interest(
        balance_at_previous_month=-98_868.70, interest_rate=1.89, month=10, year=2023
    )
-158.70
>>> compare_repayment_interest_rates(
        mortgage=130_500, interest_rates=[1, 2], mortgage_length_months=300
    )
{1: 491.82, 2: 553.13}
```

## Examples - mortgage
```python
>>> from mortgagepy import CapitalRepaymentMortgage

>>> my_mortgage = CapitalRepaymentMortgage(
        property_value=280000, mortgage=210000, term_months=300, interest_rate=1.8
    )
>>> my_mortgage.monthly_repayment()
869.79
>>> my_mortgage.ltv()
75
```