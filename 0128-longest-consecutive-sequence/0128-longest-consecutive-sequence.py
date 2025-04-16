class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique_nums = set(nums)
        longest = 0

        for num in unique_nums:
            currentNum = num
            count = 1
            if currentNum + 1 in unique_nums:
                continue
            while currentNum - 1 in unique_nums:
                currentNum -= 1
                count += 1
            
            longest = max(count, longest)
        
        return longest