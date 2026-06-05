# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_depth = self.dfs(root, 0)

        return max_depth
        
    def dfs(self, root, depth):
        if not root:
            return depth

        depth += 1
        
        return max(self.dfs(root.left, depth), self.dfs(root.right, depth))
