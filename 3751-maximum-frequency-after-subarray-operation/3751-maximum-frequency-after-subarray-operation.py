from collections import Counter

class Solution:
    def maxOccurences(self, nums, target, k):
        maxOcc = currOcc = 0

        for num in nums:
            if num == k:
                currOcc -= 1

            if num == target:
                currOcc += 1
            
            if currOcc < 0:
                currOcc = 0

            maxOcc = max(maxOcc, currOcc)
        
        return maxOcc

    def maxFrequency(self, nums: List[int], k: int) -> int:
        counter = Counter(nums)
        maxFreq = float(-inf)

        for key, frq in counter.items():
            maxFreq = max(maxFreq, self.maxOccurences(nums, key, k))
        
        return counter[k] + maxFreq