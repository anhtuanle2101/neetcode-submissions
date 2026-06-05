class Solution:
    def solve(self, board: List[List[str]]) -> None:
        self.board = board
        self.rows, self.cols = len(board), len(board[0])

        self.b = set()

        for i in range(1, self.rows-1):
            if self.board[i][0] == "O":
                self.b.add((i, 0))
            if self.board[i][self.cols-1] == "O":
                self.b.add((i, self.cols-1))
        for j in range(1, self.cols-1):
            if self.board[0][j] == "O":
                self.b.add((0, j))
            if self.board[self.rows-1][j] == "O":
                self.b.add((self.rows-1, j))
        print(self.b)
        self.c = set()   
        self.visit = set()     
        for i, j in self.b:
            self.dfs(i, j)
        print(self.c)
        for i in range(1, self.rows-1):
            for j in range(1, self.cols-1):
                if (i, j) not in self.c and board[i][j] == "O":
                    board[i][j] = "X"

    def dfs(self, i, j):
        self.visit.add((i, j))

        directions = [(-1,0),(0,-1),(1,0),(0,1)]

        for dr, dc in directions:
            cr, cc = i + dr, j + dc
            if cr in range(1, self.rows-1) and cc in range(1, self.cols-1) and (cr, cc) not in self.visit and self.board[cr][cc] == "O":
                self.c.add((cr, cc))
                self.dfs(cr, cc)
    
