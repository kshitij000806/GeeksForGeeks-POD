class Solution:
    def rotateDelete(self, arr):
        n = len(arr)
        k = 1
        while n > 1:
            arr.insert(0, arr.pop())
            id = n - k
            if id < 0:
                id = 0
            arr.pop(id)
            k += 1
            n -= 1
        
        return arr[0]
