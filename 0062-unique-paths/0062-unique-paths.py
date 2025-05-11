class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = dict()
        memo[(0, 0)] = 1

        def backtrack(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            else:
                if i < 0 or j < 0 or i >= m or j >= n:
                    return 0
                else:
                    memo[(i, j)] = backtrack(i - 1, j) + backtrack(i, j - 1)
                    return memo[(i, j)]
        
        return backtrack(m - 1, n - 1)
