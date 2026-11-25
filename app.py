"""Intentionally vulnerable command runner for SentinEX demonstrations."""

import subprocess


def run_command(arguments: list[str]) -> str:
    """Unsafe demo implementation: invokes a shell for a command argument list."""
    result = subprocess.run(
        arguments,
        shell=False,
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout.strip()
