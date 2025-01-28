class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows, cols = len(matrix), len(matrix[0]) 
        self.query_matrix = [[0] * (cols + 1) for _ in range(rows + 1)]

        for row in range(rows):
            prefix = 0
            for col in range(cols):
                prefix += matrix[row][col]
                above = self.query_matrix[row][col + 1]
                self.query_matrix[row + 1][col + 1] = prefix + above


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1, col1, row2, col2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1

        bottom_right = self.query_matrix[row2][col2]
        above  = self.query_matrix[row1 - 1] [col2]
        left = self.query_matrix[row2][col1 - 1]
        top_left = self.query_matrix[row1 - 1][col1 - 1]

        return bottom_right - above - left + top_left


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)