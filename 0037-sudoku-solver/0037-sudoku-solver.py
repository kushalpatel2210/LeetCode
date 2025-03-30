EMPTY_CELL = "."

class SudokuBoard:
    def __init__(self, board: list[list[str]]):
        self.board = board

        self._row_used = defaultdict(set)
        self._col_used = defaultdict(set)
        self._box_used = defaultdict(set)

        for i in range(len(board)):
            for j in range(len(board[i])):
                if (num := board[i][j]) != EMPTY_CELL:
                    self._row_used[i].add(num)
                    self._col_used[j].add(num)
                    self._box_used[i // 3, j // 3].add(num)

    def add(self, i: int, j: int, num: str) -> None:
        self.board[i][j] = num
        self._row_used[i].add(num)
        self._col_used[j].add(num)
        self._box_used[i // 3, j // 3].add(num)

    def remove(self, i: int, j: int) -> None:
        num = self.board[i][j]
        self.board[i][j] = EMPTY_CELL
        self._row_used[i].remove(num)
        self._col_used[j].remove(num)
        self._box_used[i // 3, j // 3].remove(num)

    def empty_cells(self) -> list[tuple[int, int, int]]:
        empty_cells = []
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == EMPTY_CELL:
                    heapq.heappush(empty_cells, (len(self.candidates(i, j)), i, j))
        return empty_cells

    def candidates(self, i: int, j: int) -> set[str]:
        candidates = set(str(num) for num in range(1, 10)) - (
            self._row_used[i] | self._col_used[j] | self._box_used[i // 3, j // 3]
        )
        return candidates


def solve_sudoku(board: SudokuBoard) -> bool:
    if not (empty_cells := board.empty_cells()):
        return True

    _, row, col = empty_cells[0]
    candidates = board.candidates(row, col)
    for candidate in candidates:
        board.add(row, col, candidate)
        if solve_sudoku(board):
            return True
        board.remove(row, col)
    return False


class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        solve_sudoku(SudokuBoard(board))
        