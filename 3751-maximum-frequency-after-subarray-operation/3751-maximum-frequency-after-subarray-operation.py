from collections import Counter

class Solution:
    def maxOccurences(self, nums, target, k):
        maxCount = currCount = 0

        for num in nums:
            if num == k:
                currCount -= 1
            
            if num == target:
                currCount += 1
            
            if currCount < 0:
                currCount = 0
            
            maxCount = max(maxCount, currCount)
        
        return maxCount

    def maxFrequency(self, nums: List[int], k: int) -> int:
        counter = Counter(nums)
        maxFreq = 0

        for key, frq in counter.items():
            maxFreq = max(maxFreq, self.maxOccurences(nums, key, k))
        
        return counter[k] + maxFreq