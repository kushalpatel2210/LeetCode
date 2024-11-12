from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        most_common = count.most_common(k)
        result = [element[0] for element in most_common]

        return result

'''
# using priority queue
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        priority_queue = []
        result = []
        
        for key, value in count.items():
            heapq.heappush(priority_queue, (-value, key))
        
        for _ in range(0, k):
            priority, element = heapq.heappop(priority_queue)
            result.append(element)

        return result
'''