# SentinEX faulty demo project

This is a deliberately unsafe demo target. `app.py` runs a command argument
list with `shell=True`, which Semgrep's Python security-audit rules flag. The
expected remediation is to use `shell=False`. A unit test checks the command
invocation options without executing a real shell command.

Suggested test command: `python -m unittest discover -v`
