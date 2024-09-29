class Solution:
    def totalCount(self, k, arr):
        count = 0
        for num in arr:
            count += (num + k - 1) // k  
        return count
