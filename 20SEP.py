class Solution:
    def countBuildings(self, height):
        count = 0
        max_height = float('-inf')

        for h in height:
            if h > max_height:
                count += 1
                max_height = h 
        
        return count
