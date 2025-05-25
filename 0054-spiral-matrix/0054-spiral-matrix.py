class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)
        res = []

        while left < right and top < bottom:
            # left to right in top row 
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1

            # top to down for last col 
            for i in range(top, bottom):
                res.append(matrix[i][right - 1])
            right -= 1

            if not (top < bottom and left < right):
                break

            # right to left for last row 
            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][i])
            bottom -= 1

            # down to up for the first col
            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])
            left += 1
        

        return res
