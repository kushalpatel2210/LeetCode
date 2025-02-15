class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        res = r

        def canShip(cap):
            ships, currCap = 1, cap
            for w in weights:
                if currCap - w < 0:
                    ships += 1
                    if ships > days:
                        return False
                    currCap = cap

                currCap -= w
            return True

        while l <= r:
            cap = (l + r) // 2
            if canShip(cap):
                res = min(res, cap)
                r = cap - 1
            else:
                l = cap + 1

        return res
        
'''
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        minWeight = max(weights)
        maxWeight = sum(weights)
        totalShipments = len(weights)
        l, r = minWeight, maxWeight
        minShipWeight = float('inf')

        while l <= r:
            m = l + (r - l) // 2
            totalDays = 0
            currentWeight = 0
            i = 0

            # calculate total days
            while i < totalShipments:
                currentWeight += weights[i]

                if currentWeight <= m:
                    if i == totalShipments - 1:
                        totalDays += 1
                    i += 1
                    continue
                # print(f" i {i} currentWeight {currentWeight}")

                totalDays += 1
                currentWeight = 0

            # print(f"l {l} r {r} m {m} totalDays {totalDays}")

            if totalDays > days:
                l = m + 1
            else:
                minShipWeight = min(minShipWeight, m)
                r = m - 1

        return minShipWeight
'''