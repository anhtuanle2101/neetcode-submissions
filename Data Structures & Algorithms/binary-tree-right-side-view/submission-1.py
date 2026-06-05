# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
    - at each level (ith steps from root) return the right most node
    - if there is no nodes in the right side of the root but there are nodes in the left side -> still returns the right most node in the left 
    subtree
        - BFS -> get list of all the nodes at each level and add the last node to the result TC O(n) and TS O(n)
            - double ended queue q = deque()
            - start from root, q.append(root)
            - until the q exhaust
                - loop through the snapshot or current nodes of q (since we are adding nodes along but not account those in)
                    - at each node, take the node out of q, check if the snapshot of q is exhausted (check if this is the right most node for this level)
                        -> if yes, append to result
                    - check its children if they are not None, append them to back to the queue
'''

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        q = deque()
        q.append(root)

        while q:
            count = len(q)
            for i in range(len(q)):
                node = q.popleft()
                count -= 1
                if not count:
                    res.append(node.val)
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return res
        