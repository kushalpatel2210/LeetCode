class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        element = nums[0]
        maxDiff = float('-inf')

        for num in nums:
            if num > element:
                maxDiff = max(maxDiff, num - element)
            else:
                element = num
        
        return -1 if maxDiff == float('-inf') else maxDiff