class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l, r = 0, 0

        while r < len(nums):
            nums[l] = nums[r]
            
            while r < len(nums) and nums[l] == nums[r]:
                r += 1
            
            l += 1
        
        return l

'''
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
'''