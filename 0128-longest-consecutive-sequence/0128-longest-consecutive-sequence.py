class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uniqueNums = set(nums)
        longest = 0

        for num in uniqueNums:
            if num - 1 not in uniqueNums:
                currLength = 0

                while num in uniqueNums:
                    currLength += 1
                    num += 1
                
                longest = max(longest, currLength)
        
        return longest