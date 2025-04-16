class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0

        for num in nums:
            currentNum = num
            count = 1
            if currentNum + 1 in nums:
                continue
            while currentNum - 1 in nums:
                currentNum -= 1
                count += 1
            
            longest = max(count, longest)
        
        return longest