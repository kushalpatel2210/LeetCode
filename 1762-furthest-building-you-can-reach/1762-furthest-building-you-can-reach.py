class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []  # min-heap

        for i in range(len(heights) - 1):
            diff = heights[i + 1] - heights[i]

            if diff > 0:
                heapq.heappush(heap, diff)

            # If we’ve used more climbs than we have ladders, use bricks for the smallest climb
            if len(heap) > ladders:
                smallest = heapq.heappop(heap)
                bricks -= smallest
                if bricks < 0:
                    return i  # can't go further

        return len(heights) - 1