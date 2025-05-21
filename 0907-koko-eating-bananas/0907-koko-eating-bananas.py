import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        minSpeed = float('inf')
        
        def timeTaken(speed):
            totalTime = 0

            for pile in piles:
                totalTime += math.ceil(pile/speed)
            
            return totalTime
        
        l, r = 1, max(piles)

        while l <= r:
            m = l + (r - l) // 2

            if timeTaken(m) <= h:
                minSpeed = min(minSpeed, m)
                r = m - 1
            else:
                l = m + 1
        
        return minSpeed