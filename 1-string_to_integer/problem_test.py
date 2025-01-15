import unittest
from .problem import Solution

class TestMyAtoi(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_case_1(self):
        s = "42"
        expected = 42
        result = self.solution.myAtoi(s)
        self.assertEqual(result, expected, f"Failed for input: {s}")

    def test_case_2(self):
        s = "   -042"
        expected = -42
        result = self.solution.myAtoi(s)
        self.assertEqual(result, expected, f"Failed for input: {s}")

    def test_case_3(self):
        s = "1337c0d3"
        expected = 1337
        result = self.solution.myAtoi(s)
        self.assertEqual(result, expected, f"Failed for input: {s}")

    def test_case_4(self):
        s = "0-1"
        expected = 0
        result = self.solution.myAtoi(s)
        self.assertEqual(result, expected, f"Failed for input: {s}")

    def test_case_5(self):
        s = "words and 987"
        expected = 0
        result = self.solution.myAtoi(s)
        self.assertEqual(result, expected, f"Failed for input: {s}")