'''
    board char[][]
    board[r][c] 'X' or 'O'
    a connected group of 'O' surrounded by 'X' need to be flipped to 'X'
    - regions on borders not considered surrounded regions
        - 'O' regions on borders cannot be flipped
            -> bfs starting from those 'O' on borders, spreading to adjancent 'O' cells
                - mark those cells so it won't be flipped
        - rest of 'O' now ensured to be surrounded by 'X' -> flip them
'''

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        q = deque()
        unflip = set()

        rows, cols = len(board), len(board[0])

        # gather 'O' regions on borders
        # left and right borders
        for i in range(rows):
            if board[i][0] == "O":
                q.append((i, 0))
                unflip.add((i, 0))
            if board[i][-1] == "O":
                q.append((i, cols - 1))
                unflip.add((i, cols - 1))

        # top and bottom borders
        for i in range(cols):
            if board[0][i] == "O":
                q.append((0, i))
                unflip.add((0, i))
            if board[-1][i] == "O":
                q.append((rows - 1, i))
                unflip.add((rows - 1, i))

        # bfs
        while q:
            for i in range(len(q)):
                r, c = q.popleft()

                directions = [(-1,0),(0,1),(0,-1),(1,0)]
                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if nr in range(rows) and nc in range(cols) and (nr, nc) not in unflip and board[nr][nc] == 'O':
                        unflip.add((nr, nc))
                        q.append((nr, nc))
        
        for r in range(rows):
            for c in range(cols):
                if (r, c) not in unflip and board[r][c] == 'O':
                    board[r][c] = 'X'
