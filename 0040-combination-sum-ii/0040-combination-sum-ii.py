class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def dfs(i, currPath, currSum):
            if currSum == target:
                res.append(currPath.copy())
                return
            if i >= len(candidates) or currSum > target:
                return
            
            currElement = candidates[i]
            currPath.append(currElement)
            dfs(i + 1, currPath, currSum + currElement)
            currPath.pop()

            while i < len(candidates) and candidates[i] == currElement:
                i += 1

            dfs(i, currPath, currSum)
        
        dfs(0, [], 0)

        return res