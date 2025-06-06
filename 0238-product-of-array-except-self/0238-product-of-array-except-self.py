class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        prefix = 1 

        for i, num in enumerate(nums):
            if i > 0:
                prefix *= nums[i - 1]
                res.append(prefix)
            else:
                res.append(prefix)
        
        suffix = 1
        for i in range(len(nums) - 2, -1, -1):
            suffix *= nums[i + 1] 
            res[i] *= suffix

        return res
                