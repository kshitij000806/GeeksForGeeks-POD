class Solution:
    def smallestWindow(self, s, p):
        if len(p) > len(s):
            return "-1"

        phash = [0] * 256
        for ch in p:
            phash[ord(ch)] += 1

        shash = [0] * 256
        minLength = float('inf')
        startIndex = -1
        count = 0
        left = 0

        for right in range(len(s)):
            ch = s[right]
            shash[ord(ch)] += 1

            if phash[ord(ch)] != 0 and shash[ord(ch)] <= phash[ord(ch)]:
                count += 1

            while count == len(p):
                if right - left + 1 < minLength:
                    minLength = right - left + 1
                    startIndex = left
                
                leftChar = s[left]
                shash[ord(leftChar)] -= 1

                if phash[ord(leftChar)] != 0 and shash[ord(leftChar)] < phash[ord(leftChar)]:
                    count -= 1
                
                left += 1  

        if startIndex == -1:
            return "-1"
        return s[startIndex:startIndex + minLength]
