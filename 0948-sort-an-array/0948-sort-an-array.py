import heapq
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        sortedList = list()
        heapq.heapify(nums)

        while len(nums) > 0:
            sortedList.append(heapq.heappop(nums))
        
        return sortedList
