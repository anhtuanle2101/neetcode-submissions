class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        self.p = {i:i for i in range(1, len(edges) + 1)}
        self.rank = {i:0 for i in range(1, len(edges) + 1)}

        for a, b in edges:
            if not self.union(a, b):
                return [a, b]

    def find_root(self, n):
        parent = self.p[n]

        while parent != self.p[parent]:
            self.p[parent] = self.p[self.p[parent]]
            parent = self.p[parent]

        return parent
    
    def union(self, n1, n2):
        r1, r2 = self.find_root(n1), self.find_root(n2)

        if r1 == r2:
            return False

        if self.rank[r1] > self.rank[r2]:
            self.p[r2] = r1
            self.rank[r1] += self.rank[r2]
        else:
            self.p[r1] = r2
            self.rank[r2] += self.rank[r1]
       
        return True

    
    

        