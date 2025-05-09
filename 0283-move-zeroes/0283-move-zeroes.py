class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        start = 0

        for i, num in enumerate(nums):
            if num != 0:
                nums[start] = num
                start += 1
        
        while start < len(nums):
            nums[start] = 0
            start += 1
            
