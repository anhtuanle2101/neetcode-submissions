# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
    - return kth smallest value (1-indexed)
    - BST at each node
        - all nodes in left subtree < node.val -> upper bound
        - all nodes in right subtree > node.val -> lower bound
        - dfs traverse throught the BST (in-order) for k times and return the value
'''

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.result = root.val
        self.count = 0

        self.dfs_traverse(root, k)

        return self.result
        
    def dfs_traverse(self, node, k):
        if not node:
            return 

        self.dfs_traverse(node.left, k)
        self.count += 1
        if self.count == k:
            self.result = node.val
            return
        self.dfs_traverse(node.right, k)