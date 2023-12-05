"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 
Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

"""
# from .execution_time import timing_decorator
from typing import List
import math


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums_aux = nums.copy()
        result = []
        itens_calculated = []
        for item in nums:
            # print(item)
            if item in itens_calculated:
                prod = result[nums_aux.index(item)]
                result.append(prod)
            else:
                itens_calculated.append(item)
                nums_aux.pop(nums_aux.index(item))
                prod = math.prod(nums_aux)
                result.append(prod)
                nums_aux = nums.copy()

        return result
    
class Solution2:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n

        # Calculate the prefix products
        prefix_product = 1
        for i in range(n):
            result[i] *= prefix_product
            prefix_product *= nums[i]

        # Calculate the suffix products
        suffix_product = 1
        for i in range(n - 1, -1, -1):
            result[i] *= suffix_product
            suffix_product *= nums[i]

        return result

s = Solution2()
s.productExceptSelf([1,2,3])