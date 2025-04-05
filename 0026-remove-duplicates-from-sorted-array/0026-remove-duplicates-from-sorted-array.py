class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        start = 0
        element = float('-inf')

        for i in range(len(nums)): 
            if nums[i] != element:
                element = nums[i]
                nums[start] = element
                start += 1
        
        return start