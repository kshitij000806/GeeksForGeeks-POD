class Solution:
    def rearrange(self, arr):
        n = len(arr)
        pos = []
        neg = []
        for i in range(n):
            if arr[i] >= 0:
                pos.append(arr[i])
            else:
                neg.append(arr[i])
        i = j = k = 0
        toggle = True
        while i < len(pos) and j < len(neg):
            if toggle:
                arr[k] = pos[i]
                i += 1
            else:
                arr[k] = neg[j]
                j += 1
            k += 1
            toggle = not toggle
        while i < len(pos):
            arr[k] = pos[i]
            i += 1
            k += 1
        while j < len(neg):
            arr[k] = neg[j]
            j += 1
            k += 1
