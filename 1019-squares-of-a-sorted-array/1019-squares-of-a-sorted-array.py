class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        sqNums = [0] * len(nums)
        l, r = 0, len(nums) - 1
        idx = len(nums) - 1

        while l <= r:
            if abs(nums[l]) > abs(nums[r]):
                sqNums[idx] = nums[l] ** 2
                l += 1
            else:
                sqNums[idx] = nums[r] ** 2
                r -= 1
            
            idx -= 1
        
        return sqNums