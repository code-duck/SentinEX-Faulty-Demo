# SentinEX faulty demo project

This is a deliberately vulnerable demo target. `app.py` uses Python `eval`,
which can execute arbitrary expressions. SentinEX should flag this and propose
using `ast.literal_eval` for safe parsing of Python literals.

Suggested test command: `python -m unittest discover -v`
