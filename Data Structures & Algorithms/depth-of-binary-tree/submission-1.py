# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
    return depth of binary tree

    depth of binary tree is max(node_nums) from root 
    - depth = max(depth_left, depth_right) + 1
    - depth of None = 0
'''

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        return self.depth_sub_tree_start_from(root)
        
    def depth_sub_tree_start_from(self, node):
        if not node:
            return 0
        
        depth = max(self.depth_sub_tree_start_from(node.left), self.depth_sub_tree_start_from(node.right)) + 1

        return depth