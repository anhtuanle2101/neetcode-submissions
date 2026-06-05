# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
    
'''

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.invert_child_of_node(root)

        return root
        
    def invert_child_of_node(self, node):
        if not node:
            return

        node.left, node.right = node.right, node.left

        if node.left:
            self.invert_child_of_node(node.left)
        if node.right:
            self.invert_child_of_node(node.right)