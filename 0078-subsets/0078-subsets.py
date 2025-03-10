class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(currentPath, index):
            res.append(currentPath.copy())

            for i in range(index, len(nums)):
                currentPath.append(nums[i]) #include
                backtrack(currentPath, i + 1) # explore
                currentPath.pop() # exclude
        
        backtrack([], 0)
        return res


'''
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            # include the number
            subset.append(nums[i])
            dfs(i + 1)
            # does not include the number
            subset.pop()
            dfs(i + 1)
        
        dfs(0)
        return res
'''