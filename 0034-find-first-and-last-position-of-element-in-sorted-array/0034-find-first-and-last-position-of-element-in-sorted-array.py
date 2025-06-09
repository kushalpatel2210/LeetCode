class Solution:
    def binarySearch(self, nums, target, leftBiased):
        res = -1
        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + (r - l) // 2

            if nums[m] == target:
                res = m
                if leftBiased:
                    r = m -1
                else:
                    l = m + 1
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1
        
        return res

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        leftMost = self.binarySearch(nums, target, True)
        rightMost = self.binarySearch(nums, target, False)

        return [leftMost, rightMost]