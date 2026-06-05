"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

'''
    - deep copy of a connected undirected graph
    - use a hash map to map each original node to the copy node
    - create the copy node for the provided root node (input node with value = 1)
    - bfs or dfs starting from copy node
        - looking at all neighbors
            - if the neighbor node exists
                - if not in the hash map yet (visited)
                    -> create the copy_node
                - make edges between the copy of current node and copy of neighbor node
                    copy_cur.neighbors.append(copy_nei)
                    copy_nei.neighbors.append(copy_cur)
        return original_to_copy(node)

'''

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        og_to_cp = {}

        q = deque()

        q.append(node)
        seen = set()
        og_to_cp[node] = Node(node.val, [])

        while q:
            for i in range(len(q)):
                cur = q.popleft()
                copy_cur = og_to_cp[cur]

                for nei in cur.neighbors:
                    if nei not in og_to_cp:
                        og_to_cp[nei] = Node(nei.val, [])
                        q.append(nei)
                    if (cur, nei) not in seen:
                        copy_nei = og_to_cp[nei]
                        copy_cur.neighbors.append(copy_nei)
                        copy_nei.neighbors.append(copy_cur)
                        seen.add((cur, nei))
                        seen.add((nei, cur))

        return og_to_cp[node]