class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #dfs
        self.m = {}
        for i in range(numCourses):
            self.m[i] = []

        for a, b in prerequisites:
            self.m[a].append(b)
        
        self.visit = set()
        for i in range(numCourses):
            if not self.dfs(i):
                return False

        return True

    def dfs(self, i):
        if i in self.visit:
            return False
        if len(self.m[i]) == 0:
            return True

        self.visit.add(i)
        
        for n in self.m[i]:
            if not self.dfs(n):
                return False
        
        self.visit.remove(i)
        
        return True

    

    