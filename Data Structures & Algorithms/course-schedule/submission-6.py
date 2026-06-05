'''
    prerequisites [a,b][]
    [a,b] -> b is prerequisite of a, must take b first before take a
    numCourses number of courses required to take
    -> return whether we can finish all courses
    
    - adj list
        - for a,b in prerequisites:
            adj_list[a].append(b) # edge from a to b
    - use bfs at each course
        - has a set called path to track which course we are exploring this path
        - dfs at course ith
            - if the course has been visited in the same path
                => cycle detection
                    return False
            - if the course has been visited before 
                stop here
            - mark the course as visited in visit and path
            - going through its prerequisites
                - add it to the queue to continue exploring
            - release the course in path set
    
    return True

'''

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = {i:[] for i in range(numCourses)}
        for a,b in prerequisites:
            adj_list[a].append(b)
        visit = set()

        def dfs(crs, visit, path):
            if crs in path:
                return False
            
            if crs in visit:
                return True

            visit.add(crs)
            path.add(crs)

            for p in adj_list[crs]:
                if not dfs(p, visit, path):
                    return False
            path.remove(crs)

            return True
            
        for crs in range(numCourses):
            path = set()
            if not dfs(crs, visit, path):
                return False

        return True