class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        if rows == 1:
            return 0

        min_heap = [(grid[0][0], 0, 0)]
        visit = set([(0,0)])

        while min_heap:
            h, r, c = heapq.heappop(min_heap)

            if r == rows - 1 and c == cols - 1:
                return h

            directions = [(-1,0),(0,-1),(1,0),(0,1)]

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if nr in range(rows) and nc in range(cols) and (nr, nc) not in visit:
                    visit.add((nr, nc))
                    heapq.heappush(min_heap, (max(grid[nr][nc], h), nr, nc))

        return -1

