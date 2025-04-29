class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        maxElement = max(nums)
        maxCount = 0
        count = 0
        left = 0

        for right in range(len(nums)):
            if nums[right] == maxElement:
                maxCount += 1
            
            while maxCount >= k:
                count += len(nums) - right
                if nums[left] == maxElement:
                    maxCount -= 1
                left += 1
        
        return count