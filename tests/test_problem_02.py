import pytest
from problems.problem_02 import Solution


def test_constraints_length_str1_greater_than_1():
    str1 = ''
    str2 = 'matheus'
    obj = Solution()
    with pytest.raises(ValueError):
        obj.gcdOfStrings(str1, str2)

def test_constraints_length_str2_lower_than_1000():
    str1 = ''
    str2 = 1000 * 'AB'
    obj = Solution()
    with pytest.raises(ValueError):
        obj.gcdOfStrings(str1, str2)

def test_constraints_str1_str2_uppercase():
    str1 = 'ABC'
    str2 = 'de'
    obj = Solution()
    with pytest.raises(ValueError):
        obj.gcdOfStrings(str1, str2)

def test_strX_contains_all_strY():
    str1 = 'ABCABC'
    str2 = 'ABC'
    obj = Solution()
    assert 'ABC' ==  obj.gcdOfStrings(str1, str2)

def test_strX_contains_partial_strY():
    str1 = 'ABABAB'
    str2 = 'ABAB'
    obj = Solution()
    assert 'AB' ==  obj.gcdOfStrings(str1, str2)

def test_():
    str1 = 'TAUXXTAUXXTAUXXTAUXXTAUXX'
    str2 = 'TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX'
    obj = Solution()
    assert 'TAUXX' ==  obj.gcdOfStrings(str1, str2)

def test_2():
    str1 = 'AAAAAAAAA'
    str2 = 'AAACCC'
    obj = Solution()
    assert '' ==  obj.gcdOfStrings(str1, str2)