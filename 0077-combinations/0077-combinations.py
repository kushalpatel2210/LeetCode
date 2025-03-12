class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def backtrack(i, currPath):
            if len(currPath) == k:
                res.append(currPath.copy())
                return
            
            for j in range(i, n + 1):
                currPath.append(j)
                backtrack(j + 1, currPath)
                currPath.pop()
        
        backtrack(1, [])

        return res
