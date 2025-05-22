class Solution:
    def binarySearch(self, nums, target, leftBias):
        i = -1 
        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + (r - l) // 2
            
            if nums[m] == target:
                i = m
                if leftBias:
                    r = m - 1
                else:
                    l = m + 1
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        
        return i

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        leftMost = self.binarySearch(nums, target, True)
        rightMost = self.binarySearch(nums, target, False)
    
        return [leftMost, rightMost]