class Solution:
    def missingNumber(self, n, arr):
        xor_total = 0
        for i in range(1, n + 1):
            xor_total ^= i
        xor_array = 0
        for num in arr:
            xor_array ^= num
        return xor_total ^ xor_array