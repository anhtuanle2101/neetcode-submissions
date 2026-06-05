# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # BFS

        q = deque()
        q.append(root)

        result = []

        while q:
            same_level_nodes = []
            for i in range(len(q)):
                cur_node = q.popleft()

                if not cur_node:
                    break
                else:
                    same_level_nodes.append(cur_node.val)
                
                if cur_node.left:
                    q.append(cur_node.left)
                if cur_node.right:
                    q.append(cur_node.right)
            if not same_level_nodes:
                break
            result.append(same_level_nodes[-1])
        
        return result