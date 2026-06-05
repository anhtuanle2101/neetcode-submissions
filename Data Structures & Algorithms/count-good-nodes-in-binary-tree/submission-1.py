# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
    node is good if path from root to node contain no nodes is greater than node.val
    - node.val >= all nodes in path from root to node => node.val = max(nodes from root to node)
    - at each node, check if node.val to the max value from root to nodes
        - if yes, increase res by 1
        - then, update the max value with node.val
'''

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0

        self.count_good_nodes(root, root.val)

        return self.res
    
    def count_good_nodes(self, node, max_val):
        if not node:
            return 
        
        if node.val >= max_val:
            self.res += 1
        
        max_val = max(max_val, node.val)

        if node.left:
            self.count_good_nodes(node.left, max_val)
        if node.right:
            self.count_good_nodes(node.right, max_val)
    