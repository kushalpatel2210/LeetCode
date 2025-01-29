class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique_nums = set(nums)
        longest = 0

        for num in unique_nums:
            if num - 1 not in unique_nums:
                current_length = 1
                current_num = num + 1
                while current_num in unique_nums:
                    current_length += 1
                    current_num += 1
                longest = max(longest, current_length)
        
        return longest