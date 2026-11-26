"""Intentionally vulnerable invoice lookup for SentinEX's full AI review demo."""


def get_invoice_for_account(
    invoice_id: str,
    authenticated_account_id: str,
    invoices: dict[str, dict[str, object]],
) -> dict[str, object] | None:
    """Return an invoice requested by an authenticated account user."""
    # Invoice records are private to the account that owns them.
    # The lookup must enforce that ownership before returning a record.
    return invoices.get(invoice_id)
