class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        self.adj_list = { i:[] for i in range(n) }

        for a, b in edges:
            self.adj_list[a].append(b)
            self.adj_list[b].append(a)

        for i in range(n):
            self.visit = set()
            if self.dfs(i, None) and len(self.visit) == n:
                return True

        return False
    
    def dfs(self, cur, prev):
        if cur in self.visit:
            return False

        self.visit.add(cur)

        for n in self.adj_list[cur]:
            if prev == n:
                continue
            if not self.dfs(n, cur):
                return False


        return True    