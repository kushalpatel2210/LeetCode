class Solution:
    def jump(self, nums: List[int]) -> int:
        l = r = res = 0

        while r < len(nums) - 1: # len(nums) - 1 is the target
            farthest = 0
            for i in range(l, r + 1): # l to r because the last element in the range is not inclusive
                farthest = max(farthest, i + nums[i])
            l = r + 1
            r = farthest
            res += 1
        
        return res