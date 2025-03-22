class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * len(nums)
        endPointer = n - 1
        l, r = 0, n - 1

        while l <= r:
            if abs(nums[l]) > abs(nums[r]):
                res[endPointer] = nums[l] ** 2
                l += 1
            else:
                res[endPointer] = nums[r] ** 2
                r -= 1
            endPointer -= 1
        
        return res
