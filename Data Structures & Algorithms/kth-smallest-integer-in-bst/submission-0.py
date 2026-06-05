# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.result = None
        self.m = {}
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.dfs(root)

        return self.m[k]
    def dfs(self, root):
        if not root:
            return 0

        left = self.dfs(root.left)
        self.m[len(self.m) + 1] = root.val
        right = self.dfs(root.right)

        return len(self.m) + 1


        


