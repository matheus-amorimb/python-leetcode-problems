class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        for right, num in enumerate(nums):
        
            if num:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1