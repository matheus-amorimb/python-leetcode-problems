from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        spots_free = 0
        range_list = len(flowerbed) - 1
        for index, spot in enumerate(flowerbed):
            if spot == 0:
                if (index == 0 or flowerbed[index - 1] == 0) and (
                    index == range_list
                    or (index < range_list and flowerbed[index + 1] == 0)
                ):
                    flowerbed[index] = 1
                    spots_free += 1

        return spots_free >= n
