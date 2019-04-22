import unittest
from trucs import add_spaces


class TestTest(unittest.TestCase):

    def test_test(self):
        print('Hello World')
        self.assertTrue(True)

    def test_add_spaces(self):
        input_str = "lala lili loulou"
        n = 4
        result = add_spaces(input_str, n)
        expected = "    lala lili loulou"
        self.assertSequenceEqual(result, expected)

    def test_lala(self):
        self.assertSequenceEqual(add_spaces('love', 1), ' love')


if __name__ == "__main__":
    unittest.main()
