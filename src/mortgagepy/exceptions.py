from typing import Optional


class IncorrectType(Exception):
    message = "Please ensure you have passed the correct arg value."

    def __init__(self, message: Optional[str] = None, errors: Optional[str] = None):
        super().__init__(message or self.message)
        self.errors = errors
