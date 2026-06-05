'''
    prerequisites [a,b][]
    [a,b] there is an edge from a to b
    adj_list -> adj_list[a] = [...] all adjacent nodes to a
        - for a, b in prerequisites:
            adj_list[a].append(b)
    - topological sort
        - dfs at every course and keep track of all visited in both global and path
            - if the course seen in the path
                -> cycle detection -> return False
            - if the course seen in visit:
                -> nothing to do here return -> True to move on
            - add cur course into visit and path
            - keep exploring the adj courses
                dfs(p, visit, path)
            - after all adj nodes are explored (all p are completed)
                -> add the course to the res list
            - release the course from the current path
            - return True to move on
'''

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        visit = set()
        adj_list = {crs: [] for crs in range(numCourses)}

        for crs, pre in prerequisites:
            adj_list[crs].append(pre)

        res = []
        def dfs(crs, visit, path):
            if crs in path:
                return False
            if crs in visit:
                return True

            path.add(crs)
            visit.add(crs)

            for p in adj_list[crs]:
                if not dfs(p, visit, path):
                    return False

            res.append(crs)
            path.remove(crs)

            return True
        
        for crs in range(numCourses):
            path = set()
            if not dfs(crs, visit, path):
                return []

        return res