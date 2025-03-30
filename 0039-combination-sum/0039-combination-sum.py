class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, currPath, total):
            if total == target:
                res.append(currPath.copy())
                return

            if i >= len(candidates) or total > target:
                return
            
            currPath.append(candidates[i])
            dfs(i, currPath, total + candidates[i])
            currPath.pop()
            dfs(i + 1, currPath, total)
        
        dfs(0, [], 0)
        return res