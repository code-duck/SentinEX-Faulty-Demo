import unittest

from invoice_service import get_invoice_for_account


class InvoiceServiceTests(unittest.TestCase):
    def setUp(self):
        self.invoices = {
            "invoice-42": {
                "owner_id": "account-b",
                "amount": 125,
            }
        }

    def test_owner_can_read_their_invoice(self):
        result = get_invoice_for_account("invoice-42", "account-b", self.invoices)
        self.assertEqual(result, self.invoices["invoice-42"])

    def test_other_account_cannot_read_invoice(self):
        result = get_invoice_for_account("invoice-42", "account-a", self.invoices)
        self.assertIsNone(result)


if __name__ == "__main__":
    unittest.main()
