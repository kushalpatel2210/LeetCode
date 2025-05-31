class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l, r = 0, 0
        window = float('-inf')

        while r < len(nums):
            if nums[r] == 0:
                k -= 1
            
            while k < 0:
                k += 1 if nums[l] == 0 else 0
                l += 1

            window = max(window, r - l + 1)
            r += 1
        
        return window