import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-ele for ele in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)

            if x != y:
                heapq.heappush(stones, -abs(y - x))
        
        return -stones[0] if stones else 0
            