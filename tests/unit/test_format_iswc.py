import unittest
from data_sources.aux_functions import clean_string_iswc

# References: https://realpython.com/python-testing/

class TestFormatISWC(unittest.TestCase):

    def test_clean_string_iswc_usual(self):
        """
        Testing hte usual behaviour of the string format
        """
        self.assertEqual(clean_string_iswc('T-042088917-3'), 'T0420889173', "Should be T0420889173")

    def test_clean_string_iswc_empty(self):
        """
        Testing empty strings
        """
        self.assertEqual(clean_string_iswc(''), '', "Should be empty")


if __name__ == '__main__':
    unittest.main()
