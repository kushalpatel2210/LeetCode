import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        priority_queue = []
        topK = []

        for key, value in counter.items():
            heapq.heappush(priority_queue, (-value, key))

        for i in range(k):
            element = heapq.heappop(priority_queue)
            topK.append(element[1])

        return topK