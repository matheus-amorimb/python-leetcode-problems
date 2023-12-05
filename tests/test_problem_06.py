import pytest
from problems.problem_6 import Solution

def test_basic_cases():
    assert Solution().reverseWords("the sky is blue") == "blue is sky the"
    assert Solution().reverseWords("  hello world  ") == "world hello"
    assert Solution().reverseWords("a good   example") == "example good a"

def test_edge_cases():
    assert Solution().reverseWords("") == ""
    assert Solution().reverseWords("singleword") == "singleword"
    assert Solution().reverseWords("  ") == ""

def test_special_characters_and_numbers():
    assert Solution().reverseWords("123 456 789") == "789 456 123"

def test_multiple_spaces_between_words():
    assert Solution().reverseWords("word1   word2   word3") == "word3 word2 word1"

def test_leading_and_trailing_spaces():
    assert Solution().reverseWords("   leading spaces") == "spaces leading"
    assert Solution().reverseWords("trailing spaces   ") == "spaces trailing"

def test_repeated_spaces():
    assert Solution().reverseWords("word1   word2   word3") == "word3 word2 word1"

# Add more test functions as needed
