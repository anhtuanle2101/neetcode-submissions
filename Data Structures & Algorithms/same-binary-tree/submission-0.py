# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.dfs(p, q)
        
    def dfs(self, root1, root2):
        if not root1 and not root2:
            return True
        
        if (root1 and not root2) or (not root1 and root2):
            return False
        
        return root1.val == root2.val and self.dfs(root1.left, root2.left) and self.dfs(root1.right, root2.right)