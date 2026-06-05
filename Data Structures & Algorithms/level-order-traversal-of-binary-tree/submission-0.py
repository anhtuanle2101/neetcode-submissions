# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # BFS 
        # make use of a double ended queue 
        # add root to the queue
        # iterate until the queue has no nodes left
        # at each level loop through every element in current 
        # state of queue, pop the node out at each time, 
        # append to a current_level_nodes arr, and 
        # add back to the queue any children the current node has
        # after the inner loop, append the current_level_nodes arr to the
        # result arr
        q = deque()
        q.append(root)
        result = []
        while q:
            cur_level_nodes = []
            for i in range(len(q)):
                cur_node = q.popleft()
                if not cur_node:
                    break
                else:
                    cur_level_nodes.append(cur_node.val)

                if cur_node.left:
                    q.append(cur_node.left)
                if cur_node.right:
                    q.append(cur_node.right)
            if not cur_level_nodes:
                break
            result.append(cur_level_nodes)
        
        return result