class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        totalBananas = sum(piles)
        minSpeed = math.ceil(totalBananas / h)
        maxSpeed = max(piles)
        l, r = minSpeed, maxSpeed
        minEatSpeed = float('inf')

        while l <= r:
            m = l + (r - l) // 2
            totalIterations = 0

            for pile in piles:
                totalIterations += math.ceil(pile / m)
            
            if totalIterations > h:
                l = m + 1
            else:
                minEatSpeed = min(minEatSpeed, m)
                r = m - 1 

        return minEatSpeed