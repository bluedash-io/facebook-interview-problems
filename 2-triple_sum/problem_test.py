import unittest
from typing import Iterable
from .problem import Solution

class TestThreeSum(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_case_1(self):
        result = self.solution.three_sum([-1, 0, 1, 2, -1, -4])
        expected = [[-1, -1, 2], [-1, 0, 1]]
        if not isinstance(result, Iterable):
            self.fail("Result is not an iterable")
        self.assertEqual(sorted(self.solution.three_sum([-1, 0, 1, 2, -1, -4])), sorted(expected))

    def test_case_2(self):
        self.assertEqual(self.solution.three_sum([0, 1, 1]), [])

    def test_case_3(self):
        self.assertEqual(self.solution.three_sum([0, 0, 0]), [[0, 0, 0]])