import pytest

from problems.problem_9 import Solution


def test_case_1():
    s = Solution()
    chars = ["a","a","b","b","c","c","c"]
    result = s.compress(chars)
    assert result == 6

def test_case_2():
    s = Solution()
    chars = ["a"]
    result = s.compress(chars)
    assert result == 1

def test_case_3():
    s = Solution()
    chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
    result = s.compress(chars)
    assert result == 4