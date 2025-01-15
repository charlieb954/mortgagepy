"""Custom exceptions for the mortgagepy package."""

from typing import Optional


class IncorrectType(Exception):
    """custom exception for incorrect type passed to a function."""

    message = "Please ensure you have passed the correct arg value."

    def __init__(
        self, message: Optional[str] = None, errors: Optional[str] = None
    ):
        """Initializes the IncorrectType exception.

        Args:
            message (Optional[str], optional): message to raise.
                Default is None.
            errors (Optional[str], optional): errors to share.
                Default is None.
        """
        super().__init__(message or self.message)
        self.errors = errors
