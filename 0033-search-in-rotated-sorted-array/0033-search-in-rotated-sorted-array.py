class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + (r - l) // 2

            if nums[m] == target:
                return m
            
            if nums[m] >= nums[l]: # Left
                if target >= nums[l] and target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else: # Right
                if target <= nums[r] and target > nums[m]:
                    l = m + 1
                else:
                    r = m - 1
        
        return -1