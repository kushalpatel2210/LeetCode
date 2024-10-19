class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        start = 0

        for num in nums:
            if num != 0:
                nums[start] = num
                start += 1
        
        while start < len(nums):
            nums[start] = 0
            start += 1

        """
        # High run time
        start = 0

        while start < len(nums):
            if nums[start] != 0:
                start += 1
            else: 
                end = start
                while nums[end] == 0 and end < len(nums):
                    if end == len(nums) - 1:
                        break
                    end += 1
                nums[start] = nums[end]
                nums[end] = 0
                start += 1
        """