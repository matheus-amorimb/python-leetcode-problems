from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:

        greatest_value = max(candies)

        return print([x + extraCandies >= greatest_value for x in candies])

candies = [2,3,5,1,3] 
extraCandies = 3

solution = Solution()
solution.kidsWithCandies(candies, extraCandies)

