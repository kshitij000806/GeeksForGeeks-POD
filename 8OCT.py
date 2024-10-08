from typing import List

class Solution:
    def pairsum(self, arr: List[int]) -> int:
        n = len(arr)
        if n < 2:
            return -1  

        first, second = float('-inf'), float('-inf')

        for num in arr:
            if num > first:
                second = first
                first = num
            elif num > second:
                second = num

        return first + second
