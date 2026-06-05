class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        self.adj_list = {i:[] for i in range(n)}

        for a, b in edges:
            self.adj_list[a].append(b)
            self.adj_list[b].append(a)

        self.count = 0
        self.visit = set()

        for i in range(n):
            if i not in self.visit:
                self.count += 1
                self.dfs(i, None)

        return self.count

    def dfs(self, i, prev):
        if i in self.visit:
            return

        self.visit.add(i)

        for n in self.adj_list[i]:
            if n == prev:
                continue
            self.dfs(n, i)