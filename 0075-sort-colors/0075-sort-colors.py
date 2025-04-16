class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Counting sort
        count = [0] * 3
        for num in nums:
            count[num] += 1
        
        index = 0
        for i in range(3):
            while count[i]:
                nums[index] = i
                count[i] -= 1
                index += 1


'''
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ptrVal = 0
        i = 0

        while i < len(nums) and ptrVal < 3:
            currVal = nums[i]
            j = i + 1
            
            if nums[i] == ptrVal:
                i += 1
            
            while j < len(nums) - 1 and nums[j] != ptrVal:
                j += 1
            
            if j < len(nums) and nums[j] == ptrVal:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                ptrVal += 1
                continue
            i += 1
'''