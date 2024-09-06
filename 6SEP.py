class Solution:
    def maxSubArraySum(self, arr):
        maxh = 0
        maxf = float('-inf')

        for num in arr:
            maxh = max(num, maxh + num)
            maxf = max(maxf, maxh)
        
        return maxf