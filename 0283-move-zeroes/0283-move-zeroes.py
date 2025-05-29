class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        start = i = 0

        while i < len(nums):
            if nums[i] != 0:
                nums[start] = nums[i]
                start += 1
            i += 1
        
        for j in range(start, len(nums)):
            nums[j] = 0