class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            res[i] *= prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        
        return res

"""
Sol 1: O(n) space
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left, right, res = [1] * len(nums), [1] * len(nums), [1] * len(nums)

        for i in range(1, len(nums)):
            left[i] = nums[i - 1] * left[i - 1]
        
        for i in range(len(nums) - 2, -1, -1):
            right[i] = right[i + 1] * nums[i + 1] 
        
        for i in range(len(nums)):
            res[i] = left[i] * right[i]
        
        return res
"""