# SentinEX faulty demo project

This repository contains two intentional Python security flaws for testing SentinEX:

- `unsafe_eval.py`: uses `eval()` on user-provided text. Semgrep should detect it. `test_unsafe_eval.py` checks safe literals and rejects executable expressions; run it with `python -m unittest test_unsafe_eval -v`.
- `invoice_service.py`: returns an invoice by ID without checking that it belongs to the authenticated account. This business-logic issue is intended for Full AI Review and may not match a Semgrep rule. `test_invoice_service.py` checks owner and non-owner access; run it with `python -m unittest test_invoice_service -v`.

Choose this repository folder in SentinEX, run **Scan project**, and use **Get full AI review** to look for the invoice ownership issue. Review each proposed diff, approve only the fix you want to demonstrate, and run the corresponding targeted unittest in Docker with image `python:3.14-slim`. Do not copy the intentionally unsafe examples into real applications.
