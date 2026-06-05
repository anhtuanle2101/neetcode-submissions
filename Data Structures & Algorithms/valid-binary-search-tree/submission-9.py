# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
    output: boolean if tree is a valid BST

    - valid BST constraints
        - at node ith
            - nodes in left subtree < node.val -> node.val is max(all nodes in left subtree) upper bound
            - nodes in right subtree > node.val -> node.val is min(all nodes in right subtree) lower bound
            - both left and right subtree is BST
        - None nodes -> valid BST -> nodes with no children -> valid BST as well

'''


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.is_bst(root, float("-inf"), float("inf"))
    
    def is_bst(self, node, lower, upper):
        if not node:
            return True

        if not (lower < node.val < upper):
            return False

        return self.is_bst(node.left, lower, node.val) and self.is_bst(node.right, node.val, upper)
    
        
