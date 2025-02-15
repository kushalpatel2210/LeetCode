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