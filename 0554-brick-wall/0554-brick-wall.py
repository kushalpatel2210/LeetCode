from collections import defaultdict
class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        res = float('inf')
        totalLength = sum(wall[0])
        hashMap = defaultdict(int)

        for bricks in wall:
            intersection = 0
            for brick in bricks:
                intersection += brick 
                hashMap[intersection] += 1
        
        if len(hashMap) == 1:
            return len(wall)

        for intersection, noOfIntersections in hashMap.items():
            if intersection < totalLength:
                res = min(res, len(wall) - noOfIntersections)

        return res