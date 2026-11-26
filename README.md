# SentinEX faulty demo project

This repository contains three intentional Python security flaws for testing SentinEX:

- `unsafe_eval.py`: uses `eval()` on user-provided text. Semgrep should detect it. `test_unsafe_eval.py` checks safe literals and rejects executable expressions; run it with `python -m unittest test_unsafe_eval -v`.
- `invoice_service.py`: returns an invoice by ID without checking that it belongs to the authenticated account. This business-logic issue is intended for Full AI Review and may not match a Semgrep rule. `test_invoice_service.py` checks owner and non-owner access; run it with `python -m unittest test_invoice_service -v`.
- `insecure_ssl.py`: creates a TLS context that skips certificate verification. Semgrep should detect it, and SentinEX offers an offline built-in remediation. `test_insecure_ssl.py` checks that certificate and hostname verification are enabled; run it with `python -m unittest test_insecure_ssl -v`.

Choose this repository folder in SentinEX and run **Scan project**. Use **Get full AI review** for the invoice ownership issue. The `eval` and TLS findings also have local built-in fixes. Review each diff, approve only the fix you want to demonstrate, and run the corresponding targeted unittest in Docker with image `python:3.14-slim`. Do not copy the intentionally unsafe examples into real applications.
