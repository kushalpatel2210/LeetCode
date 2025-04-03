from collections import defaultdict

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        self.board = board
        self.row= defaultdict(set)
        self.col= defaultdict(set)
        self.box= defaultdict(set)
        self.empty=[]
        self.initialize()
        self.solve(0)

    def initialize(self): 
        for r in range(9):
            for c in range(9):
                val = self.board[r][c]
                if val != ".":
                    self.row[r].add(val)
                    self.col[c].add(val)
                    self.box[(r //3, c // 3)].add(val)
                else:
                    self.empty.append((r,c))
    
    def add(self, r, c, val):
        self.board[r][c] = val
        self.row[r].add(val)
        self.col[c].add(val)
        self.box[(r // 3, c // 3)].add(val)
    
    def remove(self, r, c, val):
        self.board[r][c] = '.'
        self.row[r].remove(val)
        self.col[c].remove(val)
        self.box[(r // 3, c // 3)].remove(val)

    def solve(self, index):
        if index == len(self.empty):
            return True
        
        r, c = self.empty[index]

        for val in "123456789":
            if self.isSafe(r, c, val):
                self.add(r, c, val)
                if self.solve(index + 1):
                    return True
                self.remove(r, c, val)
        return False
                        
    def isSafe(self,r,c,val):
        if val in self.row[r] or val in self.col[c] or val in self.box[(r // 3, c // 3)]:
            return False
        return True