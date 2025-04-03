from collections import defaultdict

class Solution:
    def initialize(self,board): 
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if board[r][c] != ".":
                    self.row[r].add(val)
                    self.col[c].add(val)
                    self.box[(r //3, c // 3)].add(val)
                else:
                    self.empty.append((r,c))

    def solve(self,board,index):
        if index==len(self.empty):
            return True
        i,j=self.empty[index]

        
        for c in "123456789":
            if self.isSafe(i,j,c):
                board[i][j]=c
                self.row[i].add(c)
                self.col[j].add(c)
                self.box[(i // 3, j // 3)].add(c)
                if self.solve(board,index+1):
                    return True
                board[i][j]="."
                self.row[i].remove(c)
                self.col[j].remove(c)
                self.box[(i // 3, j // 3)].remove(c)
        return False
                        
    def isSafe(self,i,j,c):
        if c in self.row[i] or c in self.col[j] or c in self.box[(i // 3, j // 3)]:
            return False
        return True

    def solveSudoku(self, board: List[List[str]]) -> None:
        self.row= defaultdict(set)
        self.col= defaultdict(set)
        self.box= defaultdict(set)
        self.empty=[]
        self.initialize(board)
        self.solve(board,0)