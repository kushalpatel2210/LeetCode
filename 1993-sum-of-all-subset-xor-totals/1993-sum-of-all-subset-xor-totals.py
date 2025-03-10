class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def dfs(i, total):
            if i == len(nums):
                return total
            return dfs(i + 1, total ^ nums[i]) + dfs(i + 1, total)

        return dfs(0, 0)
        
'''
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        sumOfXor = 0

        def backtrack(currPath, index):
            nonlocal sumOfXor
            
            res = 0
            for num in currPath:
                res ^= num
            sumOfXor += res
            
            for i in range(index, len(nums)):
                currPath.append(nums[i]) # include
                backtrack(currPath, i + 1) # explore 
                currPath.pop() # exclude
        
        backtrack([], 0)
        return sumOfXor
'''