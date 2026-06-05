# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        root = None
        root = self.dfs(root, preorder, inorder)
        return root
    def dfs(self, root, preord, inord):
        if not preord or not inord:
            return None
        cur = preord[0]
        
        root = TreeNode(cur)
        index = inord.index(cur)
        root.left = self.dfs(root.left, preord[1:index+1], inord[:index])
        root.right = self.dfs(root.right, preord[index+1:], inord[index+1:])

        return root