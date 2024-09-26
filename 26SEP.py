class Solution:
    def maxStep(self, arr):
        c = 0  
        m = 0  
        for i in range(1, len(arr)):
            if arr[i] > arr[i - 1]:
                c += 1  
            else:
                m = max(m, c)  
                c = 0  
        return max(m, c)  
