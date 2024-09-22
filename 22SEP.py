class Solution:
    def lps(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0

        lpsArr = [0] * n
        j = 0

        for i in range(1, n):
            while j > 0 and s[i] != s[j]:
                j = lpsArr[j - 1]
            if s[i] == s[j]:
                j += 1
            lpsArr[i] = j

        return lpsArr[n - 1]
