import pytest
from problems.problem_01 import Solution


def test_contraint_length_word1_greater_than_1():
    word1 = ''
    word2 = 'matheus'
    obj = Solution()
    with pytest.raises(ValueError):
        obj.mergeAlternately(word1, word2)

def test_contraint_length_word2_lower_than_100():
    word1 = ''
    word2 = 100 * 'AB'
    obj = Solution()
    with pytest.raises(ValueError):
        obj.mergeAlternately(word1, word2)

def test_contraint_word1_word2_lowercase():
    word1 = 'ABC'
    word2 = 'de'
    obj = Solution()
    with pytest.raises(ValueError):
        obj.mergeAlternately(word1, word2)

def test_result_if_len_word1_equal_len_word2():
    word1 = 'abc'
    word2 =  'pqr'
    result = 'apbqcr'
    obj = Solution()
    assert result == obj.mergeAlternately(word1, word2)

def test_result_if_len_word1_greater_than_len_word2():
    word1 = 'abcd'
    word2 =  'pq'
    result = 'apbqcd'
    obj = Solution()
    assert result == obj.mergeAlternately(word1, word2)

def test_result_if_len_word2_greater_than_len_word1():
    word1 = 'ab'
    word2 =  'pqrs'
    result = 'apbqrs'
    obj = Solution()
    assert result == obj.mergeAlternately(word1, word2)