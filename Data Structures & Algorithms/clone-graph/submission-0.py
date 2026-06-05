"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        self.hash_map = {}

        return self.dfs(node)

    def dfs(self, node):
        if not node:
            return None
        
        if node in self.hash_map:
            return self.hash_map[node]
        
        copy_node = Node(node.val)
        self.hash_map[node] = copy_node

        for n in node.neighbors:
            copy_node.neighbors.append(self.dfs(n))

        return copy_node