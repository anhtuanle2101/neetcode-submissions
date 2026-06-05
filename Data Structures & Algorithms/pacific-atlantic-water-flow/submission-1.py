'''
    heights int[][] 
    Pacific top + left
    Atlantic bot + right

    water flow from height h1 to h2 where h1 >= h2
    - find all cells can flow from Pacific, 
        starting from top and left cells, bfs from those cells
        - h can be flowed from h' if h <= h'
        - h' is adjacent cells' height vertically and horizontally
    - similarly, find all cells can flow from Atlantic
    - find intersection between two lists -> all the cells can flow to both oceans
'''

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        board = heights
        q = deque()
        pac, atl = set(), set()

        # pacific
        # top and left cells into the q
        for i in range(rows):
            q.append((i, 0))
            pac.add((i, 0))
        for i in range(cols):
            q.append((0, i))
            pac.add((0, i))

        directions = [(-1,0),(0,-1),(1,0),(0,1)]
        # bfs
        while q:
            for i in range(len(q)):
                r, c = q.popleft()

                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if nr in range(rows) and nc in range(cols) and board[r][c] <= board[nr][nc] and (nr,nc) not in pac:
                        pac.add((nr, nc))
                        q.append((nr, nc))
        #atlantic
        q = deque()
        for i in range(rows):
            q.append((i, cols - 1))
            atl.add((i, cols - 1))
        for i in range(cols):
            q.append((rows - 1, i))
            atl.add((rows - 1, i))
        # bfs
        while q:
            for i in range(len(q)):
                r, c = q.popleft()

                for dr, dc in directions:
                    nr, nc = r+dr, c+dc
                    if nr in range(rows) and nc in range(cols) and board[r][c] <= board[nr][nc] and (nr,nc) not in atl:
                        atl.add((nr, nc))
                        q.append((nr, nc))
        
        res = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pac and (r, c) in atl:
                    res.append((r, c))

        return res
                