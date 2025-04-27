class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uniqueNums = set(nums)
        longestSeq = 0

        for n in uniqueNums:
            if n - 1 not in uniqueNums:
                currSeq = 0
                while n in uniqueNums:
                    currSeq += 1
                    n += 1
                longestSeq = max(longestSeq, currSeq)
        
        return longestSeq