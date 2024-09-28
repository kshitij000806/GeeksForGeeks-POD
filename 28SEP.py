class Solution:
    def minimizeCost(self, k, arr):
        n = len(arr)
        dp = [-1] * n
        dp[0] = 0
        
        for i in range(1, n):
            min_v = float('inf')
            for j in range(1, k+1):
                if i - j >= 0:
                    curr = dp[i - j] + abs(arr[i] - arr[i - j])
                    min_v = min(curr, min_v)
            dp[i] = min_v
            
        return dp[n - 1]
