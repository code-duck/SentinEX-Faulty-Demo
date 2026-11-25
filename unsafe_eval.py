import ast


def parse_literal(value: str):
    """Parse a user-provided Python literal."""
    return eval(value)
