# SentinEX faulty demo project

This repository is intentionally vulnerable for a SentinEX demonstration. Its `main` branch contains independent Python security findings:

- `unsafe_eval.py`: evaluates a string as Python code. The targeted test command is `python -m unittest test_unsafe_eval -v`.
- `insecure_ssl.py`: disables TLS certificate and hostname verification. The targeted test command is `python -m unittest test_insecure_ssl -v`.

Choose this repository folder in SentinEX and run **Scan project**. Fix one finding at a time; each proposed patch changes one file. For the Docker test step, use the matching targeted test command above with image `python:3.14-slim`. The other finding may remain after a one-file fix, so inspect and acknowledge it in SentinEX before approving a merge.

The first vulnerability fixed in PR #1 (`app.py`) is already on `main`. These two new examples are the current showcase targets. Do not copy these intentionally unsafe patterns into real applications.
