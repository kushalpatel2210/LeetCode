class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ptr = 0

        for num in nums:
            if num != val:
                nums[ptr] = num
                ptr += 1
        
        return ptr