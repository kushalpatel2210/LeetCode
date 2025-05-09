class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        start = 0

        while start < len(nums):
            if nums[start] != 0:
                start += 1
            else:
                curr = start + 1
                while curr < len(nums) and nums[curr] == 0:
                    curr += 1
                if curr != len(nums):
                    nums[start] = nums[curr]
                    nums[curr] = 0  
                start += 1
            
