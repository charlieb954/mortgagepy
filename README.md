# mortgagepy

[![ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
[![Actions status](https://github.com/charlieb954/mortgagepy/actions/workflows/ci.yml/badge.svg)](https://github.com/charlieb954/mortgagepy/actions)
<!-- ![PyPI version](https://img.shields.io/pypi/v/mortgagepy.svg) -->

**mortgagepy** is a python library used to work out common mortgage calculations
including captial repayments, total cost of ownership and single month interest.

**NOTE: This repository is still in development and the primary purpose is to
understand good python packaging practices.**

## Installation

To install `mortgagepy` use the following command:

```bash
pip install git+https://github.com/charlieb954/mortgagepy.git
```

## Examples - mortgage

Create a mortgage object and use it to compare against other mortgages.

Initialise a mortgage object.

```python
>>> from mortgagepy import CapitalRepaymentMortgage

>>> my_mortgage = CapitalRepaymentMortgage(
        property_value=280000, mortgage=210000, term_months=300, interest_rate=1.8
    )
```

Get a summary of the mortgage.

```python
>>> my_mortgage.summarise(printed=True)

property value (£)       : 280000.0
mortgage (£)             : 210000.0
loan to value (%)        : 75
monthly repayment (£)    : 869.79
term (months)            : 300
interest rate (%)        : 1.8
interest paid (£)        : 50937.0
total cost (£)           : 260937.0
```

Calculate overpayment impact of the mortgage.

```python
>>> my_mortgage.overpayment_projection(monthly_overpayment=100)

{
    'time to repay (months)': 263,
    'time saved (months)': 37.0,
    'total interest paid (%)': 23811.59,
    'interest saved (£)': 3617.41
}
```

Access individual attributes such as monthly repayments or LTV.

```python
>>> my_mortgage.monthly_repayment()

869.79
```

```python
>>> my_mortgage.ltv()

75
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
>>> monthly_interest_only_repayment(
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

Calulate the time saved by overpaying on your mortgage.

```python
>>> from mortgagepy.calculator import capital_overpayment
>>> capital_overpayment(
        mortgage=200000, interest_rate=3.5, mortgage_length_months=300, monthly_overpayment=100
    )

{
    'time to repay (months)": 262,
    'time saved (months)': 38,
    'total interest paid (%)': 87992.71
}
```

## Examples - compare

Compare the cost of two interest rates for a capital repayment mortgage.

```python
>>> from mortgagepy.compare import compare_capital_repayment_rates
>>> compare_capital_repayment_rates(
        mortgage=130_500, interest_rates=[1, 2], mortgage_length_months=300
    )

{
    0: {'interest_rate': 1, 'repayment': 491.82},
    1: {'interest_rate': 2, 'repayment': 553.13}
}
```

Compare the cost of two interest rates for an interest only mortgage.

```python
>>> from mortgagepy.compare import compare_interest_only_rates
>>> compare_interest_only_rates(
        mortgage=130_500, interest_rates=[1, 2]
    )

{
    0: {'interest_rate': 1, 'repayment': 108.75},
    1: {'interest_rate': 2, 'repayment': 217.5}
}
```
