class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        self.m = {}
        self.result = []

        for i in range(numCourses):
            self.m[i] = []
        
        for a, b in prerequisites:
            self.m[a].append(b)
        
        self.visit, self.cycle = set(), set()
        for i in range(numCourses):
            if not self.dfs(i):
                return []

        return self.result

    def dfs(self, i):
        if i in self.cycle:
            return False

        if i in self.visit:
            return True

        self.cycle.add(i)

        for n in self.m[i]:
            if not self.dfs(n):
                return False

        self.cycle.remove(i)
        self.visit.add(i)
        self.result.append(i)

        return True