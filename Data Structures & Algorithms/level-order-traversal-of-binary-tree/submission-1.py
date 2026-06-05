# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
    - level returns 
        - list of nodes on the same level (steps from root) -> BFS
            - double ended queue -> q = deque()
            - starting from root q.append(root)
            - until the q exhausted, 
                - loop through all the nodes in current level (starting 0)
                    - at each node, add the node to this level list
                    - append the child nodes of each node back to the queue
                - add the level list to the result 
'''


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        result = []
        q = deque()
        q.append(root)

        while q:
            level = []
            for i in range(len(q)):
                node = q.popleft()

                level.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            result.append(level)
        
        return result