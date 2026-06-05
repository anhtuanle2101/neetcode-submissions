# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # at each node to ensure the property of the path
        # there can be at most one split at a node
        # to create a valid path, 
        # so recursively at each node, calculate 
        # the max sum the node without split and with split
        # update the max sum accordingly, then return
        # the sum with split so that it can be used
        # to calculate ancestors' sums.

        self.max = root.val

        self.dfs(root)

        return self.max

    # return the max sum without split
    def dfs(self, root):
        if not root:
            return 0
        
        max_left = max(self.dfs(root.left), 0)
        max_right = max(self.dfs(root.right), 0)

        # sum with split at this node
        sum_split = root.val + max_left + max_right
        
        self.max = max(self.max, sum_split)

        return root.val + max(max_left, max_right)
