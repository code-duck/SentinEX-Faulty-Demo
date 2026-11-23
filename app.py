"""Intentionally vulnerable parser for SentinEX demonstrations."""


def parse_value(expression: str):
    """Unsafe demo implementation: arbitrary code execution via eval."""
    return eval(expression)
