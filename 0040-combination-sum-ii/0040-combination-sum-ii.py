class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def dfs(i, currPath, total):
            if total == target:
                res.append(currPath.copy())
                return 
            
            if total > target or i >= len(candidates):
                return 
            
            currElement = candidates[i]
            currPath.append(currElement)
            dfs(i + 1, currPath, total + currElement)
            currPath.pop()

            while i < len(candidates) and candidates[i] == currElement:
                i += 1
            
            dfs(i, currPath, total)
        
        dfs(0, [], 0)
    
        return res