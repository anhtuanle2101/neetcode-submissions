class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    q = deque()
                    q.append((i, j))
                    visit = set()
                    distance = 0
                    while q:
                        for k in range(len(q)):
                            r, c = q.popleft()

                            if r < 0 or c < 0 or r >= rows or c >= cols or (r,c) in visit:
                                continue

                            if grid[r][c] == -1:
                                continue

                            grid[r][c] = min(grid[r][c], distance)
                            visit.add((r, c))

                            directions = [(-1,0),(0,-1),(1,0),(0,1)]
                            
                            for dr, dc in directions:
                                q.append((r + dr, c + dc))

                        distance += 1
