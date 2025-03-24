class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 0

        for num in nums:
            if l < 2 or num != nums[l - 2]:
                nums[l] = num
                l += 1
                
        return l