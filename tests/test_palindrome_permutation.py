# tests/test_palindrome_permutation.py

import unittest
from student_code import palindrome_permutation  # Ensure this matches the student's function location

class TestPalindromePermutation(unittest.TestCase):

    def test_example_cases(self):
        self.assertTrue(palindrome_permutation("Tact Coa"))
        self.assertFalse(palindrome_permutation("This is not a palindrome permutation"))
        self.assertTrue(palindrome_permutation("A man a plan a canal Panama"))

    def test_empty_string(self):
        self.assertTrue(palindrome_permutation(""))

    def test_single_character(self):
        self.assertTrue(palindrome_permutation("a"))

    def test_multiple_whitespaces(self):
        self.assertTrue(palindrome_permutation("taco cat"))

if __name__ == '__main__':
    unittest.main()
