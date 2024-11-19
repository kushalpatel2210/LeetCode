class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique_elements = set()
        ans = 0

        for num in nums: 
            unique_elements.add(num)
        
        for i in range(len(nums)):
            # starting position
            if nums[i] - 1 not in unique_elements:
                j = nums[i]
                while j in unique_elements:
                    j += 1
                ans = max(ans, j - nums[i])

        return ans