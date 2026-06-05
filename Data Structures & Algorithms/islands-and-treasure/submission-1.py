'''
    grid ints[[]] 
        -1 cannot be traversed
        0 treasure
        INF can be traversed
    4 directions vertically and horizontally
    - fill land cells with distance to closest treasure chest

    - closest -> bfs from the treasure chests 
        grid[r][c] is a new chest
        - as traversing keep track of the distance from the chest, to grid[r][c] update
        to keep the minimum distance to the chest grid[r][c] = min(grid[r][c], cur_distance)

'''


class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        visit = set()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visit.add((r, c))
        
        cur_distance = 0
        while q:
            cur_distance += 1
            for i in range(len(q)):
                r, c = q.popleft()

                directions = [(-1,0),(1,0),(0,1),(0,-1)]
                
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if nr in range(rows) and nc in range(cols) and (nr, nc) not in visit and grid[nr][nc] > 0:
                        grid[nr][nc] = min(grid[nr][nc], cur_distance)
                        visit.add((nr, nc))
                        q.append((nr, nc))
    
                    