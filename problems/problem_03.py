from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:

        my_list = []

        for index, kid in enumerate(candies):
            my_list.append(True)
            for index2, others_kid in enumerate(candies):
                if index != index2:
                    if kid + extraCandies < others_kid:
                        my_list[index] = False
                        break
                    
        return my_list

candies = [2,3,5,1,3] 
extraCandies = 3

solution = Solution()
solution.kidsWithCandies(candies, extraCandies)