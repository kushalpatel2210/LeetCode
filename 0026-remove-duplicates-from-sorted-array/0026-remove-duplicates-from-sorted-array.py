class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ptr = 1 
        curr = nums[0]

        for num in nums:
            if num != curr:
                nums[ptr] = num
                curr = num
                ptr += 1
    
        return ptr