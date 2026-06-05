# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.max = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # recursively at each node,
        # we calculate the height bottom-up and the diameter
        # at that node, while calculate the diameter keep track
        # of the max diameter
        # at each node if the node is None, the height will be -1 and
        # diameter will be 0, otherwise, the height will be 1 + max(left_h, right_h)
        # and the diameter will be 2 + left_h + right_h
        self.dfs(root)

        return self.max

    def dfs(self, root):
        if not root:
            return [0, -1]

        left_height = self.dfs(root.left)[1]
        right_height = self.dfs(root.right)[1]

        cur_height = 1 + max(left_height, right_height)
        cur_diameter = 2 + left_height + right_height

        if cur_diameter > self.max:
            self.max = cur_diameter
    
        return [cur_diameter, cur_height]
    
