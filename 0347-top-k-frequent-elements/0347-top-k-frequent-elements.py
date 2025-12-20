import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = dict()

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        minHeap = []
        for num, cnt in count.items():
            heapq.heappush(minHeap, (cnt, num))

            if len(minHeap) > k:
                heapq.heappop(minHeap)
        
        res = []
        for i in range(k):
            res.append(heapq.heappop(minHeap)[1])
        
        return res


"""
Sol 1: Sorting 
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = dict()

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        arr = []
        for num, cnt in count.items():
            arr.append([cnt, num])
        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        
        return res
"""