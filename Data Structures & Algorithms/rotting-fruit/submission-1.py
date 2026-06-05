class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        q = deque()
        fresh = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    q.append((i, j))

        time = 0

        while fresh > 0 and q:
            for i in range(len(q)):
                r, c = q.popleft()

                directions = [(-1,0),(0,-1),(1,0),(0,1)]

                for dr, dc in directions:
                    cr, cc = r + dr, c + dc
                    # valid and fresh
                    if cr in range(rows) and cc in range(cols) and grid[cr][cc] == 1:
                        grid[cr][cc] = 2
                        q.append((cr, cc))
                        fresh -= 1
            time += 1

        return time if fresh == 0 else -1

