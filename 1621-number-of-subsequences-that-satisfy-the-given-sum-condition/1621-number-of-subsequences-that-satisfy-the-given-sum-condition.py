class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = 0
        mod = 10**9 + 7

        r = len(nums) -1 
        for i, left in enumerate(nums):
            while r >= i and left + nums[r] > target:
                r -= 1
            if r >= i:
                res += 2**(r-i)
        
        return res % mod


'''
# BRUTE FORCE
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        subsequences = list()
        res = 0

        def backtrack(index, currPath):
            if index >= len(nums):
                subsequences.append(currPath.copy())
                return 
            
            currPath.append(nums[index]) # include
            backtrack(index + 1, currPath) # explore
            currPath.pop() # does not include
            backtrack(index + 1, currPath)
        
        backtrack(0, [])
        
        for seq in subsequences:
            if seq and min(seq) + max(seq) <= target:
                res += 1

        return res
'''