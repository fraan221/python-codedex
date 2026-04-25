import unittest
from string_utils import reverse_string, capitalize_string, is_capitalized


class TestStringUtils(unittest.TestCase):

    def test_reverse_string(self):
        string = reverse_string("Franco")
        self.assertEqual(string, "ocnarF")

    def test_capitalize_string(self):
        string = capitalize_string("franco")
        self.assertEqual(string, "Franco")

    def test_is_capitalized(self):
        string = is_capitalized("Franco")
        self.assertTrue(string)


if __name__ == "__main__":
    unittest.main()
