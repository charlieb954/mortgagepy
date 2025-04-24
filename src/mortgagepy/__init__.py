"""mortgagepy - A Python package for mortgage calculations."""

from importlib.metadata import PackageNotFoundError, version

from . import calculator, compare, exceptions, utils
from .mortgage import (
    CapitalRepaymentMortgage,
    InterestOnlyMortgage,
    MortgageBase,
)

try:
    __version__ = version("mortgagepy")
except PackageNotFoundError:
    pass

__all__ = [
    "IncorrectType",
    "CapitalRepaymentMortgage",
    "InterestOnlyMortgage",
    "MortgageBase",
    "calculator",
    "compare",
    "exceptions",
    "utils",
]
