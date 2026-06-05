# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.dfs(root, -100, 0)[1]
    def dfs(self, root, max, count):
        if not root:
            return [max, 0]
        addition = 0
        if root.val >= max:
            addition = 1
            max = root.val
        
        return [max, addition + self.dfs(root.left, max, count)[1] + self.dfs(root.right, max, count)[1]]
