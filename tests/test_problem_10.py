import pytest
from problems.problem_10 import Solution


def test_case_1():
    s = Solution()
    nums = [0,1,0,3,12]
    result = s.moveZeroes(nums)
    assert result == [1,3,12,0,0]

def test_case_2():
    s = Solution()
    nums = [0]
    result = s.moveZeroes(nums)
    assert result == [0]
