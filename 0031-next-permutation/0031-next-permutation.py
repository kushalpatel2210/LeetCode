class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)

        pivot = -1
        for i in range(length - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                pivot = i
                break
        
        if pivot != -1:
            for j in range(length -1, pivot, -1):
                if nums[j] > nums[pivot]:
                    nums[pivot], nums[j] = nums[j], nums[pivot]
                    break
        
        nums[pivot + 1:] = reversed(nums[pivot + 1:])