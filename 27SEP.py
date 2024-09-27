import heapq

class Solution:
    def max_of_subarrays(self, k, arr):
        res = []
        maxHeap = []

        for i in range(len(arr)):
            heapq.heappush(maxHeap, (-arr[i], i))
            while maxHeap[0][1] <= i - k:
                heapq.heappop(maxHeap)
            if i >= k - 1:
                res.append(-maxHeap[0][0])

        return res
