class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        This function solves a Sudoku puzzle using Depth First Search (DFS).
        The given board is modified in-place to fill in the Sudoku solution.
        """

        def dfs(position: int):
            # Base case: if all empty positions are filled, set completion flag to True
            if position == len(empty_positions):
                self.is_solved = True
                return
          
            # Get the next position from the list of empty positions
            row_index, col_index = empty_positions[position]

            # Try placing all possible values (1-9) in the current empty cell
            for value in range(9):
                if (not rows_used[row_index][value] and 
                        not cols_used[col_index][value] and 
                        not blocks_used[row_index // 3][col_index // 3][value]):
                  
                    # Mark the value as used in the row, column, and 3x3 block
                    rows_used[row_index][value] = cols_used[col_index][value] = blocks_used[row_index // 3][col_index // 3][value] = True
                    board[row_index][col_index] = str(value + 1)

                    # Recursively try to solve the rest of the puzzle
                    dfs(position + 1)

                    # Undo the move if it didn't lead to a solution
                    rows_used[row_index][value] = cols_used[col_index][value] = blocks_used[row_index // 3][col_index // 3][value] = False

                # If puzzle is solved, exit early
                if self.is_solved:
                    return

        # Initialize tracking for used numbers in each row, column and block
        rows_used = [[False] * 9 for _ in range(9)]
        cols_used = [[False] * 9 for _ in range(9)]
        blocks_used = [[[False] * 9 for _a in range(3)] for _b in range(3)]

        empty_positions = []  # List to track the positions of empty cells
        self.is_solved = False  # Flag to indicate when the puzzle is solved

        # Process the Sudoku board to fill tracking structures and find empty cells
        for row in range(9):
            for col in range(9):
                if board[row][col] == '.':
                    # Save the position of the empty cell
                    empty_positions.append((row, col))
                else:
                    # Mark the value as used in the row, column, and block
                    value = int(board[row][col]) - 1
                    rows_used[row][value] = cols_used[col][value] = blocks_used[row // 3][col // 3][value] = True

        # Start the recursive DFS to solve the Sudoku
        dfs(0)