class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = zeroCount = maxCount = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zeroCount += 1
            
            while zeroCount > 1:
                if nums[left] == 0:
                    zeroCount -= 1
                
                left += 1

            maxCount = max(maxCount, right - left)
        
        return maxCount
