class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(i, currPath, total):
            if total == target:
                res.append(currPath.copy())
                return
            
            if total > target or i >= len(candidates):
                return 
            
            currPath.append(candidates[i]) # append
            backtrack(i, currPath, total + candidates[i]) # explore
            currPath.pop() # pop
            backtrack(i + 1, currPath, total) # explore
        
        backtrack(0, [], 0)

        return res