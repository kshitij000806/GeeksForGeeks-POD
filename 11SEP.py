import heapq

class Solution:
    def minCost(self, arr):
        heapq.heapify(arr)
        totalCost = 0
        while len(arr) > 1:
            first = heapq.heappop(arr)
            second = heapq.heappop(arr)
            cost = first + second
            totalCost += cost
            heapq.heappush(arr, cost)

        return totalCost
