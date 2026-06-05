# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
    The diameter of a binary tree is defined as the length of the longest path between any two nodes within the tree
    - not neccesasry going through the root
    - to calculate the length of a path between two nodes, use height as a tool to accomplish this
        - height(leaf nodes) = 0
        - height(node) = max(max_height_left, max_height_right) + 1
        - at each node, calculate the max_res = max(max_res, max_height_left + max_height_right + 2)


    The length of a path between two nodes in a binary tree is the number of edges between the nodes.
'''

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        self.calculate_height_from(root)

        return self.res

    def calculate_height_from(self, node):
        if not node:
            return 0
        if not node.left and not node.right:
            return 1

        max_height_left = self.calculate_height_from(node.left)
        max_height_right = self.calculate_height_from(node.right)

        self.res = max(self.res, max_height_left + max_height_right)

        return max(max_height_left, max_height_right) + 1