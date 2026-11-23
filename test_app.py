import unittest

from app import parse_value


class ParseValueTests(unittest.TestCase):
    def test_parses_integer_literal(self):
        self.assertEqual(parse_value("42"), 42)

    def test_parses_list_literal(self):
        self.assertEqual(parse_value("[1, 2, 3]"), [1, 2, 3])


if __name__ == "__main__":
    unittest.main()
