class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.board = board
        self.rows, self.cols = len(self.board), len(self.board[0])
        self.word = word
        self.cur = ""

        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j] == self.word[0]:
                    self.visit = set()
                    self.cur = ""
                    if self.dfs(i, j, 0):
                        return True

        return False

    def dfs(self, i, j, cur_i):
        if i < 0 or j < 0 or i >= self.rows or j >= self.cols or (i,j) in self.visit:
            return False
        
        if self.board[i][j] != self.word[cur_i]:
            return False

        if cur_i == len(self.word) - 1:
            return True
        
        self.cur += self.board[i][j]
        self.visit.add((i, j))

        if self.dfs(i - 1, j, cur_i + 1) or self.dfs(i + 1, j, cur_i + 1) or self.dfs(i, j - 1, cur_i + 1) or self.dfs(i, j + 1, cur_i + 1):
            return True

        self.visit.remove((i, j))

        return False

            
