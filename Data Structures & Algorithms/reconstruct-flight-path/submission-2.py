class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        self.adj_list = {s:[] for s, d in tickets}
        self.tickets = tickets
        for s, d in tickets:
            if s in self.adj_list:
                self.adj_list[s].append(d)
            else:
                self.adj_list[s] = []
        
        for k in self.adj_list:
            self.adj_list[k].sort()

        self.result = ["JFK"]
        self.visit = set()
        self.count = 0
        self.dfs("JFK")

        return self.result

    def dfs(self, a):
        if len(self.result) == len(self.tickets) + 1:
            return True
        if a not in self.adj_list:
            return False

        tmp = list(self.adj_list[a])
        for i, v in enumerate(tmp):
            if (i, v) not in self.visit:
                self.adj_list[a].pop(i)
                self.result.append(v)

                if self.dfs(v): return True

                self.adj_list[a].insert(i, v)
                self.result.pop()
        
        return False


