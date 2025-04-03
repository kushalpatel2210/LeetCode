class Solution:
    def initialize(self,board):
        
        for i in range(9):
            for j in range(9):
                if board[i][j]!=".":
                    self.row[i].add(board[i][j])
                    self.col[j].add(board[i][j])
                    self.box[(i//3)*3+(j//3)].add(board[i][j])
                else:
                    self.empty.append((i,j))
    def solve(self,board,index):
        if index==len(self.empty):
            return True
        i,j=self.empty[index]

        
        for c in "123456789":
            if self.isSafe(i,j,c):
                board[i][j]=c
                self.row[i].add(c)
                self.col[j].add(c)
                self.box[(i//3)*3+(j//3)].add(c)
                if self.solve(board,index+1):
                    return True
                board[i][j]="."
                self.row[i].remove(c)
                self.col[j].remove(c)
                self.box[(i//3)*3+(j//3)].remove(c)
        return False
                        
    def isSafe(self,i,j,c):
        if c in self.row[i] or c in self.col[j] or c in self.box[(i//3)*3+(j//3)]:
            return False
        return True
    def solveSudoku(self, board: List[List[str]]) -> None:
        self.row=[set() for _ in range(9)]
        self.col=[set() for _ in range(9)]
        self.box=[set() for _ in range(9)]
        self.empty=[]
        self.initialize(board)
        self.solve(board,0)