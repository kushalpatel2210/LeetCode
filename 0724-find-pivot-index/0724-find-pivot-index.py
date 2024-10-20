class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefixSum = 0
        totalSum = sum(nums)

        for i in range(len(nums)):
            rightSum = totalSum - prefixSum - nums[i]
            if prefixSum == rightSum:
                return i
            prefixSum += nums[i]
        
        return -1