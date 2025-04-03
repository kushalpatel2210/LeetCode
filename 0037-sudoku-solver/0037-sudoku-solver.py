from collections import defaultdict

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.board = board
        self.rows = defaultdict(set)
        self.cols = defaultdict(set)
        self.squares = defaultdict(set)
        self.empty = [] # (row, col) with empty spaces
        self.initialize()
        self.solve(0)

    def initialize(self):
        for r in range(9):
            for c in range(9):
                num = self.board[r][c]

                if num != '.':
                    self.rows[r].add(num)
                    self.cols[c].add(num)
                    self.squares[(r // 3, c // 3)].add(num)
                else:
                    self.empty.append((r, c))

    def solve(self, index):
        if index == len(self.empty):
            return True
        
        r, c = self.empty[index]

        for num in '123456789':
            if self.isValid(r, c, num):
                self.add(r, c, num)
                if self.solve(index + 1):
                    return True
                self.remove(r, c, num)

        return False
    
    def add(self, r, c, num):
        self.board[r][c] = num
        self.rows[r].add(num)
        self.cols[c].add(num)
        self.squares[(r // 3, c // 3)].add(num)
    
    def remove(self, r, c, num):
        self.board[r][c] = '.'
        self.rows[r].remove(num)
        self.cols[c].remove(num)
        self.squares[(r // 3, c // 3)].remove(num)

    def isValid(self, r, c, num):
        if num in self.rows[r] or num in self.cols[c] or num in self.squares[(r // 3, c // 3)]:
            return False
        return True
