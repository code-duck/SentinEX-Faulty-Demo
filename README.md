# SentinEX faulty demo project

This repository contains an intentional broken-access-control issue for testing SentinEX's Full AI Review workflow:

- `invoice_service.py`: returns an invoice by ID without checking that it belongs to the authenticated account. This business-logic issue may not match a Semgrep rule.
- `test_invoice_service.py`: checks both authorized and unauthorized invoice access. The targeted command is `python -m unittest test_invoice_service -v`.

Choose this repository folder in SentinEX, run **Scan project**, then run **Get full AI review**. The new example is intended to appear as a Gemini-only finding. Review its file, evidence, and proposed diff. After approving a patch, use Docker image `python:3.14-slim` and the targeted unittest command above. The test runner uses an offline disposable container; dependencies are not installed during the run.

Earlier demo issues in `app.py`, `insecure_ssl.py`, and `unsafe_eval.py` were fixed through merged PRs. Do not copy the intentionally unsafe example into real applications.
