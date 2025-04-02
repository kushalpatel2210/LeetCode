class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(i, currPath, currSum):
            if currSum == target:
                res.append(currPath.copy())
                return
            
            if currSum > target or i >= len(candidates):
                return 
            
            currPath.append(candidates[i])
            backtrack(i, currPath, currSum + candidates[i])
            currPath.pop()
            backtrack(i + 1, currPath, currSum)

        backtrack(0, [], 0)

        return res