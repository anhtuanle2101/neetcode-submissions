# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.result = True

    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        balance, h = self.dfs(root)

        return self.result
    def dfs(self, root):
        if not root:
            return [True, -1]
        
        l, r = self.dfs(root.left)[1], self.dfs(root.right)[1]

        h = 1 + max(l, r)
        
        if abs(r - l) > 1:
            self.result = False
        
        return [abs(r - l) <= 1, h]

        