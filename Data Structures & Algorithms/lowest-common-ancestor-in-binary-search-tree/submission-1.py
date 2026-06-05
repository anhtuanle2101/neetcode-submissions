# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
    - binary search tree
        - a.left.val < a.val < a.right.val

    - ancester(a) = a

    - lowest common ancester is the min val node where p and q are decendants of 
        - provided p and q
            - traverse beginning from the root (root is the common ancester of all the nodes in the tree)
                - if p.val and q.val both > root.val -> look in root.right subtree
                - else if p.val and q.val both < root.val -> look in root.left subtree
                - if root.val equals to either p.val or q.val -> p or q being the LCA
                - if p.val < root.val < q.val or q.val < root.val < p.val -> root being the LCA

'''


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        return self.LCA(root, p, q)

    def LCA(self, node, p, q):
        if not node:
            return None

        if p.val > node.val and q.val > node.val:
            return self.LCA(node.right, p, q)
        elif p.val < node.val and q.val < node.val:
            return self.LCA(node.left, p, q)
        elif p.val == node.val:
            return p
        elif q.val == node.val:
            return q
        else:
            return node