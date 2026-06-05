# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''


'''


class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        return self.is_sub_tree_of(subRoot, root)
        
    def is_sub_tree_of(self, subRoot, node):
        if not node and not subRoot:
            return True
        
        if self.is_same_as(node, subRoot):
            return True
        left, right = False, False
        if node.left:
            left = self.is_sub_tree_of(subRoot, node.left)
        if node.right:
            right = self.is_sub_tree_of(subRoot, node.right)
        
        return left or right

    def is_same_as(self, node1, node2):
        if not node1 and not node2:
            return True
        
        if node1 and node2 and node1.val == node2.val:
            return self.is_same_as(node1.left, node2.left) and self.is_same_as(node1.right, node2.right)
        
        return False