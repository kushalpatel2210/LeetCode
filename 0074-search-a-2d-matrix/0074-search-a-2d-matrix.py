class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        l, r = 0, rows * cols - 1

        while l <= r:
            m = l + (r - l) // 2
            row, col = m // cols, m % cols

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                r = m - 1
            else:
                l = m + 1
        
        return False

'''
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        l, r = 0, rows - 1

        while l <= r:
            mid = l + (r - l) // 2
            cols = len(matrix[mid])
            
            if target >= matrix[mid][0] and target <= matrix[mid][cols - 1]:
                insidel, insider = 0, cols - 1

                while insidel <= insider:
                    rowMiddle = insidel + (insider - insidel) // 2

                    if matrix[mid][rowMiddle] == target:
                        return True
                    elif matrix[mid][rowMiddle] > target:
                        insider = rowMiddle - 1
                    else:
                        insidel = rowMiddle + 1
                
                return False
            elif target > matrix[mid][cols - 1]:
                l = mid + 1
            else:
                r = mid - 1

        return False
'''