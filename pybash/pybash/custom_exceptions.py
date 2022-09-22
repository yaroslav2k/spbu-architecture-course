class UserExitException(Exception):
    """We use this exception when user wants to exit."""


class ParsingFailureException(Exception):
    """We use this exception when provided input cannot be parsed."""
