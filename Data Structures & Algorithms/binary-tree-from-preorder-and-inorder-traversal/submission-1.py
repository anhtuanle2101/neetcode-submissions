# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
    - starting with preorder = [a,b,c] inorder = [b,a,c]  
    preorder ints[] a, b, c in preorder 
        -> a is direct ancester of b and c -> create node with value of a
    inorder ints[] b, a, c in inorder 
        - after determine the highest ancestor due to preorder list
            -> b portion will be the left subtree a.left = build_nodes(preorder(b), inorder(b))
            -> c portion will be the right subtree a.right = build_nodes(preorder(b), inorder(c))
    return back the created node at the end

'''


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        return self.build_nodes(preorder, inorder)

    def build_nodes(self,preorder, inorder):
        if not preorder:
            return None

        node = TreeNode(preorder[0])
        index = inorder.index(preorder[0])
        # left portion
        left_pre = preorder[1:1+index]
        left_in = inorder[:index]
        node.left = self.build_nodes(left_pre, left_in)

        # right portion
        right_pre = preorder[index+1:]
        right_in = inorder[index+1:]
        node.right = self.build_nodes(right_pre, right_in)

        return node