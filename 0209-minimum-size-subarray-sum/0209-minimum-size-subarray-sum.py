class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        maxSum = 0
        minSubSize = float('inf')

        for r in range(len(nums)):
            maxSum += nums[r]
            while maxSum >= target:
                minSubSize = min(minSubSize, r - l + 1)
                maxSum -= nums[l]
                l += 1
        
        return 0 if minSubSize == float('inf') else minSubSize