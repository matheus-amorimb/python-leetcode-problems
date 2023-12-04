import pytest

from problems.problem_8 import Solution


def test_case_1():
    s = Solution()
    nums = [1,2,3,4,5]
    result = s.increasingTriplet(nums)
    assert result == True

def test_case_2():
    s = Solution()
    nums = [5,4,3,2,1]
    result = s.increasingTriplet(nums)
    assert result == False

def test_case_3():
    s = Solution()
    nums = [2,1,5,0,4,6]
    result = s.increasingTriplet(nums)
    assert result == True

def test_case_3():
    s = Solution()
    nums = [20,100,10,12,5,13]
    result = s.increasingTriplet(nums)
    assert result == True