class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        totalSum = sum(nums)
        res = -1
        leftSum = 0

        for i in range(len(nums)):
            leftSum += 0 if i == 0 else nums[i - 1]
            rightSum = totalSum - leftSum - nums[i] if i < len(nums) - 1 else 0

            if leftSum == rightSum:
                return i

        return res

