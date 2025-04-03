class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrack(i, currPath, total):
            if total == target:
                res.append(currPath.copy())
                return
            
            if total > target or i >= len(candidates):
                return
            
            currElement = candidates[i]
            currPath.append(currElement) # append
            backtrack(i + 1, currPath, total + currElement) # expand
            currPath.pop() # pop
            
            # do not process the same element
            while i < len(candidates) and candidates[i] == currElement:
                i += 1
            # explore
            backtrack(i, currPath, total)

        backtrack(0, [], 0)

        return res