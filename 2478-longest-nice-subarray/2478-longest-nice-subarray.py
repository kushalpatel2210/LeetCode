class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        i = 0
        bitmask = 0 
        maxWindow = float("-inf")

        for j in range(len(nums)):
            while (bitmask & nums[j]) != 0: # shrink window
                bitmask ^= nums[i]
                i += 1
            
            maxWindow = max(maxWindow, j - i + 1)
            bitmask |= nums[j] # expand window
            
        return maxWindow