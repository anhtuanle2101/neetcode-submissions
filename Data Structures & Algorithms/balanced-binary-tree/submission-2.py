# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
    A height-balanced binary tree is defined as a binary tree in which 
    the left and right subtrees of every node differ in height by no more than 1.
    - at each node
        - Condition: height(left) - height(right) <= 1
        - height(leaf) = 1, height(None) = 0
    
'''

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.res = True

        self.calculate_height_from( root)

        return self.res
        
    
    def calculate_height_from(self, node):
        if not node:
            return 0

        left = self.calculate_height_from(node.left)
        right = self.calculate_height_from(node.right)

        if abs(left - right) > 1:
            self.res = False

        return max(left, right) + 1