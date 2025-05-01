# Counting sort
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [0] * 3

        for num in nums:
            count[num] += 1
        
        index = 0
        for i, c in enumerate(count):
            while c > 0:
                nums[index] = i
                index += 1
                c -= 1
