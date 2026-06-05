class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        self.p = set()
        self.a = set()
        self.heights = heights

        self.rows, self.cols = len(heights), len(heights[0])

        for i in range(self.rows):
            self.p.add((i,0))
            self.a.add((i,self.cols-1))
        
        for j in range(self.cols):
            self.p.add((0,j))
            self.a.add((self.rows-1,j))

        self.visit = set()
        for i, j in self.p.copy():
            self.dfs_p(i, j)
        
        self.visit = set()
        for i, j in self.a.copy():
            self.dfs_a(i, j)

        return list(self.p.intersection(self.a))

    def dfs_p(self, i, j):

        self.visit.add((i, j))

        directions = [(-1,0),(0,-1),(1,0),(0,1)]

        for dr, dc in directions:
            cr, cc = i + dr, j + dc
            if cr in range(self.rows) and cc in range(self.cols) and (cr, cc) not in self.visit and self.heights[cr][cc] >= self.heights[i][j]:
                self.p.add((cr, cc))
                self.dfs_p(cr, cc)
    
    def dfs_a(self, i, j):

        self.visit.add((i, j))

        directions = [(-1,0),(0,-1),(1,0),(0,1)]

        for dr, dc in directions:
            cr, cc = i + dr, j + dc
            if cr in range(self.rows) and cc in range(self.cols) and (cr, cc) not in self.visit and self.heights[cr][cc] >= self.heights[i][j]:
                self.a.add((cr, cc))
                self.dfs_a(cr, cc)
        

        