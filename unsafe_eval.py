import ast


def parse_literal(value: str):
    """Parse a user-provided Python literal."""
    return ast.literal_eval(value)
