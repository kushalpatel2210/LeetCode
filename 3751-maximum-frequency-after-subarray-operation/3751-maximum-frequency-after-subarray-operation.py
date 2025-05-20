from collections import defaultdict

class Solution:
    def maxGain(self, nums, targetVal, k):
        maxGain, currGain = 0, 0

        for num in nums:
            if num == k:
                currGain -= 1
            
            if num == targetVal:
                currGain += 1
            
            if currGain < 0:
                currGain = 0    
            
            maxGain = max(maxGain, currGain)

        return maxGain

    def maxFrequency(self, nums: List[int], k: int) -> int:
        hashMap = defaultdict(int)
        maxFrequency = float('-inf')

        for num in nums:
            hashMap[num] += 1
        
        for num, frq in hashMap.items():
            maxFrequency = max(maxFrequency, self.maxGain(nums, num, k))

        return hashMap[k] + maxFrequency