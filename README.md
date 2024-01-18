# mortgagepy

<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a> 


**mortgagepy** is a python library used to work out common mortgage calculations including captial repayments, total cost of ownership and single month interest.

## Examples

```python
>>> import mortgagepy
>>> mortgagepy.repayment_calculator(mortgage=130_500, interest_rate=6.89, mortgage_length_months=300)
913.21
>>> mortgagepy.total_cost_of_mortgage(mortgage=130_500, interest_rate=6.89, mortgage_length_months=300)
273_963.0
>>> mortgagepy.test_interest_only_calculator(mortgage=130_500, interest_rate=3.89)
423.04
>>> mortgagepy.ltv_calculator(property_price=200_000, deposit=50_000)
75
>>> mortgagepy.monthly_interest(balance_at_previous_month=-98_868.70, interest_rate=1.89, month=10, year=2023)
-158.70
```

