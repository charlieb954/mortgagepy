# mortgagepy

[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)

**mortgagepy** is a python library used to work out common mortgage calculations
including captial repayments, total cost of ownership and single month interest.

## Installation

To use this library, currently you will need to git clone it and install using
the following command:

```bash
pip install uv
uv venv
uv pip install .[dev] # to include the developer dependencies
uv pip install .'[dev]' # for mac
```

Alternatively, it can be installed without cloning directly from this GitHub
page using the following command:

```bash
pip install git+https://github.com/charlieb954/mortgagepy.git
```

## Examples - calculator

Calculate the monthly repayment for a capital payment mortgage.
```python
>>> from mortgagepy.calculator import monthly_capital_repayment
>>> monthly_capital_repayment(
        mortgage=130_500, interest_rate=6.89, mortgage_length_months=300
    )
913.21
```

Work out the total cost of a mortgage.
```python
>>> from mortgagepy.calculator import total_cost_of_mortgage
>>> total_cost_of_mortgage(
        mortgage=130_500, interest_rate=6.89, mortgage_length_months=300
    )
273_963.0
```

Calculate repayments for an interest only mortgage.
```python
>>> from mortgagepy.calculator import monthly_interest_only
>>> monthly_interest_only(
        mortgage=130_500, interest_rate=3.89
    )
423.04
```

Calculate the loan-to-value as a percentage given a deposit and property value.
```python
>>> from mortgagepy.calculator import ltv
>>> ltv(
        property_value=200_000, deposit=50_000
    )
75
```

Calculate the monthly interest to be paid on a mortgage.
```python
>>> from mortgagepy.calculator import monthly_interest

>>> monthly_interest(
        balance_at_previous_month=98_868.70, interest_rate=1.89, month=10, year=2023
    )
158.7
```

## Examples - compare

Compare the cost of two interest rates for a capital repayment mortgage.
```python
>>> from mortgagepy.compare import compare_repayment_interest_rates
>>> compare_repayment_interest_rates(
        mortgage=130_500, interest_rates=[1, 2], mortgage_length_months=300
    )
{1: 491.82, 2: 553.13}
```

Compare the cost of two interest rates for an interest only mortgage.
```python
>>> from mortgagepy.compare import compare_interest_only_rates
>>> compare_interest_only_rates(
        mortgage=130_500, interest_rates=[1, 2]
    )
{1: 108.33, 2: 216.67}
```

## Examples - mortgage

Create a mortgage object and get important information such as loan-to-value and
monthly repayments.
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