'''
    board char[[]..]
    word string
    - return if word is present in grid

    - path horizontally or vertically
        - horizontally (0, -1) and (0, 1)
        - vertically (-1, 0) and (1, 0)
    - same cell cannot be used more than once -> set to check
    - check each cell in board
        - if board[r][c] == word[0]:
            - start search i start at 0 -> len(word) - 1
                - if i >= len(word):
                    - return False
                - mark this cell as visited
                - check 4 directions horizontally and vertically 
                    - the new cell is valid if 
                        - new cell are in bound [0, rows] and [0, cols]
                        - new cell are not visited (not in set)
                        - new cell are same with next character in word
                    - if yes, 
                        - move forward to this direction, if the direction is ultimately return True -> return True 
                        - backtrack
                return False -> starting from this cell, there is no possible word
                    
'''

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.board = board
        self.word = word

        self.rows, self.cols = len(self.board), len(self.board[0])

        for r in range(self.rows):
            for c in range(self.cols):
                if self.board[r][c] == word[0]:
                    self.visit = set()
                    if self.backtrack(r, c, 0):
                        return True

        return False
    
    def backtrack(self, r, c, i):
        if i >= len(self.word):
            return False

        if i == len(self.word)-1 and self.board[r][c] == self.word[i]:
            return True
        
        self.visit.add((r,c))
        
        directions = [(0,-1), (0,1), (-1,0), (1,0)]

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if nr in range(0, self.rows) and nc in range(0, self.cols) and (nr, nc) not in self.visit and i + 1 < len(self.word) and self.board[nr][nc] == self.word[i + 1]:
                if self.backtrack(nr, nc, i + 1):
                    return True
                self.visit.remove((nr, nc))

        return False
