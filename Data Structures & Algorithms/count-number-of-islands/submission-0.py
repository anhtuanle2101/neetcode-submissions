class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.rows, self.cols = len(grid), len(grid[0])
        self.visit = set()
        self.result = 0
        self.grid = grid

        for i in range(self.rows):
            for j in range(self.cols):
                if (i, j) not in self.visit and grid[i][j] == "1":
                    self.result += 1
                    self.dfs(i, j)

        return self.result

    def dfs(self, i, j):
        if i < 0 or j < 0 or i >= self.rows or j >= self.cols or (i, j) in self.visit or self.grid[i][j] == "0":
            return

        self.visit.add((i, j))
        
        directions = [(-1,0),(0,-1),(1,0),(0,1)]

        for dr, dc in directions:
            self.dfs(i + dr, j + dc)