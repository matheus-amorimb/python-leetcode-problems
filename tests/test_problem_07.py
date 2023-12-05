import pytest
from problems.problem_7 import Solution

def test_productExceptSelf_example_1():
    input1 = [1,2,3,4]
    output1 = [24,12,8,6]

    input2 = [-1,1,0,-3,3]
    output2 = [0,0,9,0,0]

    assert output1 == Solution().productExceptSelf(input1)
    assert output2 == Solution().productExceptSelf(input2)

def test_productExceptSelf_example_2():
    input2 = [-1,1,0,-3,3]
    output2 = [0,0,9,0,0]

    assert output2 == Solution().productExceptSelf(input2)