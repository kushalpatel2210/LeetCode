class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r = len(matrix)
        c = len(matrix[0])
        rows, cols = set(), set() # Rows and Cols that has zero value
        
        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)
        
        for i in range(r):
            for j in range(c):
                if i in rows or j in cols:
                    matrix[i][j] = 0
        