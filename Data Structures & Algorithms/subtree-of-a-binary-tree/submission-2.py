# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        return self.dfs(root, subRoot)
    def is_same_tree(self, root1, root2):
        if not root1 and not root2:
            return True

        if root1 and root2 and root1.val == root2.val:
            return self.is_same_tree(root1.left, root2.left) and self.is_same_tree(root1.right, root2.right)
        
        return False
    def dfs(self, root, sub_root):
        if not sub_root:
            return True
        
        if not root:
            return False

        if self.is_same_tree(root, sub_root):
            return True
        
        return self.dfs(root.left, sub_root) or self.dfs(root.right, sub_root)