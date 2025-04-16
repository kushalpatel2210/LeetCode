import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        minSpeed = 1
        maxSpeed = max(piles)
        speed = float('inf')

        def canFinishPiles(speed):
            currHours = 0
            for pile in piles:
                currHours += math.ceil(pile/speed)
            return currHours <= h

        while minSpeed <= maxSpeed:
            midSpeed = minSpeed + (maxSpeed - minSpeed) // 2
            KokoCanFinishPiles = canFinishPiles(midSpeed)

            if KokoCanFinishPiles:
                speed = min(speed, midSpeed)
                maxSpeed = midSpeed - 1
            else:
                minSpeed = midSpeed + 1
        
        return speed
