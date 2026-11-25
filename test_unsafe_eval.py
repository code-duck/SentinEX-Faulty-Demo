import unittest

from unsafe_eval import parse_literal


class UnsafeEvalTests(unittest.TestCase):
    def test_parses_literal_values(self):
        self.assertEqual(parse_literal("{'count': 3}"), {'count': 3})

    def test_rejects_executable_expressions(self):
        with self.assertRaises((ValueError, SyntaxError)):
            parse_literal("__import__('math').sqrt(4)")


if __name__ == '__main__':
    unittest.main()
