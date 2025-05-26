class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uniqueNums = set(nums)
        lcs = float('-inf')

        for num in uniqueNums:
            if num - 1 in uniqueNums:
                continue
            
            res = 0
            while num in uniqueNums:
                res += 1
                num += 1
            lcs = max(lcs, res)
        
        return lcs if lcs != float('-inf') else 0