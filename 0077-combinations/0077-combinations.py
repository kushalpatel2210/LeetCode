class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def backtrack(start, currPath):
            if len(currPath) == k:
                res.append(currPath.copy())
                return
            
            for i in range(start, n + 1):
                currPath.append(i)
                backtrack(i + 1, currPath)
                currPath.pop()
        
        backtrack(1, [])

        return res
