import ssl
import unittest

from insecure_ssl import client_context


class InsecureSSLTests(unittest.TestCase):
    def test_context_verifies_certificates_and_hostnames(self):
        context = client_context()
        self.assertEqual(context.verify_mode, ssl.CERT_REQUIRED)
        self.assertTrue(context.check_hostname)


if __name__ == '__main__':
    unittest.main()
