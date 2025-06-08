import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        ans = float('inf')

        def timeTakenToEatAllBananas(speed):
            time = 0
            for pile in piles:
                time += math.ceil(pile / speed)
            
            return time

        while l <= r:
            m = l + (r - l) // 2

            time = timeTakenToEatAllBananas(m)

            if time > h:
                l = m + 1
            else:
                ans = min(ans, m)
                r = m - 1
        
        return ans