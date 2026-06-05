# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''

'''


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.is_same_as(p, q)
    def is_same_as(self, node1, node2):
        if not node1 and not node2:
            return True

        if node1 and node2 and node1.val == node2.val:
            return self.is_same_as(node1.left, node2.left) and self.is_same_as(node1.right, node2.right)

        return False