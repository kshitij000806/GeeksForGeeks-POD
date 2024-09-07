class Solution:
    def findNth(self, n):
        base9num = 0
        pos = 1
        
        while n > 0:
            base9num += (n % 9) * pos
            n //= 9
            pos *= 10
        
        return base9num